"""Worked example: builds graphics/dairy/card-1.js from the Brewery card scaffold.
Use it as a starting point for a new card: keep the scaffold (shadow DOM host, Studio badge and popover, Replay,
hint pill, ghost cursor, captions, observer), replace the product window HTML, the data and the script().
Usage:  GFX_REPO=/path/to/marketing-site-graphics GFX_OUT=/path/to/output-repo python3 build_card.py
GFX_REPO must contain graphics/brewery/card-1.js (download from raw.githubusercontent.com). GFX_OUT is written to graphics/dairy/card-1.js.
"""
import json,re,os
REPO=os.environ.get('GFX_REPO','marketing-site-graphics');OUT=os.environ.get('GFX_OUT','out')
src=open(os.path.join(REPO,'graphics/brewery/card-1.js')).read()
lines=src.split('\n')
css_line=lines[5]
css=css_line[css_line.index('"')+1:css_line.rindex('"')].replace('\\"','"').replace('\\\\','\\')
css=css[:css.index('.pl-two{')]   # scaffold only: drop brewery specific rules
# Right edge rule (Simon, Oct 27 and 28): no border or rounded corner may show at the card's right edge.
# The window is 716 design px wide (the scaffold's 686 ended about 1 px short of the edge) so it runs about 30 design px past the card.
assert css.count('.win-host{position:absolute;left:7.4%;top:9%;width:686px;height:604px')==1 and css.count('.fwin{position:relative;width:686px;height:604px')==1
css=css.replace('.win-host{position:absolute;left:7.4%;top:9%;width:686px;height:604px','.win-host{position:absolute;left:7.4%;top:9%;width:716px;height:640px')
css=css.replace('.fwin{position:relative;width:686px;height:604px','.fwin{position:relative;width:716px;height:640px')  # 36 design px taller than the scaffold, so the window's bottom edge and corners are always past the card
css=css.replace('.win-host{position:absolute;left:7.4%;top:9%;width:686px;height:604px','.win-host{position:absolute;left:7.4%;top:9%;width:686px;height:604px')
css+=('.ft-h{display:flex;justify-content:space-between;align-items:center;font-weight:600;font-size:10px;padding:0 10px;margin-bottom:6px}'
'.gr{position:relative;width:656px;height:266px;flex:none}.gh{position:absolute;top:0;font-size:8.6px;font-weight:500;color:#71717A}'
'.ed{position:absolute;left:0;top:0;width:656px;height:266px;overflow:visible;pointer-events:none}.ed path{fill:none;stroke-linecap:round}'
'.ed .b{stroke:#D4D4D8;stroke-width:1.4;transition:opacity .35s ease}.ed .b.dim{opacity:.3}.ed .o{stroke:#18181B;stroke-width:1.9;opacity:0}.ed .o.on{opacity:1}.ed .o.co{stroke:#B45309;stroke-dasharray:4 3}'
'.nd3{position:absolute;width:140px;height:62px;padding:7px 9px;border:1px solid #E4E4E7;border-radius:7px;background:#fff;font:inherit;color:#18181B;text-align:left;cursor:pointer;display:flex;flex-direction:column;gap:2px;overflow:hidden;margin:0;transition:opacity .35s ease,border-color .3s ease,background-color .3s ease,box-shadow .3s ease}'
'.nd3 b{font-family:"JetBrains Mono",ui-monospace,monospace;font-size:9.4px;font-weight:600;white-space:nowrap}.nd3 b.nm{font-family:inherit;font-size:9.9px}'
'.nd3 .t{color:#3F3F46;font-size:8.8px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}.nd3 .m{color:#71717A;font-size:8.2px;font-family:"JetBrains Mono",ui-monospace,monospace;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}'
'.nd3:hover{border-color:#A1A1AA}.nd3:focus-visible{outline:2px solid #18181B;outline-offset:2px}.nd3.dim{opacity:.34}.nd3.hit{border-color:#18181B}'
'.nd3.src{border-color:#F5C451;background:#FFFBEB;box-shadow:0 0 0 1px #F5C451}.nd3.co{border:1px dashed #B45309;background:#FFFBEB}.nd3.fakehover{border-color:#A1A1AA}.nd3.press{animation:fwpress .6s ease-out 1}'
'.rec{padding:8px 0 2px}.rg{display:grid;grid-template-columns:repeat(3,1fr)}.rc{padding:5px 10px 6px;border-top:1px solid #F0F0F1;min-width:0}.rc small{display:block;color:#71717A;font-size:8.2px;margin-bottom:2px}'
'.rc span{display:block;font-family:"JetBrains Mono",ui-monospace,monospace;font-size:9.2px;font-weight:500;color:#18181B;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}'
'.rowf{display:inline-flex;align-items:center;gap:6px}.lotf{display:inline-flex;align-items:center;gap:6px;width:218px;padding:4px 8px;border:1px solid #E4E4E7;border-radius:6px;background:#fff;color:#71717A;transition:border-color .2s}.lotf:focus-within{border-color:#18181B}.lotf svg{flex:none}'
'.lotf input{border:0;outline:0;background:transparent;width:100%;min-width:0;padding:0;margin:0;font-family:"JetBrains Mono",ui-monospace,monospace;font-size:9.4px;font-weight:500;color:#18181B}.lotf input::placeholder{color:#71717A;font-family:Inter,ui-sans-serif,system-ui,sans-serif;font-weight:400}'
'.emp{position:absolute;left:0;right:0;top:22px;bottom:0;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:4px;text-align:center;color:#71717A;border:1px dashed #E4E4E7;border-radius:9px;background:#FAFAFA}.emp svg{margin-bottom:4px}.emp b{font-size:11px;font-weight:600;color:#18181B}.emp span{font-size:9.4px;max-width:320px;line-height:1.35}.gr:not(.off) .emp{display:none}'
'.gr.off .nd3,.gr.off .gh,.gr.off .ed{opacity:0;visibility:hidden;pointer-events:none}.gh{transition:opacity .35s ease}'
'.re{grid-column:1/-1;display:flex;align-items:center;justify-content:center;height:66px;border-top:1px solid #F0F0F1;color:#71717A;font-size:9.4px}'
'.lgd{display:flex;align-items:center;gap:14px;color:#52525B;font-size:8.6px;margin-top:-2px;white-space:nowrap}.lgd span{display:inline-flex;align-items:center;gap:5px}.lgd i{width:12px;height:8px;border-radius:2px;border:1px solid #E4E4E7;background:#fff;flex:none}.lgd .s1{background:#FFFBEB;border-color:#F5C451}.lgd .s2{background:#FFFBEB;border:1px dashed #B45309}.lgd .s3{background:#F4F4F5;opacity:.6}'
'.hs{position:absolute;z-index:55;pointer-events:none;border:2px solid #FFB92B;border-radius:9px;opacity:0;transition:opacity .25s ease}.hs.on{opacity:1;animation:hsr 1.6s ease-out infinite}@keyframes hsr{0%{box-shadow:0 0 0 0 rgba(255,185,43,.6)}70%,100%{box-shadow:0 0 0 9px rgba(255,185,43,0)}}'
'.stp{position:absolute;right:44px;bottom:44px;z-index:56;display:flex;align-items:center;gap:6px}.stp button{width:24px;height:24px;padding:0;border:1px solid #E4E4E7;border-radius:7px;background:#fff;color:#18181B;cursor:pointer;display:grid;place-items:center;transition:background-color .2s}.stp button:hover:not(:disabled){background:#F4F4F5}.stp button:disabled{opacity:.35;cursor:default}.stp button:focus-visible{outline:2px solid #18181B;outline-offset:2px}.stp svg{width:12px;height:12px}.stp .sn{min-width:38px;text-align:center;color:#71717A;font-size:9px}'
'.cap{max-width:360px}.cap.turn{max-width:360px}.tr-act{min-height:48px}.cap{z-index:80}')

