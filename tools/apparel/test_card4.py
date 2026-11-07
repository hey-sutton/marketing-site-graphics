#!/usr/bin/env python3
"""Card 4 click through (both modes), numbers, layout and text checks. Run: python3 tools/apparel/test_card4.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from apparel_tests import run_card, js

Q, NAVY = [6, 12, 24, 8, 6], [18, 44, 70, 9, 31]
assert sum(Q) == 56 and round(56 * 11.50, 2) == 644.00
assert round(644.00 * 0.30, 2) == 193.20 and round(644.00 - 193.20, 2) == 450.80 and 56 / 2 == 28
assert [a - b for a, b in zip(NAVY, Q)] == [12, 32, 46, 1, 25]

def start(pg, f):
    f.check(js(pg, "return r.getElementById('icu').value") == 'Pinegate Outfitters', 'step 1: customer prefilled')
    f.check('No reservations' in js(pg, "return r.getElementById('sk').innerText"), 'start: stock reservation empty until its step')
    js(pg, "r.getElementById('icl').value='Red'")
    pg.locator('#cv .hint').first.click(); pg.wait_for_timeout(400)
    f.check(js(pg, "return r.getElementById('fcl').classList.contains('err')"), 'step 1: an unknown color shows an inline error')
    js(pg, "r.getElementById('icl').value='Navy'")

def before_res(pg, f):
    f.check('No reservations' in js(pg, "return r.getElementById('sk').innerText"), 'step 2: stock still unreserved before the click')

def dep(pg, f):
    f.check(js(pg, "return r.getElementById('dam').textContent") == '$193.20', 'step 3: deposit 30% shows $193.20')
    f.check(js(pg, "var t=r.getElementById('sk').innerText;return /L\\s+9\\s+8\\s+1/.test(t)"), 'step 3: size L online availability is 1 after the reservation')

PLAN = [('Taken by size run, at the wholesale price', '$644.00'),
        ('Reserved, so nothing sells twice', 'SO-6120 holds 56'),
        ('The deposit syncs to accounting', 'Synced to accounting'),
        ('Every piece scanned against the order', '56 picked'),
        ('Packed, shipped and invoiced', 'PS-6120')]

f = run_card(4, PLAN, ['$644.00', '$193.20', '$450.80', 'Balance due, invoiced'], extra={'before': {0: start, 1: before_res, 2: dep}})
print('\n%d failures' % len(f)); sys.exit(1 if f else 0)
