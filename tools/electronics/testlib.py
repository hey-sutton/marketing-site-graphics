"""Shared test harness for the Electronics cards.

Serves the repo, opens a stub page whose card visual matches the Industries template (aspect 604/540, 8px rounded,
the card file mounted the way the loader does it), and offers helpers for the two mode click through.
Needs: pip install playwright pillow. Set PW_CHROME to a Chromium binary if Playwright's own is missing.
Env: GFX_SHOTS (screenshot folder, default /tmp/electronics_shots).
"""
import functools, http.server, os, re, socketserver, threading
from playwright.sync_api import sync_playwright

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
SHOTS = os.environ.get('GFX_SHOTS', '/tmp/electronics_shots')
os.makedirs(SHOTS, exist_ok=True)

PAGE = '''<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
<style>body{margin:0;background:#F6F6F4;font-family:Inter,sans-serif}.wrap{padding:24px 16px 1200px;display:flex;justify-content:center}
.capabilities_card-visual{position:relative;overflow:hidden;border-radius:8px;width:var(--w);max-width:calc(100vw - 32px);aspect-ratio:604/540;background:#ddd}
.capabilities_visual-bg{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}</style></head>
<body><div class="wrap"><div class="capabilities_card-visual" id="cv" style="--w:@Wpx"><img class="capabilities_visual-bg" alt="" src="/graphics/electronics/bg-@N.jpg"></div></div>
<script>var s=document.createElement('script');s.src='/graphics/electronics/card-@N.js';s.sxCard=document.getElementById('cv');document.head.appendChild(s);</script></body></html>'''

_srv = None


def serve():
    global _srv
    if _srv:
        return _srv
    pages = os.path.join(SHOTS, '_pages')
    os.makedirs(pages, exist_ok=True)

    class H(http.server.SimpleHTTPRequestHandler):
        def translate_path(self, path):
            p = path.split('?')[0]
            if p.startswith('/_pages/'):
                return os.path.join(pages, p[len('/_pages/'):])
            return os.path.join(REPO, p.lstrip('/'))

        def log_message(self, *a):
            pass
    httpd = socketserver.TCPServer(('127.0.0.1', 0), H)
    threading.Thread(target=httpd.serve_forever, daemon=True).start()
    _srv = (httpd.server_address[1], pages)
    return _srv


def page_url(n, card_w):
    port, pages = serve()
    name = 'card%d_%d.html' % (n, card_w)
    open(os.path.join(pages, name), 'w').write(PAGE.replace('@W', str(card_w)).replace('@N', str(n)))
    return 'http://127.0.0.1:%d/_pages/%s' % (port, name)


class Fail(list):
    def check(self, cond, msg):
        print(('  ok   ' if cond else '  FAIL ') + msg)
        if not cond:
            self.append(msg)


def browser(p):
    return p.chromium.launch(executable_path=os.environ.get('PW_CHROME') or None)


def open_card(b, n, vw, card_w=604, reduce=False, vh=900):
    pg = b.new_page(viewport={'width': vw, 'height': vh}, reduced_motion='reduce' if reduce else 'no-preference')
    errs = []
    pg.on('pageerror', lambda e: errs.append(str(e)))
    pg.goto(page_url(n, card_w))
    pg.wait_for_selector('#cv [data-sxg-host]', state='attached', timeout=8000)
    pg.wait_for_timeout(300)
    return pg, errs


def pill(pg):
    return (pg.locator('#cv .tbar .mode').text_content() or '').strip()


def wait_pill(pg, text, timeout=15000):
    pg.wait_for_function("t=>{const h=document.querySelector('#cv [data-sxg-host]');const m=h&&h.shadowRoot.querySelector('.tbar .mode');return m&&m.textContent.indexOf(t)>-1}", arg=text, timeout=timeout)


def win_text(pg):
    return pg.locator('#cv .fwin').inner_text()


def cap_text(pg):
    return pg.locator('#cv .cap:not(.turn)').inner_text()


def turn_text(pg):
    return pg.locator('#cv .cap.turn').inner_text()


def js(pg, expr):
    """Evaluate expr with r = the card's shadow root."""
    return pg.evaluate("e=>{const r=document.querySelector('#cv [data-sxg-host]').shadowRoot;return (new Function('r',e))(r)}", expr)


def shot(pg, name):
    pg.locator('#cv').screenshot(path=os.path.join(SHOTS, name))


