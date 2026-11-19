#!/usr/bin/env python3
"""Card 1 (record form with a side summary): the README's numbers in Python, then the click through.
Run: python3 tools/food-brand-inventory/test_card1.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fb_tests import run_card, finish, js, ids, readonly_checks, keyboard_walk, clicks_only

OH = {'wh': 1200, 'cp': 3400, 'tp': 5000}
CM = {'wh': 400, 'cp': 0, 'tp': 2500}
assert sum(OH.values()) == 9600                                   # total on hand is the sum of locations
MV = 1000
AFTER = {'wh': OH['wh'], 'cp': OH['cp'] - MV, 'tp': OH['tp'] + MV}
assert AFTER == {'wh': 1200, 'cp': 2400, 'tp': 6000}
assert sum(AFTER.values()) == 9600                                # total unchanged by the transfer
assert [k for k in OH if OH[k] != AFTER[k]] == ['cp', 'tp']       # only the two locations involved change
AV = {k: AFTER[k] - CM[k] for k in AFTER}
assert AV == {'wh': 800, 'cp': 2400, 'tp': 3500}                  # available = on hand less committed (6,000 - 2,500 = 3,500)
assert sum(CM.values()) == 2900 and sum(AV.values()) == 6700 == 9600 - 2900
LOTS = [1400, 2000]
assert sum(LOTS) == OH['cp']                                      # the lots add up to the co-packer number
assert [LOTS[0] - MV, LOTS[1]] == [400, 2000] and 400 + 2000 == AFTER['cp']   # oldest best before moves first
REP = 3100
assert OH['cp'] - REP == 300                                      # difference = on hand less reported


def start(pg, f, when='start'):
    readonly_checks(pg, f, {'iit': 'Trail Mix Case'}, when)
    t = js(pg, "return r.querySelector('.g1').innerText")
    f.check(js(pg, "return r.querySelectorAll('.loc .row,.lots,.bars,.dif').length") == 0, '%s: stock record and summary show a prompt only' % when)
    f.check(not any(s in t for s in ('1,200', '3,400', '5,000', '9,600', 'Ridgeway', 'TM-26', '3PL East')), '%s: nothing derived from the item shows' % when)


def s1(pg, f):
    f.check(ids(pg, 'oh-wh', 'oh-cp', 'oh-tp', 'oht', 'sto') == '1,200|3,400|5,000|9,600|9,600', 'step 1: 1,200, 3,400, 5,000, total 9,600')
    f.check(ids(pg, 'ohp') == '450' and 'not in your total' in js(pg, "return r.getElementById('sum').innerText"), 'step 1: 450 partner owned cases kept apart from the total')


def s2(pg, f):
    f.check(ids(pg, 'lq-TM-2611', 'lq-TM-2618') == '1,400|2,000', 'step 2: lots 1,400 and 2,000 (sum 3,400)')
    t = js(pg, "return r.querySelector('.lots').innerText")
    f.check('Mar 14, 2027' in t and 'Apr 2, 2027' in t, 'step 2: best before dates show')
    f.check(js(pg, "return r.querySelectorAll('[data-pick]').length") == 3, 'step 2: three preset quantity chips')


def s3b(pg, f):
    f.check(js(pg, "var h=r.querySelector('.hint');return h&&h.id") == 'q-1000', 'step 3: the prompt points at the 1,000 chip first')


def s3(pg, f):
    f.check(ids(pg, 'oh-wh', 'oh-cp', 'oh-tp', 'oht', 'sto') == '1,200|2,400|6,000|9,600|9,600', 'step 3: 1,200, 2,400, 6,000, total still 9,600')
    f.check(ids(pg, 'lq-TM-2611', 'lq-TM-2618') == '400|2,000', 'step 3: 1,000 leaves TM-2611, the oldest best before')


def s4(pg, f):
    f.check(ids(pg, 'cm-wh', 'cm-cp', 'cm-tp', 'av-wh', 'av-cp', 'av-tp') == '400|0|2,500|800|2,400|3,500', 'step 4: committed 400, 0, 2,500; available 800, 2,400, 3,500')
    f.check(ids(pg, 'cmtt', 'avt', 'scm', 'sav') == '2,900|6,700|2,900|6,700', 'step 4: committed 2,900, available 6,700')


def s5(pg, f):
    f.check(ids(pg, 'rep', 'ohs', 'dfq') == '3,100|3,400|300', 'step 5: reported 3,100, on hand 3,400, difference 300')


PLAN = [('One screen, every location', '9,600'),
        ('The lots behind the number', 'TM-2611'),
        ('Move finished cases to the 3PL', '6,000'),
        ('Committed to open orders at each location', '3,500'),
        ('On hand against what the partner reported', '300')]
f = run_card(1, PLAN, ['9,600', '2,400', '6,000', '2,900', '6,700', '3,100'], start=start,
             extra={'before': {2: s3b}, 'after_step': {0: s1, 1: s2, 2: s3, 3: s4, 4: s5}})
keyboard_walk(f, 1, 5)
clicks_only(f, 1, 1)
clicks_only(f, 1, 1, 358, 390)
finish(f)
