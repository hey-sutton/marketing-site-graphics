#!/usr/bin/env python3
"""Card 2 click through (both modes), numbers, layout, variety, timing, navigation and phone checks.
Run: python3 tools/distilleries/test_card2.py. The brief's sums are asserted in numbers_check.py first."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numbers_check  # noqa: F401  (asserts 511.0, 110 and 3.4%)
from distilleries_tests import run_all, js, testlib


def start(pg, f):
    f.check(js(pg, "return r.querySelector('.fwin').getAttribute('data-scr')") == 'Rickhouse', 'start: Rickhouse B')
    f.check(js(pg, "return r.querySelectorAll('.rc').length") == 6 and '290' in testlib.win_text(pg), 'start: six rows and every barrel in place')
    f.check(js(pg, "return r.querySelectorAll('.pn,.bc2.sel,.bc2.cur').length") == 0, 'start: no barrel selected and no record open')


def row(pg, f):
    f.check(js(pg, "return r.querySelectorAll('.bc2').length") == 50, 'step 1: row 4 shows 5 levels by 10 positions')
    f.check(js(pg, "return r.getElementById('lot').textContent") == '120', 'step 1: lot DS-0412 holds 120 barrels')


def record(pg, f):
    t = testlib.win_text(pg)
    f.check(all(x in t for x in ('Mar 14, 2022', '4 yr 8 mo', '53.0 L', '51.2 L', 'DS-0412')), 'step 2: fill date, age, source batch, fill and gauge')


def sel(pg, f):
    f.check(js(pg, "return r.querySelectorAll('.bc2.sel').length") == 10, 'step 4: ten barrels selected')
    f.check(js(pg, "return r.getElementById('s-tot').textContent") == '511.0 L', 'step 4: gauges total 511.0 L')
    f.check(js(pg, "return [].map.call(r.querySelectorAll('.gz b'),function(e){return e.textContent}).join(',')") == '51.2,51.0,50.8,51.4,51.1,50.9,51.3,51.0,51.2,51.1', 'step 4: the ten gauges from the brief')


def end(pg, f):
    f.check(js(pg, "return r.getElementById('d-lot').textContent+'|'+r.getElementById('lot').textContent") == '110|110', 'step 5: lot DS-0412 drops from 120 to 110')
    f.check(js(pg, "return r.querySelectorAll('.bc2.dmp').length") == 10, 'step 5: level 3 shows ten empty slots')
    f.check(js(pg, "return r.getElementById('tk').textContent") == '511.0 L of 2,000.0 L', 'step 5: BT-2 holds 511.0 L')


PLAN = [('Row 4 opens barrel by barrel', 'Level 3'), ('The barrel record opens', '51.2 L'),
        ('Gauge against fill shows the loss', '1.8 L, 3.4%'), ('Ten barrels selected for the dump', '511.0 L'),
        ('The dump posts and the lot count updates', '120 to 110')]
f = run_all(2, PLAN, ['110', '511.0 L'], extra={'before': {0: start, 1: row, 2: record, 4: sel}, 'after': end}, start=start)
print('\n%d failures' % len(f)); sys.exit(1 if f else 0)
