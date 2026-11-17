#!/usr/bin/env python3
"""Card 4 (stage chain: packing, labels and shipping): the numbers in Python, then the full click through.
Run: python3 tools/coffee-roasting/test_card4.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cr_tests import run_card, finish, js, pill, testlib, ids, enter_submits, keyboard_walk

# ---- the numbers, derived independently of the card (grams, cents) ----
LOT = 43000
B12, B5, N12, N5, RET = 340, 2268, 59, 10, 260
assert N12 * B12 == 20060 and N5 * B5 == 22680
assert N12 * B12 + N5 * B5 == 42740 and N12 * B12 + N5 * B5 + RET == LOT                # bags plus retain reconcile to 43.000 kg
assert N12 + N5 == 69                                                                     # 69 bags, 69 labels
ORD = [(24, 4), (12, 2), (18, 0)]
assert sum(o[0] for o in ORD) == 54 and sum(o[1] for o in ORD) == 6 and 54 + 6 == 60       # wholesale allocated
assert N12 - 54 == 5 and N5 - 6 == 4                                                      # left for retail and subscriptions
SO = 24 * B12 + 4 * B5 + 2 * 900
assert SO == 19032 and round(SO / 1000, 1) == 19.0 and 24 + 4 == 28                       # 2 cartons, 19.0 kg, 28 bags shipped


def start(pg, f, when='start'):
    t = js(pg, "return r.querySelector('.k4').innerText")
    f.check(js(pg, "return r.getElementById('pin').value") == '', '%s: the lot input is empty' % when)
    f.check(js(pg, "return r.querySelectorAll('#sv0,#sv1,.ppk .row,.lab,.pod .row,.pso .row').length") == 0, '%s: no totals, bags, labels or orders' % when)
    f.check(not any(s in t for s in ('43.000', '69', 'labels print', 'SO-77')), '%s: nothing derived from the lot shows' % when)


def bad_then_type(pg, f):
    inp = pg.locator('#cv #pin')
    inp.click(); inp.press_sequentially('RL-1'); inp.press('Enter'); pg.wait_for_timeout(300)
    f.check(js(pg, "return r.getElementById('pfl').classList.contains('err')"), 'step 1: an unknown lot shows an inline error')
    f.check('Your turn1 of 5' in pill(pg), 'step 1: an unknown lot does not advance')
    inp.fill(''); inp.press_sequentially('rl-8820')


def s1(pg, f):
    f.check(ids(pg, 'pb0', 'pg0', 'pb1', 'pg1', 'prt', 'pbn', 'ptt') == '59|20.060|10|22.680|0.260|69|43.000', 'step 1: 59 x 12 oz + 10 x 5 lb + 0.260 retain = 43.000 kg')
    f.check(ids(pg, 'sv-1', 'sv0', 'ss0') == '43.000 kg|69 bags|42.740 kg in bags', 'step 1: chain Roasted 43.000 kg, Packed 69 bags, 42.740 kg')


def s2(pg, f):
    f.check(ids(pg, 'plt', 'prd', 'pln', 'sv1') == 'RL-8820|Nov 17, 2026|69|69 labels', 'step 2: label with lot RL-8820 and roast date, 69 printed')


def s3(pg, f):
    f.check(ids(pg, 'po0a', 'po0b', 'po1a', 'po1b', 'po2a', 'po2b', 'pota', 'potb', 'pla', 'plb2', 'sv2') == '24|4|12|2|18|0|54|6|5|4|60 bags', 'step 3: three orders 54 + 6 = 60 bags, 5 and 4 left')


def s4(pg, f):
    f.check(ids(pg, 'pcw', 'pr0', 'pr1') == '2 cartons, 19.0 kg|$38.40|$61.25', 'step 4: SO-7716 19.0 kg, two rates')


def s5(pg, f):
    f.check(ids(pg, 'ptk', 'sv3') == 'NW 4418 2093 77|28 bags', 'step 5: tracking on SO-7716, 28 bags shipped')


PLAN = [('Packed into two bag sizes', '43.000'),
        ('Labels carry lot and roast date', '69 labels'),
        ('Open orders by customer and size', 'Copperline Market'),
        ('Rates from the sales order', '$61.25'),
        ('Tracking lands on the order', 'NW 4418 2093 77')]

f = run_card(4, PLAN, ['43.000 kg', '60 bags', '28 bags', 'NW 4418 2093 77'], start=start,
             extra={'before': {0: bad_then_type}, 'after_step': {0: s1, 1: s2, 2: s3, 3: s4, 4: s5}})
enter_submits(f, 4, '#pin', 'RL-8820', 'Your turn2 of 5')
keyboard_walk(f, 4, 5, fill=lambda pg, i: i == 0 and pg.locator('#cv #psp').click())
finish(f)
