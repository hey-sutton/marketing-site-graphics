"""Distilleries test setup (adapted from tools/footwear/footwear_tests.py).

Points the shared harness (tools/electronics/testlib.py) at graphics/footwear, adds the footwear banned words, and adds
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
sys.path.insert(1, os.path.join(os.path.dirname(HERE), 'footwear'))
import testlib  # noqa: E402
import variety_check  # noqa: E402
from playwright.sync_api import sync_playwright  # noqa: E402

testlib.KEY = 'distilleries'
testlib.SHOTS = os.environ.get('GFX_SHOTS', '/tmp/distilleries_shots')
os.makedirs(testlib.SHOTS, exist_ok=True)
# brief rules: no market size words, no concept or illustrative tags, no plan wording, no real distilleries,
# spirits brands, distributors or retailers, Sutton not Digit
testlib.EXTRA_CLAIMS = re.compile(
    r'(?i:\bsmall\b|mid ?size|enterprise|\blarge\b|startup|concept screen|live demo|live product demo|illustrative|compliance|compliant|certified|guarantee|\bplan\b|\btier\b|TTB)'
    r'|Jack Daniel|Jim Beam|Maker.s Mark|Buffalo Trace|Wild Turkey|Woodford|Bulleit|Tito|Hendrick|Tanqueray|Bombay|Beefeater|Diageo|Pernod|Brown.Forman|Southern Glazer|Republic National|Breakthru|Total Wine|BevMo|Drizly|Digit')
js, pill = testlib.js, testlib.pill
_orig_layout = testlib.layout_checks


def layout_checks(f, pg, n, label):
    if not js(pg, "return r.querySelector('.shot').classList.contains('ph')"):
        return _orig_layout(f, pg, n, label)
    d = js(pg, '''var cv=document.getElementById('cv').getBoundingClientRect(),w=r.querySelector('.fwin').getBoundingClientRect(),p=r.getElementById('pg');
return {in_:w.left>=cv.left&&w.right<=cv.right+0.5&&w.bottom<=cv.bottom,ratio:cv.height/cv.width,cw:cv.width,ov:p.scrollWidth-p.clientWidth,gap:cv.bottom-w.bottom,bn:getComputedStyle(r.querySelector('.bn')).display,rail:getComputedStyle(r.querySelector('.rail')).display,tap:[].map.call(r.querySelectorAll('.studio-chip,.mtg button,.tbar .rp'),function(b){return Math.round(b.getBoundingClientRect().height)})};''')
    want = 1.0 if d['cw'] <= 400 else 1 - 0.12 * (d['cw'] - 400) / 120
    f.check(d['in_'], '%s phone: the window sits inside the card' % label)
    f.check(abs(d['ratio'] - want) < 0.02, '%s phone: stage height %.2f of its width (want %.2f)' % (label, d['ratio'], want))
    f.check(d['ov'] <= 0, '%s phone: nothing overflows sideways' % label)
    f.check(d['gap'] < 16, '%s phone: only a slim strip of photo under the window (%.0f px)' % (label, d['gap']))
    f.check(min(d['tap']) >= 39, '%s phone: controls are 40 px tap targets %s' % (label, d['tap']))
    f.check(d['bn'] == 'none' and d['rail'] == 'none', '%s phone: no side nav and no bottom bar' % label)


testlib.layout_checks = layout_checks

# The distilleries cards hide the step arrows and the status pill (November 24, 2026). The shared run_card clicks the
# arrows and checks they sit inside shorter cards, so those two blocks are swapped for checks that both stay hidden.
# The pill keeps its text for the screen reader free checks below (pill() reads textContent, which display:none keeps).
import inspect, textwrap  # noqa: E402
_src = textwrap.dedent(inspect.getsource(testlib.run_card))
_a, _b = _src.index('        # arrows jump to a step'), _src.index('        # Replay in Try it restarts Try it')
_src = _src[:_a] + """        hid = js(pg, "var s=r.querySelector('.stp'),m=r.querySelector('.tbar .mode');return getComputedStyle(s).display==='none'&&getComputedStyle(m).display==='none'")
        f.check(hid, 'the step arrows and the status pill are hidden')
""" + _src[_b:]
_a, _b = _src.index('        # step arrows stay inside shorter cards'), _src.index('        # Studio fits at 340')
_src = _src[:_a] + _src[_b:]
_src = _src.replace("f.check(js(pg, \"return getComputedStyle(r.querySelector('.tbar .mode')).visibility\") == 'hidden', 'pill hides while the popover is open')", "pass")
_src = _src.replace("        f.check(js(pg, \"return getComputedStyle(r.querySelector('.tbar .mode .mc')).display\") == 'none', '340 px: pill hides n of N')\n", "")
_ns = dict(vars(testlib))
exec(compile(_src, testlib.__file__, 'exec'), _ns)
testlib.run_card = _ns['run_card']


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


def timing(n, f, start=None):
    """The walkthrough starts within 1.5 s of the card coming into view and the first result is up by 4 s.
    start(pg, f) checks the start screen (nothing that depends on the input before it is typed or picked)."""
    with sync_playwright() as p:
        b = testlib.browser(p)
        pg, errs = testlib.open_card(b, n, 1300, 604)
        if start:
            start(pg, f)
        t0 = pg.evaluate('performance.now()')
        pg.locator('#cv').scroll_into_view_if_needed()
        pg.wait_for_function("()=>{const h=document.querySelector('#cv [data-sxg-host]');return h.shadowRoot.querySelector('.fw-ghost.on')}", timeout=5000)
        t1 = pg.evaluate('performance.now()') - t0
        f.check(t1 < 1500, 'timing: the walkthrough starts %.0f ms after the card comes into view (under 1,500)' % t1)
        pg.wait_for_function("()=>{const h=document.querySelector('#cv [data-sxg-host]');return h.shadowRoot.querySelector('.cap.on')}", timeout=8000)
        t2 = pg.evaluate('performance.now()') - t0
        f.check(t2 < 4000, 'timing: the first result and caption are up %.0f ms after the card comes into view (under 4,000)' % t2)
        f.check(not errs, 'timing: no page errors %s' % errs[:2])
        pg.close()
        b.close()


def run_all(n, plan, numbers, extra=None, drag=None, start=None):
    f = testlib.run_card(n, plan, numbers, extra=extra)
    story = variety(n, f)
    timing(n, f, start)
    nav_walk(n, story, f, 1300, 604, 'desktop')
    nav_walk(n, story, f, 768, 604, 'tablet 768')
    nav_walk(n, story, f, 390, 358, 'phone 390')
    nav_walk(n, story, f, 1024, 480, 'phone 480')
    nav_walk(n, story, f, 372, 340, 'phone 340')
    if drag:
        drag(f)
    return f
