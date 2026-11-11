#!/usr/bin/env python3
"""Card 1 (lineage board): the brief's numbers in Python, then the click through. Run: python3 tools/frozen-food/test_card1.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ff_tests import run_card, finish, js, pill, ids, testlib
from playwright.sync_api import sync_playwright

LOT, LB_CASE, CASES_PALLET = 3000, 2, 100
BAT = {'B-4412': 1200, 'B-4416': 1000, 'B-4421': 800}
CASES = {'B-4412': 600, 'B-4416': 500, 'B-4421': 400}
DEST = {'B-4412': [('Northfield Foods', 4), ('Coastal Grocers', 2)], 'B-4416': [('Coastal Grocers', 3), ('Freezer', 2)], 'B-4421': [('Freezer', 4)]}
assert 1200 + 1000 + 800 == sum(BAT.values()) == LOT
assert all(CASES[b] * LB_CASE == BAT[b] for b in BAT) and sum(CASES.values()) == 1500
PAL = {b: CASES[b] // CASES_PALLET for b in CASES}
assert PAL == {'B-4412': 6, 'B-4416': 5, 'B-4421': 4} and 6 + 5 + 4 == sum(PAL.values()) == 15
assert all(sum(q for _, q in DEST[b]) == PAL[b] for b in BAT)
SHIP = sum(q for d in DEST.values() for c, q in d if c != 'Freezer')
FRZ = sum(q for d in DEST.values() for c, q in d if c == 'Freezer')
assert 4 + 2 + 3 == SHIP == 9 and FRZ == 6 and 9 + 6 == 15


def start(pg, f, when='start'):
    t = js(pg, "return r.querySelector('.g1').innerText")
    f.check(js(pg, "return r.getElementById('lin').value") == '' and js(pg, "return r.querySelectorAll('.it,.tl').length") == 0, '%s: empty input, every column a placeholder' % when)
    f.check(not any(s in t for s in ('3,000', 'B-44', 'pallets', 'Northfield')), '%s: nothing derived from the lot shows' % when)


def bad_then_type(pg, f):
    inp = pg.locator('#cv #lin')
    inp.click(); inp.press_sequentially('HR-0000'); inp.press('Enter'); pg.wait_for_timeout(300)
    f.check(js(pg, "return r.getElementById('flin').classList.contains('err')") and 'Your turn1 of 5' in pill(pg), 'step 1: an unknown lot shows an error and does not advance')
    inp.fill(''); inp.press_sequentially('hr-7731')
    f.check(js(pg, "return r.getElementById('lin').value") == 'hr-7731', 'step 1: typing works in the input')


def s1(pg, f):
    t = js(pg, "return r.getElementById('brd').innerText")
    f.check('3,000 lb' in t and 'Harvest Ridge Farms' in t and 'IQF broccoli' in t, 'step 1: lot HR-7731, IQF broccoli, 3,000 lb, Harvest Ridge Farms')


def s2(pg, f):
    f.check(ids(pg, 'bl0', 'bl1', 'bl2') == '1,200 lb used|1,000 lb used|800 lb used', 'step 2: 1,200, 1,000 and 800 lb')
    f.check(ids(pg, 'bc0', 'bc1', 'bc2', 'lused') == '600 cases at 2 lb|500 cases at 2 lb|400 cases at 2 lb|3,000 of 3,000 lb', 'step 2: cases at 2 lb, 3,000 of 3,000 lb used')


def s3(pg, f):
    f.check(ids(pg, 'pp0', 'pp1', 'pp2', 'npa') == '6 pallets|5 pallets|4 pallets|15', 'step 3: 6, 5 and 4 pallets, 15 in all')
    f.check(js(pg, "return r.querySelectorAll('.tl').length") == 15, 'step 3: 15 pallet tiles')


def s4(pg, f):
    f.check(ids(pg, 'cp0', 'cp1', 'cp2', 'scu', 'sfz') == '4 pallets|5 pallets|6 pallets|2|6', 'step 4: Northfield 4, Coastal 5, freezer 6')
    f.check(js(pg, "return [r.querySelectorAll('.tl.s').length,r.querySelectorAll('.tl.f').length].join()") == '9,6', 'step 4: 9 tiles shipped, 6 in the freezer')


def s5(pg, f):
    f.check(ids(pg, 'cst', 'csum') == 'Quarantined|3 batches, 15 pallets, 2 customers, 6 held.', 'step 5: Quarantined, 3 batches, 15 pallets, 2 customers, 6 held')
    f.check(js(pg, "return r.querySelectorAll('.tl.h').length") == 6, 'step 5: the 6 freezer pallets marked held')


def enter_submits(f):
    with sync_playwright() as p:
        b = testlib.browser(p)
        pg, errs = testlib.open_card(b, 1, 1300)
        pg.locator('#cv').scroll_into_view_if_needed()
        pg.locator('#cv .mtg [data-m="try"]').click(); pg.wait_for_timeout(400)
        inp = pg.locator('#cv #lin'); inp.click(); inp.press_sequentially('HR-7731'); inp.press('Enter'); pg.wait_for_timeout(500)
        f.check('Your turn2 of 5' in pill(pg), 'Enter submits the typed lot')
        b.close()


PLAN = [('Type an ingredient lot and the trace starts there', 'HR-7731'),
        ('Every batch that used the lot, with the pounds it took', '3,000 of 3,000 lb'),
        ('Batches become cases, and cases become pallets', '6 pallets'),
        ('Each pallet ends at a customer or in the freezer', 'Northfield Foods'),
        ('Hold what is still in the freezer in one click', '6 held')]
f = run_card(1, PLAN, ['3 batches, 15 pallets, 2 customers, 6 held.'], start=start,
             extra={'before': {0: bad_then_type}, 'after_step': {0: s1, 1: s2, 2: s3, 3: s4, 4: s5}})
enter_submits(f)
finish(f)
