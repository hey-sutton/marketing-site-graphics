"""Shared helpers for the Dairy card tests: serves a repo checkout, mounts the real loader, and runs the layout rules
(right edge, bottom edge, square bottom right corner, arrows, background standard, speed target) for any card number."""
import json, os, re, sys, threading, http.server, socketserver
from playwright.sync_api import sync_playwright
from PIL import Image
KEY = 'dairy'
class Ctx:
    def __init__(self, repo, port, out):
        self.repo = repo; self.port = port; self.out = out; os.makedirs(out, exist_ok=True); self.fails = []
        loader = open(repo + '/loader.html').read()
        loader, n = re.subn(r"https://cdn\.jsdelivr\.net/gh/hey-sutton/marketing-site-graphics@[^/']+/", f"http://127.0.0.1:{port}/", loader); assert n == 1
        self.loader = loader
        outer = self
        class Q(http.server.SimpleHTTPRequestHandler):
            def __init__(s, *a, **k): super().__init__(*a, directory=repo, **k)
            def log_message(s, *a): pass
            def end_headers(s): s.send_header("Access-Control-Allow-Origin", "*"); super().end_headers()
        socketserver.TCPServer.allow_reuse_address = True
        self.srv = socketserver.TCPServer(("127.0.0.1", port), Q); threading.Thread(target=self.srv.serve_forever, daemon=True).start()
        self.url = f"http://127.0.0.1:{port}/industries/{KEY}"
    def chk(self, name, cond, detail=''):
        print(('PASS ' if cond else 'FAIL ') + name + (' | ' + detail if (detail and not cond) else ''))
        if not cond: self.fails.append(name)
    def page_html(self, w):
        GIF = "data:image/gif;base64,R0lGODlGAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw=="
        cards = "".join(f'<div class="capabilities_card-visual" id="cv{i}"><img class="capabilities_visual-bg" alt="" src="{GIF}" style="display:block;width:100%;aspect-ratio:604/540">' + (self.loader if i == 1 else "") + "</div>" for i in range(1, 5))
        return f'<!doctype html><html><head><meta charset="utf-8"><style>body{{margin:0;background:#fff}}.w{{width:{w}px}}.capabilities_card-visual{{position:relative;overflow:hidden;margin-bottom:20px;border-radius:8px}}</style></head><body><section data-sx-industry="{KEY}"><div class="w">{cards}</div></section></body></html>'
    def open(self, p, n, w=640, reduced=False):
        b = p.chromium.launch(); c = b.new_context(reduced_motion='reduce' if reduced else 'no-preference', viewport={'width': w + 20, 'height': 3200}); pg = c.new_page(); errs = []
        pg.on('pageerror', lambda e: errs.append(str(e)[:200])); pg.on('console', lambda m: errs.append('console: ' + m.text[:200]) if m.type == 'error' else None)
        pg.route('https://cdn.prod.website-files.com/**', lambda r: r.abort()); pg.route(self.url + '*', lambda r: r.fulfill(status=200, content_type='text/html', body=self.page_html(w)))
        pg.goto(self.url); pg.wait_for_function(f"!!document.querySelector('#cv{n} [data-sxg-host]')", timeout=20000)
        return b, pg, errs, Helpers(pg, n)
    def close(self): self.srv.shutdown()
class Helpers:
    def __init__(self, pg, n):
        self.pg = pg; self.n = n; self.SR = f"document.querySelector('#cv{n} [data-sxg-host]').shadowRoot"
    def ev(self, js, arg=None): return self.pg.evaluate("(a)=>{const r=" + self.SR + ";" + js + "}", arg)
    def txt(self, sel): return self.ev("const e=r.querySelector(a);return e?e.textContent:null", sel)
    def cls(self, sel): return self.ev("const e=r.querySelector(a);return e?e.className:null", sel)
    def click(self, sel): self.ev("r.querySelector(a).click()", sel)
    def dis(self, sel): return self.ev("return r.querySelector(a).disabled", sel)
    def vis_text(self): return self.ev("const o=[];r.querySelectorAll('*').forEach(e=>{if(getComputedStyle(e).visibility!=='hidden'&&e.children.length===0&&e.offsetParent!==null&&e.closest('.fwin'))o.push(e.textContent)});return o.join(' | ')") or ''
    def shot(self, out, name): self.pg.locator(f'#cv{self.n}').screenshot(path=f'{out}/{name}.png')
