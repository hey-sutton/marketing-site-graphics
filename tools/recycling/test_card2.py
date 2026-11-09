#!/usr/bin/env python3
"""Card 2 click through (both modes), numbers, layout, variety, navigation, phone and real drag checks. Run: python3 tools/recycling/test_card2.py
Rounding: whole pounds, yield to 0.1 percent."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from recycling_tests import run_all, js, testlib
from playwright.sync_api import sync_playwright

assert 26280 + 18720 == 45000 and 1350 + 32400 + 9000 + 2250 == 45000 and 32400 + 9000 == 41400 and 41400 / 45000 == 0.92


def start(pg, f):
    f.check(js(pg, "return r.querySelector('.fwin').getAttribute('data-scr')") == 'New job', 'start: a new job with nothing in it')
    f.check('45,000' not in js(pg, "return r.querySelector('.fwin').innerText"), 'start: no input total before the loads are dropped')


def sort(pg, f):
    f.check(js(pg, "return r.getElementById('is').value") == '1,350', 'step 3: pulled out prefilled')
    js(pg, "var e=r.getElementById('is');e.value='60,000';e.dispatchEvent(new Event('input',{bubbles:true}))")
    pg.locator('#cv .hint').first.click(); pg.wait_for_timeout(400)
    f.check(js(pg, "return r.getElementById('fs').classList.contains('err')"), 'step 3: more than the input shows an inline error')
    js(pg, "var e=r.getElementById('is');e.value='1,350';e.dispatchEvent(new Event('input',{bubbles:true}))")


def job(pg, f):
    f.check(js(pg, "return r.getElementById('inp').textContent") == '45,000 lb', 'step 1: input 45,000 lb')


def node(pg, f):
    f.check('Not weighed' in js(pg, "return r.getElementById('nd-nat').textContent"), 'step 4: outputs hidden until opened')


def rep(pg, f):
    f.check(js(pg, "return r.getElementById('nat').textContent+'|'+r.getElementById('mix').textContent") == '32,400 lb|9,000 lb', 'step 4: 32,400 and 9,000 lb')


def yld(pg, f):
    f.check(js(pg, "return r.getElementById('yl').textContent+'|'+r.getElementById('us').textContent+'|'+r.getElementById('ls').textContent") == '92.0%|41,400|2,250', 'step 5: 92.0%, 41,400 usable, 2,250 lost')


def drag(f):
    """A real pointer drag of the two loads onto the job, at desktop and phone width."""
    with sync_playwright() as p:
        b = testlib.browser(p)
        for vw, cw, lab in ((1300, 604, 'desktop'), (390, 358, 'phone')):
            pg, errs = testlib.open_card(b, 2, vw, cw)
            pg.locator('#cv').scroll_into_view_if_needed()
            pg.locator('#cv .mtg [data-m="try"]').click()
            pg.wait_for_timeout(1200)
            a = pg.locator('#cv #grp').bounding_box(); z = pg.locator('#cv #dz').bounding_box()
            pg.mouse.move(a['x'] + a['width'] / 2, a['y'] + 12); pg.mouse.down()
            for k in range(1, 11):
                pg.mouse.move(a['x'] + a['width'] / 2 + (z['x'] + z['width'] / 2 - a['x'] - a['width'] / 2) * k / 10, a['y'] + 12 + (z['y'] + z['height'] / 2 - a['y'] - 12) * k / 10)
                pg.wait_for_timeout(30)
            pg.mouse.up(); pg.wait_for_timeout(700)
            f.check(js(pg, "return r.querySelector('.fwin').getAttribute('data-scr')") == 'Job PJ-0318', '%s: a real drag drops the loads into the job' % lab)
            f.check('Your turn2 of 6' in testlib.pill(pg) or 'Your turn' in testlib.pill(pg), '%s: the walkthrough moves on after the drop' % lab)
            f.check(not errs, '%s drag: no page errors' % lab)
            pg.close()
        b.close()


PLAN = [('Pull mixed loads together into one processing job', '45,000 lb'),
        ('Move from the job to the sorting station', 'Nothing logged yet'),
        ('Log what you pull out as you sort it', '1,350 lb'),
        ('See where each pound of input went', '32,400 lb'),
        ('Yield and loss, in the open, for this job', '92.0%'),
        ('Completing books the outputs', 'RG-0318-A')]

f = run_all(2, PLAN, ['RG-0318-A', 'RG-0318-B', '32,400 lb', '9,000 lb', '2 output labels printed'], extra={'before': {0: start, 1: job, 2: sort, 3: node, 4: rep, 5: yld}}, drag=drag)
print('\n%d failures' % len(f)); sys.exit(1 if f else 0)