def studio():
    return ('<div class="studio" data-studio><button class="studio-chip" type="button" aria-expanded="false" aria-controls="pop1"><span class="wand" aria-hidden="true"><svg viewBox="0 0 20 20" aria-hidden="true"><path class="stick" d="M3 17L12 8" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/><path class="sp sp1" d="M15 1.5L16.2 3.8L18.5 5L16.2 6.2L15 8.5L13.8 6.2L11.5 5L13.8 3.8Z"/><path class="sp sp2" d="M17 10.2L17.6 11.4L18.8 12L17.6 12.6L17 13.8L16.4 12.6L15.2 12L16.4 11.4Z"/><path class="sp sp3" d="M7 1.4L7.6 2.4L8.6 3L7.6 3.6L7 4.6L6.4 3.6L5.4 3L6.4 2.4Z"/></svg></span><span>Studio</span><span class="more"><span class="more-inner"><span class="more-text">Learn more<svg viewBox="0 0 12 12" aria-hidden="true"><path d="M2 6h8M6.5 2.5L10 6 6.5 9.5" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg></span></span></span></button>'
    '<div class="pop" id="pop1" role="dialog" aria-label="About Studio apps"><h3>Start here, make it yours</h3><p class="lede">This is a typical lot trace view, built on your Sutton data with Studio. Want it different? Describe the change and Studio builds it.</p>'
    '<ul class="examples"><li style="--i:0">Add a recall hold button</li><li style="--i:1">Show test results on every lot</li><li style="--i:2">Group by customer region</li><li style="--i:3">Email affected customers</li></ul>'
    '<dl class="rows"><div><dt>Built on</dt><dd>Lots, batch records, shipments and test results</dd></div><div><dt>Change</dt><dd>Fields, wording and workflow</dd></div><div><dt>Get help</dt><dd>Depends on your plan</dd></div></dl>'
    '<a class="go" href="/studio">See what you can build in Studio<svg viewBox="0 0 12 12" aria-hidden="true"><path d="M2 6h8M6.5 2.5L10 6 6.5 9.5" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg></a></div></div>')

