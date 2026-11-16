#!/usr/bin/env python3
"""Card 3 (formula workbench): the brief's numbers in Python, then the click through.
Run: python3 tools/pharmaceutical/test_card3.py"""
import os, sys
from decimal import Decimal as D, ROUND_HALF_UP
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ph_tests import run_card, finish, js, pill, ids, enter_submits

N, FILL, ASSAY = 200000, D(400), D('0.98')
def kg(mg): return D(mg) * N / 1000000
def r3(x): return x.quantize(D('0.001'), ROUND_HALF_UP)
def r2(x): return x.quantize(D('0.01'), ROUND_HALF_UP)
assert kg(50) == D('10.000') and kg(4) == D('0.800') and kg(400) == D('80.000')
assert kg(400) - kg(50) - kg(4) == D('69.200')
act = kg(50) / ASSAY
assert r3(act) == D('10.204')
assert r3(kg(400) - act - kg(4)) == D('68.996') and D('80.000') - D('10.204') - D('0.800') == D('68.996')
assert kg(2) == D('0.400') and r3(kg(400) - act - kg(2)) == D('69.396') and D('80.000') - D('10.204') - D('0.400') == D('69.396')
assert D('10.204') + D('68.996') + D('0.800') == D('80.000')
PKG = r2(N * D('0.012')) + r2(2000 * D('0.18')) + r2(2000 * D('0.04')) + r2(2000 * D('0.03'))
assert PKG == D('2400.00') + D('360.00') + D('80.00') + D('60.00')
def lines(mgs): return [r2(act * 480), r2((kg(400) - act - kg(mgs)) * D('6.5')), r2(kg(mgs) * 9)]
assert lines(4) == [D('4897.96'), D('448.47'), D('7.20')] and lines(2)[1:] == [D('451.07'), D('3.60')]
T4, T3 = sum(lines(4)) + PKG, sum(lines(2)) + PKG
assert T4 == D('8253.63') and T3 == D('8252.63') and T4 - T3 == D('1.00')
assert r2(T4 / 2000) == D('4.13')


def start(pg, f, when='start'):
    t = js(pg, "return r.querySelector('.g3').innerText")
    f.check(js(pg, "return r.querySelectorAll('#ibs,.ldg .row,.cmp .row,.cl').length") == 0 and 'CP-050' in t, '%s: only the formula list, with CP-050 as the only entry' % when)
    f.check(js(pg, "return r.querySelectorAll('.fl button.row').length") == 1 and not any(s in t for s in ('kg/', 'mg/', '$', '200,000', '10.000')), '%s: no ledger, converter or comparison yet' % when)


def s1(pg, f):
    f.check(ids(pg, 'mg-act', 'mg-mgs', 'mg-mcc', 'kg-act') == '50.00|4.00|346.00|', 'step 1: v4 opens in mg per capsule, kg column empty')



def s2(pg, f):
    f.check(ids(pg, 'kg-act', 'kg-mgs', 'kg-mcc', 'kg-fill') == '10.000|0.800|69.200|80.000', 'step 2: 10.000, 0.800, 69.200, fill 80.000 kg')
    f.check(ids(pg, 'eqa') == '50 mg × 200,000 = 10.000 kg' and js(pg, "var i=r.getElementById('ibs');return i.value+'|'+i.readOnly") == '200,000|true', 'step 2: batch size prefilled 200,000, converter shows 50 mg × 200,000 = 10.000 kg')
    f.check(ids(pg, 'pk-Cap', 'pk-Bot', 'pk-Lab') == '200,000|2,000|2,000', 'step 2: shells 200,000, bottles and labels 2,000')


def s3(pg, f):
    f.check(ids(pg, 'kg-act', 'kg-mcc', 'kg-mgs', 'kg-fill', 'dl-act', 'dl-mcc') == '10.204|68.996|0.800|80.000|+0.204|-0.204', 'step 3: active 10.204 (+0.204), cellulose 68.996, fill 80.000')
    f.check(ids(pg, 'mg-act', 'mg-mcc') == '51.02|344.98', 'step 3: mg per capsule follows the assay')


def s4(pg, f):
    f.check(ids(pg, 'c3m', 'c4m', 'c3c', 'c4c') == '0.400|0.800|69.396|68.996', 'step 4: lubricant 0.400 to 0.800 kg, cellulose 69.396 to 68.996 kg')
    f.check('2.00' in js(pg, "return r.getElementById('cmp').innerText") and '4.00' in js(pg, "return r.getElementById('cmp').innerText"), 'step 4: lubricant 2 mg to 4 mg')


def s5(pg, f):
    f.check(ids(pg, 'ctot', 'cpb', 'cdf') == '$8,253.63|$4.13 per bottle|+$1.00 against v3', 'step 5: $8,253.63, $4.13 per bottle, +$1.00 against v3')
    t = js(pg, "return r.querySelector('.cl').innerText")
    for v in ('4,897.96', '448.47', '7.20', '2,400.00', '360.00', '80.00', '60.00'):
        f.check(v in t, 'step 5: cost line %s' % v)


PLAN = [('Formula v4 opens in milligrams per capsule', '346.00'),
        ('Milligrams per capsule become kilograms per batch', '69.200'),
        ('The active is adjusted for the assay', '68.996'),
        ('Two versions, line by line', '69.396'),
        ('Cost rolls up to the bottle', '$8,253.63')]
f = run_card(3, PLAN, ['$8,253.63', '$4.13 per bottle', '+$1.00 against v3', '10.204', '68.996'], start=start,
             extra={'after_step': {0: s1, 1: s2, 2: s3, 3: s4, 4: s5}})

finish(f)
