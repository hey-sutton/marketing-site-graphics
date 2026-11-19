#!/usr/bin/env python3
"""Card 1 (record form with a side summary): the README's numbers in Python, then the click through.
Run: python3 tools/sauce-manufacturing/test_card1.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sm_tests import run_card, finish, js, ids, readonly_checks, keyboard_walk, clicks_only

LN = [('Soy sauce', 40, 9.0), ('Water', 300, 8.34), ('Brown sugar syrup', 90, 11.0), ('Rice vinegar', 50, 8.4), ('Garlic puree', 15, 9.2), ('Ginger puree', 5, 9.0)]
LB = [round(g * d, 2) for _, g, d in LN]
for (_, g, d), lb in zip(LN, LB):
    assert abs(g * d - lb) < 1e-9 or abs(round(g * d, 2) - lb) < 1e-9          # gallons times density equals pounds, every line
assert LB == [360, 2502, 990, 420, 138, 45]
assert sum(g for _, g, _ in LN) == 500                                          # scaled lines sum to the kettle total in gal
assert round(sum(LB), 2) == 4455                                                # and in lb
F = 4455 / 20
assert F == 222.75 and 4455 / 500 == 8.91                                       # scale factor, blend density
BASE = [round(x / F, 2) for x in LB]
assert BASE == [1.62, 11.23, 4.44, 1.89, 0.62, 0.20] and round(sum(BASE), 2) == 20.00   # the 20 lb test pot
assert 270 / 9.0 == 30                                                          # tote gallons = fill weight / density
assert 40 * 9.0 == 360 and 40 - 30 == 10 and 10 * 9.0 == 90                     # shortfall = requirement less on hand


def start(pg, f, when='start'):
    readonly_checks(pg, f, {'iks': '500 gal'}, when)
    t = js(pg, "return r.querySelector('.g1').innerText")
    f.check(js(pg, "return r.querySelectorAll('.ln,.tote,.cmp').length") == 0, '%s: no formula open, no tote, no comparison' % when)
    f.check(not any(s in t for s in ('4,455', '222.75', '360', 'Soy sauce', '30.0')), '%s: nothing derived shows' % when)


def s1(pg, f):
    f.check(ids(pg, *['lb-%d' % i for i in range(6)], 'lbt') == '1.62|11.23|4.44|1.89|0.62|0.20|20.00', 'step 1: base lines for the 20 lb test pot sum to 20.00')


def s2(pg, f):
    f.check(ids(pg, *['lb-%d' % i for i in range(6)], 'lbt') == '360.0|2,502.0|990.0|420.0|138.0|45.0|4,455.0', 'step 2: scaled lines in lb, total 4,455')
    f.check(ids(pg, 'kgl', 'klb', 'kbd', 'ksf') == '500 gal|4,455 lb|8.91|222.75', 'step 2: 500 gal, 4,455 lb, density 8.91, factor 222.75')


def s3(pg, f):
    f.check(ids(pg, *['ga-%d' % i for i in range(6)], 'gat') == '40.0|300.0|90.0|50.0|15.0|5.0|500.0', 'step 3: gallons per line, total 500.0')


def s4(pg, f):
    f.check(ids(pg, 'tgl') == '30.0 gal', 'step 4: 270 lb tote is 30.0 gal')


def s5(pg, f):
    f.check(ids(pg, 'rqg', 'rql', 'ohg', 'sfg', 'sfl') == '40.0|360|30.0|10.0|90', 'step 5: 40 gal (360 lb) needed, 30 on hand, short 10 gal (90 lb)')


PLAN = [('A base formula, by weight', '20.00'),
        ('From test pot to full kettle', '4,455'),
        ('Pounds and gallons from each density', '500.0'),
        ('A tote becomes stocked gallons', '30.0 gal'),
        ('Requirement against stock on hand', 'Shortfall')]
f = run_card(1, PLAN, ['500 gal', '4,455', '222.75', '30.0 gal', 'Shortfall', '10.0'], start=start,
             extra={'after_step': {0: s1, 1: s2, 2: s3, 3: s4, 4: s5}})
keyboard_walk(f, 1, 5)
clicks_only(f, 1, 0)
clicks_only(f, 1, 0, 358, 390)
finish(f)
