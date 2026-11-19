#!/usr/bin/env python3
"""Card 2 (list and detail): the README's checks in Python, then the click through.
Run: python3 tools/functional-beverage/test_card2.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fv_tests import run_card, finish, js, ids, readonly_checks, keyboard_walk, clicks_only

SPEC_MIN = 5.0
PASS = lambda v: v >= SPEC_MIN                                     # passes only at or above the spec minimum
assert PASS(5.2) and PASS(5.0) and not PASS(4.6) and not PASS(4.99)
SUP = {'Verdant Botanicals': True, 'Sunmere Extracts': True, 'Halcyon Herb Co.': False}
assert sum(SUP.values()) == 2 and len(SUP) - sum(SUP.values()) == 1


def start(pg, f, when='start'):
    readonly_checks(pg, f, {}, when)
    t = js(pg, "return r.getElementById('dt').innerText")
    f.check(js(pg, "return r.querySelectorAll('.dt .sp,.dt .facts,.dt .cert,.bl .opt:not(.off)').length") == 0, '%s: no lot open, no certificate, no lot picker' % when)
    f.check(not any(s in t for s in ('5.2', 'COA', 'Pass')), '%s: nothing derived shows' % when)


def s1(pg, f):
    f.check(ids(pg, 'coa') == 'COA-7731' and 'Verdant Botanicals' in js(pg, "return r.getElementById('dt').innerText"), 'step 1: ASH-2291 received with COA-7731 from Verdant Botanicals')


def s2(pg, f):
    f.check(ids(pg, 'cv-0', 'cr-0', 'cr-1', 'cr-2') == '5.2%|Pass|Pass|Pass', 'step 2: 5.2% against 5.0% minimum passes, lead and moisture pass')


def s3b(pg, f):
    pg.locator('#cv #l-ASH-2305').click(); pg.wait_for_timeout(400)
    f.check(ids(pg, 'cv-0', 'cr-0') == '4.6%|Fail', 'step 3: ASH-2305 at 4.6% fails the 5.0% minimum')
    f.check(js(pg, "var h=r.querySelector('.hint');return h&&h.id") == 'hdb', 'step 3: the prompt moves to Hold lot')


def s3(pg, f):
    f.check('On hold' in js(pg, "return r.getElementById('l-ASH-2305').innerText") and 'cannot be picked' in (ids(pg, 'hno') or ''), 'step 3: ASH-2305 on hold')
    f.check(js(pg, "return r.getElementById('o-ASH-2305').className.indexOf('off')>=0&&r.getElementById('o-ASH-2305').innerText.indexOf('not selectable')>=0&&r.getElementById('o-ASH-2291').innerText.indexOf('Selectable')>=0"), 'step 3: the held lot is excluded from batch selection, ASH-2291 stays selectable')


def s4(pg, f):
    f.check(ids(pg, 'coa') == 'COA-7731' and 'Opened from batch FB-0412' in js(pg, "return r.querySelector('.cert').innerText"), 'step 4: the certificate opens from batch FB-0412')


def s5(pg, f):
    t = js(pg, "return r.querySelector('.su').innerText")
    f.check(t.count('Not approved') == 1 and t.count('Approved') == 2 and '2 approved, 1 not approved' in ids(pg, 'sno'), 'step 5: 2 approved, 1 not approved')


PLAN = [('A lot received with its certificate', 'COA-7731'),
        ('Certificate values beside the spec', '5.2%'),
        ('An out of spec lot goes on hold', 'On hold'),
        ('The certificate, from the batch that used it', 'Opened from batch FB-0412'),
        ('Approved suppliers for the ingredient', 'Not approved')]
f = run_card(2, PLAN, ['Verdant Botanicals', 'Sunmere Extracts', 'Halcyon Herb Co.', 'Held, not selectable'], start=start,
             extra={'before': {2: s3b}, 'after_step': {0: s1, 1: s2, 2: s3, 3: s4, 4: s5}})
keyboard_walk(f, 2, 5)
clicks_only(f, 2, 1)
clicks_only(f, 2, 1, 358, 390)
finish(f)
