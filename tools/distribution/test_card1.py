#!/usr/bin/env python3
"""Card 1 click through (both modes), numbers, layout and text checks. Run: python3 tools/distribution/test_card1.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from distribution_tests import run_card, js

IT = {'GL-210': (220, 150, 100), 'TW-330': (340, 110, 120), 'BT-118': (60, 20, 80), 'LB-502': (900, 300, 250), 'PK-077': (48, 30, 40)}
avail = {k: v[0] - v[1] for k, v in IT.items()}
assert avail == {'GL-210': 70, 'TW-330': 230, 'BT-118': 40, 'LB-502': 600, 'PK-077': 18}
low = [k for k in IT if avail[k] < IT[k][2]]
assert low == ['GL-210', 'BT-118', 'PK-077'] and len(low) == 3
assert 120 + 60 + 40 == 220 and 220 - 150 == 70
atl, dal = 120 + 60 + 30, 40 - 30
assert (atl, dal) == (210, 10) and atl + dal == 220
assert 220 + 120 == 340 and 340 - 150 == 190 and 190 >= 100
assert 160 + 80 - 40 == 200 and 90 + 40 - 18 == 112


def start(pg, f):
    f.check(js(pg, "return r.getElementById('isk').value") == 'GL-210', 'start: SKU prefilled')
    f.check(js(pg, "return r.getElementById('ixq').value+'|'+r.getElementById('isq').value") == '30|120', 'start: transfer and delivery prefilled')
    f.check('No item open' in js(pg, "return r.getElementById('itm').innerText"), 'start: item panel empty until Find')
    f.check(js(pg, "return r.querySelectorAll('.bin.lit').length") == 0, 'start: no bins lit before Find')
    js(pg, "r.getElementById('isk').value='GL-999'")
    pg.locator('#cv .hint').first.click(); pg.wait_for_timeout(400)
    f.check(js(pg, "return r.getElementById('fsk').classList.contains('err')"), 'step 1: an unknown SKU shows an inline error')
    js(pg, "r.getElementById('isk').value='GL-210'")


def lit(pg, f):
    f.check(js(pg, "return [].map.call(r.querySelectorAll('.bin.lit b'),function(b){return b.textContent}).join(',')") == '120,60,40', 'step 1: three bins lit with 120, 60 and 40')


def xfer(pg, f):
    js(pg, "var e=r.getElementById('ixq');e.value='55';e.dispatchEvent(new Event('input',{bubbles:true}))")
    pg.locator('#cv .hint').first.click(); pg.wait_for_timeout(400)
    f.check(js(pg, "return r.getElementById('fxe').classList.contains('err')"), 'step 4: transferring more than Dallas holds shows an inline error')
    js(pg, "var e=r.getElementById('ixq');e.value='30';e.dispatchEvent(new Event('input',{bubbles:true}))")
    f.check(js(pg, "return r.getElementById('aoh').textContent") == '220', 'step 4: on hand 220 before the transfer')


def after_x(pg, f):
    f.check(js(pg, "return r.getElementById('q-Atlanta').textContent+'|'+r.getElementById('q-Dallas').textContent") == '210|10', 'step 4: Atlanta 210 and Dallas 10')
    f.check(js(pg, "return r.getElementById('aoh').textContent") == '220', 'step 4: on hand stays 220 after the transfer')


def before_scan(pg, f):
    after_x(pg, f)


def before_plan(pg, f):
    f.check(js(pg, "return r.getElementById('aoh').textContent+'|'+r.getElementById('aav').textContent") == '340|190', 'step 5: on hand 340, available 190')
    f.check('Above reorder point' in js(pg, "return r.getElementById('aflag').textContent"), 'step 5: low stock flag cleared')
    f.check(js(pg, "return r.querySelector('#flow b').textContent") == '2', 'step 5: low stock count drops to 2')


PLAN = [('Find any SKU and see every bin that holds it', '220'),
        ('Available to sell is what is on the shelf minus', '70'),
        ('Three of five items are under their reorder point', '18 / 40'),
        ('Move stock to where the orders are', 'TO-0931'),
        ('A scan updates the bin, the count and the low stock flag', '190'),
        ('The plan suggests what to buy', '112')]


def end(pg, f):
    f.check(js(pg, "return r.getElementById('buy-BT-118').textContent+'|'+r.getElementById('buy-PK-077').textContent") == '200|112', 'step 6: buys BT-118 200 and PK-077 112')
    f.check(js(pg, "return !r.getElementById('buy-GL-210')"), 'step 6: GL-210 needs no buy after the delivery')


f = run_card(1, PLAN, ['200', '112', 'TO-0931', 'PO-4402 received'], extra={'before': {0: start, 1: lit, 3: xfer, 4: before_scan, 5: before_plan}, 'after': end})
print('\n%d failures' % len(f)); sys.exit(1 if f else 0)
