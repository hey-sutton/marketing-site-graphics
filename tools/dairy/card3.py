"""Dairy card 3: Expiry Tracking & FIFO. Layout type: a days-left timeline against a customer's shelf life rule, plus a FIFO pick list."""
CSS = ('.tl{width:656px;padding:8px 0 6px}.tl .ft-h{margin-bottom:4px}.ax{position:relative;height:18px;margin-left:128px;width:392px}.ax span{position:absolute;top:2px;font-size:8.2px;color:#71717A;transform:translateX(-50%);white-space:nowrap}.ax span.f{transform:none}.ax span.l{transform:translateX(-100%)}'
 '.ax .thl{top:1px;font-weight:600;color:#B91C1C;background:#fff;padding:0 3px;z-index:3}.rws{position:relative}.thr{position:absolute;top:0;bottom:0;width:0;border-left:1.5px dashed #B91C1C;z-index:3;pointer-events:none;transition:left .5s cubic-bezier(.22,.9,.28,1)}'
 '.lr{display:flex;align-items:center;width:100%;height:37px;margin:0;border:0;border-top:1px solid #F0F0F1;background:transparent;padding:0 10px;font:inherit;color:inherit;text-align:left;cursor:pointer;transition:background-color .2s}.lr:hover{background:#FAFAFA}.lr:focus-visible{outline:2px solid #18181B;outline-offset:-2px}.lr.fakehover{background:#F4F4F5}.lr.press{animation:fwpress .6s ease-out 1}'
 '.lr .lb{width:118px;flex:none}.lr .lb b{display:block;font-family:"JetBrains Mono",ui-monospace,monospace;font-size:9.4px;font-weight:600}.lr .lb span{color:#71717A;font-size:8.4px}'
 '.lr .tk{position:relative;width:392px;height:17px;flex:none;background:linear-gradient(to right,#EDEDEF 1px,transparent 1px) 0 0/98px 100%}.lr .tk i{position:absolute;left:0;top:0;bottom:0;width:0;border-radius:4px;display:flex;align-items:center;padding-left:6px;font-style:normal;font-size:8.4px;font-weight:500;white-space:nowrap;overflow:hidden;transition:width .7s cubic-bezier(.22,.9,.28,1),background-color .3s}'
 '.tk i.ok{background:#52525B;color:#fff}.tk i.pk{background:#FFB92B;color:#1B1B1A}.tk i.sh{background:#D4D4D8;color:#52525B}.tk i.hd{background:repeating-linear-gradient(135deg,#E4E4E7 0 5px,#F4F4F5 5px 10px);color:#52525B}'
 '.lr .stx{width:126px;flex:none;text-align:right;font-size:9px;color:#52525B}.lr .stx b{color:#18181B;font-weight:600}.lr .stx.bad{color:#B91C1C}'
 '.pkc{width:656px;padding:8px 0 4px}.pkc .th2,.pkc .tr3{display:flex;align-items:center;padding:0 10px}.pkc .th2{height:20px;color:#71717A;font-size:8.6px;font-weight:500}.pkc .tr3{height:28px;border-top:1px solid #F0F0F1}'
 '.pkc .c0{width:28px;flex:none;color:#71717A}.pkc .c1{flex:1.3;font-family:"JetBrains Mono",ui-monospace,monospace;font-size:9.4px;font-weight:600;display:flex;align-items:center;gap:7px}.pkc .c2,.pkc .c3,.pkc .c4{flex:1;font-family:"JetBrains Mono",ui-monospace,monospace;font-size:9.2px}.pkc .c4{text-align:right}'
 '.pkc .th2 .c1,.pkc .th2 .c2,.pkc .th2 .c3,.pkc .th2 .c4{font-family:inherit;font-size:8.6px;font-weight:500}.pkc .tr3 .fw-chip{font-family:Inter,ui-sans-serif,system-ui,sans-serif;font-size:8.4px}'
 '.lgd .pk{background:#FFB92B;border-color:#FFB92B}.lgd .ok{background:#52525B;border-color:#52525B}.lgd .sh{background:#D4D4D8}.lgd .hd{background:repeating-linear-gradient(135deg,#E4E4E7 0 3px,#F4F4F5 3px 6px)}.lgd .th{width:0;height:9px;border:0;border-left:1.5px dashed #B91C1C;border-radius:0;margin:0 2px}')
