#!/usr/bin/env python3
"""Card 2 click through (both modes), numbers, layout and text checks. Run: python3 tools/electronics/test_card2.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from testlib import run_card, js

assert 420 + 0 - 1150 == -730 and 5200 + 2000 - 6480 == 720 and 31000 - 24000 == 7000
assert 380 + 400 - 1100 == -320 and 900 - 750 == 150
assert 250 + 120 + 400 + 380 == 1150
assert 420 - 120 - 250 == 50 and 400 - 50 == 350 and 350 + 380 == 730   # MO-3110 is the first to run short
assert round(800 * 4.60, 2) == 3680.00 and -730 + 800 == 70
assert (730 + 99) // 100 * 100 == 800                                   # rounded up to the supplier multiple

def bad_qty(pg, f):
    js(pg, "var i=r.getElementById('iqt');i.value='750';")
    pg.locator('#cv .hint').first.click(); pg.wait_for_timeout(400)
    f.check(js(pg, "return r.getElementById('fqt').classList.contains('err')"), 'step 4: a quantity below the shortage shows an inline error')
    f.check('Your turn4 of 5' in pg.locator('#cv .tbar .mode').text_content(), 'step 4: invalid quantity does not advance')
    js(pg, "var i=r.getElementById('iqt');i.value='800';i.dispatchEvent(new Event('input',{bubbles:true}));")

def prefill(pg, f):
    f.check(js(pg, "return r.getElementById('iqt').value") == '800', 'step 4: quantity prefilled with 800')

PLAN = [('One filter shows every part that will stop a build', '−320'),
        ('See which builds compete for the same part', 'first build to run short'),
        ('The shortage becomes a purchase order', '$3,680.00'),
        ('Approval rules are built in', 'Approve as purchasing manager'),
        ('Approved and on order', 'PO-1048')]

def start(pg, f):
    pass

f = run_card(2, PLAN, ['PO-1048', '+70', '$3,680.00', 'Released'], extra={'before': {3: lambda pg, fl: (prefill(pg, fl), bad_qty(pg, fl))}})
print('\n%d failures' % len(f)); sys.exit(1 if f else 0)
