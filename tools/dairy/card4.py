"""Dairy card 4: Planning & Replenishment. Layout type: a week schedule board (runs as blocks on three lines), a materials table and a purchase order."""
CSS = ('.gt{width:656px;padding:8px 0 6px}.gt .ft-h{margin-bottom:6px}.gh{position:relative;height:16px;margin-left:90px;width:551px}.gh span{position:absolute;top:1px;font-size:8.4px;color:#71717A;white-space:nowrap}.gh span.nw{color:#B91C1C;font-weight:600}'
 '.gb{position:relative}.gb .zone{position:absolute;top:0;bottom:0;left:0;width:0;background:repeating-linear-gradient(135deg,#FEF2F2 0 6px,#FFF 6px 12px);border-left:1.5px dashed #FCA5A5;pointer-events:none}.gb .dl{position:absolute;top:0;bottom:0;width:1px;background:#EDEDEF;pointer-events:none}'
 '.g4{position:relative;height:46px;border-top:1px solid #F0F0F1}.g4 .rl{position:absolute;left:10px;top:0;bottom:0;display:flex;align-items:center;width:78px;font-weight:500;font-size:9.4px}'
 '.bk{position:absolute;top:8px;height:30px;border:1px solid #D4D4D8;background:#F4F4F5;border-radius:6px;padding:0 7px;display:flex;flex-direction:column;justify-content:center;font-size:8.8px;white-space:nowrap;overflow:hidden;transition:left .6s cubic-bezier(.22,.9,.28,1),width .6s cubic-bezier(.22,.9,.28,1),opacity .3s,background-color .3s,border-color .3s;z-index:1}'
 '.bk b{font-weight:600;font-size:9px}.bk span{color:#71717A;font-size:8.2px}.bk.mv{border-color:#18181B}.bk.rs{background:#FFB92B;border-color:#D99A00}.bk.rs span{color:#5B4300}.bk.rs.hide{opacity:0;width:0!important;padding:0;border-width:0}.bk.lt{background:#FEE2E2;border-color:#FCA5A5}.bk.lt span{color:#991B1B}.bk.fakehover{border-color:#18181B}'
 '.mt{width:656px;padding:8px 0 4px}.mt .th2,.mt .tr3{display:flex;align-items:center;padding:0 10px}.mt .th2{height:20px;color:#71717A;font-size:8.6px;font-weight:500}.mt .tr3{height:32px;border-top:1px solid #F0F0F1}'
 '.mt .c1{flex:1.3;font-weight:500}.mt .c2,.mt .c3,.mt .c4,.mt .c5{flex:1;text-align:right;font-family:"JetBrains Mono",ui-monospace,monospace;font-size:9.2px}.mt .c6{flex:1.5;text-align:right}.mt .th2 .c2,.mt .th2 .c3,.mt .th2 .c4,.mt .th2 .c5{font-family:inherit;font-size:8.6px}'
 '.mt .tick{animation:tick .5s ease}@keyframes tick{40%{transform:scale(1.1)}}'
 '.poc{width:656px;padding:8px 0 4px;min-height:96px}.pol{margin:0 10px 6px;padding:12px 10px;border:1px dashed #E4E4E7;border-radius:7px;background:#FAFAFA;color:#71717A;font-size:9.4px;text-align:center}'
 '.pr{display:flex;align-items:center;gap:10px;padding:6px 10px;border-top:1px solid #F0F0F1;font-size:9.4px}.pr span{flex:1;font-weight:500}.pr b{font-family:"JetBrains Mono",ui-monospace,monospace;font-weight:500;font-size:9.4px}.pr em{font-style:normal;color:#71717A;width:150px;text-align:right}'
 '.lgd .nm{background:#F4F4F5;border-color:#D4D4D8}.lgd .rs{background:#FFB92B;border-color:#D99A00}.lgd .mv{background:#F4F4F5;border-color:#18181B}.lgd .lt{background:#FEE2E2;border-color:#FCA5A5}'
 '.fw-act:disabled{opacity:.4;cursor:default}.fw-act.pri:disabled:hover{background:#27272A}')
