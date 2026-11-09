#!/usr/bin/env python3
"""Card 1 click through (both modes), numbers, layout and text checks. Run: python3 tools/plastics/test_card1.py
Rounding: weights to 0.1 lb, money to cents half up."""
import os, sys
from decimal import Decimal as D, ROUND_HALF_UP
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from plastics_tests import run_card, js


def c(x):
    return x.quantize(D('0.01'), ROUND_HALF_UP)


SH = [D('92.5'), D('2.5'), D('0.5'), D('4.5')]
PR = [D('0.74'), D('2.15'), D('4.10'), D('0.30')]
W = [s * 1000 / 100 for s in SH]
assert W == [925, 25, 5, 45] and sum(W) == 1000
costs = [c(w * p) for w, p in zip(W, PR)]
assert costs == [D('684.50'), D('53.75'), D('20.50'), D('13.50')] and sum(costs) == D('772.25')
assert sum(costs) / 1000 == D('0.77225') and D('27.5') * D('0.77225') == D('21.236875') and c(D('21.236875')) == D('21.24')
assert D('21.24') + D('6.10') + D('9.00') == D('36.34')
assert D('925.0') * D('0.814') == D('752.95') and D('752.95') + D('53.75') + D('20.50') + D('13.50') == D('840.70')
assert c(D('27.5') * D('0.8407')) == D('23.12') and D('23.12') + D('15.10') == D('38.22') and D('38.22') - D('36.34') == D('1.88')
assert D('1.88') * 20 == D('37.60') and D('1.88') * 30 == D('56.40') and D('37.60') + D('56.40') == D('94.00')


def start(pg, f):
    f.check(js(pg, "return r.getElementById('iit').value") == 'CAP-38', 'start: item prefilled')
    f.check('No BOM open' in js(pg, "return r.getElementById('tre').innerText"), 'start: tree empty until opened')
    js(pg, "var e=r.getElementById('iit');e.value='CAP-99';e.dispatchEvent(new Event('input',{bubbles:true}))")
    pg.locator('#cv .hint').first.click(); pg.wait_for_timeout(400)
    f.check(js(pg, "return r.getElementById('fit').classList.contains('err')"), 'step 1: an unknown item shows an inline error')
    js(pg, "var e=r.getElementById('iit');e.value='CAP-38';e.dispatchEvent(new Event('input',{bubbles:true}))")


def scale(pg, f):
    f.check(js(pg, "return r.getElementById('iw').value") == '1,000', 'step 2: batch weight prefilled')
    f.check(js(pg, "return r.getElementById('w-PP-100').textContent") == '', 'step 2: no weights before scaling')
    js(pg, "var e=r.getElementById('iw');e.value='lots';e.dispatchEvent(new Event('input',{bubbles:true}))")
    pg.locator('#cv .hint').first.click(); pg.wait_for_timeout(400)
    f.check(js(pg, "return r.getElementById('fw').classList.contains('err')"), 'step 2: a bad weight shows an inline error')
    js(pg, "var e=r.getElementById('iw');e.value='1,000';e.dispatchEvent(new Event('input',{bubbles:true}))")


def weights(pg, f):
    f.check(js(pg, "return ['PP-100','COL-BLK','UV-02','REG-PP'].map(function(k){return r.getElementById('w-'+k).textContent}).join('|')") == '925.0 lb|25.0 lb|5.0 lb|45.0 lb', 'step 2: 925.0, 25.0, 5.0, 45.0 lb')
    f.check(js(pg, "return r.getElementById('wtot').textContent") == '1,000.0 lb', 'step 2: 1,000.0 lb in all')


def cost(pg, f):
    f.check(js(pg, "return [r.getElementById('btot').textContent,r.getElementById('plb').textContent,r.getElementById('cmp').textContent,r.getElementById('k1').textContent].join('|')") == '772.25|0.77225|21.24|36.34', 'step 3: 772.25, 0.77225 a lb, 21.24, 36.34')
    f.check(js(pg, "return r.getElementById('ipc').value") == '+10%', 'step 4: price change prefilled')


def price(pg, f):
    f.check(js(pg, "return [r.getElementById('p-PP-100').textContent,r.getElementById('btot').textContent,r.getElementById('cmp').textContent,r.getElementById('k1').textContent].join('|')") == '0.814|840.70|23.12|38.22', 'step 4: 0.814, 840.70, 23.12, 38.22')
    f.check('1.88' in js(pg, "return r.getElementById('upc').textContent"), 'step 4: up 1.88')


def runs(pg, f):
    f.check(js(pg, "return [r.getElementById('d-RUN-7712').textContent,r.getElementById('d-RUN-7716').textContent,r.getElementById('dtot').textContent].join('|')") == '+37.60|+56.40|+94.00', 'step 5: +37.60, +56.40, +94.00')
    f.check(js(pg, "return r.getElementById('d-RUN-7690').textContent") == '', 'step 5: completed runs unchanged')


def end(pg, f):
    f.check(js(pg, "return [].map.call(r.querySelectorAll('.rns .ch'),function(e){return e.textContent}).join(',')") == 'v2,v3,v3,v4,v4', 'step 6: scheduled runs on v4, earlier runs stay on v3')


PLAN = [('A part builds in levels', 'BLK-PP-92'),
        ('Set the blend once as percentages', '0.925 gaylord'),
        ('Resin, colorant, additive, regrind, packaging and labor roll up', '36.34'),
        ('See what a resin price rise does to every part', '38.22'),
        ('The runs already scheduled show their extra cost', '94.00'),
        ('Every version is kept', 'Version 4 saved')]

f = run_card(1, PLAN, ['94.00', '37.60', '56.40', '38.22'], extra={'before': {0: start, 1: scale, 2: weights, 3: cost, 4: price, 5: runs}, 'after': end})
print('\n%d failures' % len(f)); sys.exit(1 if f else 0)
