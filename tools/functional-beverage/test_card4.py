#!/usr/bin/env python3
"""Card 4 (stage chain): the README's limits in Python, then the click through, including result set 2.
Run: python3 tools/functional-beverage/test_card4.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fv_tests import run_card, finish, js, ids, readonly_checks, keyboard_walk, clicks_only

LIM = {'act': (57, 63), 'tpc': (None, 100), 'ym': (None, 100)}
OK = lambda k, v: (LIM[k][0] is None or v >= LIM[k][0]) and v <= LIM[k][1]
SET1 = {'act': 61, 'tpc': 80, 'ym': 20}
SET2 = {'act': 61, 'tpc': 80, 'ym': 150}
assert all(OK(k, v) for k, v in SET1.items())                       # set 1: all within, release allowed
assert [k for k, v in SET2.items() if not OK(k, v)] == ['ym']       # set 2: only yeast and mold flagged
assert OK('act', 57) and OK('act', 63) and not OK('act', 56) and not OK('act', 64) and OK('ym', 100) and not OK('ym', 101)
W1 = {'i-act': '61 mg', 'i-tpc': '80 CFU/mL', 'i-ym': '20 CFU/mL'}


def rel_disabled(pg):
    return js(pg, "var b=r.getElementById('rlb');return !!b&&b.disabled")


def start(pg, f, when='start'):
    readonly_checks(pg, f, {}, when)
    f.check(js(pg, "return r.querySelectorAll('.stg:not(.e),.rds,.trc').length") == 0, '%s: chain and results empty' % when)
    t = js(pg, "return r.getElementById('chn').innerText+r.getElementById('bot').innerText")
    f.check(not any(s in t for s in ('61', '18,000', 'Within', 'ASH-2291')), '%s: nothing derived shows' % when)


def s1(pg, f):
    f.check(ids(pg, 'bst') == 'On hold' and '18,000' in js(pg, "return r.getElementById('chn').innerText"), 'step 1: FB-0412, 18,000 cans on hold')


def s2(pg, f):
    readonly_checks(pg, f, W1, 'step 2')
    f.check(ids(pg, 'c-act', 'c-tpc', 'c-ym') == 'Recorded|Recorded|Recorded', 'step 2: three results recorded, not yet checked')


def s3(pg, f):
    f.check(ids(pg, 'c-act', 'c-tpc', 'c-ym') == 'Within|Within|Within' and not rel_disabled(pg), 'step 3: all within limits, Release enabled')
    pg.locator('#cv #s2').click(); pg.wait_for_timeout(400)
    readonly_checks(pg, f, {'i-act': '61 mg', 'i-tpc': '80 CFU/mL', 'i-ym': '150 CFU/mL'}, 'result set 2')
    f.check(ids(pg, 'c-act', 'c-tpc', 'c-ym') == 'Within|Within|Outside', 'result set 2: only yeast and mold 150 is flagged')
    f.check(rel_disabled(pg) and ids(pg, 'bst', 'rst') == 'Review|Review', 'result set 2: Release disabled, batch routed to review')
    pg.locator('#cv #s1').click(); pg.wait_for_timeout(400)
    f.check(not rel_disabled(pg) and ids(pg, 'bst') == 'On hold', 'back to result set 1: Release enabled again')


def s4(pg, f):
    f.check(ids(pg, 'bst', 'rst') == 'Released|Released', 'step 4: released with a sign off')


def s5(pg, f):
    f.check(js(pg, "return !!r.getElementById('t-ASH-2291')") and 'ASH-2291' in js(pg, "return r.getElementById('trc').innerText"), 'step 5: the trace lists ASH-2291')


PLAN = [('A filled batch, on hold', '18,000'),
        ('Potency and microbial results on the batch', '61 mg'),
        ('Each result against its limit', 'Within'),
        ('Released with a sign off', 'Released'),
        ('From the released lot to its inputs', 'ASH-2291')]
f = run_card(4, PLAN, ['18,000', 'ASH-2291', 'LT-0877', 'Released'], start=start,
             extra={'after_step': {0: s1, 1: s2, 2: s3, 3: s4, 4: s5}})
keyboard_walk(f, 4, 5)
clicks_only(f, 4, 0)
clicks_only(f, 4, 0, 358, 390)
finish(f)