def layout_checks(f, pg, n, label):
    """Right and bottom edge of the window hidden, square bottom right corner, no empty band."""
    d = js(pg, '''var cv=document.getElementById('cv').getBoundingClientRect(),w=r.querySelector('.fwin').getBoundingClientRect();
var cs=getComputedStyle(document.getElementById('cv'));
var host=r.querySelector('.win-host'),s=host.getBoundingClientRect().width/host.offsetWidth,low=0;
r.querySelectorAll('.fwin *').forEach(function(e){if(e.closest('.cap,.fw-ghost,.hs,.stp,.sr'))return;var b=e.getBoundingClientRect();if(b.width<2||b.height<2)return;var st=getComputedStyle(e);if(st.visibility==='hidden'||st.opacity==='0')return;
var own=[].some.call(e.childNodes,function(x){return x.nodeType===3&&x.nodeValue.trim()})||/^(BUTTON|INPUT)$/.test(e.tagName);if(!own)return;if(b.top<cv.bottom)low=Math.max(low,Math.min(b.bottom,cv.bottom));});
return {cvR:cv.right,cvB:cv.bottom,wR:w.right,wB:w.bottom,rad:cs.borderBottomRightRadius,band:(cv.bottom-low)/s};''')
    f.check(d['wR'] > d['cvR'] + 1, '%s: window right edge hidden (%.0f > %.0f)' % (label, d['wR'], d['cvR']))
    f.check(d['wB'] > d['cvB'] + 1, '%s: window bottom edge hidden' % label)
    f.check(d['rad'] == '0px', '%s: card bottom right radius is 0px (%s)' % (label, d['rad']))
    f.check(d['band'] < 60, '%s: no empty band at the bottom (%.0f design px)' % (label, d['band']))


DASH = re.compile(r'—|–| - ')
CLAIMS = re.compile(r'\b(IPC compliant|ISO 9001|AS9100|ITAR|FDA|compliant|certified)\b', re.I)


def text_scan(f, text, label):
    f.check(not DASH.search(text), '%s: no dashes used as punctuation' % label)
    f.check(not re.search(r'\bDigit\b', text), '%s: no "Digit"' % label)
    f.check(not re.search(r'\brecipe', text, re.I), '%s: no "recipe"' % label)
    f.check(not CLAIMS.search(text), '%s: no certification or compliance claims' % label)


def visible_text(pg):
    return js(pg, '''var out=[];function w(n){if(n.nodeType===3){if(n.nodeValue.trim())out.push(n.nodeValue.trim());return;}if(n.nodeType!==1&&n.nodeType!==11)return;if(n.tagName==='STYLE'||n.tagName==='SCRIPT')return;
if(n.tagName==='INPUT')out.push(n.value);if(n.getAttribute&&n.getAttribute('aria-label'))out.push(n.getAttribute('aria-label'));[].forEach.call(n.childNodes,w);}w(r);return out.join(' | ');''')


