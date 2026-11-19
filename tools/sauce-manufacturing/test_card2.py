#!/usr/bin/env python3
"""Card 2 (stage chain): the README's limits in Python, then the click through.
Run: python3 tools/sauce-manufacturing/test_card2.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sm_tests import run_card, finish, js, ids, readonly_checks, keyboard_walk, clicks_only

LIM = {'temp': lambda v: v >= 190, 'ph': lambda v: v <= 4.2, 'brix': lambda v: 24 <= v <= 26}
RD = {'temp': 192, 'ph': 4.4, 'brix': 25}
FLAG = [k for k in RD if not LIM[k](RD[k])]
assert FLAG == ['ph']                                               # flagged only when outside its limit
assert LIM['ph'](4.2) and not LIM['ph'](4.3) and LIM['temp'](190) and not LIM['temp'](189) and LIM['brix'](24) and LIM['brix'](26) and not LIM['brix'](26.1)
WANT = {'i-temp': '192 F', 'i-ph': '4.4', 'i-brix': '25'}


def fill_disabled(pg):
    return js(pg, "var b=r.getElementById('fib');return !!b&&b.disabled")


def start(pg, f, when='start'):
    readonly_checks(pg, f, {}, when)
    f.check(js(pg, "return r.querySelectorAll('.stg:not(.e),.rds,.rec').length") == 0, '%s: chain and readings empty' % when)
    t = js(pg, "return r.getElementById('chn').innerText+r.getElementById('bot').innerText")
    f.check(not any(s in t for s in ('192', '4.4', 'Flagged', 'gal')), '%s: nothing derived shows' % when)


def s1(pg, f):
    f.check(ids(pg, 'bst') == 'In process' and 'Cooked' in js(pg, "return r.getElementById('chn').innerText"), 'step 1: SP-2291 opens in the chain')


def s2(pg, f):
    readonly_checks(pg, f, WANT, 'step 2')
    f.check(ids(pg, 'c-temp', 'c-ph', 'c-brix') == '192 F|4.4|25', 'step 2: readings 192 F, pH 4.4, Brix 25 on the stages')
    f.check(js(pg, "return r.querySelectorAll('.stg .c-bad:not(#fst)').length") == 0, 'step 2: nothing flagged before the check')


def s3(pg, f):
    bad = js(pg, "return [].map.call(r.querySelectorAll('[id^=c-].c-bad'),function(e){return e.id}).join(',')")
    ok = js(pg, "return [].map.call(r.querySelectorAll('[id^=c-].c-ok'),function(e){return e.id}).join(',')")
    f.check(bad == 'c-ph' and ok == 'c-temp,c-brix', 'step 3: only the pH chip is red (%s / %s)' % (bad, ok))
    f.check(ids(pg, 'bst', 'flc') == 'Flagged|1 outside limit' and fill_disabled(pg), 'step 3: batch flagged, Fill disabled')


def s4b(pg, f):
    pg.locator('#cv #hdb').click(); pg.wait_for_timeout(400)
    f.check(ids(pg, 'bst', 'fst') == 'On hold|Blocked' and fill_disabled(pg), 'step 4: on hold, Fill disabled')
    f.check(js(pg, "var h=r.querySelector('.hint');return h&&h.id") == 'srb', 'step 4: the prompt moves to Sign off and release')


def s4(pg, f):
    f.check(ids(pg, 'bst', 'fst') == 'Released|Ready' and not fill_disabled(pg), 'step 4: after the sign off the batch is Released and Fill is enabled')
    f.check(ids(pg, 'c-temp', 'c-ph', 'c-brix') == '192 F|4.4|25', 'step 4: the readings remain')


def s5(pg, f):
    f.check(ids(pg, 'rv-temp', 'rv-ph', 'rv-brix') == '192 F|4.4|25', 'step 5: the batch record keeps all three readings')
    t = js(pg, "return r.getElementById('rec').innerText")
    f.check('Outside' in t and t.count('Within') == 2 and 'Released' in t and 'Placed on hold' in t, 'step 5: limits, results, hold and release on one page')


PLAN = [('One batch through cook, hold and fill', '500 gal'),
        ('Temperature, pH and Brix on the batch', '4.4'),
        ('A reading outside its limit flags the batch', 'Flagged'),
        ('Hold, then release after a sign off', 'Released'),
        ('The full batch record on one page', 'Batch record')]
f = run_card(2, PLAN, ['192 F', '4.4', '25', 'Released', 'Outside'], start=start,
             extra={'before': {3: s4b}, 'after_step': {0: s1, 1: s2, 2: s3, 3: s4, 4: s5}})
keyboard_walk(f, 2, 5)
clicks_only(f, 2, 1)
clicks_only(f, 2, 1, 358, 390)
finish(f)
