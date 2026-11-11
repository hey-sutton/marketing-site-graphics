#!/usr/bin/env python3
"""Card 4 (measurement chart, NCR record and audit record): the brief's numbers in Python, then the click through.
Run: python3 tools/automotive/test_card4.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from auto_tests import run_card, finish, js, pill

# ---- the brief's numbers, derived independently of the card (microns) ----
RD = [12000, 11990, 12010, 12000, 12020, 11980, 12010, 12020, 12010, 12030, 12020, 12040, 12030, 12070, 12040, 12030, 12080, 12040, 12060, 12040]
inside = [v for v in RD if 11950 <= v <= 12050]
out = [v for v in RD if not 11950 <= v <= 12050]
assert len(RD) == 20 and len(inside) == 17 and out == [12070, 12080, 12060] and 17 + 3 == 20
assert 90 + 50 == 140


def ids(pg, *names):
    return js(pg, "return %r.map(function(i){var e=r.getElementById(i);return e?e.textContent:null}).join('|')" % list(names))


def start(pg, f, when='start'):
    t = js(pg, "return r.querySelector('.g4').innerText")
    f.check(js(pg, "return r.querySelectorAll('.row.sel,.pt,.fg,.ci').length") == 0, '%s: inspection list only, nothing selected, empty record panel' % when)
    f.check(ids(pg, 'acnt') == 'Not started' and 'NCR-0318' not in t and '140' not in t, '%s: nothing derived from the inspection shows' % when)


def s1(pg, f):
    f.check(js(pg, "return r.querySelectorAll('.pt').length") == 20 and ids(pg, 'acnt') == '1 of 5', 'step 1: 20 readings plotted, audit record 1 of 5')


def s2(pg, f):
    f.check(ids(pg, 'cin') == '17 in, 3 out', 'step 2: 17 in, 3 out')
    f.check(js(pg, "return [].map.call(r.querySelectorAll('.ol'),function(x){return x.textContent;}).join()") == '12.07,12.08,12.06', 'step 2: 12.07, 12.08 and 12.06 flagged')
    f.check(js(pg, "return [r.querySelectorAll('.pt.in').length,r.querySelectorAll('.pt.out').length].join()") == '17,3' and ids(pg, 'acnt') == '2 of 5', 'step 2: 17 points inside the band, 3 outside, 2 of 5')


def s3(pg, f):
    t = js(pg, "return r.getElementById('ncr').innerText")
    f.check(ids(pg, 'aff') == '140' and all(s in t for s in ('WO-7108', 'FGL-0913', 'Tool wear on spindle 3', 'R. Diaz')), 'step 3: NCR-0318 on WO-7108, FGL-0913, 140 pieces, cause and owner')
    f.check(ids(pg, 'acnt') == '3 of 5', 'step 3: audit record 3 of 5')


def bad_split(pg, f):
    pg.locator('#cv #irw').fill('100')
    pg.locator('#cv .hint').first.click(); pg.wait_for_timeout(300)
    f.check(js(pg, "return r.getElementById('frw').classList.contains('err')"), 'step 4: a split that does not cover 140 shows an error')
    f.check('Your turn4 of 5' in pill(pg), 'step 4: the bad split does not advance')
    pg.locator('#cv #irw').fill('90')


def s4(pg, f):
    f.check(ids(pg, 'dsum', 'acnt') == 'Rework 90 and scrap 50, 140 of 140|4 of 5', 'step 4: rework 90 and scrap 50, 140 of 140, 4 of 5')


def s5(pg, f):
    f.check(ids(pg, 'acnt') == '5 of 5 complete' and js(pg, "return r.querySelectorAll('.ci.ok').length") == 5, 'step 5: audit record 5 of 5 complete')


PLAN = [('Every in process inspection keeps its plan and readings', 'Bore diameter, WO-7108'),
        ('Readings outside the band are flagged as they come in', '17 in, 3 out'),
        ('The non conformance opens with the facts filled in', 'NCR-0318'),
        ('The disposition is split and has to cover every piece', '140 of 140'),
        ('The audit record assembles itself as the work is done', '5 of 5 complete')]

f = run_card(4, PLAN, ['17 in, 3 out', 'Rework 90 and scrap 50, 140 of 140', '5 of 5 complete'], start=start,
             extra={'before': {3: bad_split}, 'after_step': {0: s1, 1: s2, 2: s3, 3: s4, 4: s5}})
finish(f)