def run_card(n, plan, numbers, extra=None):
    """plan: list of (step_label, must_text_after). numbers: list of strings the final screens must show.
    Runs Watch through every step, the take over, Try it with a wrong click, every correct click, arrows,
    Replay and the toggle, reduced motion, the Studio popover, layout at four widths, and a text scan."""
    f = Fail()
    N = len(plan)
    with sync_playwright() as p:
        b = browser(p)
        # Watch mode
        pg, errs = open_card(b, n, 1300)
        pg.locator('#cv').scroll_into_view_if_needed()
        wait_pill(pg, 'Watching', 4000)
        t0 = pg.evaluate('performance.now()')
        pg.wait_for_function("()=>{const h=document.querySelector('#cv [data-sxg-host]');return h.shadowRoot.querySelector('.cap.on')}", timeout=6000)
        f.check(pg.evaluate('performance.now()') - t0 < 4000, 'watch: first result and caption on screen within 4 s')
        f.check('of %d' % N in pill(pg), 'watch: pill shows n of %d (%s)' % (N, pill(pg)))
        seen = set()
        for i in range(N):
            wait_pill(pg, 'Watching%d of %d' % (i + 1, N), 9000)
            seen.add(i + 1)
            pg.wait_for_timeout(1500)
            shot(pg, 'card%d_watch_%d.png' % (n, i + 1))
        f.check(len(seen) == N, 'watch: ran all %d steps' % N)
        f.check(plan[-1][1] is None or plan[-1][1] in win_text(pg), 'watch: final screen shows the last result')
        wait_pill(pg, 'Watching1 of %d' % N, 12000)
        f.check(True, 'watch: loops back to step 1')
        # take over: first click only switches mode
        before = win_text(pg)
        pg.locator('#cv .fwin .hd').click(position={'x': 40, 'y': 20})
        pg.wait_for_timeout(500)
        f.check('Your turn1 of %d' % N in pill(pg), 'try: a click inside takes over and restarts (%s)' % pill(pg))
        f.check(pg.locator('#cv .fw-ghost.on').count() == 0, 'try: ghost cursor gone')
        shot(pg, 'card%d_try_start.png' % n)
        for i, (label, must) in enumerate(plan):
            pg.wait_for_timeout(1700)
            hints = pg.locator('#cv .hint')
            f.check(hints.count() == 1, 'step %d: one pulsing target (%d)' % (i + 1, hints.count()))
            f.check(pg.locator('#cv .fade').count() > 0, 'step %d: the rest dims' % (i + 1))
            f.check(pg.locator('#cv .hs.on').count() == 1, 'step %d: ripple hotspot on the target' % (i + 1))
            f.check(('Your turn%d of %d' % (i + 1, N)) in pill(pg), 'step %d: pill Your turn %d of %d' % (i + 1, i + 1, N))
            f.check(turn_text(pg).startswith('Your turn.'), 'step %d: prompt "%s"' % (i + 1, turn_text(pg)))
            # prompt and caption inside the card
            ins = js(pg, "var cv=document.getElementById('cv').getBoundingClientRect(),t=r.querySelector('.cap.turn').getBoundingClientRect();return t.left>=cv.left-1&&t.right<=cv.right+1&&t.top>=cv.top-1&&t.bottom<=cv.bottom+1;")
            f.check(ins, 'step %d: prompt inside the card' % (i + 1))
            shot(pg, 'card%d_try_%d_prompt.png' % (n, i + 1))
            if i == 0:
                pg.locator('#cv .fwin .hd .tt').click()
                pg.wait_for_timeout(300)
                f.check(('Your turn1 of %d' % N) in pill(pg) and hints.count() == 1, 'step 1: a wrong click re-shows the prompt')
            if extra and i in extra.get('before', {}):
                extra['before'][i](pg, f)
            hints.first.click()
            pg.wait_for_timeout(600)
            c = cap_text(pg)
            f.check(label in c, 'step %d caption: %s' % (i + 1, c.replace('\n', ' ')[:80]))
            if must:
                f.check(must in win_text(pg), 'step %d screen shows "%s"' % (i + 1, must))
            capin = js(pg, "var cv=document.getElementById('cv').getBoundingClientRect(),t=r.querySelector('.cap:not(.turn)').getBoundingClientRect();return t.left>=cv.left-1&&t.right<=cv.right+1&&t.bottom<=cv.bottom+1;")
            f.check(capin, 'step %d: caption inside the card' % (i + 1))
            shot(pg, 'card%d_try_%d_after.png' % (n, i + 1))
        pg.wait_for_timeout(400)
        f.check('Done' in pill(pg), 'try: ends on Done (%s)' % pill(pg))
        f.check(pg.locator('#cv .hint').count() == 0, 'try: no pulse after Done')
        txt = win_text(pg)
        for s in numbers:
            f.check(s in txt, 'final screen shows %s' % s)
        if extra and 'after' in extra:
            extra['after'](pg, f)
        # arrows jump to a step
        pg.locator('#cv #pv').click()
        pg.wait_for_timeout(500)
        f.check(('Your turn%d of %d' % (N, N)) in pill(pg), 'arrows: previous jumps to step %d (%s)' % (N, pill(pg)))
        pg.locator('#cv #pv').click()
        pg.wait_for_timeout(500)
        f.check(('Your turn%d of %d' % (N - 1, N)) in pill(pg), 'arrows: previous again to step %d' % (N - 1))
        pg.locator('#cv #nx').click()
        pg.wait_for_timeout(500)
        f.check(('Your turn%d of %d' % (N, N)) in pill(pg), 'arrows: next to step %d' % N)
        # Replay in Try it restarts Try it
        pg.locator('#cv .tbar .rp').click()
        pg.wait_for_timeout(400)
        f.check(('Your turn1 of %d' % N) in pill(pg), 'Replay restarts Try it at step 1')
        # toggle back to Watch
        pg.locator('#cv .mtg [data-m="watch"]').click()
        pg.wait_for_timeout(600)
        f.check('Watching' in pill(pg), 'toggle: Watch restarts Watch')
        pg.wait_for_timeout(1500)
        pg.locator('#cv .mtg [data-m="try"]').click()
        pg.wait_for_timeout(400)
        f.check(('Your turn1 of %d' % N) in pill(pg), 'toggle: Try it restarts at step 1')
        # Studio popover
        pg.locator('#cv .studio-chip').click()
        pg.wait_for_timeout(600)
        f.check(pg.locator('#cv .studio.open').count() == 1, 'Studio popover opens')
        f.check(js(pg, "return getComputedStyle(r.querySelector('.tbar .mode')).visibility") == 'hidden', 'pill hides while the popover is open')
        pg.keyboard.press('Escape')
        pg.wait_for_timeout(400)
        f.check(pg.locator('#cv .studio.open').count() == 0, 'Studio popover closes')
        vt = visible_text(pg)
        text_scan(f, vt, 'text')
        f.check(not errs, 'no page errors %s' % errs[:2])
        pg.close()
        # start screen, layout at four widths
        for vw, cw in ((1300, 604), (1024, 480), (768, 604), (390, 358)):
            pg, errs = open_card(b, n, vw, cw)
            pg.locator('#cv').scroll_into_view_if_needed()
            pg.wait_for_timeout(200)
            layout_checks(f, pg, n, '%d px' % vw)
            shot(pg, 'card%d_layout_%d.png' % (n, vw))
            pg.close()
        # Studio fits at 340
        pg, errs = open_card(b, n, 372, 340)
        pg.locator('#cv').scroll_into_view_if_needed()
        bar = js(pg, "var cv=document.getElementById('cv').getBoundingClientRect(),t=r.querySelector('.tbar').getBoundingClientRect(),s=r.querySelector('.studio-chip').getBoundingClientRect();return t.left>=s.right+2&&t.right<=cv.right;")
        f.check(bar, '340 px: top bar fits next to the Studio badge')
        pg.locator('#cv .studio-chip').click()
        pg.wait_for_timeout(700)
        fits = js(pg, "var cv=document.getElementById('cv').getBoundingClientRect(),p=r.querySelector('.pop').getBoundingClientRect();return {pop:p.left>=cv.left&&p.right<=cv.right+1,hid:getComputedStyle(r.querySelector('.tbar')).visibility==='hidden'};")
        f.check(fits['pop'], '340 px: Studio popover fits the card')
        f.check(fits['hid'], '340 px: the top bar steps aside while the popover is open')
        f.check(js(pg, "return getComputedStyle(r.querySelector('.tbar .mode .mc')).display") == 'none', '340 px: pill hides n of N')
        shot(pg, 'card%d_340_studio.png' % n)
        pg.keyboard.press('Escape')
        pg.close()
        # every step at 390 px (shrink to fit): prompt and caption stay inside the card
        pg, errs = open_card(b, n, 390, 358)
        pg.locator('#cv').scroll_into_view_if_needed()
        pg.locator('#cv .mtg [data-m="try"]').click()
        for i in range(N):
            pg.wait_for_timeout(1600)
            ins = js(pg, "var cv=document.getElementById('cv').getBoundingClientRect(),t=r.querySelector('.cap.turn').getBoundingClientRect();return t.width>0&&t.left>=cv.left-1&&t.right<=cv.right+1&&t.top>=cv.top-1&&t.bottom<=cv.bottom+1;")
            f.check(ins, '390 px step %d: prompt inside the card' % (i + 1))
            shot(pg, 'card%d_390_%d_prompt.png' % (n, i + 1))
            pg.locator('#cv .hint').first.click()
            pg.wait_for_timeout(600)
            capin = js(pg, "var cv=document.getElementById('cv').getBoundingClientRect(),t=r.querySelector('.cap:not(.turn)').getBoundingClientRect();return t.left>=cv.left-1&&t.right<=cv.right+1&&t.bottom<=cv.bottom+1;")
            f.check(capin, '390 px step %d: caption inside the card' % (i + 1))
            shot(pg, 'card%d_390_%d_after.png' % (n, i + 1))
        f.check('Done' in pill(pg), '390 px: reaches Done')
        f.check(not errs, '390 px: no page errors')
        pg.close()
        # reduced motion: start in Try it, no autoplay
        pg, errs = open_card(b, n, 1300, reduce=True)
        pg.locator('#cv').scroll_into_view_if_needed()
        pg.wait_for_timeout(2500)
        f.check(('Your turn1 of %d' % N) in pill(pg) and pg.locator('#cv .fw-ghost.on').count() == 0, 'reduced motion: starts in Try it, no autoplay')
        pg.close()
        b.close()
    size = os.path.getsize(os.path.join(REPO, 'graphics', 'electronics', 'card-%d.js' % n))
    f.check(40 * 1024 <= size <= 80 * 1024, 'size %.1f KB' % (size / 1024))
    return f
