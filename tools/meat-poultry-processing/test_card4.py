#!/usr/bin/env python3
"""Card 4 (record form with a side summary): the README's run numbers in Python, then the click through.
Run: python3 tools/meat-poultry-processing/test_card4.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from mp_tests import run_card, finish, js, ids, readonly_checks, keyboard_walk, clicks_only

ON, ISS = 2400, 1000
assert ON - ISS == 1400                                # meat lot falls from 2,400 to 1,400
OUT_G, BAG, CTN = 420 * 1000, 50, 120
BAGS = OUT_G // BAG
assert OUT_G % BAG == 0 and BAGS == 8400               # bags = 420,000 g / 50 g
assert BAGS % CTN == 0 and BAGS // CTN == 70           # cartons = 8,400 / 120
SPICE, CURE = 25, 5

ALL = {'iod': 'JRK-3310, Beef Jerky 420 kg', 'ilt': 'BEEF-24-0731', 'iwt': '420'}


def num(x):
    return int(x.replace(',', '').replace('−', '').split()[0])


def start(pg, f, when='start'):
    readonly_checks(pg, f, {'iod': 'JRK-3310, Beef Jerky 420 kg'}, when)
    f.check(js(pg, "return r.querySelectorAll('.sec,.mi,#fg').length") == 0, '%s: no order record or movements shown' % when)
    t = js(pg, "return r.querySelector('.g1').innerText")
    f.check(not any(s in t for s in ('8,400', '1,400', 'FG-7701', 'BEEF-24-0731', 'Feb 2')), '%s: nothing derived shows' % when)


def s1(pg, f):
    readonly_checks(pg, f, ALL, 'step 1')
    f.check(js(pg, "return r.querySelectorAll('#stg .sx').length") == 2 and 'Ready to eat' in ids(pg, 'stg'), 'step 1: raw and ready to eat stages')
    f.check(js(pg, "return r.querySelectorAll('.mi').length") == 0, 'step 1: no stock moved yet')


def s2(pg, f):
    b, a = num(ids(pg, 'lb')), num(ids(pg, 'la'))
    f.check((b, a) == (2400, 1400) and b - a == ISS, 'step 2: BEEF-24-0731 falls %d to %d after the 1,000 kg issue' % (b, a))
    f.check(ids(pg, 'isd') == '1,000 kg issued', 'step 2: 1,000 kg issued')


def s3(pg, f):
    for k, q in (('sb', SPICE), ('cu', CURE), ('bg', BAGS), ('ct', BAGS // CTN)):
        t = ids(pg, 'm-' + k)
        f.check(('−%s' % format(q, ',')) in t, 'step 3: %s deducts %d on its own (%s)' % (k, q, t[-30:]))
    f.check(js(pg, "return r.querySelectorAll('#cl .c-ok').length") == 4, 'step 3: every component shows deducted')


def s4(pg, f):
    f.check('420,000 g ÷ 50 g = 8,400' in ids(pg, 'pbg') and '8,400 ÷ 120 = 70' in ids(pg, 'pct'), 'step 4: 8,400 bags and 70 cartons on screen')


def s5(pg, f):
    f.check(ids(pg, 'fgl', 'fpk', 'fub') == 'FG-7701|Nov 2|Feb 2', 'step 5: FG-7701 with pack Nov 2 and use by Feb 2')
    f.check('New lot' in ids(pg, 'fg') and '+420 kg' in ids(pg, 'fg'), 'step 5: the finished lot is new and enters stock at 420 kg')
    f.check(ids(pg, 'mvn') == '6', 'step 5: six stock movements')


PLAN = [('A jerky order with two stages', 'Ready to eat'),
        ('Meat issued by lot', '1,400'),
        ('Spices and packaging deduct on their own', 'Deducted'),
        ('Weight out of the dehydrator', '8,400'),
        ('The finished lot enters stock', 'FG-7701')]
f = run_card(4, PLAN, ['1,400', '8,400', '70', 'Nov 2', 'Feb 2', 'New lot'], start=start,
             extra={'after_step': {0: s1, 1: s2, 2: s3, 3: s4, 4: s5}})
keyboard_walk(f, 4, 5)
clicks_only(f, 4, 0)
clicks_only(f, 4, 0, 358, 390)
finish(f)
