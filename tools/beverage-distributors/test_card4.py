#!/usr/bin/env python3
"""Card 4 click through (both modes), numbers, layout, variety, timing, navigation and phone checks.
Run: python3 tools/beverage-distributors/test_card4.py. The brief's sums are asserted in numbers_check.py first."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numbers_check  # noqa: F401  (asserts 980 + 380 + 330 = 1,690.00, 60.00 deposit, 1,750.00, boards 23 and 24)
from bd_tests import run_all, js, testlib, readonly_checks


def ids(pg, *k):
    return js(pg, "return %r.map(function(i){var e=r.getElementById(i);return e?e.textContent:null}).join('|')" % list(k))


def board(pg):
    return ids(pg, 'bd-0', 'bd-1', 'bd-2', 'bd-3')


def start(pg, f):
    readonly_checks(pg, f, {'ia': 'Pier 9 Bar'})
    f.check(board(pg) == '5|4|3|11', 'start: board baseline Open 5, Picked 4, Loaded 3, Delivered 11 (23)')
    f.check(js(pg, "return r.querySelectorAll('.ln4,.chp b,#pl').length") == 0 and '$' not in js(pg, "return r.getElementById('pg').innerText"), 'start: empty order form, no prices before the account is picked')


def acct(pg, f):
    t = testlib.win_text(pg)
    f.check(all(x in t for x in ('$24.50', '$19.00', '$165.00', 'Bar and restaurant prices')), 'step 1: the price list applies to the SKU chips')


def lines(pg, f):
    f.check(ids(pg, 'la-hl', 'la-cb', 'la-kg', 'la-dep') == '$980.00|$380.00|$330.00|$60.00', 'step 2: 980.00, 380.00, 330.00 and the deposit 60.00 on its own line')
    f.check(ids(pg, 'o-g', 'o-d', 'o-t') == '$1,690.00|$60.00|$1,750.00', 'step 2: goods 1,690.00 + deposit 60.00 = 1,750.00')
    f.check('760 available, covers 40' in ids(pg, 'sk-hl') and '780 available, covers 20' in ids(pg, 'sk-cb'), 'step 2: stock check 760 covers 40, 780 covers 20')


def made(pg, f):
    f.check(board(pg) == '6|4|3|11' and ids(pg, 'bd-t') == '24', 'step 3: order created, Open 6, 24 orders')


def end(pg, f):
    f.check(board(pg) == '5|4|3|12' and ids(pg, 'bd-t') == '24', 'step 4: delivered, Open 5, Picked 4, Loaded 3, Delivered 12 (24)')
    f.check(ids(pg, 'o-t') == '$1,750.00', 'step 4: order total $1,750.00')


PLAN = [('price list applies', 'Bar and restaurant prices'), ('Three lines, each with a stock check', '$1,750.00'),
        ('The order lands on the board', 'SO-5131'), ('Picked, loaded, delivered', 'Delivered')]
f = run_all(4, PLAN, ['$1,750.00', '12'], extra={'before': {0: start, 2: lines, 3: made}, 'after': end}, start=start)
print('\n%d failures' % len(f)); sys.exit(1 if f else 0)