ARIA='Interactive demo: a lot trace for a dairy plant. Type a lot number to trace a milk lot forward to every batch and customer it reached, or enter a complaint lot and trace back to the milk, then click any lot, batch or customer to trace it'
body=('<div class="sx-stage"><div class="shot"><div class="shot-img"><div class="win-host" role="group" aria-label="'+ARIA+'"><div class="fwin">'
 '<div class="fw-head"><svg class="fw-icon" width="16" height="16" viewBox="0 0 16 16" fill="none"><circle cx="3.2" cy="8" r="1.8" stroke="#18181B" stroke-width="1.3"/><circle cx="12.8" cy="3.6" r="1.8" stroke="#18181B" stroke-width="1.3"/><circle cx="12.8" cy="12.4" r="1.8" stroke="#18181B" stroke-width="1.3"/><path d="M4.9 7.4L11.1 4.3M4.9 8.6L11.1 11.7" stroke="#18181B" stroke-width="1.3" stroke-linecap="round"/></svg>'
 '<div class="fw-title">Lot trace</div><span class="fw-chip chip-idle" id="scope">No trace yet</span></div>'
 '<div class="fw-tabs"><div class="fw-tab on">Genealogy</div><div class="fw-tab">Shipments</div><div class="fw-tab">Records</div></div><div class="fw-div"></div>'
 '<div class="fw-body"><div class="ctl"><div class="ct-l"><small>Lot number</small><span class="rowf"><span class="lotf"><svg width="11" height="11" viewBox="0 0 12 12" fill="none" aria-hidden="true"><circle cx="5.2" cy="5.2" r="3.6" stroke="#71717A" stroke-width="1.3"/><path d="M8 8l2.6 2.6" stroke="#71717A" stroke-width="1.3" stroke-linecap="round"/></svg><input id="lotin" type="text" placeholder="Scan or type a lot number" autocomplete="off" autocapitalize="characters" spellcheck="false" aria-label="Lot number"></span><button type="button" class="fw-act pri" id="go">Trace</button></span></div>'
 '<div class="ct-l"><small>Try a sample lot</small><span class="seg2" role="group" aria-label="Sample lots" id="segm"><button type="button" data-m="lot">ML-1028-A</button><button type="button" data-m="cmp">YG-1029-2</button></span></div></div>'
 '<div class="gr off" id="gr"><svg class="ed" id="ed" width="656" height="266" viewBox="0 0 656 266" aria-hidden="true"></svg><div class="emp" id="emp"><svg width="22" height="22" viewBox="0 0 22 22" fill="none" aria-hidden="true"><circle cx="9.5" cy="9.5" r="6.2" stroke="#A1A1AA" stroke-width="1.5"/><path d="M14.2 14.2L19 19" stroke="#A1A1AA" stroke-width="1.5" stroke-linecap="round"/></svg><b>Enter a lot number</b><span>A milk lot, a pasteurized base or a batch. Its full trail, forward to customers and back to the milk, shows here.</span></div></div>'
 '<div class="tr-act neutral" id="act" role="status" aria-live="polite" style="width:656px"><span id="act-icon"></span><div><p id="act-text"></p></div></div>'
 '<div class="fw-card rec"><div class="ft-h"><span id="rtitle">Lot record</span><span class="fw-chip chip-idle" id="rchip"></span></div><div class="rg" id="rg"></div></div>'
 '<div class="lgd" aria-hidden="true"><span><i class="s1"></i>Starting lot</span><span><i class="s2"></i>Blended in the same silo</span><span><i class="s3"></i>Not affected</span></div>'
 '</div>'
 '</div>'
 '<span class="hs" id="hs" aria-hidden="true"></span>'
 '<div class="stp" role="group" aria-label="Walkthrough steps"><button type="button" id="pv" aria-label="Previous step" disabled><svg viewBox="0 0 12 12" aria-hidden="true"><path d="M7.5 2.5L4 6l3.5 3.5" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg></button><span class="sn" id="sn">1 of 6</span><button type="button" id="nx" aria-label="Next step"><svg viewBox="0 0 12 12" aria-hidden="true"><path d="M4.5 2.5L8 6 4.5 9.5" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg></button></div>'
 '</div></div></div>'+studio()+'</div></div>')

