#!/usr/bin/env python3
"""Card 3 (stage chain): the README's prices in Python (cents), then the click through.
Run: python3 tools/food-distributors/test_card3.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fd_tests import run_card, finish, js, ids, readonly_checks, keyboard_walk, clicks_only

# item: cases, list, customer price list, (break minimum, break price) or None, available before
L1 = (200, 3800, 3500, (100, 3350), 900)
L2 = (50, 9200, 8800, None, 180)
def price(l, applied=True):
    if not applied:
        return l[1]
    return l[3][1] if l[3] and l[0] >= l[3][0] else l[2]
assert 200 * 3350 == 670000 and price(L1) * L1[0] == 670000          # line 1 = 200 x 33.50 = 6,700.00
assert 50 * 8800 == 440000 and price(L2) * L2[0] == 440000           # line 2 = 50 x 88.00 = 4,400.00
assert price(L1) * L1[0] + price(L2) * L2[0] == 1110000              # total 11,100.00
assert price(L1) == L1[3][1] and price(L2) == L2[2]                  # the break applies only to line 1
assert price((99,) + L1[1:]) == 3500                                 # under 100 cases there is no break
assert sum(price(l, False) * l[0] for l in (L1, L2)) == 1220000      # 12,200.00 at list
AV_AFTER = (L1[4] - L1[0], L2[4] - L2[0])
assert AV_AFTER == (700, 130)                                        # reserved equals ordered, available falls by it


def start(pg, f, when='start'):
    readonly_checks(pg, f, {'icu': 'Greenfield Market'}, when)
    f.check(js(pg, "return r.querySelectorAll('.ql .row,.pl,.sk,.stg:not(.e)').length") == 0, '%s: quote, prices, stock and chain empty' % when)
    t = js(pg, "return r.querySelector('.g3c').innerText")
    f.check(not any(s in t for s in ('$', 'Penne', '200', 'SO-3110')), '%s: nothing derived shows' % when)


def s1(pg, f):
    f.check(ids(pg, 'p0', 't0', 'p1', 't1', 'qtt') == '$38.00|$7,600.00|$92.00|$4,600.00|$12,200.00', 'step 1: two lines at list, $12,200.00')
    f.check(js(pg, "return r.getElementById('cvb').disabled"), 'step 1: Convert waits for pricing')


def s2(pg, f):
    f.check(ids(pg, 'p0', 't0', 'p1', 't1', 'qtt') == '$33.50|$6,700.00|$88.00|$4,400.00|$11,100.00', 'step 2: $6,700.00 + $4,400.00 = $11,100.00')
    f.check(ids(pg, 'src0', 'src1') == 'Break, 100 or more|Price list', 'step 2: the break applies to line 1 only')


def s3(pg, f):
    f.check(ids(pg, 'co', 'cq', 'ost') == '$11,100.00|$11,100.00|Order SO-3110', 'step 3: SO-3110 total equals the quote total')


def s4(pg, f):
    f.check(ids(pg, 'r0', 'r1', 'a0', 'a1', 'cr') == '200|50|700|130|250 of 250', 'step 4: reserved equals ordered, available 700 and 130')


def s5(pg, f):
    f.check(ids(pg, 'lnk', 'ost') == 'SO-3110 order status|Link sent', 'step 5: status link chip')


PLAN = [('A quote with two lines', '$12,200.00'),
        ('Customer price list and a quantity break', '$11,100.00'),
        ('Quote converted to a sales order', 'SO-3110'),
        ('Stock reserved against the order', '250 of 250'),
        ('Order status link sent', 'SO-3110 order status')]
f = run_card(3, PLAN, ['$6,700.00', '$4,400.00', '$11,100.00', '700', '130'], start=start,
             extra={'after_step': {0: s1, 1: s2, 2: s3, 3: s4, 4: s5}})
keyboard_walk(f, 3, 5)
clicks_only(f, 3, 0)
clicks_only(f, 3, 0, 358, 390)
finish(f)
