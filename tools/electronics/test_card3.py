#!/usr/bin/env python3
"""Card 3 click through (both modes), numbers, layout and text checks. Run: python3 tools/electronics/test_card3.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from testlib import run_card, js

assert 9 + 1 == 10                       # 10 units = 9 good + 1 rework
assert 18 * 10 == 180 and 1 * 10 == 10   # CAP-1006 and MCU-STM32 deducted
assert len([1, 1, 18, 64, 2, 3]) == 6    # kit lines 6 of 6
assert [q * 10 for q in [1, 1, 18, 64, 2, 3]] == [10, 10, 180, 640, 20, 30]

def bad_supply(pg, f):
    f.check(js(pg, "return r.getElementById('sv').value") == '5.02', 'step 4: supply prefilled 5.02')
    js(pg, "r.getElementById('sv').value='5.40'")
    pg.locator('#cv .hint').first.click(); pg.wait_for_timeout(400)
    f.check(js(pg, "return r.getElementById('fsv').classList.contains('err')"), 'step 4: a reading outside the limit shows an inline error')
    f.check('Your turn4 of 6' in pg.locator('#cv .tbar .mode').text_content(), 'step 4: invalid reading does not advance')
    js(pg, "r.getElementById('sv').value='5.02'")

def prefilled_scan(pg, f):
    f.check(js(pg, "return [r.getElementById('kp').value,r.getElementById('kl').value,r.getElementById('kr').value].join(' ')") == 'CAP-1006 2631 R-0457', 'step 1: scan prefilled CAP-1006, lot 2631, reel R-0457')
    f.check('5 of 6 lines' in pg.locator('#cv .fwin').inner_text(), 'start: kit shows 5 of 6 lines')

PLAN = [('Scan to kit, and the reel is tied to the build', '6 of 6 lines'),
        ('Each station sees its own queue', 'SMT line 1'),
        ('Builds move station by station', 'Testing 8 of 10'),
        ('Test results are saved on the serial', 'SN-004212 passed'),
        ('A failed unit goes to rework with its reason', 'No boot, from test'),
        ('Good units in stock, components deducted', 'B-01 closed')]

f = run_card(3, PLAN, ['+9', 'CAP-1006', '180', 'Batch closed'], extra={'before': {0: prefilled_scan, 3: bad_supply}})
print('\n%d failures' % len(f)); sys.exit(1 if f else 0)
