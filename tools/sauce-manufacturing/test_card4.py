#!/usr/bin/env python3
"""Card 4 (board): the README's trace and allergen rules in Python, then the click through.
Run: python3 tools/sauce-manufacturing/test_card4.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sm_tests import run_card, finish, js, ids, readonly_checks, keyboard_walk, clicks_only

BAT = ['SP-2283', 'SP-2286', 'SP-2291']
FLS = [('FL-9088', 'SP-2283', 'Harbor Market Co.'), ('FL-9089', 'SP-2283', 'Pine Street Co-op'), ('FL-9094', 'SP-2286', 'Harbor Market Co.'),
       ('FL-9095', 'SP-2286', 'Northway Foods'), ('FL-9101', 'SP-2291', 'Elm Grove Grocers')]
assert len(BAT) == 3 and len(FLS) == 5 and {b for _, b, _ in FLS} == set(BAT)
CUST = sorted({c for *_, c in FLS})
assert len(CUST) == 4                                              # the customer list equals the customers of the filled lots
ING = {'Soy sauce': {'soy'}, 'Sesame spice blend': {'sesame'}, 'Rice vinegar': set(), 'Brown sugar syrup': set()}
CONTAINS = sorted(set().union(*ING.values()))
assert CONTAINS == ['sesame', 'soy']                               # Contains = union of ingredient allergens
NEXT = sorted(set(CONTAINS) | {'peanut'})


def differs(a, b):
    return sorted(a) != sorted(b)


assert differs(CONTAINS, NEXT) and not differs(CONTAINS, ['soy', 'sesame'])   # warning only when the set differs


def start(pg, f, when='start'):
    readonly_checks(pg, f, {'ilt': 'SP-LOT-5530'}, when)
    t = js(pg, "return r.getElementById('brd').innerText+r.getElementById('ru').innerText")
    f.check(js(pg, "return r.querySelectorAll('.col .k,#wn,#clk').length") == 0, '%s: board columns empty, no warning, no cleaning' % when)
    f.check(not any(s in t for s in ('SP-22', 'FL-9', 'Harbor', 'Contains:')), '%s: nothing derived from the lot shows' % when)


def s1(pg, f):
    f.check('SP-LOT-5530' in js(pg, "return r.querySelector('.k.l').innerText"), 'step 1: the lot card shows')


def s2(pg, f):
    b = js(pg, "return [].map.call(r.querySelectorAll('[id^=b-SP]'),function(e){return e.id.slice(2)}).join(',')")
    fl = js(pg, "return [].map.call(r.querySelectorAll('[id^=f-FL]'),function(e){return e.id.slice(2)}).join(',')")
    f.check(b == ','.join(BAT) and fl == ','.join(x[0] for x in FLS) and ids(pg, 'nb', 'nf') == '3|5', 'step 2: 3 batches and 5 filled lots in their columns')


def s3(pg, f):
    c = sorted(js(pg, "return [].map.call(r.querySelectorAll('.k.cu b'),function(e){return e.textContent})"))
    f.check(c == CUST and ids(pg, 'nc') == '4', 'step 3: the 4 customers of the filled lots (%s)' % c)


def s4(pg, f):
    f.check(ids(pg, 'ctn') == 'Contains: Sesame, Soy', 'step 4: Contains statement is the union, sesame and soy')
    f.check(ids(pg, 'ra-0', 'ra-1', 'ra-2') == 'sesamesoy|sesamesoy|sesamesoy', 'step 4: the flags reach base sauce, flavored sauce and jar')


def s5b(pg, f):
    f.check(js(pg, "return r.getElementById('wn')") is None, 'step 5: no warning before the check')
    pg.locator('#cv #ncb').click(); pg.wait_for_timeout(400)
    f.check('adds peanut' in (ids(pg, 'wn') or '') and js(pg, "var h=r.querySelector('.hint');return h&&h.id") == 'lcb', 'step 5: the changed set warns (adds peanut), prompt moves to Log cleaning')


def s5(pg, f):
    f.check(js(pg, "return !!r.getElementById('clk')") and 'Cleared to run' in js(pg, "return r.getElementById('rn').innerText"), 'step 5: cleaning card on the board, SP-2296 cleared to run')


PLAN = [('One ingredient lot', 'SP-LOT-5530'),
        ('Every batch and filled lot that used it', 'FL-9101'),
        ('The customers who received those lots', 'Elm Grove Grocers'),
        ('Allergens roll up to the finished jar', 'Contains: Sesame, Soy'),
        ('A changed allergen set needs a cleaning', 'Cleaning')]
f = run_card(4, PLAN, ['SP-2291', 'FL-9095', 'Northway Foods', 'Contains: Sesame, Soy', 'peanut', 'Logged'], start=start,
             extra={'before': {4: s5b}, 'after_step': {0: s1, 1: s2, 2: s3, 3: s4, 4: s5}})
keyboard_walk(f, 4, 5)
clicks_only(f, 4, 1)
clicks_only(f, 4, 1, 358, 390)
finish(f)
