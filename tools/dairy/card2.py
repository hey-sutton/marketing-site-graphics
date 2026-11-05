"""Dairy card 2: Yield & Byproduct Management. Layout type: bars and a stacked split, with a cost table and a bulk to retail strip."""
CSS = ('.rg2{display:flex;gap:10px;width:656px;align-items:stretch}.yc,.oc{width:323px;flex:none;padding:8px 0 6px;height:190px}'
 '.yb{display:flex;align-items:center;gap:8px;padding:5px 10px}.yb small{width:48px;color:#52525B;font-size:8.8px;flex:none}.yt{flex:1;height:14px;background:#F4F4F5;border-radius:4px;overflow:hidden;position:relative}'
 '.yt i{position:absolute;left:0;top:0;bottom:0;border-radius:4px;transition:width .7s cubic-bezier(.22,.9,.28,1);width:0}.yt i.e{background:#D4D4D8}.yt i.a{background:#18181B}.yb b{width:56px;text-align:right;font-family:"JetBrains Mono",ui-monospace,monospace;font-size:9.2px;font-weight:500;flex:none}'
 '.sg{display:grid;grid-template-columns:1fr 1fr;margin-top:6px;border-top:1px solid #F0F0F1}.sg div{padding:9px 10px 7px;min-width:0;border-bottom:1px solid #F0F0F1}.sg div:nth-child(odd){border-right:1px solid #F0F0F1}.sg small{display:block;color:#71717A;font-size:8.2px;margin-bottom:2px}.sg span{display:block;font-family:"JetBrains Mono",ui-monospace,monospace;font-size:9.2px;font-weight:500;white-space:nowrap}.sg span.bad{color:#B91C1C}'
 '.sbx{display:flex;height:12px;border-radius:5px;overflow:hidden;margin:2px 10px 8px;background:#F4F4F5}.sbx div{height:100%;transition:width .7s cubic-bezier(.22,.9,.28,1)}'
 '.ol div.r{display:flex;align-items:center;gap:7px;padding:6px 10px;font-size:9.2px;color:#3F3F46}.ol i{width:8px;height:8px;border-radius:2px;flex:none}.ol b{margin-left:auto;font-family:"JetBrains Mono",ui-monospace,monospace;font-weight:500;color:#18181B;font-size:9.2px}.ol em{font-style:normal;width:40px;text-align:right;color:#71717A;font-family:"JetBrains Mono",ui-monospace,monospace;font-size:8.8px}'
 '.ct{width:656px;padding:8px 0 4px}.ct .th2,.ct .tr3{display:flex;align-items:center;padding:0 10px}.ct .th2{height:20px;color:#71717A;font-size:8.6px;font-weight:500}.ct .tr3{height:30px;border-top:1px solid #F0F0F1}'
 '.ct .c1{flex:1.4}.ct .c2{flex:1.2;font-family:"JetBrains Mono",ui-monospace,monospace;font-size:9px;color:#52525B}.ct .c3,.ct .c4,.ct .c5{flex:1;text-align:right;font-family:"JetBrains Mono",ui-monospace,monospace;font-size:9.2px}.ct .c1{font-weight:500}.ct .th2 .c2,.ct .th2 .c3,.ct .th2 .c4,.ct .th2 .c5{font-family:inherit;font-size:8.6px}.ct .tick{animation:tick .5s ease}@keyframes tick{40%{transform:scale(1.12)}}'
 '.cvs{display:flex;align-items:center;gap:10px;width:656px;padding:12px 10px}.ic{display:flex;justify-content:space-between;margin:6px 10px 0;padding-top:7px;border-top:1px solid #F0F0F1;font-size:9.2px;color:#52525B}.ic b{font-family:"JetBrains Mono",ui-monospace,monospace;font-weight:500;color:#18181B}.cvb{flex:1;min-width:0;border:1px solid #E4E4E7;border-radius:7px;padding:6px 9px;background:#fff}.cvb b{display:block;font-family:"JetBrains Mono",ui-monospace,monospace;font-size:9.4px;font-weight:600}.cvb span{display:block;color:#52525B;font-size:8.8px;margin-top:1px}'
 '.cvb.dash{border-style:dashed;background:#FAFAFA;color:#71717A}.cvb.ok{border-color:#BBF7D0;background:#F0FDF4}.cva{flex:none;color:#A1A1AA}.cvs button.fw-act{flex:none;padding:6px 10px}'
 '.seg2 button:disabled{opacity:.4;cursor:default}.lgd .e{background:#D4D4D8}.lgd .a{background:#18181B;border-color:#18181B}.lgd .p{background:#B45309;border-color:#B45309}.lgd .l{background:#E4E4E7}')
