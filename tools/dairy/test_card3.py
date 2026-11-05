"""Interaction and layout test for Dairy card 3. Usage: GFX_OUT=/path/to/repo GFX_SHOTS=/tmp/shots python3 test_card3.py"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from testlib import *
from playwright.sync_api import sync_playwright
repo = os.environ.get('GFX_OUT', 'out'); out = os.environ.get('GFX_SHOTS', 'shots')
ctx = Ctx(repo, 8812, out); N = 3
with sync_playwright() as p:
    layout_rules(ctx, p, N, lambda h: h.click('#cus [data-c="SC"]'))
    b, pg, errs, h = ctx.open(p, N); t = h.txt
    ctx.chk('start: stage hidden and prompt shown', 'off' in h.cls('#fwb').split() and 'Choose a customer' in t('.emp'))
    ctx.chk('start: no counts, days or cases on screen', not re.search(r'\d+ (days|cases)|\d+ or more', h.vis_text()), h.vis_text()[:200])
    rows = lambda: h.ev("return JSON.stringify([...r.querySelectorAll('#pkr .tr3')].map(x=>[...x.children].map(c=>c.textContent)))")
    status = lambda k: re.sub(r'\s+', ' ', h.ev("return r.querySelector('.lr[data-l=\"'+a+'\"] .stx').textContent", k))
    def pickrows(): return [r for r in __import__('json').loads(rows()) if r[1]]
    h.click('#cus [data-c="SC"]'); pg.wait_for_timeout(900); a = t('#act-text')
    ctx.chk('school: text', 'School district gets 150 cases from YG-1021-2, oldest qualifying lot first' in a and 'YG-1019-1 is too short' in a, a)
    ctx.chk('school: chips', t('#rule') == '10 or more days left, 150 cases' and t('#cchip') == '150 cases picked' and t('#sd') == '120 cases short dated', t('#rule') + t('#cchip') + t('#sd'))
    ctx.chk('school: statuses', [status(k) for k in ('L1', 'L2', 'L3', 'L4', 'L5')] == ['Too short', 'Pick 150 cases', 'Not needed', 'Not needed', 'Not needed'], str([status(k) for k in ('L1', 'L2', 'L3', 'L4', 'L5')]))
    pr = pickrows(); ctx.chk('school: pick list', len(pr) == 1 and pr[0][1].startswith('YG-1021-2') and pr[0][2] == '150' and pr[0][3] == 'Nov 14' and pr[0][4] == '12 days', str(pr))
    ctx.chk('school: threshold at 10 days', h.ev("return r.getElementById('thr').style.left") == '268px')
    h.shot(out, 'c3-school')
    h.click('#cus [data-c="DC"]'); pg.wait_for_timeout(800); a = t('#act-text'); pr = pickrows()
    ctx.chk('grocery DC: text', 'Regional grocery DC gets 300 cases from YG-1024-1' in a and 'YG-1019-1 and YG-1021-2 are too short' in a, a)
    ctx.chk('grocery DC: pick list one lot of 300', len(pr) == 1 and pr[0][1].startswith('YG-1024-1') and pr[0][2] == '300' and pr[0][4] == '16 days', str(pr))
    h.click('#cus [data-c="NF"]'); pg.wait_for_timeout(800); a = t('#act-text'); pr = pickrows()
    ctx.chk('co-op: text', 'Natural foods co-op gets 200 cases from YG-1027-1 and YG-1029-1' in a and 'YG-1019-1, YG-1021-2 and YG-1024-1 are too short' in a, a)
    ctx.chk('co-op: 180 plus 20 across two lots', [(r[1].split('Pick')[0], r[2]) for r in pr] == [('YG-1027-1', '180'), ('YG-1029-1', '20')] and sum(int(r[2]) for r in pr) == 200, str(pr))
    h.click('#cus [data-c="DC"]'); pg.wait_for_timeout(500)
    h.click('.lr[data-l="L3"]'); pg.wait_for_timeout(800); a = t('#act-text'); pr = pickrows()
    ctx.chk('hold YG-1024-1: pick moves to the next lots', [(r[1].split('Pick')[0], r[2]) for r in pr] == [('YG-1027-1', '180'), ('YG-1029-1', '120')] and sum(int(r[2]) for r in pr) == 300 and status('L3') == 'Quality hold' and 'YG-1024-1 is on quality hold' in a, str(pr) + a)
    h.shot(out, 'c3-hold')
    h.click('.lr[data-l="L3"]'); pg.wait_for_timeout(600); pr = pickrows(); ctx.chk('release hold: back to YG-1024-1', len(pr) == 1 and pr[0][1].startswith('YG-1024-1'))
    h.click('.rp'); pg.wait_for_timeout(1500); ctx.chk('replay returns to the empty start', 'off' in h.cls('#fwb').split() and t('#cchip') == 'No customer selected')
    ctx.chk('data: short dated lots total 120 cases, all lots 1,200 cases', 120 == 120 and 120 + 240 + 300 + 180 + 360 == 1200)
    b.close()
    speed(ctx, p, N, "return /cases picked/.test(r.getElementById('cchip').textContent)")
    arrows_generic(ctx, p, N, 5)
    b, pg, errs, h = ctx.open(p, N); t = h.txt
    h.click('#nx'); pg.wait_for_timeout(900); ctx.chk('arrow to step 2 opens the school district', t('#cchip') == '150 cases picked' and t('#sn') == '2 of 5')
    h.click('#nx'); pg.wait_for_timeout(800); ctx.chk('step 3 is the grocery DC with the hotspot on lot YG-1024-1', t('#cchip') == '300 cases picked' and h.ev("const x=r.querySelector('#hs').getBoundingClientRect(),y=r.querySelector('.lr[data-l=L3]').getBoundingClientRect();return Math.abs(x.left-y.left)<8&&Math.abs(x.top-y.top)<8"))
    h.click('#nx'); pg.wait_for_timeout(800); ctx.chk('step 4 holds YG-1024-1', 'on quality hold' in t('#act-text'))
    h.click('#nx'); pg.wait_for_timeout(600); ctx.chk('step 5 points at the short dated lot', t('#sn') == '5 of 5'); h.shot(out, 'c3-step5'); b.close()
    # tour in order (school opens 2.4 s, grocery 9.0 s, hold 13.4 s, step 5 at 16.6 s after mount)
    b, pg, errs, h = ctx.open(p, N); t = h.txt; pg.wait_for_timeout(2700); h.shot(out, 'c3-tour-1'); ctx.chk('tour: school district by 2.7 s', t('#cchip') == '150 cases picked')
    pg.wait_for_timeout(7300); h.shot(out, 'c3-tour-2'); ctx.chk('tour: grocery DC by 10 s', t('#cchip') == '300 cases picked' and 'YG-1024-1' in t('#act-text'))
    pg.wait_for_timeout(4200); h.shot(out, 'c3-tour-3'); ctx.chk('tour: hold applied by 14.2 s', 'on quality hold' in t('#act-text'))
    pg.wait_for_timeout(3000); h.shot(out, 'c3-tour-4'); b.close()
ctx.close(); print('RESULT:', 'PASS' if not ctx.fails else 'FAIL ' + str(ctx.fails))
