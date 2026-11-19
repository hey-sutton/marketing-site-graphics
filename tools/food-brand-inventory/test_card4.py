#!/usr/bin/env python3
"""Card 4 (stage chain): the README's numbers in Python, then the click through.
Run: python3 tools/food-brand-inventory/test_card4.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fb_tests import run_card, finish, js, ids, readonly_checks, keyboard_walk, clicks_only

M = '−'   # minus sign for negative quantities
OH, DEM, SS, LEAD, WK = 12000, 4000, 2000, 3, 6
LOC = {'wh': (4000, 1000), 'cp': (8000, 3000), 'tp': (0, 0)}
assert sum(o for o, _ in LOC.values()) == OH and sum(d for _, d in LOC.values()) == DEM
assert 2500 + 1500 == DEM                                          # sales orders plus EDI orders a week
PROJ = [OH - DEM * w for w in range(1, WK + 1)]                    # weekly projection = on hand less cumulative demand
assert PROJ[:4] == [8000, 4000, 0, -4000] and PROJ[3] < 0
for w in range(1, WK + 1):
    assert sum(o - d * w for o, d in LOC.values()) == PROJ[w - 1]  # the location rows add up to the item row
FIRST = next(w for w, v in enumerate(PROJ, 1) if v < SS)
assert FIRST == 3                                                  # the first week under safety stock is week 3
assert FIRST - LEAD == 0                                           # 3 week lead time: order this week
PO = DEM * WK + SS - OH
assert PO == 24000 + 2000 - 12000 == 14000                         # draft PO quantity
AFTER = [v + (PO if w >= LEAD else 0) for w, v in enumerate(PROJ, 1)]
assert AFTER[LEAD - 1] == PROJ[LEAD - 1] + 14000 == 14000          # balance after receipt = prior balance plus 14,000
assert AFTER[-1] == SS                                             # six weeks later the pouch ends at its safety stock
assert [OH, OH - 24000, OH - 24000 - SS, OH - 24000 - SS + PO] == [12000, -12000, -14000, 0]   # running totals in the chain


def sg(n):
    return (M if n < 0 else '') + format(abs(n), ',')


def start(pg, f, when='start'):
    readonly_checks(pg, f, {'ibc': 'PO-7760'}, when)
    t = js(pg, "return r.querySelector('.chain').innerText+'|'+r.querySelector('.bot').innerText")
    f.check(js(pg, "return r.querySelectorAll('.stg b,.stg .run,#flg,.it .row.sub,#rcd,.tl').length") == 0, '%s: the chain is empty, no shortage flag, no PO, no receipt' % when)
    f.check(not any(s in t for s in ('12,000', '14,000', '24,000', 'Week 3')), '%s: nothing derived shows in the chain or the action cards' % when)


def s1(pg, f):
    f.check(ids(pg, *['w-pouch-%d' % w for w in range(1, 7)]) == '|'.join(sg(v) for v in PROJ), 'step 1: pouch 8,000, 4,000, 0, then below zero')
    f.check(ids(pg, 'flg') == 'Short wk 3', 'step 1: the pouch carries the week 3 shortage flag')


def s2(pg, f):
    for k, (o, d) in enumerate(LOC.values()):
        f.check(ids(pg, *['l%d-%d' % (k, w) for w in range(1, 7)]) == '|'.join(sg(o - d * w) for w in range(1, 7)), 'step 2: location row %d projects on hand less cumulative demand' % k)
    f.check(ids(pg, 'k-oh', 'k-dm', 'k-ss', 'r1', 'r2', 'r3') == '12,000|%s24,000|%s2,000|12,000|%s12,000|%s14,000' % (M, M, M, M), 'step 2: chain 12,000, demand 24,000, safety 2,000, running to 14,000 short')


def s3(pg, f):
    f.check(ids(pg, 'ltw', 'ndw', 'obw') == '3 weeks|Week 3|This week', 'step 3: lead time 3 weeks, needed week 3, order this week')


def s4(pg, f):
    f.check(ids(pg, 'poq', 'k-po', 'r4') == '14,000|+14,000|0', 'step 4: draft PO 14,000 closes the gap to 0')
    f.check(ids(pg, 'pom') == '24,000 + 2,000 %s 12,000 = 14,000' % M, 'step 4: 24,000 + 2,000 less 12,000 = 14,000')


def s5(pg, f):
    f.check(ids(pg, 'bb', 'ba', 'k-rc') == '0|14,000|14,000', 'step 5: week 3 balance 0 to 14,000 after the scan')
    f.check(ids(pg, *['w-pouch-%d' % w for w in range(1, 7)]) == '|'.join(sg(v) for v in AFTER), 'step 5: weeks 3 to 6 rise by 14,000, week 6 ends at 2,000')


PLAN = [('Weekly availability for every location', 'Wk 6'),
        ('A projected shortage on a packaging item', '24,000'),
        ('Lead time against the date needed', 'This week'),
        ('The shortage becomes a draft PO', '14,000'),
        ('Received by barcode', 'Received')]
f = run_card(4, PLAN, ['12,000', '14,000', '24,000 + 2,000', 'Week 3', '3 weeks'], start=start,
             extra={'after_step': {0: s1, 1: s2, 2: s3, 3: s4, 4: s5}})
keyboard_walk(f, 4, 5)
clicks_only(f, 4, 0)
clicks_only(f, 4, 0, 358, 390)
finish(f)
