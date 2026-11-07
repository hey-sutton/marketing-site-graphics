#!/usr/bin/env python3
"""Card 4 click through (both modes), numbers, layout and text checks. Run: python3 tools/distribution/test_card4.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from distribution_tests import run_card, js

L = [(24, 7.40, 8.50), (12, 18.00, 18.00), (6, 9.50, 9.50)]
assert sum(q for q, _, _ in L) == 42
amts = [round(q * p, 2) for q, p, _ in L]
assert amts == [177.60, 216.00, 57.00] and round(sum(amts), 2) == 450.60
assert round(24 * (8.50 - 7.40), 2) == 26.40


def start(pg, f):
    f.check(js(pg, "return r.querySelectorAll('.inb button.row').length") == 1, 'start: rep view shows one order')
    f.check('No order open' in js(pg, "return r.getElementById('ord').innerText"), 'start: order panel empty')
    f.check('Nothing to pick' in js(pg, "return r.getElementById('pk').innerText"), 'start: pick route empty until release')
    f.check(js(pg, "return r.getElementById('ipk').value+'|'+r.getElementById('imd').value") == '1 pallet|LTL', 'start: shipping prefilled')
    f.check('450.60' not in js(pg, "return r.querySelector('.fwin').innerText"), 'start: no order total before it opens')


def inbox(pg, f):
    f.check(js(pg, "return [].map.call(r.querySelectorAll('.inb .l1 .cn'),function(e){return e.textContent}).join(',')") == 'Rep,Portal,Marketplace,EDI', 'step 1: four orders, four channel chips')


def scan(pg, f):
    f.check(js(pg, "return r.getElementById('isc').value") == 'TW-331', 'step 4: look-alike SKU prefilled')
    js(pg, "var e=r.getElementById('isc');e.value='hello';e.dispatchEvent(new Event('input',{bubbles:true}))")
    pg.locator('#cv .hint').first.click(); pg.wait_for_timeout(400)
    f.check(js(pg, "return r.getElementById('fsc').classList.contains('err')"), 'step 4: a malformed scan shows an inline error')
    js(pg, "var e=r.getElementById('isc');e.value='TW-331';e.dispatchEvent(new Event('input',{bubbles:true}))")


def flagged(pg, f):
    f.check(js(pg, "return !!r.getElementById('flag')&&r.getElementById('pkc').textContent") == '0 of 42 picked', 'step 4: flagged, nothing picked')


def before_ship(pg, f):
    f.check(js(pg, "return r.getElementById('pkc').textContent") == '42 of 42 picked', 'step 5: 42 of 42 picked')
    f.check(js(pg, "return r.querySelectorAll('.ord .ok2').length") == 3, 'step 5: every line ticked')


def end(pg, f):
    t = js(pg, "return r.querySelector('.fwin').innerText")
    f.check('on hand' not in t.lower() and 'available' not in t.lower(), 'end: no stock figures shown after shipping')
    f.check(js(pg, "return r.getElementById('opc').textContent+'|'+r.getElementById('otot').textContent") == '42|450.60', 'end: 42 pieces, 450.60')


PLAN = [('Rep, portal, marketplace and EDI orders land in one inbox', 'Northgate Retail'),
        ("The customer's own price list is applied", '26.40'),
        ('The order releases to pick along the shortest bin route', 'C-03-1'),
        ('A scan that does not match the order is flagged', 'not on this order'),
        ('The right items go in, line by line', '42 of 42 picked'),
        ('The packing slip and bill of lading come from the order', 'BL-3301')]

f = run_card(4, PLAN, ['450.60', '177.60', '216.00', '57.00', '26.40', 'PS-3301', 'Shipped'], extra={'before': {0: start, 1: inbox, 3: scan, 4: flagged, 5: before_ship}, 'after': end})
print('\n%d failures' % len(f)); sys.exit(1 if f else 0)
