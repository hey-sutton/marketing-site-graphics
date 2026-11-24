#!/usr/bin/env python3
"""Card 1 click through (both modes), numbers, layout, variety, timing, navigation and phone checks.
Run: python3 tools/distilleries/test_card1.py. The brief's sums are asserted in numbers_check.py first."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numbers_check  # noqa: F401  (asserts mash bill totals, 346.00, 3.25, 19.50, 20.35, 692.00)
from distilleries_tests import run_all, js, testlib
from playwright.sync_api import sync_playwright


def txt(pg, ids):
    return js(pg, "return %r.map(function(i){var e=r.getElementById(i);return e?e.textContent:null}).join('|')" % ids)


def start(pg, f):
    f.check(js(pg, "return r.querySelector('.fwin').getAttribute('data-scr')") == 'SKU search', 'start: the empty SKU search')
    t = js(pg, "return r.getElementById('pg').innerText")
    f.check(js(pg, "return r.querySelectorAll('.tr,.cp').length") == 0 and '$' not in t, 'start: no tree and no cost before a SKU is picked')
    f.check(js(pg, "return r.getElementById('iq').value") == '', 'start: the SKU field is empty')


def bad(pg, f):
    start(pg, f)
    js(pg, "var e=r.getElementById('iq');e.value='Vodka 1 L';e.dispatchEvent(new Event('input',{bubbles:true}))")
    pg.locator('#cv #iq').press('Enter'); pg.wait_for_timeout(300)
    f.check(js(pg, "return r.getElementById('fs').classList.contains('err')"), 'step 1: a SKU that does not exist shows an inline error')
    js(pg, "var e=r.getElementById('iq');e.value='';e.dispatchEvent(new Event('input',{bubbles:true}))")


def bottle(pg, f):
    f.check(txt(pg, ['p-btl', 'p-6', 'p-case']) == '$3.25|$19.50|$20.35', 'step 1: bottle $3.25, 6 bottles $19.50, case $20.35')


def batch(pg, f):
    f.check(txt(pg, ['g0', 'g1', 'g2', 'p-gr', 'p-bt', 'p-pl']) == '$196.00|$88.00|$62.00|$346.00|$2,000.00|$4.00', 'step 3: grain 196 + 88 + 62 = $346.00, batch $2,000.00, $4.00 per liter')
    t = testlib.win_text(pg)
    f.check(all(x in t for x in ('1,400 lb', '400 lb', '200 lb', '70%', '20%', '10%', '$24.00', '$1,630.00')), 'step 3: 1,400, 400 and 200 lb at 70, 20 and 10%, yeast $24.00, labor $1,630.00')


def end(pg, f):
    f.check(txt(pg, ['g0', 'g1', 'g2', 'p-gr', 'p-bt', 'p-pl', 'p-btl']) == '$392.00|$176.00|$124.00|$692.00|$4,000.00|$4.00|$3.25', 'step 4: 4,000 lb mash, grain $692.00, still $4.00 per liter and $3.25 a bottle')
    t = testlib.win_text(pg)
    f.check(all(x in t for x in ('2,800 lb', '800 lb', '400 lb', '1,000 L')), 'step 4: corn 2,800, rye 800, malted barley 400 lb, 1,000 L')
    f.check('DS-0371' in t and 'v2' in t, 'versions: v2 listed with its batches')


def enter(f):
    with sync_playwright() as p:
        b = testlib.browser(p)
        for vw, cw, lab in ((1300, 604, 'desktop'), (390, 358, 'phone')):
            pg, errs = testlib.open_card(b, 1, vw, cw)
            pg.locator('#cv').scroll_into_view_if_needed()
            pg.locator('#cv .mtg [data-m="try"]').click(); pg.wait_for_timeout(500)
            pg.locator('#cv #iq').click(); pg.keyboard.type('barrel rye 750 ml'); pg.keyboard.press('Enter'); pg.wait_for_timeout(700)
            f.check(js(pg, "return r.querySelector('.fwin').getAttribute('data-scr')") == 'BOM tree', '%s: typing the SKU and pressing Enter opens the BOM' % lab)
            f.check(not errs, '%s typing: no page errors' % lab)
            pg.close()
        b.close()


PLAN = [('The BOM opens at the bottle', '$20.35'), ('The blend opens to its distillate', '450 ml'),
        ('The distillate opens to its batch and mash bill', '$2,000.00'), ('Every quantity scales with the mash', '$692.00')]
f = run_all(1, PLAN, ['$692.00', '2,800 lb'], extra={'before': {0: bad, 1: bottle, 3: batch}, 'after': end}, drag=enter, start=start)
print('\n%d failures' % len(f)); sys.exit(1 if f else 0)
