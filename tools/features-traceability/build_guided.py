#!/usr/bin/env python3
"""
Features, traceability: rebuild cards 1 to 6 with the guided handoff (Simon's Loom, November 6, 2026).

  * One step autoplay intro (status pill: Watching), then a hard handoff (Your turn), then Done.
  * One dimmed, pulsing target at a time with the prompt beside it, a caption after every click.
  * Inputs prefilled, nothing derived from them shows until the reader runs the step.
  * 4 steps for the simple cards, 5 for the complex ones, and the screen changes at every step.
  * The last caption always says what to do next.

Card 2 is the approved Serialized inventory prototype (tools/features-traceability/card-2-prototype.js).
Cards 1, 3, 4, 5 and 6 keep their window, data and render code; this script swaps the old looping
autoplay for the intro plus guided steps. Run from the repo root:

  python3 tools/features-traceability/build_guided.py
"""
import os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DIR = os.path.join(ROOT, "graphics", "features-traceability")
HERE = os.path.dirname(os.path.abspath(__file__))


def one(s, old, new, label):
    n = s.count(old)
    if n != 1:
        sys.exit("%s: expected 1 match, found %d" % (label, n))
    return s.replace(old, new)


# Extra CSS, the same as the prototype: status pill, fade, narrow card popover.
CSS_ADD = (
    ".mode{position:absolute;top:10px;right:92px;z-index:6;height:30px;display:inline-flex;align-items:center;gap:7px;padding:0 12px;border-radius:9px;font-size:13px;font-weight:500;background:rgba(255,255,255,.92);color:#2A2A28;border:1px solid rgba(0,0,0,.08);white-space:nowrap}"
    ".mode .dt{width:8px;height:8px;border-radius:50%;background:#A1A1AA}.mode .mc{color:#71717A;font-weight:400}"
    ".mode.t{background:#FFB92B;color:#1B1B1A;border-color:transparent}.mode.t .dt{background:#1B1B1A;animation:capdot 1.3s ease-in-out infinite}.mode.t .mc{color:#5B3F00}"
    ".mode.d{background:#DCFCE7;color:#166534;border-color:#BBF7D0}.mode.d .dt{background:#166534}.mode.d .mc{color:#166534}"
    ".fade{opacity:.4;transition:opacity .25s ease}"
    ".pop{width:min(348px,calc(var(--cw,604px) - 28px))}.shot.nar .pop{padding:14px}.shot.nar .pop .examples,.shot.nar .pop .rows{display:none}.shot.nar .pop .lede{margin-bottom:10px}"
    ".shot.nar .mode .mc{display:none}.shot.nar .mode{right:84px;padding:0 10px}.studio.open~.mode{opacity:0;visibility:hidden}"
)

# Shared guided engine. Each card defines FOC (what dims), NSTEP, G (steps) and INTRO (caption + point target).
ENGINE = r"""
var yt=false,gi=0;
var md=document.createElement('div');md.className='mode';md.setAttribute('aria-hidden','true');shot.appendChild(md);
function setMode(k,t,n){md.className='mode '+k;md.innerHTML='<span class="dt"></span><span>'+t+'</span><span class="mc">'+n+' of '+NSTEP+'</span>';}
function focusOff(){[].slice.call(root.querySelectorAll('.fade')).forEach(function(x){x.classList.remove('fade');});}
function focusOn(el,keep){focusOff();if(!el)return;keep=(keep||[]).concat([el]);[].slice.call(root.querySelectorAll(FOC)).forEach(function(x){for(var i=0;i<keep.length;i++){var k=keep[i];if(!k)continue;if(x===k||x.contains(k)||k.contains(x))return;}x.classList.add('fade');});}
function startGuided(i){engaged=true;yt=true;gi=i;showPrompt();}
function showPrompt(){var g=G[gi];if(!g)return;clearHints();var el=g.tg();if(!el)return;focusOn(el,g.keep?g.keep():null);el.classList.add('hint');setMode('t','Your turn',g.n);turnSay(g.t,el,g.w||'below');
var r=rel(el),tw=turn.offsetWidth,th=turn.offsetHeight;
if(g.p==='bl')placeCap(turn,r.l,r.t+r.h+10);else if(g.p==='br')placeCap(turn,r.l+r.w-tw,r.t+r.h+10);else if(g.p==='al')placeCap(turn,r.l,r.t-th-10);else if(g.p==='ar')placeCap(turn,r.l+r.w-tw,r.t-th-10);}
function act(a){if(!yt)return;var g=G[gi];if(!g||g.a!==a){showPrompt();return;}
clearHints();turnOff();focusOff();var f=g.after;say(f[0],f[1],f[2],null);gi++;
if(gi<G.length){later(showPrompt,1500);}else{yt=false;setMode('d','Done',NSTEP);}}
function prompt(){startGuided(0);}
function script(){var t=1200;
later(function(){setMode('','Watching',1);say(1,INTRO[0],INTRO[1]);},t-900);point(INTRO[2],t,INTRO[3],INTRO[4]);t+=3800;
later(function(){hush();ghost.classList.remove('on');},t);t+=500;
later(function(){startGuided(0);},t);
return t+300;}
"""