WIN = ('<div class="fw-head"><svg class="fw-icon" width="16" height="16" viewBox="0 0 16 16" fill="none"><rect x="2" y="3" width="12" height="3" rx="1" stroke="#18181B" stroke-width="1.3"/><rect x="2" y="8" width="7" height="3" rx="1" stroke="#18181B" stroke-width="1.3"/><rect x="5" y="12.5" width="9" height="1.5" rx=".75" fill="#18181B"/></svg><div class="fw-title">Production schedule</div><span class="fw-chip chip-ok" id="pchip">On track</span></div>'
 '<div class="fw-tabs"><div class="fw-tab on">Schedule</div><div class="fw-tab">Materials</div><div class="fw-tab">Orders</div></div><div class="fw-div"></div>'
 '<div class="fw-body" id="fwb"><div class="ctl"><div class="ct-l"><small>Rush order, vanilla yogurt</small><span class="seg2" id="rush" role="group" aria-label="Rush order size"><button type="button" data-i="0">200 cases</button><button type="button" data-i="1">400 cases</button><button type="button" data-i="2">600 cases</button></span></div>'
 '<div class="ct-l" style="text-align:right"><small>Shortages</small><button type="button" class="fw-act pri" id="po" disabled>Create purchase order</button></div></div>'
 '<div class="fw-card gt" id="gt"><div class="ft-h"><span>This week, a 40 hour week on each line</span><span class="fw-chip chip-idle" id="gtc"></span></div><div class="gh" id="gh"></div><div class="gb" id="gb"></div></div>'
 '<div class="fw-card mt" id="mt"><div class="th2"><span class="c1">Material</span><span class="c2">On hand</span><span class="c3">Committed</span><span class="c4">Available</span><span class="c5">Rush needs</span><span class="c6">Status</span></div>'
 '<div class="tr3"><span class="c1">Milk</span><span class="c2" id="m1"></span><span class="c3" id="m2"></span><span class="c4" id="m3"></span><span class="c5" id="m4"></span><span class="c6"><span class="fw-chip chip-ok" id="m5"></span></span></div>'
 '<div class="tr3"><span class="c1">Vanilla base</span><span class="c2" id="v1"></span><span class="c3" id="v2"></span><span class="c4" id="v3"></span><span class="c5" id="v4"></span><span class="c6"><span class="fw-chip chip-ok" id="v5"></span></span></div></div>'
 '<div class="fw-card poc" id="poc"><div class="ft-h"><span>Purchase order</span><span class="fw-chip chip-idle" id="poch">None yet</span></div><div id="pob"></div></div>'
 '<div class="tr-act neutral" id="act" role="status" aria-live="polite" style="width:656px"><span id="act-icon"></span><div><p id="act-text"></p></div></div>'
 '<div class="lgd" aria-hidden="true"><span><i class="nm"></i>Scheduled run</span><span><i class="rs"></i>Rush order</span><span><i class="mv"></i>Moved</span><span><i class="lt"></i>Past Friday</span></div></div>')
