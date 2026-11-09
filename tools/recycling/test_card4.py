#!/usr/bin/env python3
"""Card 4 click through (both modes), numbers, layout, variety, navigation and phone checks. Run: python3 tools/recycling/test_card4.py
Rounding: whole pounds, money to cents."""
import os, sys
from decimal import Decimal as D
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from recycling_tests import run_all, js

assert 32 * 1250 == 40000 and 40000 * D('0.46') == D('18400.00') and 62540 - 22220 == 40320 and 40320 * D('0.46') == D('18547.20')


def start(pg, f):
    f.check(js(pg, "return r.querySelector('.fwin').getAttribute('data-scr')") == 'Sales orders', 'start: the sales order list')
    f.check('18,400' not in js(pg, "return r.querySelector('.fwin').innerText"), 'start: no order total before the price is set')


def price(pg, f):
    f.check(js(pg, "return r.getElementById('ip').value") == '0.46', 'step 2: price prefilled')
    f.check('After the price' in js(pg, "return r.getElementById('tot').textContent"), 'step 2: total hidden until the price is used')
    js(pg, "var e=r.getElementById('ip');e.value='free';e.dispatchEvent(new Event('input',{bubbles:true}))")
    pg.locator('#cv .hint').first.click(); pg.wait_for_timeout(400)
    f.check(js(pg, "return r.getElementById('fp').classList.contains('err')"), 'step 2: a bad price shows an inline error')
    js(pg, "var e=r.getElementById('ip');e.value='0.46';e.dispatchEvent(new Event('input',{bubbles:true}))")


def scan(pg, f):
    f.check(js(pg, "return r.getElementById('tot').textContent") == '18,400.00', 'step 2: 40,000 lb at 0.46 is 18,400.00')
    f.check(js(pg, "return r.getElementById('isc').value") == 'G-4412', 'step 3: gaylord prefilled in the scan field')


def picked(pg, f):
    f.check(js(pg, "return r.getElementById('pkd').textContent") == '32 of 32 picked', 'step 3: 32 of 32 picked')


def weighed(pg, f):
    f.check(js(pg, "return r.getElementById('net').textContent+'|'+r.getElementById('cq').textContent+'|'+r.getElementById('ctot').textContent") == '40,320 lb|40,320|18,547.20', 'step 4: net 40,320 lb, corrected to 18,547.20')


def docs(pg, f):
    f.check(js(pg, "return r.getElementById('bln').textContent+'|'+r.getElementById('itot').textContent") == '40,320|18,547.20', 'step 5: BL-5520 with 40,320 lb, invoice total 18,547.20')


def end(pg, f):
    f.check('CR-1190' in js(pg, "return r.getElementById('cr').textContent") and '18,547.20' in js(pg, "return r.getElementById('inv').textContent"), 'step 6: certificate CR-1190 and invoice for 18,547.20')


PLAN = [("Open a buyer's order", 'Brightfield Extrusion'),
        ('The price is set for this load', '18,400.00'),
        ('Scan to pick the right gaylords', '32 of 32 picked'),
        ('Correct the order to what the scale says', '18,547.20'),
        ('The bill of lading prints from the order', 'BL-5520'),
        ('One click ships it, with the certificate attached', 'Certificate CR-1190 issued')]

f = run_all(4, PLAN, ['CR-1190', 'INV-6630', '18,547.20', '40,320'], extra={'before': {0: start, 1: price, 2: scan, 3: picked, 4: weighed, 5: docs}, 'after': end})
print('\n%d failures' % len(f)); sys.exit(1 if f else 0)
