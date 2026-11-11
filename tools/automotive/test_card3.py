#!/usr/bin/env python3
"""Card 3 (week board with capacity line): the brief's numbers in Python, then the click through.
Run: python3 tools/automotive/test_card3.py"""
import os, sys
from itertools import accumulate
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from auto_tests import run_card, finish, js

# ---- the brief's numbers, derived independently of the card ----
DEM = [600, 600, 800, 800, 600]
CAP = 700
PLAN_BRIEF = [700, 700, 700, 700, 600]
assert sum(DEM) == 3400 and sum(PLAN_BRIEF) == sum(DEM)          # plan total = demand total
assert all(p <= CAP for p in PLAN_BRIEF)
REQ, BUILT = list(accumulate(DEM)), list(accumulate(PLAN_BRIEF))
assert REQ == [600, 1200, 2000, 2800, 3400] and BUILT == [700, 1400, 2100, 2800, 3400]
assert all(b >= q for b, q in zip(BUILT, REQ))                     # built never below required
assert [p - d for p, d in zip(PLAN_BRIEF, DEM)][:2] == [100, 100]   # 100 pulled forward on Mon and Tue
NEED = sum(PLAN_BRIEF) * 2
assert NEED == 6800 and NEED - 5200 == 1600
OTHER = {'STP-300': (1, 4000), 'WSH-044': (2, 7500), 'BSH-07': (1, 3600), 'LBL-12': (1, 5000)}
assert all(q * 3400 <= s for q, s in OTHER.values())               # only FST-121 is short


def ids(pg, *names):
    return js(pg, "return %r.map(function(i){var e=r.getElementById(i);return e?e.textContent:null}).join('|')" % list(names))


def start(pg, f, when='start'):
    t = js(pg, "return r.querySelector('.g3').innerText")
    f.check(js(pg, "return !!r.getElementById('imp')&&!!r.querySelector('.cap7')&&r.querySelectorAll('.br b').length===0"), '%s: empty week board with the capacity line and Import release' % when)
    f.check(all(d in t for d in ('Dec 7', 'Dec 11')), '%s: the board shows Dec 7 to Dec 11' % when)
    f.check('3,400' not in t and 'REL-' not in t and 'FST-121' not in t, '%s: nothing from the release shows' % when)


def s1(pg, f):
    t = js(pg, "return r.getElementById('rel').innerText")
    f.check('REL-4410' in t and '3,400 pcs' in t and js(pg, "return r.querySelectorAll('.br b').length") == 0, 'step 1: REL-4410 for 3,400 in the inbox, the board still empty')


def s2(pg, f):
    f.check(ids(pg, 'dm0', 'dm1', 'dm2', 'dm3', 'dm4') == '600|600|800|800|600', 'step 2: demand Mon 600, Tue 600, Wed 800, Thu 800, Fri 600')
    f.check(ids(pg, 'flg') == 'Wed and Thu over by 100', 'step 2: Wed and Thu flagged over capacity')


def s3(pg, f):
    f.check(ids(pg, 'pl0', 'pl1', 'pl2', 'pl3', 'pl4') == '700|700|700|700|600', 'step 3: plan 700, 700, 700, 700, 600')
    f.check(ids(pg, 'pst', 'flg') == 'Plan 3,400 of 3,400|100 built ahead Mon and Tue', 'step 3: plan 3,400 of 3,400, 100 built ahead')
    rows = js(pg, "return [].map.call(r.querySelectorAll('.gt .row'),function(x){return x.innerText.replace(/\\s+/g,' ').trim();})")
    f.check('Cum. required 600 1,200 2,000 2,800 3,400' in rows and 'Cum. built 700 1,400 2,100 2,800 3,400' in rows, 'step 3: cumulative rows')
    f.check('Ahead of release 100 200 100 0 0' in rows, 'step 3: built is never below required')


def s4(pg, f):
    f.check(ids(pg, 'nd-FST-121', 'sh-FST-121', 'msh') == '6,800|1,600|1 short', 'step 4: FST-121 needs 6,800, short 1,600')
    f.check(ids(pg, 'sh-STP-300', 'sh-WSH-044', 'sh-BSH-07', 'sh-LBL-12') == '0|0|0|0', 'step 4: no other line short')


def s5(pg, f):
    f.check(ids(pg, 'poq') == '1,600 pcs from Ridgefield Fasteners' and 'Due Mon Dec 7' in js(pg, "return r.getElementById('mat').innerText"), 'step 5: PO draft for 1,600, due Monday')


PLAN = [('A customer release arrives with its daily quantities', 'REL-4410'),
        ('Demand lands on the week board against the capacity line', 'Wed and Thu over by 100'),
        ('The plan builds ahead so no day goes over capacity', 'Plan 3,400 of 3,400'),
        ('Every BOM line is checked against stock for the week', '1,600'),
        ('The shortage becomes a purchase order in one click', 'PO draft, FST-121')]

f = run_card(3, PLAN, ['Plan 3,400 of 3,400', '6,800', '1,600 pcs from Ridgefield Fasteners'], start=start,
             extra={'after_step': {0: s1, 1: s2, 2: s3, 3: s4, 4: s5}})
finish(f)