# Per card: everything between "var S;" and "if(!STATIC)host.addEventListener" is replaced.
# Each card keeps its original data and render functions; only event wiring, resetState, prompt and script change.
CARDS = {}

CARDS[1] = dict(
    comment="Batch and lot tracking. One step intro, then three guided clicks: complete the order (lot and best by assigned), open Cost, open Shipments.",
    keep_from="var S;", keep_to="function prompt(){",
    drop=["cmp.addEventListener('click',complete);"],
    wire=r"""
cmp.addEventListener('click',function(){complete();act('complete');});
tabs.forEach(function(b){b.addEventListener('click',function(){act('tab:'+b.getAttribute('data-t'));});});
""",
    reset_extra="",
    foc=".fw-head>*,.meta,.fw-tab,#cbox",
    nstep=4,
    intro=["MO-2291 is packed and ready to close", "1,200 cases of granola. The lot number is set when you complete it.", "function(){return $('cbox');}", 200, 60],
    G=r"""[
{n:2,a:'complete',tg:function(){return cmp;},t:'Your turn. Click Complete order',w:'below',p:'br',after:[2,'Lot GR-1021A is assigned for you','Best by 04/19/2027 from the item shelf life. Every input lot is on the record.']},
{n:3,a:'tab:co',tg:function(){return tabs[1];},t:'Your turn. Open Cost',p:'bl',after:[3,'Actual cost per case, $18.40','$22,080.00 over 1,200 cases, $0.25 under plan.']},
{n:4,a:'tab:sh',tg:function(){return tabs[2];},t:'Your turn. Open Shipments',p:'bl',after:[4,'Where every case went','1,200 cases to 5 customers, by sales order. Open Inputs to see each ingredient lot.']}]""",
)

CARDS[3] = dict(
    comment="Regulations and compliance. One step intro, then four guided clicks: open the supplier COA, open a QC photo, build the FSMA 204 sheet, sort it by date.",
    keep_from="var S;", keep_to="function prompt(){",
    drop=[],
    wire=r"""
$('checks').addEventListener('click',function(e){var b=e.target.closest&&e.target.closest('.ckb');if(b)act('view:'+b.getAttribute('data-k'));});
exp.addEventListener('click',function(){act('export');});
$('srt').addEventListener('click',function(){act('sort');});
""",
    reset_extra="",
    foc=".fw-head>*,.chk .ch,#checks .tr,.att,.pv,.sh>*,.grid,.sf>*",
    nstep=5,
    intro=["Every check on lot AB-1024B, in one record", "5 of 5 passed, with the supplier COA and photos attached.", "function(){return $('checks');}", 220, 70],
    G=r"""[
{n:2,a:'view:coa',tg:function(){return root.querySelector('.ckb[data-k="coa"]');},t:'Your turn. Click View COA',w:'below',p:'br',after:[2,'The supplier COA rides with the lot','Within spec, attached at receiving on RT-3307.']},
{n:3,a:'view:md',tg:function(){return root.querySelector('.ckb[data-k="md"]');},t:'Your turn. Open the metal detector photo',w:'below',p:'br',after:[3,'QC checks with photos','Who did it, when, and the result, on every step.']},
{n:4,a:'export',tg:function(){return exp;},t:'Your turn. Export the FSMA 204 sheet',w:'below',p:'br',after:[4,'The FSMA 204 sheet, built for you','Every key data element for AB-1024B: received, made and shipped.']},
{n:5,a:'sort',tg:function(){return $('srt');},t:'Your turn. Sort by date',w:'below',p:'br',after:[5,'Sorted, newest first','300 cases shipped to 3 customers. Download the .xlsx when an inspector asks.']}]""",
)

