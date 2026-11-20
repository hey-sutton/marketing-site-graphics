#!/usr/bin/env python3
"""Card 4 (stage chain): the README's allocation numbers in Python, then the click through.
Run: python3 tools/wineries/test_card4.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from wn_tests import run_card, finish, js, ids, readonly_checks, keyboard_walk, clicks_only

BOTTLED, REST = 300, [50, 40, 30]
STATES = []
promised = sum(REST)
for add in (0, 100, 60):
    promised += add
    STATES.append((promised, BOTTLED - promised))
assert STATES == [(120, 180), (220, 80), (280, 20)]                            # free 180, then 80, then 20
assert all(p + f == BOTTLED for p, f in STATES)                                # bottled = promised + free at every step
STAGES = ['Open', 'Picking', 'Packed', 'Shipped']
assert len(STAGES) == 4


def counts(pg):
    return ids(pg, 'cbt', 'cpr', 'cfr')


def start(pg, f, when='start'):
    readonly_checks(pg, f, {'irl': 'Cellar Select Syrah, 300 cases'}, when)
    f.check(js(pg, "return r.querySelectorAll('.tl,.oc,.orw,.lg2 .row').length") == 0, '%s: no counts, orders or log shown' % when)
    t = js(pg, "return r.querySelector('.g4').innerText")
    f.check(not any(s in t for s in ('120', '180', 'SO-7', 'Westvale', 'Picking')), '%s: nothing derived shows' % when)


def s1(pg, f):
    f.check(js(pg, "return r.querySelectorAll('.chn .oc').length") == 3 and js(pg, "return r.querySelectorAll('.chn .sc').length") == 4, 'step 1: three restaurant orders on the four stage chain')
    f.check(js(pg, "return r.querySelectorAll('.tl').length") == 0, 'step 1: counts not shown yet')


def s2(pg, f):
    f.check(counts(pg) == '300|120|180' and ids(pg, 'ceq') == '300 = 120 + 180', 'step 2: 300 bottled = 120 promised + 180 free')


def s3(pg, f):
    f.check(counts(pg) == '300|220|80' and ids(pg, 'ceq') == '300 = 220 + 80', 'step 3: distributor 100, free drops to 80')
    f.check(js(pg, "return !!r.querySelector('#st-0 #o-SO-7410')"), 'step 3: the distributor order is open')


def s4(pg, f):
    f.check(counts(pg) == '300|280|20' and ids(pg, 'ceq') == '300 = 280 + 20', 'step 4: club 60, free drops to 20')
    rows = js(pg, "return [].map.call(r.querySelectorAll('.lg2 .row:not(.h)'),function(e){var c=e.children;return c[2].textContent+'+'+c[3].textContent+'='+c[4].textContent})")
    f.check(rows == ['120+180=300 ✓', '220+80=300 ✓', '280+20=300 ✓'], 'step 4: the log keeps bottled = promised + free %s' % rows)


def s5(pg, f):
    f.check(js(pg, "return !!r.querySelector('#st-3 #o-SO-7410')"), 'step 5: the distributor order is in Shipped')
    f.check(ids(pg, 'dtr') == '✓ Open ✓ Picking ✓ Packed ✓ Shipped', 'step 5: the advanced order shows all four stages')
    f.check(counts(pg) == '300|280|20', 'step 5: counts unchanged by shipping, still 300 = 280 + 20')


PLAN = [('A limited release and its orders', 'Marlow Room'),
        ('Bottled, promised and free cases', '300 = 120 + 180'),
        ('A distributor order draws on free cases', '300 = 220 + 80'),
        ('A club order and what is left', '300 = 280 + 20'),
        ('An order moved from open to shipped', 'Shipped')]
f = run_card(4, PLAN, ['300 = 280 + 20', 'SO-7410', 'CL-1124', 'Picking'], start=start,
             extra={'after_step': {0: s1, 1: s2, 2: s3, 3: s4, 4: s5}})
keyboard_walk(f, 4, 5)
clicks_only(f, 4, 0)
clicks_only(f, 4, 0, 358, 390)
finish(f)
