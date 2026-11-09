#!/usr/bin/env python3
"""Card 3 click through (both modes), numbers, layout, variety, navigation, phone and real drag checks. Run: python3 tools/recycling/test_card3.py
Rounding: whole pounds."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from recycling_tests import run_all, js, testlib
from playwright.sync_api import sync_playwright

assert 52400 + 61300 + 28900 + 18200 + 9800 == 170600 and 11500 + 8000 + 6100 + 3300 == 28900 and 6100 + 3300 == 9400
assert 36800 - 6100 == 30700 and 14200 + 6100 == 20300 and 4200 + 3100 + 2100 == 9400
for g in ([30200, 14100, 6000, 2100], [38400, 16900, 4500, 1500], [9800, 5600, 2000, 800], [6300, 2700, 600, 200]):
    pass
assert [sum(g) for g in ([30200, 14100, 6000, 2100], [38400, 16900, 4500, 1500], [9800, 5600, 2000, 800], [6300, 2700, 600, 200])] == [52400, 61300, 18200, 9800]


def start(pg, f):
    f.check(js(pg, "return r.querySelector('.fwin').getAttribute('data-scr')") == 'Inventory by grade', 'start: stock by grade')
    f.check(js(pg, "return r.getElementById('tot').textContent") == '170,600', 'start: 170,600 lb across five grades')


def chip(pg, f):
    f.check(js(pg, "return r.getElementById('agt').textContent") == '28,900', 'step 2: all lots 28,900 lb before the filter')


def flt(pg, f):
    f.check(js(pg, "return r.getElementById('agt').textContent+'|'+r.querySelectorAll('.ym .bn2').length") == '9,400|2', 'step 2: 9,400 lb in two bins')


def bn(pg, f):
    f.check(js(pg, "return r.getElementById('bq').textContent") == '36,800', 'step 3: Y1-04 holds 36,800 of 40,000')


def part(pg, f):
    f.check(js(pg, "return r.getElementById('har').textContent") == '4,200', 'step 4: Harlan Plastics 4,200 lb older than 60 days')


def end(pg, f):
    f.check(js(pg, "return r.getElementById('mv-Y1-04').textContent+'|'+r.getElementById('mv-Y2-11').textContent") == '30,700|20,300', 'step 5: Y1-04 30,700 and Y2-11 20,300')


def drag(f):
    with sync_playwright() as p:
        b = testlib.browser(p)
        for vw, cw, lab in ((1300, 604, 'desktop'), (390, 358, 'phone')):
            pg, errs = testlib.open_card(b, 3, vw, cw)
            pg.locator('#cv').scroll_into_view_if_needed()
            pg.locator('#cv .mtg [data-m="try"]').click()
            pg.wait_for_timeout(600)
            pg.locator('#cv #nx').click(); pg.wait_for_timeout(300)
            for _ in range(3):
                pg.locator('#cv #nx').click(); pg.wait_for_timeout(300)
            pg.wait_for_timeout(900)
            a = pg.locator('#cv #tile').bounding_box(); z = pg.locator('#cv #dz').bounding_box()
            pg.mouse.move(a['x'] + 20, a['y'] + 12); pg.mouse.down()
            for k in range(1, 11):
                pg.mouse.move(a['x'] + 20 + (z['x'] + z['width'] / 2 - a['x'] - 20) * k / 10, a['y'] + 12 + (z['y'] + z['height'] / 2 - a['y'] - 12) * k / 10)
                pg.wait_for_timeout(30)
            pg.mouse.up(); pg.wait_for_timeout(700)
            f.check(js(pg, "return r.querySelector('.fwin').getAttribute('data-scr')") == 'Move stock', '%s: a real drag moves the stock' % lab)
            f.check('Done' in testlib.pill(pg), '%s: the walkthrough ends on Done after the drop' % lab)
            f.check(not errs, '%s drag: no page errors' % lab)
            pg.close()
        b.close()


PLAN = [('See which grade has been sitting', '28,900'),
        ('Filter to material that has sat too long', '9,400'),
        ('See a bin nearing capacity', '36,800'),
        ("Open a supplier's aging report", '4,200'),
        ('Move aged stock to another bin', 'MV-0442')]

f = run_all(3, PLAN, ['30,700', '20,300', 'MV-0442'], extra={'before': {0: start, 1: chip, 2: flt, 3: bn, 4: part}, 'after': end}, drag=drag)
print('\n%d failures' % len(f)); sys.exit(1 if f else 0)