WIN = ('<div class="fw-head"><svg class="fw-icon" width="16" height="16" viewBox="0 0 16 16" fill="none"><path d="M2.5 13.5V6M6.2 13.5V3M9.9 13.5V8M13.5 13.5V5" stroke="#18181B" stroke-width="1.6" stroke-linecap="round"/></svg><div class="fw-title">Production run</div><span class="fw-chip chip-idle" id="vchip">No run selected</span></div>'
 '<div class="fw-tabs"><div class="fw-tab on">Yield</div><div class="fw-tab">Byproducts</div><div class="fw-tab">Cost</div></div><div class="fw-div"></div>'
 '<div class="fw-body off" id="fwb"><div class="ctl"><div class="ct-l"><small>Production run</small><span class="seg2" id="runs" role="group" aria-label="Production run"><button type="button" data-r="BT">Butter BT-1030-2</button><button type="button" data-r="CH">Cheddar CH-1030-1</button></span></div>'
 '<div class="ct-l rv"><small>Byproduct share of cost</small><span class="seg2" id="shr" role="group" aria-label="Byproduct share of cost"><button type="button" data-i="0">4%</button><button type="button" data-i="1">6%</button><button type="button" data-i="2">8%</button></span></div></div>'
 '<div class="stg" id="stg" style="height:367px;width:656px"><div class="emp"><svg width="22" height="22" viewBox="0 0 22 22" fill="none" aria-hidden="true"><path d="M4 18V9M9 18V4M14 18V11M19 18V7" stroke="#A1A1AA" stroke-width="1.6" stroke-linecap="round"/></svg><b>Choose a production run</b><span>See expected against actual yield, the byproduct the run made, how the cost is shared and how bulk turns into retail packs.</span></div>'
 '<div class="rv" style="display:flex;flex-direction:column;gap:10px">'
 '<div class="rg2"><div class="fw-card yc" id="ycard"><div class="ft-h"><span>Yield</span><span class="fw-chip chip-idle" id="ychip"></span></div>'
 '<div class="yb"><small>Expected</small><div class="yt"><i class="e" id="bexp"></i></div><b id="vexp"></b></div><div class="yb"><small>Actual</small><div class="yt"><i class="a" id="bact"></i></div><b id="vact"></b></div>'
 '<div class="sg"><div><small>Input</small><span id="sIn"></span></div><div><small>Standard yield</small><span id="sStd"></span></div><div><small>Actual yield</small><span id="sAct"></span></div><div><small>Variance</small><span id="sVar" class="bad"></span></div></div></div>'
 '<div class="fw-card oc"><div class="ft-h"><span>Where the input went</span><span class="fw-chip chip-idle" id="ochip"></span></div><div class="sbx" id="sbx"></div><div class="ol" id="ol"></div><div class="ic"><span id="icl"></span><b id="icost"></b></div></div></div>'
 '<div class="fw-card ct" id="ctab"><div class="th2"><span class="c1">Product</span><span class="c2">Lot</span><span class="c3">Share of cost</span><span class="c4">Cost</span><span class="c5">Per lb</span></div><div class="tr3"><span class="c1" id="n1"></span><span class="c2" id="l1"></span><span class="c3" id="s1"></span><span class="c4" id="k1"></span><span class="c5" id="p1"></span></div><div class="tr3"><span class="c1" id="n2"></span><span class="c2" id="l2"></span><span class="c3" id="s2"></span><span class="c4" id="k2"></span><span class="c5" id="p2"></span></div></div>'
 '<div class="fw-card cvs" id="cvs"><div class="cvb" id="cvL"></div><svg class="cva" width="18" height="12" viewBox="0 0 18 12" fill="none" aria-hidden="true"><path d="M1 6h14M11 2l4 4-4 4" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg><div class="cvb dash" id="cvR"></div><button type="button" class="fw-act pri" id="cvb">Convert to retail packs</button></div>'
 '</div></div>'
 '<div class="tr-act neutral" id="act" role="status" aria-live="polite" style="width:656px"><span id="act-icon"></span><div><p id="act-text"></p></div></div>'
 '<div class="lgd" aria-hidden="true"><span><i class="e"></i>Expected</span><span><i class="a"></i>Actual</span><span><i class="p"></i>Byproduct</span><span><i class="l"></i>Loss</span></div></div>')
