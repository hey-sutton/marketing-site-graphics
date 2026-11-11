#!/usr/bin/env python3
"""Check demo cards against the November 11, 2026 UI rules, on preview pages built by make_preview_page.py.

  python3 check_demo_ui.py --html preview1.html --widths 1300 390 340
  python3 check_demo_ui.py --cards preview1.html preview2.html preview3.html preview4.html

--html, at each width (1300 is a viewport width with the card at its desktop size; widths under 640 are card widths):
  FAIL  control row: order Studio chip, Watch and Try it toggle, step counter, Replay; under 600 px of card width two
        lines (Studio and Replay on line 1, toggle and counter on line 2); every control visible, inside the card, not
        covered, not overlapping another, and at least 40 CSS px under 600 px
  FAIL  Replay is an icon only, with aria-label and title "Replay"
  FAIL  the window runs past the card's right and bottom edges, and the card's bottom right corner is square
  FAIL  Studio popover opens on tap (touch, no hover); the walkthrough controls work by tap
  FAIL  no colliding text inside the window, on the start screen and after every step of Try it
  FAIL  text: no dashes as punctuation, "Digit", "recipe", price, plan or trial wording, concept or illustrative tags
  WARN  the popover does not fit inside the card; an empty band at the bottom of the start screen; card size
        outside 40 to 65 KB
--cards: nav and profile must be the same on every card (data-shell="sidebar", data-shell="profile", or none on all),
  and every window must have the same header (icon, title, subtitle) in the same place.
Exit code 1 when any FAIL is found. Set PW_CHROME to a Chromium binary if Playwright's own browser is missing.
"""
import argparse, os, re, sys
from playwright.sync_api import sync_playwright

HOST = "document.querySelector('#cv%d [data-sxg-host]').shadowRoot"
DASH = re.compile(r'\u2014|\u2013| - ')
WORDS = re.compile(r'(?i:\bpricing\b|\bprice plan|\byour plan\b|\bpaid plan|\bplan tier|\bper month\b|/mo\b|free trial|\btrial\b|subscription|concept screen|live product demo|illustrative data|\brecipe)|\bDigit\b')


class Report:
    def __init__(self):
        self.fails, self.warns = [], []

    def ok(self, cond, msg, warn=False):
        if cond:
            print('  PASS ' + msg)
        elif warn:
            print('  WARN ' + msg); self.warns.append(msg)
        else:
            print('  FAIL ' + msg); self.fails.append(msg)


def ev(pg, i, body, arg=None):
    return pg.evaluate("a=>{const r=%s;const cvEl=document.getElementById('cv%d');%s}" % (HOST % i, i, body), arg)


CTRL = '''var cv=cvEl.getBoundingClientRect();function bx(e){if(!e)return null;var b=e.getBoundingClientRect(),cs=getComputedStyle(e),hid=false;for(var x=e;x&&x.nodeType===1;x=x.parentElement||(x.getRootNode&&x.getRootNode().host)){var s=getComputedStyle(x);if(s.visibility==='hidden'||s.display==='none')hid=true;if(x===cvEl)break;}
return {l:b.left,t:b.top,r:b.right,b:b.bottom,w:b.width,h:b.height,vis:!hid&&b.width>0&&b.height>0};}
var els={studio:r.querySelector('.studio-chip'),watch:r.querySelector('[data-m="watch"]'),tryit:r.querySelector('[data-m="try"]'),prev:r.getElementById('pv'),counter:r.querySelector('.tbar .mode'),next:r.getElementById('nx'),replay:r.querySelector('.tbar .rp')};
var out={};for(var k in els){var b=bx(els[k]);if(b&&b.vis&&k!=='counter'){var el=r.elementFromPoint(b.l+b.w/2,b.t+b.h/2);b.free=!!el&&(el===els[k]||els[k].contains(el));}out[k]=b;}
var rp=els.replay;return {cv:{l:cv.left,t:cv.top,r:cv.right,b:cv.bottom,w:cv.width,h:cv.height},c:out,rpText:rp?rp.innerText.trim():'x',rpAria:rp&&rp.getAttribute('aria-label'),rpTitle:rp&&rp.getAttribute('title'),
win:(function(){var w=r.querySelector('.fwin').getBoundingClientRect();return {r:w.right,b:w.bottom};})(),rad:getComputedStyle(cvEl).borderBottomRightRadius};'''

