#!/usr/bin/env python3
"""Card 1 (record form with a side summary): the README's stock numbers in Python, then the click through.
Run: python3 tools/food-distributors/test_card1.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fd_tests import run_card, finish, js, ids, readonly_checks, keyboard_walk, clicks_only

# bin, in stock, expected, committed before, the order's allocation
MAIN = [('B-12-3', 700, 0, 500, 200), ('B-14-1', 500, 0, 400, 100), ('DK-2', 0, 600, 0, 0)]
COLD = [('C-01-2', 250, 0, 60, 0), ('C-03-1', 150, 0, 40, 0)]
ROP, ORDER, PO = 800, 300, 1000
AV = lambda i, e, c: i + e - c


def totals(rows, after=False):
    i = sum(r[1] for r in rows); e = sum(r[2] for r in rows); c = sum(r[3] + (r[4] if after else 0) for r in rows)
    return i, e, c, AV(i, e, c)


assert totals(MAIN) == (1200, 600, 900, 900)                         # 1,200 + 600 - 900 = 900
assert totals(COLD)[0] == 400 and totals(COLD)[2] == 100 and totals(COLD)[3] == 300
assert totals(MAIN, True) == (1200, 600, 1200, 600)                  # 1,200 + 600 - 1,200 = 600
assert sum(r[4] for r in MAIN) == ORDER                              # the order changes committed by exactly 300
for r in MAIN + COLD:                                                # available per row is never negative
    assert AV(r[1], r[2], r[3]) >= 0 and AV(r[1], r[2], r[3] + r[4]) >= 0
FLAG = lambda av: av < ROP
assert not FLAG(900) and FLAG(600)                                   # the flag shows only under 800
assert PO == 1000
OPEN_MAIN, OPEN_COLD = [300, 250, 350], [100]
assert sum(OPEN_MAIN) == totals(MAIN)[2] and sum(OPEN_COLD) == totals(COLD)[2]   # committed is the sum of open orders
assert sum(OPEN_MAIN) + ORDER == totals(MAIN, True)[2]


def rows(pg):
    """[[bin, in stock, expected, committed, available], ...] as shown, plus the total row."""
    return js(pg, """return [].map.call(r.querySelectorAll('#bn .row:not(.h)'),function(e){var s=e.querySelectorAll(':scope>span');
      return [s[0].querySelector('b')?s[0].querySelector('b').textContent:s[0].textContent].concat([1,2,3,4].map(function(i){return +s[i].textContent.replace(/,/g,'');}));});""")


def check_rows(pg, f, want, total, when):
    got = rows(pg)
    f.check([g[0] for g in got[:-1]] == [w[0] for w in want], '%s: bins %s' % (when, [g[0] for g in got]))
    f.check(all(g[4] == g[1] + g[2] - g[3] for g in got), '%s: available = in stock + expected - committed on every row' % when)
    f.check(got[-1][1:] == list(total), '%s: total row %s' % (when, got[-1][1:]))
    return got


def start(pg, f, when='start'):
    readonly_checks(pg, f, {'iit': 'Penne Pasta 20 lb Case'}, when)
    f.check(js(pg, "return r.querySelectorAll('#bn,.seg,#sav').length") == 0, '%s: no stock shown' % when)
    t = js(pg, "return r.querySelector('.g1').innerText")
    f.check(not any(s in t for s in ('1,200', '900', 'B-12-3', 'Rossi')), '%s: nothing derived shows' % when)


def s1(pg, f):
    check_rows(pg, f, MAIN, totals(MAIN), 'step 1 main')
    f.check(ids(pg, 'sav', 'scal', 'fst') == '900|1,200 + 600 − 900 = 900|In stock' and not js(pg, "return r.getElementById('trw').classList.contains('bad')"), 'step 1: 900 available, no flag')
    f.check(ids(pg, 'olc') == '900 cases', 'step 1: open orders add up to the 900 committed')


def s2(pg, f):
    check_rows(pg, f, COLD, totals(COLD), 'step 2 cold room')
    f.check(ids(pg, 'sav', 'scm') == '300|100', 'step 2: cold room 300 available, 100 committed')
    f.check(ids(pg, 'olc') == '100 cases', 'step 2: cold room orders add up to 100')


def s3(pg, f):
    got = check_rows(pg, f, MAIN, totals(MAIN, True), 'step 3 main after the order')
    before = [[r[0], r[1], r[2], r[3], AV(r[1], r[2], r[3])] for r in MAIN]
    diff = [(a[0], [g - b for g, b in zip(a[1:], b2[1:])]) for a, b2 in zip(got[:-1], before)]
    f.check(sum(d[1][2] for d in diff) == 300 and all(d[1][0] == 0 and d[1][1] == 0 for d in diff), 'step 3: only committed changes, by exactly 300 %s' % diff)
    f.check(ids(pg, 'sav', 'scm', 'fst') == '600|1,200|Below reorder point' and js(pg, "return r.getElementById('trw').classList.contains('bad')"), 'step 3: 600 available, the total row turns red')
    f.check(ids(pg, 'olc') == '1,200 cases', 'step 3: open orders with SO-3124 add up to 1,200')


def s4(pg, f):
    f.check('Short by 200' in ids(pg, 'snt'), 'step 4: short by 200 against 800')


def s5(pg, f):
    f.check(ids(pg, 'poq') == '1,000' and 'Rossi Imports' in ids(pg, 'por'), 'step 5: PO for 1,000 cases from Rossi Imports')


PLAN = [('One item, its whole stock position', '900'),
        ('Each warehouse and bin', 'C-01-2'),
        ('Available drops with the order', '600'),
        ('A shortage, flagged on the item', 'Short by'),
        ('A purchase order from the shortage', 'PO-4471')]
f = run_card(1, PLAN, ['1,200', '600', 'PO-4471', '1,000'], start=start,
             extra={'after_step': {0: s1, 1: s2, 2: s3, 3: s4, 4: s5}})
keyboard_walk(f, 1, 5)
clicks_only(f, 1, 0)
clicks_only(f, 1, 0, 358, 390)
finish(f)
