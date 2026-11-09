#!/usr/bin/env python3
"""Card 3 Quote to Configured Order: click through (both modes), the 3 x 3 x 3 pricing grid, numbers, layout, variety,
navigation and phone checks. Run: python3 tools/furniture-woodworking/test_card3.py"""
import itertools, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from furniture_tests import run_all, js, start_rule, testlib
from playwright.sync_api import sync_playwright
import card3

assert 56 * 12.50 == 700 and 18 * 52 == 936 and 700 + 54 + 42 + 936 == 1732 and round(1732 / 0.62) == 2794
assert 64 * 12.50 - 700 == 100 and 20 * 52 - 936 == 104 and 1732 + 204 == 1936 and round(1936 / 0.62) == 3123 and 3123 - 2794 == 329
assert card3.price(1, 1, 1) == (1732.0, 2794) and card3.price(1, 2, 1) == (1936.0, 3123)


def grid(f):
    """Every one of the 27 option combinations prices the same in the card as in the formula."""
    with sync_playwright() as p:
        b = testlib.browser(p)
        pg, errs = testlib.open_card(b, 3, 1300)
        bad = []
        for sp, w, fi in itertools.product(range(3), range(3), range(3)):
            c = js(pg, 'var c=r.host.sxCalc(%d,%d,%d);return [c.cost,c.price];' % (sp, w, fi))
            want = card3.price(sp, w, fi)
            if abs(c[0] - want[0]) > 0.001 or c[1] != want[1]:
                bad.append((sp, w, fi, c, want))
        f.check(not bad, 'pricing: all 27 combinations match cost / (1 - 0.38) %s' % bad[:2])
        b.close()


def start(pg, f):
    start_rule(pg, f, ['2,794', '1,732', ' bf', 'Lumber'])
    f.check('Pick a product to configure it.' in js(pg, "return r.getElementById('pg').innerText"), 'start: the prompt shows')


def price(pg, f):
    f.check(js(pg, "return r.getElementById('cost').textContent+'|'+r.getElementById('price').textContent") == '$1,732.00|$2,794', 'step 4: cost $1,732.00, price $2,794')


def delta(pg, f):
    got = js(pg, "return ['dbf','dlum','dh','dlab','dpr','ncost'].map(function(i){return r.getElementById(i).textContent}).join('|')")
    f.check(got == '+8 bf|+$100.00|+2 h|+$104.00|+$329|$1,936.00', 'step 7: lumber +8 bf +$100.00, labor +2 h +$104.00, price +$329, cost $1,936.00 (%s)' % got)
    f.check(js(pg, "return r.getElementById('mvbf').textContent") == '5664 bf', 'step 7: MO-3306 lumber 56 to 64 bf')


def end(pg, f):
    f.check(js(pg, "return r.getElementById('mo-bf').textContent") == '5664 bf', 'end: the production order BOM reads 64 bf, was 56')


PLAN = [('Start a quote from the piece the customer wants', 'Hollis residence'),
        ('Choose the options that change the build', 'White oak'),
        ('Every choice rewrites the BOM', '56 bf'),
        ('Cost and price follow the BOM, not a guess', '$2,794'),
        ('The quote becomes an order and a production order', 'WO-3306-4'),
        ('The customer adds length after approval', '84 in'),
        ('Only the difference moves, and the shop sees it', '+$329'),
        ('Quote, order and production stay in step', 'Rev B')]

f = run_all(3, PLAN, ['Rev B', '64 bf', 'Dec 10'], extra={'before': {0: start, 4: price}, 'after': end}, more=grid)
# the delta screen check runs on its own (it sits between the before hooks of steps 7 and 8)
with sync_playwright() as p:
    from furniture_tests import adv
    b = testlib.browser(p)
    pg, errs = testlib.open_card(b, 3, 1300)
    pg.locator('#cv').scroll_into_view_if_needed()
    pg.locator('#cv .mtg [data-m="try"]').click()
    for _ in range(7):
        pg.wait_for_timeout(1600); adv(pg)
    pg.wait_for_timeout(500)
    delta(pg, f)
    b.close()
print('\n%d failures' % len(f)); sys.exit(1 if f else 0)
