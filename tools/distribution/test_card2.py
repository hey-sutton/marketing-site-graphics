#!/usr/bin/env python3
"""Card 2 click through (both modes), numbers, layout and text checks. Run: python3 tools/distribution/test_card2.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from distribution_tests import run_card, js

SHIP = [120, 80, 100, 60]
assert sum(SHIP) == 360 and 400 - 360 == 40 and 30 + 10 == 40
assert 190 - 40 == 150   # card 1 ended with GL-210 available 190


def start(pg, f):
    f.check(js(pg, "return r.getElementById('isn').value+'|'+r.getElementById('ilt').value") == 'SN-7714|L-24091', 'start: serial and lot prefilled')
    f.check('Nothing traced yet' in js(pg, "return r.getElementById('det').innerText"), 'start: details empty until a trace')
    f.check(js(pg, "return r.querySelectorAll('.net path.on').length") == 0, 'start: no path drawn')
    js(pg, "r.getElementById('isn').value='SN-0000'")
    pg.locator('#cv .hint').first.click(); pg.wait_for_timeout(400)
    f.check(js(pg, "return r.getElementById('fsn').classList.contains('err')"), 'step 1: an unknown serial shows an inline error')
    js(pg, "r.getElementById('isn').value='SN-7714'")


def path(pg, f):
    f.check(js(pg, "return r.querySelectorAll('.net path.on').length") == 2, 'step 1: path drawn in two legs, supplier to warehouse to customer')
    js(pg, "r.getElementById('ilt').value='L-1'")
    pg.locator('#cv .hint').first.click(); pg.wait_for_timeout(400)
    f.check(js(pg, "return r.getElementById('flt').classList.contains('err')"), 'step 2: an unknown lot shows an inline error')
    js(pg, "r.getElementById('ilt').value='L-24091'")


def lot(pg, f):
    f.check(js(pg, "return r.getElementById('rcv').textContent+'|'+r.getElementById('shp').textContent") == '400|360', 'step 2: 400 received, 360 shipped')
    f.check(js(pg, "return r.getElementById('lft').textContent") == 'Not checked', 'step 2: shelf stock not shown before its step')


def held(pg, f):
    f.check(js(pg, "var n=0;r.querySelectorAll('.det .sh~.row .mono.r').forEach(function(e){n+=+e.textContent});return r.getElementById('lft').textContent+'|'+n") == '40|40', 'step 3: 40 left on the shelf')


def before_exp(pg, f):
    f.check(js(pg, "return r.getElementById('av2').textContent") == '190 to 150', 'step 4: available to sell drops by 40, 190 to 150')
    f.check(js(pg, "return r.querySelectorAll('.det .ch.c-bad').length>=3"), 'step 4: both shelf rows on hold')


PLAN = [('Pick a serial and see its whole path', 'Calder Clinic'),
        ('Open a lot and see where every unit went', '360'),
        ('The same lot is still on the shelf in two warehouses', 'D-02-3'),
        ('Held stock cannot be picked or sold', '190 to 150'),
        ('The list of affected customers is ready to send', 'L-24091-customers.csv')]

f = run_card(2, PLAN, ['400', '360', '40', 'L-24091-customers.csv, 4 customers', '10/29'], extra={'before': {0: start, 1: path, 2: lot, 3: held, 4: before_exp}})
print('\n%d failures' % len(f)); sys.exit(1 if f else 0)
