"""Textile test harness (a copy of tools/automotive/auto_tests.py with the textile key and word list), on top of the shared one in tools/electronics/testlib.py.

run_all(n, plan, numbers, ...) runs, for card n:
  * testlib-style click through: Watch through every step, the take over, Try it with a wrong click, every step's
    caption and screen text, the arrows, Replay, the toggle, the Studio popover, reduced motion, layout at 1300, 1024,
    768 and 390 px (window past the right and bottom edges, square corner, no empty band), short card shapes, a text
    scan and the card size;
  * the November 11, 2026 control row rules at card widths 604, 480, 390, 358 and 340: order Studio, toggle, step
    counter, Replay; two lines under 600 px (Studio and Replay on line 1, toggle and counter on line 2); every control
    inside the card, uncovered, at least 40 CSS px under 600 px, and working by touch (the popover opens on tap);
    Replay is an icon only with aria-label and title "Replay";
  * no side nav and no profile; the header has the icon, title and subtitle;
  * the start screen (start(pg, f)) and timing: walkthrough within 1.5 s, first result within 4 s;
  * every step at 390 and 340 px card widths: prompt and caption inside the card.
Run a card test with PW_CHROME set to a Chromium binary if Playwright's own browser is missing.
"""
import os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(HERE), 'electronics'))
import testlib  # noqa: E402
sys.path.insert(0, HERE)
import data  # noqa: E402,F401  (asserts the shared numbers)
from playwright.sync_api import sync_playwright  # noqa: E402

testlib.KEY = 'textile'
testlib.SHOTS = os.environ.get('GFX_SHOTS', '/tmp/textile_shots')
os.makedirs(testlib.SHOTS, exist_ok=True)
# no Sutton price, plan or trial words, no market size words, no concept or illustrative tags, no compliance claims,
# no real mill, brand or supplier names
testlib.EXTRA_CLAIMS = re.compile(
    r'(?i:\bpricing\b|\bprice plan|\byour plan\b|\bpaid plan|\bplan tier|\bper month\b|/mo\b|free trial|\btrial\b|subscription|\bsmall\b|mid ?size|enterprise|\blarge\b|startup|concept screen|live product demo|illustrative|compliance|compliant|certified|OEKO|GOTS|bluesign)'
    r'|\b(?:Milliken|Burlington|Unifi|Parkdale|Avondale|Mohawk|Shaw|Culp|Levi|Gap|Nike|Inditex|Zara|Digit)\b')
js, pill, shot = testlib.js, testlib.pill, testlib.shot

CTRL = '''var cv=document.getElementById('cv').getBoundingClientRect();
function box(e){if(!e)return null;var b=e.getBoundingClientRect(),cs=getComputedStyle(e);return {l:b.left,t:b.top,r:b.right,b:b.bottom,w:b.width,h:b.height,vis:cs.visibility!=='hidden'&&cs.display!=='none'&&b.width>0};}
var c={studio:box(r.querySelector('.studio-chip')),watch:box(r.querySelector('.mtg [data-m="watch"]')),tryit:box(r.querySelector('.mtg [data-m="try"]')),
pv:box(r.getElementById('pv')),counter:box(r.querySelector('.tbar .mode')),nx:box(r.getElementById('nx')),replay:box(r.querySelector('.tbar .rp'))};
var cover={};['studio','watch','tryit','pv','nx','replay'].forEach(function(k){var b=c[k];if(!b||!b.vis){cover[k]=false;return;}var el=r.elementFromPoint(b.l+b.w/2,b.t+b.h/2),want=k==='studio'?r.querySelector('.studio-chip'):k==='watch'?r.querySelector('.mtg [data-m="watch"]'):k==='tryit'?r.querySelector('.mtg [data-m="try"]'):k==='replay'?r.querySelector('.tbar .rp'):r.getElementById(k);cover[k]=!!el&&(el===want||want.contains(el));});
var rp=r.querySelector('.tbar .rp');
return {cv:{l:cv.left,t:cv.top,r:cv.right,b:cv.bottom,w:cv.width},c:c,cover:cover,rpText:rp.innerText.trim(),rpAria:rp.getAttribute('aria-label'),rpTitle:rp.getAttribute('title'),
inBar:r.getElementById('pv').closest('.tbar')!==null,shell:r.querySelectorAll('[data-shell],.rail,.bn').length,
hd:!!r.querySelector('.fwin>.hd .hi svg')&&!!r.querySelector('.fwin>.hd .tt')&&!!r.querySelector('.fwin>.hd .sb')};'''


