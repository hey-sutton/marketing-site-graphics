#!/usr/bin/env python3
"""Card 4 click through (both modes), numbers, layout, variety, timing, navigation and phone checks.
Run: python3 tools/footwear/test_card4.py. Money to two decimals, percentages rounded half up to one decimal."""
import os, sys
from decimal import Decimal as D, ROUND_HALF_UP
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from footwear_tests import run_all, js

# ---- the brief's numbers, derived independently of the card ----
SZ = [7, 8, 9, 10, 11, 12]
MAT = [D('16.40') + i for i in range(6)]
LAB, OVH, LND = D('6.80'), D('3.10'), D('1.40') + D('1.00')
TOT = [m + LAB + OVH + LND for m in MAT]
assert LND == D('2.40') and TOT[2] == D('30.70')
assert TOT == [D(x) for x in ('28.70', '29.70', '30.70', '31.70', '32.70', '33.70')]
QUO = D('29.50')
VAR = [t - QUO for t in TOT]
assert VAR == [D(x) for x in ('-0.80', '0.20', '1.20', '2.20', '3.20', '4.20')]


def p1(n, d):
    return (n / d * 100).quantize(D('0.1'), ROUND_HALF_UP)


assert p1(VAR[2], QUO) == D('4.1')
assert D('735') + D('525') == D('1260') and D('1260') / 525 == D('2.40') and D('2.40') * 525 == D('1260')
RCP = [60, 90, 120, 110, 85, 60]
assert sum(RCP) == 525 and sum(p * LND for p in RCP) == D('1260.00')
PRICE = {'wh': D('52.00'), 'dr': D('78.00')}
MG = {k: [p1(p - t, p) for t in TOT] for k, p in PRICE.items()}
assert MG['wh'][2] == D('41.0') and MG['dr'][2] == D('60.6')


def fmt(v):
    return ('+' if v > 0 else '-' if v < 0 else '') + '%.2f' % abs(v)


def start(pg, f):
    f.check(js(pg, "return r.querySelector('.fwin').getAttribute('data-scr')") == 'Cost by size', 'start: the empty style picker')
    f.check(js(pg, "return r.querySelectorAll('.bc2,.ct2').length") == 0 and js(pg, "return r.getElementById('iq').value") == '', 'start: no chart and no costs before a style is picked')


def bad(pg, f):
    start(pg, f)
    js(pg, "var e=r.getElementById('iq');e.value='ZZ-1';e.dispatchEvent(new Event('input',{bubbles:true}))")
    pg.locator('#cv #iq').press('Enter'); pg.wait_for_timeout(300)
    f.check(js(pg, "return r.getElementById('fs').classList.contains('err')"), 'step 1: a style that does not exist shows an inline error')
    js(pg, "var e=r.getElementById('iq');e.value='';e.dispatchEvent(new Event('input',{bubbles:true}))")


def cost(pg, f):
    got = js(pg, "return [7,8,9,10,11,12].map(function(s){return r.getElementById('tt-'+s).textContent}).join('|')")
    f.check(got == '|'.join('%.2f' % t for t in TOT), 'step 2: totals 28.70 to 33.70 by size (%s)' % got)
    f.check(js(pg, "return r.getElementById('t9').textContent") == '30.70', 'step 2: size 9 selected at 30.70')


def land(pg, f):
    f.check(js(pg, "return ['lp','lf','ld','lpp','lt'].map(function(i){return r.getElementById(i).textContent}).join('|')") == '525|$735.00|$525.00|2.40|$1,260.00', 'step 3: 525 pairs, $735.00 and $525.00, 2.40 a pair, $1,260.00')


def qv(pg, f):
    got = js(pg, "return [7,8,9,10,11,12].map(function(s){return r.getElementById('vr-'+s).textContent+'/'+r.getElementById('mg-'+s).textContent}).join('|')")
    f.check(got == '|'.join('%s/%s%%' % (fmt(v), m) for v, m in zip(VAR, MG['wh'])), 'step 5: variance and wholesale margin by size (%s)' % got)


def end(pg, f):
    got = js(pg, "return [7,8,9,10,11,12].map(function(s){return r.getElementById('mg-'+s).textContent}).join('|')")
    f.check(got == '|'.join('%s%%' % m for m in MG['dr']), 'step 5: direct margin by size (%s)' % got)


PLAN = [('Cost per pair stacks up for every size', '30.70'),
        ('Landed cost comes from the receipt', '$1,260.00'),
        ('Back to the cost stack for HR-210', '33.70'),
        ('Quoted cost sits next to actual cost', '+1.20'),
        ('Margin changes by channel', '60.6%')]

f = run_all(4, PLAN, ['60.6%', '+1.20', '4.1%'], extra={'before': {0: bad, 1: cost, 2: land, 4: qv}, 'after': end}, start=start)
print('\n%d failures' % len(f)); sys.exit(1 if f else 0)
