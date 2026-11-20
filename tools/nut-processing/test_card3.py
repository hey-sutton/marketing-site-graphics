#!/usr/bin/env python3
"""Card 3 (list and detail): the README's bin and lot numbers in Python, then the click through.
Run: python3 tools/nut-processing/test_card3.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from np_tests import run_card, finish, js, ids, readonly_checks, keyboard_walk, clicks_only

B101, B102 = 4000, 3000
BLEND = B101 + B102
assert BLEND == 7000                                                     # blend weight = sum of the bins
assert (round(B101 / BLEND * 100, 1), round(B102 / BLEND * 100, 1)) == (57.1, 42.9)
RETAIL, BULK = 1000 * 5, 2000
assert RETAIL == 5000 and RETAIL + BULK == 7000                         # retail plus bulk = 7,000 lb
TRACE = ['NP-0711', 'NP-0709']
CUS = [400, 350, 250]
assert sum(CUS) == 1000 and len(CUS) == 3


def start(pg, f, when='start'):
    readonly_checks(pg, f, {'ibn': 'B-101'}, when)
    f.check(js(pg, "return r.querySelectorAll('.ls .row,.lt,.rm').length") == 0, '%s: no bins or lots shown' % when)
    t = js(pg, "return r.querySelector('.g3').innerText")
    f.check(not any(s in t for s in ('4,000', 'L-A', 'NP-0711', '7,000')), '%s: nothing derived shows' % when)


def s1(pg, f):
    f.check(ids(pg, 'ltl') == '4,000' and 'L-A' in ids(pg, 'lt') and 'NP-0711' in ids(pg, 'lt'), 'step 1: B-101 holds 4,000 lb of L-A from NP-0711')
    f.check(ids(pg, 'rheld') == '7,000', 'step 1: 7,000 lb held in the room')


def s2(pg, f):
    f.check(ids(pg, 'bt', 'sh-L-A', 'sh-L-B', 'bcal') == '7,000|57.1%|42.9%|4,000 + 3,000 = 7,000 lb', 'step 2: blend 7,000 lb at 57.1% and 42.9%')
    f.check(ids(pg, 'rbin', 'rheld') == '7,000|7,000', 'step 2: weight held unchanged')


def s3(pg, f):
    num = lambda x: int(x.replace(',', ''))
    r, k, t = (num(ids(pg, x)) for x in ('rlb', 'klb', 'stl'))
    f.check((r, k, t) == (5000, 2000, 7000) and r + k == t, 'step 3: retail %d + bulk %d = %d' % (r, k, t))
    f.check(ids(pg, 'rbin', 'rpk', 'rheld') == '0|7,000|7,000', 'step 3: all 7,000 lb now packed')


def s4(pg, f):
    tr = ids(pg, 'tr')
    f.check(all(d in tr for d in TRACE) and 'B-200' in tr and 'B-101' in tr and 'B-102' in tr, 'step 4: trace lists both raw deliveries')
    f.check(ids(pg, 'd0', 'd1').count('NP-07') == 2, 'step 4: two raw delivery nodes')


def s5(pg, f):
    f.check(js(pg, "return r.querySelectorAll('#cu .row:not(.h):not(.sm)').length") == 3, 'step 5: 3 customers')
    f.check(ids(pg, 'cq', 'clb') == '1,000|5,000', 'step 5: 1,000 packs, 5,000 lb shipped')


PLAN = [('A bulk bin and the lots it holds', 'L-A'),
        ('A blend forms a new lot', '57.1%'),
        ('A split into retail and bulk', 'BK-2210'),
        ('A packed lot traced to its deliveries', 'NP-0709'),
        ('Every customer who received the lot', 'Pinecrest Snack Co.')]
f = run_card(3, PLAN, ['NP-0711', 'NP-0709', '1,000', 'Morning Trail Granola', 'Sunbank Grocers'], start=start,
             extra={'after_step': {0: s1, 1: s2, 2: s3, 3: s4, 4: s5}})
keyboard_walk(f, 3, 5)
clicks_only(f, 3, 0)
clicks_only(f, 3, 0, 358, 390)
finish(f)
