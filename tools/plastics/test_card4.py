#!/usr/bin/env python3
"""Card 4 click through (both modes), numbers, layout and text checks. Run: python3 tools/plastics/test_card4.py
Rounding: whole pounds, money to cents."""
import os, sys
from decimal import Decimal as D
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from plastics_tests import run_card, js

M = '−'
assert 11000 + 0 - 24500 == -13500 and 150 + 0 - 340 == -190 and 40 - 38 == 2 and 600 - 480 == 120
assert 1100 + 9200 + 8400 + 5800 == 24500 and 1100 + 9200 == 10300 < 11000 and 10300 + 8400 == 18700 > 11000
assert 14000 * D('0.74') == D('10360.00') and 11000 + 0 + 14000 - 24500 == 500
assert 11000 + 6000 == 17000 and 14000 - 6000 == 8000 and 17000 + 8000 - 24500 == 500


def start(pg, f):
    f.check(js(pg, "return r.querySelectorAll('.pln button.row').length") == 4, 'start: grid shows all four materials')
    f.check(js(pg, "return !!r.getElementById('dh')&&!r.getElementById('first')"), 'start: demand by run hidden until an item is opened')
    f.check('No order yet' in js(pg, "return r.getElementById('po').innerText"), 'start: no purchase order')


def short(pg, f):
    f.check(js(pg, "return [].map.call(r.querySelectorAll('.pln button.row'),function(e){return e.id}).join(',')") == 'r-PP-100,r-COL-BLK', 'step 1: two rows remain')
    f.check(js(pg, "return r.getElementById('nt-PP-100').textContent+'|'+r.getElementById('nt-COL-BLK').textContent") == M + '13,500|' + M + '190', 'step 1: short 13,500 and 190')


def sel(pg, f):
    f.check(js(pg, "return r.getElementById('cu-RUN-7722').textContent+'|'+r.getElementById('cu-RUN-7725').textContent+'|'+r.getElementById('cu-RUN-7731').textContent") == '10,300|18,700|24,500', 'step 2: running total 10,300, 18,700, 24,500')
    f.check(js(pg, "return r.getElementById('first').closest('.row').firstChild.textContent") == 'RUN-7725', 'step 2: RUN-7725 is the first run short')
    f.check(js(pg, "return [r.getElementById('isu').value,r.getElementById('iq').value,r.getElementById('ip').value].join('|')") == 'Northfield Polymers|14,000|0.74', 'step 3: supplier, quantity and price prefilled')
    f.check('10,360' not in js(pg, "return r.getElementById('po').innerText"), 'step 3: no total before the PO exists')
    js(pg, "var e=r.getElementById('iq');e.value='14,500';e.dispatchEvent(new Event('input',{bubbles:true}))")
    pg.locator('#cv .hint').first.click(); pg.wait_for_timeout(400)
    f.check(js(pg, "return r.getElementById('fq').classList.contains('err')"), 'step 3: a part gaylord shows an inline error')
    js(pg, "var e=r.getElementById('iq');e.value='14,000';e.dispatchEvent(new Event('input',{bubbles:true}))")


def sent(pg, f):
    f.check(js(pg, "return r.getElementById('oo-PP-100').textContent+'|'+r.getElementById('nt-PP-100').textContent") == '14,000|500', 'step 5: on order 14,000, net 500')
    f.check(js(pg, "return r.getElementById('igy').value+'|'+r.getElementById('ilt').value") == '6|L-55212', 'step 6: 6 gaylords and lot prefilled')


def end(pg, f):
    f.check(js(pg, "return ['oh-PP-100','oo-PP-100','nt-PP-100','nt-COL-BLK'].map(function(k){return r.getElementById(k).textContent}).join('|')") == '17,000|8,000|500|' + M + '190', 'step 6: on hand 17,000, on order 8,000, net 500, COL-BLK still short 190')
    f.check(js(pg, "return r.getElementById('pot').textContent") == '10,360.00', 'end: PO total stays 10,360.00')


PLAN = [('One filter shows every material that will stop a run', 'COL-BLK'),
        ('You see which runs are competing for the same resin', 'First run short'),
        ('The shortage becomes a purchase order', '10,360.00'),
        ('Approval rules send larger orders', 'Awaiting approval'),
        ('Approved and on its way', 'Sent to supplier'),
        ('A partial delivery is received gaylord by gaylord', '8,000 lb still on order')]

f = run_card(4, PLAN, ['17,000', '8,000', '10,360.00', 'L-55212'], extra={'before': {0: start, 1: short, 2: sel, 5: sent}, 'after': end})
print('\n%d failures' % len(f)); sys.exit(1 if f else 0)