def overlap(a, b):
    return min(a['r'], b['r']) - max(a['l'], b['l']) > 0.5 and min(a['b'], b['b']) - max(a['t'], b['t']) > 0.5


def control_checks(f, pg, label, cw):
    d = js(pg, CTRL)
    c, cv = d['c'], d['cv']
    two = cw < 600
    f.check(d['rpText'] == '' and d['rpAria'] == 'Replay' and d['rpTitle'] == 'Replay', '%s: Replay is an icon with aria-label and title "Replay"' % label)
    f.check(d['shell'] == 0, '%s: no side nav and no profile' % label)
    f.check(d['hd'], '%s: header has the icon, title and subtitle' % label)
    keys = ['studio', 'watch', 'tryit', 'pv', 'counter', 'nx', 'replay'] if two else ['studio', 'watch', 'tryit', 'counter', 'replay']
    for k in keys:
        b = c[k]
        f.check(b and b['vis'] and b['l'] >= cv['l'] - 0.5 and b['r'] <= cv['r'] + 0.5 and b['t'] >= cv['t'] - 0.5 and b['b'] <= cv['b'] + 0.5, '%s: %s visible inside the card' % (label, k))
    for k in [x for x in keys if x != 'counter']:
        f.check(d['cover'][k], '%s: %s is not covered' % (label, k))
    for i, a in enumerate(keys):
        for b in keys[i + 1:]:
            f.check(not overlap(c[a], c[b]), '%s: %s and %s do not overlap' % (label, a, b))
    if two:
        f.check(d['inBar'], '%s: step arrows sit in the control row' % label)
        for k in ['studio', 'watch', 'tryit', 'pv', 'nx', 'replay']:
            f.check(c[k]['w'] >= 40 - 0.5 and c[k]['h'] >= 40 - 0.5, '%s: %s at least 40 by 40 CSS px (%.0f by %.0f)' % (label, k, c[k]['w'], c[k]['h']))
        l1 = abs(c['studio']['t'] - c['replay']['t']) < 2
        l2 = len({round(c[k]['t']) for k in ['watch', 'pv', 'counter', 'nx']}) == 1
        f.check(l1 and l2 and c['watch']['t'] >= c['studio']['b'], '%s: line 1 Studio and Replay, line 2 toggle and counter' % label)
        f.check(c['studio']['r'] < c['replay']['l'] and c['watch']['r'] <= c['tryit']['l'] + 0.5 and c['tryit']['r'] < c['pv']['l'] and c['pv']['r'] < c['counter']['l'] and c['counter']['r'] < c['nx']['l'], '%s: order Studio, toggle, counter, Replay' % label)
        win_top = js(pg, "return r.querySelector('.fwin').getBoundingClientRect().top")
        f.check(win_top >= c['watch']['b'] + 2, '%s: the window starts below the control row' % label)
    else:
        same = len({round(c[k]['t'] + c[k]['h'] / 2) for k in keys}) <= 2
        f.check(same and c['studio']['r'] < c['watch']['l'] and c['tryit']['r'] < c['counter']['l'] and c['counter']['r'] < c['replay']['l'], '%s: one row in order Studio, toggle, counter, Replay' % label)
    return d


