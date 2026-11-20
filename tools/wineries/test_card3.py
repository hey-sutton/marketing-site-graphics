#!/usr/bin/env python3
"""Card 3 (list and detail): the README's lot numbers in Python, then the click through.
Run: python3 tools/wineries/test_card3.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from wn_tests import run_card, finish, js, ids, readonly_checks, keyboard_walk, clicks_only

RECEIVED = 16000
RUNS = {'BT-0318': (500, 6000, {'Harbor Wine Co': 300, 'Club release': 200}),
        'BT-0322': (400, 4800, {'Northside Distributors': 400}),
        'BT-0327': (300, 3600, {'Harbor Wine Co': 100, 'Web orders': 200})}
USED = sum(c for _, c, _ in RUNS.values())
assert all(cs * 12 == ck for cs, ck, _ in RUNS.values())                    # corks = cases x 12
assert USED == 14400 and RECEIVED == USED + 1600                              # 16,000 = 14,400 + 1,600
assert sum(cs for cs, _, _ in RUNS.values()) == 1200                          # cases sum to 1,200
assert all(sum(sh.values()) == cs for cs, _, sh in RUNS.values())             # each run's shipments equal its cases
TRACE = {'runs': ['BT-0322'], 'cork': ['CK-2410-77'], 'glass': ['GL-5532']}
assert [len(v) for v in TRACE.values()] == [1, 1, 1]                          # one run, one cork lot, one glass lot
assert 'Northside Distributors' in RUNS[TRACE['runs'][0]][2]


def start(pg, f, when='start'):
    readonly_checks(pg, f, {'ilt': 'CK-2410-77'}, when)
    f.check(js(pg, "return r.querySelectorAll('.ls .row,.bal,.tb').length") == 0, '%s: no lots, balance or tables shown' % when)
    t = js(pg, "return r.querySelector('.g3').innerText")
    f.check(not any(s in t for s in ('16,000', 'BT-0318', 'Oct 14', 'SO-6120', 'Harbor')), '%s: nothing derived shows' % when)


def s1(pg, f):
    f.check(ids(pg, 'brc', 'bus', 'brm') == '16,000|Open|Open', 'step 1: 16,000 received, runs not shown yet')
    f.check('Oct 14, 2024' in js(pg, "return r.querySelector('.dt').innerText") and 'Alder Cork Supply' in js(pg, "return r.querySelector('.dt').innerText"), 'step 1: supplier and received date')


def s2(pg, f):
    f.check(js(pg, "return r.querySelectorAll('#tru .row:not(.h):not(.sm)').length") == 3, 'step 2: three runs listed')
    f.check(ids(pg, 'cu-BT-0318', 'cu-BT-0322', 'cu-BT-0327', 'rck', 'rcs') == '6,000|4,800|3,600|14,400|1,200', 'step 2: 6,000 + 4,800 + 3,600 = 14,400')
    f.check(ids(pg, 'bus', 'brm') == '14,400|1,600' and '16,000 received = 14,400 used + 1,600 left' in ids(pg, 'bcal'), 'step 2: received = used + remaining')


def s3(pg, f):
    f.check(ids(pg, 'rs-BT-0318', 'rs-BT-0322', 'rs-BT-0327', 'cst') == '500 of 500|400 of 400|300 of 300|1,200', "step 3: each run's shipments equal its cases, 1,200 in all")
    t = js(pg, "return r.getElementById('tca').innerText")
    f.check(all(a in t for a in ('Harbor Wine Co', 'Club release', 'Northside Distributors', 'Web orders')), 'step 3: accounts listed')


def s4(pg, f):
    f.check(js(pg, "return r.querySelectorAll('#tdt .row:not(.h)').length") == 5, 'step 4: five lots dated')
    f.check('Oct 14' in ids(pg, 'dt-CK-2410-77') and 'Mar 22' in ids(pg, 'dt-BT-0322') and 'Feb 3' in ids(pg, 'dt-GL-5532'), 'step 4: received and bottled dates')


def s5(pg, f):
    f.check(ids(pg, 'trn', 'tck', 'tgl') == '1|1|1', 'step 5: the trace lists one run, one cork lot and one glass lot')
    f.check('BT-0322' in ids(pg, 'tr-run') and 'CK-2410-77' in ids(pg, 'tr-ck') and 'GL-5532' in ids(pg, 'tr-gl'), 'step 5: SO-6120 back to BT-0322, CK-2410-77, GL-5532')


PLAN = [('A cork lot and where it came from', 'Alder Cork Supply'),
        ('The bottling runs that used it', 'BT-0327'),
        ('Cases and accounts it reached', 'Northside Distributors'),
        ('Received and bottled dates', 'Mar 27'),
        ('One order traced back to its lots', 'GL-5532')]
f = run_card(3, PLAN, ['SO-6120', 'BT-0322', 'CK-2410-77', 'GL-5532', '1,600 left'], start=start,
             extra={'after_step': {0: s1, 1: s2, 2: s3, 3: s4, 4: s5}})
keyboard_walk(f, 3, 5)
clicks_only(f, 3, 0)
clicks_only(f, 3, 0, 358, 390)
finish(f)
