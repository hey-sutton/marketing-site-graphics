#!/usr/bin/env python3
"""Card 1 (record form with a side summary): the README's blend, conversion and cost numbers in Python, then the
click through. Money is in units of 1/10,000 dollar so every check is exact.
Run: python3 tools/wineries/test_card1.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from wn_tests import run_card, finish, js, ids, readonly_checks, keyboard_walk, clicks_only

CASES, PER, ML = 1200, 12, 750
RUN_L = CASES * PER * ML // 1000
COMP = {'Cabernet Sauvignon': (8100, 42000), 'Merlot': (1620, 36000), 'Cabernet Franc': (1080, 50000)}   # liters, $/L x 10,000
assert RUN_L == 10800 and sum(l for l, _ in COMP.values()) == 10800                         # components sum to 10,800 L
assert [l * 100 // RUN_L for l, _ in COMP.values()] == [75, 15, 10]                          # ratios 75 : 15 : 10
assert RUN_L * 1000 // ML == 14400 and 14400 // PER == 1200                                   # 10,800 / 0.75 = 14,400 bottles = 1,200 cases
BLEND = sum(l * c for l, c in COMP.values()) // RUN_L
assert BLEND == 41900 and [l * c // RUN_L for l, c in COMP.values()] == [31500, 5400, 5000]  # $4.19 = 3.15 + 0.54 + 0.50
WINE = BLEND * ML // 1000
assert WINE == 31425                                                                         # 0.75 x 4.19 = 3.1425
GLASS, CORK, SCREW, CAP, LABEL, CARTON = 6200, 3800, 2900, 1200, 2100, 14000
B1, B2 = WINE + GLASS + CORK + CAP + LABEL, WINE + GLASS + SCREW + CAP + LABEL
assert B1 == 44725 and B2 == 43825
cents = lambda x: '$%.2f' % (round(x / 100) / 100)
assert cents(B1) == '$4.47' and cents(B2) == '$4.38'
C1, C2 = B1 * PER + CARTON, B2 * PER + CARTON
assert B1 * PER == 536700 and C1 == 550700 and C2 == 539900 and C1 - C2 == 10800             # $53.67 + $1.40 = $55.07, $53.99, $1.08
assert cents(B1 * PER) == '$53.67' and cents(C1) == '$55.07' and cents(C2) == '$53.99' and cents(C1 - C2) == '$1.08'
assert round(4.47 * 12, 2) == 53.64   # why the case is built from the unrounded bottle cost


def start(pg, f, when='start'):
    readonly_checks(pg, f, {'ibl': 'Reserve Red'}, when)
    f.check(js(pg, "return r.querySelectorAll('.tre,.bm,.cvs,.vs,.mx').length") == 0, '%s: no tree, cost or versions shown' % when)
    t = js(pg, "return r.querySelector('.g1').innerText")
    f.check(not any(s in t for s in ('Merlot', '10,800', '4.19', '75%', '55.07')), '%s: nothing derived shows' % when)


def s1(pg, f):
    f.check(ids(pg, 'pc0', 'pc1', 'pc2') == '75%|15%|10%', 'step 1: tree shows 75, 15, 10 percent')
    f.check('Cabernet Sauvignon' in js(pg, "return r.getElementById('tre').innerText") and ids(pg, 'cl0') == 'None', 'step 1: component wines listed, no liters yet')


def s2(pg, f):
    f.check(ids(pg, 'cl0', 'cl1', 'cl2', 'ltot') == '8,100|1,620|1,080|10,800', 'step 2: 8,100 + 1,620 + 1,080 = 10,800 L')


def s3(pg, f):
    f.check(ids(pg, 'cvl', 'cvb2', 'cvc') == '10,800 L|14,400|1,200', 'step 3: 10,800 L, 14,400 bottles, 1,200 cases')
    f.check('10,800 L ÷ 0.75 L = 14,400 bottles ÷ 12 = 1,200 cases' in ids(pg, 'cvcal'), 'step 3: the conversion is shown')


def s4(pg, f):
    f.check(ids(pg, 'cb0', 'cb1', 'cb2', 'bpl') == '$3.15|$0.54|$0.50|$4.19', 'step 4: blend $4.19 per liter = 3.15 + 0.54 + 0.50')
    f.check(ids(pg, 'bwn', 'bbt', 'spb') == '$3.1425|$4.47|$4.47', 'step 4: wine $3.1425, bottle $4.47')
    f.check(ids(pg, 's12', 'spc') == '$53.67|$55.07', 'step 4: 12 bottles $53.67, case $55.07')


def s5(pg, f):
    f.check(ids(pg, 'v1c', 'v2c', 'vdf') == '$55.07|$53.99|$1.08', 'step 5: version 1 still $55.07, version 2 $53.99, $1.08 less')
    f.check(ids(pg, 'spb', 'spc', 's12') == '$4.38|$53.99|$52.59', 'step 5: screwcap bottle $4.38, case $53.99')
    f.check(js(pg, "return r.querySelectorAll('#vs .row').length") == 2 and ids(pg, 'ver') == 'Version 2', 'step 5: both versions listed')


PLAN = [('A blend and its component wines', 'Cabernet Franc'),
        ('Scaled to a 1,200 case run', '8,100'),
        ('Liters to bottles and cases', '14,400'),
        ('Cost per bottle and per case', '$55.07'),
        ('A closure change saved as a new version', '$53.99')]
f = run_card(1, PLAN, ['$55.07', '$53.99', '$1.08', '$4.19', '10,800'], start=start,
             extra={'after_step': {0: s1, 1: s2, 2: s3, 3: s4, 4: s5}})
keyboard_walk(f, 1, 5)
clicks_only(f, 1, 0)
clicks_only(f, 1, 0, 358, 390)
finish(f)
