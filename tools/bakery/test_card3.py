#!/usr/bin/env python3
"""Card 3 (allergen grid, batches, recipient cards, hold panel): the brief's numbers in Python, then the full click through.
Run: python3 tools/bakery/test_card3.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bk_tests import run_card, finish, js, pill, testlib, ids, enter_submits

# ---- the brief's numbers, derived independently of the card ----
LOT_KG, B4411, B4420 = 100, 30, 20
assert B4411 + B4420 == 50 and LOT_KG - 50 == 50
assert 2400 / 12 == 200 and 1800 / 12 == 150 and 200 + 150 == 350
SHIP = [('SH-9301', 10, 'B-4411', 120, 'Eastside Cafe Group'), ('SH-9304', 11, 'B-4411', 60, 'Lakeview Markets'), ('SH-9312', 13, 'B-4420', 100, 'Eastside Cafe Group')]
BDATE = {'B-4411': 9, 'B-4420': 12}
assert 120 + 60 + 100 == sum(s[3] for s in SHIP) == 280 and 350 - 280 == 70
assert 200 - 120 - 60 == 20 and 150 - 100 == 50 and 20 + 50 == 70
assert 120 + 100 == 220 and 220 + 60 == 280
assert all(d >= BDATE[b] for _, d, b, _, _ in SHIP), 'a shipment is dated before its batch'
GRID = {'Almond Croissant': 'WMET', 'Almond Cookie': 'WET', 'Plain Baguette': 'W', 'Brioche Bun': 'WME'}
USES = {'Almond Croissant', 'Almond Cookie'}
assert all('T' in GRID[p] for p in USES)


def start(pg, f, when='start'):
    t = js(pg, "return r.querySelector('.k3').innerText")
    f.check(js(pg, "return r.getElementById('kli').value") == '', '%s: the lot input is empty' % when)
    f.check(js(pg, "return [].every.call(r.querySelectorAll('.kgr i'),function(i){return !i.className&&!i.textContent.trim()})") and js(pg, "return r.querySelectorAll('.kgr i').length") == 16, '%s: grid shows labels only, all 16 cells neutral' % when)
    f.check(not any(s in t for s in ('Harbor Mill', 'B-4411', 'SH-93', 'Eastside', '100.000', 'Contains')), '%s: nothing derived from AF-1042 shows' % when)


def bad_then_type(pg, f):
    inp = pg.locator('#cv #kli')
    inp.click(); inp.press_sequentially('AF-9999'); inp.press('Enter'); pg.wait_for_timeout(300)
    f.check(js(pg, "return r.getElementById('kfl').classList.contains('err')"), 'step 1: an unknown lot shows an inline error')
    f.check('Your turn1 of 5' in pill(pg), 'step 1: an unknown lot does not advance')
    f.check(js(pg, "return r.querySelector('.k3h').innerText.indexOf('Harbor')<0"), 'step 1: nothing from AF-1042 before a valid search')
    inp.fill(''); inp.press_sequentially('af-1042')


def s1(pg, f):
    t = js(pg, "return r.getElementById('k3h').innerText")
    f.check(all(s in t for s in ('AF-1042', 'Almond flour', '100.000 kg', 'Harbor Mill Supply', 'Received November 2', 'Certificate attached')), 'step 1: lot header AF-1042, almond flour, 100.000 kg, Harbor Mill Supply, November 2, certificate')
    f.check(js(pg, "return r.querySelectorAll('.klit,.kyes').length") == 0, 'step 1: the grid is still neutral')


def s2(pg, f):
    lit = js(pg, "return [].map.call(r.querySelectorAll('.klit'),function(i){return i.id}).sort().join(',')")
    f.check(lit == 'kx0T,kx1T', 'step 2: only Tree nut on Almond Croissant and Almond Cookie lights (%s)' % lit)
    f.check(js(pg, "return r.querySelectorAll('.kgr span.kp.kdim').length") == 2 and js(pg, "return [].map.call(r.querySelectorAll('.kgr span.kp.kdim'),function(e){return e.textContent}).join(',')") == 'Plain Baguette,Brioche Bun', 'step 2: Plain Baguette and Brioche Bun are dimmed')
    for i, (p, al) in enumerate(GRID.items()):
        got = ''.join(a for a in 'WMET' if js(pg, "return r.getElementById('kx%d%s').textContent!==''" % (i, a)))
        f.check(got == al, 'step 2: %s shows %s' % (p, al))


def s3(pg, f):
    f.check(ids(pg, 'kbg0', 'kbg1') == '30.000 kg of AF-1042|20.000 kg of AF-1042', 'step 3: B-4411 30.000 kg, B-4420 20.000 kg')
    f.check(ids(pg, 'kbf') == '50.000 kg used, 50.000 kg on hand', 'step 3: 50.000 kg used, 50.000 kg on hand')
    t = js(pg, "return r.getElementById('kbs').innerText")
    f.check('2,400 pieces, 200 cases of 12' in t and '1,800 pieces, 150 cases of 12' in t, 'step 3: 200 and 150 cases of 12')


def s4(pg, f):
    t = js(pg, "return r.getElementById('krc').innerText")
    f.check(ids(pg, 'kct0', 'kct1') == '220 cases|60 cases' and t.index('Eastside Cafe Group') < t.index('Lakeview Markets'), 'step 4: Eastside Cafe Group 220 cases, Lakeview Markets 60 cases')
    f.check(all(s in t for s in ('SH-9301', 'SH-9312', 'SH-9304')), 'step 4: SH-9301, SH-9312 and SH-9304')
    f.check(ids(pg, 'ksum', 'kon') == '280 shipped, 70 on site|70 cases', 'step 4: 280 shipped, 70 on site')
    f.check(ids(pg, 'kbc0', 'kbc1') == '20 on site|50 on site', 'step 4: 20 of B-4411 and 50 of B-4420 on site')


def s5(pg, f):
    f.check(ids(pg, 'khq0', 'khq1', 'khg', 'kht') == '20 cases|50 cases|50.000 kg|70 cases', 'step 5: hold 20 + 50 cases and 50.000 kg')
    f.check(ids(pg, 'kbc0', 'kbc1', 'klh') == 'Held 20 cases|Held 50 cases|50.000 kg held', 'step 5: batches and the lot change to Held')


PLAN = [('Search the flagged lot', 'Harbor Mill Supply'),
        ('See which products carry the allergen', 'AF-1042'),
        ('Find every batch that used the lot', '50.000 kg used'),
        ('See who received them', '280 shipped, 70 on site'),
        ('Hold what is still on site', '70 cases')]

f = run_card(3, PLAN, ['70 cases', '50.000 kg held', 'Held 20 cases', 'Held 50 cases'], start=start,
             extra={'before': {0: bad_then_type}, 'after_step': {0: s1, 1: s2, 2: s3, 3: s4, 4: s5}})
enter_submits(f, 3, '#kli', 'AF-1042', 'Your turn2 of 5')
finish(f)
