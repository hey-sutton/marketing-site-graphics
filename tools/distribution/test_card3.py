#!/usr/bin/env python3
"""Card 3 click through (both modes), numbers, layout and text checks. Run: python3 tools/distribution/test_card3.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from distribution_tests import run_card, js

assert round(200 * 4.10, 2) == 820.00 and round(112 * 6.25, 2) == 700.00 and 820.00 > 500.00
assert 200 - 120 == 80 and 60 + 120 == 180          # card 1: BT-118 on hand 60
add = round((96.00 + 24.00) / 120, 2)
assert add == 1.00 and round(4.10 + add, 2) == 5.10 and round(120 * 5.10, 2) == 612.00


def start(pg, f):
    f.check('No suggestions loaded' in js(pg, "return r.getElementById('sug').innerText"), 'start: suggestions empty until loaded')
    f.check('No purchase order yet' in js(pg, "return r.getElementById('po').innerText"), 'start: no purchase order')
    f.check(js(pg, "return r.getElementById('if').value+'|'+r.getElementById('id').value") == '96.00|24.00', 'start: freight and duty prefilled')
    f.check(js(pg, "return !!r.getElementById('lce')"), 'start: landed cost empty until its step')


def form(pg, f):
    f.check(js(pg, "return [r.getElementById('iq').value,r.getElementById('ip').value,r.getElementById('iw').value].join('|')") == '200|4.10|Atlanta', 'step 2: quantity, price and ship to prefilled')
    f.check('820' not in js(pg, "return r.getElementById('sug').innerText+r.getElementById('po').innerText"), 'step 2: no total before the PO exists')
    js(pg, "var e=r.getElementById('iw');e.value='Paris';e.dispatchEvent(new Event('input',{bubbles:true}))")
    pg.locator('#cv .hint').first.click(); pg.wait_for_timeout(400)
    f.check(js(pg, "return r.getElementById('fw').classList.contains('err')"), 'step 2: an unknown ship to shows an inline error')
    js(pg, "var e=r.getElementById('iw');e.value='Atlanta';e.dispatchEvent(new Event('input',{bubbles:true}))")


def recv(pg, f):
    js(pg, "var e=r.getElementById('ir');e.value='250';e.dispatchEvent(new Event('input',{bubbles:true}))")
    pg.locator('#cv .hint').first.click(); pg.wait_for_timeout(400)
    f.check(js(pg, "return r.getElementById('fr').classList.contains('err')"), 'step 5: receiving more than ordered shows an inline error')
    js(pg, "var e=r.getElementById('ir');e.value='120';e.dispatchEvent(new Event('input',{bubbles:true}))")


def before_lc(pg, f):
    f.check(js(pg, "return r.getElementById('rcv').textContent+'|'+r.getElementById('open').textContent") == '120 of 200|80 still on order', 'step 5: 120 of 200, 80 on order')
    f.check('60 to 180' in js(pg, "return r.getElementById('stk').textContent"), 'step 5: BT-118 stock 60 to 180')
    f.check(js(pg, "return !!r.getElementById('lce')"), 'step 5: landed cost still empty before its step')


def end(pg, f):
    f.check(js(pg, "return [r.getElementById('add').textContent,r.getElementById('lcu').textContent,r.getElementById('lcv').textContent,r.getElementById('pot').textContent].join('|')") == '1.00|5.10|612.00|820.00', 'step 6: 1.00 a unit, landed 5.10, 612.00, order still 820.00')


PLAN = [('Reorder suggestions arrive grouped by vendor', '112 rolls'),
        ('The suggestion becomes a purchase order', '820.00'),
        ('Approval rules send larger orders', 'Awaiting approval'),
        ('Approved and on its way to the vendor', 'Sent to vendor'),
        ('A partial delivery is received line by line', '80 still on order'),
        ('Freight and duties are spread across what arrived', '612.00')]

f = run_card(3, PLAN, ['5.10', '612.00', '820.00', '120 of 200'], extra={'before': {0: start, 1: form, 4: recv, 5: before_lc}, 'after': end})
print('\n%d failures' % len(f)); sys.exit(1 if f else 0)
