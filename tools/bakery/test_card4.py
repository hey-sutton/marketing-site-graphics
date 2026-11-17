#!/usr/bin/env python3
"""Card 4 (transfer pipeline, location cards, rack tags): the brief's numbers in Python, then the full click through.
Run: python3 tools/bakery/test_card4.py"""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bk_tests import run_card, finish, js, pill, testlib, ids, enter_submits

# ---- the brief's numbers, derived independently of the card ----
STOCK = {'loaf': 120, 'bun': 60}
RACK = 15
ORDERS = {'TO-3301': (40, 20), 'TO-3302': (30, 15), 'SO-3303': (30, 15)}
assert 40 + 30 + 30 == sum(o[0] for o in ORDERS.values()) == 100
assert 20 + 15 + 15 == sum(o[1] for o in ORDERS.values()) == 50
assert 100 + 50 == 150 and 120 - 100 == 20 and 60 - 50 == 10
assert 60 / 15 == 4 and 45 / 15 == 3 and 4 + 3 + 3 == 10 and 150 / 15 == 10
RACKS = {k: math.ceil(sum(v) / RACK) for k, v in ORDERS.items()}
assert RACKS == {'TO-3301': 4, 'TO-3302': 3, 'SO-3303': 3}


def start(pg, f, when='start'):
    t = js(pg, "return r.querySelector('.k4').innerText")
    f.check(js(pg, "return r.getElementById('kq0').value+'|'+r.getElementById('kq1').value") == '|', '%s: the portal inputs are empty' % when)
    f.check(js(pg, "return [0,1,2,3].every(function(k){return r.getElementById('kpc'+k).textContent===''})"), '%s: the pipeline has no counts' % when)
    f.check(js(pg, "return r.querySelectorAll('.ktag,.kln2').length") == 0 and js(pg, "return !!r.getElementById('kpl')"), '%s: no order lines, no rack tags, Place order shown' % when)
    f.check(not any(s in t for s in ('TO-3301', 'SO-3303', 'L-5120', '100 of 120', 'In transit')), '%s: nothing derived from the order shows' % when)


def bad_then_type(pg, f):
    pg.locator('#cv #kq0').fill('100'); pg.locator('#cv #kq1').fill('15')
    pg.locator('#cv #kpl').click(); pg.wait_for_timeout(300)
    f.check(js(pg, "return r.getElementById('kptl').classList.contains('err')") and ids(pg, 'kqe') == 'Only 50 loaf and 25 bun crates are free', 'step 1: more than the free stock shows an inline error')
    f.check('Your turn1 of 5' in pill(pg), 'step 1: an order over stock does not advance')
    for sel, v in (('#kq0', '30'), ('#kq1', '15')):
        inp = pg.locator('#cv ' + sel); inp.fill(''); inp.press_sequentially(v)
    f.check(js(pg, "return r.getElementById('kq0').value+'|'+r.getElementById('kq1').value") == '30|15', 'step 1: typing works in both inputs')


def s1(pg, f):
    f.check(ids(pg, 'kb2', 'kq20', 'kq21') == 'Pending approval|30 crates|15 crates', 'step 1: SO-3303 Pending approval, 30 and 15 crates')
    f.check(not js(pg, "return !!r.getElementById('kpk')"), 'step 1: no picking before approval')
    f.check(js(pg, "return r.querySelectorAll('#kl0 .kln2,#kl1 .kln2').length") == 0, 'step 1: the shop cards are still empty')


def s2(pg, f):
    f.check(ids(pg, 'kpc0', 'kps0') == '3|Loaf 100 of 120, bun 50 of 60', 'step 2: Commit counts 3, loaf 100 of 120, bun 50 of 60')
    f.check(ids(pg, 'kb0', 'kb1', 'kb2') == 'Committed|Committed|Committed', 'step 2: three orders committed')
    f.check(ids(pg, 'ktot0', 'ktot1', 'ktot2') == '60 crates, 4 racks|45 crates, 3 racks|45 crates, 3 racks', 'step 2: 60, 45 and 45 crates, 4, 3 and 3 racks')
    f.check(js(pg, "return r.querySelectorAll('[id^=krv]').length") == 0, 'step 2: nothing can be received before it ships')


def s3(pg, f):
    lots = [ids(pg, 'klot%d0' % i, 'klot%d1' % i) for i in range(3)]
    f.check(lots == ['L-5120|L-5121'] * 3, 'step 3: L-5120 and L-5121 on every order')
    per = js(pg, "var o={};[].forEach.call(r.querySelectorAll('.ktag'),function(t){o[t.dataset.o]=(o[t.dataset.o]||0)+1});return [o[0],o[1],o[2]].join(',')")
    f.check(ids(pg, 'ktn') == '10 tags' and per == '4,3,3', 'step 3: 10 rack tags, 4, 3 and 3 (%s)' % per)
    crates = js(pg, "var o=[0,0,0];[].forEach.call(r.querySelectorAll('.ktag'),function(t){o[+t.dataset.o]+=parseInt(t.querySelector('.kq').textContent,10)});return o.join(',')")
    f.check(crates == '60,45,45', 'step 3: the tags add up to 60, 45 and 45 crates')
    f.check(ids(pg, 'krf') == '4 + 3 + 3 = 10 racks, 150 crates, 15 to a rack', 'step 3: 4 + 3 + 3 = 10 racks, 150 crates')


def s4(pg, f):
    f.check(ids(pg, 'kb0', 'kb1', 'kb2', 'kpc2') == 'In transit|In transit|In transit|3', 'step 4: all three In transit')


def s5(pg, f):
    f.check(ids(pg, 'kb0', 'kb1', 'kb2', 'kpc3') == 'Received|In transit|In transit|1', 'step 5: Maple Street Received, the others In transit')
    f.check('L-5120, L-5121' in ids(pg, 'khis0'), 'step 5: Maple Street keeps lot history L-5120 and L-5121')


def free_receive(pg, f):
    pg.locator('#cv #krv1').click(); pg.wait_for_timeout(400)
    f.check(ids(pg, 'kb1', 'kpc3') == 'Received|2', 'after Done: Harbor Road can be received too')


PLAN = [('A franchise orders from the central bakery', 'Pending approval'),
        ('Approve it and stock is committed', 'Loaf 100 of 120, bun 50 of 60'),
        ('Pick by lot and print rack tags', '10 tags'),
        ('Ship, and every location sees it', 'In transit'),
        ('Receive at the shop with lot history intact', 'Lot history kept')]


def prep4(pg):
    pg.locator('#cv #kq1').fill('15')


f = run_card(4, PLAN, ['1 of 3 received', 'Lot history kept', 'L-5120, L-5121'], start=start,
             extra={'before': {0: bad_then_type}, 'after_step': {0: s1, 1: s2, 2: s3, 3: s4, 4: s5}, 'after': free_receive})
enter_submits(f, 4, '#kq0', '30', 'Your turn2 of 5', prep=prep4)
finish(f)
