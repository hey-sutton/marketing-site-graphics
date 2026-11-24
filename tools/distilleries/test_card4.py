#!/usr/bin/env python3
"""Card 4 click through (both modes), numbers, layout, variety, timing, navigation and phone checks.
Run: python3 tools/distilleries/test_card4.py. The brief's sums are asserted in numbers_check.py first."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numbers_check  # noqa: F401  (asserts 560, the 400 + 100 + 60 split and 276.00)
from distilleries_tests import run_all, js, testlib


def tiles(pg):
    return js(pg, "return ['t-st-v','t-ex-v','t-cm-v','t-av-v'].map(function(i){return r.getElementById(i).textContent}).join('|')")


def setv(pg, i, v):
    js(pg, "var e=r.getElementById('sp-%d');e.value='%s';e.dispatchEvent(new Event('input',{bubbles:true}))" % (i, v))


def start(pg, f):
    f.check(tiles(pg) == '900|300|640|560', 'start: the four tiles hold baseline stock 900, 300, 640, 560')
    f.check(js(pg, "return r.querySelectorAll('#sp-0,#commit,#mk-sp').length") == 0, 'start: the split table is empty')


def split(pg, f):
    f.check(js(pg, "return [0,1,2].map(function(i){return r.getElementById('sp-'+i).value}).join('|')") == '400|100|60', 'step 2: distributors 400, tasting room 100, online 60')
    f.check(js(pg, "return r.getElementById('sp-t').textContent+'|'+r.getElementById('sp-left').textContent") == '560|0 left', 'step 2: total 560, 0 left')
    setv(pg, 1, '150')
    f.check(js(pg, "return r.getElementById('sp-t').textContent+'|'+r.getElementById('sp-av').textContent") == '610|-50', 'step 3: typing a number updates the total live')
    pg.locator('#cv .hint').first.click(); pg.wait_for_timeout(400)
    f.check(js(pg, "return r.getElementById('f-0').classList.contains('err')"), 'step 3: a split over 560 shows an inline error')
    setv(pg, 1, '100')


def committed(pg, f):
    f.check(tiles(pg) == '900|300|1,200|0', 'step 3: committed 640 to 1,200, available 560 to 0')


def dry(pg, f):
    f.check(js(pg, "return ['d-nd-v','d-oh-v','d-sh-v'].map(function(i){return r.getElementById(i).textContent}).join('|')") == '1,800|1,500|300', 'step 4: 1,800 bottles needed, 1,500 on hand, 300 short')


def end(pg, f):
    f.check(js(pg, "return r.getElementById('po-q').textContent+'|'+r.getElementById('po-t').textContent") == '300|$276.00', 'step 5: PO for 300 bottles at $0.92, $276.00')


PLAN = [('Four live numbers, and how available is figured', '560'), ('A split across three channels', '0 left'),
        ('Committed and available update', '1,200'), ('The next run is short on glass', '1,800'), ('The PO covers the shortage', '$276.00')]
f = run_all(4, PLAN, ['$276.00', '300'], extra={'before': {0: start, 2: split, 3: committed, 4: dry}, 'after': end}, start=start)
print('\n%d failures' % len(f)); sys.exit(1 if f else 0)
