#!/usr/bin/env python3
"""Card 2 (three lane release board): the brief's numbers in Python, then the click through.
Run: python3 tools/pharmaceutical/test_card2.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ph_tests import run_card, finish, js, pill, ids, enter_submits

# grams, so every kilogram sum is exact
ON_HAND, AP8842, COMMIT = 18000, 30000, [10204, 10204]
assert sum(COMMIT) == 20408                          # 10.204 + 10.204 = 20.408
assert ON_HAND - sum(COMMIT) == -2408                # 18.000 - 20.408 = -2.408, a shortage of 2.408
assert ON_HAND + AP8842 == 48000                     # 18.000 + 30.000 = 48.000
assert ON_HAND + AP8842 - sum(COMMIT) == 27592       # 48.000 - 20.408 = 27.592


def avail(pg):
    return ids(pg, 'aoh', 'aqu', 'acm', 'aav', 'asm')


def start(pg, f, when='start'):
    t = js(pg, "return r.querySelector('.g2').innerText")
    f.check(js(pg, "var i=r.getElementById('ipo');return i.value+'|'+i.readOnly") == 'PO-4420|true' and js(pg, "return r.querySelectorAll('.lk').length") == 0, '%s: prefilled read only input, three empty lanes' % when)
    f.check(avail(pg) == '||||On hand less committed' and not any(s in t for s in ('kg', 'AP-88', 'EX-33', 'Shortage')), '%s: availability shows its row labels only' % when)



def lane(pg, k):
    return js(pg, "return [].map.call(r.querySelectorAll('#ln-%s .lk'),function(e){return e.id.slice(2)}).join(',')" % k)


def s1(pg, f):
    f.check(lane(pg, 'q') == 'AP-8842,EX-3312', 'step 1: AP-8842 and EX-3312 in Quarantine')
    q = js(pg, "return r.getElementById('ln-q').innerText")
    f.check('30.000 kg' in q and '150.000 kg' in q and 'QA-01' in q, 'step 1: 30.000 and 150.000 kg into QA-01')
    f.check(avail(pg) == '18.000 kg|30.000 kg|20.408 kg|-2.408 kg|Shortage of 2.408 kg', 'step 1: on hand 18.000, quarantined 30.000, committed 20.408, available -2.408, shortage 2.408')


def s2(pg, f):
    f.check(lane(pg, 't') == 'AP-8842,EX-3312' and lane(pg, 'q') == '', 'step 2: both lots in test')
    c = js(pg, "return r.querySelector('#k-AP-8842 .cert').innerText")
    f.check(all(s in c for s in ('Certificate attached', '98.0%', '2028-10-31', '2027-10-31')), 'step 2: certificate with assay, expiry and retest')
    f.check(ids(pg, 'aav') == '-2.408 kg', 'step 2: a lot in test does not count toward available')


def s3(pg, f):
    f.check(ids(pg, 'pmsg') == 'Lot is in quarantine', 'step 3: pick blocked, "Lot is in quarantine"')
    f.check(avail(pg).startswith('18.000 kg|30.000 kg|20.408 kg|-2.408 kg'), 'step 3: availability unchanged')


def s4(pg, f):
    t = js(pg, "return r.querySelector('#k-AP-8842 .so').innerText")
    f.check('JL' in t and 'Nov 16, 10:42' in t and js(pg, "return r.querySelectorAll('img').length") == 0, 'step 4: sign off shows initials and time, no photo')
    f.check(ids(pg, 'aav') == '-2.408 kg', 'step 4: still not available before the sign off')


def s5(pg, f):
    f.check(lane(pg, 'rel') == 'AP-8790,AP-8842' and lane(pg, 't') == 'EX-3312', 'step 5: AP-8842 released, EX-3312 stays in test')
    f.check(avail(pg) == '48.000 kg|0.000 kg|20.408 kg|27.592 kg|Shortage cleared', 'step 5: on hand 48.000, committed 20.408, available 27.592, shortage cleared')
    f.check(ids(pg, 'shc') == 'Covered', 'step 5: shortage chip cleared')


PLAN = [('Received lots wait in quarantine', 'Shortage of 2.408 kg'),
        ('The certificate rides with the lot', '2028-10-31'),
        ('Untested material cannot be picked', 'Lot is in quarantine'),
        ('A release needs a named sign off', '10:42'),
        ('Released stock counts at once', '27.592 kg')]
f = run_card(2, PLAN, ['48.000 kg', '20.408 kg', '27.592 kg', 'Shortage cleared'], start=start,
             extra={'after_step': {0: s1, 1: s2, 2: s3, 3: s4, 4: s5}})
finish(f)
