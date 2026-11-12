#!/usr/bin/env python3
"""Card 3 (cut table, split view with bars): the brief's numbers in Python, then the full click through in the browser.
Run: python3 tools/textile/test_card3.py"""
import os, sys
from decimal import Decimal
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from textile_tests import run_card, finish, js, pill, testlib
from playwright.sync_api import sync_playwright

# ---- the brief's numbers, derived independently of the card ----
assert 36 * 3 == 108 and 109 - 108 == 1 and 119 - 109 == 10
assert Decimal(108) * Decimal('0.015') == Decimal('1.62') and 1 <= Decimal('1.62')


def ids(pg, *names):
    return js(pg, "return %r.map(function(i){var e=r.getElementById(i);return e?e.textContent:null}).join('|')" % list(names))


def start(pg, f, when='start'):
    t = js(pg, "return r.querySelector('.g3').innerText")
    f.check('CO-771' in t and 'DL-2611-B' in t and '3 of 36 yd' in t, '%s: the order header CO-771, needs DL-2611-B, 3 lays of 36 yd' % when)
    f.check(js(pg, "return r.getElementById('sin').value") == '', '%s: the scan field is empty' % when)
    f.check(js(pg, "return r.querySelectorAll('.bar,.sg').length") == 0, '%s: no roll bar drawn' % when)
    f.check(not any(s in t for s in ('119', '109', 'R-48214-R1', 'Within tolerance')), '%s: nothing derived from a scan shows' % when)


def wrong_first(pg, f):
    inp = pg.locator('#cv #sin')
    inp.click(); inp.press_sequentially('R-12345'); inp.press('Enter'); pg.wait_for_timeout(300)
    f.check(js(pg, "return r.getElementById('fsc').classList.contains('err')"), 'step 1: an unknown roll shows an inline error')
    inp.fill(''); inp.press_sequentially('R-48330'); pg.wait_for_timeout(100)


def s1(pg, f):
    f.check('Wrong dye lot. This order needs DL-2611-B.' in ids(pg, 'ck'), 'step 1: red check, wrong dye lot, needs DL-2611-B')
    f.check(js(pg, "return r.querySelectorAll('.bar').length") == 0 and 'R-48330 rejected' in js(pg, "return r.getElementById('rb').innerText"), 'step 1: R-48330 rejected and no bar drawn')


def s2(pg, f):
    f.check('R-48214 accepted.' in ids(pg, 'ck') and js(pg, "return r.querySelectorAll('.chk.ok').length") == 1, 'step 2: green check for R-48214')
    f.check(js(pg, "return r.querySelectorAll('.bar').length") == 1 and '119 yd' in js(pg, "return r.querySelector('.rbh').innerText"), 'step 2: the bar for 119 yd appears')


def s3(pg, f):
    f.check(js(pg, "return [].map.call(r.querySelectorAll('.sg'),function(e){return e.textContent}).join(',')") == 'Lay 1,Lay 2,Lay 3', 'step 3: three lay segments')
    w = js(pg, "var b=r.getElementById('bar').getBoundingClientRect().width;return [].map.call(r.querySelectorAll('.sg'),function(e){return Math.round(e.style.width.replace('px','')*119/370)})")
    f.check(w == [36, 36, 36], 'step 3: each segment is 36 of 119 yd (%s)' % w)
    f.check(ids(pg, 'tp', 'u-pl', 'rbs') == '108 yd|108 yd|108 yd planned', 'step 3: 108 yd planned')


def bad_used(pg, f):
    inp = pg.locator('#cv #uin')
    inp.fill(''); inp.press_sequentially('130'); inp.press('Enter'); pg.wait_for_timeout(300)
    f.check(js(pg, "return r.getElementById('fus').classList.contains('err')"), 'step 4: more than the roll holds shows an inline error')
    f.check('Your turn4 of 4' in pill(pg), 'step 4: an invalid entry does not advance')
    inp.fill(''); inp.press_sequentially('109'); pg.wait_for_timeout(100)


def s4(pg, f):
    f.check(ids(pg, 'u-pl', 'u-ac', 'u-va', 'u-rm', 'u-tl', 'flg') == '108 yd|109 yd|+1 yd|10 yd|1.62 yd|Within tolerance', 'step 4: planned 108, actual 109, variance +1, remnant 10, tolerance 1.62, within tolerance')
    f.check(ids(pg, 'tu', 'tr') == '109 yd|10 yd', 'step 4: used 109, remnant 10 on the bar card')
    f.check('R-48214-R1' in ids(pg, 'rmn') and 'DL-2611-B' in ids(pg, 'rmn') and '10 yd' in ids(pg, 'rmn'), 'step 4: remnant label R-48214-R1, 10 yd, DL-2611-B')
    f.check(js(pg, "return r.querySelectorAll('.sg.ws').length") == 1 and js(pg, "return r.querySelector('.sg.rm').textContent") == '10', 'step 4: waste and remnant segments')


def over_tol(f):
    with sync_playwright() as p:
        b = testlib.browser(p)
        pg, errs = testlib.open_card(b, 3, 1300)
        pg.locator('#cv').scroll_into_view_if_needed()
        pg.locator('#cv .mtg [data-m="try"]').click(); pg.wait_for_timeout(300)
        pg.locator('#cv [data-v="R-48330"]').click()
        for _ in range(3):
            pg.wait_for_timeout(300); pg.locator('#cv .hint').first.click(); pg.wait_for_timeout(1700)
        inp = pg.locator('#cv #uin'); inp.fill('111'); inp.press('Enter'); pg.wait_for_timeout(500)
        f.check(ids(pg, 'u-va', 'flg', 'u-rm') == '+3 yd|Over tolerance|8 yd', 'typed 111 yd: variance +3, over tolerance, remnant 8 (Enter submits)')
        f.check(not errs, 'no page errors in the typed path')
        b.close()


PLAN = [('Scan the roll at the cut table', 'Wrong dye lot'),
        ('Right lot, the roll is accepted', '119 yd'),
        ('Confirm each lay', '108 yd planned'),
        ('Record what was actually used', 'Within tolerance')]

f = run_card(3, PLAN, ['108 yd', '109 yd', '+1 yd', '10 yd', 'R-48214-R1', 'Within tolerance'], start=start,
             extra={'before': {0: wrong_first, 3: bad_used}, 'after_step': {0: s1, 1: s2, 2: s3, 3: s4}})
over_tol(f)
finish(f)