JS = r'''var fwb=$('fwb'),act=$('act'),INTRO=fwb,CAPBOX=fwb,PROMPT='Choose a production run';
var RUNS={
BT:{k:'BT',name:'Butter',lot:'BT-1030-2',inp:'Cream, 40% fat',inLb:4800,rate:1.72,exp:2300,act:2240,by:'Buttermilk',byLot:'BM-1030-2',byLb:2540,shares:[4,6,8],def:1,bulk:'7 totes',ret:'PR-1031-1',retTxt:'2,240 one pound prints, 56 cases'},
CH:{k:'CH',name:'Cheddar',lot:'CH-1030-1',inp:'Milk, 3.7% fat',inLb:20000,rate:0.22,exp:2000,act:1960,by:'Whey',byLot:'WY-1030-1',byLb:17960,shares:[6,8,10],def:1,bulk:'49 blocks',ret:'PR-1031-2',retTxt:'3,920 half pound bars, 196 cases'}};
function fl(n){return Math.round(n).toLocaleString('en-US');}
function usd(n){return '$'+n.toLocaleString('en-US',{minimumFractionDigits:2,maximumFractionDigits:2});}
function calc(r,si){var sh=r.shares[si],tot=r.inLb*r.rate,byC=tot*sh/100,mainC=tot-byC;return{sh:sh,tot:tot,byC:byC,mainC:mainC,mainPer:mainC/r.act,byPer:byC/r.byLb,loss:r.inLb-r.act-r.byLb,vr:r.exp-r.act,vp:(r.exp-r.act)/r.exp*100,stdp:r.exp/r.inLb*100,actp:r.act/r.inLb*100};}
var S={run:null,si:1,conv:false};
function tx(i,t){var e=$(i);if(e.textContent!==t){e.textContent=t;if(e.classList.contains('c3')||e.classList.contains('c4')||e.classList.contains('c5')){e.classList.remove('tick');void e.offsetWidth;e.classList.add('tick');}}}
function render(){var seg=[].slice.call($('runs').children);seg.forEach(function(b){b.classList.toggle('on',b.dataset.r===S.run);});
if(!S.run){fwb.classList.add('off');$('vchip').textContent='No run selected';$('vchip').className='fw-chip chip-idle';act.className='tr-act neutral';$('act-icon').innerHTML=infoSvg;setText($('act-text'),'<b>Choose a production run.</b> Expected against actual yield, the byproduct and the cost share all follow from it.');return;}
var r=RUNS[S.run],c=calc(r,S.si);fwb.classList.remove('off');
[].slice.call($('shr').children).forEach(function(b,i){b.textContent=r.shares[i]+'%';b.classList.toggle('on',i===S.si);});
var vc=$('vchip');vc.textContent=fl(c.vr)+' lb under standard';vc.className='fw-chip chip-warn';
var yc=$('ychip');yc.textContent=r.name+' '+r.lot;
var mx=Math.max(r.exp,r.act);$('bexp').style.width=(r.exp/mx*100)+'%';$('bact').style.width=(r.act/mx*100)+'%';
tx('vexp',fl(r.exp)+' lb');tx('vact',fl(r.act)+' lb');tx('sIn',fl(r.inLb)+' lb');tx('sStd',c.stdp.toFixed(1)+'%');tx('sAct',c.actp.toFixed(1)+'%');tx('sVar',fl(c.vr)+' lb under, '+c.vp.toFixed(1)+'%');
$('ochip').textContent=r.inp;
var parts=[[r.name,r.act,'#18181B'],[r.by,r.byLb,'#B45309'],['Loss',c.loss,'#D4D4D8']];
$('sbx').innerHTML=parts.map(function(p){return '<div style="width:'+(p[1]/r.inLb*100)+'%;background:'+p[2]+'"></div>';}).join('');
$('ol').innerHTML=parts.map(function(p){return '<div class="r"><i style="background:'+p[2]+'"></i>'+p[0]+'<b>'+fl(p[1])+' lb</b><em>'+(p[1]/r.inLb*100).toFixed(1)+'%</em></div>';}).join('');
tx('icl','Input cost, '+fl(r.inLb)+' lb at '+usd(r.rate));tx('icost',usd(c.tot));tx('n1',r.name);tx('l1',r.lot);tx('s1',(100-c.sh)+'%');tx('k1',usd(c.mainC));tx('p1',usd(c.mainPer));tx('n2',r.by+' (byproduct)');tx('l2',r.byLot);tx('s2',c.sh+'%');tx('k2',usd(c.byC));tx('p2',usd(c.byPer));
$('cvL').innerHTML='<b>'+r.lot+'</b><span>'+r.bulk+', '+fl(r.act)+' lb bulk</span>';
var cr=$('cvR'),cb=$('cvb');if(S.conv){cr.className='cvb ok';cr.innerHTML='<b>'+r.ret+'</b><span>'+r.retTxt+', lot history kept</span>';cb.textContent='Converted';cb.classList.add('done');cb.disabled=true;}else{cr.className='cvb dash';cr.innerHTML='<b>Not converted yet</b><span>Bulk stays on the run lot</span>';cb.textContent='Convert to retail packs';cb.classList.remove('done');cb.disabled=false;}
var html;if(S.conv)html='<b>'+r.bulk+' of '+r.name.toLowerCase()+' became '+r.retTxt+'.</b> The lot history carries over, so a retail case still traces back to run '+r.lot+'.';
else html='<b>'+r.name+' came in '+fl(c.vr)+' lb under standard, '+c.vp.toFixed(1)+'%.</b> '+r.by+' is recorded as a byproduct, '+fl(r.byLb)+' lb, and takes '+c.sh+'% of the input cost, so '+r.name.toLowerCase()+' costs '+usd(c.mainPer)+' a pound.';
act.className='tr-act ok';$('act-icon').innerHTML=checkSvg;setText($('act-text'),html);}
function setState(run,si,conv){if(S.run===run&&S.si===si&&S.conv===conv)return;S.run=run;S.si=si;S.conv=conv;render();}
function selectRun(k){setState(k,RUNS[k].def,false);}
function resetState(){S={run:null,si:1,conv:false};render();hideTip();marker(1);showHot(engaged&&!reduce?runBtn('BT'):null);}
function runBtn(k){return $('runs').querySelector('[data-r="'+k+'"]');}
function shrBtn(i){return $('shr').children[i];}
function applyState(i){if(i<=2)setState('BT',1,false);else if(i===3)setState('BT',2,false);else if(i===4)setState('BT',2,true);else setState('CH',RUNS.CH.def,false);}
var ST=[
{m:'Pick a production run',s:'Butter run BT-1030-2: cream in, butter out.',tg:function(){return runBtn('BT');},dx:60,dy:10,hot:function(){return nx;}},
{m:'Expected against actual',s:'Butter came in 60 lb under standard, 2.6% short.',tg:function(){return $('ycard');},dx:150,dy:60,hot:function(){return shrBtn(2);}},
{m:'Set the cost share',s:'Move 8% of the cost to buttermilk and butter costs less a pound.',tg:function(){return shrBtn(2);},dx:20,dy:10,hot:function(){return $('cvb');}},
{m:'Convert bulk to retail',s:'7 totes become 56 cases, and the lot history carries over.',tg:function(){return $('cvb');},dx:60,dy:10,hot:function(){return runBtn('CH');}},
{m:'Try another run',s:'Cheddar makes whey, with its own standard yield.',tg:function(){return runBtn('CH');},dx:60,dy:10,hot:null}];
function adv(i){if(engaged)goStep(i);}
$('runs').addEventListener('click',function(e){var b=e.target.closest&&e.target.closest('button');if(!b)return;e.stopPropagation();var k=b.dataset.r;if(engaged&&k==='BT'&&!S.run)goStep(1);else if(engaged&&k==='CH'&&cur<=4)goStep(5);else{selectRun(k);if(engaged){turnOff();hush();showHot(null);}}});
$('shr').addEventListener('click',function(e){var b=e.target.closest&&e.target.closest('button');if(!b)return;e.stopPropagation();var i=+b.dataset.i;if(engaged&&S.run==='BT'&&i===2&&cur<=2)goStep(3);else{if(S.run){S.si=i;S.conv=false;render();}if(engaged){turnOff();hush();showHot(null);}}});
$('cvb').addEventListener('click',function(e){e.stopPropagation();if(!S.run||S.conv)return;if(engaged&&S.run==='BT'&&cur<=3)goStep(4);else{S.conv=true;render();if(engaged){turnOff();hush();showHot(null);}}});
function script(){var t=300;
later(function(){showStep(1,true);},t);click(function(){return runBtn('BT');},function(){selectRun('BT');},t+900);t+=2800;
later(function(){showStep(2,true);},t);t+=3800;
later(function(){showStep(3,true);},t);click(function(){return shrBtn(2);},function(){applyState(3);},t+900);t+=4400;
later(function(){showStep(4,true);},t);click(function(){return $('cvb');},function(){applyState(4);},t+900);t+=4400;
later(function(){showStep(5,true);},t);click(function(){return runBtn('CH');},function(){applyState(5);},t+900);t+=4400;
later(function(){hush();ghost.classList.remove('on');},t);t+=700;
later(function(){resetState();showHot(runBtn('BT'));turnSay('Your turn. Pick a production run',fwb);},t);t+=6000;
later(function(){turnOff();showHot(null);},t);
return t+200;}
'''
SUMMARY='Dairy, card 2: Yield & Byproduct Management (expected against actual yield, byproduct recording, cost share, bulk to retail conversion)'
ARIA='Interactive demo: a production run for a dairy plant. Pick a butter or cheddar run to see expected against actual yield, the byproduct it made and how its cost is shared, change the cost share, then convert bulk to retail packs'
LEDE='This is a typical production run view, built on your Sutton data with Studio. Want it different? Describe the change and Studio builds it.'
EXAMPLES=['Alert on yield variance','Compare runs by week','Show cost per case','Add a target yield per product']
BUILT_ON='Production runs, yields, byproducts and costs'
