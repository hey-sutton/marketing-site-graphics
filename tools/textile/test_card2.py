#!/usr/bin/env python3
"""Card 2 (stage board): the brief's numbers in Python, then the full click through in the browser.
Run: python3 tools/textile/test_card2.py"""
import os, sys
from decimal import Decimal, ROUND_HALF_UP
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from textile_tests import run_card, finish, js, pill, testlib
from playwright.sync_api import sync_playwright

# ---- the brief's numbers, derived independently of the card ----
assert 300 + 180 == 480 and 6 * 400 == 2400 and 6 * 392 == 2352
assert 2400 - 2352 == 48 and Decimal(48) / Decimal(2400) == Decimal('0.02')
assert 2352 - 12 == 2340 and 6 * 390 == 2340
yarn, dye, fin = Decimal('14.20') * 480, Decimal('0.85') * 2400, Decimal('0.30') * 2352
assert (yarn, dye, fin) == (Decimal('6816.00'), Decimal('2040.00'), Decimal('705.60'))
tot = yarn + dye + fin
assert tot == Decimal('9561.60')
q = lambda x: x.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
assert 2400 * 99 // 100 == 2376
assert q(tot / 2376) == Decimal('4.02') and q(tot / 2340) == Decimal('4.09')


def ids(pg, *names):
    return js(pg, "return %r.map(function(i){var e=r.getElementById(i);return e?e.textContent:null}).join('|')" % list(names))


def start(pg, f, when='start'):
    t = js(pg, "return r.querySelector('.g2').innerText")
    f.check('Select a work order' in t and 'WO-5520' in t and 'WO-5524' in t, '%s: prompt "Select a work order" and the list WO-5520, WO-5524' % when)
    f.check(js(pg, "return r.querySelectorAll('.wc').length") == 0, '%s: no work order cards in any column' % when)
    f.check(all(c in t for c in ('Yarn', 'Weaving', 'Dyeing', 'Finishing', 'Inspection')), '%s: the five column headers show' % when)
    f.check(not any(s in t for s in ('480 kg', '2,340', '$', 'yd out', 'kg issued')), '%s: nothing derived from a work order shows' % when)


def s1(pg, f):
    f.check(js(pg, "return r.querySelectorAll('.wc:not(.wait)').length") == 3, 'step 1: cards in Yarn, Weaving and Dyeing')
    t = js(pg, "return r.getElementById('brd').innerText.replace(/\\s+/g,' ')")
    f.check('480 kg issued' in t and 'Warp 300 kg' in t and 'Weft 180 kg' in t, 'step 1: yarn 480 kg, warp 300, weft 180')
    f.check('2,400 yd greige' in t and '6 rolls of 400 yd' in t and '2,400 yd out' in t, 'step 1: 2,400 yd greige in 6 rolls of 400, 2,400 yd out')
    f.check(ids(pg, 'cy', 'cd') == '$6,816.00|$2,040.00', 'step 1: yarn $6,816.00 and dyeing $2,040.00')


def s2(pg, f):
    f.check(ids(pg, 'cn1', 'cn2', 'cn3') == '0 rolls, 0 yd|6 rolls, 2,400 yd out|0 rolls, 0 yd', 'step 2: Weaving 0, Dyeing 2,400 yd out, Finishing 0 (%s)' % ids(pg, 'cn1', 'cn2', 'cn3'))
    v = js(pg, "return r.getElementById('vp').innerText.replace(/\\s+/g,' ')")
    f.check('Bayside Dye Works' in v and '2,400 yd, 6 rolls' in v and 'Not yet' in v, 'step 2: vendor record, 2,400 yd in 6 rolls, not returned')


def s3(pg, f):
    f.check(ids(pg, 'var', 'vret', 'vvar') == '−48 yd, 2.0%|2,352 yd, 6 rolls|−48 yd, 2.0%', 'step 3: 2,352 yd back, variance minus 48 yd, 2.0%')
    f.check(js(pg, "return r.querySelectorAll('#col2 .rl.d').length") == 6 and '392' in ids(pg, 'col2'), 'step 3: 6 dyed rolls of 392')
    f.check(ids(pg, 'cn2', 'cn3') == '0 rolls out|6 rolls, 2,352 yd', 'step 3: 0 out at the vendor, finishing 2,352 yd')
    f.check(ids(pg, 'cf', 'ctot', 'pbom') == '$705.60|$9,561.60|$4.02 per yd', 'step 3: finishing $705.60, total $9,561.60, BOM estimate $4.02 per yd')


def bad_measure(pg, f):
    inp = pg.locator('#cv #myd')
    inp.fill(''); inp.press_sequentially('2500'); inp.press('Enter'); pg.wait_for_timeout(300)
    f.check(js(pg, "return r.getElementById('fmy').classList.contains('err')"), 'step 4: more yards than received shows an inline error')
    f.check('Your turn4 of 4' in pill(pg), 'step 4: an invalid measure does not advance')
    inp.fill(''); inp.press_sequentially('2,340'); pg.wait_for_timeout(100)


def s4(pg, f):
    f.check(ids(pg, 'iq', 'fls') == '2,340 yd measured|12 yd lost at finishing', 'step 4: 2,340 yd measured, 12 yd lost')
    f.check(ids(pg, 'pact', 'pem') == '$4.09 per yd|2,340 yd, replaces the estimate', 'step 4: $4.09 per yd from the measured yield')
    f.check(js(pg, "return [].map.call(r.querySelectorAll('#col4 .rl'),function(e){return e.textContent}).join(',')") == '390,390,390,390,390,390', 'step 4: six rolls of 390 yd at inspection')
    f.check(ids(pg, 'stg', 'sin', 'sout') == '5 of 5 stages complete|480 kg|2,340 yd', 'step 4: all stages complete, 480 kg in, 2,340 yd out')


def other_measure(f):
    with sync_playwright() as p:
        b = testlib.browser(p)
        pg, errs = testlib.open_card(b, 2, 1300)
        pg.locator('#cv').scroll_into_view_if_needed()
        pg.locator('#cv .mtg [data-m="try"]').click(); pg.wait_for_timeout(300)
        for _ in range(3):
            pg.wait_for_timeout(300); pg.locator('#cv .hint').first.click(); pg.wait_for_timeout(1700)
        inp = pg.locator('#cv #myd'); inp.fill('2352'); inp.press('Enter'); pg.wait_for_timeout(500)
        f.check(ids(pg, 'pact') == '$4.07 per yd' and ids(pg, 'fls') == '0 yd lost at finishing', 'typed 2,352 yd: $4.07 per yd, 0 yd lost (Enter submits)')
        f.check(not errs, 'no page errors in the typed path')
        b.close()


PLAN = [('Pick a work order', '2,400 yd out'),
        ('Work in process between stages', 'Bayside Dye Works'),
        ('Steps at an outside processor sit in the routing', '2,352 yd back'),
        ('Measured yield replaces the BOM estimate', '$4.09 per yd')]

assert q(tot / 2352) == Decimal('4.07')
f = run_card(2, PLAN, ['480 kg', '2,340 yd', '$9,561.60', '$4.09 per yd', '5 of 5 stages complete'], start=start,
             extra={'before': {3: bad_measure}, 'after_step': {0: s1, 1: s2, 2: s3, 3: s4}})
other_measure(f)
finish(f)
