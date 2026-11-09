"""Recycling test setup.

Points the shared harness (tools/electronics/testlib.py) at graphics/recycling, adds the recycling banned words, and adds
the checks that are new for these cards:
  * layout: under 520 px of card width the card is a phone stage, so the window sits inside the card instead of running
    past its edges (testlib.layout_checks is replaced with a version that knows both);
  * variety: each card's storyboard (card N's STORY) passes the rules in variety_check.py;
  * navigation walk, at 1300 px and at 390 px: after every step the screen, breadcrumb and active nav item match the
    storyboard, navigation steps change all three, and at 390 px every target sits inside the card and the phone
    window, captions are one line, the bottom nav shows, and nothing overflows sideways.
"""
import importlib, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(HERE), 'electronics'))
sys.path.insert(0, HERE)
import testlib  # noqa: E402
import variety_check  # noqa: E402
from playwright.sync_api import sync_playwright  # noqa: E402

testlib.KEY = 'recycling'
testlib.SHOTS = os.environ.get('GFX_SHOTS', '/tmp/recycling_shots')
os.makedirs(testlib.SHOTS, exist_ok=True)
# claim words from the brief, scale makers, real recyclers and buyers (case sensitive where plain words could collide)
testlib.EXTRA_CLAIMS = re.compile(
    r'\bEPA\b|\bDOT\b|(?i:compliance|compliant|hazardous|hazmat|\bcash\b|ID scan|seller ID|theft|market price|commodity price|certified|regulat|setup in)'
    r'|\$\d|Mettler|Toledo|Fairbanks|Avery|Rice Lake|Cardinal Scale|Walmart|Waste Management|Republic Services|Digit')
js, pill = testlib.js, testlib.pill
_orig_layout = testlib.layout_checks


def layout_checks(f, pg, n, label):
    if not js(pg, "return r.querySelector('.shot').classList.contains('ph')"):
        return _orig_layout(f, pg, n, label)
    d = js(pg, '''var cv=document.getElementById('cv').getBoundingClientRect(),w=r.querySelector('.fwin').getBoundingClientRect(),p=r.getElementById('pg'),s=r.querySelector('.stp').getBoundingClientRect();
return {in_:w.left>=cv.left&&w.right<=cv.right+0.5&&w.bottom<=cv.bottom,ratio:cv.height/cv.width,cw:cv.width,ov:p.scrollWidth-p.clientWidth,stp:s.bottom<=cv.bottom&&s.top>=w.bottom-2,bn:getComputedStyle(r.querySelector('.bn')).display,rail:getComputedStyle(r.querySelector('.rail')).display};''')
    want = 1.0 if d['cw'] <= 400 else 1 - 0.12 * (d['cw'] - 400) / 120
    f.check(d['in_'], '%s phone: the window sits inside the card' % label)
    f.check(abs(d['ratio'] - want) < 0.02, '%s phone: stage height %.2f of its width (want %.2f)' % (label, d['ratio'], want))
    f.check(d['ov'] <= 0, '%s phone: nothing overflows sideways' % label)
    f.check(d['stp'], '%s phone: step arrows in the strip under the window' % label)
    f.check(d['bn'] == 'flex' and d['rail'] == 'none', '%s phone: bottom nav replaces the side nav' % label)


testlib.layout_checks = layout_checks


def variety(n, f):
    m = importlib.import_module('card%d' % n)
    head = ['#', 'screen', 'target type', 'position']
    rows = [[str(i + 1), s, t, p] for i, (s, _, t, p) in enumerate(m.STORY)]
    probs = variety_check.check('card %d' % n, head, rows)
    f.check(not probs, 'variety: %d steps, %d screens, %d target types, %d positions %s' % (
        len(rows), len({r[1] for r in rows}), len({r[2] for r in rows}), len({r[3] for r in rows}), probs or ''))
    f.check(len(m.STORY) == m.STEPS, 'variety: the storyboard has one row per step')
    return m.STORY


def state(pg):
    return js(pg, "var w=r.querySelector('.fwin'),a=r.querySelector('.ni.on,.bi.on');return {scr:w.getAttribute('data-scr'),mod:w.getAttribute('data-mod'),bc:r.getElementById('bc').textContent,nav:a&&a.getAttribute('data-m')}")


