#!/usr/bin/env python3
"""Card 1 click through (both modes), numbers, layout and text checks. Run: python3 tools/apparel/test_card1.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from apparel_tests import run_card, js

STOCK = {'Black': [24, 60, 85, 12, 40], 'Navy': [18, 44, 70, 9, 31], 'Sand': [12, 30, 52, 6, 22]}
RUN = {'Black': [10, 20, 30, 60, 20], 'Navy': [10, 20, 30, 50, 20], 'Sand': [10, 10, 20, 40, 10]}
low = [(c, i) for c in STOCK for i, v in enumerate(STOCK[c]) if v < 15]
assert low == [('Black', 3), ('Navy', 3), ('Sand', 0), ('Sand', 3)] and len(low) == 4      # 4 of 15, three are L
assert [sum(RUN[c]) for c in RUN] == [140, 130, 90] and 140 + 130 + 90 == 360
cols = [sum(RUN[c][j] for c in RUN) for j in range(5)]
assert cols == [30, 50, 80, 150, 50] and sum(cols) == 360
yd = [round(q * y, 1) for q, y in zip(cols, [1.0, 1.1, 1.2, 1.3, 1.4])]
assert yd == [30.0, 55.0, 96.0, 195.0, 70.0] and round(sum(yd), 1) == 446.0

def start(pg, f):
    f.check(js(pg, "return r.getElementById('isz').value") == 'XS, S, M, L, XL', 'start: sizes prefilled')
    f.check('No run yet' in js(pg, "return r.getElementById('mat').innerText"), 'start: materials panel stays empty')
    js(pg, "r.getElementById('ico').value='Black, Red'")
    pg.locator('#cv .hint').first.click(); pg.wait_for_timeout(400)
    f.check(js(pg, "return r.getElementById('fco').classList.contains('err')"), 'step 1: an unknown color shows an inline error')
    js(pg, "r.getElementById('ico').value='Black, Navy, Sand'")

def mid(pg, f):
    f.check(js(pg, "return r.getElementById('gt').textContent") == '360', 'step 4: run grand total 360')
    f.check(js(pg, "return r.getElementById('ct-3').textContent") == '150', 'step 4: size L column total 150')
    f.check('No run yet' in js(pg, "return r.getElementById('mat').innerText"), 'step 4: materials still empty before Calculate')

PLAN = [('Every size and color counted on its own', 'Sand'),
        ('Four of fifteen variants are running short', 'Low stock4'),
        ('Enter the whole size run in one grid', 'RUN-0412'),
        ('Each size draws its own fabric', '446.0 yd'),
        ('Released to the cutting room', 'Cut order CUT-0412 created')]

f = run_card(1, PLAN, ['446.0 yd', '195.0 yd', '96.0 yd', '360', 'CUT-0412'], extra={'before': {0: start, 3: mid}})
print('\n%d failures' % len(f)); sys.exit(1 if f else 0)