TEXT = '''var win=r.querySelector('.fwin'),out=[],skip='.cap,.fw-ghost,.hs,.sr,.tbar';
function inter(a,b){return {l:Math.max(a.l,b.l),t:Math.max(a.t,b.t),r:Math.min(a.r,b.r),b:Math.min(a.b,b.b)};}
function shown(el){for(var x=el;x&&x!==win.parentNode;x=x.parentElement){var s=getComputedStyle(x);if(s.display==='none'||s.visibility==='hidden'||parseFloat(s.opacity)<0.05)return false;}return true;}
var tw=document.createTreeWalker(win,NodeFilter.SHOW_TEXT),n;
while((n=tw.nextNode())){if(!n.nodeValue.trim())continue;var el=n.parentElement;if(!el||el.closest(skip)||!shown(el))continue;
var rg=document.createRange();rg.selectNodeContents(n);var rs=[].slice.call(rg.getClientRects());if(!rs.length)continue;
var clips=[];for(var a=el;a&&a!==win.parentNode;a=a.parentElement){var s=getComputedStyle(a);if(s.overflowX!=='visible'||s.overflowY!=='visible'){var b=a.getBoundingClientRect();clips.push({l:b.left,t:b.top,r:b.right,b:b.bottom});}}
var lines=[];rs.forEach(function(x){var R={l:x.left,t:x.top,r:x.right,b:x.bottom};clips.forEach(function(c){R=inter(R,c);});if(R.r-R.l>=1&&R.b-R.t>=1)lines.push(R);});
if(lines.length)out.push({t:n.nodeValue.trim().slice(0,24),L:lines,el:el});}
var hits=[];for(var i=0;i<out.length;i++)for(var j=i+1;j<out.length;j++){if(out[i].el===out[j].el)continue;var hit=false;
out[i].L.forEach(function(A){out[j].L.forEach(function(B){var w=Math.min(A.r,B.r)-Math.max(A.l,B.l),h=Math.min(A.b,B.b)-Math.max(A.t,B.t),lh=Math.min(A.b-A.t,B.b-B.t);if(w>1&&h>Math.max(1,lh*0.25))hit=true;});});
if(hit)hits.push(out[i].t+' / '+out[j].t);}
return {n:out.length,hits:hits.slice(0,6)};'''


def overlap(a, b):
    return min(a['r'], b['r']) - max(a['l'], b['l']) > 0.5 and min(a['b'], b['b']) - max(a['t'], b['t']) > 0.5


def mount(b, path, vw, cw, touch=False):
    ctx = b.new_context(viewport={'width': vw, 'height': 1000}, has_touch=touch, is_mobile=touch)
    pg = ctx.new_page()
    errs = []
    pg.on('pageerror', lambda e: errs.append(str(e)[:160]))
    pg.goto('file://' + os.path.abspath(path))
    if cw:
        pg.add_style_tag(content='.stage{width:%dpx!important;max-width:none!important}#grid{grid-template-columns:%dpx!important}main{padding-left:8px!important;padding-right:8px!important}' % (cw, cw))
    pg.wait_for_selector('#cv0 [data-sxg-host]', state='attached', timeout=8000)
    pg.locator('#cv0').scroll_into_view_if_needed()
    pg.wait_for_timeout(500)
    return ctx, pg, errs


def controls(rep, d, label):
    c, cv = d['c'], d['cv']
    two = cv['w'] < 600
    rep.ok(d['rpText'] == '' and d['rpAria'] == 'Replay' and d['rpTitle'] == 'Replay', '%s: Replay is an icon only, aria-label and title "Replay"' % label)
    keys = ['studio', 'watch', 'tryit', 'prev', 'counter', 'next', 'replay'] if two else ['studio', 'watch', 'tryit', 'counter', 'replay']
    for k in keys:
        b = c[k]
        rep.ok(b and b['vis'] and b['l'] >= cv['l'] - .5 and b['r'] <= cv['r'] + .5 and b['t'] >= cv['t'] - .5 and b['b'] <= cv['b'] + .5, '%s: %s visible and inside the card' % (label, k))
        if b and k != 'counter':
            rep.ok(b.get('free'), '%s: %s not covered' % (label, k))
        if two and k != 'counter':
            rep.ok(b and b['w'] >= 39.5 and b['h'] >= 39.5, '%s: %s tap size %.0f by %.0f CSS px (40 or more)' % (label, k, b['w'] if b else 0, b['h'] if b else 0))
    bad = [(a, x) for i, a in enumerate(keys) for x in keys[i + 1:] if c[a] and c[x] and overlap(c[a], c[x])]
    rep.ok(not bad, '%s: no controls overlap %s' % (label, bad or ''))
    if two:
        line1 = abs(c['studio']['t'] - c['replay']['t']) < 2 and c['studio']['r'] < c['replay']['l']
        line2 = max(c[k]['t'] for k in ('watch', 'prev', 'counter', 'next')) - min(c[k]['t'] for k in ('watch', 'prev', 'counter', 'next')) < 2 and c['watch']['t'] >= c['studio']['b']
        order = c['watch']['r'] <= c['tryit']['l'] + .5 and c['tryit']['r'] <= c['prev']['l'] and c['prev']['r'] <= c['counter']['l'] and c['counter']['r'] <= c['next']['l']
        rep.ok(line1 and line2 and order, '%s: two lines, Studio and Replay on line 1, toggle and counter on line 2, in order' % label)
    else:
        mid = [c[k]['t'] + c[k]['h'] / 2 for k in keys]
        rep.ok(max(mid) - min(mid) < 4 and c['studio']['r'] < c['watch']['l'] and c['tryit']['r'] < c['counter']['l'] and c['counter']['r'] < c['replay']['l'], '%s: one row in order Studio, toggle, counter, Replay' % label)
    rep.ok(d['win']['r'] > cv['r'] + 1 and d['win']['b'] > cv['b'] + 1, '%s: window runs past the right and bottom edges' % label)
    rep.ok(d['rad'] == '0px', '%s: card bottom right corner is square (%s)' % (label, d['rad']))


