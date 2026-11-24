#!/usr/bin/env python3
"""Card 3 click through (both modes), numbers, layout, variety, timing, navigation and phone checks.
Run: python3 tools/distilleries/test_card3.py. The brief's case counts are asserted in numbers_check.py first."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numbers_check  # noqa: F401  (asserts 80 + 70 = 150 and the account split)
from distilleries_tests import run_all, js, testlib
from playwright.sync_api import sync_playwright


def start(pg, f):
    f.check(js(pg, "return r.querySelector('.fwin').getAttribute('data-scr')") == 'Lot search', 'start: the empty lot field')
    f.check(js(pg, "return r.querySelectorAll('.nd,.vr').length") == 0 and '150' not in testlib.win_text(pg), 'start: no trace before a lot is entered')
    f.check(js(pg, "return r.getElementById('iq').value") == '', 'start: the lot field is empty')


def bad(pg, f):
    start(pg, f)
    js(pg, "var e=r.getElementById('iq');e.value='ZZ-0000';e.dispatchEvent(new Event('input',{bubbles:true}))")
    pg.locator('#cv #iq').press('Enter'); pg.wait_for_timeout(300)
    f.check(js(pg, "return r.getElementById('fs').classList.contains('err')"), 'step 1: a lot that does not exist shows an inline error')
    js(pg, "var e=r.getElementById('iq');e.value='';e.dispatchEvent(new Event('input',{bubbles:true}))")


def fwd(pg, f):
    f.check(js(pg, "return [].map.call(r.querySelectorAll('.nd.ac em'),function(e){return e.textContent}).join(',')") == '60,12,8,30,40', 'step 1: accounts 60, 12, 8 (run A) and 30, 40 (run B)')
    f.check(js(pg, "return r.querySelector('#n-ra em').textContent+'|'+r.querySelector('#n-rb em').textContent+'|'+r.getElementById('f-cs').textContent") == '80 cases|70 cases|150', 'step 1: run A 80, run B 70, 150 cases')
    f.check(js(pg, "return r.querySelectorAll('#fl svg path').length") == 8, 'step 1: eight links drawn in the flow')


def recall(pg, f):
    f.check(js(pg, "return r.getElementById('r-tot').textContent+'|'+r.getElementById('r-a').textContent+'|'+r.getElementById('r-b').textContent") == '150|80|70', 'step 3: 150 cases, 80 from run A and 70 from run B')


def end(pg, f):
    f.check(js(pg, "return r.getElementById('h-cs').textContent") == '60', 'step 4: Harbor Wine and Spirits holds 60 cases')


def typing(f):
    with sync_playwright() as p:
        b = testlib.browser(p)
        pg, errs = testlib.open_card(b, 3, 1300, 604)
        t0 = pg.evaluate('performance.now()')
        pg.locator('#cv').scroll_into_view_if_needed()
        pg.wait_for_function("()=>{const r=document.querySelector('#cv [data-sxg-host]').shadowRoot,i=r.getElementById('iq');return i&&i.value.length>0}", timeout=5000)
        t1 = pg.evaluate('performance.now()') - t0
        f.check(t1 < 1700, 'watch: the lot starts typing %.0f ms after the card comes into view (about 1.3 s)' % t1)
        pg.wait_for_function("()=>{const r=document.querySelector('#cv [data-sxg-host]').shadowRoot;return r.querySelector('.fwin').getAttribute('data-scr')==='Forward trace'}", timeout=5000)
        t2 = pg.evaluate('performance.now()') - t0
        f.check(t2 < 4000, 'watch: the full trace is up %.0f ms after the card comes into view (under 4,000)' % t2)
        pg.close()
        for vw, cw, lab in ((1300, 604, 'desktop'), (390, 358, 'phone')):
            pg, errs = testlib.open_card(b, 3, vw, cw)
            pg.locator('#cv').scroll_into_view_if_needed()
            pg.locator('#cv .mtg [data-m="try"]').click(); pg.wait_for_timeout(500)
            pg.locator('#cv #iq').click(); pg.keyboard.type('bt-2209'); pg.keyboard.press('Enter'); pg.wait_for_timeout(700)
            f.check(js(pg, "return r.querySelector('.fwin').getAttribute('data-scr')") == 'Forward trace', '%s: typing bt-2209 and pressing Enter traces the lot' % lab)
            f.check(not errs, '%s typing: no page errors' % lab)
            pg.close()
        b.close()


PLAN = [('The full trace on one screen', '150'), ('Run B traced back to its source lots', 'CR-1180'),
        ('Every account that holds the lot', 'Ridgeway Beverage Supply'), ('One account, down to the order', 'SO-4471')]
f = run_all(3, PLAN, ['SO-4471', '60'], extra={'before': {0: bad, 1: fwd, 3: recall}, 'after': end}, drag=typing, start=start)
print('\n%d failures' % len(f)); sys.exit(1 if f else 0)