WIN = ('<div class="fw-head"><svg class="fw-icon" width="16" height="16" viewBox="0 0 16 16" fill="none"><rect x="2" y="3" width="12" height="11" rx="2" stroke="#18181B" stroke-width="1.3"/><path d="M2 6.5h12M5.5 1.8v2.4M10.5 1.8v2.4" stroke="#18181B" stroke-width="1.3" stroke-linecap="round"/></svg><div class="fw-title">Cooler stock</div><span class="fw-chip chip-idle" id="cchip">No customer selected</span></div>'
 '<div class="fw-tabs"><div class="fw-tab on">Lots</div><div class="fw-tab">Pick lists</div><div class="fw-tab">Holds</div></div><div class="fw-div"></div>'
 '<div class="fw-body off" id="fwb"><div class="ctl"><div class="ct-l"><small>Customer</small><span class="seg2" id="cus" role="group" aria-label="Customer"><button type="button" data-c="DC">Regional grocery DC</button><button type="button" data-c="SC">School district</button><button type="button" data-c="NF">Natural foods co-op</button></span></div>'
 '<div class="ct-l rv" style="text-align:right"><small>Shelf life rule</small><span class="fw-chip chip-idle" id="rule"></span></div></div>'
 '<div class="stg" id="stg" style="height:386px;width:656px"><div class="emp"><svg width="22" height="22" viewBox="0 0 22 22" fill="none" aria-hidden="true"><rect x="3" y="4.5" width="16" height="14" rx="2.5" stroke="#A1A1AA" stroke-width="1.5"/><path d="M3 9h16M7.5 2.5v3.5M14.5 2.5v3.5" stroke="#A1A1AA" stroke-width="1.5" stroke-linecap="round"/></svg><b>Choose a customer</b><span>Each customer accepts a different amount of shelf life. See which lots qualify and which ships first.</span></div>'
 '<div class="rv" style="display:flex;flex-direction:column;gap:10px"><div class="fw-card tl"><div class="ft-h"><span>Plain yogurt, days of shelf life left</span><span class="fw-chip chip-warn" id="sd"></span></div>'
 '<div class="ax" id="ax"><span class="f" style="left:0">Today</span><span style="left:98px">7</span><span style="left:196px">14</span><span style="left:294px">21</span><span class="l" style="left:392px">28 days</span><span class="thl" id="thl"></span></div>'
 '<div class="rws" id="rws"><span class="thr" id="thr"></span></div></div>'
 '<div class="fw-card pkc" id="pkc"><div class="ft-h"><span>Pick list, oldest qualifying lot first</span><span class="fw-chip chip-idle" id="pchip"></span></div><div class="th2"><span class="c0">#</span><span class="c1">Lot</span><span class="c2">Cases</span><span class="c3">Best before</span><span class="c4">Days left</span></div><div id="pkr"></div></div>'
 '</div></div>'
 '<div class="tr-act neutral" id="act" role="status" aria-live="polite" style="width:656px"><span id="act-icon"></span><div><p id="act-text"></p></div></div>'
 '<div class="lgd" aria-hidden="true"><span><i class="pk"></i>Picked</span><span><i class="ok"></i>Qualifies</span><span><i class="sh"></i>Too short</span><span><i class="hd"></i>On hold</span><span><i class="th"></i>Customer minimum</span></div></div>')
