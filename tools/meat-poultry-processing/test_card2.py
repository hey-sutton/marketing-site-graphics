#!/usr/bin/env python3
"""Card 2 (list and detail): the README's trace numbers in Python, then the click through.
Run: python3 tools/meat-poultry-processing/test_card2.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from mp_tests import run_card, finish, js, ids, readonly_checks, keyboard_walk, clicks_only

REC = 2400
RUNS = {'JRK-3310': 1000, 'GRD-3314': 600, 'SAU-3318': 400}
USED = sum(RUNS.values())
assert USED == 2000                                       # run uses sum to 2,000
LEFT = REC - USED
assert LEFT == 400 and REC == USED + LEFT                # received equals used plus remaining
FG = {'FG-7701': (420, 'JRK-3310', [('Lakeside Market', 250), ('Ridge Foods', 170)]),
      'FG-7704': (570, 'GRD-3314', [('Ridge Foods', 570)]),
      'FG-7708': (380, 'SAU-3318', [('Lakeside Market', 380)])}
assert sum(q for _, q in FG['FG-7701'][2]) == 420        # FG-7701 shipments sum to 420
assert all(kg == sum(q for _, q in sh) for kg, _, sh in FG.values())
CUST = {}
for kg, run, sh in FG.values():
    for c, q in sh:
        CUST[c] = CUST.get(c, 0) + q
assert CUST == {'Lakeside Market': 630, 'Ridge Foods': 740}   # customer totals
SO8841 = [('FG-7701', 170), ('FG-7704', 570)]
TR_RUNS = sorted({FG[l][1] for l, _ in SO8841})
assert TR_RUNS == ['GRD-3314', 'JRK-3310'] and len(TR_RUNS) == 2   # the trace lists exactly two runs
assert sum(q for _, q in SO8841) == 740


def num(x):
    return int(x.split()[0].replace(',', ''))


def start(pg, f, when='start'):
    readonly_checks(pg, f, {'ilt': 'BEEF-24-0731'}, when)
    f.check(js(pg, "return r.querySelectorAll('.ls .row,.tb,.dh').length") == 0, '%s: no lots, runs or record shown' % when)
    t = js(pg, "return r.querySelector('.g3').innerText")
    f.check(not any(s in t for s in ('2,400', 'Prairie', 'JRK-3310', 'Nov 27', 'SO-8841')), '%s: nothing derived shows' % when)


def s1(pg, f):
    f.check(ids(pg, 'dsp', 'drc') == 'Prairie Ridge Beef|2,400 kg', 'step 1: supplier and 2,400 kg received')
    f.check(js(pg, "return r.querySelectorAll('#ru,#fg,#dts').length") == 0, 'step 1: runs, customers and dates wait for a click')


def s2(pg, f):
    got = {k: num(ids(pg, 'ru-' + k)) for k in RUNS}
    f.check(got == RUNS, 'step 2: runs JRK-3310, GRD-3314, SAU-3318 %s' % got)
    u, l = num(ids(pg, 'ruu')), num(ids(pg, 'rul'))
    f.check(u == sum(got.values()) == 2000 and l == 400 and u + l == num(ids(pg, 'drc')), 'step 2: used %d + remaining %d = received on screen' % (u, l))
    f.check(ids(pg, 'rcal') == '2,000 used + 400 left = 2,400 kg received', 'step 2: the sum line')


def s3(pg, f):
    sh = js(pg, "return [].map.call(r.querySelectorAll('.sh-FG-7701'),function(e){return +e.textContent.replace(/,/g,'')})")
    f.check(sh == [250, 170] and sum(sh) == num(ids(pg, 'fk-FG-7701')) == 420, 'step 3: FG-7701 shipments %s sum to 420' % sh)
    for k in ('FG-7704', 'FG-7708'):
        s = js(pg, "return [].map.call(r.querySelectorAll('.sh-%s'),function(e){return +e.textContent.replace(/,/g,'')})" % k)
        f.check(sum(s) == num(ids(pg, 'fk-' + k)), 'step 3: %s shipments add up' % k)
    f.check(ids(pg, 'cl', 'cr') == '630 kg|740 kg', 'step 3: Lakeside Market 630, Ridge Foods 740')
    f.check(js(pg, "return !!r.getElementById('trb')"), 'step 3: Trace order sits beside SO-8841')


def s4(pg, f):
    f.check(ids(pg, 'dpk', 'dub') == 'Oct 28|Nov 27', 'step 4: pack Oct 28, use by Nov 27')


def s5(pg, f):
    runs = js(pg, "return [].map.call(r.querySelectorAll('#tr .tr-run b'),function(e){return e.textContent})")
    lots = js(pg, "return [].map.call(r.querySelectorAll('#tr .tr-lot b'),function(e){return e.textContent})")
    f.check(sorted(set(runs)) == TR_RUNS and set(lots) == {'BEEF-24-0731'}, 'step 5: trace has two runs %s and one supplier lot %s' % (runs, lots))
    f.check(ids(pg, 'trn', 'trl', 'soq') == '2|1|740', 'step 5: 2 runs, 1 supplier lot, 740 kg on the order')


PLAN = [('A supplier lot found', 'Prairie Ridge Beef'),
        ('The runs that used it', 'SAU-3318'),
        ('Customers and shipments it reached', 'Lakeside Market'),
        ('Pack and use by dates', 'Nov 27'),
        ('A customer order traced back', 'Back to the supplier lots')]
f = run_card(2, PLAN, ['JRK-3310', 'GRD-3314', 'BEEF-24-0731', 'Ridge Foods', '740'], start=start,
             extra={'after_step': {0: s1, 1: s2, 2: s3, 3: s4, 4: s5}})
keyboard_walk(f, 2, 5)
clicks_only(f, 2, 0)
clicks_only(f, 2, 0, 358, 390)
finish(f)
