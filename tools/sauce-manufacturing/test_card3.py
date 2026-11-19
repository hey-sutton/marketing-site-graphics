#!/usr/bin/env python3
"""Card 3 (list and detail): the README's numbers in Python, then the click through.
Run: python3 tools/sauce-manufacturing/test_card3.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sm_tests import run_card, finish, js, ids, readonly_checks, keyboard_walk, clicks_only

BULK = 400
AL = [200, 80, 100]
LOSS = 20
assert sum(AL) + LOSS == BULK and sum(AL) == 380                    # filled plus loss equals bulk
REM = []
r = BULK
for g in AL:
    r -= g; REM.append(r)
assert REM == [200, 120, 20] and r - LOSS == 0                     # remaining after each fill, then 0
assert sum(AL) / BULK * 100 == 95.0                                # yield = filled / bulk
JAR = [0.62, 0.18, 0.35]
assert round(sum(JAR), 2) == 1.15                                  # jar cost = ingredients + labor + packaging
assert round(12 * 1.15, 2) == 13.80                                # case cost = 12 x jar cost
assert [200 * 128 // 12, 80 * 128 // 32, 100 * 128 // 12] == [2133, 320, 1066]


def start(pg, f, when='start'):
    readonly_checks(pg, f, {}, when)
    t = js(pg, "return r.getElementById('dt').innerText+r.getElementById('rm').innerText")
    f.check(js(pg, "return r.querySelectorAll('.al,.facts,.hist').length") == 0, '%s: no bulk lot open' % when)
    f.check(not any(s in t for s in ('200', '95', '$', 'FL-91')), '%s: nothing derived shows' % when)


def s1(pg, f):
    f.check(ids(pg, 'rmg', 'h-0') == '400 gal|400', 'step 1: BL-7710 opens with 400 gal')


def s2(pg, f):
    f.check(ids(pg, 'alt', 'j-0', 'j-1', 'j-2') == '380|2,133|320|1,066', 'step 2: three allocations, 380 gal planned')


def s3b(pg, f):
    for i, want in ((0, '200 gal'), (1, '120 gal')):
        f.check(js(pg, "var h=r.querySelector('.hint');return h&&h.id") == 'fb-%d' % i, 'step 3: the prompt points at Fill %d' % (i + 1))
        pg.locator('#cv #fb-%d' % i).click(); pg.wait_for_timeout(400)
        f.check(ids(pg, 'rmg') == want, 'step 3: %s left after fill %d' % (want, i + 1))


def s3(pg, f):
    f.check(ids(pg, 'rmg', 'h-1', 'h-2', 'h-3') == '20 gal|200|120|20', 'step 3: 200, 120, 20 left after each fill')
    t = js(pg, "return r.querySelector('.fls').innerText")
    f.check(all(s in t for s in ('FL-9101', 'FL-9102', 'FL-9103')) and t.count('BL-7710') == 3, 'step 3: every filled lot carries BL-7710')


def s4(pg, f):
    f.check(ids(pg, 'yf', 'yl', 'yp', 'yr', 'rmg') == '380 gal|20 gal|95.0%|0 gal|0 gal', 'step 4: 380 filled, 20 loss, 95.0%, tank at 0')


def s5(pg, f):
    f.check(ids(pg, 'cc-0', 'cc-1', 'cc-2', 'cpj', 'cpc') == '$0.62|$0.18|$0.35|$1.15|$13.80', 'step 5: $1.15 a jar, $13.80 a case of 12')


PLAN = [('A cooked bulk lot in a holding tank', '400 gal'),
        ('Two flavors, two jar sizes, three fills', 'Spicy, 12 oz'),
        ('Remaining bulk drops with each fill', '20 gal'),
        ('Yield and loss on the batch', '95.0%'),
        ('Cost per jar and per case', '$13.80')]
f = run_card(3, PLAN, ['380 gal', '20 gal', '95.0%', '$1.15', '$13.80', 'FL-9103'], start=start,
             extra={'before': {2: s3b}, 'after_step': {0: s1, 1: s2, 2: s3, 3: s4, 4: s5}})
keyboard_walk(f, 3, 5)
clicks_only(f, 3, 2)
clicks_only(f, 3, 2, 358, 390)
finish(f)
