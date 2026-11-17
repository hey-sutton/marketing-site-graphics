#!/usr/bin/env python3
"""Card 4 (pack, label and ship stage chain): the brief's numbers in Python, then the full click through.
Run: python3 tools/coffee-roasting/test_card4.py"""
import datetime, os, sys
from decimal import Decimal as D, ROUND_HALF_UP
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cr_tests import run_card, finish, js, pill, testlib, ids, enter_submits


def kg(g):
    return str((D(g) / 1000).quantize(D('0.001'), ROUND_HALF_UP))


# ---- the brief's numbers, derived independently of the card ----
OZ12, LB5, LOT = 12 * D('28.3495'), 5 * D('453.592'), D(36000)
a, b = 48 * OZ12, 8 * LB5
assert kg(a) == '16.329' and kg(b) == '18.144' and kg(a + b) == '34.473' and kg(LOT - a - b) == '1.527'
assert D(kg(a)) + D(kg(b)) == D(kg(a + b)) and D(kg(a + b)) + D(kg(LOT - a - b)) == D('36.000')   # reconciles on screen too
assert a + b + (LOT - a - b) == LOT
ORDERS = [('SO-6101', 24, 4), ('SO-6102', 16, 2), ('SO-6103', 8, 2)]
assert sum(o[1] for o in ORDERS) == 48 and sum(o[2] for o in ORDERS) == 8 and 48 + 8 == 56
assert kg(24 * OZ12 + 4 * LB5) == '17.236'
assert D('31.75') - D('18.40') == D('13.35')
assert (datetime.date(2026, 11, 18) + datetime.timedelta(days=90)) == datetime.date(2027, 2, 16)


def start(pg, f, when='start'):
    t = js(pg, "return r.querySelector('.q4').innerText")
    f.check(js(pg, "return r.getElementById('qn12').value+'|'+r.getElementById('qn5').value") == '|', '%s: bag inputs empty' % when)
    f.check(js(pg, "return [1,2,3,4].every(function(i){return r.getElementById('qv'+i).textContent===''})"), '%s: the chain shows only the roasted lot' % when)
    f.check(not any(s in t for s in ('34.473', 'SO-6101', 'Nov 18, 2026', '$18.40', 'NLF')), '%s: nothing packed, labeled or shipped shows' % when)


def bad_then_type(pg, f):
    pg.locator('#cv #qn12').fill('200'); pg.locator('#cv #qn5').fill('10')
    pg.locator('#cv #qpb').click(); pg.wait_for_timeout(300)
    f.check(js(pg, "return r.getElementById('qpk').classList.contains('err')") and 'Your turn1 of 5' in pill(pg), 'step 1: more bags than the lot holds shows an error')
    for sel, v in (('#qn12', '48'), ('#qn5', '8')):
        inp = pg.locator('#cv ' + sel); inp.fill(''); inp.press_sequentially(v)


def s1(pg, f):
    f.check(ids(pg, 'qk12', 'qk5', 'qkp', 'qkl', 'qkr') == '16.329|18.144|34.473|1.527|36.000', 'step 1: 16.329 + 18.144 = 34.473 packed, 1.527 left, 36.000 roasted')
    f.check(ids(pg, 'qv1') == '56', 'step 1: chain Packed 56 bags')


def s2(pg, f):
    f.check(ids(pg, 'qll', 'qlr', 'qlc') == 'RL-1118-2|Nov 18, 2026|56 printed', 'step 2: label with lot RL-1118-2 and roast date Nov 18, 2026')


def s3(pg, f):
    f.check(ids(pg, 'qo12', 'qo5', 'qs3') == '48|8|56 of 56 bags, 3 orders', 'step 3: 3 orders take 48 x 12 oz and 8 x 5 lb')


def s4(pg, f):
    f.check(ids(pg, 'qrp0', 'qrp1', 'qwt') == '$18.40|$31.75|17.236 kg', 'step 4: two rates for SO-6101, 17.236 kg')


def s5(pg, f):
    f.check(ids(pg, 'qtk', 'qv4') == 'NLF 7714 2093 18|28', 'step 5: tracking on SO-6101, 28 bags shipped')


def prep(pg):
    pg.locator('#cv #qn12').fill('48')


PLAN = [('Pack a roasted lot into 12 ounce and 5 pound bags', '34.473'),
        ('Print a label with the lot number and roast date', 'Nov 18, 2026'),
        ('See open wholesale orders by customer and bag size', 'SO-6103'),
        ('Compare carrier rates from the sales order', '$31.75'),
        ('Book the shipment and see tracking on the order', 'NLF 7714 2093 18')]

f = run_card(4, PLAN, ['1.527', 'NLF 7714 2093 18', '17.236 kg'], start=start,
             extra={'before': {0: bad_then_type}, 'after_step': {0: s1, 1: s2, 2: s3, 3: s4, 4: s5}})
enter_submits(f, 4, '#qn5', '8', 'Your turn2 of 5', prep=prep)
finish(f)
