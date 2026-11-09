#!/usr/bin/env python3
"""Card 2 click through (both modes), numbers, layout and text checks. Run: python3 tools/plastics/test_card2.py
Rounding: whole pounds and whole caps."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from plastics_tests import run_card, js

assert 5000 + 6500 + 3000 == 14500 and 20000 - 14500 == 5500 and 2500 + 3000 == 5500
assert 120000 + 60000 == 180000 and 100000 + 135000 == 235000 and 40000 + 30000 + 40000 == 110000
assert 120000 + 100000 == 220000 and 60000 + 40000 == 100000 and 135000 + 30000 == 165000
assert 220000 + 100000 + 165000 == 485000 and 180000 + 235000 + 110000 == 525000 and 525000 - 485000 == 40000


def start(pg, f):
    f.check(js(pg, "return r.getElementById('ifl').value") == 'FL-7714', 'start: finished lot prefilled')
    f.check('Nothing traced yet' in js(pg, "return r.getElementById('det').innerText"), 'start: details empty until a trace')
    f.check(js(pg, "return r.querySelectorAll('.net path.on').length") == 0, 'start: no path drawn')
    js(pg, "r.getElementById('ifl').value='FL-1'")
    pg.locator('#cv .hint').first.click(); pg.wait_for_timeout(400)
    f.check(js(pg, "return r.getElementById('ffl').classList.contains('err')"), 'step 1: an unknown lot shows an inline error')
    js(pg, "r.getElementById('ifl').value='FL-7714'")


def back(pg, f):
    f.check(js(pg, "return r.querySelectorAll('.net path.on').length") == 5, 'step 1: four material lots into RUN-7714, then FL-7714')
    f.check(js(pg, "return r.querySelector('.nd.key b').textContent") == 'L-55120', 'step 1: L-55120 highlighted')


def lot(pg, f):
    f.check(js(pg, "return ['rcv','usd','lft'].map(function(k){return r.getElementById(k).textContent}).join('|')") == '20,000 lb|14,500 lb|5,500 lb', 'step 2: 20,000 received, 14,500 used, 5,500 left')


def fwd(pg, f):
    f.check(js(pg, "return ['AL','PW','HD'].map(function(k){return r.getElementById('c-'+k).textContent}).join('|')") == '220,000|100,000|165,000', 'step 3: 220,000, 100,000, 165,000 caps')
    f.check(js(pg, "return r.getElementById('mad').textContent+'|'+r.getElementById('shp').textContent") == '525,000|485,000', 'step 3: 525,000 made, 485,000 shipped')


def now(pg, f):
    f.check(js(pg, "return r.getElementById('rl').textContent+'|'+r.getElementById('fh').textContent") == '5,500 lb|40,000 caps', 'step 4: 5,500 lb and 40,000 caps on hand')
    f.check(js(pg, "return !r.getElementById('hn')"), 'step 4: nothing on hold yet')


def held(pg, f):
    f.check(js(pg, "return r.querySelectorAll('.det .ch.c-bad').length") >= 4, 'step 5: resin and caps on hold')


PLAN = [('Start from a part a customer reports', 'MB-3318'),
        ('Open a resin lot and see every run that used it', '14,500 lb'),
        ('Going the other way, you find every customer', '485,000'),
        ('The same lot is still on the shelf', 'RES-05'),
        ('Held stock cannot be picked, run or shipped', 'out of available stock'),
        ('The list of affected customers is ready to send', 'L-55120-customers.csv')]

f = run_card(2, PLAN, ['L-55120-customers.csv, 3 customers', '485,000', '10/30'], extra={'before': {0: start, 1: back, 2: lot, 3: fwd, 4: now, 5: held}})
print('\n%d failures' % len(f)); sys.exit(1 if f else 0)
