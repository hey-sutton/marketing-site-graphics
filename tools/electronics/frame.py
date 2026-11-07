"""
Shared frame and engine for the Electronics cards (graphics/electronics/card-N.js).

Frame: the Brewery card's frame (shadow DOM host, Studio badge and popover, Replay, captions, ghost cursor,
visibility observer) with the 716 by 640 window from tools/dairy/gfx_scaffold.py, a squared bottom right corner,
step arrows and ripple hotspots.

Engine: one step list per card, run in two modes (Simon, November 6, 2026).
  * Watch (default when the card scrolls into view): every step runs on its own, ghost cursor, ripple, caption,
    gray pill "Watching n of N", hold 2.5 s after the last step, reset and loop.
  * Try it (any click inside the product window while Watch runs, or the Try it toggle): restarts at step 1,
    no ghost, yellow pill "Your turn n of N", the rest of the screen dims, the target pulses, a prompt sits
    below it, a caption follows every click, then the next prompt 1.4 s later. Green "Done" at the end.
Each step is data, written once: {id, target(), prompt, run(quick), after:[title, text] or function, back(), ok(), where}.
Watch calls run() after moving the cursor to target(); Try it calls run() from the reader's click.

Timing and wording live in the TUNE object at the top of the engine, so the feel is easy to adjust.
"""
import json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
sys.path.append(os.path.join(REPO, 'tools', 'dairy'))
from gfx_scaffold import Scaffold, COMMON_CSS  # noqa: E402

KEY = 'electronics'   # build scripts for other industries set frame.KEY and frame.LABEL
LABEL = 'Electronics'

