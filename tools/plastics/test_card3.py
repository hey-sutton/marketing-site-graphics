#!/usr/bin/env python3
"""Card 3 click through (both modes), numbers, layout and text checks. Run: python3 tools/plastics/test_card3.py
Rounding: caps whole, compound to 0.1 lb, regrind to 0.01 lb."""
import os, sys
from decimal import Decimal as D
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from plastics_tests import run_card, js

assert 18500 + 700 == 19200 and 20200 + 600 == 20800 and 19200 + 20800 == 40000
assert 18500 + 20200 == 38700 and 700 + 600 == 1300 and 38700 + 1300 == 40000
assert 40000 * D('0.0275') == D('1100.0') and 1300 * D('0.0275') == D('35.75') and D('1112.5') - D('1100.0') == D('12.5')


def start(pg, f):
    f.check(js(pg, "return [r.getElementById('iq').value,r.getElementById('ip').value,r.getElementById('im').value].join('|')") == '40,000|Press 4|M-0412', 'start: run, press and mold prefilled')
    f.check(js(pg, "return !!r.getElementById('me')"), 'start: expected vs actual empty until its step')
    f.check(not js(pg, "return !!r.getElementById('res')"), 'start: no compound reserved before release')
    js(pg, "var e=r.getElementById('im');e.value='mold';e.dispatchEvent(new Event('input',{bubbles:true}))")
    pg.locator('#cv .hint').first.click(); pg.wait_for_timeout(400)
    f.check(js(pg, "return r.getElementById('fm').classList.contains('err')"), 'step 1: a bad mold shows an inline error')
    js(pg, "var e=r.getElementById('im');e.value='M-0412';e.dispatchEvent(new Event('input',{bubbles:true}))")


def rel(pg, f):
    f.check('1,100.0 lb' in js(pg, "return r.getElementById('res').textContent"), 'step 1: 1,100.0 lb reserved')
    f.check(js(pg, "return r.getElementById('ig').value+'|'+r.getElementById('is').value") == '18,500|700', 'step 2: shift 1 prefilled')
    js(pg, "var e=r.getElementById('ig');e.value='lots';e.dispatchEvent(new Event('input',{bubbles:true}))")
    pg.locator('#cv .hint').first.click(); pg.wait_for_timeout(400)
    f.check(js(pg, "return r.getElementById('fg').classList.contains('err')"), 'step 2: a bad count shows an inline error')
    js(pg, "var e=r.getElementById('ig');e.value='18,500';e.dispatchEvent(new Event('input',{bubbles:true}))")


def s1(pg, f):
    f.check(js(pg, "return r.getElementById('prog').textContent") == '19,200 of 40,000', 'step 2: 19,200 of 40,000')
    f.check(js(pg, "return r.getElementById('ig').value+'|'+r.getElementById('is').value") == '20,200|600', 'step 3: shift 2 prefilled')


def s2(pg, f):
    f.check(js(pg, "return r.getElementById('prog').textContent") == '40,000 of 40,000', 'step 3: 40,000 of 40,000')
    f.check(js(pg, "return !!r.getElementById('me')"), 'step 3: comparison still empty before its step')


def cmp(pg, f):
    f.check(js(pg, "return ['ag','as','ec','ac','ov'].map(function(k){return r.getElementById(k).textContent}).join('|')") == '38,700|1,300|1,100.0|1,112.5|12.5 lb', 'step 4: 38,700 good, 1,300 scrap, 1,112.5 against 1,100.0, over 12.5')


def end(pg, f):
    f.check('38,700' in js(pg, "return r.getElementById('fl').textContent") and '35.75 lb' in js(pg, "return r.getElementById('rg').textContent"), 'step 5: FL-7720 38,700 caps, 35.75 lb to regrind')


PLAN = [('Each run carries its steps, its press, its mold', '1,100.0 lb'),
        ('The operator logs output at the press', '19,200 of 40,000'),
        ('A second shift adds to the same run', '38,700 good'),
        ('Compare what you expected with what the run really made', '1,112.5'),
        ('Completing a run books the finished lot', 'FL-7720')]

f = run_card(3, PLAN, ['FL-7720, 38,700 caps to stock', '35.75 lb to regrind', '1,112.5 lb compound deducted'], extra={'before': {0: start, 1: rel, 2: s1, 3: s2, 4: cmp}, 'after': end})
print('\n%d failures' % len(f)); sys.exit(1 if f else 0)
