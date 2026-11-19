#!/usr/bin/env python3
"""Card 3 (board): the README's numbers in Python, then the click through.
Run: python3 tools/food-brand-inventory/test_card3.py"""
import datetime as dt, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fb_tests import run_card, finish, js, ids, readonly_checks, keyboard_walk, clicks_only

DEL = dt.date(2026, 12, 1)
BB = {'LOT-A': dt.date(2027, 3, 6), 'LOT-B': dt.date(2027, 4, 20), 'LOT-C': dt.date(2027, 5, 30), 'LOT-D': dt.date(2027, 3, 21)}
RC = {'LOT-A': dt.date(2026, 9, 22), 'LOT-B': dt.date(2026, 10, 6), 'LOT-C': dt.date(2026, 9, 8), 'LOT-D': dt.date(2026, 10, 20)}
DAYS = {k: (v - DEL).days for k, v in BB.items()}
assert DAYS == {'LOT-A': 95, 'LOT-D': 110, 'LOT-B': 140, 'LOT-C': 180}           # remaining days at delivery
FIFO = sorted(RC, key=RC.get)
FEFO = sorted(BB, key=BB.get)
assert FIFO == ['LOT-C', 'LOT-A', 'LOT-B', 'LOT-D'] and FEFO == ['LOT-A', 'LOT-D', 'LOT-B', 'LOT-C']
assert [DAYS[k] for k in FEFO] == sorted(DAYS.values())                          # FEFO order is ascending remaining days
QUAL = [k for k in FEFO if DAYS[k] >= 120]
assert set(QUAL) == {'LOT-B', 'LOT-C'} and {k for k in DAYS if DAYS[k] < 120} == {'LOT-A', 'LOT-D'}   # qualifying lots are exactly those at or above 120
assert QUAL[0] == min(QUAL, key=DAYS.get) == 'LOT-B'                             # first pick is the lowest qualifying remaining days
HELD = {'LOT-B'}
assert [k for k in QUAL if k not in HELD][0] == 'LOT-C'                          # holding LOT-B moves the pick list to LOT-C


def order(pg):
    return js(pg, "return [].map.call(r.querySelectorAll('#rank .lt'),function(e){return e.id.slice(2)}).join(',')")


def start(pg, f, when='start'):
    readonly_checks(pg, f, {'iac': 'Greenfield Grocers', 'imr': '120 days'}, when)
    f.check(order(pg) == ','.join(FIFO), '%s: lots on hand in received order (FIFO) %s' % (when, order(pg)))
    t = js(pg, "return r.querySelector('.g3').innerText")
    f.check(js(pg, "return r.querySelectorAll('.lt.q,.lt.n,.pl .row:not(.acc .row),#rch,.c-flag').length") == 0 and 'Qualifies' not in t, '%s: no rule, no qualifying marks, no pick list yet' % when)


def s1(pg, f):
    f.check(order(pg) == ','.join(FEFO), 'step 1: FEFO order A, D, B, C (%s)' % order(pg))
    f.check(ids(pg, 'd-LOT-A', 'd-LOT-D', 'd-LOT-B', 'd-LOT-C') == '95|110|140|180', 'step 1: 95, 110, 140, 180 days at delivery')


def s2(pg, f):
    f.check(ids(pg, 'rch') == 'Rule on SO-4471: 120 days or more', 'step 2: the 120 day rule is on the order')


def s3(pg, f):
    q = js(pg, "return [].map.call(r.querySelectorAll('#rank .lt.q'),function(e){return e.id.slice(2)}).join(',')")
    n = js(pg, "return [].map.call(r.querySelectorAll('#rank .lt.n'),function(e){return e.id.slice(2)}).join(',')")
    f.check(q == 'LOT-B,LOT-C' and n == 'LOT-A,LOT-D', 'step 3: B and C green, A and D gray (%s / %s)' % (q, n))
    f.check(js(pg, "return r.querySelector('#p-0 b').textContent") == 'LOT-B' and ids(pg, 'pq-0', 'pqt') == '800|800', 'step 3: the pick list starts with LOT-B, 800 cases')


def s4(pg, f):
    fl = js(pg, "return [].map.call(r.querySelectorAll('.c-flag[id]'),function(e){return e.id.slice(3)}).sort().join(',')")
    f.check(fl == 'LOT-A,LOT-D', 'step 4: short dated flags on LOT-A and LOT-D only (%s)' % fl)


def s5(pg, f):
    picks = js(pg, "return [].map.call(r.querySelectorAll('.pl .row[id] b'),function(e){return e.textContent}).join(',')")
    f.check(picks == 'LOT-C' and ids(pg, 'pq-0') == '800', 'step 5: pick list moves to LOT-C, 800 cases (%s)' % picks)
    f.check('LOT-B' not in picks and js(pg, "return r.querySelector('#c3 #l-LOT-B')!==null&&r.querySelector('#rank #l-LOT-B')===null"), 'step 5: no held lot in the pick list, LOT-B sits in On hold')


PLAN = [('Lots ranked by best before date', 'LOT-A'),
        ('The account minimum goes on the order', '120 days or more'),
        ('Only lots the retailer will accept', 'Qualifies'),
        ('Short dated lots carry a flag', 'Short dated'),
        ('A held lot leaves the pick list', 'On hold')]
f = run_card(3, PLAN, ['LOT-C', '800', '180', 'Short dated', 'On hold'], start=start,
             extra={'after_step': {0: s1, 1: s2, 2: s3, 3: s4, 4: s5}})
keyboard_walk(f, 3, 5)
clicks_only(f, 3, 0)
clicks_only(f, 3, 0, 358, 390)
finish(f)