CARDS[4] = dict(
    comment="Inventory control. One step intro, then three guided clicks: sort by best by, open a bin's lot cost history, preview the low stock alert.",
    keep_from="var S;", keep_to="function prompt(){",
    drop=[],
    wire=r"""
$('bins').addEventListener('click',function(e){var b=e.target.closest&&e.target.closest('button.tr');if(b)act('bin:'+b.getAttribute('data-b'));});
srt.addEventListener('click',function(){act('sort');});
alb.addEventListener('click',function(){act('alert');});
""",
    reset_extra="",
    foc=".fw-head,.kp,.tool>*,#bins .tr,.lower",
    nstep=4,
    intro=["Every bin, every lot", "10,440 lb of almonds in 3 bins, each lot valued at what you paid.", "function(){return $('bins');}", 300, 60],
    G=r"""[
{n:2,a:'sort',tg:function(){return srt;},t:'Your turn. Sort by best by',w:'below',p:'br',after:[2,'Oldest best by goes first','Lot SN-24-0802 is flagged to use first.']},
{n:3,a:'bin:RM-A1',tg:function(){return $('bins').querySelector('[data-b="RM-A1"]');},t:'Your turn. Open bin RM-A1',w:'below',p:'bl',after:[3,'Cost history on every lot','16,000 lb received at $4.10, 6,810 lb used, 9,190 lb left.']},
{n:4,a:'alert',tg:function(){return alb;},t:'Your turn. Preview the alert',w:'below',p:'br',after:[4,'A heads up before you run short','Purchasing gets an email every morning below 12,000 lb. Pick any bin to see its lot.']}]""",
)

CARDS[5] = dict(
    comment="Supplier and raw material traceability. One step intro, then three guided clicks with the supplier already filled in: search, open PO-1187, open PO-1142.",
    keep_from="var S;", keep_to="function prompt(){",
    drop=[],
    wire=r"""
go.addEventListener('click',function(){if(S.found)act('search');});
q.addEventListener('keydown',function(e){if(e.key==='Enter'&&S.found)act('search');});
$('pos').addEventListener('click',function(e){var b=e.target.closest&&e.target.closest('button.tr');if(b)act('po:'+b.getAttribute('data-p'));});
""",
    reset_extra="q.value='Sierra Nut Co';",
    foc=".fw-head>*,#supc,#pos .ch,#pos .tr,#det",
    nstep=4,
    intro=["Start from the supplier", "Sierra Nut Co is filled in. You can also search a PO number.", "function(){return q;}", 60, 12],
    G=r"""[
{n:2,a:'search',tg:function(){return go;},keep:function(){return [q];},t:'Your turn. Click Search',w:'below',p:'br',after:[2,'Every PO from this supplier','2 purchase orders, both received and checked at the dock.']},
{n:3,a:'po:PO-1187',tg:function(){return $('pos').querySelector('[data-p="PO-1187"]');},t:'Your turn. Open PO-1187',w:'below',p:'bl',after:[3,'The lot, its COA and every batch','SN-24-0917 went into 3 batches: 6,810 lb used, 9,190 lb on hand.']},
{n:4,a:'po:PO-1142',tg:function(){return $('pos').querySelector('[data-p="PO-1142"]');},t:'Your turn. Open PO-1142',w:'below',p:'bl',after:[4,'Compare the older lot','SN-24-0802 went into 2 batches, 1,250 lb left. Open either PO to switch back.']}]""",
)

CARDS[6] = dict(
    comment="Forward and backward traceability (recall console). One step intro, then four guided clicks through the real recall steps: trace forward, hold on site stock, open the customer list, close it to see the recall steps.",
    keep_from="var S;", keep_to="function prompt(){",
    drop=[],
    wire=r"""
go.addEventListener('click',function(){act('trace');});
hold.addEventListener('click',function(){if(S.held)act('hold');});
cus.addEventListener('click',function(){if(S.list)act('list');});
$('cls').addEventListener('click',function(){act('close');});
""",
    reset_extra="",
    foc=".fw-head,.ban>*,.tree,.kpis,.acts>*,.steps,.sh>*,.cl,.sf>*",
    nstep=5,
    intro=["A supplier flags an almond lot", "Sierra Nut Co, lot SN-24-0917, possible Salmonella.", "function(){return $('ban');}", 180, 24],
    G=r"""[
{n:2,a:'trace',tg:function(){return go;},t:'Your turn. Start the trace',w:'below',p:'br',after:[2,'Traced forward in seconds','3 finished lots, 3,250 cases: 2,410 shipped, 640 on site, 200 in packing.']},
{n:3,a:'hold',tg:function(){return hold;},t:'Your turn. Hold the stock on site',w:'above',p:'al',after:[3,'Everything still here is on hold','640 cases, 200 in packing and 9,190 lb of raw almonds.']},
{n:4,a:'list',tg:function(){return cus;},t:'Your turn. Open the customer list',w:'above',p:'al',after:[4,'Who to call, with order numbers','9 customers and 2,410 cases, pulled from each sales order.']},
{n:5,a:'close',tg:function(){return $('cls');},t:'Your turn. Close the list',w:'below',p:'br',after:[5,'4 of 5 recall steps done','Found, held and listed in minutes. Export the list any time for your customer notices.']}]""",
)


