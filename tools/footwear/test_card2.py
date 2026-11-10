#!/usr/bin/env python3
"""Card 2 click through (both modes), numbers, layout, variety, timing, navigation and phone checks.
Run: python3 tools/footwear/test_card2.py. Pairs are whole; leather is square feet to one decimal."""
import os, sys
from decimal import Decimal as D, ROUND_HALF_UP
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from footwear_tests import run_all, js

# ---- the brief's numbers, derived independently of the card ----
ORDER = ['cut', 'sti', 'las', 'fin', 'pac']
IP = {'cut': 0, 'sti': 60, 'las': 48, 'fin': 20, 'pac': 0}
DONE = {'cut': 240, 'sti': 180, 'las': 96, 'fin': 40, 'pac': 0}


def queues(ip, done):
    out, up = {}, 240
    for k in ORDER:
        out[k] = up - (ip[k] + done[k]); up = done[k]
    return out


Q = queues(IP, DONE)
assert Q == {'cut': 0, 'sti': 0, 'las': 36, 'fin': 36, 'pac': 40}  # the brief's table
assert 180 - (96 + 48) == 36 and 96 - (40 + 20) == 36 and 40 - 0 == 40
IP2, DONE2 = dict(IP, las=48 - 12), dict(DONE, las=96 + 12)
Q2 = queues(IP2, DONE2)
assert (DONE2['las'], IP2['las'], Q2['las']) == (108, 36, 36) and Q2['fin'] == 48
assert 120 - 96 == 24 and 120 - 108 == 12
STD = D(240) * D('3.0')
assert STD == D('720.0')
YIELD = (STD / D('752.4') * 100).quantize(D('0.1'), ROUND_HALF_UP)
assert YIELD == D('95.7') and D('18.0') + D('14.4') == D('32.4') == D('752.4') - STD
assert D('380.2') + D('372.2') == D('752.4') and 40 - 6 == 34


def ids(pg, *names):
    return js(pg, "return %r.map(function(i){var e=r.getElementById(i);return e?e.textContent:null}).join('|')" % list(names))


def start(pg, f):
    f.check(js(pg, "return r.querySelector('.fwin').getAttribute('data-scr')") == 'Work orders', 'start: the work order list')
    f.check(js(pg, "return r.querySelectorAll('.col,.bar').length") == 0 and 'Queue' not in js(pg, "return r.getElementById('pg').innerText"), 'start: nothing about stages before the work order is opened')


def board(pg, f):
    want = '|'.join(str(x) for k in ORDER for x in (Q[k], IP[k], DONE[k]))
    f.check(ids(pg, *[k + s for k in ORDER for s in ('-q', '-p', '-d')]) == want, 'step 2: queue, in process and done for all five stages')
    f.check(ids(pg, 'flag') == 'Behind by 24', 'step 2: Lasting flagged behind by 24')


def cut(pg, f):
    f.check(ids(pg, 'act', 'beh') == '96|24', 'step 3: callout planned 120, actual 96, behind 24')


def cutd(pg, f):
    f.check(ids(pg, 'std', 'act2', 'yl', 'ov', 'rem', 'scr', 'lt') == '720.0|752.4|95.7%|32.4|18.0|14.4|752.4', 'step 4: 720.0 standard, 752.4 actual, 95.7%, 18.0 and 14.4 offcuts')


def after(pg, f):
    f.check(ids(pg, 'las-d', 'las-p', 'las-q', 'fin-q', 'act', 'beh') == '108|36|36|48|108|12', 'step 5: Lasting done 108, in process 36, queue 36, Finishing queue 48, behind 12')


def end(pg, f):
    f.check(ids(pg, 'sec') == '6', 'step 6: 6 second quality pairs logged')
    f.check('6 of 40 finished pairs' in js(pg, "return r.getElementById('pg').innerText") and '34 first quality' in js(pg, "return r.getElementById('pg').innerText"), 'step 6: 6 of 40 seconds, 34 first quality')


PLAN = [('Open a work order and see every stage at once', 'Behind by 24'),
        ('The stage that is falling behind stands out', 'Planned by now'),
        ('Leather used against standard, with offcuts logged', '95.7%'),
        ('The floor records work on a tablet at the station', 'Record 12 pairs'),
        ('Back on the board, Lasting catches up', 'Behind by 12'),
        ('Second quality is logged where it happens', '34 first quality')]

f = run_all(2, PLAN, ['108', '34 first quality'], extra={'before': {1: board, 2: cut, 3: cutd, 5: after}, 'after': end}, start=start)
print('\n%d failures' % len(f)); sys.exit(1 if f else 0)
