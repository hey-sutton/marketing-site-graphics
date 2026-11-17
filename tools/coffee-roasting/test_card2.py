#!/usr/bin/env python3
"""Card 2 (green lot record and roast yield): the brief's numbers in Python, then the full click through.
Run: python3 tools/coffee-roasting/test_card2.py"""
import os, sys
from decimal import Decimal as D, ROUND_HALF_UP
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cr_tests import run_card, finish, js, pill, testlib, ids, enter_submits


def pct(i, o):
    return (D(i - o) * 100 / D(i)).quantize(D('0.1'), ROUND_HALF_UP)


# ---- the brief's numbers, derived independently of the card ----
BAL, BAG = 840000, 60000                     # GL-2207: 840.000 kg on hand in 60 kg bags
assert BAL // BAG == 14 and BAL % BAG == 0
assert BAL - 60000 == 780000 and (BAL - 60000) // BAG == 13   # the roast takes exactly 60.000 kg
assert pct(60000, 51600) == D('14.0')                            # 60.000 in, 51.600 out: 14.0%
assert pct(60000, 50400) == D('16.0')                            # the brief's 50.4 kg would be 16.0%, not 14.0%
HIST = {('Ethiopia', 0): [(60000, 52200), (60000, 51960)], ('Ethiopia', 1): [(60000, 51300), (60000, 51420)], ('Ethiopia', 2): [(60000, 50100)],
        ('Colombia', 0): [(70000, 61180), (70000, 60900)], ('Colombia', 1): [(70000, 60480), (70000, 60200)], ('Colombia', 2): [(70000, 59080)],
        ('Brazil', 0): [(60000, 52500)], ('Brazil', 1): [(60000, 51840), (60000, 51600)], ('Brazil', 2): [(60000, 50400), (60000, 50160)]}


def avg(rows):
    return pct(sum(i for i, _ in rows), sum(o for _, o in rows))


assert avg(HIST[('Ethiopia', 0)]) == D('13.2')
HIST[('Ethiopia', 0)].append((60000, 51600))
WANT = {('Ethiopia', 0): '13.5', ('Ethiopia', 1): '14.4', ('Ethiopia', 2): '16.5', ('Colombia', 0): '12.8', ('Colombia', 1): '13.8',
        ('Colombia', 2): '15.6', ('Brazil', 0): '12.5', ('Brazil', 1): '13.8', ('Brazil', 2): '16.2'}
for k, v in WANT.items():
    assert str(avg(HIST[k])) == v, (k, avg(HIST[k]))
assert max(WANT.items(), key=lambda kv: D(kv[1]))[0] == ('Ethiopia', 2)


def start(pg, f, when='start'):
    t = js(pg, "return r.querySelector('.q2').innerText")
    f.check(js(pg, "return r.getElementById('qli').value+'|'+r.getElementById('qgi').value+'|'+r.getElementById('qro').value") == '||', '%s: all inputs empty' % when)
    f.check(js(pg, "return r.getElementById('qgi').disabled&&r.getElementById('qro').disabled"), '%s: the roast form waits for a lot' % when)
    f.check(not any(s in t for s in ('Highmark', '840.000', 'RB-1112-2', '14.0%', 'Ethiopia')), '%s: nothing from the lot shows' % when)


def bad_then_type(pg, f):
    inp = pg.locator('#cv #qli')
    inp.click(); inp.press_sequentially('GL-9999'); inp.press('Enter'); pg.wait_for_timeout(300)
    f.check(js(pg, "return r.getElementById('qfl').classList.contains('err')") and 'Your turn1 of 5' in pill(pg), 'step 1: an unknown lot shows an error and does not advance')
    inp.fill(''); inp.press_sequentially('gl-2207')


def type_green(pg, f):
    inp = pg.locator('#cv #qgi')
    f.check(inp.input_value() == '60.000', 'step 2: the planned charge 60.000 is prefilled')
    inp.fill('900'); pg.locator('#cv #qlb').click(); pg.wait_for_timeout(300)
    f.check(js(pg, "return r.getElementById('qfg').classList.contains('err')") and 'Your turn2 of 5' in pill(pg), 'step 2: more than the lot balance shows an error')
    inp.fill(''); inp.press_sequentially('60')


def type_out(pg, f):
    inp = pg.locator('#cv #qro')
    inp.fill('61'); pg.locator('#cv #qrc').click(); pg.wait_for_timeout(300)
    f.check(js(pg, "return r.getElementById('qfo').classList.contains('err')") and 'Your turn3 of 5' in pill(pg), 'step 3: more out than in shows an error')
    inp.fill(''); inp.press_sequentially('51.6')


def s1(pg, f):
    f.check(ids(pg, 'qoh', 'qbg', 'qbal') == '840.000 kg|14|840.000', 'step 1: GL-2207 840.000 kg, 14 bags')
    t = js(pg, "return r.getElementById('qlg').innerText")
    f.check(all(s in t for s in ('Ethiopia, Yirgacheffe', 'Highmark Green Imports', 'Oct 28, 2026', '20 of 60.000 kg')), 'step 1: origin, supplier, arrival and bags')


def s2(pg, f):
    f.check(ids(pg, 'qbal', 'qbg', 'qdl') == '780.000|13|Down 60.000 kg on RB-1119-4', 'step 2: balance drops by exactly 60.000 kg to 780.000, 13 bags')


def s3(pg, f):
    f.check(ids(pg, 'qloss', 'qrol') == '14.0%|51.600', 'step 3: 51.600 kg out is a 14.0% loss')


def s4(pg, f):
    got = {k: ids(pg, 'qa-%s-%d' % k) for k in WANT}
    f.check(all(got[k] == v + '%' for k, v in WANT.items()), 'step 4: shrink by origin and level matches (%s)' % got)


def s5(pg, f):
    t = ids(pg, 'qtg')
    f.check('GL-2207' in t and '60.000 kg' in t and 'Yirgacheffe' in t, 'step 5: RL-1119-4 traces back to 60.000 kg of GL-2207')


PLAN = [('Open a green lot with origin, supplier and bags', '840.000'),
        ('Log a roast batch and watch the lot balance drop', '780.000'),
        ('Record roasted weight and read the roast loss', '14.0%'),
        ('Compare shrink across origins and roast levels', '13.5%'),
        ('Trace a roasted lot back to its green lot', 'Highmark Green Imports')]

f = run_card(2, PLAN, ['780.000', '14.0%', 'RL-1119-4', '16.5%'], start=start,
             extra={'before': {0: bad_then_type, 1: type_green, 2: type_out}, 'after_step': {0: s1, 1: s2, 2: s3, 3: s4, 4: s5}})
enter_submits(f, 2, '#qli', 'GL-2207', 'Your turn2 of 5')
finish(f)
