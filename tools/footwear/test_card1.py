#!/usr/bin/env python3
"""Card 1 click through (both modes), numbers, layout, variety, timing, navigation and phone checks.
Run: python3 tools/footwear/test_card1.py. Counts are whole pairs; leather is square feet to one decimal."""
import math, os, sys
from decimal import Decimal, ROUND_HALF_UP
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from footwear_tests import run_all, js, testlib
from playwright.sync_api import sync_playwright

# ---- the brief's numbers, derived independently of the card ----
SZ = [7, 8, 9, 10, 11, 12]
OH = {'B': [24, 36, 18, 40, 32, 20], 'S': [16, 28, 34, 30, 22, 14], 'N': [12, 22, 26, 28, 20, 10]}
CM = {'B': [10, 22, 46, 28, 30, 12], 'S': [8, 12, 20, 24, 18, 6], 'N': [6, 14, 30, 12, 14, 4]}
AV = {k: [o - c for o, c in zip(OH[k], CM[k])] for k in OH}
assert AV == {'B': [14, 14, -28, 12, 2, 8], 'S': [8, 16, 14, 6, 4, 8], 'N': [6, 8, -4, 16, 6, 6]}  # the brief's table
assert sum(map(sum, OH.values())) == 432 and sum(map(sum, CM.values())) == 316 and sum(map(sum, AV.values())) == 116
SHORT_R = [(k, SZ[i]) for k in 'BSN' for i in range(6) if AV[k][i] < 0]
assert SHORT_R == [('B', 9), ('N', 9)]


def hu(x):
    return int(Decimal(str(x)).quantize(Decimal('1'), rounding=ROUND_HALF_UP))


OHW = {k: [hu(v * Decimal('0.4')) for v in OH[k]] for k in OH}
CMW = {k: [hu(v * Decimal('0.3')) for v in CM[k]] for k in CM}
AVW = {k: [o - c for o, c in zip(OHW[k], CMW[k])] for k in OHW}
for k in 'BSN':
    for i in range(6):
        assert AVW[k][i] == OHW[k][i] - CMW[k][i] and AV[k][i] == OH[k][i] - CM[k][i]
assert (sum(map(sum, OHW.values())), sum(map(sum, CMW.values())), sum(map(sum, AVW.values()))) == (173, 95, 78)
assert AVW['B'][2] == -7 and OHW['B'][2] == 7 and CMW['B'][2] == 14
SHORT_W = [(k, SZ[i]) for k in 'BSN' for i in range(6) if AVW[k][i] < 0]
assert SHORT_W == [('B', 9)]
# shortage detail for Black size 9 Regular
PAIRS = CM['B'][2] - OH['B'][2]
assert PAIRS == 28 and 18 + 16 + 12 == 46
NEED = Decimal('3.0') * PAIRS
GAP = NEED - Decimal('61.5')
assert NEED == Decimal('84.0') and GAP == Decimal('22.5')
PO = Decimal(math.ceil(GAP / 5) * 5)
assert PO == Decimal('25') and PO * Decimal('4.60') == Decimal('115.00')
# open orders: Regular sums to the committed total, Wide rounds each order at 0.3 and sums to the Wide committed total
ORD = [96, 84, 62, 44, 30]
assert sum(ORD) == 316 and sum(hu(o * Decimal('0.3')) for o in ORD) == 95

CELLS = "var o={};r.querySelectorAll('.gc').forEach(function(c){o[c.id]=c.querySelector('b').textContent;});return o;"


def grid_ok(pg, f, w, want, label):
    got = js(pg, CELLS)
    exp = {'c-%s-%d-%s' % (k, SZ[i], w): str(want[k][i]) for k in 'BSN' for i in range(6)}
    f.check(got == exp, '%s: all 18 cells show available = on hand minus committed' % label)


def start(pg, f):
    f.check(js(pg, "return r.querySelector('.fwin').getAttribute('data-scr')") == 'Style search', 'start: the empty style search')
    t = js(pg, "return r.getElementById('pg').innerText")
    f.check(js(pg, "return r.querySelectorAll('.gc,.tile').length") == 0 and '432' not in t and '28' not in t, 'start: no grid, counts or totals before a style is picked')
    f.check(js(pg, "return r.getElementById('iq').value") == '', 'start: the search field is empty')


def bad_search(pg, f):
    start(pg, f)
    js(pg, "var e=r.getElementById('iq');e.value='XX-999';e.dispatchEvent(new Event('input',{bubbles:true}))")
    pg.locator('#cv #iq').press('Enter'); pg.wait_for_timeout(300)
    f.check(js(pg, "return r.getElementById('fs').classList.contains('err')"), 'step 1: a style that does not exist shows an inline error')
    js(pg, "var e=r.getElementById('iq');e.value='';e.dispatchEvent(new Event('input',{bubbles:true}))")


