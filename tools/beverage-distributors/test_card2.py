#!/usr/bin/env python3
"""Card 2 click through (both modes), numbers, layout, variety, timing, navigation and phone checks.
Run: python3 tools/beverage-distributors/test_card2.py. The brief's sums are asserted in numbers_check.py first."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numbers_check  # noqa: F401  (asserts 28, 70, 112 days, 1,200 cases, the 180 + 320 pick and the move to B and C)
from bd_tests import run_all, js, testlib, readonly_checks


def ids(pg, *k):
    return js(pg, "return %r.map(function(i){var e=r.getElementById(i);return e?e.textContent:null}).join('|')" % list(k))


def start(pg, f):
    readonly_checks(pg, f, {})
    f.check(js(pg, "return r.querySelector('.fwin').getAttribute('data-scr')") == 'SKU list', 'start: the SKU list only')
    f.check(js(pg, "return r.querySelectorAll('.lr,.thr,.pl').length") == 0, 'start: no lots, bars, threshold or pick list')


def lots(pg, f):
    readonly_checks(pg, f, {'io': 'SO-5126, 500 cases'}, 'step 2')
    f.check(js(pg, "return r.querySelectorAll('.lr').length") == 3 and js(pg, "return r.querySelectorAll('.thr').length") == 1, 'step 1: three lot bars and a threshold line')
    t = testlib.win_text(pg)
    f.check(all(x in t for x in ('28 days', '70 days', '112 days', 'Dec 14', 'Jan 25', 'Mar 8', '30 day threshold')), 'step 1: days left 28, 70, 112 against the 30 day threshold')
    f.check(ids(pg, 'lq-0', 'lq-1', 'lq-2') == '180|420|600', 'step 1: 180 + 420 + 600 = 1,200 cases')


def pick(pg, f):
    f.check(ids(pg, 'pk-0', 'pk-1', 'pk-t') == '180|320|500', 'step 2: pick 180 from A, then 320 from B = 500')


def risk(pg, f):
    f.check(ids(pg, 'r-d', 'r-q') == '28|180', 'step 3: lot A 28 days left, 180 cases at risk')
    f.check(js(pg, "return r.getElementById('lot-0').classList.contains('risk')"), 'step 3: lot A is flagged')


def end(pg, f):
    f.check(ids(pg, 'lq-0', 'lq-1', 'lq-2', 'o-t') == '0|0|520|520', 'step 4: lot A drops to 0, cases left 520')
    f.check(ids(pg, 'pk-1', 'pk-2', 'pk-t') == '420|80|500', 'step 4: the pick moves to B and C, 420 + 80 = 500')


PLAN = [('Three lots, drawn as days left', '112 days'), ('The pick takes the oldest lots first', '320'),
        ('Lot A is flagged at risk', '180 cases at risk'), ('The near date lot finds a buyer', 'Dockside Taproom')]
f = run_all(2, PLAN, ['SO-5127', 'Dockside Taproom'], extra={'before': {0: start, 1: lots, 2: pick, 3: risk}, 'after': end}, start=start)
print('\n%d failures' % len(f)); sys.exit(1 if f else 0)
