#!/usr/bin/env python3
"""Card 1 (record form with a side summary): the README's intake numbers in Python, then the click through.
Run: python3 tools/nut-processing/test_card1.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from np_tests import run_card, finish, js, ids, readonly_checks, keyboard_walk, clicks_only

SPEC = 6.0
# truckload: gross, tare, moisture
TK = {'NP-0709': (38200, 13800, 5.6), 'NP-0711': (42000, 14000, 5.2), 'NP-0712': (40500, 13800, 7.1)}
NET = lambda t: TK[t][0] - TK[t][1]
HELD = lambda m: m > SPEC

assert NET('NP-0711') == 28000 and 42000 - 14000 == 28000            # net equals gross minus tare
assert NET('NP-0709') == 24400 and NET('NP-0712') == 26700
assert not HELD(5.2) and HELD(7.1) and not HELD(6.0) and not HELD(5.6)  # held only when moisture is above 6.0
PUT = [t for t in TK if not HELD(TK[t][2])]
assert sorted(PUT) == ['NP-0709', 'NP-0711'] and 'NP-0712' not in PUT    # a held lot is left out of put away
assert sum(NET(t) for t in PUT) == 52400
assert sum(NET(t) for t in TK) == 79100 and len(TK) == 3
assert round(sum(round(NET(t) / 79100 * 100, 1) for t in TK), 1) == 100.0

ALL_INPUTS = {'itk': 'NP-0711', 'imo': '5.2', 'isz': '23/25', 'ilb': 'VAL-3318', 'ibm': '7.1'}


def start(pg, f, when='start'):
    readonly_checks(pg, f, {'itk': 'NP-0711'}, when)
    f.check(js(pg, "return r.querySelectorAll('.rc .sec,#dk,#pa,#il').length") == 0, '%s: no record, dock or put away shown' % when)
    t = js(pg, "return r.querySelector('.g1').innerText")
    f.check(not any(s in t for s in ('28,000', '42,000', 'Harlan', 'NP-0712')), '%s: nothing derived shows' % when)


def s1(pg, f):
    readonly_checks(pg, f, ALL_INPUTS, 'step 1')
    g, t, n, c = ids(pg, 'wgr', 'wta', 'wnt', 'wcal').split('|')
    num = lambda x: int(x.replace(',', ''))
    f.check(num(n) == num(g) - num(t) == 28000 and c == '42,000 − 14,000 = 28,000', 'step 1: net = gross - tare on screen (%s)' % c)
    f.check(ids(pg, 'rgr', 'rgd', 'snt') == 'Harlan Orchards|Nonpareil 23/25|28,000', 'step 1: grower, grade, net in the summary')


def s2(pg, f):
    f.check(ids(pg, 'mst', 'mrd') == 'Within spec|5.2% read', 'step 2: 5.2% is within the 6.0% maximum')


def s3(pg, f):
    f.check(js(pg, "return !!r.getElementById('lbr')") and ids(pg, 'lst') == 'Accepted', 'step 3: lab result attached, lot accepted')
    f.check('Ready' in ids(pg, 'p-NP-0711'), 'step 3: NP-0711 ready to put away')


def s4(pg, f):
    f.check(ids(pg, 'hst') == 'Held' and '7.1% is above the 6.0% maximum' in ids(pg, 'hnt'), 'step 4: NP-0712 held at the dock')
    f.check(js(pg, "return r.getElementById('p-NP-0712').classList.contains('x')") and 'Held' in ids(pg, 'p-NP-0712'), 'step 4: held lot struck from put away')
    f.check(ids(pg, 'ptot') == '52,400', 'step 4: put away total excludes the held lot (%s)' % ids(pg, 'ptot'))


def s5(pg, f):
    rows = js(pg, "return [].map.call(r.querySelectorAll('#il .row:not(.h)'),function(e){return e.id})")
    f.check(sorted(rows) == ['i-NP-0709', 'i-NP-0711', 'i-NP-0712'], 'step 5: 3 incoming lots %s' % rows)
    f.check(ids(pg, 'ipa', 'iho', 'itot') == '52,400 lb|26,700 lb|79,100 lb in', 'step 5: put away, held and total weights')
    f.check(js(pg, "return r.querySelectorAll('#il .gr').length") == 2, 'step 5: grouped by 2 grades')


PLAN = [('A truckload with its origin and grower', '28,000'),
        ('Moisture and size grade at the scale', 'Within spec'),
        ('A lab result on the lot', 'Aflatoxin'),
        ('A lot outside its spec is held', 'Held at the dock'),
        ('Incoming lots by grade and supplier', 'By supplier')]
f = run_card(1, PLAN, ['52,400', '26,700', 'Harlan Orchards', 'Tule Bend Farms', 'Delmar Ranch'], start=start,
             extra={'after_step': {0: s1, 1: s2, 2: s3, 3: s4, 4: s5}})
keyboard_walk(f, 1, 5)
clicks_only(f, 1, 0)
clicks_only(f, 1, 0, 358, 390)
finish(f)
