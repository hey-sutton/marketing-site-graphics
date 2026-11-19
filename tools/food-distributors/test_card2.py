#!/usr/bin/env python3
"""Card 2 (list and detail): the README's lot numbers in Python, then the click through.
Run: python3 tools/food-distributors/test_card2.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fd_tests import run_card, finish, js, ids, readonly_checks, keyboard_walk, clicks_only

RECEIVED = 2000
SHIPPED = {'Greenfield Market': 600, 'Harbor Deli': 450, 'Corner Pantry': 250}
REMAINING = 700
TRACE = {'L-24-0817': 200, 'L-24-0822': 100}
assert sum(SHIPPED.values()) == 1300                       # shipped is the sum of the three customer rows
assert RECEIVED == sum(SHIPPED.values()) + REMAINING       # 2,000 = 1,300 + 700
ALLOC = {'SO-3110': 200, 'SO-3112': 120}
assert ALLOC['SO-3110'] == TRACE['L-24-0817']                # SO-3110 takes 200 from this lot, as the trace shows
assert REMAINING - sum(ALLOC.values()) == 380                # free to allocate
assert sum(TRACE.values()) == 300                          # SO-3110 carries 300 cases across its two lots


def start(pg, f, when='start'):
    readonly_checks(pg, f, {'ilt': 'L-24-0817'}, when)
    f.check(js(pg, "return r.querySelectorAll('.facts,.qty,#shp,#trc,#pvw').length") == 0, '%s: no lot record shown' % when)
    t = js(pg, "return r.getElementById('dt').innerText+r.getElementById('rs').innerText")
    f.check(not any(s in t for s in ('2,000', '1,300', '700', 'B-12-3', 'Penne Pasta 20 lb Case')), '%s: nothing derived shows' % when)


def s1(pg, f):
    f.check(js(pg, "return !!r.getElementById('r-L-24-0817')") and js(pg, "return r.querySelectorAll('.facts').length") == 0, 'step 1: the lot is found, the record is not open yet')


def s2(pg, f):
    f.check(ids(pg, 'fbin', 'fexp', 'qrc', 'qsh', 'qrm', 'wbq') == 'B-12-3|Mar 15, 2027|2,000|1,300|700|700', 'step 2: stored in B-12-3, 2,000 received, 1,300 shipped, 700 left')


def s3(pg, f):
    rows = js(pg, "return [].map.call(r.querySelectorAll('#shp .row:not(.h):not(.sm)'),function(e){var s=e.querySelectorAll('span');return [s[0].textContent,+s[3].textContent.replace(/,/g,'')];})")
    f.check(dict(rows) == SHIPPED, 'step 3: one row per customer %s' % rows)
    f.check(ids(pg, 'tsh') == '1,300' and sum(x[1] for x in rows) == 1300, 'step 3: total shipped 1,300 is the sum of the rows')
    f.check('Free to allocate in B-12-3380' in js(pg, "return r.getElementById('dt').innerText.replace(/\\s+/g,'')").replace('Freetoallocatein', 'Free to allocate in ') , 'step 3: 380 free to allocate after 200 and 120')


def s4(pg, f):
    t = ids(pg, 'pvw')
    f.check('Certificate of analysis' in t and 'Rossi Imports' in t and 'L-24-0817' in t, 'step 4: the supplier document preview opens')


def s5(pg, f):
    lots = js(pg, "return [].map.call(r.querySelectorAll('#trc .row:not(.h):not(.sm)'),function(e){var s=e.querySelectorAll('span');return [s[0].textContent,+s[4].textContent.replace(/,/g,'')];})")
    f.check(dict(lots) == TRACE, 'step 5: the trace lists exactly the lots on SO-3110 %s' % lots)
    f.check(ids(pg, 'ttq') == '300', 'step 5: 300 cases in total')


PLAN = [('The lot, found by its number', 'L-24-0817'),
        ('Where it is stored, how much is left', 'B-12-3'),
        ('Every customer that received the lot', 'Corner Pantry'),
        ('The supplier document on the lot', 'Certificate of analysis'),
        ('From a customer order back to its lots', 'L-24-0822')]
f = run_card(2, PLAN, ['SO-3110', 'L-24-0817', 'L-24-0822', '300'], start=start,
             extra={'after_step': {0: s1, 1: s2, 2: s3, 3: s4, 4: s5}})
keyboard_walk(f, 2, 5)
clicks_only(f, 2, 0)
clicks_only(f, 2, 0, 358, 390)
finish(f)
