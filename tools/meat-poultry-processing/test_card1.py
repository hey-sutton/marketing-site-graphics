#!/usr/bin/env python3
"""Card 1 (stage chain): the README's yield and loss numbers in Python, then the click through.
Run: python3 tools/meat-poultry-processing/test_card1.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from mp_tests import run_card, finish, js, ids, readonly_checks, keyboard_walk, clicks_only

RAW, SPEC = 1000, 45.0
W = [950, 900, 420]                                   # after drainage, trim, drying
INS = [RAW] + W[:-1]
LOSS = [i - o for i, o in zip(INS, W)]
assert LOSS == [50, 50, 480]
assert sum(LOSS) == 580                               # the three loss lines sum to 580
assert RAW - sum(LOSS) == 420 == W[-1]                # 1,000 minus 580 equals 420
YIELD = W[-1] / RAW * 100
assert round(YIELD, 1) == 42.0                        # yield equals 420 / 1,000
EXP = RAW * SPEC / 100
assert EXP == 450
assert EXP - W[-1] == 30                              # the gap equals 450 minus 420

INPUT = {'ibt': 'JRK-3310, Beef Jerky, 1,000 kg raw'}


def start(pg, f, when='start'):
    readonly_checks(pg, f, INPUT, when)
    f.check(js(pg, "return r.querySelectorAll('.sg,.lr,.cr,.ys').length") == 0, '%s: no stages, loss lines or spec shown' % when)
    t = js(pg, "return r.querySelector('.g2').innerText")
    f.check(not any(s in t for s in ('950', '450', '45.0', '420', '580')), '%s: nothing derived shows' % when)


def s1(pg, f):
    f.check(ids(pg, 'spy', 'spk', 'win') == '45.0%|450|1,000', 'step 1: spec 45.0%, 450 kg expected, 1,000 kg in')
    f.check(js(pg, "return r.querySelectorAll('.chain .sg').length") == 4, 'step 1: weight in plus three stage boxes')
    f.check(js(pg, "return r.querySelectorAll('#w-dr,#w-tr,#w-dy').length") == 0, 'step 1: no stage weights yet')


def s2(pg, f):
    f.check(ids(pg, 'w-dr', 'pr-dr') == '950|95.0%', 'step 2: 950 kg after drainage')
    f.check(js(pg, "return r.querySelectorAll('#w-tr,#w-dy').length") == 0, 'step 2: trim and drying not logged yet')


def s3(pg, f):
    f.check(ids(pg, 'w-tr', 'w-dy') == '900|420', 'step 3: 900 kg after trim, 420 kg after drying')


def s4(pg, f):
    got = [int(ids(pg, 'ln-' + k).split()[0].replace(',', '')) for k in ('dr', 'tr', 'dy')]
    f.check(got == LOSS, 'step 4: loss lines %s' % got)
    tot = int(ids(pg, 'lt').split()[0].replace(',', ''))
    f.check(tot == sum(got) == 580, 'step 4: loss lines sum to the 580 kg total on screen')
    f.check(ids(pg, 'lcal') == '50 + 50 + 480 = 580 kg1,000 − 580 = 420 kg out', 'step 4: 1,000 minus 580 = 420 on screen (%s)' % ids(pg, 'lcal'))
    f.check(ids(pg, 'lo-dr', 'lo-tr', 'lo-dy') == 'Loss 50 kg|Loss 50 kg|Loss 480 kg', 'step 4: each box carries its loss line')


def s5(pg, f):
    f.check(ids(pg, 'cs', 'ca', 'ack') == '45.0%|42.0%|420', 'step 5: 42.0% actual against 45.0% spec')
    f.check(round(int(ids(pg, 'ack')) / int(ids(pg, 'win').replace(',', '')) * 100, 1) == float(ids(pg, 'ca')[:-1]), 'step 5: yield = 420 / 1,000 on screen')
    f.check('30 kg' in ids(pg, 'gap') and int(ids(pg, 'spk')) - int(ids(pg, 'ack')) == 30, 'step 5: gap 450 minus 420 = 30 kg')


PLAN = [('A batch with its expected yield', '450'),
        ('Weight in and after drainage', '950'),
        ('Trim and cook weights logged', '420'),
        ('Each loss on its own line', '580 kg'),
        ('Actual yield against the spec', 'under spec')]
f = run_card(1, PLAN, ['580 kg', '42.0%', '45.0%', '30 kg', '480 kg'], start=start,
             extra={'after_step': {0: s1, 1: s2, 2: s3, 3: s4, 4: s5}})
keyboard_walk(f, 1, 5)
clicks_only(f, 1, 1)
clicks_only(f, 1, 1, 358, 390)
finish(f)
