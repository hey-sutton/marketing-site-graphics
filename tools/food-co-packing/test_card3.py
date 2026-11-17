#!/usr/bin/env python3
"""Card 3 (stage chain: cross client traceability): the numbers in Python, then the full click through.
Run: python3 tools/food-co-packing/test_card3.py"""
import os, sys
from decimal import Decimal as D
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fc_tests import run_card, finish, js, pill, testlib, ids, enter_submits

# ---- the numbers, derived independently of the card ----
LOT = D('2000')
RUNS = {'R-5202': ('B', D('600'), 'FL-8802', 1200), 'R-5207': ('O', D('450'), 'FL-8807', 900), 'R-5211': ('B', D('350'), 'FL-8811', 700)}
SHIP = [('SH-4401', 'FL-8802', 'Northgate Grocers', 700), ('SH-4405', 'FL-8802', 'Lakeside Market', 500), ('SH-4409', 'FL-8807', 'Northgate Grocers', 600), ('SH-4412', 'FL-8811', 'Pinewood Foodservice', 400)]
USED = sum(r[1] for r in RUNS.values())
assert USED == 600 + 450 + 350 == 1400 and LOT - USED == 600
MADE = sum(r[3] for r in RUNS.values())
assert MADE == 1200 + 900 + 700 == 2800
SHIPPED = sum(s[3] for s in SHIP)
assert SHIPPED == 700 + 500 + 600 + 400 == 2200 and MADE - SHIPPED == 600
assert len({r[0] for r in RUNS.values()}) == 2                      # more than one brand
FL_BRAND = {r[2]: r[0] for r in RUNS.values()}
B_MADE = sum(r[3] for r in RUNS.values() if r[0] == 'B')
B_SHIP = sum(s[3] for s in SHIP if FL_BRAND[s[1]] == 'B')
O_MADE, O_SHIP = MADE - B_MADE, SHIPPED - B_SHIP
assert B_MADE == 1900 and B_SHIP == 700 + 500 + 400 == 1600 and B_MADE - B_SHIP == 300
assert O_MADE == 900 and O_SHIP == 600 and O_MADE - O_SHIP == 300 and 300 + 300 == 600
assert len({s[2] for s in SHIP if FL_BRAND[s[1]] == 'B'}) == 3
assert RUNS['R-5207'][1] == D('450')                                   # FL-8807 traces back to 450 kg of SE-3318


def start(pg, f, when='start'):
    t = js(pg, "return r.querySelector('.c3').innerText")
    f.check(js(pg, "return r.getElementById('tin').value") == '', '%s: the lot input is empty' % when)
    f.check(js(pg, "return [0,1,2,3].every(function(i){return r.getElementById('sv'+i).textContent===''})"), '%s: every stage total is empty' % when)
    f.check(not any(s in t for s in ('Pinecrest', 'R-52', 'FL-88', 'SH-44', '2,000')), '%s: nothing derived from the lot shows' % when)


def bad_then_type(pg, f):
    inp = pg.locator('#cv #tin')
    inp.click(); inp.press_sequentially('SE-9999'); inp.press('Enter'); pg.wait_for_timeout(300)
    f.check(js(pg, "return r.getElementById('tfl').classList.contains('err')"), 'step 1: an unknown lot shows an inline error')
    f.check('Your turn1 of 5' in pill(pg), 'step 1: an unknown lot does not advance')
    inp.fill(''); inp.press_sequentially('se-3318')


def s1(pg, f):
    f.check(ids(pg, 'sv0') == '2,000.000 kg' and 'Pinecrest Ingredients' in js(pg, "return r.getElementById('tdt').innerText"), 'step 1: SE-3318, 2,000.000 kg from Pinecrest Ingredients')


def s2(pg, f):
    f.check(ids(pg, 'sv1', 'ss1', 'ss0') == '3 runs|2 brands, 1,400.000 kg used|1,400.000 kg used, 600.000 kg on hand', 'step 2: 3 runs, 2 brands, 1,400.000 used, 600.000 on hand')
    f.check(ids(pg, 'tu0', 'tu1', 'tu2') == '600.000 kg|450.000 kg|350.000 kg', 'step 2: 600 + 450 + 350 kg')


def s3(pg, f):
    f.check(ids(pg, 'sv2', 'ss2', 'tc0', 'tc1', 'tc2') == '3 lots|2,800 cases made|1,200|900|700', 'step 3: 1,200 + 900 + 700 = 2,800 cases')
    t = ids(pg, 'tbk')
    f.check('SE-3318' in t and '450.000 kg' in t and 'OF-2290' in t and 'HN-1175' in t, 'step 3: FL-8807 back to its ingredient lots')


def s4(pg, f):
    f.check(ids(pg, 'sv3', 'ss3', 'tgsB', 'tgsO') == '4 shipments|2,200 cases shipped, 600 on site|1,600 of 1,900 cases|600 of 900 cases', 'step 4: 2,200 shipped, 600 on site, by brand')


def s5(pg, f):
    f.check(ids(pg, 'tshB', 'tosB', 'tshO', 'tosO', 'tex') == '1,600|300|600|300|Exported', 'step 5: scope per brand, exported')
    f.check(ids(pg, 'txs').startswith('Brightfield Snacks: 2 runs, 2 finished lots, 1,900 cases, 1,600 shipped to 3 customers.'), 'step 5: Brightfield scope only')


PLAN = [('Search an ingredient lot', 'Pinecrest Ingredients'),
        ('One lot, runs for more than one brand', '1,400.000 kg used'),
        ('Open a finished lot back to its ingredients', 'OF-2290'),
        ('Shipments and customers by brand', '2,200 cases shipped'),
        ('Export the recall scope for one client', 'Exported')]

f = run_card(3, PLAN, ['1,900 cases', '1,600 shipped to 3 customers', 'Exported'], start=start,
             extra={'before': {0: bad_then_type}, 'after_step': {0: s1, 1: s2, 2: s3, 3: s4, 4: s5}})
enter_submits(f, 3, '#tin', 'SE-3318', 'Your turn2 of 5')
finish(f)
