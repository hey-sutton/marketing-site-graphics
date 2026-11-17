#!/usr/bin/env python3
"""Card 1 (list and detail, client inventory and ownership): the numbers in Python, then the full click through.
Run: python3 tools/food-co-packing/test_card1.py"""
import os, sys
from decimal import Decimal as D
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fc_tests import run_card, finish, js, pill, testlib, ids, enter_submits

# ---- the numbers, derived independently of the card ----
CLIENT = {'Brightfield Snacks': D('1200'), 'Oakline Foods': D('800'), 'Kettlewood Brands': D('450')}
PLANT = D('600')
assert sum(CLIENT.values()) == D('2450')
assert sum(CLIENT.values()) + PLANT == D('3050')          # plant stock plus client stock equals total on hand
R5108, R5112 = D('420'), D('950')
AFTER = dict(CLIENT, **{'Brightfield Snacks': CLIENT['Brightfield Snacks'] - R5108})
assert AFTER['Brightfield Snacks'] == D('780')               # the run consumes only the chosen owner
assert AFTER['Oakline Foods'] == D('800') and AFTER['Kettlewood Brands'] == D('450')
assert sum(AFTER.values()) == D('2030') and sum(AFTER.values()) + PLANT == D('2630') == D('3050') - R5108
assert R5112 - AFTER['Oakline Foods'] == D('150')            # shortage before the run
assert D('300') <= AFTER['Kettlewood Brands']                # R-5115 is covered


def start(pg, f, when='start'):
    t = js(pg, "return r.querySelector('.c1').innerText")
    f.check(js(pg, "return r.getElementById('qin').value") == '', '%s: the item input is empty' % when)
    f.check(js(pg, "return r.querySelectorAll('.qls .row,.qfg .row,.qrun .row,.qb').length") == 0, '%s: no lots, runs or balances' % when)
    f.check(not any(s in t for s in ('RF-22', 'Brightfield', '3,050', 'R-51', 'FG-77')), '%s: nothing derived from the item shows' % when)


def bad_then_type(pg, f):
    inp = pg.locator('#cv #qin')
    inp.click(); inp.press_sequentially('Oat bran'); inp.press('Enter'); pg.wait_for_timeout(300)
    f.check(js(pg, "return r.getElementById('qfl').classList.contains('err')"), 'step 1: an unknown item shows an inline error')
    f.check('Your turn1 of 5' in pill(pg), 'step 1: an unknown item does not advance')
    inp.fill(''); inp.press_sequentially('rice flour')
    f.check(js(pg, "return r.getElementById('qin').value") == 'rice flour', 'step 1: typing works in the input')


def s1(pg, f):
    f.check(ids(pg, 'qow', 'qg0', 'qg1', 'qg2', 'qg3') == 'Brightfield Snacks|1,200.000 kg|800.000 kg|450.000 kg|600.000 kg', 'step 1: RF-2201 owned by Brightfield Snacks, four lots listed')


def s2(pg, f):
    f.check(ids(pg, 'qbB', 'qbO', 'qbK', 'qbP', 'qtt') == '1,200.000 kg|800.000 kg|450.000 kg|600.000 kg|3,050.000 kg', 'step 2: balances by owner, 3,050.000 kg on hand')
    f.check(ids(pg, 'qsplit') == 'Client 2,450.000 kg, plant 600.000 kg', 'step 2: client 2,450.000 + plant 600.000')


def s3(pg, f):
    f.check(ids(pg, 'qbB', 'qbO', 'qbK', 'qbP', 'qtt', 'qg0') == '780.000 kg|800.000 kg|450.000 kg|600.000 kg|2,630.000 kg|780.000 kg', 'step 3: only Brightfield drops to 780.000, total 2,630.000')


def s4(pg, f):
    f.check(ids(pg, 'qr1', 'qr2') == 'Short 150.000|Covered', 'step 4: R-5112 short 150.000, R-5115 covered')


def s5(pg, f):
    f.check(ids(pg, 'qfc1', 'qfc0', 'qfc2') == 'Held, bay C3|Dock staging|Dock staging', 'step 5: only FG-7730 held in bay C3')


PLAN = [('Every lot carries its owner', 'Brightfield Snacks'),
        ('Client and plant stock side by side', '3,050.000 kg'),
        ('A run draws only from its owner', '780.000 kg'),
        ('Shortages show before the run', 'Short 150.000'),
        ('Finished goods held apart', 'Held, bay C3')]

f = run_card(1, PLAN, ['2,630.000 kg', 'Short 150.000', 'Held, bay C3'], start=start,
             extra={'before': {0: bad_then_type}, 'after_step': {0: s1, 1: s2, 2: s3, 3: s4, 4: s5}})
enter_submits(f, 1, '#qin', 'Rice flour', 'Your turn2 of 5')
finish(f)