JS = r'''var fwb=$('fwb'),act=$('act'),INTRO=fwb,CAPBOX=fwb,PROMPT='Pick a rush order size';
var PXH=10.6,LBL=90,WK=40,TOT=52,RATE=50,RUSH=[200,400,600];
var LINES=[['Yogurt line',[['P','Plain',12],['V','Vanilla',10],['R','Rush vanilla',0],['S','Strawberry',8],['G','Greek',8]]],['Cheese vats',[['C1','Cheddar',18],['C2','Mozzarella',16]]],['Butter churn',[['B1','Butter',14],['B2','Cultured butter',10]]]];
var MAT={milk:{on:52000,cm:41500,per:34},van:{on:120,cm:70,per:0.35}};
var S={ri:null,po:false},bkEl={},base={};
function fl(n){return Math.round(n).toLocaleString('en-US');}
function jn(a){return a.length<2?a.join(''):a.slice(0,-1).join(', ')+' and '+a[a.length-1];}
var gh=$('gh'),gb=$('gb');
['Mon','Tue','Wed','Thu','Fri'].forEach(function(d,i){var s=document.createElement('span');s.style.left=(i*8*PXH+4)+'px';s.textContent=d;gh.appendChild(s);});
var nw=document.createElement('span');nw.className='nw';nw.style.left=(WK*PXH+4)+'px';nw.textContent='Past Friday';gh.appendChild(nw);
var zone=document.createElement('div');zone.className='zone';zone.style.left=(LBL+WK*PXH)+'px';zone.style.width=((TOT-WK)*PXH)+'px';gb.appendChild(zone);
for(var k=1;k<5;k++){var dl=document.createElement('div');dl.className='dl';dl.style.left=(LBL+k*8*PXH)+'px';gb.appendChild(dl);}
LINES.forEach(function(L){var row=document.createElement('div');row.className='g4';var lab=document.createElement('span');lab.className='rl';lab.textContent=L[0];row.appendChild(lab);L[1].forEach(function(b){var e=document.createElement('div');e.className='bk'+(b[0]==='R'?' rs hide':'');e.innerHTML='<b>'+b[1]+'</b><span></span>';row.appendChild(e);bkEl[b[0]]=e;});gb.appendChild(row);});
function sched(N){var pos={},t=0;LINES.forEach(function(L){var t=0;L[1].forEach(function(b){var d=b[0]==='R'?N/RATE:b[2];if(b[0]==='R'&&!N)d=0;pos[b[0]]={s:t,e:t+d,d:d};t+=d;});});return pos;}
var B0=sched(0);
function mat(N){var o={};['milk','van'].forEach(function(k){var m=MAT[k],av=m.on-m.cm,need=N*m.per;o[k]={on:m.on,cm:m.cm,av:av,need:need,sh:Math.max(0,need-av)};});return o;}
function render(){var N=S.ri===null?0:RUSH[S.ri],P=sched(N),M=mat(N);
[].slice.call($('rush').children).forEach(function(b,i){b.classList.toggle('on',i===S.ri);});
Object.keys(P).forEach(function(k){var e=bkEl[k],p=P[k];if(k==='R'){e.classList.toggle('hide',!N);}var late=p.e>WK&&p.d>0;e.style.left=(LBL+p.s*PXH)+'px';e.style.width=(p.d*PXH-2)+'px';e.querySelector('span').textContent=p.d+' h';e.classList.toggle('lt',late);e.classList.toggle('mv',!!N&&k!=='R'&&B0[k]&&Math.abs(p.s-B0[k].s)>0.01);});
var gEnd=P.G.e,lateG=Math.max(0,gEnd-WK);
$('gtc').textContent='Yogurt line done at hour '+gEnd+' of '+WK;$('gtc').className='fw-chip '+(lateG?'chip-warn':'chip-idle');
var pc=$('pchip');if(N){pc.textContent='Greek '+lateG+' h past Friday';pc.className='fw-chip chip-warn';}else{pc.textContent='On track';pc.className='fw-chip chip-ok';}
function setM(pre,m,lbl){function tx(i,t){var e=$(pre+i);if(e.textContent!==t){e.textContent=t;e.classList.remove('tick');void e.offsetWidth;e.classList.add('tick');}}
tx('1',fl(m.on)+' lb');tx('2',fl(m.cm)+' lb');tx('3',fl(m.av)+' lb');tx('4',N?fl(m.need)+' lb':'');var st=$(pre+'5');
if(!N){st.textContent='OK';st.className='fw-chip chip-ok';}else if(m.sh>0&&S.po){st.textContent='On order PO-2231';st.className='fw-chip chip-ok';}else if(m.sh>0){st.textContent='Short '+fl(m.sh)+' lb';st.className='fw-chip chip-risk';}else{st.textContent='Covered';st.className='fw-chip chip-ok';}}
setM('m',M.milk);setM('v',M.van);
var lines=[];if(M.milk.sh>0)lines.push(['Milk',M.milk.sh]);if(M.van.sh>0)lines.push(['Vanilla base',M.van.sh]);
var po=$('po');po.disabled=!(N&&lines.length&&!S.po);po.textContent=S.po?'Created':'Create purchase order';po.classList.toggle('done',S.po);
$('poch').textContent=S.po?'PO-2231, draft':'None yet';$('poch').className='fw-chip '+(S.po?'chip-ok':'chip-idle');
$('pob').innerHTML=S.po?lines.map(function(l){return '<div class="pr"><span>'+l[0]+'</span><b>'+fl(l[1])+' lb</b><em>Short for the '+N+' case rush</em></div>';}).join(''):'<div class="pol">Shortages from a rush order become one purchase order here.</div>';
var html,cl='tr-act ok',ic=checkSvg;
if(!N){cl='tr-act neutral';ic=infoSvg;html='<b>This week is on track.</b> The four yogurt runs finish at hour '+B0.G.e+' of '+WK+', and milk and vanilla base are in stock. Pick a rush order size to see what moves.';}
else if(S.po){html='<b>PO-2231 is raised for '+jn(lines.map(function(l){return fl(l[1])+' lb of '+l[0].toLowerCase();}))+'.</b> The shortages are on order, and the schedule does not change.';}
else{var lateN=['S','G'].filter(function(k){return P[k].e>WK;}).map(function(k){return k==='S'?'Strawberry':'Greek';});cl='tr-act';ic=warn;
html='<b>A rush of '+N+' cases adds '+P.R.d+' hours on the yogurt line.</b> Strawberry and Greek move back, and '+(lateN.length>1?'both finish':'Greek finishes')+' past Friday, Greek by '+lateG+' hours. '+(lines.length?jn(lines.map(function(l){return l[0]+' is '+fl(l[1])+' lb short';}))+'.':'Stock covers it.');}
act.className=cl;$('act-icon').innerHTML=ic;setText($('act-text'),html);}
function setState(ri,po){if(S.ri===ri&&S.po===po)return;S.ri=ri;S.po=po;render();}
function rushBtn(i){return $('rush').children[i];}
function resetState(){S={ri:null,po:false};render();hideTip();marker(1);showHot(engaged&&!reduce?rushBtn(1):null);}
function applyState(i){if(i<=1)setState(null,false);else if(i<=4)setState(1,false);else setState(1,true);}
var ST=[
{m:'Plan around real stock',s:'Yogurt, cheese and butter runs, with milk and vanilla base beside them.',tg:function(){return $('gt');},dx:200,dy:70,hot:function(){return rushBtn(1);}},
{m:'Add a rush order',s:'400 cases of vanilla yogurt for the school district.',tg:function(){return rushBtn(1);},dx:40,dy:10,hot:function(){return nx;}},
{m:'The schedule moves',s:'Strawberry and Greek move back, and Greek finishes 6 hours past Friday.',tg:function(){return bkEl.G;},dx:40,dy:12,hot:function(){return nx;}},
{m:'Shortages show up',s:'Milk is 3,100 lb short and vanilla base is 90 lb short.',tg:function(){return $('mt');},dx:480,dy:44,hot:function(){return $('po');}},
{m:'Raise the purchase order',s:'One click turns the shortages into PO-2231.',tg:function(){return $('po');},dx:60,dy:10,hot:null}];
$('rush').addEventListener('click',function(e){var b=e.target.closest&&e.target.closest('button');if(!b)return;e.stopPropagation();var i=+b.dataset.i;if(engaged&&i===1&&S.ri===null&&cur<=1)goStep(2);else{S.ri=i;S.po=false;render();if(engaged){turnOff();hush();showHot(null);}}});
$('po').addEventListener('click',function(e){e.stopPropagation();if($('po').disabled)return;if(engaged&&S.ri===1&&cur<=4)goStep(5);else{S.po=true;render();if(engaged){turnOff();hush();showHot(null);}}});
function script(){var t=300;
later(function(){showStep(1,true);},t);t+=1700;
later(function(){showStep(2,true);},t);click(function(){return rushBtn(1);},function(){applyState(2);},t+900);t+=3700;
later(function(){showStep(3,true);},t);t+=3800;
later(function(){showStep(4,true);},t);t+=3800;
later(function(){showStep(5,true);},t);click(function(){return $('po');},function(){applyState(5);},t+900);t+=4400;
later(function(){hush();ghost.classList.remove('on');},t);t+=700;
later(function(){resetState();showHot(rushBtn(1));turnSay('Your turn. Pick a rush order size',fwb);},t);t+=6000;
later(function(){turnOff();showHot(null);},t);
return t+200;}
'''
SUMMARY='Dairy, card 4: Planning & Replenishment (week schedule, rush order, milk and vanilla shortages, purchase order from the shortage)'
ARIA='Interactive demo: a production schedule for a dairy plant. Pick a rush order size to see which runs move back and which run finishes past Friday, see the milk and vanilla base shortages, and raise a purchase order from them'
LEDE='This is a typical schedule view, built on your Sutton data with Studio. Want it different? Describe the change and Studio builds it.'
EXAMPLES=['Add a second shift','Show runs by customer','Reorder at a minimum level','Alert on late runs']
BUILT_ON='Production runs, stock, orders and purchase orders'
