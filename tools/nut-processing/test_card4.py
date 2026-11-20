#!/usr/bin/env python3
"""Card 4 (board): the README's cleaning minutes in Python, then the click through.
Run: python3 tools/nut-processing/test_card4.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from np_tests import run_card, finish, js, ids, readonly_checks, keyboard_walk, clicks_only

G = {'R1': 'F', 'R2': 'P', 'R3': 'T', 'R4': 'F'}
CLEAN = {'FF': 15, 'FT': 30, 'TF': 45, 'FP': 60, 'PF': 120, 'PT': 120, 'TP': 45}
legs = lambda o: [CLEAN[G[a] + G[b]] for a, b in zip(o, o[1:])]
CUR, NEW = ['R1', 'R3', 'R4', 'R2'], ['R1', 'R2', 'R3', 'R4']
assert legs(CUR) == [30, 45, 60] and sum(legs(CUR)) == 135                # start order total
assert legs(NEW) == [60, 120, 45] and sum(legs(NEW)) == 225               # after the move
assert sum(legs(NEW)) - sum(legs(CUR)) == 90                              # extra = 225 - 135


def order(pg):
    return js(pg, "return [].map.call(r.querySelectorAll('.wk .rn'),function(e){return e.id.slice(2)})")


def r3_disabled(pg):
    return js(pg, "return r.getElementById('r3b').disabled")


def start(pg, f, when='start'):
    readonly_checks(pg, f, {'iln': 'Line 1'}, when)
    f.check(js(pg, "return r.querySelectorAll('.rn,.po,.ck').length") == 0, '%s: no runs, preview or cleaning shown' % when)
    t = js(pg, "return r.querySelector('.g4').innerText")
    f.check(not any(s in t for s in ('135', 'R1', 'Peanut', '30 min', 'Free from')), '%s: nothing derived shows' % when)


def s1(pg, f):
    f.check(order(pg) == CUR, 'step 1: board order R1, R3, R4, R2 %s' % order(pg))
    f.check(js(pg, "return r.querySelectorAll('.ag .ch').length") == 0, 'step 1: groups not shown yet')


def s2(pg, f):
    readonly_checks(pg, f, {'iln': 'Line 1', 'isb': 'D. Moreno'}, 'step 2')
    f.check(ids(pg, 'g-R1', 'g-R3', 'g-R4', 'g-R2') == 'Free from|Tree nut|Free from|Peanut', 'step 2: allergen group on every run')
    f.check(ids(pg, 'cm1', 'cm2', 'cm3', 'ctot') == '30 min clean|45 min clean|60 min clean|Cleaning 135 min', 'step 2: 30 + 45 + 60 = 135')
    f.check(r3_disabled(pg) and ids(pg, 'r3s') == 'Blocked', 'step 2: R3 blocked before the sign off')


def s3(pg, f):
    f.check(ids(pg, 'pcur', 'pnew', 'pext') == '135 min|225 min|+90 min', 'step 3: 135 now, 225 after, +90 shown')
    f.check(order(pg) == CUR and ids(pg, 'ctot') == 'Cleaning 135 min', 'step 3: not committed, board order and total unchanged')
    f.check(r3_disabled(pg), 'step 3: R3 still blocked')


def s4(pg, f):
    f.check(not r3_disabled(pg) and ids(pg, 'r3s', 'cst') == 'Ready|Signed', 'step 4: the sign off enables R3')


def s5(pg, f):
    f.check(ids(pg, 'r3s', 'r4s') == 'Running|Blocked', 'step 5: R3 running, R4 blocked until its cleaning is signed')
    f.check('45 min' in ids(pg, 'nnt'), 'step 5: next cleaning is tree nut to free from, 45 min')


PLAN = [('A week schedule by line', 'Seed and fruit mix'),
        ('The allergen group of every run', 'Cleaning 135 min'),
        ('A move shows its extra cleaning first', '+90 min'),
        ('A changeover cleaning with a sign off', 'Signed off'),
        ('A run waits for the cleaning before it', 'Running')]
f = run_card(4, PLAN, ['135 min', '225 min', '+90 min', 'Signed'], start=start,
             extra={'after_step': {0: s1, 1: s2, 2: s3, 3: s4, 4: s5}})
keyboard_walk(f, 4, 5)
clicks_only(f, 4, 0)
clicks_only(f, 4, 0, 358, 390)
finish(f)
