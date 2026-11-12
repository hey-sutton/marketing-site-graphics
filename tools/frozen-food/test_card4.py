#!/usr/bin/env python3
"""Card 4 (stage board): the brief's numbers in Python, then the click through. Run: python3 tools/frozen-food/test_card4.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ff_tests import run_card, finish, js, ids

IN, EXP, ACT = 400, [392, 388, 386, 385, 384], [392, 386, 382, 380, 378]
assert all(a <= e for a, e in zip(ACT, EXP))                  # actuals never exceed expected
assert EXP[-1] == 400 * 96 // 100 and IN - ACT[-1] == 22 and IN - EXP[-1] == 16 and EXP[-1] - ACT[-1] == 6
loss = [(IN if i == 0 else ACT[i - 1]) - ACT[i] for i in range(5)]
assert loss == [8, 6, 4, 2, 2] and sum(loss) == 22
assert 378 / 6 == 63 and 384 / 6 == 64 and 160 - 150 == 10 and 120 <= 140


def start(pg, f, when='start'):
    t = js(pg, "return r.querySelector('.g4').innerText")
    f.check(all(s in t for s in ('Prep', 'Cook', 'Assemble', 'Freeze', 'Pack')) and js(pg, "return r.querySelectorAll('.bx b,.rn.sel').length") == 0, '%s: five stage names, no run selected' % when)
    f.check('392' not in t and '63' not in t, '%s: no output before a run is selected' % when)


def s2(pg, f):
    f.check(ids(pg, 'e0', 'e1', 'e2', 'e3', 'e4') == '392|388|386|385|384', 'step 2: expected 392, 388, 386, 385, 384')


def s3(pg, f):
    f.check(ids(pg, 'a0', 'a1', 'a2', 'a3', 'a4') == '392|386|382|380|378', 'step 3: actual 392, 386, 382, 380, 378')
    f.check(ids(pg, 'l0', 'l1', 'l2', 'l3', 'l4') == '8 lb lost|6 lb lost|4 lb lost|2 lb lost|2 lb lost', 'step 3: loss at each stage')
    f.check(ids(pg, 'tls', 'vpk') == 'Total loss 22 lb against 16 lb expected.|Pack 6 lb under', 'step 3: 22 lb lost against 16, pack 6 under')


def s4(pg, f):
    f.check(ids(pg, 'fgc') == '63' and 'Expected 64, 1 case short' in ids(pg, 'fgg') and 'Holding freezer A' in js(pg, "return r.getElementById('fg').innerText"), 'step 4: 63 cases to Holding freezer A, 1 short of 64')


def s5(pg, f):
    f.check(ids(pg, 'msh', 'ms0', 'ms1', 'ms2') == '1 short|10|0|0', 'step 5: chicken short 10 lb, nothing else short')


def po(pg, f):
    pg.locator('#cv #cpo').click(); pg.wait_for_timeout(400)
    f.check('10 lb from Harvest Ridge Farms' in (ids(pg, 'pod') or ''), 'Create purchase order adds a draft for 10 lb')


PLAN = [('One run, five stages, 400 lb in', 'Run MO-6105'),
        ('The routing sets expected output at every stage', '384'),
        ('Actual output fills in stage by stage, with the loss at each', 'Total loss 22 lb'),
        ('Finished cases post straight to a freezer', 'cases to Holding freezer A'),
        ('The next run is checked against stock before it starts', 'Create purchase order')]
f = run_card(4, PLAN, ['Total loss 22 lb against 16 lb expected.', 'Holding freezer A'], start=start,
             extra={'after_step': {1: s2, 2: s3, 3: s4, 4: s5}, 'after': po})
finish(f)