ENGINE_CSS = (
 # top bar: Watch | Try it toggle, status pill, Replay
 '.tbar{position:absolute;top:9px;right:12px;z-index:7;display:flex;align-items:center;gap:6px}'
 '.tbar .rp{position:static;display:inline-flex;align-items:center;gap:6px}.tbar .rp svg{width:13px;height:13px;flex:none}'
 '.mtg{display:inline-flex;height:30px;padding:2px;gap:2px;border:1px solid rgba(0,0,0,.08);border-radius:9px;background:rgba(255,255,255,.92);-webkit-backdrop-filter:blur(8px);backdrop-filter:blur(8px)}'
 '.mtg button{font:inherit;font-size:12.5px;font-weight:500;padding:0 10px;border:0;border-radius:7px;background:transparent;color:#52525B;cursor:pointer;transition:background-color .2s,color .2s}'
 '.mtg button[aria-pressed="true"]{background:#1B1B1A;color:#fff}.mtg button:focus-visible{outline:2px solid #1B1B1A;outline-offset:1px}'
 '.mode{height:30px;display:inline-flex;align-items:center;gap:7px;padding:0 11px;border-radius:9px;font-size:12.5px;font-weight:500;background:rgba(255,255,255,.92);color:#2A2A28;border:1px solid rgba(0,0,0,.08);white-space:nowrap}'
 '.mode .dt{width:8px;height:8px;border-radius:50%;background:#A1A1AA;flex:none}.mode .mc{color:#71717A;font-weight:400}'
 '.mode.t{background:#FFB92B;color:#1B1B1A;border-color:transparent}.mode.t .dt{background:#1B1B1A;animation:capdot 1.3s ease-in-out infinite}.mode.t .mc{color:#5B3F00}'
 '.mode.d{background:#DCFCE7;color:#166534;border-color:#BBF7D0}.mode.d .dt{background:#166534}.mode.d .mc{color:#166534}'
 '.shot.sopen .tbar .mode{visibility:hidden}.shot.nar.sopen .tbar{visibility:hidden}'
 # narrow cards
 '.pop{width:min(348px,calc(var(--cw,604px) - 28px))}.shot.nar .pop{padding:14px}.shot.nar .pop .examples,.shot.nar .pop .rows{display:none}.shot.nar .pop .lede{margin-bottom:10px;font-size:13px}'
 '.shot.nar .win-host{top:44px}.shot.nar .mode .mc{display:none}.shot.nar .tbar{right:8px;gap:4px}.shot.nar .tbar .rp{padding:0 8px}.shot.nar .tbar .rp span{display:none}.shot.nar .mtg button{padding:0 7px;font-size:11.5px}.shot.nar .mode{padding:0 8px;font-size:11.5px}.shot.nar .studio{left:8px}'
 # focus, pulse, press, hotspot
 '.fade{opacity:.4;transition:opacity .25s ease}'
 '.hint{animation:exhint 1.8s ease-out infinite}@keyframes exhint{0%{box-shadow:0 0 0 0 rgba(255,185,43,.75)}70%{box-shadow:0 0 0 8px rgba(255,185,43,0)}100%{box-shadow:0 0 0 0 rgba(255,185,43,0)}}'
 '.press{animation:express .6s ease-out 1}@keyframes express{0%{transform:scale(1)}25%{transform:scale(.94)}55%{transform:scale(1)}}'
 '.hs.flash{opacity:1;animation:hsf .9s ease-out 1 forwards}@keyframes hsf{0%{opacity:1;box-shadow:0 0 0 0 rgba(255,185,43,.7)}100%{opacity:0;box-shadow:0 0 0 14px rgba(255,185,43,0)}}'
 '.sr{position:absolute;width:1px;height:1px;margin:-1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap;border:0}'
 '.cap{max-width:330px}.cap.turn{max-width:300px}.cap .s{font-size:10.6px}'
 # window base used by every card
 '.fwin button{font:inherit;color:inherit}.fwin *{box-sizing:border-box}'
 '.hd{height:44px;padding:0 16px;display:flex;align-items:center;gap:9px;border-bottom:1px solid #E4E4E7}.hd .tt{font-size:12.6px;font-weight:600;white-space:nowrap}.hd .sb{color:#71717A;font-size:10.2px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}'
 '.grow{flex:1;min-width:0}.mono{font-family:"JetBrains Mono",ui-monospace,SFMono-Regular,Menlo,monospace;letter-spacing:-.01em}.mut{color:#71717A}.r{text-align:right}'
 '.ch{display:inline-flex;align-items:center;gap:4px;padding:2px 6px;border-radius:4px;font-size:9.2px;font-weight:500;white-space:nowrap;line-height:1.35;transition:background-color .35s ease,color .35s ease}'
 '.c-ok{background:#DCFCE7;color:#166534}.c-warn{background:#FEF3C7;color:#92400E}.c-bad{background:#FEE2E2;color:#B91C1C}.c-idle{background:#F4F4F5;color:#52525B}.c-info{background:#E8EEFC;color:#1E3A8A}'
 '.cd{border:1px solid #E4E4E7;border-radius:8px;background:#fff;overflow:hidden}.ct{display:flex;align-items:center;justify-content:space-between;gap:8px;height:30px;padding:0 11px;border-bottom:1px solid #E4E4E7;font-weight:600;font-size:10.6px}'
 '.bt{font-size:10.2px;padding:5px 10px;border:1px solid #E4E4E7;border-radius:6px;background:#fff;font-weight:500;cursor:pointer;white-space:nowrap;transition:background-color .2s,border-color .2s,color .2s,opacity .25s}'
 '.bt:hover{background:#F4F4F5}.bt:focus-visible{outline:2px solid #18181B;outline-offset:2px}.bt.pri{background:#18181B;border-color:#18181B;color:#fff}.bt.pri:hover{background:#3F3F46}'
 '.bt.done{background:#DCFCE7;border-color:#BBF7D0;color:#166534;cursor:default}.bt.fakehover{background:#F4F4F5}.bt.pri.fakehover{background:#3F3F46}.bt[hidden]{display:none}'
 '.tabs{height:30px;padding:0 12px;display:flex;align-items:flex-end;gap:16px;border-bottom:1px solid #E4E4E7}'
 '.tab{border:0;background:none;padding:0 2px 8px;color:#52525B;cursor:pointer;position:relative;font-size:10.4px;border-radius:5px 5px 0 0}.tab.on{color:#18181B;font-weight:600}.tab.on::after{content:"";position:absolute;left:0;right:0;bottom:-1px;height:2px;background:#18181B;border-radius:2px}.tab:focus-visible{outline:2px solid #18181B;outline-offset:2px}'
 '.row{display:grid;align-items:center;min-height:26px;padding:0 11px;border-top:1px solid #F0F0F1;gap:8px}.row.h{min-height:24px;background:#FAFAFA;color:#71717A;font-size:9.2px;font-weight:500;border-top:0}'
 'button.row{width:100%;border-left:0;border-right:0;border-bottom:0;background:#fff;text-align:left;cursor:pointer;transition:background-color .2s}button.row:hover,button.row.fakehover{background:#FAFAFA}button.row.sel{background:#F4F4F5;box-shadow:inset 3px 0 0 #18181B}button.row:focus-visible{outline:2px solid #18181B;outline-offset:-2px}'
 '.in{animation:exin .45s cubic-bezier(.22,.9,.28,1) both}@keyframes exin{from{opacity:0;transform:translateY(5px)}}'
 '.flash{animation:exflash 1.2s ease}@keyframes exflash{0%{background:#FFF4D6}100%{background:transparent}}'
 '.fld{display:flex;flex-direction:column;gap:3px;min-width:0}.fld small{color:#71717A;font-size:8.9px}.fld input{font:inherit;font-family:"JetBrains Mono",ui-monospace,monospace;font-size:10px;padding:5px 7px;border:1px solid #D4D4D8;border-radius:6px;background:#fff;color:#18181B;width:100%;min-width:0}'
 '.fld input:focus-visible{outline:2px solid #18181B;outline-offset:1px}.fld.err input{border-color:#F87171;background:#FEF2F2}.fld .em{display:none;color:#B91C1C;font-size:8.8px}.fld.err .em{display:block}'
 '.empt{display:flex;flex-direction:column;align-items:center;justify-content:center;gap:5px;text-align:center;color:#71717A;border:1px dashed #E4E4E7;border-radius:8px;background:#FAFAFA;padding:18px 14px;line-height:1.4}.empt b{font-size:10.8px;font-weight:600;color:#18181B}.empt span{font-size:9.6px;max-width:300px}'
 '.kv{display:flex;flex-direction:column;gap:2px}.kv small{color:#71717A;font-size:8.9px}.kv b{font-weight:600;font-size:10.6px}.big{font-size:22px;font-weight:600;letter-spacing:-.02em;line-height:1.1}'
)

