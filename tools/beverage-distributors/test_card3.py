#!/usr/bin/env python3
"""Card 3 click through (both modes), numbers, layout, variety, timing, navigation and phone checks.
Run: python3 tools/beverage-distributors/test_card3.py. The brief's sums are asserted in numbers_check.py first."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numbers_check  # noqa: F401  (asserts 960 = 40 x 24, 780 over five accounts and 780 + 180 = 960)
from bd_tests import run_all, js, testlib, readonly_checks


def ids(pg, *k):
    return js(pg, "return %r.map(function(i){var e=r.getElementById(i);return e?e.textContent:null}).join('|')" % list(k))


def start(pg, f):
    readonly_checks(pg, f, {'il': 'BRW-4471'})
    f.check(js(pg, "return r.querySelector('.fwin').getAttribute('data-scr')") == 'Lot search', 'start: the lot field and an empty prompt')
    t = js(pg, "return r.getElementById('pg').innerText")
    f.check(not any(x in t for x in ('960', '780', '180', 'C-04', 'Dockside')), 'start: nothing derived from the lot shows')


def trace(pg, f):
    f.check(ids(pg, 'f-rc', 'f-sh', 'f-oh') == '960|780|180', 'step 1: 960 received, 780 shipped, 180 on hand')
    t = testlib.win_text(pg)
    f.check('40 pallets of 24' in t and 'C-04' in t, 'step 1: 40 pallets of 24, cooler bin C-04')


def accts(pg, f):
    f.check(ids(pg, 'ac-0', 'ac-1', 'ac-2', 'ac-3', 'ac-4', 'ac-t') == '120|240|60|300|60|780', 'step 2: 120 + 240 + 60 + 300 + 60 = 780')
    t = testlib.win_text(pg)
    f.check(all(x in t for x in ('Nov 6', 'Nov 7', 'Nov 9', 'Nov 10', 'Nov 12')), 'step 2: every delivery date is in November')


def hold(pg, f):
    f.check(ids(pg, 'h-st') == 'On hold, H-0311', 'step 3: hold placed on the 180 cases')


def end(pg, f):
    f.check(js(pg, "return !!r.getElementById('dld')") and 'recall-BRW-4471.csv' in testlib.win_text(pg), 'step 4: the account list is downloaded')


PLAN = [('The whole lot on one screen', '960'), ('Every account, with dates and cases', 'Elm Street Liquor'),
        ('The stock still on hand is held', 'H-0311'), ('The account list, ready to send', 'recall-BRW-4471.csv')]
f = run_all(3, PLAN, ['780', 'H-0311'], extra={'before': {0: start, 1: trace, 2: accts, 3: hold}, 'after': end}, start=start)
print('\n%d failures' % len(f)); sys.exit(1 if f else 0)