def nav_walk(n, story, f, vw, cw, label, extra=None):
    """Try it through every step, checking screen, breadcrumb and nav after each, and the phone rules when narrow."""
    with sync_playwright() as p:
        b = testlib.browser(p)
        pg, errs = testlib.open_card(b, n, vw, cw)
        pg.locator('#cv').scroll_into_view_if_needed()
        pg.locator('#cv .mtg [data-m="try"]').click()
        phone = js(pg, "return r.querySelector('.shot').classList.contains('ph')")
        prev = state(pg)
        seen = {prev['scr']}
        for i, (scr, mod, typ, pos) in enumerate(story):
            pg.wait_for_timeout(1600)
            if phone:
                t = js(pg, '''var cv=document.getElementById('cv').getBoundingClientRect(),w=r.querySelector('.fwin').getBoundingClientRect(),h=r.querySelector('.hint');if(!h)return null;var b=h.getBoundingClientRect();
return b.width>0&&b.left>=cv.left-1&&b.right<=cv.right+1&&b.top>=Math.max(cv.top,w.top)-1&&b.bottom<=Math.min(cv.bottom,w.bottom)+1;''')
                f.check(t, '%s step %d: the target is inside the phone window' % (label, i + 1))
            if extra and i in extra:
                extra[i](pg, f)
            pg.locator('#cv .hint').first.click()
            pg.wait_for_timeout(700)
            st = state(pg)
            seen.add(st['scr'])
            f.check(scr in (prev['scr'], st['scr']), '%s step %d: on screen "%s" (%s to %s)' % (label, i + 1, scr, prev['scr'], st['scr']))
            f.check(mod in (prev['mod'], st['mod']) and st['nav'] == st['mod'], '%s step %d: module %s, active nav item follows (%s)' % (label, i + 1, mod, st['nav']))
            if typ in ('nav item', 'breadcrumb'):
                f.check(st['mod'] != prev['mod'] and st['bc'] != prev['bc'] and st['scr'] != prev['scr'], '%s step %d: navigation changes the screen, breadcrumb and nav' % (label, i + 1))
            elif st['scr'] != prev['scr'] and not phone:
                f.check(st['bc'] != prev['bc'], '%s step %d: a new screen moves the breadcrumb' % (label, i + 1))
            if phone:
                c = js(pg, '''var c=r.querySelector('.cap:not(.turn)'),m=c.querySelector('.m'),cv=document.getElementById('cv').getBoundingClientRect(),b=c.getBoundingClientRect(),p=r.getElementById('pg');
return {one:m.scrollHeight<=m.clientHeight+1&&m.getBoundingClientRect().height<30,sub:!!c.querySelector('.s')&&getComputedStyle(c.querySelector('.s')).display!=='none',full:m.scrollWidth<=m.clientWidth+1,in_:b.left>=cv.left-1&&b.right<=cv.right+1&&b.bottom<=cv.bottom+1,ov:p.scrollWidth-p.clientWidth,vo:Math.max(p.scrollHeight-p.clientHeight,[].reduce.call(p.querySelectorAll('.cd,.doc,.prc,.wbox'),function(m,e){return Math.max(m,e.scrollHeight-e.clientHeight);},0))}''')
                f.check(c['one'] and not c['sub'], '%s step %d: caption is one line with no subtext' % (label, i + 1))
                f.check(c['full'], '%s step %d: the caption fits without being cut' % (label, i + 1))
                f.check(c['in_'], '%s step %d: caption inside the card' % (label, i + 1))
                f.check(c['ov'] <= 0, '%s step %d: nothing overflows sideways' % (label, i + 1))
                f.check(c['vo'] <= 1, '%s step %d: nothing cut off at the bottom (%dpx over)' % (label, i + 1, c['vo']))
            testlib.shot(pg, 'card%d_%s_%d.png' % (n, label.replace(' ', ''), i + 1))
            prev = st
        f.check({x[0] for x in story} <= seen, '%s: visits every storyboard screen' % label)
        f.check('Done' in pill(pg), '%s: reaches Done' % label)
        f.check(not errs, '%s: no page errors %s' % (label, errs[:2]))
        pg.close()
        b.close()


def run_all(n, plan, numbers, extra=None, drag=None):
    f = testlib.run_card(n, plan, numbers, extra=extra)
    story = variety(n, f)
    nav_walk(n, story, f, 1300, 604, 'desktop')
    nav_walk(n, story, f, 390, 358, 'phone 390')
    nav_walk(n, story, f, 1024, 480, 'phone 480')
    if drag:
        drag(f)
    return f
