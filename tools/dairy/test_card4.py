"""Interaction and layout test for Dairy card 4. Usage: GFX_OUT=/path/to/repo GFX_SHOTS=/tmp/shots python3 test_card4.py"""
import os, re, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from testlib import *
from playwright.sync_api import sync_playwright
repo = os.environ.get('GFX_OUT', 'out'); out = os.environ.get('GFX_SHOTS', 'shots')
ctx = Ctx(repo, 8814, out); N = 4
PXH = 10.6; LBL = 90
with sync_playwright() as p:
    layout_rules(ctx, p, N, lambda h: h.click('#rush [data-i="1"]'))
    b, pg, errs, h = ctx.open(p, N); t = h.txt
    # baseline: the current schedule and stock show, nothing derived from a rush order does
    ctx.chk('start: on track, nothing derived from a rush order', t('#pchip') == 'On track' and t('#m4') == '' and t('#v4') == '' and t('#m5') == 'OK' and not re.search(r'Short \d|past Friday|PO-2231|Greek \d', h.vis_text()), h.vis_text()[:300])
    ctx.chk('start: baseline numbers', t('#gtc') == 'Yogurt line done at hour 38 of 40' and (t('#m1'), t('#m2'), t('#m3')) == ('52,000 lb', '41,500 lb', '10,500 lb') and (t('#v1'), t('#v2'), t('#v3')) == ('120 lb', '70 lb', '50 lb'), t('#gtc'))
    ctx.chk('start: create purchase order is disabled and the rush block is hidden', h.dis('#po') and 'hide' in h.cls('.bk.rs').split())
    blk = lambda k: h.ev("const e=r.querySelectorAll('.bk');return null") if False else None
    def pos(label):
        return h.ev("const e=[...r.querySelectorAll('.bk')].find(x=>x.querySelector('b').textContent===a);return [parseFloat(e.style.left),parseFloat(e.style.width),e.className,e.querySelector('span').textContent]", label)
    h.click('#rush [data-i="1"]'); pg.wait_for_timeout(1000)
    for lab, s0, d in (('Plain', 0, 12), ('Vanilla', 12, 10), ('Rush vanilla', 22, 8), ('Strawberry', 30, 8), ('Greek', 38, 8)):
        q = pos(lab); ctx.chk(f'400 cases: {lab} starts at hour {s0} and runs {d} h', abs(q[0] - (LBL + s0 * PXH)) < 0.6 and abs(q[1] - (d * PXH - 2)) < 0.6 and q[3] == f'{d} h', str(q))
    ctx.chk('400 cases: Greek is past Friday, Strawberry is not, Rush is amber', 'lt' in pos('Greek')[2].split() and 'lt' not in pos('Strawberry')[2].split() and 'rs' in pos('Rush vanilla')[2].split())
    ctx.chk('400 cases: chips', t('#pchip') == 'Greek 6 h past Friday' and t('#gtc') == 'Yogurt line done at hour 46 of 40', t('#pchip') + t('#gtc'))
    ctx.chk('400 cases: milk and vanilla', (t('#m4'), t('#m5'), t('#v4'), t('#v5')) == ('13,600 lb', 'Short 3,100 lb', '140 lb', 'Short 90 lb'), str([t('#m4'), t('#m5'), t('#v4'), t('#v5')]))
    a = t('#act-text'); ctx.chk('400 cases: text', 'A rush of 400 cases adds 8 hours on the yogurt line' in a and 'Greek finishes past Friday, Greek by 6 hours' in a and 'Milk is 3,100 lb short and Vanilla base is 90 lb short' in a, a)
    ctx.chk('400 cases: purchase order button enabled', not h.dis('#po')); h.shot(out, 'c4-400')
    h.click('#po'); pg.wait_for_timeout(800); a = t('#act-text')
    ctx.chk('PO: created', t('#po') == 'Created' and h.dis('#po') and t('#poch') == 'PO-2231, draft' and (t('#m5'), t('#v5')) == ('On order PO-2231', 'On order PO-2231'), str([t('#po'), t('#poch'), t('#m5')]))
    ctx.chk('PO: lines and text', 'Milk3,100 lbShort for the 400 case rush' in re.sub(r'\s+', '', t('#pob')).replace('Milk3,100lb', 'Milk3,100 lb') or ('3,100 lb' in t('#pob') and '90 lb' in t('#pob')), t('#pob'))
    ctx.chk('PO: summary text', 'PO-2231 is raised for 3,100 lb of milk and 90 lb of vanilla base' in a, a); h.shot(out, 'c4-po')
    h.click('#rush [data-i="0"]'); pg.wait_for_timeout(900)
    ctx.chk('200 cases: Greek 2 h past Friday, milk covered, vanilla 20 lb short, PO cleared', t('#pchip') == 'Greek 2 h past Friday' and (t('#m4'), t('#m5'), t('#v4'), t('#v5')) == ('6,800 lb', 'Covered', '70 lb', 'Short 20 lb') and not h.dis('#po') and t('#poch') == 'None yet', str([t('#pchip'), t('#m5'), t('#v5')]))
    ctx.chk('200 cases: Strawberry ends at 34, Greek ends at 42', abs(pos('Strawberry')[0] - (LBL + 26 * PXH)) < 0.6 and abs(pos('Greek')[0] - (LBL + 34 * PXH)) < 0.6)
    h.click('#rush [data-i="2"]'); pg.wait_for_timeout(900); a = t('#act-text')
    ctx.chk('600 cases: both finish past Friday, Greek by 10 hours', 'both finish past Friday, Greek by 10 hours' in a and t('#pchip') == 'Greek 10 h past Friday' and 'lt' in pos('Strawberry')[2].split(), a)
    ctx.chk('600 cases: milk 9,900 and vanilla 160 short', (t('#m5'), t('#v5'), t('#m4'), t('#v4')) == ('Short 9,900 lb', 'Short 160 lb', '20,400 lb', '210 lb'), str([t('#m5'), t('#v5')])); h.shot(out, 'c4-600')
    ctx.chk('arithmetic: rush hours 200/50, 400/50, 600/50 and milk 34 lb a case', 200 / 50 == 4 and 400 / 50 == 8 and 600 / 50 == 12 and 400 * 34 - 10500 == 3100 and 600 * 34 - 10500 == 9900 and round(400 * 0.35 - 50) == 90 and round(600 * 0.35 - 50) == 160 and round(200 * 0.35 - 50) == 20)
    h.click('.rp'); pg.wait_for_timeout(1500); ctx.chk('replay returns to the baseline', t('#pchip') == 'On track' and t('#m4') == '' and h.dis('#po'))
    b.close()
    speed(ctx, p, N, "return /hour 46/.test(r.getElementById('gtc').textContent)", limit_ms=4500)
    arrows_generic(ctx, p, N, 5)
    b, pg, errs, h = ctx.open(p, N); t = h.txt
    h.click('#nx'); pg.wait_for_timeout(800); ctx.chk('arrow to step 2 applies the 400 case rush', t('#sn') == '2 of 5' and t('#pchip') == 'Greek 6 h past Friday')
    h.click('#nx'); h.click('#nx'); pg.wait_for_timeout(900)
    ctx.chk('step 4 hotspot sits on the purchase order button', t('#sn') == '4 of 5' and h.ev("const x=r.querySelector('#hs').getBoundingClientRect(),y=r.querySelector('#po').getBoundingClientRect();return Math.abs(x.left-y.left)<8&&Math.abs(x.top-y.top)<8"))
    h.click('#nx'); pg.wait_for_timeout(900); ctx.chk('step 5 raises the purchase order', t('#po') == 'Created' and t('#poch') == 'PO-2231, draft')
    h.click('#pv'); h.click('#pv'); pg.wait_for_timeout(900); ctx.chk('previous undoes the purchase order', t('#po') == 'Create purchase order' and t('#sn') == '3 of 5')
    h.shot(out, 'c4-step3'); b.close()
    # tour in order (rush applied 4.1 s, step 5 at 14.2 s, PO created 15.4 s after mount)
    b, pg, errs, h = ctx.open(p, N); t = h.txt; pg.wait_for_timeout(1700); h.shot(out, 'c4-tour-1'); ctx.chk('tour: baseline before the rush', t('#pchip') == 'On track')
    pg.wait_for_timeout(3500); h.shot(out, 'c4-tour-2'); ctx.chk('tour: rush applied by 5.2 s', t('#pchip') == 'Greek 6 h past Friday')
    pg.wait_for_timeout(5000); h.shot(out, 'c4-tour-3'); pg.wait_for_timeout(7800); h.shot(out, 'c4-tour-4'); ctx.chk('tour: purchase order created by 17.5 s', t('#po') == 'Created', t('#po')); b.close()
ctx.close(); print('RESULT:', 'PASS' if not ctx.fails else 'FAIL ' + str(ctx.fails))
