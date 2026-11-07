#!/usr/bin/env python3
"""Card 4 click through (both modes), numbers, layout and text checks. Run: python3 tools/electronics/test_card4.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from testlib import run_card, js

assert 6 + 5 + 3 == 14                                  # lot 2631 forward trace: 14 units, 3 customers
assert round(0.5 * 42.00, 2) == 21.00 and round(21.00 + 0.12, 2) == 21.12

def bad_serial(pg, f):
    f.check(js(pg, "return r.getElementById('isn').value") == 'SN-004187', 'step 1: serial prefilled SN-004187')
    f.check(js(pg, "return r.querySelectorAll('.nd').length") == 0, 'start: graph is empty until the trace runs')
    js(pg, "r.getElementById('isn').value='SN-999999'")
    pg.locator('#cv .hint').first.click(); pg.wait_for_timeout(400)
    f.check(js(pg, "return r.getElementById('fsn').classList.contains('err')"), 'step 1: an unknown serial shows an inline error')
    f.check('Your turn1 of 7' in pg.locator('#cv .tbar .mode').text_content(), 'step 1: unknown serial does not advance')
    js(pg, "r.getElementById('isn').value='SN-004187'")

def reason(pg, f):
    f.check(js(pg, "return r.getElementById('irs').value") == 'Intermittent reset', 'step 4: reason prefilled')

PLAN = [('Any serial, and exactly what went into it', 'SN-B-1127'),
        ('Down to the reel and the date code', 'R-0457'),
        ('Going the other way, every customer', 'Tern Audio'),
        ('The return starts from the serial', '10/09/2027'),
        ('Rework runs as its own order', 'lot 2640'),
        ('The repair is on the unit record', '$21.12'),
        ('One record from first build to repair', 'Shipped back 11/06')]

f = run_card(4, PLAN, ['RMA-0071', 'Closed', 'Shipped back 11/06'], extra={'before': {0: bad_serial, 3: reason}})
print('\n%d failures' % len(f)); sys.exit(1 if f else 0)
