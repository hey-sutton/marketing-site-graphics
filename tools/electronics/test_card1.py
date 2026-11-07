#!/usr/bin/env python3
"""Card 1 click through (both modes), numbers, layout and text checks. Run: python3 tools/electronics/test_card1.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from testlib import run_card, js

# the arithmetic the card shows, in cents
L = [320, 460, 18 * 12, 64 * 1, 2 * 135, 3 * 90]
assert L == [320, 460, 216, 64, 270, 270] and sum(L) == 1600          # 3.20+4.60+2.16+0.64+2.70+2.70 = 16.00
assert 1600 + 450 == 2050 and 2050 + 625 + 1140 == 3815             # board 20.50, unit 38.15
assert 1600 - 216 + 18 * 15 == 1654 and 1654 + 450 == 2104          # rev D board material 16.54, board 21.04
assert 2104 + 625 + 1140 == 3869 and 3869 - 3815 == 54              # unit 38.69, up 0.54
assert 54 * 250 == 13500 and 54 * 400 == 21600 and 13500 + 21600 == 35100   # 135.00, 216.00, 351.00

def bad_input(i):
    def f(pg, fl):
        # an invalid replacement shows an inline error and does not advance; fixing it does
        js(pg, "var i=r.getElementById('rw');i.value='CAP-9999';")
        pg.locator('#cv .hint').first.click(); pg.wait_for_timeout(400)
        fl.check(js(pg, "return r.getElementById('frw').classList.contains('err')"), 'step 3: invalid part shows an inline error')
        fl.check('Your turn3 of 6' in pg.locator('#cv .tbar .mode').text_content(), 'step 3: invalid input does not advance')
        js(pg, "var i=r.getElementById('rw');i.value='CAP-1007';")
    return f

def leave_and_back(pg, fl):
    pass

PLAN = [('Each level is costed on its own', 'PCB-210'),
        ('Unit cost rolls up from every level', '$38.15'),
        ('Every change is a new revision', '+$0.54'),
        ('See the builds a change touches first', 'Will switch to rev D'),
        ('Released, without stopping the line', 'Finish on rev C'),
        ('You saw what one part change costs', '$38.69')]

def back_check(pg, fl):
    pass

def before4(pg, fl):
    # leave the Revisions tab: the prompt must point back to it
    js(pg, "r.querySelectorAll('.tab')[0].click()")
    pg.wait_for_timeout(300)
    fl.check('Back to Revisions' in pg.locator('#cv .cap.turn').inner_text(), 'step 4: leaving the tab re-points the prompt to Revisions')
    pg.locator('#cv .hint').first.click(); pg.wait_for_timeout(300)

f = run_card(1, PLAN, ['$38.69', '$21.04', '+$135.00', '+$216.00', '+$351.00'], extra={'before': {2: bad_input(2), 3: before4}})
print('\n%d failures' % len(f)); sys.exit(1 if f else 0)
