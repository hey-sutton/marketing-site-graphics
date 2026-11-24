#!/usr/bin/env python3
"""Card 1 click through (both modes), numbers, layout, variety, timing, navigation and phone checks.
Run: python3 tools/beverage-distributors/test_card1.py. The brief's sums are asserted in numbers_check.py first."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numbers_check  # noqa: F401  (asserts 300 split, 6.0 days, 250 short, 2,850.00 and the other rows)
from bd_tests import run_all, js, testlib, readonly_checks


def ids(pg, *k):
    return js(pg, "return %r.map(function(i){var e=r.getElementById(i);return e?e.textContent:null}).join('|')" % list(k))


def start(pg, f):
    readonly_checks(pg, f, {})
    f.check(js(pg, "return r.querySelector('.fwin').getAttribute('data-scr')") == 'Planning', 'start: the planning table')
    f.check(js(pg, "return r.querySelectorAll('.tl .tile b').length") == 0, 'start: the four tiles are empty until a SKU is picked')
    f.check(ids(pg, 'cv-0', 'cv-1', 'cv-2', 'cv-3') == '6.0|20.0|12.0|30.0', 'start: baseline coverage 6.0, 20.0, 12.0, 30.0 days')
    t = testlib.win_text(pg)
    f.check('250' not in t and 'short' not in t.lower() and '$' not in t, 'start: no shortage and no order before a SKU is picked')
    f.check(js(pg, "return r.querySelectorAll('.row.am').length") == 0, 'start: no amber row')


def tiles(pg, f):
    f.check(ids(pg, 't-st-v', 't-ex-v', 't-cm-v', 't-dc-v') == '300|150|700|6.0', 'step 1: tiles 300 in stock, 150 expected, 700 committed, 6.0 days')
    f.check('50 cases a day' in testlib.win_text(pg), 'step 1: 700 over 14 days is 50 cases a day')


def locs(pg, f):
    f.check(ids(pg, 'lc-0', 'lc-1', 'lc-2', 'lc-t') == '180|90|30|300', 'step 2: warehouse 180 + cooler 90 + 3PL 30 = 300')


def short(pg, f):
    f.check(ids(pg, 's-av') == '250 short' and ids(pg, 's-dc') == '6.0', 'step 3: 300 + 150 less 700 = 250 short, 6.0 days')
    f.check(js(pg, "return r.querySelectorAll('.row.am').length") == 1 and js(pg, "return r.getElementById('r-0').classList.contains('am')"), 'step 3: the Citrus Seltzer coverage bar turns amber')


def end(pg, f):
    f.check(ids(pg, 'o-q', 'o-t') == '250|$2,850.00', 'step 4: 250 cases at $11.40 = $2,850.00')


PLAN = [('Four numbers for the SKU you picked', '6.0'), ('Stock split by location', 'Cooler'),
        ('The row turns amber and the shortage shows', '250 short'), ('A supplier order for the gap', '$2,850.00')]
f = run_all(1, PLAN, ['$2,850.00', 'PO-2214'], extra={'before': {0: start, 1: tiles, 2: locs, 3: short}, 'after': end}, start=start)
print('\n%d failures' % len(f)); sys.exit(1 if f else 0)
