#!/usr/bin/env python3
"""Card 3 (board): the README's cut plan numbers in Python, then the click through.
Run: python3 tools/meat-poultry-processing/test_card3.py"""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from mp_tests import run_card, finish, js, ids, readonly_checks, keyboard_walk, clicks_only

Y = {'rb': 12, 'bk': 14, 'tr': 85}                   # yield per carcass, kg
DAYS = {'rb': [84, 96, 72], 'bk': [0, 140, 126], 'tr': [900, 500, 300]}
ORDER = {k: sum(v) for k, v in DAYS.items()}
assert ORDER == {'rb': 252, 'bk': 266, 'tr': 1700}
OH = {'rb': 36, 'bk': 0, 'tr': 85}
NET = {k: ORDER[k] - OH[k] for k in Y}
assert NET == {'rb': 216, 'bk': 266, 'tr': 1615}      # net need equals order minus stock for each cut
CAR = {k: math.ceil(NET[k] / Y[k]) for k in Y}
assert CAR == {'rb': 18, 'bk': 19, 'tr': 19}         # carcasses = net need / yield, rounded up
GROSS = {k: math.ceil(ORDER[k] / Y[k]) for k in Y}
assert GROSS == {'rb': 21, 'bk': 19, 'tr': 20}
PO = max(CAR.values())
assert PO == 19                                      # the purchase order equals the largest figure
assert PO * Y['rb'] == 228 and PO * Y['rb'] - NET['rb'] == 12   # ribeye surplus is 12 kg


def num(x):
    return int(x.replace(',', ''))


def start(pg, f, when='start'):
    readonly_checks(pg, f, {'iwk': 'Week 47, 3 customer orders'}, when)
    f.check(js(pg, "return r.querySelectorAll('.oc,.pg,.wl,.pt').length") == 0, '%s: no orders, rows or PO shown' % when)
    t = js(pg, "return r.querySelector('.g4').innerText")
    f.check(not any(s in t for s in ('252', 'Ribeye', 'SO-9101', '19 carcasses')), '%s: nothing derived shows' % when)


def s1(pg, f):
    f.check(js(pg, "return r.querySelectorAll('.oc').length") == 3, 'step 1: 3 customer orders')
    f.check(js(pg, "return r.querySelectorAll('.pg .row').length") == 0, 'step 1: no cut rows yet')


def s2(pg, f):
    got = {k: num(ids(pg, 'n-' + k)) for k in Y}
    f.check(got == ORDER, 'step 2: rows ribeye 252, brisket 266, trim 1,700 %s' % got)
    rows = js(pg, "return [].map.call(r.querySelectorAll('.pg .row:not(.h)'),function(e){return [].slice.call(e.children,1,4).map(function(c){return +c.textContent.replace(/,/g,'')||0})})")
    f.check([sum(x) for x in rows] == [252, 266, 1700], 'step 2: ship days add up to each order kg')


def s3(pg, f):
    got = {k: int(ids(pg, 'g-' + k)) for k in Y}
    yl = {k: int(ids(pg, 'y-' + k)) for k in Y}
    f.check(yl == Y and got == {k: math.ceil(ORDER[k] / yl[k]) for k in Y}, 'step 3: carcass column fills from order / yield %s' % got)


def s4(pg, f):
    oh = {k: num(ids(pg, 'h-' + k)) for k in Y}
    net = {k: num(ids(pg, 't-' + k)) for k in Y}
    f.check(oh == OH and net == NET and all(net[k] == ORDER[k] - oh[k] for k in Y), 'step 4: net need = order minus stock %s' % net)
    car = {k: int(ids(pg, 'c-' + k)) for k in Y}
    f.check(car == {k: math.ceil(net[k] / Y[k]) for k in Y} == {'rb': 18, 'bk': 19, 'tr': 19}, 'step 4: carcasses 18, 19, 19 on screen %s' % car)
    f.check(ids(pg, 'w-rb') == '252 − 36 = 216 ÷ 12 = 18', 'step 4: working line for ribeye (%s)' % ids(pg, 'w-rb'))


def s5(pg, f):
    car = [int(ids(pg, 'c-' + k)) for k in Y]
    f.check(ids(pg, 'poq') == '%d carcasses' % max(car) == '19 carcasses', 'step 5: PO for the largest figure, 19')
    f.check(ids(pg, 'b-rb', 's-rb') == '228|12', 'step 5: ribeye 228 kg, surplus 12 kg')
    f.check(ids(pg, 's-bk', 's-tr') == '0|0', 'step 5: brisket and trim come out even')


PLAN = [('The week’s orders', 'Copper Kettle Grill'),
        ('The quantity needed of each cut', '1,700'),
        ('Worked back to carcasses', '21'),
        ('Stock on hand nets the need down', '1,615'),
        ('A purchase order for the gap', '19 carcasses')]
f = run_card(3, PLAN, ['216', '266', '1,615', '228', '19 carcasses'], start=start,
             extra={'after_step': {0: s1, 1: s2, 2: s3, 3: s4, 4: s5}})
keyboard_walk(f, 3, 5)
clicks_only(f, 3, 0)
clicks_only(f, 3, 0, 358, 390)
finish(f)
