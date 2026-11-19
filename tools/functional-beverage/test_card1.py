#!/usr/bin/env python3
"""Card 1 (record form with a side summary): the README's numbers in Python, then the click through.
Run: python3 tools/functional-beverage/test_card1.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fv_tests import run_card, finish, js, ids, readonly_checks, keyboard_walk, clicks_only

M = '−'
DOSE, CLAIM = 1200, 60
assert round(DOSE * 0.050, 1) == 60.0                     # dose x potency = active per can at 5.0%
assert round(DOSE * 0.045, 1) == 54.0                     # and at 4.5%
assert CLAIM - 54 == 6                                    # 6 mg shortfall
FLAG = lambda active: active < CLAIM
assert not FLAG(60.0) and FLAG(54.0)                      # the flag appears only when active is below the claim


def start(pg, f, when='start'):
    readonly_checks(pg, f, {'isv': '12 oz can'}, when)
    t = js(pg, "return r.querySelector('.g1').innerText")
    f.check(js(pg, "return r.querySelectorAll('.ln,.pc,#sact').length") == 0, '%s: no formula open' % when)
    f.check(not any(s in t for s in ('60', '1,200', 'ASH-2291', 'Meets')), '%s: nothing derived shows' % when)


def s1(pg, f):
    f.check('1,200 mg' in js(pg, "return r.querySelector('.ln').innerText") and ids(pg, 'lact') == '', 'step 1: the formula opens with 1,200 mg extract, active not yet calculated')


def s2(pg, f):
    f.check(ids(pg, 'lpot', 'lact', 'sact', 'scal') == '5.0%|60.0 mg|60.0 mg|1,200 mg x 5.0% = 60.0 mg', 'step 2: 1,200 mg x 5.0% = 60.0 mg')


def s3(pg, f):
    f.check(ids(pg, 'sdif', 'sst') == '0.0 mg|Meets' and js(pg, "return r.getElementById('flb')") is None, 'step 3: meets the 60 mg claim, no flag offered')


def s4(pg, f):
    f.check(ids(pg, 'lact', 'sact', 'sdif', 'sst') == '54.0 mg|54.0 mg|%s6.0 mg|Below' % M, 'step 4: 4.5% gives 54.0 mg, 6.0 mg short')
    f.check('not approved' in js(pg, "return r.getElementById('sm').innerText"), 'step 4: shown as a preview before approval')


def s5(pg, f):
    f.check(ids(pg, 'fst') == 'Flagged, below claim' and 'Flagged' in js(pg, "return r.getElementById('f-CAT-12').innerText"), 'step 5: the formula is flagged')


PLAN = [('A formula with its actives', '1,200 mg'),
        ('Active per serving from dose and potency', '60.0 mg'),
        ('Checked against the label claim', 'Meets'),
        ('A new lot potency, previewed before approval', '54.0 mg'),
        ('Flagged before it reaches a batch', 'Flagged')]
f = run_card(1, PLAN, ['60 mg', '54.0 mg', '6.0 mg', 'Flagged'], start=start,
             extra={'after_step': {0: s1, 1: s2, 2: s3, 3: s4, 4: s5}})
keyboard_walk(f, 1, 5)
clicks_only(f, 1, 0)
clicks_only(f, 1, 0, 358, 390)
finish(f)