ENGINE_JS = r'''
/* ===== Watch and Try it engine (shared by the four Electronics cards). Tune the feel here. ===== */
var TUNE={startDelay:600,lead:900,press:300,dwell:2900,hold:2500,nextPrompt:1400,watch:'Watching',turn:'Your turn',done:'Done'};
var mode='watch',cur=0,watchOn=false;
var bar=document.createElement('div');bar.className='tbar';
var tgl=document.createElement('div');tgl.className='mtg';tgl.setAttribute('role','group');tgl.setAttribute('aria-label','Demo mode');
tgl.innerHTML='<button type="button" data-m="watch" aria-pressed="true">Watch</button><button type="button" data-m="try" aria-pressed="false">Try it</button>';
var md=document.createElement('div');md.className='mode';md.setAttribute('aria-hidden','true');
bar.appendChild(tgl);bar.appendChild(md);bar.appendChild(rp);shot.appendChild(bar);
var live=document.createElement('div');live.className='sr';live.setAttribute('aria-live','polite');winEl.appendChild(live);
var hs=$('hs'),pv=$('pv'),nx=$('nx'),sn=$('sn');
function setPill(){var n=mode==='done'?NS:Math.min(cur+1,NS),k=mode==='watch'?'':mode==='try'?'t':'d',t=mode==='watch'?TUNE.watch:mode==='try'?TUNE.turn:TUNE.done;
md.className='mode '+k;md.innerHTML='<span class="dt"></span><span>'+t+'</span><span class="mc">'+n+' of '+NS+'</span>';
[].forEach.call(tgl.children,function(b){b.setAttribute('aria-pressed',(b.getAttribute('data-m')==='watch')===(mode==='watch')?'true':'false');});
sn.textContent=n+' of '+NS;pv.disabled=mode!=='done'&&cur<=0;nx.disabled=mode==='done'||cur>=NS-1;}
function placeBox(box,l,t){var w=box.offsetWidth,hh=box.offsetHeight;box.style.left=Math.max(8,Math.min(visW()-w-8,l))+'px';box.style.top=Math.max(48,Math.min(visH()-hh-8,t))+'px';}
function capPos(){var hh=cap.offsetHeight;return typeof CAPAT==='function'?CAPAT(hh):{l:14,t:visH()-hh-14};}
function caption(i){var s=ST[i],a=typeof s.after==='function'?s.after():s.after;say2(i+1,a[0],a[1]);}
function say2(num,main,sub){clearTimeout(capT);live.textContent=main+(sub?'. '+sub:'');var run=function(){cap.innerHTML='<div class="m"><i>'+num+'</i>'+main+'</div>'+(sub?'<div class="s">'+sub+'</div>':'');cap.className='cap';cap.style.left='-999px';void cap.offsetWidth;var p=capPos();placeBox(cap,p.l,p.t);void cap.offsetWidth;cap.classList.add('on');};if(cap.classList.contains('on')){cap.classList.remove('on');capT=setTimeout(run,180);}else run();}
function hush(){clearTimeout(capT);cap.classList.remove('on');}
function prompt2(text,el,where){live.textContent=text;turn.innerHTML='<div class="m"><span class="pd"></span>'+text+'</div>';turn.className='cap turn';turn.style.left='-999px';void turn.offsetWidth;
var r=rel(el),hh=turn.offsetHeight,w=turn.offsetWidth,l=where==='right'?r.l+r.w+10:(where==='end'?r.l+r.w-w:r.l),t=where==='above'?r.t-hh-8:(where==='right'?r.t+r.h/2-hh/2:r.t+r.h+8);
if(where!=='above'&&where!=='right'&&t+hh>visH()-8)t=r.t-hh-8;placeBox(turn,l,t);void turn.offsetWidth;turn.classList.add('on');}
function turnOff(){turn.classList.remove('on');}
function hot(el,flash){if(!el){hs.className='hs';return;}var r=rel(el);hs.style.left=(r.l-3)+'px';hs.style.top=(r.t-3)+'px';hs.style.width=(r.w+6)+'px';hs.style.height=(r.h+6)+'px';hs.className='hs';void hs.offsetWidth;hs.className='hs '+(flash?'flash':'on');}
function clearHints(){[].slice.call(root.querySelectorAll('.hint,.fakehover,.press')).forEach(function(b){b.classList.remove('hint','fakehover','press');});}
function focusOff(){[].slice.call(root.querySelectorAll('.fade')).forEach(function(x){x.classList.remove('fade');});}
function focusOn(el){focusOff();if(!el)return;[].slice.call(winEl.querySelectorAll(FOC)).forEach(function(x){if(x===el||x.contains(el)||el.contains(x))return;x.classList.add('fade');});}
function cancelAll(){timers.forEach(clearTimeout);timers=[];watchOn=false;ghost.classList.remove('on','pr');hush();turnOff();clearHints();focusOff();hot(null);}
function gpos(el){var r=rel(el);return{l:r.l+Math.min(r.w*0.5,60),t:r.t+r.h*0.55};}
function watchStep(i,delay){cur=i;
later(function(){setPill();var el=ST[i].target();if(el)moveGhost(gpos(el));},delay);
later(function(){var el=ST[i].target();ghost.classList.add('pr');if(el){el.classList.add('fakehover','press');hot(el,true);}},delay+TUNE.lead);
later(function(){var el=ST[i].target();ghost.classList.remove('pr');if(el)el.classList.remove('fakehover','press');ST[i].run(false);caption(i);},delay+TUNE.lead+TUNE.press);
var end=delay+TUNE.lead+TUNE.press+TUNE.dwell;
if(i+1<NS)later(function(){watchStep(i+1,0);},end);
else later(function(){hush();ghost.classList.remove('on');later(function(){if(mode==='watch'&&visible)startWatch();},400);},end+TUNE.hold-400);}
function startWatch(){mode='watch';engaged=false;cancelAll();resetState();cur=0;setPill();if(reduce||!visible)return;watchOn=true;ghost.classList.add('on');moveGhost({l:visW()*0.5,t:visH()*0.5},true);watchStep(0,150);}
function showPrompt(){if(mode!=='try')return;var s=ST[cur];clearHints();hot(null);var el=s.target(),txt=s.prompt,b=s.back&&s.back();if(b){el=b[0];txt=b[1];}
if(!el){turnOff();return;}focusOn(el);el.classList.add('hint');hot(el,false);setPill();prompt2(TUNE.turn+'. '+txt,el,b?(b[2]||'below'):(s.where||'below'));}
function startTry(){mode='try';engaged=true;cancelAll();resetState();cur=0;setPill();showPrompt();}
function doStep(){var s=ST[cur];if(s.ok&&!s.ok()){showPrompt();return;}clearHints();turnOff();focusOff();hot(null);s.run(false);caption(cur);
if(cur+1<NS){cur++;setPill();later(showPrompt,TUNE.nextPrompt);}else{mode='done';setPill();}}
function jump(i){if(i<0||i>=NS)return;var m=mode==='watch'?'watch':'try';cancelAll();resetState();for(var k=0;k<i;k++)ST[k].run(true);cur=i;
if(m==='watch'&&!reduce){mode='watch';watchOn=true;ghost.classList.add('on');setPill();watchStep(i,150);}else{mode='try';engaged=true;setPill();showPrompt();}}
pv.addEventListener('click',function(e){e.stopPropagation();jump(mode==='done'?NS-1:cur-1);});
nx.addEventListener('click',function(e){e.stopPropagation();jump(cur+1);});
tgl.addEventListener('click',function(e){var b=e.target.closest&&e.target.closest('button');if(!b)return;if(b.getAttribute('data-m')==='watch'){visible=true;startWatch();}else startTry();});
rp.addEventListener('click',function(){if(mode==='watch'){visible=true;startWatch();}else startTry();});
winEl.addEventListener('click',function(e){if(e.target.closest&&e.target.closest('.stp'))return;
if(mode==='watch'){e.preventDefault();e.stopPropagation();startTry();return;}
if(mode==='try'){var s=ST[cur],el=s.target(),b=s.back&&s.back();
if(!b&&el&&(el===e.target||el.contains(e.target))){e.preventDefault();e.stopPropagation();doStep();return;}
if(e.target.closest&&e.target.closest('input'))return;
setTimeout(showPrompt,40);}},true);
winEl.addEventListener('keydown',function(e){if(e.key==='Enter'&&e.target.tagName==='INPUT'&&mode==='try'){e.preventDefault();var s=ST[cur],el=s.target();if(el&&el.closest('.frm')&&el.closest('.frm').contains(e.target))doStep();}e.stopPropagation();});
root.addEventListener('scroll',function(e){var t=e.target;if(t&&t.nodeType===1&&(t.scrollTop||t.scrollLeft)&&!t.closest('.pop')){t.scrollTop=0;t.scrollLeft=0;}},true);
function onResize(){if(mode==='try')later(showPrompt,60);}
if('ResizeObserver'in window)new ResizeObserver(function(){onResize();}).observe(host.parentNode);
function startObserver(){if('IntersectionObserver'in window){new IntersectionObserver(function(es){es.forEach(function(en){visible=en.intersectionRatio>=0.3;
if(visible&&mode==='watch'&&!watchOn&&!reduce){watchOn=true;later(startWatch,TUNE.startDelay);}
if(!visible&&mode==='watch'&&watchOn){cancelAll();resetState();cur=0;setPill();}});},{threshold:[0,0.3,0.6]}).observe(host.parentNode);}else{visible=true;later(startWatch,TUNE.startDelay);}}
'''

