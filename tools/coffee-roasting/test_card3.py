#!/usr/bin/env python3
"""Card 3 (blend list and BOM detail): the brief's numbers in Python, then the full click through.
Run: python3 tools/coffee-roasting/test_card3.py"""
import os, sys
from decimal import Decimal as D, ROUND_HALF_UP
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cr_tests import run_card, finish, js, pill, testlib, ids, enter_submits

# ---- the brief's numbers, derived independently of the card ----
PRICE = {'Brazil': D('6.20'), 'Colombia': D('7.40'), 'Ethiopia': D('8.60'), 'Guatemala': D('7.10'), 'Honduras': D('5.90')}
BLENDS = {'HB': {'Brazil': 45, 'Colombia': 35, 'Ethiopia': 20}, 'NO': {'Brazil': 60, 'Guatemala': 40}, 'SL': {'Ethiopia': 70, 'Colombia': 30}}
for b in BLENDS.values():
    assert sum(b.values()) == 100
GREEN_PER_BAG = {'12 oz': D('0.400'), '5 lb': D('2.668')}


def lines(kg):
    return [str((D(kg) * p / 100).quantize(D('0.001'))) for p in BLENDS['HB'].values()]


assert lines(5) == ['2.250', '1.750', '1.000'] and sum(D(x) for x in lines(5)) == 5
assert lines(120) == ['54.000', '42.000', '24.000'] and sum(D(x) for x in lines(120)) == 120


def bag(blend, size, swap=False):
    per_kg = sum(PRICE['Honduras' if swap and o == 'Brazil' else o] * D(p) / 100 for o, p in BLENDS[blend].items())
    return (per_kg * GREEN_PER_BAG[size]).quantize(D('0.01'), ROUND_HALF_UP)


WANT = {('HB', '12 oz'): ('2.84', '2.79'), ('HB', '5 lb'): ('18.94', '18.58'), ('NO', '12 oz'): ('2.62', '2.55'), ('NO', '5 lb'): ('17.50', '17.02')}
for (b, s), (o, n) in WANT.items():
    assert str(bag(b, s)) == o and str(bag(b, s, True)) == n, (b, s, bag(b, s), bag(b, s, True))
assert [k for k, v in BLENDS.items() if 'Brazil' in v] == ['HB', 'NO']   # 2 blends, 4 bag sizes; Sunrise Light unchanged


def start(pg, f, when='start'):
    t = js(pg, "return r.querySelector('.q3').innerText")
    f.check(js(pg, "return r.querySelectorAll('.qdt .row,.qar,.qvr').length") == 0, '%s: no BOM lines, no swap, no versions' % when)
    f.check(js(pg, "return ['qfr','qto','qpw'].every(function(i){return r.getElementById(i).disabled})"), '%s: the swap form waits' % when)
    f.check(not any(s in t for s in ('GL-2214', '2.250', '$2.84', 'Kept for reference')), '%s: nothing from the blend shows' % when)


def type_batch(pg, f):
    inp = pg.locator('#cv #qbs')
    inp.fill('0'); pg.locator('#cv #qrz').click(); pg.wait_for_timeout(300)
    f.check(js(pg, "return r.getElementById('qfs').classList.contains('err')") and 'Your turn2 of 5' in pill(pg), 'step 2: a 0 kg batch shows an error')
    inp = pg.locator('#cv #qbs'); inp.fill(''); inp.press_sequentially('120')


def s1(pg, f):
    t = js(pg, "return r.getElementById('qdt').innerText")
    f.check('45%' in t and '35%' in t and '20%' in t and ids(pg, 'qps') == '100%', 'step 1: Brazil 45%, Colombia 35%, Ethiopia 20%, total 100%')
    f.check(ids(pg, 'qk0', 'qk1', 'qk2', 'qkt') == '|'.join(lines(5) + ['5.000']), 'step 1: test roast lines 2.250, 1.750, 1.000 = 5.000 kg')


def s2(pg, f):
    f.check(ids(pg, 'qk0', 'qk1', 'qk2', 'qkt') == '|'.join(lines(120) + ['120.000']), 'step 2: 120 kg batch lines 54.000, 42.000, 24.000')


def s3(pg, f):
    f.check(ids(pg, 'qaff') == '2 blends and 4 bag sizes change. 1 blend unchanged.', 'step 3: 2 blends and 4 bag sizes change')
    t = js(pg, "return r.getElementById('qdt').innerText")
    f.check('Honduras' in t and 'GL-2219' in t and ids(pg, 'qvc') == 'v2 not saved', 'step 3: Honduras replaces Brazil, not saved yet')
    f.check(ids(pg, 'qk0', 'qkt') == '54.000|120.000' and ids(pg, 'qps') == '100%', 'step 3: the swap keeps 45% and the 120 kg batch')


def s4(pg, f):
    got = ids(pg, 'qc-HB0', 'qc-HB1', 'qc-NO0', 'qc-NO1')
    f.check(got == '$2.79|$18.58|$2.55|$17.02', 'step 4: new cost per bag (%s)' % got)
    t = js(pg, "return r.getElementById('qcost').innerText")
    f.check(all('$' + o in t for o, _ in WANT.values()), 'step 4: old cost per bag shown beside the new')


def s5(pg, f):
    f.check(ids(pg, 'qvc') == 'v2 current' and 'Kept for reference' in ids(pg, 'qv1'), 'step 5: v2 current, v1 kept for reference')
    f.check('Honduras 45%' in ids(pg, 'qb0') and 'Honduras 60%' in ids(pg, 'qb1') and 'Honduras' not in ids(pg, 'qb2'), 'step 5: both blends using Brazil now list Honduras, Sunrise Light unchanged')


def prep(pg):
    pg.locator('#cv #qb0').click(); pg.wait_for_timeout(1700)


PLAN = [('Open a house blend and read its origin percentages', '100%'),
        ('Resize the blend from a test roast to a production batch', '120.000'),
        ('Swap one origin across every blend', 'Honduras'),
        ('See cost per bag change with the new bean', '$2.79'),
        ('Keep the earlier version for reference', 'Kept for reference')]

f = run_card(3, PLAN, ['$2.79', '$18.58', '$17.02', 'v2 current'], start=start,
             extra={'before': {1: type_batch}, 'after_step': {0: s1, 1: s2, 2: s3, 3: s4, 4: s5}})
enter_submits(f, 3, '#qbs', '120', 'Your turn3 of 5', prep=prep)
finish(f)
