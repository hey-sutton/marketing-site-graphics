#!/usr/bin/env python3
"""Card 1 (batch list and dossier): the brief's numbers in Python, then the click through.
Run: python3 tools/pharmaceutical/test_card1.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ph_tests import run_card, finish, js, pill, ids, enter_submits

# grams, so every kilogram sum is exact
REC, B2611, B2614 = 150000, 68996, 34498
assert B2611 + B2614 == 103494                      # 68.996 + 34.498 = 103.494
assert REC - (B2611 + B2614) == 46506               # 150.000 - 103.494 = 46.506
BOT = {'B-2611': 2000, 'B-2614': 1000}
assert sum(BOT.values()) == 3000                    # 2,000 + 1,000
SHIP = [('SH-3101', 'B-2611', 'Kestrel Wellness', 800), ('SH-3104', 'B-2611', 'Bayline Compounding', 400), ('SH-3109', 'B-2614', 'Kestrel Wellness', 600)]
SITE = {'B-2611': 800, 'B-2614': 400}
shipped = sum(q for *_, q in SHIP)
assert shipped == 800 + 400 + 600 == 1800
assert sum(SITE.values()) == 800 + 400 == 1200
assert shipped + sum(SITE.values()) == 3000
for b in BOT:
    assert sum(q for _, x, _, q in SHIP if x == b) + SITE[b] == BOT[b]
kes = sum(q for _, _, c, q in SHIP if c == 'Kestrel Wellness'); bay = sum(q for _, _, c, q in SHIP if c == 'Bayline Compounding')
assert kes == 800 + 600 == 1400 and bay == 400 and kes + bay == 1800
assert 10204 + 68996 + 800 == 80000                 # B-2611 weighed inputs 80.000 kg


def start(pg, f, when='start'):
    t = js(pg, "return r.querySelector('.g1').innerText")
    f.check(js(pg, "return r.getElementById('ilt').value") == '' and js(pg, "return r.querySelectorAll('.bls .row,.dos .tab,.lot .kv').length") == 0, '%s: empty input, list and dossier show a prompt only' % when)
    f.check(not any(s in t for s in ('150.000', 'B-26', 'Alder', 'Kestrel', 'kg')), '%s: nothing derived from the lot shows' % when)


def bad_then_type(pg, f):
    inp = pg.locator('#cv #ilt')
    inp.click(); inp.press_sequentially('EX-0000'); inp.press('Enter'); pg.wait_for_timeout(300)
    f.check(js(pg, "return r.getElementById('flt').classList.contains('err')") and 'Your turn1 of 5' in pill(pg), 'step 1: an unknown lot shows an error and does not advance')
    inp.fill(''); inp.press_sequentially('ex-3307')
    f.check(js(pg, "return r.getElementById('ilt').value") == 'ex-3307', 'step 1: typing works in the input')


def s1(pg, f):
    t = js(pg, "return r.getElementById('lot').innerText")
    f.check('150.000 kg' in t and 'Alder Ridge Supply' in t and 'Microcrystalline cellulose' in t, 'step 1: EX-3307, cellulose, 150.000 kg, Alder Ridge Supply')


def s2(pg, f):
    f.check(ids(pg, 'bu-B-2611', 'bu-B-2614', 'bu-B-2609', 'lcs', 'loh') == '68.996 kg|34.498 kg|0.000 kg|103.494 kg|46.506 kg', 'step 2: 68.996 and 34.498 kg used, 103.494 consumed, 46.506 on hand')
    t = js(pg, "return r.getElementById('bls').innerText")
    f.check(t.count('Affected') == 2 and 'Not affected' in t and 'EX-3190' in t, 'step 2: two batches affected, B-2609 (EX-3190) not affected')


def s3(pg, f):
    t = js(pg, "return r.querySelector('.inp').innerText")
    for s in ('AP-8841', '10.204 kg', 'Assay 98.0%', 'EX-3307', '68.996 kg', 'EX-4410', '0.800 kg', 'CS-1192', '200,000', 'PK-7720', 'PK-7731', 'LB-5503'):
        f.check(s in t, 'step 3: inputs show %s' % s)
    f.check(ids(pg, 'bkg') == '80.000 kg' and t.count('Attached') == 3, 'step 3: blend 80.000 kg, three certificates attached')
    f.check('Supplier lot EX-3307' in js(pg, "return r.querySelector('.dos .ct').innerText"), 'step 3: supplier lot beside the batch number')


def s4(pg, f):
    t = js(pg, "return r.querySelector('.shp').innerText")
    f.check(all(s in t for s in ('SH-3101', 'SH-3104', 'SH-3109', 'Kestrel Wellness', 'Bayline Compounding')), 'step 4: three shipments with customers')
    f.check(ids(pg, 'smd', 'ssh', 'sos') == '3,000|1,800|1,200', 'step 4: 3,000 made, 1,800 shipped, 1,200 on site')
    c = js(pg, "return r.querySelector('.cus').innerText")
    f.check('1,400 bottles' in c and '400 bottles' in c, 'step 4: Kestrel Wellness 1,400, Bayline Compounding 400')


def s5(pg, f):
    f.check(js(pg, "return r.getElementById('hsum').firstChild.textContent") == '2 batches, 2 customers, 1,200 bottles held.', 'step 5: 2 batches, 2 customers, 1,200 bottles held')
    f.check(ids(pg, 'rkg', 'lst') == '46.506 kg|On hold', 'step 5: 46.506 kg of EX-3307 on hold')
    f.check(js(pg, "return r.querySelectorAll('.sts .c-hold').length") == 3, 'step 5: both bottle lines and the lot line on hold')


PLAN = [('A supplier notice names one lot', '150.000 kg'),
        ('Every batch that used the lot', '103.494 kg'),
        ('The dossier lists every input by supplier lot', '80.000 kg'),
        ('Follow the bottles to customers', '1,800'),
        ('One click holds what is still on site', '1,200 bottles held')]
f = run_card(1, PLAN, ['2 batches, 2 customers, 1,200 bottles held.', '46.506 kg'], start=start,
             extra={'before': {0: bad_then_type}, 'after_step': {0: s1, 1: s2, 2: s3, 3: s4, 4: s5}})
enter_submits(f, 1, '#ilt', 'EX-3307', 'Your turn2 of 5')
finish(f)
