#!/usr/bin/env python3
"""Card 1 (roast day board): the brief's numbers in Python, then the full click through in the browser.
Run: python3 tools/coffee-roasting/test_card1.py"""
import math, os, sys
from decimal import Decimal as D
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cr_tests import run_card, finish, js, pill, testlib, ids

# ---- the brief's numbers, derived independently of the card ----
OZ12, LB5 = D('340.194'), D('2267.96')          # grams per bag: 12 x 28.3495 g, 5 x 453.592 g
assert OZ12 == 12 * D('28.3495') and LB5 == 5 * D('453.592')
NEED = 40 * OZ12 + 8 * LB5                        # SO-5120: 40 x 12 oz, 8 x 5 lb
assert NEED == D('31751.44')
BATCHES = [D(12000), D(12000), NEED - 24000]
assert math.ceil(NEED / 12000) == 3 and sum(BATCHES) == NEED and BATCHES[2] == D('7751.44')
GREEN = [(b / D('0.86')).quantize(D('0.001')) for b in BATCHES]   # planned shrink 14%
assert str((GREEN[0] / 1000).quantize(D('0.001'))) == '13.953' and str((GREEN[2] / 1000).quantize(D('0.001'))) == '9.013'
# stage counts on Thursday: 3 batches and 2 pack jobs, then +3 batches and +2 pack jobs, then the rush adds 1 and 1
THU = [(3, 2), (6, 4), (7, 5)]
assert THU[1] == (3 + 3, 2 + 2) and THU[2] == (6 + 1, 4 + 1)
# packing stations: 12 oz 24 + 40 = 64 of 120; 5 lb 6 + 8 = 14 of 30, then + 4 = 18 of 30
assert 24 + 40 == 64 and round(D(64) / 120 * 100, 1) == D('53.3')
assert 6 + 8 == 14 and round(D(14) / 30 * 100, 1) == D('46.7') and D(18) / 30 * 100 == 60
# rush pulled into slot 5 (11:00): the batches in slots 5 and 6 move one slot, nothing else moves
SLOTS = {'B-411': 1, 'B-412': 2, 'B-413': 3, 'B-414': 4, 'B-415': 5, 'B-416': 6}
moved = sorted(k for k, s in SLOTS.items() if s >= 5)
assert moved == ['B-415', 'B-416']


def start(pg, f, when='start'):
    t = js(pg, "return r.querySelector('.q1').innerText")
    f.check(js(pg, "return r.querySelectorAll('.qit,.qwk,.qmo,.qsts').length") == 0, '%s: no batches, no week or month grid, no stations' % when)
    f.check(js(pg, "return ['qvD','qvW','qvM'].every(function(i){return r.getElementById(i).disabled})"), '%s: the view toggle waits for a day' % when)
    f.check(not any(s in t for s in ('B-411', 'B-414', '13.953', '53.3%', 'What moves')), '%s: nothing from the day shows' % when)


def s1(pg, f):
    f.check(ids(pg, 'qc0', 'qc1', 'qc2', 'qc3') == '3|3|3|2', 'step 1: Thursday Pick 3, Roast 3, Rest 3, Pack 2')


def s2(pg, f):
    f.check(ids(pg, 'qc0', 'qc1', 'qc2', 'qc3') == '6|6|6|4', 'step 2: the order adds 3 batches and 2 pack jobs')
    r = [ids(pg, 'qr-B-41%d' % i) for i in (4, 5, 6)]
    f.check(r[0].startswith('B-414 10:00') and r[1].startswith('B-415 11:00') and r[2].startswith('B-416 12:00'), 'step 2: B-414, B-415, B-416 at 10:00, 11:00, 12:00')
    t = js(pg, "return r.querySelector('.qcols').innerText")
    f.check('B-416 7.751' in t and '9.013 kg green' in t and '13.953 kg green' in t, 'step 2: batches 12.000, 12.000 and 7.751 kg roasted; 13.953 and 9.013 kg green')