def check_html(path, widths):
    rep = Report()
    src = open(path, encoding='utf-8').read()
    m = re.search(r'<script type="text/plain" id="card-src0">(.*?)</script>', src, re.S)
    size = len(m.group(1).encode()) if m else 0
    print('%s' % path)
    rep.ok(40 * 1024 <= size <= 65 * 1024, 'card size %.1f KB (40 to 65)' % (size / 1024), warn=True)
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=os.environ.get('PW_CHROME') or None)
        for w in widths:
            cw = None if w >= 640 else w
            vw = w if w >= 640 else w + 16
            label = ('viewport %d' % w) if cw is None else ('card %d' % cw)
            ctx, pg, errs = mount(b, path, vw, cw)
            d = ev(pg, 0, CTRL)
            controls(rep, d, label)
            t = ev(pg, 0, TEXT)
            rep.ok(not t['hits'], '%s start screen: no colliding text (%d text runs) %s' % (label, t['n'], t['hits'] or ''))
            band = ev(pg, 0, '''var cv=cvEl.getBoundingClientRect(),host=r.querySelector('.win-host'),s=host.getBoundingClientRect().width/host.offsetWidth,low=0;
r.querySelectorAll('.fwin *').forEach(function(e){if(e.closest('.cap,.fw-ghost,.hs,.stp,.sr'))return;var b=e.getBoundingClientRect();if(b.width<2||b.height<2)return;var own=[].some.call(e.childNodes,function(x){return x.nodeType===3&&x.nodeValue.trim()})||/^(BUTTON|INPUT)$/.test(e.tagName);if(own&&b.top<cv.bottom)low=Math.max(low,Math.min(b.bottom,cv.bottom));});return (cv.bottom-low)/s;''')
            rep.ok(band < 60, '%s start screen: no empty band at the bottom (%.0f design px)' % (label, band), warn=True)
            # Try it through every step: text collisions after each one
            pg.locator('#cv0 [data-m="try"]').click()
            ns = int(pg.locator('#cv0 #sn').text_content().split(' of ')[1])
            hits = []
            for i in range(ns):
                pg.wait_for_timeout(1600)
                if i == 0 and pg.locator('#cv0 [data-sample]').count():
                    pg.locator('#cv0 [data-sample]').first.click(); pg.wait_for_timeout(150)
                pg.locator('#cv0 .hint').first.click()
                pg.wait_for_timeout(1000)
                t = ev(pg, 0, TEXT)
                hits += ['step %d: %s' % (i + 1, h) for h in t['hits']]
            done = 'Done' in pg.locator('#cv0 .tbar .mode').text_content()
            rep.ok(done, '%s: Try it reaches Done in %d steps' % (label, ns))
            rep.ok(not hits, '%s: no colliding text after any step %s' % (label, hits[:6] or ''))
            txt = ev(pg, 0, '''var o=[];function w(n){if(n.nodeType===3){if(n.nodeValue.trim())o.push(n.nodeValue.trim());return;}if(n.nodeType!==1&&n.nodeType!==11)return;if(n.tagName==='STYLE'||n.tagName==='SCRIPT')return;if(n.getAttribute&&n.getAttribute('aria-label'))o.push(n.getAttribute('aria-label'));[].forEach.call(n.childNodes,w);}w(r);return o.join(' | ');''')
            mm = DASH.search(txt) or WORDS.search(txt)
            rep.ok(not mm, '%s: text has no dashes, "Digit", "recipe", price, plan or trial wording %s' % (label, ('(found "%s")' % mm.group(0)) if mm else ''))
            rep.ok(not errs, '%s: no page errors %s' % (label, errs[:2]))
            ctx.close()
            # touch: the popover opens on tap, the controls work by tap
            ctx, pg, errs = mount(b, path, vw, cw, touch=True)
            pg.locator('#cv0 .studio-chip').tap(); pg.wait_for_timeout(700)
            op = ev(pg, 0, "var cv=cvEl.getBoundingClientRect(),p=r.querySelector('.pop').getBoundingClientRect();return {open:!!r.querySelector('.studio.open'),fit:p.left>=cv.left-.5&&p.right<=cv.right+.5&&p.top>=cv.top-.5&&p.bottom<=cv.bottom+.5};")
            rep.ok(op['open'], '%s touch: tapping Studio opens the popover' % label)
            rep.ok(op['fit'], '%s touch: the popover fits inside the card' % label, warn=True)
            pg.locator('#cv0 .studio-chip').tap(); pg.wait_for_timeout(500)
            mode = lambda: pg.locator('#cv0 .tbar .mode').text_content()
            pg.locator('#cv0 [data-m="try"]').tap(); pg.wait_for_timeout(400); a1 = 'Your turn1 of' in mode()
            pg.locator('#cv0 #nx').tap(); pg.wait_for_timeout(400); a2 = 'Your turn2 of' in mode()
            pg.locator('#cv0 #pv').tap(); pg.wait_for_timeout(400); a3 = 'Your turn1 of' in mode()
            pg.locator('#cv0 [data-m="watch"]').tap(); pg.wait_for_timeout(400); a4 = 'Watching' in mode()
            pg.locator('#cv0 .tbar .rp').tap(); pg.wait_for_timeout(400); a5 = 'Watching1 of' in mode()
            rep.ok(a1 and a2 and a3 and a4 and a5, '%s touch: Try it, next, previous, Watch and Replay all work by tap' % label)
            ctx.close()
        b.close()
    return rep


