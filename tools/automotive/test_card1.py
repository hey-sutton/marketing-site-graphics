#!/usr/bin/env python3
"""Card 1 (genealogy graph): the brief's numbers in Python, then the full click through in the browser.
Run: python3 tools/automotive/test_card1.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from auto_tests import run_card, finish, js, pill, testlib
from playwright.sync_api import sync_playwright

# ---- the brief's numbers, derived independently of the card ----
LOT = 12000
WO = {'WO-7102': 4800, 'WO-7108': 4200, 'WO-7115': 3000}
PER = 2
FGL = {'FGL-0912': 2400, 'FGL-0913': 2100, 'FGL-0914': 1500}
SHIP = {'FGL-0912': [('SH-5521', 'Plant North', 2400)], 'FGL-0913': [('SH-5530', 'Plant North', 1800)], 'FGL-0914': [('SH-5534', 'Plant South', 900)]}
assert 4800 + 4200 + 3000 == sum(WO.values()) == LOT == 12000
for (w, f) in zip(WO, FGL):
    assert FGL[f] * PER == WO[w]            # each lot x 2 = fasteners
assert 2400 + 2100 + 1500 == sum(FGL.values()) == 6000
SHIPPED = sum(q for v in SHIP.values() for _, _, q in v)
ONHAND = {f: FGL[f] - sum(q for _, _, q in SHIP[f]) for f in FGL}
assert SHIPPED == 5100 and ONHAND == {'FGL-0912': 0, 'FGL-0913': 300, 'FGL-0914': 600}
assert 5100 + 900 == 6000 == SHIPPED + sum(ONHAND.values())


def ids(pg, *names):
    return js(pg, "return %r.map(function(i){var e=r.getElementById(i);return e?e.textContent:null}).join('|')" % list(names))


def start(pg, f, when='start'):
    t = js(pg, "return r.querySelector('.g1').innerText")
    f.check(js(pg, "return r.getElementById('lin').value") == '', '%s: the suspect lot input is empty' % when)
    f.check(js(pg, "return r.querySelectorAll('.nd,.tl').length") == 0, '%s: no graph nodes and no totals' % when)
    f.check(not any(s in t for s in ('12,000', 'WO-', 'FGL-', '6,000', '5,100', '900')), '%s: nothing derived from the lot shows' % when)


def bad_then_type(pg, f):
    inp = pg.locator('#cv #lin')
    inp.click(); inp.press_sequentially('SL-9999'); inp.press('Enter'); pg.wait_for_timeout(300)
    f.check(js(pg, "return r.getElementById('flin').classList.contains('err')"), 'step 1: an unknown lot shows an inline error')
    f.check('Your turn1 of 5' in pill(pg), 'step 1: an unknown lot does not advance')
    inp.fill(''); inp.press_sequentially('sl-4471'); pg.wait_for_timeout(100)
    f.check(js(pg, "return r.getElementById('lin').value") == 'sl-4471', 'step 1: typing works in the input')


def s1(pg, f):
    t = js(pg, "return r.getElementById('gph').innerText")
    f.check('SL-4471' in t and 'FST-118, 12,000 pcs' in t and 'Ridgefield Fasteners' in t, 'step 1: lot node SL-4471, FST-118, 12,000 pcs, Ridgefield Fasteners')
    f.check(js(pg, "return r.querySelectorAll('.nd').length") == 1, 'step 1: only the lot so far')


def s2(pg, f):
    f.check(ids(pg, 'wq0', 'wq1', 'wq2') == '4,800 fasteners|4,200 fasteners|3,000 fasteners', 'step 2: WO-7102 4,800, WO-7108 4,200, WO-7115 3,000')
    f.check(ids(pg, 'wol') == 'Work orders, 12,000 of 12,000 used', 'step 2: 12,000 of 12,000 used')


def s3(pg, f):
    f.check(ids(pg, 'fq0', 'fq1', 'fq2') == '2,400 assemblies|2,100 assemblies|1,500 assemblies', 'step 3: FGL-0912 2,400, FGL-0913 2,100, FGL-0914 1,500')
    f.check(ids(pg, 'fgl', 't-blt') == 'Finished lots, 6,000 built|6,000', 'step 3: 6,000 built')


def s4(pg, f):
    f.check(ids(pg, 'lf0', 'lf1', 'lf2', 'lf3', 'lf4') == 'Plant North, 2,400|Plant North, 1,800|Finished goods, 300|Plant South, 900|Finished goods, 600', 'step 4: shipments and on hand per lot')
    f.check(ids(pg, 't-shp', 't-oh') == '5,100|900', 'step 4: 5,100 shipped, 900 on hand')


def s5(pg, f):
    f.check(ids(pg, 'cst', 'csum') == 'Quarantined|6,000 built, 5,100 shipped, 900 held.', 'step 5: Quarantined, 6,000 built, 5,100 shipped, 900 held')
    f.check(js(pg, "return r.querySelectorAll('.nd.hold').length") == 2, 'step 5: both on hand lots marked Held')


def enter_submits(f):
    with sync_playwright() as p:
        b = testlib.browser(p)
        pg, errs = testlib.open_card(b, 1, 1300)
        pg.locator('#cv').scroll_into_view_if_needed()
        pg.locator('#cv .mtg [data-m="try"]').click(); pg.wait_for_timeout(400)
        inp = pg.locator('#cv #lin'); inp.click(); inp.press_sequentially('SL-4471'); inp.press('Enter'); pg.wait_for_timeout(500)
        f.check('Your turn2 of 5' in pill(pg) and 'SL-4471' in js(pg, "return r.getElementById('gph').innerText"), 'Enter submits the typed lot')
        pg.close()
        pg, errs = testlib.open_card(b, 1, 1300)
        pg.locator('#cv').scroll_into_view_if_needed()
        pg.locator('#cv .mtg [data-m="try"]').click(); pg.wait_for_timeout(400)
        pg.locator('#cv #smp').click(); pg.wait_for_timeout(100)
        f.check(js(pg, "return r.getElementById('lin').value") == 'SL-4471', 'the sample button fills SL-4471')
        b.close()


PLAN = [('Type a suspect lot and the trace starts at the supplier lot', 'SL-4471'),
        ('See every work order that consumed the lot', '12,000 of 12,000 used'),
        ('Each work order leads to the finished lots it built', '6,000 built'),
        ('Then to every shipment, and what is still on the shelf', '5,100'),
        ('Hold what is still in the plant in one click', '900 held')]

f = run_card(1, PLAN, ['6,000 built, 5,100 shipped, 900 held.', 'Quarantined'], start=start,
             extra={'before': {0: bad_then_type}, 'after_step': {0: s1, 1: s2, 2: s3, 3: s4, 4: s5}})
enter_submits(f)
finish(f)
