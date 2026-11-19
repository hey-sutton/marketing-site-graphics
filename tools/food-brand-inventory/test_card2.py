#!/usr/bin/env python3
"""Card 2 (list and detail): the README's numbers in Python, then the click through.
Run: python3 tools/food-brand-inventory/test_card2.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fb_tests import run_card, finish, js, ids, readonly_checks, keyboard_walk, clicks_only

ING = {'Peanuts': 3600, 'Raisins': 2700, 'Sunflower seeds': 1700}
assert sum(ING.values()) == 8000
LINES = {'ingredients': 8000, 'packaging': 2500, 'fee': 4000, 'freight': 500}
assert sum(LINES.values()) == 15000                               # cost lines sum to $15,000
Q, RCV = 2000, 1950
assert Q - RCV == 50                                              # variance is 2,000 minus 1,950
assert (Q - RCV) / Q * 100 == 2.5                                 # 2.5 percent
CPC = round(15000 / RCV, 2)
assert CPC == 7.69
assert abs(RCV * CPC - 15000) < RCV * 0.005                       # received cases times unit cost equals order cost within rounding
POS = {'PO-7741': 4000, 'PO-7742': 2500}
assert POS['PO-7741'] == LINES['fee'] and POS['PO-7742'] == LINES['packaging']   # the two POs match the fee and packaging lines
BASE = [300, 300, 550]
assert sum(BASE) == 1150 and 1150 + 8000 == 9150                  # the co-packer balance rises by the components sent
assert [500 * 0.6, 500 * 0.6, 1375 * 0.4] == BASE and [6000 * 0.6, 4500 * 0.6, 4250 * 0.4] == [3600, 2700, 1700]


def start(pg, f, when='start'):
    readonly_checks(pg, f, {}, when)
    t = js(pg, "return r.getElementById('dt').innerText")
    f.check(js(pg, "return r.querySelectorAll('.dt .sec,.dt .facts').length") == 0 and 'OP-1190' not in js(pg, "return r.querySelector('.g2').innerText"), '%s: no order open, the detail shows a prompt only' % when)
    f.check(not any(s in t for s in ('2,000', '$', '1,950')), '%s: nothing derived from the order shows' % when)
    f.check(ids(pg, 'bv') == '$1,150', '%s: the co-packer balance shows its existing $1,150' % when)


def s1(pg, f):
    f.check(ids(pg, 'pq', 'ost') == '2,000|Draft', 'step 1: OP-1190 opens with 2,000 cases preset, Draft')
    f.check(js(pg, "return r.querySelector('.ol .row').innerText").startswith('OP-1190'), 'step 1: the new order tops the list')


def s2(pg, f):
    f.check(ids(pg, 'ingt', 'bv', 'cl-ing', 'cl-frt', 'ctot') == '$8,000|$9,150|$8,000|$500|$8,500', 'step 2: $8,000 sent, balance $1,150 to $9,150, freight $500')
    f.check(ids(pg, 'bl-0', 'bl-1', 'bl-2') == '6,500 lb|5,000 lb|5,625 lb', 'step 2: component balances at the co-packer rise')


def s3(pg, f):
    f.check(ids(pg, 'pa-PO-7741', 'pa-PO-7742', 'cl-pak') == '$4,000|$2,500|$2,500', 'step 3: two POs, $4,000 fee and $2,500 packaging')


def s4(pg, f):
    f.check(ids(pg, 'cl-ing', 'cl-pak', 'cl-fee', 'cl-frt', 'ctot') == '$8,000|$2,500|$4,000|$500|$15,000', 'step 4: fee line $4,000, total $15,000')


def s5b(pg, f):
    f.check(js(pg, "var h=r.querySelector('.hint');return h&&h.id") == 'q-1950', 'step 5: the prompt points at the 1,950 chip first')


def s5(pg, f):
    f.check(ids(pg, 'rq', 'rv', 'rpc') == '1,950|50 (2.5%)|$7.69', 'step 5: 1,950 received, variance 50 (2.5%), $7.69 a case')
    f.check(ids(pg, 'bv', 'ost') == '$1,150|Received', 'step 5: components used, balance back to $1,150')


PLAN = [('A new outsourced order opens', '2,000'),
        ('Components go out, the co-packer balance rises', '$9,150'),
        ('Two POs from the same order', 'PO-7742'),
        ('The fee books against the order', '$15,000'),
        ('Cases back, with yield and cost per case', '$7.69')]
f = run_card(2, PLAN, ['$15,000', '1,950', '50 (2.5%)', '$7.69', '$4,000', '$2,500'], start=start,
             extra={'before': {4: s5b}, 'after_step': {0: s1, 1: s2, 2: s3, 3: s4, 4: s5}})
keyboard_walk(f, 2, 5)
clicks_only(f, 2, 1)
clicks_only(f, 2, 1, 358, 390)
finish(f)