BOOT_HEAD = r'''function boot(root){
var reduce=window.matchMedia('(prefers-reduced-motion: reduce)').matches;
var shot=root.querySelector('.shot');
var studios=[].slice.call(root.querySelectorAll('[data-studio]')),closeTimer=new WeakMap();
function setOpen(el,o){el.classList.toggle('open',o);shot.classList.toggle('sopen',o);el.querySelector('.studio-chip').setAttribute('aria-expanded',o?'true':'false');}
function refreshStudio(el){setOpen(el,!!(el._hover||el._pinned||el._focus));}
studios.forEach(function(el){var b=el.querySelector('.studio-chip');
el.addEventListener('pointerenter',function(e){if(e.pointerType!=='mouse')return;clearTimeout(closeTimer.get(el));el._hover=true;refreshStudio(el);});
el.addEventListener('pointerleave',function(e){if(e.pointerType!=='mouse')return;closeTimer.set(el,setTimeout(function(){el._hover=false;refreshStudio(el);},140));});
b.addEventListener('click',function(){el._pinned=!el._pinned;refreshStudio(el);});
el.addEventListener('focusin',function(){if(el.querySelector(':focus-visible')){el._focus=true;refreshStudio(el);}});
el.addEventListener('focusout',function(e){if(!el.contains(e.relatedTarget)){el._focus=false;refreshStudio(el);}});});
document.addEventListener('click',function(e){studios.forEach(function(el){if(e.composedPath().indexOf(el)<0){el._pinned=false;refreshStudio(el);}});});
document.addEventListener('keydown',function(e){if(e.key!=='Escape')return;studios.forEach(function(el){el._pinned=el._hover=el._focus=false;refreshStudio(el);});});
var rp=document.createElement('button');rp.className='rp';rp.type='button';rp.innerHTML='<svg viewBox="0 0 14 14" fill="none" aria-hidden="true"><path d="M2.5 7a4.5 4.5 0 1 0 1.4-3.3M2.5 2v2.6h2.6" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"/></svg><span>Replay</span>';rp.setAttribute('aria-label','Replay');
var host=root.querySelector('.win-host'),winEl=host.querySelector('.fwin');
function fit(){var cw=host.parentNode.clientWidth;host.style.transform='scale('+(cw/742)+')';shot.style.setProperty('--cw',cw+'px');shot.classList.toggle('nar',cw<430);}
fit();if('ResizeObserver'in window)new ResizeObserver(fit).observe(host.parentNode);window.addEventListener('resize',fit);
var $=function(i){return root.getElementById(i);};
var engaged=false,visible=false,timers=[],capT=null;
function later(fn,ms){var x=setTimeout(fn,ms);timers.push(x);return x;}
var ghost=document.createElement('div');ghost.className='fw-ghost';ghost.innerHTML='<svg width="16" height="20" viewBox="0 0 16 20" fill="none"><path d="M2 1.5v14l3.6-3.4 2.4 5.4 2.3-1-2.4-5.3h5L2 1.5z" fill="#fff" stroke="#18181B" stroke-width="1.2" stroke-linejoin="round"/></svg>';winEl.appendChild(ghost);
var cap=document.createElement('div');cap.className='cap';winEl.appendChild(cap);
var turn=document.createElement('div');turn.className='cap turn';winEl.appendChild(turn);
function scaleS(){return host.getBoundingClientRect().width/host.offsetWidth||1;}
function rel(el){var s=scaleS(),w=winEl.getBoundingClientRect(),r=el.getBoundingClientRect();return{l:(r.left-w.left)/s,t:(r.top-w.top)/s,w:r.width/s,h:r.height/s};}
function moveGhost(pos,instant){if(instant)ghost.style.transition='none';ghost.style.left=pos.l+'px';ghost.style.top=pos.t+'px';if(instant){void ghost.offsetWidth;ghost.style.transition='';}}
function visW(){return Math.min(winEl.offsetWidth,(host.parentNode.clientWidth-host.offsetLeft)/scaleS());}
function visH(){return Math.min(winEl.offsetHeight,(host.parentNode.clientHeight-host.offsetTop)/scaleS());}
function m2(n){return '$'+n.toLocaleString('en-US',{minimumFractionDigits:2,maximumFractionDigits:2});}
function n0(n){return n.toLocaleString('en-US');}
'''