SHELL = '''var hd=r.querySelector('.fwin>.hd'),w=r.querySelector('.fwin').getBoundingClientRect();function rel(e){if(!e)return null;var b=e.getBoundingClientRect(),s=w.width/716;return [Math.round((b.left-w.left)/s),Math.round((b.top-w.top)/s),Math.round(b.height/s)];}
return {sidebar:r.querySelectorAll('[data-shell="sidebar"]').length,profile:r.querySelectorAll('[data-shell="profile"]').length,rail:r.querySelectorAll('.rail,nav').length,
hd:hd?[rel(hd),rel(hd.querySelector('.hi')),rel(hd.querySelector('.tt')),rel(hd.querySelector('.sb'))]:null};'''


def check_cards(paths):
    rep = Report()
    rows = []
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=os.environ.get('PW_CHROME') or None)
        for path in paths:
            ctx, pg, errs = mount(b, path, 1300, None)
            d = ev(pg, 0, SHELL)
            rows.append((path, d))
            print('  %s: sidebar %d, profile %d, other nav %d, header %s' % (path, d['sidebar'], d['profile'], d['rail'], d['hd']))
            ctx.close()
        b.close()
    shells = {(d['sidebar'] > 0, d['profile'] > 0, d['rail'] > 0) for _, d in rows}
    rep.ok(len(shells) == 1, 'nav and profile are the same on every card (%s)' % ('none on all' if shells == {(False, False, False)} else shells))
    rep.ok(all(d['rail'] == 0 or d['sidebar'] > 0 for _, d in rows), 'any nav is marked data-shell="sidebar"')
    heads = [d['hd'] for _, d in rows]
    ok = all(h and all(h) for h in heads) and all(h[0] == heads[0][0] and h[1] == heads[0][1] and h[2][:2] == heads[0][2][:2] for h in heads)
    rep.ok(ok, 'every window has the same header (icon, title, subtitle) in the same place')
    return rep


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--html')
    ap.add_argument('--widths', nargs='+', type=int, default=[1300, 390, 340])
    ap.add_argument('--cards', nargs='+')
    a = ap.parse_args()
    if not (a.html or a.cards):
        print(__doc__); sys.exit(2)
    rep = check_html(a.html, a.widths) if a.html else check_cards(a.cards)
    print('RESULT: %s (%d FAIL, %d WARN)' % ('FAIL' if rep.fails else 'PASS', len(rep.fails), len(rep.warns)))
    sys.exit(1 if rep.fails else 0)
