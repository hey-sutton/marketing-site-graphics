#!/usr/bin/env python3
"""Card 3 click through (both modes), numbers, layout and text checks. Run: python3 tools/apparel/test_card3.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from apparel_tests import run_card, js

B = [('XS', 1, 30), ('S', 2, 25), ('M', 2, 40), ('L', 5, 30), ('XL', 2, 25)]
assert sum(b[1] for b in B) == 12 and [b[1] * b[2] for b in B] == [30, 50, 80, 150, 50] and sum(b[1] * b[2] for b in B) == 360
assert 354 + 6 == 360 and round(354 * 0.85, 2) == 300.90 and 350 + 4 == 354
assert 350 / 50 == 7 and 350 + 6 + 4 == 360

def start(pg, f):
    f.check(js(pg, "return r.getElementById('iro').value") == 'R-4410, R-4411', 'step 1: rolls prefilled')
    f.check(js(pg, "return r.querySelectorAll('.bd').length") == 0, 'start: no bundles until the ticket is made')

def sew(pg, f):
    js(pg, "r.getElementById('igd').value='350'")
    pg.locator('#cv .hint').first.click(); pg.wait_for_timeout(400)
    f.check(js(pg, "return r.getElementById('fgd').classList.contains('err')"), 'step 3: good plus defects not 360 shows an inline error')
    f.check('Your turn3 of 6' in pg.locator('#cv .tbar .mode').text_content(), 'step 3: invalid count does not advance')
    js(pg, "r.getElementById('igd').value='354'")

def vend(pg, f):
    f.check(js(pg, "return r.getElementById('vch').textContent") == '$300.90', 'step 4: vendor charge $300.90 shown')

PLAN = [('A tag for every bundle', 'B12'),
        ('The count moves with the bundles', 'Sew'),
        ('Defects caught at sewing, by size', '354 good'),
        ('Pieces at a vendor stay on the books', 'Still in stock'),
        ('Back through receiving with a check', '350 ready'),
        ('Packed, with every held piece traced', 'RUN-0412 packed')]

f = run_card(3, PLAN, ['+350', 'C7', '$300.90', '10 pieces'], extra={'before': {0: start, 2: sew, 3: vend}})
print('\n%d failures' % len(f)); sys.exit(1 if f else 0)
