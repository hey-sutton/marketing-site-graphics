#!/usr/bin/env python3
"""Card 1 (board: roast planning and scheduling): the numbers in Python, then the full click through.
Run: python3 tools/coffee-roasting/test_card1.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cr_tests import run_card, finish, js, pill, testlib, ids, keyboard_walk

# ---- the numbers, derived independently of the card ----
ORDER_G, BATCHES = 60000, ['B-301', 'B-302', 'B-303']
assert ORDER_G % len(BATCHES) == 0 and ORDER_G // len(BATCHES) == 20000          # 3 batches of 20.0 kg
assert sum([ORDER_G // 3] * 3) == 60000                                            # batches add back to the order
SLOT0, SLOT = 7 * 60, 45


def hm(t):
    return '%02d:%02d' % divmod(t, 60)


before = {b: hm(SLOT0 + i * SLOT) for i, b in enumerate(BATCHES)}
after_q = BATCHES[:1] + ['B-305'] + BATCHES[1:]
after = {b: hm(SLOT0 + i * SLOT) for i, b in enumerate(after_q)}
moved = [b for b in BATCHES if before[b] != after[b]]
assert moved == ['B-302', 'B-303'] and len(moved) == 2                          # the rush moves two later batches
assert all(after_q.index(b) - BATCHES.index(b) == 1 for b in moved)                # by exactly one slot each
assert (before['B-302'], after['B-302'], before['B-303'], after['B-303'], after['B-305']) == ('07:45', '08:30', '08:30', '09:15', '07:45')
assert 96 * 100 // 240 == 40 and 96 * 100 % 240 == 0                               # 12 oz station 40% of its shift
assert 8 * 100 // 40 == 20 and 8 * 100 % 40 == 0                                   # 5 lb station 20%
WED = {'start': (0, 0, 2, 0), 'order': (3, 3, 2, 0), 'stations': (3, 3, 2, 2), 'rush': (4, 4, 2, 2)}


def counts(pg, prefix):
    return tuple(int(x) for x in ids(pg, *[prefix + k for k in 'PREK']).split('|'))


def views_equal(pg, f, want, label, back='D'):
    """Day, week and month views count Wed 18 the same."""
    got = {}
    for v, pre in (('D', 'kc'), ('W', 'kw'), ('M', 'km')):
        pg.locator('#cv #kv' + v).click(); pg.wait_for_timeout(250)
        got[v] = counts(pg, pre)
    f.check(got['D'] == got['W'] == got['M'] == want, '%s: Wed 18 counts equal in day, week and month %s (want %s)' % (label, got, want))
    pg.locator('#cv #kv' + back).click(); pg.wait_for_timeout(250)


def start(pg, f, when='start'):
    t = js(pg, "return r.querySelector('.k1').innerText")
    f.check(js(pg, "return r.querySelectorAll('.col,.it,.sl,.oc,.st,#kcP').length") == 0, '%s: no board, batches, orders or stations' % when)
    f.check(not any(s in t for s in ('B-30', 'W-2041', 'L-1117', 'bags')), '%s: nothing derived from the day shows' % when)


def s1(pg, f):
    f.check(counts(pg, 'kc') == WED['start'], 'step 1: Wed 18 board Pick 0, Roast 0, Rest 2, Pack 0')


def s2(pg, f):
    f.check(counts(pg, 'kc') == WED['order'], 'step 2: the order adds 3 picks and 3 roast batches')
    f.check(ids(pg, 'ks0', 'ks1', 'ks2').replace('\n', ' ').count('20.0 kg green') == 3, 'step 2: three 20.0 kg batches in the queue')
    t = js(pg, "return r.getElementById('kbd').innerText")
    f.check(all(b in t for b in BATCHES), 'step 2: B-301, B-302 and B-303 on the board')


def s3(pg, f):
    f.check(counts(pg, 'kw') == WED['order'], 'step 3: the week view counts Wed 18 as 3, 3, 2, 0')
    views_equal(pg, f, WED['order'], 'step 3', back='W')


def s4(pg, f):
    f.check(counts(pg, 'kc') == WED['stations'], 'step 4: Pack shows 2 stations')
    f.check(ids(pg, 'kp0', 'kp1') == '96 bags|8 bags', 'step 4: 96 bags of 12 oz, 8 bags of 5 lb')
    q = ids(pg, 'kq0', 'kq1')
    f.check('40% of 240' in q and '20% of 40' in q, 'step 4: 40%% and 20%% of shift (%s)' % q)


def s5(pg, f):
    f.check(ids(pg, 'kmv', 'krb', 'krm0', 'krm1') == 'Moves 2|New at 07:45|07:45 to 08:30|08:30 to 09:15', 'step 5: rush takes 07:45, two batches move one slot')
    f.check('B-305' in ids(pg, 'ks1') and 'B-303' in ids(pg, 'ks3'), 'step 5: the queue shows B-305 in slot 2 and B-303 in slot 4')
    f.check(counts(pg, 'kc') == WED['rush'], 'step 5: Pick 4, Roast 4 after the rush')


def done(pg, f):
    views_equal(pg, f, WED['rush'], 'done')
    pg.locator('#cv #kcf').click(); pg.wait_for_timeout(300)
    f.check('Confirmed' in js(pg, "return r.getElementById('krs').innerText"), 'done: Confirm marks the rush confirmed')


def drag(f):
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        b = testlib.browser(p)
        pg, errs = testlib.open_card(b, 1, 1300)
        pg.locator('#cv').scroll_into_view_if_needed()
        pg.locator('#cv .mtg [data-m="try"]').click(); pg.wait_for_timeout(400)
        pg.locator('#cv #kd2').click(); pg.wait_for_timeout(1800)
        pg.locator('#cv #kor1').drag_to(pg.locator('#cv #kbd'))
        pg.wait_for_timeout(600)
        f.check('Your turn3 of 5' in pill(pg) or 'Your turn' in pill(pg) and counts(pg, 'kc') == WED['order'], 'drag: dropping W-2041 on the board schedules it (%s)' % pill(pg))
        f.check(counts(pg, 'kc') == WED['order'], 'drag: the board shows the 3 batches')
        f.check(not errs, 'drag: no page errors')
        b.close()


PLAN = [('A day board by stage', 'L-1117'),
        ('An order becomes roast batches', 'B-303'),
        ('One schedule, three views', 'Week of Nov 16'),
        ('Stations filled by bag size', '96 bags'),
        ('A rush order shows what moves', '08:30 to 09:15')]

f = run_card(1, PLAN, ['B-305', '07:45 to 08:30', '96 bags'], start=start,
             extra={'after_step': {0: s1, 1: s2, 2: s3, 3: s4, 4: s5}, 'after': done})
drag(f)
keyboard_walk(f, 1, 5)
finish(f)
