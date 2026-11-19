#!/usr/bin/env python3
"""Card 3 (board): the README's numbers in Python, then the click through.
Run: python3 tools/functional-beverage/test_card3.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fv_tests import run_card, finish, js, ids, readonly_checks, keyboard_walk, clicks_only

M = '−'
V7 = [9, 12, 38, 25]
V8 = [7, 9, 38, 25]
assert sum(V7) == 84 and sum(V8) == 79                             # $0.84 and $0.79 a can
assert sum(V8) - sum(V7) == -5                                     # cost change = v8 minus v7
assert round((sum(V8) - sum(V7)) / sum(V7) * 100, 1) == -6.0       # minus 6.0 percent, rounded


def start(pg, f, when='start'):
    readonly_checks(pg, f, {'ifm': 'Focus Citrus Sparkling'}, when)
    t = js(pg, "return r.querySelector('.g3').innerText")
    f.check(js(pg, "return r.querySelectorAll('.vc,.hk').length") == 0, '%s: board columns empty' % when)
    f.check(not any(s in t for s in ('v7', 'v8', '$0.', 'Stevia')), '%s: nothing derived shows' % when)


def col(pg, cid):
    return js(pg, "return [].map.call(r.querySelectorAll('#%s .vc'),function(e){return e.id.slice(3)}).join(',')" % cid)


def s1(pg, f):
    f.check(col(pg, 'c2') == 'v7' and col(pg, 'c3') == 'v8' and col(pg, 'c1') == '', 'step 1: v7 in production, v8 draft beside it')


def s2(pg, f):
    add = js(pg, "return [].map.call(r.querySelectorAll('#vc-v8 .row.add span:first-child'),function(e){return e.textContent}).join(',')")
    rem = js(pg, "return [].map.call(r.querySelectorAll('#vc-v7 .row.rem span:first-child'),function(e){return e.textContent}).join(',')")
    chg = js(pg, "return [].map.call(r.querySelectorAll('#vc-v8 .row.chg'),function(e){return e.innerText.replace(/\\s+/g,' ')}).join(',')")
    f.check(add == 'Stevia leaf extract' and rem == 'Cane sugar' and chg == 'Natural citrus flavor 0.6%', 'step 2: stevia added, cane sugar removed, flavor 0.8%% to 0.6%% (%s / %s / %s)' % (add, rem, chg))


def s3(pg, f):
    f.check(ids(pg, 'cpc-v7', 'cpc-v8', 's7', 's8', 'sdc', 'spc') == '$0.84|$0.79|$0.84|$0.79|%s$0.05|%s6.0%%' % (M, M), 'step 3: $0.84 against $0.79, change minus $0.05 (minus 6.0%)')


def s4(pg, f):
    f.check(col(pg, 'c2') == 'v8' and js(pg, "return r.querySelectorAll('#c2 .vc').length") == 1, 'step 4: exactly one version in production, v8')
    f.check(col(pg, 'c1') == 'v7' and 'Nov 19, 2026' in ids(pg, 'h7') and col(pg, 'c3') == '', 'step 4: v7 in history with its dates, no draft left')


def s5(pg, f):
    f.check(ids(pg, 'hct') == '3 versions' and js(pg, "return !!r.getElementById('h-v6')&&!!r.getElementById('h-v5')&&!!r.getElementById('h7')"), 'step 5: v7, v6 and v5 in history')


PLAN = [('Production beside the draft', 'v8'),
        ('What changed from production', 'Stevia leaf extract'),
        ('Cost per can for each version', '$0.79'),
        ('Approval promotes the draft', 'v8 in production'),
        ('Every earlier version, kept', 'v5')]
f = run_card(3, PLAN, ['$0.84', '$0.79', '6.0%', 'v6', 'v7'], start=start,
             extra={'after_step': {0: s1, 1: s2, 2: s3, 3: s4, 4: s5}})
keyboard_walk(f, 3, 5)
clicks_only(f, 3, 0)
clicks_only(f, 3, 0, 358, 390)
finish(f)
