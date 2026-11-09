#!/usr/bin/env python3
"""Card 4 Estimated vs Actual Job Margin: click through (both modes), every figure, layout, variety, navigation, phone and
typing checks. Run: python3 tools/furniture-woodworking/test_card4.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from furniture_tests import run_all, js, start_rule, typed
import card4

R = card4.RATE
est = {s[0]: s[2][0] + s[2][1] * R + s[2][2] for s in card4.SUBS}
act = {s[0]: s[3][0] + s[3][1] * R + s[3][2] for s in card4.SUBS}
rev = {s[0]: s[1] for s in card4.SUBS}
assert est == {'Kitchen': 33340, 'Primary closet': 11140, 'Mudroom': 5760}
assert act == {'Kitchen': 36486, 'Primary closet': 10568, 'Mudroom': 6374}
assert [s[2][1] * R for s in card4.SUBS] == [11440, 3640, 2080] and [s[3][1] * R for s in card4.SUBS] == [12896, 3328, 2444]
pm = lambda r, c: round((r - c) / r * 100, 1)
assert [pm(rev[k], est[k]) for k in est] == [35.9, 39.8, 41.2] and [pm(rev[k], act[k]) for k in act] == [29.8, 42.9, 35.0]
assert [rev[k] - est[k] for k in est] == [18660, 7360, 4040] and [rev[k] - act[k] for k in act] == [15514, 7932, 3426]
RV, E, A = sum(rev.values()), sum(est.values()), sum(act.values())
assert (RV, E, A, RV - E, RV - A, A - E) == (80300, 50240, 53428, 30060, 26872, 3188) and pm(RV, E) == 37.4 and pm(RV, A) == 33.5
k = card4.SUBS[0]
assert (k[3][0] - k[2][0], (k[3][1] - k[2][1]) * R, k[3][2] - k[2][2]) == (1550, 1456, 140) and 1550 + 1456 + 140 == 3146 == 36486 - 33340
assert sum(d[2] for d in card4.DEPTS) == 248 and sum(d[1] for d in card4.DEPTS) == 220 and [d[2] - d[1] for d in card4.DEPTS] == [6, 8, 6, 8]
assert sum(x[3] for x in card4.BUILD_LOG) + card4.BUILD_REST[1] == 74


def start(pg, f):
    start_rule(pg, f, ['$', '%', 'Kitchen', '3,188'])
    f.check(js(pg, "return r.getElementById('ip').value") == '', 'start: the project field is empty')


def load(pg, f):
    js(pg, "var e=r.getElementById('ip');e.value='P-9';e.dispatchEvent(new Event('input',{bubbles:true}))")
    pg.locator('#cv .hint').first.click(); pg.wait_for_timeout(400)
    f.check(js(pg, "return r.getElementById('fp').classList.contains('err')"), 'step 2: an unknown project shows an inline error')
    js(pg, "var e=r.getElementById('ip');e.value='';e.dispatchEvent(new Event('input',{bubbles:true}))")


def chips(pg, f):
    got = js(pg, "return [0,1,2].map(function(i){return r.getElementById('mc-'+i).textContent}).join('|')")
    f.check(got == '35.9% to 29.8%|39.8% to 42.9%|41.2% to 35.0%', 'step 3: margin chips per sub job (%s)' % got)


def totals(pg, f):
    f.check(js(pg, "return r.getElementById('pm').textContent+'|'+r.getElementById('gap').textContent") == '37.4% to 33.5%|$3,188 over', 'step 4: 37.4% to 33.5%, $3,188 over')


def var(pg, f):
    got = js(pg, "return ['vv-0','vv-1','vv-2','vt'].map(function(i){return r.getElementById(i).textContent}).join('|')")
    f.check(got == '+$1,550|+$1,456|+$140|+$3,146', 'step 5: Kitchen +$1,550, +$1,456, +$140 = +$3,146 (%s)' % got)


def labor(pg, f):
    f.check(js(pg, "return ['lte','lta','lto'].map(function(i){return r.getElementById(i).textContent}).join('|')") == '220 h|248 h|+28 h', 'step 6: 220 h estimated, 248 h actual, +28 h')


def end(pg, f):
    f.check(js(pg, "return r.getElementById('g-c').classList.contains('win')"), 'end: the Primary closet bars are highlighted green')


PLAN = [('Pick a project to see how it really went', 'P-0409'),
        ('Estimate and actual, side by side', '36,486'),
        ('The project ran $3,188 over', '37.4% to 33.5%'),
        ('The Kitchen is where the margin went', '+$3,146'),
        ('Labor shows which departments ran long', '248 h'),
        ('Build ran eight hours over', '74 h, 11 entries'),
        ('Some jobs beat the estimate. Now you know which', '42.9%')]

f = run_all(4, PLAN, ['42.9%', '$3,188 over', '37.4% to 33.5%'], extra={'before': {0: start, 1: load, 2: chips, 3: totals, 4: var, 5: labor}, 'after': end},
            more=lambda f: typed(4, f, 1, 'ip', 'P-0412', 'Project margin', "return !!r.getElementById('g-k')"))
print('\n%d failures' % len(f)); sys.exit(1 if f else 0)
