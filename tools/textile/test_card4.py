#!/usr/bin/env python3
"""Card 4 (two direction genealogy graph): the brief's numbers in Python, then the full click through in the browser.
Run: python3 tools/textile/test_card4.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from textile_tests import run_card, finish, js, pill, testlib
from playwright.sync_api import sync_playwright

# ---- the brief's numbers, derived independently of the card ----
assert 300 + 180 == 480
assert 360 + 744 + 480 + 768 == 2352


def ids(pg, *names):
    return js(pg, "return %r.map(function(i){var e=r.getElementById(i);return e?e.textContent:null}).join('|')" % list(names))


def start(pg, f, when='start'):
    t = js(pg, "return r.querySelector('.g4').innerText")
    f.check(js(pg, "return r.getElementById('lin').placeholder") == 'Enter a roll or lot number' and js(pg, "return r.getElementById('lin').value") == '', '%s: empty input "Enter a roll or lot number"' % when)
    f.check(js(pg, "return r.querySelectorAll('.nd').length") == 0, '%s: no nodes drawn' % when)
    f.check(not any(s in t for s in ('GR-1177', 'YL-7702', 'SO-3301', '2,352')), '%s: nothing derived from the input shows' % when)


def bad_then_type(pg, f):
    inp = pg.locator('#cv #lin')
    inp.click(); inp.press_sequentially('R-11111'); inp.press('Enter'); pg.wait_for_timeout(300)
    f.check(js(pg, "return r.getElementById('flin').classList.contains('err')"), 'step 1: an unknown number shows an inline error')
    inp.fill(''); inp.press_sequentially('R-48211'); pg.wait_for_timeout(100)


def nodes(pg):
    return js(pg, "return [].map.call(r.querySelectorAll('.nd .id'),function(e){return e.firstChild.textContent})")


def s1(pg, f):
    n = nodes(pg)
    f.check(n == ['YL-7702', 'YL-7715', 'GR-1177', 'CH-0931', 'CH-0944', 'DL-2611-B', 'R-48211'], 'step 1: the full backward graph (%s)' % n)
    f.check(js(pg, "return r.querySelector('.nd.sel .id').textContent") == 'R-48211', 'step 1: the roll is the selected node')
    rec = js(pg, "return r.getElementById('rec').innerText.replace(/\\s+/g,' ')")
    f.check(all(s in rec for s in ('DL-2611-B', '2,352 yd', 'GR-1177', '2,400 yd', 'YL-7702', 'Calder Fiber', '300 kg', 'YL-7715', 'Northfield Spinning', '180 kg')), 'step 1: record card with dye lot, greige, both yarn lots and suppliers')


def s2(pg, f):
    f.check(js(pg, "return r.querySelector('.nd.sel .id').textContent") == 'YL-7702', 'step 2: YL-7702 selected')
    f.check(ids(pg, 'fl0', 'fl1') == 'PDFYL-7702 test reportOct 2214 KB|PDFCalder Fiber scope certificateJan 15388 KB', 'step 2: test report and scope certificate attached')


def s3(pg, f):
    f.check(ids(pg, 'fq0', 'fq1', 'fq2', 'fq3') == '360 yd|744 yd|480 yd|768 yd', 'step 3: forward 360, 744, 480 and 768 in stock')
    f.check(ids(pg, 'ftot') == 'Forward 360 + 744 + 480 + 768 = 2,352 yd', 'step 3: the small total adds up to 2,352')
    rec = js(pg, "return r.getElementById('rec').innerText.replace(/\\s+/g,' ')")
    f.check(all(s in rec for s in ('SO-3301 Linden Apparel Works 360 yd', 'SO-3322 Harbor Home Textiles 744 yd', 'SO-3329 Pell Street Furnishings 480 yd', '768 yd')), 'step 3: shipments with customers and the stock')
    f.check(ids(pg, 'rtot') == 'Total 2,352 yd, matches the dye lot', 'step 3: total 2,352 yd matches the dye lot')


def s4(pg, f):
    f.check('AP-2611-B generated: 7 records, 4 forward links, 2 files' in ids(pg, 'apk'), 'step 4: the audit pack row')


def lot_sample(f):
    with sync_playwright() as p:
        b = testlib.browser(p)
        pg, errs = testlib.open_card(b, 4, 1300)
        pg.locator('#cv').scroll_into_view_if_needed()
        pg.locator('#cv .mtg [data-m="try"]').click(); pg.wait_for_timeout(300)
        pg.locator('#cv [data-v="DL-2611-B"]').click(); pg.locator('#cv #lin').press('Enter'); pg.wait_for_timeout(500)
        f.check('Your turn2 of 4' in pill(pg) and nodes(pg)[-1] == 'DL-2611-B', 'the DL-2611-B sample traces from the dye lot (Enter submits)')
        f.check(not errs, 'no page errors in the lot path')
        b.close()


PLAN = [('Type or scan any roll', 'GR-1177'),
        ('Attach supplier test reports and certificates', 'scope certificate'),
        ('Follow the lot forward', '2,352 yd'),
        ('Package the record', 'AP-2611-B')]

f = run_card(4, PLAN, ['2,352 yd', 'SO-3301', 'SO-3322', 'SO-3329', 'AP-2611-B'], start=start,
             extra={'before': {0: bad_then_type}, 'after_step': {0: s1, 1: s2, 2: s3, 3: s4}})
lot_sample(f)
finish(f)