# scaffold JS from the Brewery card
js=src
a=js.index('function boot(root){')
b=js.index("var tree=$('tree'),INTRO=tree")
scaffold=js[a:b]
assert scaffold.count('setTimeout(tour,2200)')==1
scaffold=scaffold.replace('setTimeout(tour,2200)','setTimeout(tour,900)')
tail=js[js.index("host.removeEventListener('pointerdown',engage,true)"):]

custom=r'''var gr=$('gr'),ed=$('ed'),act=$('act'),lotin=$('lotin'),INTRO=gr,CAPBOX=gr,PROMPT='Type a lot number, or click a sample lot';
var XS=[0,172,344,516],NW=140,NH=62,SVGNS='http://www.w3.org/2000/svg';
var ND=[
{k:'A',c:0,y:22,v:9840,t:'ML-1028-A',a:'9,840 lb, Route 7 tanker',m:'Fat 3.9, protein 3.2',rt:'Milk intake lot',r:[['Volume','9,840 lb'],['Received','Oct 28, 5:40 am'],['Source','Route 7 tanker'],['Fat, protein','3.9%, 3.2%'],['pH','6.7'],['Documents','2 attached']]},
{k:'B',c:0,y:96,v:8120,t:'ML-1028-B',a:'8,120 lb, Route 3 tanker',m:'Fat 4.0, protein 3.3',rt:'Milk intake lot',r:[['Volume','8,120 lb'],['Received','Oct 28, 7:05 am'],['Source','Route 3 tanker'],['Fat, protein','4.0%, 3.3%'],['pH','6.7'],['Documents','2 attached']]},
{k:'C',c:0,y:200,v:6500,t:'ML-1028-C',a:'6,500 lb, Route 9 tanker',m:'Fat 3.8, protein 3.1',rt:'Milk intake lot',r:[['Volume','6,500 lb'],['Received','Oct 28, 9:30 am'],['Source','Route 9 tanker'],['Fat, protein','3.8%, 3.1%'],['pH','6.7'],['Documents','2 attached']]},
{k:'PB1',c:1,y:59,s:'S1',t:'PB-1028-1',a:'Pasteurized base',m:'Silo S1, 17,960 lb',rt:'Pasteurized base lot'},
{k:'PB2',c:1,y:200,s:'S2',t:'PB-1028-2',a:'Pasteurized base',m:'Silo S2, 6,500 lb',rt:'Pasteurized base lot'},
{k:'YG1',c:2,y:22,t:'YG-1029-1',a:'Plain yogurt',m:'Culture CU-0914',ing:['culture CU-0914'],rt:'Batch'},
{k:'YG2',c:2,y:96,t:'YG-1029-2',a:'Vanilla yogurt',m:'CU-0914, VN-2207',ing:['culture CU-0914','vanilla VN-2207'],rt:'Batch'},
{k:'MK',c:2,y:200,t:'MK-1029-1',a:'Whole milk, half gallon',m:'No added ingredients',ing:[],rt:'Batch'},
{k:'DC',c:3,y:22,nm:1,t:'Regional grocery DC',m:'YG-1029-1, YG-1029-2',rt:'Customer',last:'Oct 31'},
{k:'NF',c:3,y:111,nm:1,t:'Natural foods co-op',m:'YG-1029-1, MK-1029-1',rt:'Customer',last:'Oct 31'},
{k:'SC',c:3,y:200,nm:1,t:'School district',m:'YG-1029-2, MK-1029-1',rt:'Customer',last:'Nov 1'}];
var ED=[['A','PB1'],['B','PB1'],['C','PB2'],['PB1','YG1',0,10000],['PB1','YG2',0,7960],['PB2','MK',0,6500],['YG1','DC',12],['YG1','NF',6],['YG2','DC',4],['YG2','SC',3],['MK','SC',5],['MK','NF',2]];
var by={},par={},kid={},nodeEl={},edEl=[];
ND.forEach(function(n){by[n.k]=n;par[n.k]=[];kid[n.k]=[];});
ED.forEach(function(e){kid[e[0]].push(e[1]);par[e[1]].push(e[0]);});
function palIn(k){var s=0;ED.forEach(function(e){if(e[1]===k&&e[2])s+=e[2];});return s;}
function palOut(k){var s=0;ED.forEach(function(e){if(e[0]===k&&e[2])s+=e[2];});return s;}
ND.filter(function(n){return n.c===3;}).forEach(function(n){n.pal=palIn(n.k);n.a=n.pal+' pallets';var bs=par[n.k].map(function(x){return by[x].t;});n.r=[['Pallets',String(n.pal)],['Batches',String(bs.length)],['Last shipment',n.last],['Lots received',bs.join(', ')]];});
ND.filter(function(n){return n.c===2;}).forEach(function(n){var b=by[par[n.k][0]];var mk={YG1:'Plain yogurt',YG2:'Vanilla yogurt',MK:'Whole milk'}[n.k];n.r=[['Product',mk],['Made','Oct 29'],['Base lot',b.t],[n.k==='MK'?'Package':'Cultures',n.k==='MK'?'Half gallon':n.m],['Best before',n.k==='MK'?'Nov 16':'Nov 26'],['Shipped',palOut(n.k)+' pallets']];});
ND.filter(function(n){return n.c===1;}).forEach(function(n){var ps=par[n.k],vol=0;ps.forEach(function(x){vol+=by[x].v;});n.vol=vol;n.r=[['Volume',vol.toLocaleString('en-US')+' lb'],['Held in','Silo '+n.s],['Made from',ps.map(function(x){return by[x].t;}).join(', ')],['Pasteurized','Oct 28'],['Quality','Released'],['Fed',pl(kid[n.k].length,'batch','batches')]];});
function walk(k,m,s){(m[k]||[]).forEach(function(x){if(!s[x]){s[x]=1;walk(x,m,s);}});}
function scopeOf(k,dir){var s={};s[k]=1;if(dir!=='back')walk(k,kid,s);if(dir!=='fwd')walk(k,par,s);return s;}
function coOf(k,dir,sc){var co={};if(dir!=='back'&&by[k].c===0){ND.forEach(function(n){if(n.c===1&&sc[n.k])par[n.k].forEach(function(p){if(!sc[p])co[p]=1;});});}return co;}
function colIn(sc,c){return ND.filter(function(n){return n.c===c&&sc[n.k];}).map(function(n){return n.k;});}
function names(l){return l.map(function(x){return by[x].t;});}
function jn(a){return a.length<2?a.join(''):a.slice(0,-1).join(', ')+' and '+a[a.length-1];}
function palScope(sc){var s=0;ED.forEach(function(e){if(e[2]&&sc[e[0]]&&sc[e[1]])s+=e[2];});return s;}
var S={sel:'A',dir:null,cmp:false,open:false};
var cols=[['Milk intake',0],['Pasteurized base',1],['Batch',2],['Customer',3]];
cols.forEach(function(c){var h=document.createElement('div');h.className='gh';h.style.left=XS[c[1]]+'px';h.textContent=c[0];gr.appendChild(h);});
ND.forEach(function(n){var b=document.createElement('button');b.type='button';b.className='nd3';b.dataset.k=n.k;b.style.left=XS[n.c]+'px';b.style.top=n.y+'px';b.style.transitionDelay=(n.c*90)+'ms,0ms,0ms,0ms';b.innerHTML='<b'+(n.nm?' class="nm"':'')+'>'+n.t+'</b>'+(n.a?'<span class="t">'+n.a+'</span>':'')+'<span class="m">'+n.m+'</span>';gr.appendChild(b);nodeEl[n.k]=b;});
ED.forEach(function(e){var A=by[e[0]],B=by[e[1]],x1=XS[A.c]+NW,y1=A.y+NH/2,x2=XS[B.c],y2=B.y+NH/2,cx=(x2-x1)/2,d='M'+x1+' '+y1+' C'+(x1+cx)+' '+y1+' '+(x2-cx)+' '+y2+' '+x2+' '+y2;
var p=document.createElementNS(SVGNS,'path');p.setAttribute('d',d);p.setAttribute('class','b');var o=document.createElementNS(SVGNS,'path');o.setAttribute('d',d);o.setAttribute('class','o');ed.appendChild(p);ed.appendChild(o);var L=60;try{L=o.getTotalLength()||60;}catch(x){}o._len=L;edEl.push({b:p,o:o});});
function showRec(k){var n=by[k],c=$('rchip');$('rtitle').textContent=n.rt;c.textContent=n.nm?'Customer':n.t;c.style.display='';$('rg').innerHTML=n.r.map(function(r){return '<div class="rc"><small>'+r[0]+'</small><span>'+r[1]+'</span></div>';}).join('');}
function recEmpty(){$('rtitle').textContent='Lot record';var c=$('rchip');c.textContent='';c.style.display='none';$('rg').innerHTML='<div class="re">Lot details appear here once a lot is entered.</div>';}
function drawEdge(o,isCo){o.style.transition='none';o.style.strokeDasharray='';o.style.strokeDashoffset='';if(isCo||reduce){o.classList.add('on');if(isCo)o.classList.add('co');return;}var L=o._len;o.style.strokeDasharray=L+' '+L;o.style.strokeDashoffset=L;o.classList.add('on');void o.getBoundingClientRect();o.style.transition='stroke-dashoffset .7s cubic-bezier(.22,.9,.28,1)';o.style.strokeDashoffset=0;}
function clearTrace(){ND.forEach(function(n){var e=nodeEl[n.k];e.classList.remove('dim','hit','src','co');if(n.c===3){e.querySelector('.t').textContent=n.pal+' pallets';}});edEl.forEach(function(x){x.b.classList.remove('dim');x.o.classList.remove('on','co');x.o.style.transition='none';x.o.style.strokeDasharray='';x.o.style.strokeDashoffset='';});}
function trace(k,dir,cmp){var was=S.open;S.open=true;gr.classList.remove('off');S.sel=k;S.dir=dir;S.cmp=!!cmp;clearTrace();var sc=scopeOf(k,dir),co=coOf(k,dir,sc),pal=palScope(sc);
ND.forEach(function(n){var e=nodeEl[n.k];if(co[n.k])e.classList.add('co');else if(sc[n.k]){e.classList.add('hit');if(n.k===k)e.classList.add('src');}else e.classList.add('dim');
if(n.c===3&&sc[n.k]&&dir!=='back'){var q=0;ED.forEach(function(x){if(x[1]===n.k&&x[2]&&sc[x[0]])q+=x[2];});e.querySelector('.t').textContent=q+' pallets in scope';}});
var draw=function(){edEl.forEach(function(x,i){var e=ED[i],on=(sc[e[0]]||co[e[0]])&&(sc[e[1]]||co[e[1]]);if(on)drawEdge(x.o,!!co[e[0]]);});};
edEl.forEach(function(x,i){var e=ED[i],on=(sc[e[0]]||co[e[0]])&&(sc[e[1]]||co[e[1]]);if(!on)x.b.classList.add('dim');});
if(was||reduce)draw();else later(draw,380);
var lots=colIn(sc,0),bat=colIn(sc,2),cus=colIn(sc,3),bases=colIn(sc,1),n=by[k],chip,html,sil=bases.map(function(x){return by[x].s;}),silTxt=(sil.length>1?'silos ':'silo ')+jn(sil);
if(dir==='fwd'){var out=ND.filter(function(x){return x.c!==1&&x.c!==3&&!sc[x.k]&&!co[x.k];}).map(function(x){return x.t;});chip=pal+' pallets, '+pl(cus.length,'customer','customers');
html='<b>'+n.t+' reached '+pl(bat.length,'batch','batches')+' and '+pl(cus.length,'customer','customers')+', '+pal+' pallets in all.</b> '+(Object.keys(co).length?'It was blended with '+jn(names(Object.keys(co)))+' in '+silTxt+', so '+(Object.keys(co).length>1?'those lots are':'that lot is')+' in scope too. ':'')+(out.length?'Not affected: '+jn(out)+'.':'');}
else if(dir==='back'){chip=pl(lots.length,'milk lot','milk lots')+', '+pl(bat.length,'batch','batches');
if(n.c===2){var ig=n.ing.length?', plus '+jn(n.ing):'';html='<b>'+(cmp?'Complaint on '+n.a.toLowerCase()+' '+n.t+'.':n.t+' traces back to '+pl(lots.length,'milk lot','milk lots')+'.')+'</b> '+(cmp?'It traces back to '+pl(lots.length,'milk lot','milk lots')+': ':'')+jn(names(lots))+', blended in '+silTxt+ig+'.';}
else{html='<b>'+n.t+' received '+pl(bat.length,'batch','batches')+', made from '+pl(lots.length,'milk lot','milk lots')+'.</b> '+jn(names(bat))+', from '+silTxt+'.';}}
else{chip=pl(lots.length,'milk lot','milk lots')+', '+pl(cus.length,'customer','customers');var pp=palScope(sc);html='<b>'+n.t+' came from '+pl(lots.length,'milk lot','milk lots')+' and reached '+pl(cus.length,'customer','customers')+'.</b> '+pp+' pallets shipped.';}
var sp=$('scope');sp.textContent=chip;sp.className='fw-chip chip-warn';
act.className='tr-act ok';$('act-icon').innerHTML=checkSvg;setText($('act-text'),html);
showRec(k);[].slice.call($('segm').children).forEach(function(b){b.classList.toggle('on',(b.dataset.m==='lot'&&k==='A'&&dir==='fwd'&&!cmp)||(b.dataset.m==='cmp'&&k==='YG2'&&cmp));});}
function lookup(v){v=String(v||'').trim().toUpperCase();var k=null;ND.forEach(function(n){if(n.c<3&&n.t.toUpperCase()===v)k=n.k;});return k;}
function showErr(){act.className='tr-act';$('act-icon').innerHTML=warn;setText($('act-text'),'<b>No lot matches that number.</b> Try ML-1028-A or YG-1029-2.');}
function enterLot(raw,mode){var k=lookup(raw);if(!k){showErr();return false;}lotin.value=by[k].t;if(mode==='cmp')trace(k,'back',true);else{var c=by[k].c;trace(k,c===0?'fwd':'both',false);}return true;}
var pv=$('pv'),nx=$('nx'),sn=$('sn'),hs=$('hs'),cur=1,NS=5;
function btn(m){return $('segm').querySelector('[data-m="'+m+'"]');}
function showHot(el){if(!el){hs.classList.remove('on');return;}var r=rel(el);hs.style.left=(r.l-3)+'px';hs.style.top=(r.t-3)+'px';hs.style.width=(r.w+6)+'px';hs.style.height=(r.h+6)+'px';hs.classList.add('on');}
function marker(i){cur=i;sn.textContent=i+' of '+NS;pv.disabled=i<=1;nx.disabled=i>=NS;}
function applyState(st){if(st==='fwd'){if(!(S.open&&S.dir==='fwd'&&S.sel==='A'&&!S.cmp))enterLot('ML-1028-A');}else if(st==='cmp'){if(!S.cmp)enterLot('YG-1029-2','cmp');}}
var ST=[
{m:'Start with a lot number',s:'Type ML-1028-A and its whole trail opens.',st:'fwd',tg:function(){return lotin;},dx:60,dy:8,hot:function(){return nx;}},
{m:'Blended lots come along',s:'ML-1028-B shared silo S1, so it is in scope too.',st:'fwd',tg:function(){return nodeEl.B;},dx:70,dy:20,hot:function(){return nx;}},
{m:'Only what is affected',s:'Lot C and the whole milk are clear.',st:'fwd',tg:function(){return nodeEl.MK;},dx:70,dy:20,hot:function(){return btn('cmp');}},
{m:'Now start from a complaint',s:'Enter the vanilla yogurt lot that came back.',st:'cmp',tg:function(){return lotin;},dx:60,dy:8,hot:function(){return nx;}},
{m:'Walk back to the source',s:'Milk lots, cultures and vanilla in one view.',st:'cmp',tg:function(){return nodeEl.PB1;},dx:70,dy:20,hot:null}];
function showStep(i,auto){var s=ST[i-1];marker(i);say(i,s.m,s.s);moveGhost(winPos(s.tg(),s.dx,s.dy));if(!auto){ghost.classList.add('on');showHot(s.hot?s.hot():null);}}
function goStep(i){if(i<1||i>NS)return;if(!engaged){engaged=true;cancelAll();}turnOff();applyState(ST[i-1].st);showStep(i,false);}
pv.addEventListener('click',function(e){e.stopPropagation();goStep(cur-1);});
nx.addEventListener('click',function(e){e.stopPropagation();goStep(cur+1);});
function pick(k){var c=by[k].c;lotin.value=c<3?by[k].t:'';trace(k,c===0?'fwd':c===3?'back':'both',false);if(engaged){turnOff();hush();showHot(null);later(function(){turnSay('Try another lot, or press Replay',act);},1100);later(turnOff,6500);}}
gr.addEventListener('click',function(e){var b=e.target.closest&&e.target.closest('.nd3');if(!b)return;e.stopPropagation();pick(b.dataset.k);});
function submit(){if(enterLot(lotin.value)&&engaged){turnOff();hush();showHot(null);}}
$('go').addEventListener('click',function(e){e.stopPropagation();submit();});
lotin.addEventListener('keydown',function(e){e.stopPropagation();if(e.key==='Enter'){e.preventDefault();submit();}});
$('segm').addEventListener('click',function(e){var b=e.target.closest&&e.target.closest('button');if(!b)return;e.stopPropagation();var m=b.dataset.m;
if(engaged&&m==='lot'&&!S.open)goStep(1);else if(engaged&&m==='cmp'&&cur<=3)goStep(4);
else{if(m==='lot')enterLot('ML-1028-A');else enterLot('YG-1029-2','cmp');if(engaged){turnOff();hush();showHot(null);}}});
function resetState(){S={sel:'A',dir:null,cmp:false,open:false};clearTrace();gr.classList.add('off');lotin.value='';var sp=$('scope');sp.textContent='No trace yet';sp.className='fw-chip chip-idle';act.className='tr-act neutral';$('act-icon').innerHTML=infoSvg;setText($('act-text'),'<b>Enter a lot number.</b> A milk lot, a pasteurized base or a batch, and its full trail lights up.');recEmpty();[].slice.call($('segm').children).forEach(function(b){b.classList.remove('on');});hideTip();marker(1);showHot(engaged&&!reduce?btn('lot'):null);}
function onCancel(){[].slice.call(root.querySelectorAll('.fakehover,.press')).forEach(function(b){b.classList.remove('fakehover','press');});}
function typeLot(text,t0,done){later(function(){lotin.value='';},t0);for(var i=0;i<text.length;i++){(function(i){later(function(){lotin.value=text.slice(0,i+1);},t0+60+i*85);})(i);}later(done,t0+60+text.length*85+220);}
function script(){var t=300;
later(function(){showStep(1,true);},t);typeLot('ML-1028-A',t+300,function(){enterLot('ML-1028-A');});t+=3000;
later(function(){showStep(2,true);},t);t+=3800;
later(function(){showStep(3,true);},t);t+=3400;
later(function(){showStep(4,true);},t);typeLot('YG-1029-2',t+400,function(){enterLot('YG-1029-2','cmp');});t+=4600;
later(function(){showStep(5,true);},t);t+=3800;
later(function(){hush();ghost.classList.remove('on');},t);t+=700;
later(function(){resetState();showHot(btn('lot'));turnSay('Your turn. Type a lot number or click a sample',gr);},t);t+=6000;
later(function(){turnOff();showHot(null);},t);
return t+200;}
'''
out=[]
out.append('/* Dairy, card 1: Milk Lot Traceability (lot genealogy from milk intake to customer: trace forward from a milk lot, trace back from a complaint, blended silo lots, lot records)\n   Loaded by the site loader. Mounts into the card visual passed in by the loader.\n   Source of truth for this graphic: edit here, open a pull request, then release a new tag. */')
out.append('(function(){')
out.append("var SRC=document.currentScript&&document.currentScript.src;var BGU=SRC?new URL('bg-1.jpg',SRC).href:'';")
out.append('var CSS='+json.dumps(css)+".replace('__BG__',BGU);")
out.append('var BODY='+json.dumps(body)+';')
pre=src[src.index("var c=document.currentScript&&document.currentScript.sxCard;"):src.index('function boot(root){')]
pre=pre.replace("{aspect-ratio:604/523}}'","{aspect-ratio:604/523}}.capabilities_card-visual[data-sx-industry*=\\\"dairy\\\"]{border-bottom-right-radius:0}'")
pre=pre.replace("'brewery'","'dairy'").replace('sx-brewery-card-css','sx-dairy-card-css').replace('data-sx-industry*=\\"brewery\\"','data-sx-industry*=\\"dairy\\"').replace('data-sx-industry*="brewery"','data-sx-industry*="dairy"')
assert 'brewery' not in pre, [m.start() for m in re.finditer('brewery',pre)]
out.append(pre.rstrip('\n'))
out.append(scaffold.rstrip('\n'))
out.append(custom.rstrip('\n'))
out.append(tail.rstrip('\n'))
res='\n'.join(out)+'\n'
import os
os.makedirs(os.path.join(OUT,'graphics/dairy'),exist_ok=True)
open(os.path.join(OUT,'graphics/dairy/card-1.js'),'w').write(res)
print(len(res.encode()),'bytes')
