#!/usr/bin/env python3
"""Card 2 (BOM comparison and approval stepper): the brief's numbers in Python (cents), then the click through.
Run: python3 tools/automotive/test_card2.py"""
import os, sys
from datetime import date
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from auto_tests import run_card, finish, js, pill

# ---- the brief's numbers, derived independently of the card ----
REV_C = [('STP-300', 1, 210), ('FST-118', 2, 46), ('BSH-07', 1, 120), ('LBL-12', 1, 60)]
REV_D = [('STP-300', 1, 210), ('FST-121', 2, 52), ('WSH-044', 2, 5), ('BSH-07', 1, 120), ('LBL-12', 1, 60)]
C = sum(q * u for _, q, u in REV_C)
D = sum(q * u for _, q, u in REV_D)
assert 2 * 46 == 92 and 2 * 52 == 104 and 2 * 5 == 10
assert C == 482 and D == 504 and D - C == 22            # $4.82, $5.04, +$0.22
EFF = date(2026, 12, 1)
WOS = {'WO-7132': date(2026, 11, 20), 'WO-7140': date(2026, 12, 2), 'WO-7146': date(2026, 12, 9)}
SWITCH = [w for w, d in WOS.items() if d >= EFF]
assert SWITCH == ['WO-7140', 'WO-7146'] and len(SWITCH) == 2 and len(WOS) - len(SWITCH) == 1


def ids(pg, *names):
    return js(pg, "return %r.map(function(i){var e=r.getElementById(i);return e?e.textContent:null}).join('|')" % list(names))


def start(pg, f, when='start'):
    t = js(pg, "return r.querySelector('.g2').innerText")
    f.check(js(pg, "return r.querySelectorAll('.tb,.apv .sp,.wo,.row.sel').length") == 0, '%s: ECO list only, nothing selected, empty comparison' % when)
    f.check('$' not in t and 'WO-' not in t and 'Rev D' not in t and 'FST-121' not in t, '%s: nothing derived from ECO-0192 shows' % when)


def s1(pg, f):
    t = js(pg, "return r.getElementById('apv').innerText")
    f.check('A. Patel' in t and 'L. Ortiz' in t and js(pg, "return r.querySelectorAll('.apv .sp').length") == 3, 'step 1: stepper with engineering review (A. Patel), quality sign off (L. Ortiz), release')


def s2(pg, f):
    f.check(js(pg, "return [r.querySelectorAll('.tb .row.rm').length,r.querySelectorAll('.tb .row.ad').length].join()") == '1,2', 'step 2: one line out (FST-118), two in (FST-121, WSH-044)')


def s3(pg, f):
    f.check(ids(pg, 'rc', 'rd', 'dlt') == '$4.82|$5.04|+$0.22 per assembly', 'step 3: $4.82 to $5.04, +$0.22')
    f.check(ids(pg, 'cc-FST-118', 'cd-FST-121', 'cd-WSH-044', 'cc-STP-300', 'cd-STP-300') == '$0.92|$1.04|$0.10|$2.10|$2.10', 'step 3: line costs 0.92, 1.04, 0.10, 2.10')


def bad_date(pg, f):
    i = pg.locator('#cv #ief')
    i.fill('Dec first')
    pg.locator('#cv .hint').first.click(); pg.wait_for_timeout(300)
    f.check(js(pg, "return r.getElementById('fef').classList.contains('err')"), 'step 4: an invalid date shows an inline error')
    f.check('Your turn4 of 5' in pill(pg), 'step 4: an invalid date does not advance')
    i.fill('12/01/2026')


def s4(pg, f):
    f.check(ids(pg, 'spl', 'r-WO-7132', 'r-WO-7140', 'r-WO-7146') == '1 stays, 2 switch|Stays on Rev C|Switches to Rev D|Switches to Rev D', 'step 4: WO-7132 stays, WO-7140 and WO-7146 switch')


def s5(pg, f):
    f.check(ids(pg, 'ast') == 'Released' and js(pg, "return r.querySelectorAll('.apv .sp.ok').length") == 3, 'step 5: all three steps approved, status Released')


PLAN = [('An engineering change opens with the BOM and the work orders it touches', 'ECO-0192'),
        ('Both revisions side by side, changes highlighted', 'FST-121'),
        ('The cost change rolls up from every line', '+$0.22 per assembly'),
        ('Open work orders switch only after the date', '1 stays, 2 switch'),
        ('Approvals step through in order, then the change is released', 'Rev D released')]

f = run_card(2, PLAN, ['$4.82', '$5.04', '+$0.22 per assembly', 'Stays on Rev C', 'Released'], start=start,
             extra={'before': {3: bad_date}, 'after_step': {0: s1, 1: s2, 2: s3, 3: s4, 4: s5}})
finish(f)
