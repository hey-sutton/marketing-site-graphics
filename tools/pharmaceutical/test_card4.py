#!/usr/bin/env python3
"""Card 4 (operator tablet with a step rail and a record sheet): the brief's numbers in Python, then the click through.
Run: python3 tools/pharmaceutical/test_card4.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ph_tests import run_card, finish, js, pill, ids, enter_submits

WEIGH = {'AP-8842': 10204, 'EX-4410': 800, 'EX-3190': 68996}    # grams
assert sum(WEIGH.values()) == 80000                                # 10.204 + 0.800 + 68.996 = 80.000
PLAN, FILLED, REJ, PER, ISSUED = 200000, 198400, 1600, 100, 2000
assert FILLED + REJ == PLAN
assert FILLED * 1000 // PLAN == 992 and FILLED * 1000 % PLAN == 0  # 99.2 percent exactly
assert FILLED // PER == 1984 and FILLED % PER == 0
assert ISSUED - FILLED // PER == 16
assert 380 <= 399.6 <= 420


def start(pg, f, when='start'):
    t = js(pg, "return r.querySelector('.g4').innerText")
    f.check(js(pg, "var i=r.getElementById('imo');return i.value+'|'+i.readOnly") == 'MO-7210|true' and js(pg, "return r.querySelectorAll('.tl2').length") == 5, '%s: prefilled read only input, the five step names' % when)
    f.check(all(n in t for n in ('Weigh out', 'Blend', 'Encapsulate', 'In-process check', 'Package')), '%s: step rail lists the five steps' % when)
    f.check(js(pg, "return r.querySelectorAll('.rl:not(.h):not(.bl)').length") == 0 and not any(s in t for s in ('B-2620', 'kg', '200,000', 'MK', 'RD')), '%s: the record sheet is blank' % when)



def lines(pg):
    return js(pg, "return r.querySelectorAll('.rl:not(.h):not(.bl)').length")


def s1(pg, f):
    t = js(pg, "return r.querySelector('.ph').innerText")
    f.check(all(s in t for s in ('MO-7210', 'B-2620', 'CP-050', 'v4')) and ids(pg, 'pcp', 'pbt') == '200,000|2,000', 'step 1: MO-7210, B-2620, CP-050 v4, 200,000 capsules, 2,000 bottles planned')
    f.check(lines(pg) == 0, 'step 1: the sheet has no lines yet')


def s2(pg, f):
    f.check(ids(pg, 'w0', 'w1', 'w2', 'wt') == '10.204 kg|0.800 kg|68.996 kg|80.000 kg', 'step 2: 10.204, 0.800 and 68.996 kg, 80.000 kg total')
    t = js(pg, "return r.querySelector('.pg').innerText")
    f.check(all(s in t for s in ('AP-8842', 'EX-4410', 'EX-3190', '07:52', '07:55', '07:58')) and t.count('MK') == 3, 'step 2: three lot scans with time and initials MK')


def s3(pg, f):
    f.check(ids(pg, 'enc', 'rej') == '198,400 filled of 200,000 planned|1,600 rejected', 'step 3: 198,400 filled of 200,000 planned, 1,600 rejected')
    f.check('08:10 to 08:40' in js(pg, "return r.querySelector('.pg').innerText"), 'step 3: blend 08:10 to 08:40')


def s4(pg, f):
    f.check(ids(pg, 'chk', 'chr') == 'Average fill weight 399.6 mg over 20 capsules|Pass', 'step 4: 399.6 mg over 20 capsules, Pass')
    f.check('Limit 380 to 420 mg' in js(pg, "return r.querySelector('.pg').innerText"), 'step 4: limit 380 to 420 mg')


def s5(pg, f):
    f.check(ids(pg, 'pkt', 'pki', 'pst') == '198,400 ÷ 100 = 1,984 bottles|2,000 issued, 16 returned to stock|1,984 bottles to QA-01, quarantine', 'step 5: 1,984 bottles, 16 returned, posted to QA-01')
    f.check(ids(pg, 'pfs', 'yld') == 'Record complete, waiting for release|Yield 99.2%', 'step 5: record complete, waiting for release, yield 99.2%')
    f.check('2028-11-30' in js(pg, "return r.querySelector('.pg').innerText") and js(pg, "return r.querySelectorAll('.tl2.dn').length") == 5, 'step 5: expiry 2028-11-30, all five steps done')


PLAN = [('The order brings its steps and a blank record', 'B-2620'),
        ('Each scan writes a line with lot, time and initials', '80.000 kg'),
        ('Blend and encapsulation log in order', '198,400 filled of 200,000 planned'),
        ('The check records its result against the limit', '399.6 mg'),
        ('Finished bottles post to quarantine', 'Record complete, waiting for release')]
f = run_card(4, PLAN, ['1,984 bottles to QA-01', '16 returned to stock', 'Yield 99.2%'], start=start,
             extra={'after_step': {0: s1, 1: s2, 2: s3, 3: s4, 4: s5}})
finish(f)
