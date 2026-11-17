#!/usr/bin/env python3
"""Card 4 (record form with a side summary: run billing and client portal): the numbers in Python, then the click through.
Run: python3 tools/food-co-packing/test_card4.py"""
import os, sys
from decimal import Decimal as D, ROUND_HALF_UP
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fc_tests import run_card, finish, js, pill, testlib, ids, enter_submits

# ---- the numbers, derived independently of the card ----
CASES, HOURS, BATCHES = 2400, D('6.5'), 3
assert CASES * D('0.85') == D('2040.00')          # per unit
assert HOURS * D('310.00') == D('2015.00')        # per hour
assert BATCHES * D('680.00') == D('2040.00')      # per batch
BAGS = CASES * 12
assert BAGS == 28800 and BAGS * D('0.04') == D('1152.00') and CASES * D('0.35') == D('840.00')
PACK = D('1152.00') + D('840.00')
assert PACK == D('1992.00')
INVOICE = D('2040.00') + PACK + D('0.00')         # client materials are recorded at $0.00
assert INVOICE == D('4032.00')
RICE = (D('1200'), D('420'), D('780'))
OIL = (D('300'), D('62.5'), D('235'))
assert RICE[0] - RICE[1] == D('780') and RICE[0] - RICE[1] - RICE[2] == 0
assert OIL[0] - OIL[1] == D('237.5') and OIL[0] - OIL[1] - OIL[2] == D('2.5')
assert (D('2.5') / D('237.5') * 100).quantize(D('0.01'), ROUND_HALF_UP) == D('1.05')


def start(pg, f, when='start'):
    t = js(pg, "return r.querySelector('.c4').innerText")
    f.check(js(pg, "return r.getElementById('bin').value+'|'+r.getElementById('brt').value") == '|', '%s: the run and rate inputs are empty' % when)
    f.check(js(pg, "return r.querySelectorAll('.bl .row,.rc .row,.pr').length") == 0, '%s: no billing lines, no reconcile rows, no portal' % when)
    f.check(not any(s in t for s in ('Brightfield', '2,400', '$4,032', 'INV-3051', '1,152')), '%s: nothing derived from the run shows' % when)


def bad_then_type(pg, f):
    inp = pg.locator('#cv #bin')
    inp.click(); inp.press_sequentially('R-9999'); inp.press('Enter'); pg.wait_for_timeout(300)
    f.check(js(pg, "return r.getElementById('bfl').classList.contains('err')"), 'step 1: an unknown run shows an inline error')
    f.check('Your turn1 of 5' in pill(pg), 'step 1: an unknown run does not advance')
    inp.fill(''); inp.press_sequentially('r-5108')


def fee_input(pg, f):
    pg.locator('#cv #fbh').click(); pg.wait_for_timeout(150)
    f.check(js(pg, "return r.getElementById('brt').value") == '310.00', 'step 2: per hour fills the contract rate 310.00')
    pg.locator('#cv #fbb').click(); pg.wait_for_timeout(150)
    f.check(js(pg, "return r.getElementById('brt').value") == '680.00', 'step 2: per batch fills the contract rate 680.00')
    pg.locator('#cv #fbu').click(); pg.wait_for_timeout(150)
    inp = pg.locator('#cv #brt'); inp.fill('abc'); pg.locator('#cv #bad').click(); pg.wait_for_timeout(300)
    f.check('Your turn2 of 5' in pill(pg) and js(pg, "return r.getElementById('bfr').classList.contains('err')"), 'step 2: a bad rate shows an inline error')
    inp.fill(''); inp.press_sequentially('0.85')


def s1(pg, f):
    f.check(ids(pg, 'blp0', 'blp1', 'blt', 'sp') == '$1,152.00|$840.00|$1,992.00|$1,992.00', 'step 1: packaging $1,152.00 + $840.00 = $1,992.00, fee not set')


def s2(pg, f):
    f.check(ids(pg, 'blf', 'blt', 'stt') == '$2,040.00|$4,032.00|$4,032.00', 'step 2: fee $2,040.00, total $4,032.00')
    t = ids(pg, 'bcr')
    f.check('$2,015.00' in t and '$2,040.00' in t, 'step 2: per hour $2,015.00, per batch $2,040.00')


def s3(pg, f):
    f.check(ids(pg, 'bis', 'stt') == 'INV-3051 posted|$4,032.00', 'step 3: INV-3051 posted for $4,032.00')


def s4(pg, f):
    t = js(pg, "return r.getElementById('bs').innerText")
    f.check(ids(pg, 'pr1', 'pin', 'ps0', 'ps1') == 'Completed, invoiced|$4,032.00|780.000 kg|235.000 kg', 'step 4: portal shows the run, the invoice and the stock')
    f.check('Oakline' not in t and 'Kettlewood' not in t, 'step 4: no other client in the portal')


def s5(pg, f):
    f.check(ids(pg, 'rx0', 'rv0', 'rx1', 'rv1') == '780.000|0.000|237.500|2.500', 'step 5: expected 780.000 and 237.500, variance 0.000 and 2.500')
    f.check('1.05%' in ids(pg, 'rcs') and '0.00%' in ids(pg, 'rcs'), 'step 5: 1.05% and 0.00%')


PLAN = [('Open a completed run and read its billing lines', '$1,992.00'),
        ('Add a conversion fee by unit, hour or batch', '$2,040.00'),
        ('Post the run to the client invoice', 'INV-3051 posted'),
        ('The client checks the portal, not the phone', 'Other clients are not visible'),
        ('Reconcile material used against received', '1.05%')]

f = run_card(4, PLAN, ['$4,032.00', '237.500', '1.05%'], start=start,
             extra={'before': {0: bad_then_type, 1: fee_input}, 'after_step': {0: s1, 1: s2, 2: s3, 3: s4, 4: s5}})
enter_submits(f, 4, '#bin', 'R-5108', 'Your turn2 of 5')
finish(f)
