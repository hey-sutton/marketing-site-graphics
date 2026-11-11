#!/usr/bin/env python3
"""Card 2 (freezer floor plan): the brief's numbers in Python, then the click through. Run: python3 tools/frozen-food/test_card2.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ff_tests import run_card, finish, js, pill, ids

ON = {'Blast freezer 1': 300, 'Holding freezer A': 1200, 'Holding freezer B': 800, 'Outside cold store': 700}
SO = {'SO-3318': 1000, 'SO-3322': 600}
assert sum(ON.values()) == 3000 and sum(SO.values()) == 1600
MOVED = dict(ON, **{'Blast freezer 1': 300 - 100, 'Holding freezer B': 800 + 100})
assert MOVED['Blast freezer 1'] == 200 and MOVED['Holding freezer B'] == 900 and sum(MOVED.values()) == 3000
assert 3000 - 1600 == 1400 and (3000 - 700) - 1600 == 700
assert 200 + 100 == 300 and 700 + 500 == 1200 and 500 + 300 == 800 and 400 + 300 == 700   # zone lots add up


def start(pg, f, when='start'):
    t = js(pg, "return r.querySelector('.g2').innerText")
    f.check(js(pg, "return r.querySelectorAll('.bin.f,.bin.me').length") == 0 and js(pg, "return r.getElementById('isc').value") == '', '%s: zone names and empty bins only, empty scan input' % when)
    f.check(not any(s in t for s in ('3,000', '1,200', 'cases on hand', 'LT-')), '%s: no quantities before a scan' % when)


def s1(pg, f):
    f.check(ids(pg, 'tot', 'q-bf1', 'q-ha', 'q-hb', 'q-ob') == '3,000 cases on hand|300 cases|1,200 cases|800 cases|700 cases', 'step 1: 300, 1,200, 800, 700, total 3,000')
    f.check(js(pg, "return r.querySelectorAll('.bin.f').length+r.querySelectorAll('.bin.me').length") == 30 and js(pg, "return r.querySelectorAll('#zn-bf1 .bin.me').length") == 1, 'step 1: 30 pallets in bins, P-0912 lit in Blast freezer 1')
    f.check(ids(pg, 'ploc') == 'Blast freezer 1, rack 2, bin 3', 'step 1: rack 2, bin 3')


def s2(pg, f):
    t = js(pg, "return r.getElementById('zl').innerText")
    f.check(ids(pg, 'zlt') == '300' and 'Apr 12, 2027' in t and 'May 3, 2027' in t, 'step 2: Blast freezer 1 lots with expiry dates, 300 cases')


def scan(pg, f):
    inp = pg.locator('#cv #isc')
    inp.click(); inp.press_sequentially('P-9999'); inp.press('Enter'); pg.wait_for_timeout(300)
    f.check(js(pg, "return r.getElementById('fsc').classList.contains('err')") and 'Your turn1 of 5' in pill(pg), 'step 1: an unknown pallet shows an error and does not advance')
    inp.fill('')
    pg.locator('#cv #smp').click(); pg.wait_for_timeout(100)
    f.check(js(pg, "return r.getElementById('isc').value") == 'P-0912', 'step 1: the sample button fills P-0912')


def bad_bin(pg, f):
    pg.locator('#cv #imv').fill('HA-R9-B9')
    pg.locator('#cv .hint').first.click(); pg.wait_for_timeout(300)
    f.check(js(pg, "return r.getElementById('fmv').classList.contains('err')") and 'Your turn3 of 5' in pill(pg), 'step 3: an unknown bin shows an error and does not advance')
    pg.locator('#cv #imv').fill('HB-R1-B4')


def s3(pg, f):
    f.check(ids(pg, 'q-bf1', 'q-hb', 'tot', 'ploc', 'zlt') == '200 cases|900 cases|3,000 cases on hand|Holding freezer B, rack 1, bin 4|900', 'step 3: 200 and 900, total still 3,000, zone lots 900')


def s4(pg, f):
    f.check(ids(pg, 'soh', 'shd', 'scm', 'sav') == '3,000|0|1,600|1,400', 'step 4: on hand 3,000, committed 1,600, available 1,400')


def s5(pg, f):
    f.check(ids(pg, 'soh', 'shd', 'scm', 'sav') == '3,000|700|1,600|700', 'step 5: 700 on hold, available 700')


PLAN = [('Every pallet has a place, down to the bin', '3,000 cases on hand'),
        ('Each zone lists its lots with expiry dates', 'LT-5101'),
        ('A scan moves the pallet, and both zones update', '900 cases'),
        ('Available follows open orders and holds', '1,400'),
        ('A quality hold comes off available straight away', 'Quality hold')]
f = run_card(2, PLAN, ['3,000 cases on hand', 'Quality hold'], start=start,
             extra={'before': {0: scan, 2: bad_bin}, 'after_step': {0: s1, 1: s2, 2: s3, 3: s4, 4: s5}})
finish(f)
