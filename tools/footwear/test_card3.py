#!/usr/bin/env python3
"""Card 3 click through (both modes), numbers, layout, variety, timing, navigation and phone checks.
Run: python3 tools/footwear/test_card3.py. Money to two decimals."""
import os, sys
from decimal import Decimal as D
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from footwear_tests import run_all, js

# ---- the brief's numbers, derived independently of the card ----
assert D('3.4') * D('4.20') == D('14.28')
LINES = {'upr': D('14.28'), 'out': D('6.10'), 'box': D('0.85'), 'ins': D('1.20'), 'lac': D('0.35'), 'fee': D('9.50')}
YOU0, FAC0 = {'upr', 'out', 'box'}, {'ins', 'lac', 'fee'}
you0, fac0 = sum(LINES[k] for k in YOU0), sum(LINES[k] for k in FAC0)
assert (you0, fac0, you0 + fac0, 180 * fac0) == (D('21.23'), D('11.05'), D('32.28'), D('1989.00'))
you1, fac1 = you0 + LINES['ins'], fac0 - LINES['ins']
assert (you1, fac1, 180 * fac1, you1 + fac1) == (D('22.43'), D('9.85'), D('1773.00'), D('32.28'))
assert 180 * LINES['fee'] + 180 * LINES['lac'] == D('1773.00')
assert 180 - 72 == 108 and 72 * D('32.28') == D('2324.16')


def ids(pg, *names):
    return js(pg, "return %r.map(function(i){var e=r.getElementById(i);return e?e.textContent:null}).join('|')" % list(names))


def start(pg, f):
    f.check(js(pg, "return r.querySelector('.fwin').getAttribute('data-scr')") == 'Outsourced orders', 'start: the outsourced order list')
    t = js(pg, "return r.getElementById('pg').innerText")
    f.check(not any(x in t for x in ('21.23', '11.05', '32.28', '1,989', 'Insole', 'Factory fee')), 'start: no materials or cost before the order is opened')


def split(pg, f):
    f.check(ids(pg, 't-you', 't-fac', 'per', 'po') == '21.23|11.05|32.28|$1,989.00', 'step 2: 21.23 you, 11.05 factory, 32.28 a pair, PO $1,989.00')


def moved(pg, f):
    f.check(ids(pg, 't-you', 't-fac', 'per', 'po') == '22.43|9.85|32.28|$1,773.00', 'step 3: 22.43 you, 9.85 factory, still 32.28, PO $1,773.00')


def po(pg, f):
    f.check(ids(pg, 'pot') == '$1,773.00', 'step 4: the factory PO totals $1,773.00')


def rcv(pg, f):
    f.check(js(pg, "return r.getElementById('ir').value") == '72', 'step 5: 72 pairs prefilled')
    js(pg, "var e=r.getElementById('ir');e.value='400';e.dispatchEvent(new Event('input',{bubbles:true}))")
    pg.locator('#cv .hint').first.click(); pg.wait_for_timeout(400)
    f.check(js(pg, "return r.getElementById('fr').classList.contains('err')"), 'step 5: more pairs than the order shows an inline error')
    js(pg, "var e=r.getElementById('ir');e.value='72';e.dispatchEvent(new Event('input',{bubbles:true}))")


def end(pg, f):
    f.check(ids(pg, 'got', 'open', 'val', 'prog') == '72|108|$2,324.16|72 of 180', 'step 5: 72 received, 108 open, $2,324.16 semi finished, Northgate 72 of 180')


PLAN = [('Split a build by who supplies what', '$1,989.00'),
        ('Move a line and both columns update', '$1,773.00'),
        ('Sutton raises the factory purchase order on its own', '$1,773.00'),
        ('Receive pairs back from the factory', 'Receive 72 pairs'),
        ('Progress per factory and the stock value', '$2,324.16')]

f = run_all(3, PLAN, ['$2,324.16', '108'], extra={'before': {1: split, 2: moved, 3: po, 4: rcv}, 'after': end}, start=start)
print('\n%d failures' % len(f)); sys.exit(1 if f else 0)
