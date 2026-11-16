#!/usr/bin/env python3
"""Card 4 (stage board): the brief's numbers in Python, then the click through. Run: python3 tools/frozen-food/test_card4.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ff_tests import run_card, finish, js, ids, pill

IN, EXP, ACT = 400, [392, 388, 386, 385, 384], [392, 386, 382, 380, 378]
loss = [(IN if i == 0 else ACT[i - 1]) - ACT[i] for i in range(5)]
inputs = [IN] + ACT[:4]
assert inputs == [400, 392, 386, 382, 380]                    # stage inputs chain
assert loss == [8, 6, 4, 2, 2] and IN - sum(loss) == 378 == ACT[-1]
assert IN - ACT[-1] == 22 and IN - EXP[-1] == 16 and EXP[-1] == IN * 96 // 100
assert all(a <= e for a, e in zip(ACT, EXP))                  # each actual at most its expected
assert ACT[-1] - EXP[-1] == -6                                # pack variance
assert 378 / 6 == 63 and 384 / 6 == 64
assert 160 - 150 == 10 and 140 - 120 == 20                    # chicken short, broccoli spare


def start(pg, f, when='start'):
    t = js(pg, "return r.querySelector('.g4').innerText")
    f.check(all(s in t for s in ('Prep', 'Cook', 'Assemble', 'Freeze', 'Pack')) and js(pg, "return r.querySelectorAll('.bx b,.hit').length") == 0, '%s: five stage names, no run selected' % when)
    f.check(js(pg, "return r.getElementById('moi').value") == '' and ids(pg, 'mst') == 'No order open', '%s: empty Manufacturing order input, no order open' % when)
    f.check('392' not in t and '63' not in t, '%s: no output before a run is selected' % when)


def bad_then_type(pg, f):
    inp = pg.locator('#cv #moi')
    inp.click(); inp.press_sequentially('MO-0000'); inp.press('Enter'); pg.wait_for_timeout(300)
    f.check(js(pg, "return r.getElementById('fmo').classList.contains('err')") and 'Your turn1 of 5' in pill(pg), 'step 1: an unknown order shows an error and does not advance')
    inp.fill(''); inp.press_sequentially('mo-6105')
    f.check(js(pg, "return r.getElementById('moi').value") == 'mo-6105', 'step 1: typing works in the input')


def s1(pg, f):
    f.check(ids(pg, 'mst') == 'MO-6105 open' and js(pg, "return r.querySelectorAll('.hit').length") == 5, 'step 1: MO-6105 open, five stage columns')


def s2(pg, f):
    f.check(ids(pg, 'e0', 'e1', 'e2', 'e3', 'e4') == '392|388|386|385|384', 'step 2: expected 392, 388, 386, 385, 384')


def s3(pg, f):
    f.check(ids(pg, 'a0', 'a1', 'a2', 'a3', 'a4') == '392|386|382|380|378', 'step 3: actual 392, 386, 382, 380, 378')
    f.check(ids(pg, 'l0', 'l1', 'l2', 'l3', 'l4') == '8 lb lost|6 lb lost|4 lb lost|2 lb lost|2 lb lost', 'step 3: loss at each stage')
    f.check(ids(pg, 'tls', 'vpk') == 'Total loss 22 lb against 16 lb expected.|Pack 6 lb under', 'step 3: 22 lb lost against 16, pack 6 under')


def s4(pg, f):
    f.check(ids(pg, 'fgc') == '63' and 'Expected 64, 1 case short' in ids(pg, 'fgg') and 'Holding freezer A' in js(pg, "return r.getElementById('fg').innerText"), 'step 4: 63 cases to Holding freezer A, 1 short of 64')


def s5(pg, f):
    f.check(ids(pg, 'msh', 'ms0', 'ms1') == '1 short|10 short|20 spare', 'step 5: chicken 10 lb short, broccoli covered with 20 lb spare')


def stage(pg, f, i, want):
    pg.locator('#cv .hit[data-i="%d"]' % i).click(); pg.wait_for_timeout(250)
    got = ids(pg, 'sdt') or ''
    f.check(want in got, 'try: click a stage shows its input, output and loss (%s)' % got)


def po(pg, f):
    stage(pg, f, 1, 'Cook: 392 lb in, 386 lb out, 6 lb lost')
    stage(pg, f, 4, 'Pack: 380 lb in, 378 lb out, 2 lb lost')
    pg.locator('#cv #cpo').click(); pg.wait_for_timeout(400)
    f.check('10 lb from Harvest Ridge Farms' in (ids(pg, 'pod') or '') and ids(pg, 'mst') == 'Draft purchase order created', 'Create purchase order adds a draft for 10 lb, status reads Draft purchase order created')
    f.check(pg.locator('#cv #cpo').count() == 0, 'Create purchase order can be pressed once')
    # Replay resets, then Enter in the input submits
    pg.locator('#cv .tbar .rp').click(); pg.wait_for_timeout(500)
    f.check(js(pg, "return r.querySelectorAll('#pod,.bx b').length") == 0 and ids(pg, 'mst') == 'No order open', 'Replay resets the draft PO and the bars')
    inp = pg.locator('#cv #moi'); inp.click(); inp.press_sequentially('MO-6105'); inp.press('Enter'); pg.wait_for_timeout(1700)
    f.check('Your turn2 of 5' in pill(pg) and ids(pg, 'mst') == 'MO-6105 open', 'Enter in the input submits the order (%s)' % pill(pg))
    for _ in range(4):
        pg.locator('#cv .hint').first.click(); pg.wait_for_timeout(1700)
    f.check('Done' in pill(pg), 'try: back to Done after Enter (%s)' % pill(pg))


PLAN = [('One run, five stages, 400 lb in', 'Run MO-6105'),
        ('The routing sets expected output at every stage', '384'),
        ('Actual output fills in stage by stage, with the loss at each', 'Total loss 22 lb'),
        ('Finished cases post straight to a freezer', 'cases to Holding freezer A'),
        ('The next run is checked against stock before it starts', 'Create purchase order')]
f = run_card(4, PLAN, ['Total loss 22 lb against 16 lb expected.', 'Holding freezer A'], start=start,
             extra={'before': {0: bad_then_type}, 'after_step': {0: s1, 1: s2, 2: s3, 3: s4, 4: s5}, 'after': po})
finish(f)