def layout_rules(ctx, p, n, prep):
    """prep(h) is called after load, it must put the card in a state with content (for the bottom band test)."""
    im = Image.open(f'{ctx.repo}/graphics/{KEY}/bg-{n}.jpg'); sz = os.path.getsize(f'{ctx.repo}/graphics/{KEY}/bg-{n}.jpg')
    ctx.chk(f'card {n}: background 604 by 540, progressive, under 70 KB', im.size == (604, 540) and bool(im.info.get('progressive', 0)) and sz < 70 * 1024, f'{im.size} {sz}')
    code = open(f'{ctx.repo}/graphics/{KEY}/card-{n}.js', encoding='utf-8').read()
    ctx.chk(f'card {n}: file 40 to 65 KB', 40 * 1024 <= len(code.encode()) <= 65 * 1024, str(len(code.encode())))
    ctx.chk(f'card {n}: no concept screen, illustrative or live demo tags', not re.search(r'concept screen|illustrative data|live product demo', code, re.I))
    ctx.chk(f'card {n}: no dashes, recipe or Digit', not re.search('[\u2013\u2014]|\\brecipe\\b|\\bDigit\\b', code, re.I))
    ctx.chk(f'card {n}: only non ASCII free', all(ord(c) < 128 for c in code))
    for w in (1300, 1024, 768, 390):
        b, pg, errs, h = ctx.open(p, n, w); pg.wait_for_timeout(300); prep(h); pg.wait_for_timeout(900)
        m = json.loads(h.ev("""const c=document.querySelector('#cv%d').getBoundingClientRect(),f=r.querySelector('.fwin').getBoundingClientRect(),hh=r.querySelector('.win-host'),s=hh.getBoundingClientRect().width/hh.offsetWidth;
          let low=0;r.querySelectorAll('.fw-body > *').forEach(e=>{if(getComputedStyle(e).visibility!=='hidden')low=Math.max(low,e.getBoundingClientRect().bottom)});
          const st=r.querySelector('.stp').getBoundingClientRect(),cv=document.querySelector('#cv%d'),cs=getComputedStyle(cv);
          let mr=0;r.querySelectorAll('.fw-body *').forEach(e=>{const q=e.getBoundingClientRect(),g=getComputedStyle(e);if(q.width<=0||g.visibility==='hidden'||e.closest('.cap')||e.closest('.fw-tip')||e.closest('.hs'))return;let own=false;for(const n of e.childNodes)if(n.nodeType===3&&n.nodeValue.trim())own=true;const painted=parseFloat(g.borderTopWidth)>0&&g.borderTopStyle!=='none'||(g.backgroundColor!=='rgba(0, 0, 0, 0)'&&g.backgroundColor!=='transparent');if(own||painted)mr=Math.max(mr,q.right)});
          return JSON.stringify({over:f.right-c.right,overB:f.bottom-c.bottom,need:(9.15+1)*s+3,gap:(c.bottom-low)/s,s:s,brr:cs.borderBottomRightRadius,tlr:cs.borderTopLeftRadius,arR:c.right-st.right,arB:c.bottom-st.bottom,contentRight:c.right-mr})""" % (n, n)))
        ctx.chk(f'card {n} at {w}px: right border and corner hidden (window {m["over"]:.0f}px past)', m['over'] >= m['need'], json.dumps(m))
        ctx.chk(f'card {n} at {w}px: bottom edge and corners hidden ({m["overB"]:.0f}px past)', m['overB'] >= m['need'], json.dumps(m))
        ctx.chk(f'card {n} at {w}px: bottom right corner square, others keep the template radius', m['brr'] == '0px' and m['tlr'] == '8px', json.dumps(m))
        ctx.chk(f'card {n} at {w}px: arrows inside the card', m['arR'] >= 6 * m['s'] and m['arB'] >= 4 * m['s'], json.dumps(m))
        ctx.chk(f'card {n} at {w}px: content not clipped at the right', m['contentRight'] >= 4 * m['s'], json.dumps(m))
        ctx.chk(f'card {n} at {w}px: bottom empty band under 40 design px (is {m["gap"]:.0f})', m['gap'] <= 40, json.dumps(m))
        real = [e for e in errs if 'attachShadow' not in e and 'ERR_FAILED' not in e]; ctx.chk(f'card {n} at {w}px: no page errors', not real, str(real)); b.close()
def speed(ctx, p, n, key_js, limit_ms=4200):
    """first caption within 1.8 s and the key result (key_js returns truthy) within limit_ms."""
    b, pg, errs, h = ctx.open(p, n, 640)
    r = pg.evaluate("""async()=>{const r=%s;const t0=performance.now();
      const wait=f=>new Promise(res=>{const i=setInterval(()=>{if(f()){clearInterval(i);res(performance.now()-t0);}},30);setTimeout(()=>{clearInterval(i);res(-1);},9000);});
      const a=await wait(()=>r.querySelector('.cap.on')),k=await wait(()=>{%s});return [a,k];}""" % (h.SR, key_js))
    print(f'card {n} timing: first caption {r[0]:.0f} ms, key result {r[1]:.0f} ms')
    ctx.chk(f'card {n} speed: walkthrough starts within 1.8 s', 0 < r[0] < 1800, str(r)); ctx.chk(f'card {n} speed: key result by about 4 s', 0 < r[1] < limit_ms, str(r)); b.close()
def arrows_generic(ctx, p, n, steps):
    b, pg, errs, h = ctx.open(p, n, 640)
    ctx.chk(f'card {n}: previous disabled at step 1', h.dis('#pv')); 
    for i in range(2, steps + 1):
        h.click('#nx'); pg.wait_for_timeout(500)
        ctx.chk(f'card {n}: next reaches step {i}', h.txt('#sn') == f'{i} of {steps}', h.txt('#sn'))
    ctx.chk(f'card {n}: next disabled at the last step', h.dis('#nx'))
    h.click('#pv'); pg.wait_for_timeout(400); ctx.chk(f'card {n}: previous goes back', h.txt('#sn') == f'{steps-1} of {steps}')
    b.close()
    b, pg, errs, h = ctx.open(p, n, 640, reduced=True); pg.wait_for_timeout(2500)
    h.click('#nx'); pg.wait_for_timeout(600); an = h.ev("return getComputedStyle(r.getElementById('hs')).animationName")
    ctx.chk(f'card {n}: reduced motion, arrows work and hotspot is not animated', h.txt('#sn') == f'2 of {steps}' and an == 'none', an); b.close()
