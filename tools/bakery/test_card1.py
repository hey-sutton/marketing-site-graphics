#!/usr/bin/env python3
"""Card 1 (layer panels and cost waterfall): the brief's numbers in Python, then the full click through in the browser.
Run: python3 tools/bakery/test_card1.py"""
import os, sys
from decimal import Decimal as D
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bk_tests import run_card, finish, js, pill, testlib, ids, enter_submits

# ---- the brief's numbers, derived independently of the card ----
DOUGH = {'Bread flour': (D('25'), D('0.90')), 'Whole milk': (D('14'), D('1.10')), 'Butter': (D('6'), D('7.50')), 'Sugar': (D('3'), D('1.20')), 'Yeast': (D('0.5'), D('6.00'))}
FILL = {'Brown sugar': (D('4'), D('1.60')), 'Cinnamon': (D('0.25'), D('14.00')), 'Butter': (D('2'), D('7.50'))}
GLAZE = {'Powdered sugar': (D('5'), D('1.40')), 'Cream cheese': (D('2.5'), D('6.00')), 'Milk': (D('1'), D('1.10'))}
kgs = lambda L: sum(q for q, _ in L.values())
cst = lambda L: sum(q * p for q, p in L.values())
assert kgs(DOUGH) == D('48.5') and kgs(FILL) == D('6.25') and kgs(GLAZE) == D('8.5')
assert cst(DOUGH) == D('89.50') and cst(FILL) == D('24.90') and cst(GLAZE) == D('23.10')
ING = cst(DOUGH) + cst(FILL) + cst(GLAZE)
assert ING == D('137.50')
PKG, LAB = 250 * D('0.05'), 2 * D('22.00')
assert PKG == D('12.50') and LAB == D('44.00') and ING + PKG + LAB == D('194.00')
assert D('194.00') / 250 == D('0.776')
assert kgs(DOUGH) * 3 == D('145.5') and kgs(FILL) * 3 == D('18.75') and kgs(GLAZE) * 3 == D('25.5')
assert D('75') / 25 == 3
assert ING * 3 == D('412.50') and PKG * 3 == D('37.50') and LAB * 3 == D('132.00') and D('412.50') + D('37.50') + D('132.00') == D('582.00')
assert 5 * D('7.50') == D('37.50') and D('194.00') - D('7.50') == D('186.50') and D('186.50') * 3 == D('559.50')
assert D('186.50') / 250 == D('0.746') and D('0.776') - D('0.746') == D('0.030')
assert (6 + 2) * D('0.50') == D('4.00') and D('194.00') + D('4.00') == D('198.00') and D('198.00') / 250 == D('0.792') and D('198.00') * 3 == D('594.00')
assert (6 + 2) * 3 == 24 and 24 * D('0.50') == D('12.00') and D('582.00') + D('12.00') == D('594.00')
BATCH = [[q * 3 for q, _ in L.values()] for L in (DOUGH, FILL, GLAZE)]


def kg(x):
    return '{:,.3f}'.format(x)


def start(pg, f, when='start'):
    t = js(pg, "return r.querySelector('.k1').innerText")
    f.check(js(pg, "return r.getElementById('kpi').value+'|'+r.getElementById('kri').value") == '|', '%s: product and batch inputs are empty' % when)
    f.check(js(pg, "return r.querySelectorAll('.kpn,.kwc').length") == 0, '%s: no layer panels and no waterfall' % when)
    f.check(not any(s in t for s in ('48.500', 'Bread flour', '$0.776', '$194.00', 'v3 previous', 'sacks')), '%s: nothing derived from the product shows' % when)


def bad_then_type(pg, f):
    inp = pg.locator('#cv #kpi')
    inp.click(); inp.press_sequentially('Croissant'); inp.press('Enter'); pg.wait_for_timeout(300)
    f.check(js(pg, "return r.getElementById('kfp').classList.contains('err')"), 'step 1: an unknown product shows an inline error')
    f.check('Your turn1 of 5' in pill(pg), 'step 1: an unknown product does not advance')
    inp.fill(''); inp.press_sequentially('cinnamon roll'); pg.wait_for_timeout(100)
    f.check(js(pg, "return r.getElementById('kpi').value") == 'cinnamon roll', 'step 1: typing works in the product input')