def touch_popover(f, b, n, cw):
    ctx = b.new_context(viewport={'width': max(cw + 32, 360), 'height': 900}, has_touch=True, is_mobile=True)
    pg = ctx.new_page()
    pg.goto(testlib.page_url(n, cw))
    pg.wait_for_selector('#cv [data-sxg-host]', state='attached', timeout=8000)
    pg.locator('#cv').scroll_into_view_if_needed()
    pg.wait_for_timeout(400)
    pg.locator('#cv .studio-chip').tap()
    pg.wait_for_timeout(600)
    f.check(pg.locator('#cv .studio.open').count() == 1, '%d px touch: tapping Studio opens the popover' % cw)
    ok = js(pg, "var cv=document.getElementById('cv').getBoundingClientRect(),p=r.querySelector('.pop').getBoundingClientRect();return p.left>=cv.left-0.5&&p.right<=cv.right+0.5&&p.top>=cv.top&&p.bottom<=cv.bottom+0.5")
    f.check(ok, '%d px touch: the popover fits inside the card' % cw)
    f.check(pg.locator('#cv .pop .examples li').count() == 4 and pg.locator('#cv .pop .examples').is_visible() and pg.locator('#cv .pop .rows').is_visible(), '%d px touch: the popover shows the four examples and the rows' % cw)
    shot(pg, 'card%d_%d_touch_studio.png' % (n, cw))
    pg.locator('#cv .studio-chip').tap()
    pg.wait_for_timeout(500)
    f.check(pg.locator('#cv .studio.open').count() == 0, '%d px touch: tapping Studio again closes it' % cw)
    m0 = pill(pg)
    pg.locator('#cv .mtg [data-m="try"]').tap()
    pg.wait_for_timeout(400)
    f.check('Your turn1 of' in pill(pg), '%d px touch: tapping Try it starts Try it (%s)' % (cw, pill(pg)))
    pg.locator('#cv #nx').tap()
    pg.wait_for_timeout(400)
    f.check('Your turn2 of' in pill(pg), '%d px touch: tapping next moves to step 2' % cw)
    pg.locator('#cv #pv').tap()
    pg.wait_for_timeout(400)
    f.check('Your turn1 of' in pill(pg), '%d px touch: tapping previous moves back to step 1' % cw)
    pg.locator('#cv .tbar .rp').tap()
    pg.wait_for_timeout(400)
    f.check('Your turn1 of' in pill(pg), '%d px touch: tapping Replay restarts' % cw)
    ctx.close()


def fill_sample(pg):
    if pg.locator('#cv [data-sample]').count():
        pg.locator('#cv [data-sample]').first.click()
        pg.wait_for_timeout(150)