def s3(pg, f):
    wk = [ids(pg, 'qw%d-19' % i) for i in range(4)]
    f.check(wk == ['6', '6', '6', '4'], 'step 3: week view Thursday 6, 6, 6, 4 (%s)' % wk)
    f.check(ids(pg, 'qsl') == 'Pick 6, Roast 6, Rest 6, Pack 4', 'step 3: week summary Pick 6, Roast 6, Rest 6, Pack 4')
    pg.locator('#cv #qvM').click(); pg.wait_for_timeout(300)
    m = ids(pg, 'qm19')
    f.check('6 roasts' in m and '4 packs' in m and ids(pg, 'qsl') == 'Pick 6, Roast 6, Rest 6, Pack 4', 'step 3: month view Thursday 6 roasts, 4 packs')
    pg.locator('#cv #qvD').click(); pg.wait_for_timeout(300)
    f.check(ids(pg, 'qc0', 'qc1', 'qc2', 'qc3') == '6|6|6|4', 'step 3: day view still 6, 6, 6, 4, stage counts equal in all three views')


def s4(pg, f):
    f.check(ids(pg, 'qsv12', 'qsv5') == '64 of 120 bags, 53.3%|14 of 30 bags, 46.7%', 'step 4: 12 oz 64 of 120 (53.3%), 5 lb 14 of 30 (46.7%)')


def s5(pg, f):
    f.check('11:00' in ids(pg, 'qmv-B-415') and '12:00' in ids(pg, 'qmv-B-415') and '12:00' in ids(pg, 'qmv-B-416') and '13:00' in ids(pg, 'qmv-B-416'), 'step 5: B-415 11:00 to 12:00, B-416 12:00 to 13:00')
    f.check(js(pg, "return r.querySelectorAll('[id^=\"qmv-\"]').length") == 2 and ids(pg, 'qmc') == '2 batches move one slot', 'step 5: exactly two batches move one slot')
    f.check(ids(pg, 'qc0', 'qc1', 'qc2', 'qc3', 'qsv5') == '7|7|7|5|18 of 30 bags, 60.0%', 'step 5: Thursday 7, 7, 7, 5 and the 5 lb station 18 of 30')
    pg.locator('#cv #qvW').click(); pg.wait_for_timeout(300)
    f.check(ids(pg, 'qw1-19', 'qw1-20') == '7|3', 'step 5: week view moves the batch from Friday (4 to 3) to Thursday')
    pg.locator('#cv #qvD').click(); pg.wait_for_timeout(300)


def confirm(pg, f):
    pg.locator('#cv #qcf').click(); pg.wait_for_timeout(300)
    f.check(ids(pg, 'qmc') == 'Confirmed', 'after Done: Confirm publishes the moves')


def drag(f):
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        b = testlib.browser(p)
        pg, errs = testlib.open_card(b, 1, 1300)
        pg.locator('#cv').scroll_into_view_if_needed()
        pg.locator('#cv .mtg [data-m="try"]').click(); pg.wait_for_timeout(400)
        pg.locator('#cv #qd19').click(); pg.wait_for_timeout(1700)
        pg.locator('#cv #qo1').drag_to(pg.locator('#cv #qbd')); pg.wait_for_timeout(600)
        f.check('Your turn3 of 5' in pill(pg) and ids(pg, 'qc1') == '6', 'dragging SO-5120 onto the board schedules it (%s)' % pill(pg))
        b.close()


PLAN = [('Open the roast day board', 'B-411'),
        ('Drop a wholesale order on the day', 'B-416'),
        ('Switch between day, week and month', 'Pick 6, Roast 6, Rest 6, Pack 4'),
        ('See packing stations filled by bag size', '53.3%'),
        ('Pull a rush order forward and read what moves', '13:00')]

f = run_card(1, PLAN, ['60.0%', '13:00', '2 batches move one slot'], start=start,
             extra={'after_step': {0: s1, 1: s2, 2: s3, 3: s4, 4: s5}, 'after': confirm})
drag(f)
finish(f)