JS = r'''var fwb=$('fwb'),act=$('act'),INTRO=fwb,CAPBOX=fwb,PROMPT='Choose a customer';
var LOTS=[{k:'L1',t:'YG-1019-1',d:8,cs:120,bb:'Nov 10'},{k:'L2',t:'YG-1021-2',d:12,cs:240,bb:'Nov 14'},{k:'L3',t:'YG-1024-1',d:16,cs:300,bb:'Nov 18'},{k:'L4',t:'YG-1027-1',d:22,cs:180,bb:'Nov 24'},{k:'L5',t:'YG-1029-1',d:24,cs:360,bb:'Nov 26'}];
var CUS={DC:{n:'Regional grocery DC',min:14,order:300},SC:{n:'School district',min:10,order:150},NF:{n:'Natural foods co-op',min:18,order:200}};
var PX=14,S={c:null,hold:{}},rowEl={},barEl={},stEl={};
function fl(n){return n.toLocaleString('en-US');}
function jn(a){return a.length<2?a.join(''):a.slice(0,-1).join(', ')+' and '+a[a.length-1];}
var rws=$('rws');
LOTS.forEach(function(l){var b=document.createElement('button');b.type='button';b.className='lr';b.dataset.l=l.k;b.innerHTML='<span class="lb"><b>'+l.t+'</b><span>'+fl(l.cs)+' cases, '+l.bb+'</span></span><span class="tk"><i></i></span><span class="stx"></span>';rws.appendChild(b);rowEl[l.k]=b;barEl[l.k]=b.querySelector('i');stEl[l.k]=b.querySelector('.stx');});
var minAll=Math.min.apply(null,Object.keys(CUS).map(function(k){return CUS[k].min;})),shortCs=0;LOTS.forEach(function(l){if(l.d<minAll)shortCs+=l.cs;});
function plan(){var c=CUS[S.c],rem=c.order,picks=[];LOTS.forEach(function(l){l.el=l.d>=c.min&&!S.hold[l.k];l.take=0;if(l.el&&rem>0){var t=Math.min(l.cs,rem);l.take=t;rem-=t;picks.push(l);}});return{c:c,picks:picks,rem:rem};}
function render(){[].slice.call($('cus').children).forEach(function(b){b.classList.toggle('on',b.dataset.c===S.c);});
if(!S.c){fwb.classList.add('off');$('cchip').textContent='No customer selected';$('cchip').className='fw-chip chip-idle';act.className='tr-act neutral';$('act-icon').innerHTML=infoSvg;setText($('act-text'),'<b>Choose a customer.</b> Each one accepts a different amount of shelf life, and the oldest lot that qualifies ships first.');return;}
fwb.classList.remove('off');var P=plan(),c=P.c;
$('cchip').textContent=c.order+' cases picked';$('cchip').className='fw-chip chip-ok';$('rule').textContent=c.min+' or more days left, '+c.order+' cases';$('sd').textContent=fl(shortCs)+' cases short dated';
$('thr').style.left=(10+118+c.min*PX)+'px';
var th=$('thl');th.textContent='Min '+c.min+' days';th.style.left=(c.min*PX)+'px';
LOTS.forEach(function(l){var held=!!S.hold[l.k],bar=barEl[l.k],st=stEl[l.k],cl,txt,cls='';
if(held){cl='hd';txt='Quality hold';cls='bad';}else if(l.d<c.min){cl='sh';txt='Too short';cls='bad';}else if(l.take>0){cl='pk';txt='Pick <b>'+fl(l.take)+' cases</b>';}else{cl='ok';txt='Not needed';}
bar.className=cl;bar.style.width=(l.d*PX)+'px';bar.textContent=l.d+' days';st.innerHTML=txt;st.className='stx '+cls;});
var rows='';for(var i=0;i<3;i++){var l=P.picks[i];rows+='<div class="tr3">'+(l?'<span class="c0">'+(i+1)+'</span><span class="c1">'+l.t+(i===0?'<span class="fw-chip chip-ok">Pick first</span>':'')+'</span><span class="c2">'+fl(l.take)+'</span><span class="c3">'+l.bb+'</span><span class="c4">'+l.d+' days</span>':'<span class="c0"></span><span class="c1"></span><span class="c2"></span><span class="c3"></span><span class="c4"></span>')+'</div>';}
$('pkr').innerHTML=rows;$('pchip').textContent=c.n+', '+c.order+' cases';
var short=LOTS.filter(function(l){return l.d<c.min;}).map(function(l){return l.t;}),heldN=LOTS.filter(function(l){return S.hold[l.k];}).map(function(l){return l.t;});
var html='<b>'+c.n+' gets '+c.order+' cases from '+jn(P.picks.map(function(l){return l.t;}))+', oldest qualifying lot first.</b> They need '+c.min+' or more days left, so '+jn(short)+(short.length>1?' are':' is')+' too short.'+(heldN.length?' '+jn(heldN)+(heldN.length>1?' are':' is')+' on quality hold.':'')+(P.rem>0?' Still '+fl(P.rem)+' cases short.':'');
act.className='tr-act ok';$('act-icon').innerHTML=checkSvg;setText($('act-text'),html);}
function setState(c,h3){var hk=h3?{L3:1}:{};if(S.c===c&&!!S.hold.L3===!!h3&&Object.keys(S.hold).length===Object.keys(hk).length)return;S.c=c;S.hold=hk;render();}
function cusBtn(k){return $('cus').querySelector('[data-c="'+k+'"]');}
function resetState(){S={c:null,hold:{}};render();hideTip();marker(1);showHot(engaged&&!reduce?cusBtn('SC'):null);}
function applyState(i){if(i<=2)setState('SC',false);else if(i===3)setState('DC',false);else setState('DC',true);}
var ST=[
{m:'Pick a customer',s:'The school district takes lots with 10 or more days left.',tg:function(){return cusBtn('SC');},dx:60,dy:10,hot:function(){return nx;}},
{m:'Oldest qualifying lot first',s:'YG-1021-2 is the oldest lot that qualifies, so it ships first.',tg:function(){return rowEl.L2;},dx:260,dy:12,hot:function(){return cusBtn('DC');}},
{m:'Each customer has its own rule',s:'The grocery DC needs 14 days, so YG-1021-2 is too short.',tg:function(){return cusBtn('DC');},dx:60,dy:10,hot:function(){return rowEl.L3;}},
{m:'Hold a lot and the list updates',s:'Put YG-1024-1 on quality hold and the pick moves to the next lots.',tg:function(){return rowEl.L3;},dx:260,dy:12,hot:function(){return nx;}},
{m:'Short dated stock is flagged',s:'120 cases have 8 days left, and no customer will take them.',tg:function(){return rowEl.L1;},dx:260,dy:12,hot:null}];
$('cus').addEventListener('click',function(e){var b=e.target.closest&&e.target.closest('button');if(!b)return;e.stopPropagation();var k=b.dataset.c;if(engaged&&k==='SC'&&!S.c)goStep(1);else if(engaged&&k==='DC'&&cur<=2)goStep(3);else{S.c=k;S.hold={};render();if(engaged){turnOff();hush();showHot(null);}}});
rws.addEventListener('click',function(e){var b=e.target.closest&&e.target.closest('.lr');if(!b)return;e.stopPropagation();var k=b.dataset.l;if(engaged&&S.c==='DC'&&k==='L3'&&!S.hold.L3&&cur<=3)goStep(4);else{if(S.hold[k])delete S.hold[k];else S.hold[k]=1;render();if(engaged){turnOff();hush();showHot(null);}}});
function script(){var t=300;
later(function(){showStep(1,true);},t);click(function(){return cusBtn('SC');},function(){setState('SC',false);},t+900);t+=2800;
later(function(){showStep(2,true);},t);t+=3800;
later(function(){showStep(3,true);},t);click(function(){return cusBtn('DC');},function(){setState('DC',false);},t+900);t+=4400;
later(function(){showStep(4,true);},t);click(function(){return rowEl.L3;},function(){setState('DC',true);},t+900);t+=4600;
later(function(){showStep(5,true);},t);t+=4000;
later(function(){hush();ghost.classList.remove('on');},t);t+=700;
later(function(){resetState();showHot(cusBtn('SC'));turnSay('Your turn. Pick a customer',fwb);},t);t+=6000;
later(function(){turnOff();showHot(null);},t);
return t+200;}
'''
SUMMARY='Dairy, card 3: Expiry Tracking & FIFO (days of shelf life left against each customer\'s minimum, FIFO pick list, quality holds, short dated stock)'
ARIA='Interactive demo: cooler stock for a dairy plant. Pick a customer to see which yogurt lots meet their shelf life rule and which ships first, put a lot on quality hold to see the pick list change, and see the short dated stock no customer will take'
LEDE='This is a typical cooler stock view, built on your Sutton data with Studio. Want it different? Describe the change and Studio builds it.'
EXAMPLES=['Add a markdown action','Email short dated lots','Show shelf life by SKU','Add a hold reason']
BUILT_ON='Lots, best before dates, holds and customer rules'
