"""
Automotive layer on the shared Watch and Try it frame (tools/electronics/frame.py).

It applies the UI rules from the November 11, 2026 review without changing the shared frame for other industries:
  * Replay is an icon only button (circular arrow, aria-label and title "Replay", no visible word).
  * Control row order at every width: Studio chip, Watch and Try it toggle, step counter, Replay icon.
  * Under 600 px of card width the row wraps to two lines: Studio and Replay on line 1, the toggle and the step
    counter (with the previous and next arrows either side of it) on line 2. Every control is drawn at a fixed CSS
    size outside the scaled window, at least 40 CSS px to tap, so it stays usable at 390 and 340 px.
  * The window keeps its full 716 by 640 size at every width and still bleeds past the card's right and bottom edges.
    Under 600 px the card visual grows taller (aspect ratio set on the card) so the window sits below the two control
    lines and shows the same 600 design px of content as on desktop.
  * No side nav and no profile on any automotive card: every window starts with the same header (icon, title,
    subtitle), built by header() below.
"""
import os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(HERE), 'electronics'))
import frame  # noqa: E402

frame.KEY = 'automotive'
frame.LABEL = 'Automotive'

TOPC = 102     # CSS px from the card top to the window under 600 px: 8 + 40 + 6 + 40 + 8
VISD = 600     # design px of window content shown under 600 px (matches desktop)

REPLAY_OLD = '<span>Replay</span>\';rp.setAttribute(\'aria-label\',\'Replay\');'
REPLAY_NEW = '\';rp.setAttribute(\'aria-label\',\'Replay\');rp.setAttribute(\'title\',\'Replay\');'

CTRL_CSS = (
 # desktop: icon only Replay, same height as the toggle and the pill
 '.tbar .rp{width:30px;height:30px;padding:0;justify-content:center}.tbar .rp svg{width:14px;height:14px}'
 '.ctl{width:40px;height:40px;padding:0;border:1px solid rgba(0,0,0,.08);border-radius:9px;background:rgba(255,255,255,.92);color:#18181B;display:grid;place-items:center;cursor:pointer;-webkit-backdrop-filter:blur(8px);backdrop-filter:blur(8px)}'
 '.ctl:disabled{opacity:.45;cursor:default}.ctl svg{width:14px;height:14px}.ctl:focus-visible,.tbar .rp:focus-visible{outline:2px solid #1B1B1A;outline-offset:1px}'
 # under 600 px: two lines, fixed CSS sizes, 40 px targets
 '.shot.c2 .win-host{top:' + str(TOPC) + 'px}'
 '.shot.c2 .studio{top:8px;left:8px}.shot.c2 .studio-chip{height:40px}'
 '.shot.c2 .tbar{left:8px;right:8px;top:8px;display:grid;grid-template-columns:auto auto auto auto 1fr auto;grid-template-rows:40px 40px;column-gap:6px;row-gap:6px;align-items:center;pointer-events:none}'
 '.shot.c2 .tbar>*{pointer-events:auto}'
 '.shot.c2 .mtg{grid-row:2;grid-column:1;height:40px;padding:0;gap:0;border:0;box-shadow:0 0 0 1px rgba(0,0,0,.08);border-radius:9px}.shot.c2 .mtg button{height:40px;min-width:48px;padding:0 9px;font-size:12px;border-radius:8px}'
 '.shot.c2 .tbar #pv{grid-row:2;grid-column:2}.shot.c2 .tbar .mode{grid-row:2;grid-column:3;height:40px;padding:0 10px}.shot.c2 .tbar #nx{grid-row:2;grid-column:4}'
 '.shot.c2 .tbar .rp{grid-row:1;grid-column:6;width:40px;height:40px;padding:0}'
 '.shot.c2 .mode>span:nth-child(2){display:none}.shot.c2 .mode .mc{display:inline;color:inherit;font-weight:500}'
 '.shot.c2 .stp{display:none}'
 # the popover keeps its four examples and three rows on a phone, set smaller so it fits the card
 '.shot.c2 .pop{padding:12px 13px}.shot.c2 .pop h3{font-size:14px;margin-bottom:4px}.shot.c2 .pop .lede{font-size:11.5px;line-height:1.4;margin-bottom:8px}.shot.c2 .pop .examples{display:flex;gap:4px;margin-bottom:8px}.shot.c2 .pop .examples li{font-size:10.5px;padding:3px 8px}'
 '.shot.c2 .pop .rows{display:block;margin-bottom:8px}.shot.c2 .pop .rows div{grid-template-columns:70px 1fr;padding:5px 0;font-size:11px}.shot.c2 .pop .go{font-size:12px}'
 '.shot.nar .pop{padding:10px 11px}.shot.nar .pop h3{font-size:12.5px;margin-bottom:3px}.shot.nar .pop .lede{font-size:10.5px;line-height:1.35;margin-bottom:6px}.shot.nar .pop .examples{gap:3px;margin-bottom:6px}.shot.nar .pop .examples li{font-size:9.5px;padding:2px 7px}'
 '.shot.nar .pop .rows{margin-bottom:6px}.shot.nar .pop .rows div{grid-template-columns:58px 1fr;padding:3px 0;font-size:10px;gap:6px}.shot.nar .pop .go{font-size:11px}'
 '.shot.c2.sopen .tbar>*:not(.rp){visibility:hidden}'
)

