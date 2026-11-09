#!/usr/bin/env python3
"""Card 1 click through (both modes), numbers, layout, variety, navigation and phone checks. Run: python3 tools/recycling/test_card1.py
Rounding: whole pounds."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from recycling_tests import run_all, js

assert 41260 - 14980 == 26280 and 12 * 2190 == 26280 and 41500 + 26280 == 67780


def start(pg, f):
    f.check(js(pg, "return r.querySelector('.fwin').getAttribute('data-scr')") == 'Inbound loads', 'start: the inbound loads list')
    f.check('26,280' not in js(pg, "return r.querySelector('.fwin').innerText"), 'start: no net weight before the reading')


def gross(pg, f):
    f.check(js(pg, "return r.getElementById('ig').value") == '41,260', 'step 2: gross prefilled from the scale')
    f.check('After the reading' in js(pg, "return r.getElementById('net').textContent"), 'step 2: net hidden until the reading is used')
    js(pg, "var e=r.getElementById('ig');e.value='9,000';e.dispatchEvent(new Event('input',{bubbles:true}))")
    pg.locator('#cv .hint').first.click(); pg.wait_for_timeout(400)
    f.check(js(pg, "return r.getElementById('fg').classList.contains('err')"), 'step 2: a gross under the tare shows an inline error')
    js(pg, "var e=r.getElementById('ig');e.value='41,260';e.dispatchEvent(new Event('input',{bubbles:true}))")


def net(pg, f):
    f.check(js(pg, "return r.getElementById('net').textContent") == '26,280 lb', 'step 2: net 26,280 lb')


def labels(pg, f):
    f.check(js(pg, "return r.getElementById('po').textContent").startswith('PO-7710 created'), 'step 4: PO-7710 created')
    f.check(js(pg, "return !!r.getElementById('mi-lab')"), 'step 5: the more menu opens to the label item')


def lab_done(pg, f):
    f.check(js(pg, "return r.getElementById('per').textContent+'|'+r.getElementById('lt').textContent+'|'+r.querySelectorAll('.lb').length") == '2,190 lb each|26,280 lb in all|12', 'step 5: 12 labels of 2,190 lb, 26,280 lb')


def end(pg, f):
    f.check(js(pg, "return r.getElementById('ppv').textContent") == '67,780', 'step 6: PP mixed scrap 67,780 lb')


PLAN = [('Open any inbound load from the list', 'Use reading'),
        ('The scale reading drops in', '26,280 lb'),
        ('Photos and a contamination note stay with the load', 'Metal inserts in two pallets'),
        ('Received first, and the purchase order follows', 'PO-7710 created'),
        ('Every pallet gets its own serialized label', 'PL-2291-12'),
        ('The load lands in stock by grade and bin', '67,780')]

f = run_all(1, PLAN, ['67,780', 'LD-2291 added 26,280 lb to Y1-03'], extra={'before': {0: start, 1: gross, 2: net, 4: labels, 5: lab_done}, 'after': end})
print('\n%d failures' % len(f)); sys.exit(1 if f else 0)
