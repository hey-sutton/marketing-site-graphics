#!/usr/bin/env python3
"""Card 3 (BOM tree and cost table): the brief's numbers in Python with Decimal, then the click through.
Run: python3 tools/frozen-food/test_card3.py"""
import os, sys
from decimal import Decimal as D, ROUND_HALF_UP
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ff_tests import run_card, finish, js, pill, ids

c2 = lambda x: x.quantize(D('0.01'), ROUND_HALF_UP)
sb110 = D('0.95') * D('2.10') + D('0.05') * D('3.00')
sb210 = D('0.60') * D('1.60') + D('0.15') * D('4.00') + D('0.10') * D('5.00') + D('0.15') * D('1.00')
assert sb110 == D('2.145') and sb210 == D('2.21')
L = [40 * sb110, 30 * D('0.85'), 30 * sb210]
assert L == [D('85.80'), D('25.50'), D('66.30')] and sum(L) == D('177.60')
sb110b = D('0.95') * D('2.40') + D('0.15')
assert sb110b == D('2.43') and 40 * sb110b == D('97.20') and D('97.20') + D('25.50') + D('66.30') == D('189.00')
assert D('189.00') - D('177.60') == D('11.40') and D('189.00') * 4 == D('756.00') and 160 + 120 + 120 == 400
assert 400 * 96 // 100 == 384 and c2(D(756) / 384) == D('1.97') and c2(D(756) / 378) == D('2.00')


def start(pg, f, when='start'):
    t = js(pg, "return r.querySelector('.g3').innerText")
    f.check(js(pg, "return r.querySelectorAll('.tn,.row.sel,.alg').length") == 0 and '$' not in t, '%s: BOM list only, nothing selected, no costs' % when)


def s1(pg, f):
    f.check(ids(pg, 'c-SB-110', 'c-IQF-30', 'c-SB-210', 'btot') == '$85.80|$25.50|$66.30|$177.60', 'step 1: 85.80 + 25.50 + 66.30 = 177.60')


def s2(pg, f):
    f.check(ids(pg, 'talg') == 'Contains milk' and js(pg, "return r.querySelectorAll('.tre .alg').length") >= 6, 'step 2: milk on cream, butter, parmesan, SB-210 and FE-2210')
    t = js(pg, "return r.getElementById('cst').innerText")
    f.check('$2.145' in t and '$2.21' in t, 'step 2: SB-110 at $2.145 a lb, SB-210 at $2.21 a lb')


def bad_price(pg, f):
    pg.locator('#cv #ick').fill('two forty')
    pg.locator('#cv .hint').first.click(); pg.wait_for_timeout(300)
    f.check(js(pg, "return r.getElementById('fck').classList.contains('err')") and 'Your turn3 of 5' in pill(pg), 'step 3: a bad price shows an error and does not advance')
    pg.locator('#cv #ick').fill('2.40')


def s3(pg, f):
    f.check(ids(pg, 'c-SB-110', 'btot', 'dlt') == '$97.20|$189.00|+$11.40 a batch', 'step 3: SB-110 97.20, batch 189.00, +11.40')
    f.check('$2.43' in js(pg, "return r.getElementById('cst').innerText"), 'step 3: SB-110 at $2.43 a lb')


def s4(pg, f):
    t = js(pg, "return r.getElementById('tre').innerText")
    f.check(ids(pg, 'btot', 'bsz') == '$756.00|400 lb batch' and all(s in t for s in ('160 lb', '120 lb', '400 lb')), 'step 4: 400 lb run, 160, 120 and 120 lb, $756.00')


def bad_out(pg, f):
    pg.locator('#cv #iout').fill('500')
    pg.locator('#cv .hint').first.click(); pg.wait_for_timeout(300)
    f.check(js(pg, "return r.getElementById('fout').classList.contains('err')") and 'Your turn5 of 5' in pill(pg), 'step 5: output above the run shows an error')
    pg.locator('#cv #iout').fill('378')


def s5(pg, f):
    f.check(ids(pg, 'yout', 'yexp', 'yact') == '378 lb|$1.97|$2.00', 'step 5: 378 lb, $1.97 expected, $2.00 actual')


PLAN = [('Pick a product and its BOM costs roll up', '$177.60'),
        ('Sub-assemblies open to every ingredient, and allergens carry up', 'Contains milk'),
        ('A price change rolls up through every level', '$189.00'),
        ('Scale the run and every quantity follows', '$756.00'),
        ('Expected and actual yield set the true cost per pound', '$2.00')]
f = run_card(3, PLAN, ['$756.00', '$1.97', '$2.00', '+$11.40 a batch'], start=start,
             extra={'before': {2: bad_price, 4: bad_out}, 'after_step': {0: s1, 1: s2, 2: s3, 3: s4, 4: s5}})
finish(f)