def matrix(pg, f):
    grid_ok(pg, f, 'R', AV, 'step 2 Regular')
    f.check(js(pg, "return [r.getElementById('t-oh'),r.getElementById('t-cm'),r.getElementById('t-av'),r.getElementById('t-sh')].map(function(e){return e.textContent}).join('|')") == '432|316|116|2', 'step 2: totals 432, 316, 116 and 2 short cells')
    f.check(js(pg, "return [].map.call(r.querySelectorAll('.gc.short'),function(e){return e.id}).join(',')") == 'c-B-9-R,c-N-9-R', 'step 2: Black 9 and Navy 9 Regular are flagged short')


def detail(pg, f):
    f.check(js(pg, "return r.getElementById('d-sh').textContent+'|'+r.getElementById('m-need').textContent+'|'+r.getElementById('m-gap').textContent") == '28|84.0|Short 22.5 sq ft', 'step 3: 28 short, 84.0 sq ft needed, 22.5 short')
    f.check(js(pg, "return r.querySelectorAll('.mt .ch.c-bad').length") == 1, 'step 3: leather is the only short material')


def po(pg, f):
    f.check(js(pg, "return r.getElementById('iq2').value") == '25.0', 'step 4: PO quantity prefilled at 25.0 sq ft')
    f.check(js(pg, "return r.getElementById('amt2').textContent") == '$115.00', 'step 4: PO total $115.00')
    js(pg, "var e=r.getElementById('iq2');e.value='10';e.dispatchEvent(new Event('input',{bubbles:true}))")
    pg.locator('#cv .hint').first.click(); pg.wait_for_timeout(400)
    f.check(js(pg, "return r.getElementById('fq').classList.contains('err')"), 'step 4: less than the short shows an inline error')
    js(pg, "var e=r.getElementById('iq2');e.value='25.0';e.dispatchEvent(new Event('input',{bubbles:true}))")


def raised(pg, f):
    f.check(js(pg, "var p=r.getElementById('po-flag');return !!p&&p.parentNode.id==='c-B-9-R'"), 'step 5: PO raised sits on the Black 9 Regular cell')


def end(pg, f):
    grid_ok(pg, f, 'W', AVW, 'step 5 Wide')
    f.check(js(pg, "return r.getElementById('t-oh').textContent+'|'+r.getElementById('t-cm').textContent+'|'+r.getElementById('t-av').textContent") == '173|95|78', 'step 5: Wide totals 173, 95, 78')


def enter(f):
    """Typing works and Enter submits, at desktop and phone width."""
    with sync_playwright() as p:
        b = testlib.browser(p)
        for vw, cw, lab in ((1300, 604, 'desktop'), (390, 358, 'phone')):
            pg, errs = testlib.open_card(b, 1, vw, cw)
            pg.locator('#cv').scroll_into_view_if_needed()
            pg.locator('#cv .mtg [data-m="try"]').click(); pg.wait_for_timeout(500)
            pg.locator('#cv #iq').click(); pg.keyboard.type('hr-210'); pg.keyboard.press('Enter'); pg.wait_for_timeout(700)
            f.check(js(pg, "return r.querySelector('.fwin').getAttribute('data-scr')") == 'Size matrix', '%s: typing hr-210 and pressing Enter opens the grid' % lab)
            f.check(not errs, '%s typing: no page errors' % lab)
            pg.close()
        b.close()


PLAN = [('Every size and color of a style in one grid', '432'),
        ('A short cell opens to the materials behind it', 'Short 22.5 sq ft'),
        ('The purchase order is drafted from the gap', '$115.00'),
        ('Back on the grid, the cell shows PO raised', 'PO raised'),
        ('Wide has its own counts', '173')]

f = run_all(1, PLAN, ['173', '95', '78', '-7'], extra={'before': {0: bad_search, 2: detail, 3: po, 4: raised}, 'after': end},
            drag=enter, start=start)
# the grid numbers after step 2 are checked in a short Try it run of their own
with sync_playwright() as p:
    b = testlib.browser(p)
    pg, errs = testlib.open_card(b, 1, 1300, 604)
    pg.locator('#cv').scroll_into_view_if_needed()
    pg.locator('#cv .mtg [data-m="try"]').click(); pg.wait_for_timeout(1500)
    pg.locator('#cv .hint').first.click(); pg.wait_for_timeout(900)
    matrix(pg, f)
    pg.close(); b.close()
print('\n%d failures' % len(f)); sys.exit(1 if f else 0)
