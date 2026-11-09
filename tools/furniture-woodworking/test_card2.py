#!/usr/bin/env python3
"""Card 2 Offcuts & Remnants: click through (both modes), numbers, layout, variety, navigation, phone and typing checks.
Run: python3 tools/furniture-woodworking/test_card2.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from furniture_tests import run_all, js, start_rule, typed
import card2

# guillotine layout on one 96 x 48 in sheet: parts and the remnant fill it exactly, no overlaps
sheet = 96 * 48
areas = [w * h for _, _, _, w, h in card2.PARTS]
rem = card2.REMNANT[2] * card2.REMNANT[3]
assert areas == [720, 720, 864, 864, 900] and sum(areas) == 4068 and rem == 540 and sum(areas) + rem == sheet == 4608
assert round(sum(areas) / sheet * 100, 1) == 88.3 and round(rem / sheet * 100, 1) == 11.7 and rem / 144 == 3.75
cells = set()
for x, y, w, h in [p[1:] for p in card2.PARTS] + [card2.REMNANT]:
    for i in range(x, x + w):
        for j in range(y, y + h):
            assert (i, j) not in cells and 0 <= i < 96 and 0 <= j < 48
            cells.add((i, j))
assert len(cells) == sheet


def start(pg, f):
    start_rule(pg, f, ['88.3', 'Side panel', 'RM-0031', '30 x 18'])
    f.check(js(pg, "return r.getElementById('ij').value") == '', 'start: the job field is empty')
    f.check(js(pg, "return r.getElementById('sh0').textContent+'|'+r.getElementById('rm0').textContent") == '12|2', 'start: 12 sheets and 2 remnants')


def job(pg, f):
    js(pg, "var e=r.getElementById('ij');e.value='J-9999';e.dispatchEvent(new Event('input',{bubbles:true}))")
    pg.locator('#cv .hint').first.click(); pg.wait_for_timeout(400)
    f.check(js(pg, "return r.getElementById('fj').classList.contains('err')"), 'step 2: an unknown job shows an inline error')
    js(pg, "var e=r.getElementById('ij');e.value='';e.dispatchEvent(new Event('input',{bubbles:true}))")


def leftover(pg, f):
    f.check(js(pg, "return [r.getElementById('rsz').textContent,r.getElementById('rsf').textContent,r.getElementById('yl').textContent].join('|')") == '30 x 18 in|3.75 sq ft|88.3%', 'step 4: 30 x 18 in, 3.75 sq ft, yield 88.3%')


def inv(pg, f):
    f.check(js(pg, "return r.getElementById('ish').textContent+'|'+r.getElementById('irm').textContent") == '11|3', 'step 6: 11 sheets and 3 remnants')
    f.check('R2-04' in js(pg, "return r.getElementById('rw-RM-0031').textContent"), 'step 6: RM-0031 on shelf R2-04')


def end(pg, f):
    ids = js(pg, "return [].map.call(r.querySelectorAll('.rt .row:not(.h)'),function(x){return x.id}).join(',')")
    f.check(ids == 'rw-RM-0026,rw-RM-0031', 'end: width 24 in or more leaves two remnants (%s)' % ids)


PLAN = [('Start from the stock you actually have', 'Maple plywood, 3/4 in'),
        ("Load a job's cut list", '36 x 24'),
        ('Parts nest on one sheet', 'Nested'),
        ('The leftover is a usable piece, not waste', '88.3%'),
        ('One click books it back', 'RM-0031 on shelf R2-04'),
        ('It lands in inventory with its size and shelf', 'R2-04'),
        ('Find leftovers by width before ordering new sheets', 'RM-0031')]

f = run_all(2, PLAN, ['RM-0031', 'R2-04', 'Width 24 in or more'], extra={'before': {0: start, 1: job, 4: leftover, 6: inv}, 'after': end},
            more=lambda f: typed(2, f, 1, 'ij', 'J-2417', 'Cut list J-2417'))
print('\n%d failures' % len(f)); sys.exit(1 if f else 0)