def build(n, cfg):
    path = os.path.join(DIR, "card-%d.js" % n)
    s = open(path, encoding="utf-8").read()
    if "var FOC=" in s:
        sys.exit("card-%d.js is already converted. Restore the v1.19.0 file first: git checkout v1.19.0 -- graphics/features-traceability" % n)
    # header comment
    s = re.sub(r"^/\* Features, traceability, card %d: [^\n]*" % n,
               "/* Features, traceability, card %d: %s" % (n, cfg["comment"]), s, count=1)
    # CSS
    s = one(s, "\".replace('__BG__',BGU);", CSS_ADD.replace('"', '\\"') + "\".replace('__BG__',BGU);", "css %d" % n)
    # fit(): expose card width, narrow mode
    s = one(s, "function fit(){host.style.transform='scale('+(host.parentNode.clientWidth*0.9/640)+')';",
            "function fit(){var cw=host.parentNode.clientWidth;host.style.transform='scale('+(cw*0.9/640)+')';shot.style.setProperty('--cw',cw+'px');shot.classList.toggle('nar',cw<430);", "fit %d" % n)
    # cancelAll also ends guided mode
    s = one(s, "function cancelAll(){timers.forEach(clearTimeout);", "function cancelAll(){focusOff();yt=false;timers.forEach(clearTimeout);", "cancel %d" % n)
    # no more autoplay loop: the intro hands off once
    s = re.sub(r"later\(function\(\)\{tourOn=false;tour\(\);\},total\);", "", s)
    assert "tourOn=false;tour();},total" not in s
    # card specific block
    a = s.index(cfg["keep_from"]); b = s.index(cfg["keep_to"]); e = s.index("if(!STATIC)host.addEventListener('click',engage,true);")
    keep = s[a:b]
    for d in cfg["drop"]:
        keep = one(keep, d, "", "drop %d" % n)
    # resetState: leave guided mode, prefill, set the pill
    keep = one(keep, "function resetState(){", "function resetState(){yt=false;gi=0;focusOff();", "reset %d" % n)
    i = keep.index("function resetState(){") + len("function resetState(){"); depth = 1; j = i
    while depth:  # find the closing brace of resetState
        depth += {"{": 1, "}": -1}.get(keep[j], 0); j += 1
    keep = keep[:j - 1] + cfg["reset_extra"] + "setMode('',reduce?'Your turn':'Watching',1);" + keep[j - 1:]
    intro = cfg["intro"]
    head = "var FOC='%s',NSTEP=%d;\n" % (cfg["foc"], cfg["nstep"])
    tail = (cfg["wire"] + ENGINE +
            "var G=%s;\n" % cfg["G"] +
            "var INTRO=['%s','%s',%s,%d,%d];\n\n" % (intro[0], intro[1], intro[2], intro[3], intro[4]))
    # the engine defines setMode, which resetState calls: hoisted function declarations, so order is fine
    s = s[:a] + head + keep + tail + s[e:]
    open(path, "w", encoding="utf-8").write(s)
    print("card-%d.js  %.1f KB" % (n, len(s.encode()) / 1024))


def card2():
    s = open(os.path.join(HERE, "card-2-prototype.js"), encoding="utf-8").read()
    s = s.replace("/* Features, traceability, card 2 (REVISED PROTOTYPE): Serialized inventory.",
                  "/* Features, traceability, card 2: Serialized inventory.", 1)
    assert "PROTOTYPE" not in s
    open(os.path.join(DIR, "card-2.js"), "w", encoding="utf-8").write(s)
    print("card-2.js  %.1f KB" % (len(s.encode()) / 1024))


if __name__ == "__main__":
    card2()
    for n, cfg in CARDS.items():
        build(n, cfg)
