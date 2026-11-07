#!/usr/bin/env python3
"""Card 2 click through (both modes), numbers, layout and text checks. Run: python3 tools/apparel/test_card2.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from apparel_tests import run_card, js

assert 140.0 + 120.0 == 260.0 and 260.0 + 150.0 == 410.0
assert 140.0 + 55.0 == 195.0 and 1.3 * 150 == 195.0
assert 140.0 + 52.0 == 192.0 and 195.0 - 192.0 == 3.0
assert 120.0 - 52.0 == 68.0 and 0.0 + 68.0 + 150.0 == 218.0 == 410.0 - 192.0

def start(pg, f):
    f.check(js(pg, "return r.getElementById('koh').textContent") == '260.0 yd', 'start: on hand 260.0 yd')
    f.check(js(pg, "return [r.getElementById('ir1').value,r.getElementById('ir2').value,r.getElementById('ir4').value].join(' ')") == 'R-4417 150.0 NAV-2618', 'step 1: receiving prefilled')
    js(pg, "r.getElementById('ir4').value='blue'")
    pg.locator('#cv .hint').first.click(); pg.wait_for_timeout(400)
    f.check(js(pg, "return r.getElementById('fr4').classList.contains('err')"), 'step 1: a bad dye lot shows an inline error')
    js(pg, "r.getElementById('ir4').value='NAV-2618'")

def s2(pg, f):
    f.check(js(pg, "return r.getElementById('koh').textContent") == '410.0 yd', 'step 2: on hand 410.0 yd after receiving')

PLAN = [('Each roll arrives with its own dye lot', 'R-4417'),
        ('Yardage set aside from one dye lot', '195.0 yd'),
        ('A roll from another dye lot is flagged', 'does not match'),
        ('The right roll goes through', 'Cut done'),
        ('Leftover yardage goes back to the roll', 'now 68.0 yd')]

f = run_card(2, PLAN, ['218.0 yd', '68.0', '192.0 yd', '3.0 yd back to R-4411'], extra={'before': {0: start, 1: s2}})
print('\n%d failures' % len(f)); sys.exit(1 if f else 0)
