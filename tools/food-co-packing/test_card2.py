#!/usr/bin/env python3
"""Card 2 (board: line schedule and changeovers): the numbers in Python, then the full click through.
Run: python3 tools/food-co-packing/test_card2.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fc_tests import run_card, finish, js, pill, testlib, ids

# ---- the numbers, derived independently of the card ----
CO = {('GF', 'GF'): 15, ('PN', 'PN'): 15, ('TN', 'TN'): 15, ('GF', 'PN'): 20, ('GF', 'TN'): 20, ('PN', 'GF'): 90, ('PN', 'TN'): 60, ('TN', 'GF'): 75, ('TN', 'PN'): 45}
RUN = {'A': (120, 'GF'), 'B': (150, 'PN'), 'D': (100, 'GF'), 'C': (90, 'TN'), 'X': (60, 'PN')}
START, END = 6 * 60, 16 * 60


def clean(o):
    return sum(CO[(RUN[a][1], RUN[b][1])] for a, b in zip(o, o[1:]))


def run(o):
    return sum(RUN[k][0] for k in o)


def hm(t):
    return '%02d:%02d' % divmod(t, 60)


INIT, SWAP = ['A', 'B', 'D', 'C'], ['A', 'D', 'B', 'C']
assert clean(INIT) == 20 + 90 + 20 == 130 and run(INIT) == 460 and hm(START + 460 + 130) == '15:50'
assert clean(SWAP) == 15 + 20 + 60 == 95 and 130 - 95 == 35 and hm(START + 460 + 95) == '15:15'
WITH = ['A', 'D', 'B', 'X', 'C']
assert clean(WITH) == 15 + 20 + 15 + 60 == 110 and run(WITH) == 520 and START + 630 == 16 * 60 + 30 > END   # would end 16:30
FINAL = ['A', 'D', 'B', 'X']
assert clean(FINAL) == 50 and run(FINAL) == 430 and hm(START + 480) == '14:00'
SHEET = ['06:00 to 08:00  R-6101', '08:15 to 09:55  R-6104', '10:15 to 12:45  R-6102', '13:00 to 14:00  R-6109']


def start(pg, f, when='start'):
    t = js(pg, "return r.querySelector('.c2').innerText")
    f.check(js(pg, "return r.querySelectorAll('.bk,.co,.ro .row').length") == 0, '%s: no runs on the board' % when)
    f.check(not any(s in t for s in ('R-61', 'Brightfield', '130 min', '15:50')), '%s: nothing from the day shows' % when)


def s1(pg, f):
    f.check(js(pg, "return r.querySelectorAll('.bk').length") == 4 and ids(pg, 'tb', 'tn', 'te') == '130 min|130 min|15:50', 'step 1: 4 runs, cleaning 130 min, done 15:50')


def s2(pg, f):
    f.check(ids(pg, 'gcA', 'gcB', 'gcD', 'gcC') == 'Gluten free|Peanut|Gluten free|Tree nut', 'step 2: allergen group on every run')


def s3(pg, f):
    f.check(ids(pg, 'tb', 'tn', 'tsv', 'te') == '130 min|95 min|35 min|15:15', 'step 3: cleaning 130 to 95 min, 35 saved, done 15:15')
    f.check(js(pg, "return [].map.call(r.querySelectorAll('.ro .rn small'),function(e){return e.textContent.split(',')[0]}).join(',')") == 'R-6101,R-6104,R-6102,R-6103', 'step 3: new order A, D, B, C')


def s4(pg, f):
    f.check(ids(pg, 'tn', 'te', 'tsv') == '50 min|14:00|35 min', 'step 4: with the rush run cleaning 50 min, done 14:00')
    f.check('would end at 16:30' in ids(pg, 'tdn') and 'Granola clusters moves to Thursday' in ids(pg, 'tdn'), 'step 4: would end 16:30, granola clusters displaced')
    f.check(js(pg, "return !r.getElementById('bkC')&&!!r.getElementById('bkX')"), 'step 4: R-6103 off the day, R-6109 on it')


def s5(pg, f):
    got = js(pg, "return r.getElementById('rsl').innerText")
    f.check([' '.join(x.split()) for x in got.split('\n')] == [' '.join(x.split()) for x in SHEET], 'step 5: run sheet times (%s)' % got.replace('\n', ' | '))
    f.check(ids(pg, 'wps') == 'Sent to printer', 'step 5: sent to printer')


PLAN = [('Open the day for Line 2', '15:50'),
        ('Every run shows its allergen group', 'Gluten free'),
        ('Reorder runs and read the cleaning saved', '95 min'),
        ('A rush run shows what it displaces', '16:30'),
        ('Print the run sheet for the line', 'Sent to printer')]

f = run_card(2, PLAN, ['50 min', '14:00', 'Sent to printer'], start=start,
             extra={'after_step': {0: s1, 1: s2, 2: s3, 3: s4, 4: s5}})
finish(f)
