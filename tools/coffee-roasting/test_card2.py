#!/usr/bin/env python3
"""Card 2 (record form with side summary: green lots and roast yield): the numbers in Python, then the full click through.
Run: python3 tools/coffee-roasting/test_card2.py"""
import os, sys
from decimal import Decimal as D, ROUND_HALF_UP
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cr_tests import clicks_only, run_card, finish, js, pill, testlib, ids, enter_submits, keyboard_walk


def pct(loss, inn):
    return str((D(loss) * 100 / D(inn)).quantize(D('0.1'), rounding=ROUND_HALF_UP)) + '%'


# ---- the numbers, derived independently of the card (grams) ----
# The README example said 60 kg in, 50.4 kg out is a 14.0% loss. It is 16.0%. The card keeps 14.0% by using 51.6 kg.
assert pct(60000 - 50400, 60000) == '16.0%'
assert pct(60000 - 51600, 60000) == '14.0%' and 60000 - 51600 == 8400                # 8.4 kg lost, 14.0%
BAL, BW, BAGS = 840000, 60000, 20
assert BAL - 60000 == 780000 and BAL - (BAL - 60000) == 60000                        # the lot drops by exactly 60.0 kg
assert BAL // BW == 14 and (BAL - 60000) // BW == 13 and BAGS * BW == 1200000
assert 840000 + 980000 + 1260000 == 3080000 and 3080000 - 60000 == 3020000           # total green on hand
HIST = [(0, 'L', 60000, 52500), (0, 'L', 40000, 35000), (0, 'M', 60000, 51000), (0, 'D', 30000, 25200),
        (1, 'L', 60000, 52800), (1, 'M', 60000, 52200), (1, 'D', 60000, 50400), (2, 'L', 60000, 52200), (2, 'M', 60000, 51300), (2, 'D', 60000, 49800),
        (0, 'M', 60000, 51600)]                                                       # the new batch RB-5120


def shr(o=None, l=None):
    xs = [h for h in HIST if (o is None or h[0] == o) and (l is None or h[1] == l)]
    a, z = sum(h[2] for h in xs), sum(h[3] for h in xs)
    return pct(a - z, a)


WANT = {}
for o in (0, 1, 2):
    for l in 'LMD':
        WANT['gx%d%s' % (o, l)] = shr(o, l)
    WANT['gx%dA' % o] = shr(o)
for l in 'LMD':
    WANT['gxA' + l] = shr(None, l)
WANT['gxAA'] = shr()
assert (WANT['gx0A'], WANT['gx1A'], WANT['gx2A']) == ('13.9%', '13.7%', '14.8%')     # by origin
assert (WANT['gxAL'], WANT['gxAM'], WANT['gxAD'], WANT['gxAA']) == ('12.5%', '14.1%', '16.4%', '14.1%')   # by roast level
assert WANT['gx0M'] == '14.5%'                                                         # Ethiopia medium includes RB-5120
USE = [20000, 18000, 12000]
assert sum(USE) == 50000 and pct(50000 - 43000, 50000) == '14.0%'                     # RL-8820 traces to 50.0 kg green


def start(pg, f, when='start'):
    t = js(pg, "return r.querySelector('.k2').innerText")
    f.check(js(pg, "return r.getElementById('gin').value") == '', '%s: the lot input is empty' % when)
    f.check(js(pg, "return r.querySelectorAll('.gg,.glots .row,.gshr .row,.grl .row,.tw').length") == 0, '%s: no lot record, balances or shrink' % when)
    f.check(not any(s in t for s in ('Ethiopia', '840.0', 'RB-5120', 'RL-8820')), '%s: nothing derived from the lot shows' % when)


def bad_then_type(pg, f):
    inp = pg.locator('#cv #gin')
    inp.click(); inp.press_sequentially('GL-9999'); inp.press('Enter'); pg.wait_for_timeout(300)
    f.check(js(pg, "return r.getElementById('gfl').classList.contains('err')"), 'step 1: an unknown lot shows an inline error')
    f.check('Your turn1 of 5' in pill(pg), 'step 1: an unknown lot does not advance')
    inp.fill(''); inp.press_sequentially('gl-4471')
    f.check(js(pg, "return r.getElementById('gin').value") == 'gl-4471', 'step 1: typing works in the input')


def bad_weight(pg, f):
    f.check(js(pg, "return r.getElementById('gout').value") == '51.6', 'step 3: the scale reading 51.6 is in the field')
    inp = pg.locator('#cv #gout'); inp.fill('70'); pg.locator('#cv #gsv').click(); pg.wait_for_timeout(300)
    f.check(js(pg, "return r.getElementById('gofl').classList.contains('err')"), 'step 3: a weight above the green in shows an inline error')
    f.check('Your turn3 of 5' in pill(pg), 'step 3: a bad weight does not advance')
    inp.fill(''); inp.press_sequentially('51.6')


def s1(pg, f):
    f.check(ids(pg, 'gbg', 'gbl', 'gb0', 'gk0', 'gk1', 'gk2', 'gtt') == '14 of 20, 60.0 kg|840.0 kg|14|840.0|980.0|1,260.0|3,080.0 kg', 'step 1: GL-4471 14 of 20 bags, 840.0 kg; three origins, 3,080.0 kg')


def s2(pg, f):
    f.check(ids(pg, 'gbg', 'gbl', 'gb0', 'gk0', 'gtt') == '13 of 20, 60.0 kg|780.0 kg|13|780.0|3,020.0 kg', 'step 2: the lot drops by exactly 60.0 kg to 780.0 kg')


def s3(pg, f):
    f.check(ids(pg, 'ggi', 'glw', 'gls') == '60.0 kg|8.4 kg|14.0%', 'step 3: 60.0 kg in, 51.6 out, 8.4 kg lost, 14.0%')


def s4(pg, f):
    got = dict(zip(WANT, ids(pg, *WANT).split('|')))
    f.check(got == WANT, 'step 4: every shrink cell matches (%s)' % {k: v for k, v in got.items() if WANT[k] != v})


def s5(pg, f):
    f.check(ids(pg, 'gt0', 'gt1', 'gt2', 'gts', 'gtl') == '20.0 kg|18.0 kg|12.0 kg|50.0 kg green in, 43.0 kg out|14.0% loss', 'step 5: RL-8820 traces to 20.0 + 18.0 + 12.0 = 50.0 kg green')


PLAN = [('Every green lot keeps its source', '840.0 kg'),
        ('A roast draws down the lot', '780.0 kg'),
        ('Roast loss from the scale', '14.0%'),
        ('Shrink by origin and roast level', '16.4%'),
        ('Every roasted lot traces back', '50.0 kg green in')]

f = run_card(2, PLAN, ['780.0 kg', '14.0%', '13.9%', '50.0 kg green in'], start=start,
             extra={'before': {0: bad_then_type, 2: bad_weight}, 'after_step': {0: s1, 1: s2, 2: s3, 3: s4, 4: s5}})
enter_submits(f, 2, '#gin', 'GL-4471', 'Your turn2 of 5')
keyboard_walk(f, 2, 5, fill=lambda pg, i: i == 0 and pg.locator('#cv #gsm').click())
clicks_only(f, 2)
clicks_only(f, 2, card_w=358, vw=390)
finish(f)
