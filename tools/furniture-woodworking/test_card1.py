#!/usr/bin/env python3
"""Card 1 Stage Scheduling & Capacity: click through (both modes), numbers, layout, variety, navigation and phone checks.
Run: python3 tools/furniture-woodworking/test_card1.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from furniture_tests import run_all, js, start_rule

# Finish room, week of Nov 23: 32 + 20 + 24 + 16 = 92 of 80; move J-2421 (16 h) to Nov 30: 76 and 28 + 16 = 44
assert 32 + 20 + 24 + 16 == 92 and 92 - 80 == 12 and 92 - 16 == 76 and 28 + 16 == 44 and 6.5 + 3.5 == 10


def start(pg, f):
    f.check(js(pg, "return r.getElementById('cl-1').textContent+'|'+r.getElementById('cl-2').textContent") == '92 of 80 h|28 of 80 h', 'start: Nov 23 92 of 80 h, Nov 30 28 of 80 h')
    f.check(js(pg, "return r.getElementById('cc-1').classList.contains('ov')"), 'start: the Nov 23 week is flagged amber')
    start_rule(pg, f, ['In Finish', '76 of 80'])


def panel(pg, f):
    f.check(js(pg, "return r.getElementById('cpt').textContent") == '92 h', 'step 2: the panel totals 92 h')


def moved(pg, f):
    f.check(js(pg, "return r.getElementById('cl-1').textContent+'|'+r.getElementById('cl-2').textContent") == '76 of 80 h|44 of 80 h', 'step 3: Nov 23 76 of 80 h, Nov 30 44 of 80 h')
    f.check(js(pg, "return r.getElementById('cc-1').classList.contains('ok')"), 'step 3: Nov 23 turns green')


def sheet(pg, f):
    f.check(js(pg, "return r.getElementById('is').value") == '3.5', 'step 7: 3.5 h prefilled')
    js(pg, "var e=r.getElementById('is');e.value='0';e.dispatchEvent(new Event('input',{bubbles:true}))")
    pg.locator('#cv .hint').first.click(); pg.wait_for_timeout(400)
    f.check(js(pg, "return r.getElementById('fs').classList.contains('err')"), 'step 7: zero hours shows an inline error')
    js(pg, "var e=r.getElementById('is');e.value='3.5';e.dispatchEvent(new Event('input',{bubbles:true}))")
    f.check(js(pg, "return r.getElementById('stt').textContent") == '10 of 10 h', 'step 7: stain total 10 of 10 h')


def fin(pg, f):
    f.check('10 of 10 h' in js(pg, "return r.getElementById('sd').textContent"), 'step 7: stain closed at 10 of 10 h')


def end(pg, f):
    f.check(js(pg, "return r.getElementById('j-J-2417').textContent").find('In Finish') > -1, 'end: J-2417 shows In Finish on the board')


PLAN = [('Every job, every stage, one calendar', 'Week of Dec 7'),
        ('Finish is booked 92 of 80 hours this week', 'Over by 12 h'),
        ('Move one stage and capacity updates', '76 of 80 h'),
        ('Both weeks now fit', '44 of 80 h'),
        ('Open any job to see where it stands', '6.5 of 10 h'),
        ('Operators clock into a step on any device', 'Start Finish'),
        ('Stain closes at 10 of 10 hours and finish starts', 'In Finish'),
        ('The calendar follows the floor without a status meeting', 'In Finish')]

f = run_all(1, PLAN, ['In Finish', '76 of 80 h', '44 of 80 h'], extra={'before': {0: start, 2: panel, 3: moved, 6: sheet, 7: fin}, 'after': end})
print('\n%d failures' % len(f)); sys.exit(1 if f else 0)
