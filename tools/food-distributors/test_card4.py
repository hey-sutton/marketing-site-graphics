#!/usr/bin/env python3
"""Card 4 (board): the README's pick and stock numbers in Python, then the click through.
Run: python3 tools/food-distributors/test_card4.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fd_tests import run_card, finish, js, ids, readonly_checks, keyboard_walk, clicks_only

# The README's sample data, in sales order entry order (not bin order)
ORDER = [('B-12-3', 'Penne', 200, 700), ('A-02-1', 'Lime', 40, 500), ('A-04-2', 'Lavender', 30, 300)]
PICK = sorted(ORDER)
assert [p[0] for p in PICK] == ['A-02-1', 'A-04-2', 'B-12-3']                  # ascending bin order
TOTAL = sum(p[2] for p in PICK)
assert TOTAL == 40 + 30 + 200 == 270                                            # total picked
AFTER = {p[1]: p[3] - p[2] for p in PICK}
assert AFTER == {'Lime': 460, 'Lavender': 270, 'Penne': 500}                    # each on hand falls by its picked quantity
assert sum(p[3] for p in PICK) - sum(AFTER.values()) == TOTAL                   # stock falls by exactly what was picked


def upc_ok(c):
    return len(c) == 12 and (sum(int(x) for x in c[0:11:2]) * 3 + sum(int(x) for x in c[1:11:2]) + int(c[11])) % 10 == 0


BC = {'Lime': '085012340412', 'Lavender': '085012340429', 'Penne': '085034120207'}
assert all(upc_ok(c) for c in BC.values()) and len(set(BC.values())) == 3       # valid, distinct case barcodes
F = lambda c: '%s %s %s %s' % (c[0], c[1:6], c[6:11], c[11])


def chips(pg):
    return ids(pg, 's-A-02-1', 's-A-04-2', 's-B-12-3')


def start(pg, f, when='start'):
    readonly_checks(pg, f, {'iso': 'SO-3110'}, when)
    f.check(js(pg, "return r.querySelectorAll('.pk,.lg,.oh,.doc,#k-cs').length") == 0, '%s: pick list, scans, stock and totals empty' % when)
    t = js(pg, "return r.querySelector('.g3').innerText")
    f.check(not any(s in t for s in ('270', 'A-02-1', 'Lime', '460', 'PS-3110')), '%s: nothing derived shows' % when)


def s1(pg, f):
    order = js(pg, "return [].map.call(r.querySelectorAll('.pk'),function(e){return e.id})")
    f.check(order == ['p-A-02-1', 'p-A-04-2', 'p-B-12-3'], 'step 1: three lines in ascending bin order %s' % order)
    f.check(ids(pg, 'k-cs', 'k-ln') == '0 of 270|0 of 3' and chips(pg) == 'Next|Open|Open', 'step 1: 0 of 270 cases, nothing confirmed yet')
    f.check(ids(pg, 'o-Lime', 'o-Lavender', 'o-Penne', 'a-Lime') == '500|300|700|', 'step 1: on hand 500, 300, 700 before the pick')
    readonly_checks(pg, f, {'iso': 'SO-3110', 'ibc': F(BC['Lime'])}, 'step 1')


def s2(pg, f):
    f.check(chips(pg) == 'Picked|Next|Open' and 'ok' in js(pg, "return r.getElementById('p-A-02-1').className"), 'step 2: A-02-1 turns green, Picked')
    f.check(ids(pg, 'k-cs', 'k-ln', 'k-wr') == '40 of 270|1 of 3|0', 'step 2: 40 cases picked, 1 of 3 lines')


def s3(pg, f):
    w = js(pg, "var e=r.getElementById('wn');return e?e.innerText:''")
    f.check('Dish Soap Lime 12 pk' in w and 'Dish Soap Lavender 12 pk' in w and 'Lime against Lavender' in w, 'step 3: warning names Lime against Lavender')
    f.check(js(pg, "return r.querySelectorAll('#wn svg').length") == 2, 'step 3: warning shows both item pictures')
    f.check(chips(pg) == 'Picked|Wrong item|Open' and ids(pg, 'k-ln', 'k-cs', 'k-wr') == '1 of 3|40 of 270|1', 'step 3: the wrong scan does not confirm line 2')
    f.check(js(pg, "var b=r.getElementById('cpb');return b.disabled"), 'step 3: Complete pick stays disabled')
    readonly_checks(pg, f, {'iso': 'SO-3110', 'ibc': F(BC['Lavender'])}, 'step 3 (case swapped)')


def s4(pg, f):
    f.check(chips(pg) == 'Picked|Picked|Picked' and js(pg, "return r.querySelectorAll('.pk.ok').length") == 3, 'step 4: every line green')
    f.check(ids(pg, 'k-cs', 'k-ln', 'k-wr') == '270 of 270|3 of 3|1', 'step 4: 270 cases picked')
    f.check(ids(pg, 'a-Lime', 'a-Lavender', 'a-Penne') == '460|270|500', 'step 4: on hand 460, 270, 500')


def s5(pg, f):
    f.check(js(pg, "return r.querySelectorAll('.doc').length") == 2 and ids(pg, 'k-dc', 'rst') == '2 of 2|Ready to ship', 'step 5: two documents generated')
    f.check('Packing slip PS-3110' in ids(pg, 'd-ps') and 'Bill of lading BOL-3110' in ids(pg, 'd-bol'), 'step 5: packing slip and bill of lading')


PLAN = [('A pick list in bin order', 'A-02-1'),
        ('Right item, line confirmed', 'Picked'),
        ('A similar variant, caught', 'Wrong variant scanned'),
        ('Pick complete, stock updated', '460'),
        ('Packing slip and bill of lading', 'BOL-3110')]
f = run_card(4, PLAN, ['270 of 270', '460', '270', '500', 'PS-3110', 'BOL-3110'], start=start,
             extra={'after_step': {0: s1, 1: s2, 2: s3, 3: s4, 4: s5}})
keyboard_walk(f, 4, 5)
clicks_only(f, 4, 2)
clicks_only(f, 4, 2, 358, 390)
finish(f)