TAIL = r'''
resetState();setPill();
if(reduce){startTry();}
startObserver();
}
})();
'''


def studio(lede, examples, built_on, change):
    ex = ''.join('<li style="--i:%d">%s</li>' % (i, e) for i, e in enumerate(examples))
    sc = Scaffold.studio(lede, examples, built_on)
    sc = sc.replace('<dd>Fields, wording and workflow</dd>', '<dd>' + change + '</dd>')
    assert ex in sc and change in sc
    return sc


def build(n, summary, aria, win, css, js, steps, studio_html):
    sc = Scaffold(REPO)
    base_css = sc.css + COMMON_CSS + ENGINE_CSS + css
    body = ('<div class="sx-stage"><div class="shot"><div class="shot-img"><div class="win-host" role="group" aria-label="' + aria + '"><div class="fwin">'
            + win + sc.chevrons().replace('1 of 5', '1 of %d' % steps) + '</div></div></div>' + studio_html + '</div></div>')
    pre = sc.pre
    rule = '.capabilities_card-visual[data-sx-industry*="%s"]{border-bottom-right-radius:0}' % KEY
    assert pre.count("{aspect-ratio:604/523}}'") == 1
    pre = pre.replace("{aspect-ratio:604/523}}'", "{aspect-ratio:604/523}}" + rule + "'")
    pre = pre.replace("'brewery'", "'%s'" % KEY).replace('sx-brewery-card-css', 'sx-%s-card-css' % KEY).replace('data-sx-industry*="brewery"', 'data-sx-industry*="%s"' % KEY)
    assert 'brewery' not in pre
    out = [('/* %s, card %d: %s\n   Loaded by the site loader. Mounts into the card visual passed in by the loader.\n   Source of truth: tools/%s/build.py. Edit there, rebuild, open a pull request, then release a new tag. */' % (LABEL, n, summary, KEY)),
           '(function(){',
           "var SRC=document.currentScript&&document.currentScript.src;var BGU=SRC?new URL('bg-%d.jpg',SRC).href:'';" % n,
           'var CSS=' + json.dumps(base_css) + ".replace('__BG__',BGU);",
           'var BODY=' + json.dumps(body) + ';',
           pre.rstrip('\n'), BOOT_HEAD.rstrip('\n'), ('var NS=%d;' % steps) + js.rstrip('\n'), ENGINE_JS.rstrip('\n'), TAIL.strip('\n')]
    res = '\n'.join(out) + '\n'
    d = os.path.join(REPO, 'graphics', KEY)
    os.makedirs(d, exist_ok=True)
    open(os.path.join(d, 'card-%d.js' % n), 'w', encoding='utf-8').write(res)
    return len(res.encode())
