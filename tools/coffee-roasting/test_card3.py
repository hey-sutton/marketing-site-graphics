#!/usr/bin/env python3
"""Card 3 (list and detail: blends and bean substitution): the numbers in Python, then the full click through.
Run: python3 tools/coffee-roasting/test_card3.py"""
import os, sys
from fractions import Fraction as F
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cr_tests import clicks_only, run_card, finish, js, pill, testlib, ids, enter_submits, keyboard_walk

# ---- the numbers, derived independently of the card ----
COST = {'BR': 520, 'CO': 640, 'ET': 760, 'HN': 580, 'DC': 790}       # cents per kg of green
BL = {'Foundry espresso': [('BR', 50), ('CO', 30), ('ET', 20)], 'Daybreak roast': [('CO', 60), ('BR', 40)],
      'Mesa decaf': [('DC', 100)], 'Ridgeline cold brew': [('BR', 70), ('CO', 30)]}
BAG = [('12 oz', 400, 38), ('5 lb', 2650, 95)]                       # green grams per bag, bag and label cents


def swap(m):
    return [('HN' if o == 'BR' else o, p) for o, p in m]


for n, m in BL.items():
    assert sum(p for _, p in m) == 100 and sum(p for _, p in swap(m)) == 100, n          # every blend sums to exactly 100
uses = [n for n, m in BL.items() if any(o == 'BR' for o, _ in m)]
assert len(uses) == 3 and len(uses) * len(BAG) == 6                                         # 3 blends, 6 bag sizes
FE = BL['Foundry espresso']
assert [F(5000 * p, 100) for _, p in FE] == [2500, 1500, 1000]                               # 5 kg test roast
assert [F(120000 * p, 100) for _, p in FE] == [60000, 36000, 24000] and sum([60000, 36000, 24000]) == 120000   # 120 kg batch


def cpk(m):
    return F(sum(p * COST[o] for o, p in m), 100)


def bag(m, i):
    v = F(BAG[i][1]) * cpk(m) / 1000 + BAG[i][2]
    assert v - int(v) != F(1, 2), 'no rounding ties'
    return round(v)


assert cpk(FE) == 604 and cpk(swap(FE)) == 634                                               # $6.04 to $6.34 per kg
assert (bag(FE, 0), bag(swap(FE), 0), bag(FE, 1), bag(swap(FE), 1)) == (280, 292, 1696, 1775)
assert bag(swap(FE), 0) - bag(FE, 0) == 12 and bag(swap(FE), 1) - bag(FE, 1) == 79           # +$0.12 and +$0.79 per bag


def start(pg, f, when='start'):
    f.check(js(pg, "return r.querySelectorAll('.bom,.cg,.bhi .row,#bsz').length") == 0, '%s: no BOM, batch, cost or versions open' % when)
    t = js(pg, "return r.querySelector('.k3r').innerText")
    f.check(not any(s in t for s in ('GL-4510', '120.0', '$', 'v2')), '%s: nothing derived from a blend shows' % when)


def bad_size(pg, f):
    inp = pg.locator('#cv #bsz'); inp.fill('abc'); pg.locator('#cv #brz').click(); pg.wait_for_timeout(300)
    f.check(js(pg, "return r.getElementById('bfl').classList.contains('err')"), 'step 2: a bad batch size shows an inline error')
    f.check('Your turn2 of 5' in pill(pg), 'step 2: a bad batch size does not advance')
    inp.fill(''); inp.press_sequentially('120')


def s1(pg, f):
    f.check(ids(pg, 'bp0', 'bp1', 'bp2', 'bpt') == '50%|30%|20%|100%', 'step 1: Brazil 50, Colombia 30, Ethiopia 20, total 100')
    f.check(ids(pg, 'bk0', 'bk1', 'bk2', 'bkt') == '2.5|1.5|1.0|5.0', 'step 1: 5 kg test roast lines 2.5, 1.5, 1.0')


def s2(pg, f):
    f.check(ids(pg, 'bk0', 'bk1', 'bk2', 'bkt', 'bpt') == '60.0|36.0|24.0|120.0|100%', 'step 2: 120 kg batch lines 60.0, 36.0, 24.0')


def s3(pg, f):
    f.check(ids(pg, 'bsn', 'bsb', 'bu0', 'bu1', 'bu2', 'bpt') == '3|6|50%|40%|70%|100%', 'step 3: Honduras in 3 blends, 6 bag sizes, still 100%')
    t = js(pg, "return r.getElementById('bls').innerText")
    f.check('Brazil' not in t and t.count('Honduras') == 3, 'step 3: no blend lists Brazil, three list Honduras')


def s4(pg, f):
    f.check(ids(pg, 'bck', 'bco0', 'bcn0', 'bcd0', 'bco1', 'bcn1', 'bcd1') == 'Green $6.04 to $6.34 per kg|$2.80|$2.92|+$0.12 per bag|$16.96|$17.75|+$0.79 per bag', 'step 4: cost per bag before and after')


def s5(pg, f):
    f.check(ids(pg, 'bv2', 'bv1') == 'Current|Kept for reference', 'step 5: v2 current, v1 kept for reference')


PLAN = [('A blend is a BOM by origin', '100%'),
        ('From test roast to production', '120.0'),
        ('One swap, every blend', 'Honduras Marcala'),
        ('Cost per bag before you save', '$2.92'),
        ('The earlier version stays', 'Kept for reference')]

f = run_card(3, PLAN, ['$17.75', '120.0', 'Kept for reference'], start=start,
             extra={'before': {1: bad_size}, 'after_step': {0: s1, 1: s2, 2: s3, 3: s4, 4: s5}})
enter_submits(f, 3, '#bsz', '120', 'Your turn3 of 5', prep=lambda pg: (pg.locator('#cv #bl0').click(), pg.wait_for_timeout(1700)))
keyboard_walk(f, 3, 5)
clicks_only(f, 3)
clicks_only(f, 3, card_w=358, vw=390)
finish(f)
