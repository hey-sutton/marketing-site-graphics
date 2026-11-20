#!/usr/bin/env python3
"""Card 2 (stage chain): the README's yield numbers in Python, then the click through.
Run: python3 tools/nut-processing/test_card2.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from np_tests import run_card, finish, js, ids, readonly_checks, keyboard_walk, clicks_only

RAW, OUTS, EXP = 20000, [12800, 12160, 11552], 56.0
INS = [RAW] + OUTS[:-1]
LOSS = [(i - o) / i * 100 for i, o in zip(INS, OUTS)]
assert [round(x, 6) for x in LOSS] == [36.0, 5.0, 5.0]                       # each loss percent
YIELD = OUTS[-1] / RAW * 100
assert round(YIELD, 6) == 57.76 and abs(0.64 * 0.95 * 0.95 * 100 - YIELD) < 1e-9   # total = product of stage yields
ORG = {'A26': round(YIELD, 1), 'B26': 55.0, 'A25': 58.1, 'B25': 56.4}
assert ORG['A26'] == 57.8
FLAG = [k for k, v in ORG.items() if v < EXP]
assert FLAG == ['B26']                                                         # the flag only below 56
assert RAW - OUTS[-1] == 8448


def start(pg, f, when='start'):
    readonly_checks(pg, f, {'ilt': 'L-2417'}, when)
    f.check(js(pg, "return r.querySelectorAll('.sg,.lr,.orw').length") == 0, '%s: no stages, loss or yield shown' % when)
    t = js(pg, "return r.querySelector('.g2').innerText")
    f.check(not any(s in t for s in ('20,000', '12,800', '57.76', 'Shelling')), '%s: nothing derived shows' % when)


def s1(pg, f):
    f.check(js(pg, "return r.querySelectorAll('.chain .sg').length") == 5, 'step 1: raw lot plus four stage boxes')
    f.check(js(pg, "return r.querySelectorAll('#in0,#out0').length") == 0, 'step 1: weights not shown yet')


def s2(pg, f):
    num = lambda x: int(x.replace(',', ''))
    ins = [num(ids(pg, 'in%d' % i)) for i in range(3)]; outs = [num(ids(pg, 'out%d' % i)) for i in range(3)]
    f.check(ins == INS and outs == OUTS, 'step 2: weights in %s and out %s' % (ins, outs))
    f.check(all(ins[i + 1] == outs[i] for i in range(2)), 'step 2: each stage takes in what the last put out')
    f.check(ids(pg, 'pk', 'ty', 'ry0', 'ry1', 'ry2') == '11,552|57.76%|64.0%|60.8%|57.76%', 'step 2: running yield 64.0, 60.8, 57.76')


def s3(pg, f):
    f.check(ids(pg, 'lo0', 'lo1', 'lo2') == 'Loss 36.0%|Loss 5.0%|Loss 5.0%', 'step 3: loss chips on the stage boxes')
    f.check(ids(pg, 'lp0', 'lp1', 'lp2') == '36.0%|5.0%|5.0%', 'step 3: loss bars 36, 5, 5')
    f.check(ids(pg, 'yp') == '0.64 × 0.95 × 0.95 = 57.76% yield' and ids(pg, 'lst') == '8,448', 'step 3: yield product and 8,448 lb lost')


def s4(pg, f):
    f.check(ids(pg, 'oy-A26', 'oy-B26', 'oy-A25', 'oy-B25') == '57.8%|55.0%|58.1%|56.4%', 'step 4: yield by origin and season')
    f.check(js(pg, "return r.querySelectorAll('.orw.fl').length") == 0, 'step 4: nothing flagged before the check')


def s5(pg, f):
    fl = js(pg, "return [].map.call(r.querySelectorAll('.orw.fl'),function(e){return e.id})")
    f.check(fl == ['o-B26'], 'step 5: only origin B 2026 at 55.0%% is flagged (56.4%% is not) %s' % fl)
    f.check('L-2433' in ids(pg, 'fnt'), 'step 5: flag note names lot L-2433')


PLAN = [('A raw lot through every stage', 'Blanching'),
        ('Weight in and out at each stage', '11,552'),
        ('Loss by stage', '36.0%'),
        ('Yield across origins', '55.0%'),
        ('A lot below expected yield is flagged', 'Flagged for review')]
f = run_card(2, PLAN, ['57.76%', '8,448', '57.8%', '55.0%'], start=start,
             extra={'after_step': {0: s1, 1: s2, 2: s3, 3: s4, 4: s5}})
keyboard_walk(f, 2, 5)
clicks_only(f, 2, 0)
clicks_only(f, 2, 0, 358, 390)
finish(f)
