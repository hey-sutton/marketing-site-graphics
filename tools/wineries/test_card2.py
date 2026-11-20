#!/usr/bin/env python3
"""Card 2 (board): the README's dry goods numbers in Python, then the click through.
Run: python3 tools/wineries/test_card2.py"""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from wn_tests import run_card, finish, js, ids, readonly_checks, keyboard_walk, clicks_only

CASES, PER, BOTTLING, PAL = 1200, 12, 314, 700          # dates as month*100 + day: Mar 14 = 314
NEED = CASES * PER
assert NEED == 14400                                                          # need = cases x 12
DG = {'gl': (9000, [(6000, 328)]), 'ck': (12000, [(4000, 220)]), 'cp': (14400, []), 'lb': (15000, [])}
avail = lambda k, extra=(): DG[k][0] + sum(q for q, d in list(DG[k][1]) + list(extra) if d <= BOTTLING)
assert avail('gl') == 9000                                                    # an order arriving after Mar 14 is not counted
assert NEED - avail('gl') == 5400                                             # glass shortage 5,400
PALLETS = math.ceil((NEED - avail('gl')) / PAL)
assert PALLETS == 8 and PALLETS * PAL == 5600 and 5600 % PAL == 0 and 5600 - PAL < 5400   # next multiple of 700
assert avail('gl', [(5600, 306)]) == 14600 and 14600 - NEED == 200            # position after the PO
assert avail('ck') == 16000 and avail('ck') - NEED == 1600                    # corks surplus 1,600
assert all(avail(k) >= NEED for k in ('ck', 'cp', 'lb'))                     # corks, capsules and labels: no flag
assert avail('cp') - NEED == 0 and avail('lb') - NEED == 600


def start(pg, f, when='start'):
    readonly_checks(pg, f, {'ipl': 'Reserve Red, bottling Mar 14, 1,200 cases'}, when)
    f.check(js(pg, "return r.querySelectorAll('.pr,.pl,.cl2').length") == 0, '%s: no rows, order or check shown' % when)
    t = js(pg, "return r.querySelector('.g2').innerText")
    f.check(not any(s in t for s in ('14,400', '9,000', 'Glass', 'short', 'PO-')), '%s: nothing derived shows' % when)


def s1(pg, f):
    f.check(ids(pg, 'n-gl', 'n-ck', 'n-cp', 'n-lb') == '14,400|14,400|14,400|14,400', 'step 1: need 14,400 for each dry good')
    f.check(ids(pg, 'o-gl') == '', 'step 1: stock not shown yet')


def s2(pg, f):
    f.check(ids(pg, 'o-gl', 'o-ck', 'o-cp', 'o-lb') == '9,000|12,000|14,400|15,000', 'step 2: stock on hand')
    f.check(ids(pg, 'v-gl', 'v-ck', 'v-cp', 'v-lb') == '9,000|16,000|14,400|15,000', 'step 2: counts by Mar 14, the Mar 28 glass left out')
    f.check(js(pg, "return !!r.querySelector('#r-gl .ln.af #a-PO-2188') && !!r.querySelector('#r-ck .ln:not(.af) #a-PO-2191')"), 'step 2: Mar 28 glass after the date, Feb 20 corks before it')


def s3(pg, f):
    f.check(js(pg, "return r.getElementById('r-gl').classList.contains('sh')") and ids(pg, 'f-gl', 'p-gl') == 'Short|5,400 short', 'step 3: glass red, 5,400 short')
    f.check('late' in ids(pg, 'a-PO-2188'), 'step 3: the Mar 28 order is flagged late')
    f.check(ids(pg, 'f-ck', 'f-cp', 'f-lb') == 'No flag|No flag|No flag' and ids(pg, 'p-ck', 'p-lb') == '1,600 over|600 over', 'step 3: corks, capsules and labels show no flag')


def s4(pg, f):
    f.check(ids(pg, 'ppl', 'pbt', 'pos') == '8|5,600|Draft', 'step 4: PO of 8 pallets, 5,600 bottles')
    f.check('5,400 short ÷ 700 a pallet, rounded up = 8 pallets' in ids(pg, 'pcal'), 'step 4: next multiple of 700 shown')


def s5(pg, f):
    f.check(js(pg, "return r.getElementById('r-gl').classList.contains('ok')") and ids(pg, 'f-gl', 'p-gl', 'v-gl') == 'Clear|200 over|14,600', 'step 5: glass green, 14,600, 200 over')
    f.check(ids(pg, 'pos', 'pst') == 'Placed|Plan clear', 'step 5: order placed, plan clear')


PLAN = [('A bottling plan for a date', 'Capsules'),
        ('Stock, orders and arrival dates', '16,000'),
        ('The item marked short', '5,400 short'),
        ('A supplier order from the short line', 'PO-2207'),
        ('The plan clears once ordered', '200 over')]
f = run_card(2, PLAN, ['14,600', '200 over', '1,600 over', '5,600'], start=start,
             extra={'after_step': {0: s1, 1: s2, 2: s3, 3: s4, 4: s5}})
keyboard_walk(f, 2, 5)
clicks_only(f, 2, 0)
clicks_only(f, 2, 0, 358, 390)
finish(f)