def type750(pg, f):
    inp = pg.locator('#cv #kri')
    f.check(inp.input_value() == '250', 'step 2: the batch starts at the standard 250')
    inp.fill('0'); pg.locator('#cv #ksc').click(); pg.wait_for_timeout(300)
    f.check('Your turn2 of 5' in pill(pg) and js(pg, "return r.getElementById('kfr').classList.contains('err')"), 'step 2: a batch of 0 shows an inline error and does not advance')
    inp.fill(''); inp.press_sequentially('750')


def type800(pg, f):
    inp = pg.locator('#cv #kpr')
    inp.fill(''); inp.press_sequentially('8.00')


def s1(pg, f):
    f.check(ids(pg, 'kt0', 'kt1', 'kt2') == '48.500 kg|6.250 kg|8.500 kg', 'step 1: dough 48.500, filling 6.250, glaze 8.500 kg at 250')
    f.check(js(pg, "return r.querySelectorAll('.kpn').length") == 3, 'step 1: three layer panels')


def s2(pg, f):
    f.check(ids(pg, 'kt0', 'kt1', 'kt2') == '145.500 kg|18.750 kg|25.500 kg', 'step 2: dough 145.500, filling 18.750, glaze 25.500 kg')
    f.check(ids(pg, 'ksk') == '3 sacks of 25 kg', 'step 2: "3 sacks of 25 kg" beside the flour')
    got = [[ids(pg, 'kq%d%d' % (i, j)) for j in range(len(B))] for i, B in enumerate(BATCH)]
    f.check(got == [[kg(q) for q in B] for B in BATCH], 'step 2: every batch quantity is 3 times the per 250 quantity')
    f.check(ids(pg, 'kbf', 'kbl') == '3|6 hours', 'step 2: factor 3, labor 6 hours')


def s3(pg, f):
    f.check(ids(pg, 'kw-ing', 'kw-pkg', 'kw-lab', 'kw-tot', 'kw-per') == '$412.50|$37.50|$132.00|$582.00|$0.776', 'step 3: $412.50, $37.50, $132.00, total $582.00, $0.776 per roll')
    f.check(ids(pg, 'kc0', 'kc1', 'kc2') == '$268.50|$74.70|$69.30', 'step 3: layer costs $268.50 + $74.70 + $69.30 = $412.50')


def s4(pg, f):
    f.check(ids(pg, 'kw-tot', 'kw-per', 'kdd') == '$559.50|$0.746|+$0.030 per roll in v4', 'step 4: v3 total $559.50, $0.746 per roll, +$0.030 per roll in v4')
    f.check(ids(pg, 'kq02') == '15.000', 'step 4: v3 dough butter 15.000 kg for 750')


def s5(pg, f):
    f.check(ids(pg, 'kw-tot', 'kw-per', 'kbu', 'kvc') == '$594.00|$0.792|24.000 kg|v4 current', 'step 5: back on v4, butter 24.000 kg, total $594.00, $0.792 per roll')
    f.check(ids(pg, 'kw-ing') == '$424.50', 'step 5: ingredients $412.50 + $12.00 = $424.50')


PLAN = [('Pick a layered product and every layer loads', '48.500 kg'),
        ('Enter a batch size and every layer scales', '145.500 kg'),
        ('The cost rolls up to a cost per roll', '$0.776'),
        ('Compare with the previous BOM version', '$0.746'),
        ('Change an ingredient price and watch the cost move', '$594.00')]

f = run_card(1, PLAN, ['$594.00', '$0.792', '24.000 kg'], start=start,
             extra={'before': {0: bad_then_type, 1: type750, 4: type800}, 'after_step': {0: s1, 1: s2, 2: s3, 3: s4, 4: s5}})
enter_submits(f, 1, '#kpi', 'Cinnamon Roll', 'Your turn2 of 5')
finish(f)
