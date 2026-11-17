#!/usr/bin/env python3
"""Card 2 (bake list, stock gauges, purchase order strip): the brief's numbers in Python, then the full click through.
Run: python3 tools/bakery/test_card2.py"""
import math, os, sys
from decimal import Decimal as D
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bk_tests import run_card, finish, js, pill, testlib, ids

# ---- the brief's numbers, derived independently of the card ----
STOCK = {'flour': D('1000'), 'butter': D('40'), 'lbag': 2500, 'bbag': 400, 'rbox': 150}
assert 2000 * D('0.400') == 800 and 1500 * D('0.060') == 90 and 600 * D('0.100') == 60 and 800 + 90 + 60 == 950
assert 2000 * D('0.010') == 20 and 1500 * D('0.012') == 18 and 600 * D('0.030') == 18 and 20 + 18 + 18 == 56
assert 56 - 40 == 16
assert 40 - 20 == 20 and 20 - 18 == 2 and 18 - 2 == 16
assert math.ceil(1500 / 6) == 250 and math.ceil(600 / 6) == 100
assert 2 * 10 == 20 and 40 + 20 == 60 and 60 - 56 == 4
assert 950 <= STOCK['flour'] and 2000 <= STOCK['lbag'] and 250 <= STOCK['bbag'] and 100 <= STOCK['rbox']


def start(pg, f, when='start'):
    t = js(pg, "return r.querySelector('.k2').innerText")
    f.check(js(pg, "return r.querySelectorAll('.kbl button.row,.kg,.kps').length") == 0, '%s: no bake rows, no gauges, no purchase order' % when)
    f.check(js(pg, "return [].filter.call(r.querySelectorAll('.k2 button'),function(b){return b.offsetWidth>0}).map(function(b){return b.textContent}).join('|')") == "Load tomorrow's bake list", '%s: the only button is Load tomorrow\'s bake list' % when)
    f.check(not any(s in t for s in ('Sandwich Loaf', '950.000', '56.000', 'PO-7210', 'Short', 'Clear')), '%s: nothing from the bake list shows' % when)


def s1(pg, f):
    f.check(ids(pg, 'kc0', 'kc1', 'kc2') == 'Not checked|Not checked|Not checked', 'step 1: three rows, all Not checked')
    f.check(js(pg, "return r.querySelectorAll('.kg').length") == 0, 'step 1: the gauges are still empty')


def s2(pg, f):
    f.check(ids(pg, 'kgv-flour', 'kgv-butter', 'kgv-lbag', 'kgv-bbag', 'kgv-rbox') == '950.000 kg of 1,000.000 kg|56.000 kg of 40.000 kg|2,000 of 2,500|250 of 400|100 of 150', 'step 2: gauges flour 950 of 1,000, butter 56 of 40, bags 2,000 of 2,500, 250 of 400, boxes 100 of 150')
    f.check(js(pg, "return !!r.querySelector('#kg-butter .kov')") and ids(pg, 'kgs-butter') == 'Short 16.000 kg', 'step 2: butter gauge red, short 16.000 kg')
    f.check(js(pg, "return r.querySelectorAll('.kov').length") == 1, 'step 2: only the butter gauge is red')
    f.check(ids(pg, 'kc0', 'kc1', 'kc2') == 'Clear|Clear|Short', 'step 2: chips Clear, Clear, Short')
    f.check(js(pg, "return r.getElementById('ksf').disabled"), 'step 2: Send to floor is disabled while a product is short')


def s3(pg, f):
    f.check(ids(pg, 'kmsg').startswith('Needs 18.000 kg butter, 2.000 kg left, short 16.000 kg.'), 'step 3: "Needs 18.000 kg butter, 2.000 kg left, short 16.000 kg"')
    t = js(pg, "return r.querySelector('.kat').innerText")
    f.check('20.000' in t and '2.000' in t and 'short 16.000' in t, 'step 3: allocation 40 to 20 to 2, short 16')


def s4(pg, f):
    f.check(ids(pg, 'kpq', 'kpt') == '2 cases of 10.000 kg|20.000 kg', 'step 4: PO-7210, 2 cases, 20.000 kg')
    t = js(pg, "return r.getElementById('kpo').innerText")
    f.check('PO-7210' in t and 'Cedar Dairy Supply' in t and 'November 17' in t, 'step 4: PO-7210 to Cedar Dairy Supply, expected November 17')
    pg.locator('#cv #ksf').click(force=True); pg.wait_for_timeout(200)
    f.check(js(pg, "return r.querySelectorAll('.kwo').length") == 0, 'step 4: a short product can not be sent to the floor')


def s5(pg, f):
    f.check(ids(pg, 'kgv-butter', 'kgs-butter') == '56.000 kg of 60.000 kg|4.000 kg left', 'step 5: butter 56.000 needed of 60.000, 4.000 left')
    f.check(ids(pg, 'kc0', 'kc1', 'kc2', 'kps') == 'Clear|Clear|Clear|Received', 'step 5: all three Clear, PO Received')
    f.check(not js(pg, "return r.getElementById('ksf').disabled"), 'step 5: Send to floor is enabled')


def floor(pg, f):
    pg.wait_for_timeout(1200)
    f.check(js(pg, "return r.getElementById('ksf').classList.contains('hint')"), 'after Done: Send to floor pulses')
    pg.locator('#cv #ksf').click(); pg.wait_for_timeout(500)
    f.check(ids(pg, 'kw0', 'kw1', 'kw2') == 'WO-5301, 2,000 loaves|WO-5302, 1,500 buns|WO-5303, 600 rolls', 'Send to floor: three work orders')
    f.check('Three work orders on the floor' in testlib.cap_text(pg), 'Send to floor: caption')


PLAN = [("Load tomorrow's bake list", 'Not checked'),
        ('Check every ingredient and pack against stock', 'Short 16.000 kg'),
        ('The last product in line is the one held back', 'short 16.000 kg'),
        ('The gap becomes a purchase order', 'PO-7210'),
        ('Receive it and the bake list clears', '60.000 kg')]

f = run_card(2, PLAN, ['56.000 kg of 60.000 kg', '4.000 kg left', 'Received'], start=start,
             extra={'after_step': {0: s1, 1: s2, 2: s3, 3: s4, 4: s5}, 'after': floor})
finish(f)
