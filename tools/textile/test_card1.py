#!/usr/bin/env python3
"""Card 1 (roll table and record panel): the brief's numbers in Python, then the full click through in the browser.
Run: python3 tools/textile/test_card1.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from textile_tests import run_card, finish, js, pill, testlib, data as D
from playwright.sync_api import sync_playwright

# ---- the brief's numbers, derived independently of the card ----
R = {'R-48211': 120, 'R-48212': 118, 'R-48213': 122, 'R-48214': 119, 'R-48215': 121}
assert sum(R.values()) == 600 and 600 + 84 + 84 == 768
assert R['R-48211'] + R['R-48212'] + R['R-48213'] == 360
assert 60 + 61 == R['R-48215'] == 121
assert R['R-48214'] + R['R-48215'] == 240 == 600 - 360
assert 360 + 744 + 480 == 1584 and 1584 + 768 == 2352


def ids(pg, *names):
    return js(pg, "return %r.map(function(i){var e=r.getElementById(i);return e?e.textContent:null}).join('|')" % list(names))


def start(pg, f, when='start'):
    t = js(pg, "return r.querySelector('.g1').innerText")
    f.check(js(pg, "return r.getElementById('rin').value") == '', '%s: the scan field is empty' % when)
    f.check('Scan or type a roll ID' in t, '%s: prompt "Scan or type a roll ID"' % when)
    f.check(js(pg, "return r.querySelectorAll('.tb .row,.tl,.lab').length") == 0, '%s: no roll rows, no label and no totals' % when)
    f.check(not any(s in t for s in ('DL-2611', '768', '600 yd', '240', 'R-48214')), '%s: nothing derived from a scan shows' % when)


def bad_then_type(pg, f):
    inp = pg.locator('#cv #rin')
    inp.click(); inp.press_sequentially('R-99999'); inp.press('Enter'); pg.wait_for_timeout(300)
    f.check(js(pg, "return r.getElementById('frin').classList.contains('err')"), 'step 1: an unknown roll shows an inline error')
    f.check('Your turn1 of 4' in pill(pg), 'step 1: an unknown roll does not advance')
    inp.fill(''); inp.press_sequentially('r-48214'); pg.wait_for_timeout(100)
    f.check(js(pg, "return r.getElementById('rin').value") == 'r-48214', 'step 1: typing works in the scan field')


def s1(pg, f):
    rec = js(pg, "return r.getElementById('rec').innerText.replace(/\\s+/g,' ')")
    f.check(ids(pg, 'lid') == 'R-48214', 'step 1: the label shows R-48214')
    f.check(all(x in rec for x in ('DL-2611-B', 'NVY-204', '58 in', '119 yd', 'C-07', 'Available')), 'step 1: record DL-2611-B, NVY-204, 58 in, 119 yd, C-07, Available (%s)' % rec)
    f.check(js(pg, "return r.querySelectorAll('.lab .bcd rect').length") > 20, 'step 1: the label has a barcode')
    f.check(js(pg, "return r.querySelectorAll('.tb .row:not(.h)').length") == 8, 'step 1: eight rolls listed')
    f.check(ids(pg, 't-stk') == '768 yd' and '768 yd in 7 rolls, 600 available, 168 held' in ids(pg, 'tf'), 'step 1: lot DL-2611-B 768 yd in 7 rolls, 600 available, 168 held')


def s2(pg, f):
    f.check(ids(pg, 'rqty', 'rst', 't-res', 't-av') == '360 of 360 yd|Reserved|360 of 360 yd|240 yd', 'step 2: 360 of 360 reserved, 240 yd still available')
    pk = js(pg, "return [].map.call(r.querySelectorAll('.pk'),function(e){return e.innerText.replace(/\\s+/g,' ')}).join('|')")
    f.check(pk == 'R-48211 DL-2611-B 120 yd|R-48212 DL-2611-B 118 yd|R-48213 DL-2611-B 122 yd', 'step 2: picks R-48211 120, R-48212 118, R-48213 122 (%s)' % pk)
    f.check(js(pg, "return r.querySelector('.pr .bar i').style.width") == '100%', 'step 2: the progress bar is full')


def s3(pg, f):
    b = ids(pg, 'blk')
    f.check('Dye lot DL-2611-C does not match DL-2611-B on this order' in b and 'Override with reason' in b, 'step 3: blocked message and the override button')
    f.check(ids(pg, 'lid') == 'R-48330' and 'DL-2611-C' in js(pg, "return r.querySelector('.lab').innerText"), 'step 3: the label shows R-48330 and its lot chip DL-2611-C')
    f.check('Blocked' in ids(pg, 'rw-R-48330'), 'step 3: R-48330 is blocked in the table')
    f.check(ids(pg, 'rqty') == '360 of 360 yd', 'step 3: the reservation stays at 360')
    pg.locator('#cv #ovr').click(); pg.wait_for_timeout(200)
    f.check('A reason and a supervisor sign off are required.' in ids(pg, 'blk'), 'step 3: Override asks for a reason')


def s4(pg, f):
    a, b = ids(pg, 'rw-R-48215-A'), ids(pg, 'rw-R-48215-B')
    f.check('60 yd' in a and 'DL-2611-B' in a and 'parent R-48215' in a, 'step 4: R-48215-A 60 yd, DL-2611-B, parent R-48215')
    f.check('61 yd' in b and 'DL-2611-B' in b and 'parent R-48215' in b, 'step 4: R-48215-B 61 yd, DL-2611-B, parent R-48215')
    f.check(js(pg, "return !r.getElementById('rw-R-48215')"), 'step 4: R-48215 is replaced by its two parts')
    f.check(ids(pg, 'lid', 'lpar') == 'R-48215-A|Split from R-48215, lot kept', 'step 4: label R-48215-A, split from R-48215')
    f.check(ids(pg, 't-res', 't-av') == '360 of 360 yd|240 yd', 'step 4: summary 360 of 360 reserved, 240 yd available')
    f.check('R-48214 119 + R-48215 121' in js(pg, "return r.getElementById('sm').innerText"), 'step 4: 240 is R-48214 119 + R-48215 121')
    f.check('R-48215 split into R-48215-A 60 yd and R-48215-B 61 yd, both DL-2611-B.' in ids(pg, 'sln'), 'step 4: strip says R-48215 split into A and B')


def enter_and_samples(f):
    with sync_playwright() as p:
        b = testlib.browser(p)
        pg, errs = testlib.open_card(b, 1, 1300)
        pg.locator('#cv').scroll_into_view_if_needed()
        pg.locator('#cv .mtg [data-m="try"]').click(); pg.wait_for_timeout(400)
        inp = pg.locator('#cv #rin'); inp.click(); inp.press_sequentially('R-48214'); inp.press('Enter'); pg.wait_for_timeout(500)
        f.check('Your turn2 of 4' in pill(pg) and ids(pg, 'lid') == 'R-48214', 'Enter submits the typed roll')
        pg.close()
        for v, lot in (('R-48211', 'DL-2611-B'), ('R-48330', 'DL-2611-C')):
            pg, errs = testlib.open_card(b, 1, 1300)
            pg.locator('#cv').scroll_into_view_if_needed()
            pg.locator('#cv .mtg [data-m="try"]').click(); pg.wait_for_timeout(400)
            pg.locator('#cv [data-v="%s"]' % v).click(); pg.wait_for_timeout(100)
            f.check(js(pg, "return r.getElementById('rin').value") == v, 'the sample button fills %s' % v)
            pg.locator('#cv #scn').click(); pg.wait_for_timeout(400)
            f.check(ids(pg, 'lid') == v and lot in js(pg, "return r.getElementById('rec').innerText"), 'scanning sample %s shows its label with %s' % (v, lot))
            pg.close()
        b.close()


PLAN = [('Scan a roll label', 'DL-2611-B'),
        ('Reserve rolls from one dye lot', '360 of 360 yd'),
        ('A pick that mixes lots is blocked', 'does not match DL-2611-B on this order'),
        ('Split a roll and keep its lot', 'R-48215-B')]

f = run_card(1, PLAN, ['360 of 360 yd', '240 yd', 'R-48215-A', 'R-48215-B', 'parent R-48215'], start=start,
             extra={'before': {0: bad_then_type}, 'after_step': {0: s1, 1: s2, 2: s3, 3: s4}})
enter_and_samples(f)
finish(f)