def run_card(n, plan, numbers, extra=None, start=None):
    f = testlib.Fail()
    N = len(plan)
    with sync_playwright() as p:
        b = testlib.browser(p)
        # start screen and timing
        pg, errs = testlib.open_card(b, n, 1300)
        if start:
            start(pg, f)
        shot(pg, 'card%d_start.png' % n)
        t0 = pg.evaluate('performance.now()')
        pg.locator('#cv').scroll_into_view_if_needed()
        pg.wait_for_function("()=>{const h=document.querySelector('#cv [data-sxg-host]');return h.shadowRoot.querySelector('.fw-ghost.on')}", timeout=5000)
        t1 = pg.evaluate('performance.now()') - t0
        f.check(t1 < 1500, 'timing: walkthrough starts %.0f ms after the card is visible (under 1,500)' % t1)
        pg.wait_for_function("()=>{const h=document.querySelector('#cv [data-sxg-host]');return h.shadowRoot.querySelector('.cap.on')}", timeout=8000)
        t2 = pg.evaluate('performance.now()') - t0
        f.check(t2 < 4000, 'timing: first result and caption up %.0f ms after the card is visible (under 4,000)' % t2)
        # Watch through every step
        seen = set()
        for i in range(N):
            testlib.wait_pill(pg, 'Watching%d of %d' % (i + 1, N), 9000)
            seen.add(i + 1)
            pg.wait_for_timeout(1500)
            shot(pg, 'card%d_watch_%d.png' % (n, i + 1))
        f.check(len(seen) == N, 'watch: ran all %d steps' % N)
        f.check(plan[-1][1] in testlib.win_text(pg), 'watch: final screen shows "%s"' % plan[-1][1])
        testlib.wait_pill(pg, 'Watching1 of %d' % N, 12000)
        f.check(True, 'watch: loops back to step 1')
        # take over
        pg.locator('#cv .fwin .hd').click(position={'x': 40, 'y': 20})
        pg.wait_for_timeout(500)
        f.check('Your turn1 of %d' % N in pill(pg), 'try: a click inside takes over and restarts (%s)' % pill(pg))
        f.check(pg.locator('#cv .fw-ghost.on').count() == 0, 'try: ghost cursor gone')
        for i, (label, must) in enumerate(plan):
            pg.wait_for_timeout(1700)
            hints = pg.locator('#cv .hint')
            f.check(hints.count() == 1, 'step %d: one pulsing target' % (i + 1))
            f.check(pg.locator('#cv .hs.on').count() == 1, 'step %d: ripple hotspot on the target' % (i + 1))
            f.check(('Your turn%d of %d' % (i + 1, N)) in pill(pg), 'step %d: pill Your turn %d of %d' % (i + 1, i + 1, N))
            ins = js(pg, "var cv=document.getElementById('cv').getBoundingClientRect(),t=r.querySelector('.cap.turn').getBoundingClientRect();return t.left>=cv.left-1&&t.right<=cv.right+1&&t.top>=cv.top-1&&t.bottom<=cv.bottom+1;")
            f.check(ins, 'step %d: prompt inside the card' % (i + 1))
            if i == 0:
                pg.locator('#cv .fwin .hd .tt').click()
                pg.wait_for_timeout(300)
                f.check(('Your turn1 of %d' % N) in pill(pg) and hints.count() == 1, 'step 1: a wrong click re-shows the prompt')
            if extra and i in extra.get('before', {}):
                extra['before'][i](pg, f)
            hints.first.click()
            pg.wait_for_timeout(700)
            c = testlib.cap_text(pg)
            f.check(label in c, 'step %d caption: %s' % (i + 1, c.replace('\n', ' ')[:90]))
            f.check(must in testlib.win_text(pg), 'step %d screen shows "%s"' % (i + 1, must))
            if extra and i in extra.get('after_step', {}):
                extra['after_step'][i](pg, f)
            shot(pg, 'card%d_try_%d.png' % (n, i + 1))
        pg.wait_for_timeout(400)
        f.check('Done' in pill(pg), 'try: ends on Done (%s)' % pill(pg))
        txt = testlib.win_text(pg)
        for s in numbers:
            f.check(s in txt, 'final screen shows %s' % s)
        if extra and 'after' in extra:
            extra['after'](pg, f)
        # arrows, Replay, toggle
        pg.locator('#cv #pv').click(); pg.wait_for_timeout(500)
        f.check(('Your turn%d of %d' % (N, N)) in pill(pg), 'arrows: previous jumps to step %d' % N)
        pg.locator('#cv #pv').click(); pg.wait_for_timeout(500)
        f.check(('Your turn%d of %d' % (N - 1, N)) in pill(pg), 'arrows: previous again to step %d' % (N - 1))
        pg.locator('#cv #nx').click(); pg.wait_for_timeout(500)
        f.check(('Your turn%d of %d' % (N, N)) in pill(pg), 'arrows: next to step %d' % N)
        pg.locator('#cv .tbar .rp').click(); pg.wait_for_timeout(400)
        f.check(('Your turn1 of %d' % N) in pill(pg), 'Replay restarts Try it at step 1')
        if start:
            start(pg, f, 'after Replay')
        pg.locator('#cv .mtg [data-m="watch"]').click(); pg.wait_for_timeout(600)
        f.check('Watching' in pill(pg), 'toggle: Watch restarts Watch')
        pg.wait_for_timeout(1500)
        pg.locator('#cv .mtg [data-m="try"]').click(); pg.wait_for_timeout(400)
        f.check(('Your turn1 of %d' % N) in pill(pg), 'toggle: Try it restarts at step 1')
        pg.locator('#cv .studio-chip').click(); pg.wait_for_timeout(600)
        f.check(pg.locator('#cv .studio.open').count() == 1, 'Studio popover opens')
        pt = pg.locator('#cv .pop').inner_text()
        f.check(all(w in pt for w in ('Built on', 'Change', 'Get help', 'See what you can build in Studio')) and pg.locator('#cv .pop .examples li').count() == 4, 'Studio popover: four examples, Built on, Change, Get help and the Studio link')
        pg.keyboard.press('Escape'); pg.wait_for_timeout(400)
        f.check(pg.locator('#cv .studio.open').count() == 0, 'Studio popover closes')
        testlib.text_scan(f, testlib.visible_text(pg) + ' | ' + pt, 'text')
        f.check(not errs, 'no page errors %s' % errs[:2])
        pg.close()
        # layout and control row at several widths
        for vw, cw in ((1300, 604), (1024, 480), (768, 604), (390, 358), (372, 340)):
            pg, errs = testlib.open_card(b, n, vw, cw)
            pg.locator('#cv').scroll_into_view_if_needed()
            pg.wait_for_timeout(250)
            testlib.layout_checks(f, pg, n, '%d px' % vw)
            control_checks(f, pg, '%d px card %d' % (vw, cw), cw)
            shot(pg, 'card%d_layout_%d.png' % (n, cw))
            pg.close()
        for vw, cw, ar in ((1500, 604, '604/523'), (1300, 584, '584/460'), (1300, 700, '700/430')):
            pg, errs = testlib.open_card(b, n, vw, cw)
            pg.evaluate("a=>{document.getElementById('cv').style.aspectRatio=a}", ar)
            pg.locator('#cv').scroll_into_view_if_needed()
            pg.wait_for_timeout(300)
            ok = js(pg, "var cv=document.getElementById('cv').getBoundingClientRect();return [r.getElementById('pv'),r.getElementById('nx')].every(function(e){var s=e.getBoundingClientRect();return s.width>0&&s.bottom<=cv.bottom-4&&s.top>=cv.top&&s.right<=cv.right&&s.left>=cv.left;})")
            f.check(ok, 'card %s: step arrows inside the card' % ar)
            pg.close()
        for cw in (390, 340):
            touch_popover(f, b, n, cw)
        # every step at 390 and 340 px card widths
        for vw, cw in ((430, 390), (372, 340)):
            pg, errs = testlib.open_card(b, n, vw, cw)
            pg.locator('#cv').scroll_into_view_if_needed()
            pg.locator('#cv .mtg [data-m="try"]').click()
            for i in range(N):
                pg.wait_for_timeout(1600)
                ins = js(pg, "var cv=document.getElementById('cv').getBoundingClientRect(),t=r.querySelector('.cap.turn').getBoundingClientRect();return t.width>0&&t.left>=cv.left-1&&t.right<=cv.right+1&&t.top>=cv.top-1&&t.bottom<=cv.bottom+1;")
                f.check(ins, '%d px step %d: prompt inside the card' % (cw, i + 1))
                if i == 0:
                    fill_sample(pg)
                pg.locator('#cv .hint').first.click()
                pg.wait_for_timeout(700)
                capin = js(pg, "var cv=document.getElementById('cv').getBoundingClientRect(),t=r.querySelector('.cap:not(.turn)').getBoundingClientRect();return t.left>=cv.left-1&&t.right<=cv.right+1&&t.bottom<=cv.bottom+1;")
                f.check(capin, '%d px step %d: caption inside the card' % (cw, i + 1))
                shot(pg, 'card%d_%d_%d.png' % (n, cw, i + 1))
            f.check('Done' in pill(pg), '%d px: reaches Done' % cw)
            f.check(not errs, '%d px: no page errors' % cw)
            pg.close()
        pg, errs = testlib.open_card(b, n, 1300, reduce=True)
        pg.locator('#cv').scroll_into_view_if_needed()
        pg.wait_for_timeout(2500)
        f.check(('Your turn1 of %d' % N) in pill(pg) and pg.locator('#cv .fw-ghost.on').count() == 0, 'reduced motion: starts in Try it, no autoplay')
        pg.close()
        b.close()
    size = os.path.getsize(os.path.join(testlib.REPO, 'graphics', 'textile', 'card-%d.js' % n))
    f.check(40 * 1024 <= size <= 65 * 1024, 'size %.1f KB (40 to 65)' % (size / 1024))
    from PIL import Image
    bg = os.path.join(testlib.REPO, 'graphics', 'textile', 'bg-%d.jpg' % n)
    im = Image.open(bg)
    f.check(im.size == (604, 540) and im.info.get('progressive', im.info.get('progression')) and 35 * 1024 <= os.path.getsize(bg) <= 65 * 1024, 'background bg-%d.jpg: 604 by 540, progressive, %.0f KB' % (n, os.path.getsize(bg) / 1024))
    return f


def finish(f):
    print('\n%d failures' % len(f))
    sys.exit(1 if f else 0)