CTRL_JS = r'''
/* ===== Automotive control row (November 11, 2026 rules). Replaces fit() and placeStp() above. ===== */
var stpEl=host.querySelector('.stp'),snEl=$('sn');
pv.classList.add('ctl');nx.classList.add('ctl');
function fit(){var P=host.parentNode,W=P.clientWidth,c2=W<600,s=W/742,cv=root.host&&root.host.parentElement;
shot.style.setProperty('--cw',W+'px');shot.classList.toggle('nar',W<430);shot.classList.toggle('c2',c2);
if(cv&&cv.style)cv.style.aspectRatio=c2?(W/Math.round(@TOPC@+@VISD@*s)).toFixed(4):'';
host.style.transform='scale('+s+')';ctlPlace(c2);if(!c2)placeStp();}
function placeStp(){var st=host.querySelector('.stp'),P=host.parentNode,sc=P.clientWidth/742;if(!st||!sc)return;var vh=(P.clientHeight-host.offsetTop)/sc;st.style.bottom=Math.max(44,Math.round(640-vh+28))+'px';}
function ctlPlace(c2){if(typeof bar==='undefined'||!bar||!stpEl)return;
if(c2&&pv.parentNode!==bar){bar.insertBefore(pv,md);bar.insertBefore(nx,rp);}
else if(!c2&&pv.parentNode!==stpEl){stpEl.insertBefore(pv,snEl);stpEl.appendChild(nx);}
pv.classList.toggle('ctl',c2);nx.classList.toggle('ctl',c2);}
fit();
'''


def header(icon, title, sub, right=''):
    """The one window header every automotive card uses: icon, title, subtitle, then optional chips on the right."""
    return ('<div class="hd"><span class="hi" aria-hidden="true"><svg width="16" height="16" viewBox="0 0 16 16" fill="none" stroke="#18181B" stroke-width="1.25" stroke-linecap="round" stroke-linejoin="round">'
            + icon + '</svg></span><span class="tt">' + title + '</span><span class="sb grow">' + sub + '</span>' + right + '</div>')


GET_HELP = 'From the Sutton team'

HEAD_CSS = '.hd .hi{width:24px;height:24px;border-radius:6px;background:#F4F4F5;display:grid;place-items:center;flex:none}.hd{padding-right:44px}'


def build(n, m):
    """Build graphics/automotive/card-N.js from card module m (SUMMARY, ARIA, WIN, CSS, JS, STEPS, STUDIO)."""
    st = frame.studio(**m.STUDIO)
    # no plan wording anywhere (November 11, 2026): the shared popover's "Depends on your plan" is replaced
    assert st.count('<dd>Depends on your plan</dd>') == 1
    st = st.replace('<dd>Depends on your plan</dd>', '<dd>' + GET_HELP + '</dd>')
    boot, eng = frame.BOOT_HEAD, frame.ENGINE_JS
    assert boot.count(REPLAY_OLD) == 1
    try:
        frame.BOOT_HEAD = boot.replace(REPLAY_OLD, REPLAY_NEW)
        frame.ENGINE_JS = eng + CTRL_JS.replace('@TOPC@', str(TOPC)).replace('@VISD@', str(VISD))
        return frame.build(n, m.SUMMARY, m.ARIA, m.WIN, HEAD_CSS + m.CSS + CTRL_CSS, m.JS, m.STEPS, st)
    finally:
        frame.BOOT_HEAD, frame.ENGINE_JS = boot, eng
