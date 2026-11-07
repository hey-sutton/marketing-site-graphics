"""Electronics card 2: Shortages & Purchase Orders. Layout: parts table with inline supply bars and a filter chip, demand by build panel, then a PO form and an approval card."""
SUMMARY = 'Shortages & Purchase Orders (net availability across open builds, demand by build, a PO from the shortage, approval by amount)'
ARIA = 'Interactive product screen: filter components to shortages, open the microcontroller to see which builds compete for it, create a purchase order for the shortage, send it for approval and approve it'
STEPS = 5
STUDIO = dict(lede='A typical shortage and purchasing screen, built on your Sutton data with Studio. Want it different? Describe the change.',
              examples=['A shortage view by supplier', 'Approval limits by buyer', 'A lead time watch list', 'A reorder suggestion screen'],
              built_on='Items, stock, purchase orders and manufacturing orders', change='Approval rules, fields and views')

CSS = (
 '.b2{display:grid;grid-template-columns:428px 1fr;gap:12px;padding:12px 40px 0 16px;height:596px}'
 '.l2c{display:flex;flex-direction:column;gap:10px;min-height:0}'
 '.flt{display:flex;align-items:center;gap:6px}.fc{border:1px solid #E4E4E7;border-radius:999px;background:#fff;padding:4px 10px;font-size:9.8px;cursor:pointer;transition:background-color .2s,border-color .2s,color .2s}'
 '.fc b{font-weight:600;margin-left:4px}.fc.on{background:#18181B;border-color:#18181B;color:#fff}.fc:focus-visible{outline:2px solid #18181B;outline-offset:2px}.fc.hint{border-radius:999px}'
 '.lg{margin-left:auto;display:flex;gap:10px;color:#52525B;font-size:8.8px}.lg span{display:inline-flex;align-items:center;gap:4px}.lg i{width:10px;height:7px;border-radius:2px;flex:none}'
 '.pt .row{grid-template-columns:1.25fr .62fr .62fr .72fr .7fr 96px;min-height:36px}.pt .row.h{min-height:24px}.pt .row.dim{opacity:.35}'
 '.pt .pn{display:flex;flex-direction:column;gap:2px}.pt .pn small{color:#71717A;font-size:8.6px}.neg{color:#B91C1C;font-weight:600}.pos{color:#166534;font-weight:600}'
 '.bar{position:relative;height:10px;background:#F4F4F5;border-radius:3px;overflow:visible}.bar i{position:absolute;top:0;bottom:0;border-radius:3px;transition:width .6s cubic-bezier(.22,.9,.28,1),left .6s cubic-bezier(.22,.9,.28,1)}'
 '.bar .oh{background:#3F3F46;left:0}.bar .oo{background:#A1A1AA}.bar .cm{position:absolute;top:-3px;bottom:-3px;width:2px;background:#B91C1C;border-radius:1px;transition:left .6s ease}.bar .cm.ok{background:#166534}'
 '.bl .row{grid-template-columns:62px 1fr 60px 52px;min-height:24px}.sp{flex:1 1 0;min-height:0}.sp .row{grid-template-columns:1.2fr 1.3fr .7fr .5fr;min-height:24px}.sum{display:flex;justify-content:space-between;align-items:center;padding:8px 11px;border-top:1px solid #F0F0F1;background:#FAFAFA}'
 '.dp{display:flex;flex-direction:column;gap:10px;min-height:0}'
 '.dk{display:grid;grid-template-columns:1fr 1fr;gap:8px;padding:10px 11px}'
 '.db{padding:6px 11px 8px}.db .dr{display:grid;grid-template-columns:52px 1fr 34px;align-items:center;gap:7px;height:25px;font-size:9.4px}'
 '.db .tk{position:relative;height:9px;background:#F4F4F5;border-radius:3px;overflow:hidden}.db .tk i{position:absolute;top:0;bottom:0;transition:width .6s ease}.db .tk .cv2{background:#3F3F46;left:0}.db .tk .sh{background:#F87171}'
 '.db .note{margin-top:6px;font-size:9.4px;color:#3F3F46;line-height:1.4}'
 '.frm .g{display:grid;grid-template-columns:1fr 1fr;gap:8px;padding:9px 11px}.frm .g .w{grid-column:1/-1}.frm .sum{display:flex;justify-content:space-between;align-items:center;padding:8px 11px;border-top:1px solid #F0F0F1;background:#FAFAFA}'
 '.frm .ft{display:flex;justify-content:flex-end;padding:8px 11px 10px}.frm .nt{padding:0 11px;color:#71717A;font-size:8.9px;line-height:1.4}'
 '.apv{padding:10px 11px;display:flex;flex-direction:column;gap:8px}.apv p{margin:0;font-size:9.6px;line-height:1.45;color:#3F3F46}'
)

WIN = (
 '<div class="hd"><svg width="16" height="16" viewBox="0 0 16 16" fill="none" aria-hidden="true"><path d="M2.5 13.5h11M4 11V6.5M7 11V3.5M10 11V8M13 11V5" stroke="#18181B" stroke-width="1.4" stroke-linecap="round"/></svg>'
 '<span class="tt">Component availability</span><span class="ch c-idle" id="hst">4 open builds</span><span class="sb grow">PCS-200 motor controller parts</span></div>'
 '<div class="b2"><div class="l2c">'
 '<div class="flt" id="flt"><button type="button" class="fc on" data-f="all">All parts<b>5</b></button><button type="button" class="fc" data-f="short" id="fsh">Shortages only<b id="nsh">2</b></button>'
 '<span class="lg" aria-hidden="true"><span><i style="background:#3F3F46"></i>On hand</span><span><i style="background:#A1A1AA"></i>On order</span><span><i style="background:#B91C1C;width:2px"></i>Committed</span></span></div>'
 '<div class="cd pt"><div class="row h"><span>Part</span><span class="r">On hand</span><span class="r">On order</span><span class="r">Committed</span><span class="r">Available</span><span>Supply and demand</span></div><div id="ptr"></div></div>'
 '<div class="cd bl"><div class="ct">Open builds using these parts<span class="mut" style="font-weight:500">By need date</span></div><div id="blr"></div></div>'
 '<div class="cd sp"><div class="ct">Suppliers and lead times<span class="mut" style="font-weight:500">Last price paid</span></div><div class="row h"><span>Supplier</span><span>Parts</span><span class="r">Lead time</span><span class="r">Price</span></div>'
 '<div class="row"><span>Northline Components</span><span class="mono">MCU-STM32</span><span class="mono r">21 days</span><span class="mono r">$4.60</span></div>'
 '<div class="row"><span>Kestrel Passives</span><span class="mono">CAP-1006, RES-0402</span><span class="mono r">14 days</span><span class="mono r">$0.12</span></div>'
 '<div class="row"><span>Ardent Power</span><span class="mono">IC-PWR</span><span class="mono r">28 days</span><span class="mono r">$1.35</span></div>'
 '<div class="row"><span>Corlink Connectors</span><span class="mono">CON-J12</span><span class="mono r">10 days</span><span class="mono r">$0.90</span></div></div>'
 '</div><div class="dp" id="dp"></div></div>'
)

JS = r'''
var FOC='.hd>*,.fc,.lg,.pt .row,.bl .ct,.bl .row,.dp .cd';
var P=[['MCU-STM32','Microcontroller',420,0,1150],['CAP-1006','10 uF capacitor',5200,2000,6480],['RES-0402','10k resistor',31000,0,24000],['IC-PWR','Power regulator',380,400,1100],['CON-J12','12 pin connector',900,0,750]];
var B=[['MO-3105','In progress',120,'11/07'],['MO-3102','Scheduled',250,'11/10'],['MO-3110','Scheduled',400,'12/01'],['MO-3118','Scheduled',380,'12/08']];
var PRICE=4.60,LEAD=21,LIMIT=2500,SUP='Northline Components';
var S;
function avail(p){return p[2]+p[3]+(p[0]==='MCU-STM32'&&S.rel?S.qty:0)-p[4];}
function onord(p){return p[3]+(p[0]==='MCU-STM32'&&S.rel?S.qty:0);}
function sgn(n){return (n>0?'+':n<0?'−':'')+n0(Math.abs(n));}
function render(){
[].forEach.call($('flt').querySelectorAll('.fc'),function(b){b.classList.toggle('on',b.getAttribute('data-f')===(S.f?'short':'all'));});
$('nsh').textContent=P.filter(function(p){return avail(p)<0;}).length;
var h='';P.forEach(function(p,i){var a=avail(p),oo=onord(p),show=!S.f||a<0||(p[0]==='MCU-STM32'&&S.rel);if(!show)return;var mx=Math.max(p[2]+oo,p[4])*1.08,isM=p[0]==='MCU-STM32';
var cells='<span class="pn"><b class="mono">'+p[0]+'</b><small>'+p[1]+'</small></span><span class="mono r">'+n0(p[2])+'</span><span class="mono r">'+n0(oo)+'</span><span class="mono r">'+n0(p[4])+'</span><span class="mono r '+(a<0?'neg':(isM&&S.rel?'pos':''))+'">'+sgn(a)+'</span>'+
'<span class="bar"><i class="oh" style="width:'+(p[2]/mx*100)+'%"></i><i class="oo" style="left:'+(p[2]/mx*100)+'%;width:'+(oo/mx*100)+'%"></i><i class="cm'+(a<0?'':' ok')+'" style="left:'+(p[4]/mx*100)+'%"></i></span>';
h+=isM?'<button type="button" class="row'+(S.sel?' sel':'')+(S.anim?' in':'')+'" id="rmcu" style="animation-delay:'+(i*50)+'ms">'+cells+'</button>':'<div class="row'+(S.anim?' in':'')+'" style="animation-delay:'+(i*50)+'ms">'+cells+'</div>';});
$('ptr').innerHTML=h;
var cum=P[0][2],bl='';B.forEach(function(b){var cov=Math.max(0,Math.min(b[2],cum));cum-=b[2];bl+='<div class="row"><span class="mono">'+b[0]+'</span><span class="mut">'+b[1]+', needs '+b[3]+'</span><span class="mono r">'+n0(b[2])+'</span>'+(S.sel&&!S.rel?(cov<b[2]?'<span class="ch c-bad">Short</span>':'<span class="ch c-ok">Covered</span>'):(S.rel?'<span class="ch c-ok">Covered</span>':'<span class="ch c-idle">Open</span>'))+'</div>';});$('blr').innerHTML=bl;
var st=$('hst');st.className='ch '+(S.rel?'c-ok':'c-idle');st.textContent=S.rel?'PO-1048 on order':'4 open builds';
var dp=$('dp');if(!S.sel){dp.innerHTML='<div class="cd" style="flex:1"><div class="ct">Part detail</div><div style="padding:10px 11px"><div class="empt"><b>Pick a part</b><span>See every build that needs it, where on hand stock runs out and what to order.</span></div></div></div>';S.anim=false;return;}
var m=P[0],a=avail(m),d='<div class="cd'+(S.anim&&!S.po?' in':'')+'"><div class="ct"><span class="mono">MCU-STM32</span><span class="ch '+(a<0?'c-bad':'c-ok')+'">'+(a<0?'Short '+n0(-a):'Covered')+'</span></div>'+
'<div class="dk"><div class="kv"><small>On hand</small><b class="mono">'+n0(m[2])+'</b></div><div class="kv"><small>On order</small><b class="mono">'+n0(onord(m))+'</b></div><div class="kv"><small>Committed</small><b class="mono">'+n0(m[4])+'</b></div><div class="kv"><small>Available</small><b class="mono '+(a<0?'neg':'pos')+'">'+sgn(a)+'</b></div></div>';
if(!S.po){var c2=m[2],rows='',first='';B.forEach(function(b){var cov=Math.max(0,Math.min(b[2],c2));c2-=b[2];if(cov<b[2]&&!first)first=b[0];rows+='<div class="dr"><span class="mono">'+b[0]+'</span><span class="tk"><i class="cv2" style="width:'+(cov/400*100)+'%"></i><i class="sh" style="left:'+(cov/400*100)+'%;width:'+((b[2]-cov)/400*100)+'%"></i></span><span class="mono r">'+n0(b[2])+'</span></div>';});
d+='<div class="db"><div class="mut" style="font-size:8.9px;margin-bottom:3px">Demand by build, in need order</div>'+rows+'<div class="note">On hand covers MO-3105 and MO-3102. <b>'+first+'</b> is the first build to run short.</div></div><div class="frm"><div class="ft"><button type="button" class="bt pri" id="cpo">Create PO</button></div></div></div>';}
else{d+='</div>';var tot=S.qty*PRICE;
if(!S.sent){d+='<div class="cd frm'+(S.anim?' in':'')+'"><div class="ct">New purchase order<span class="ch c-idle">Draft</span></div><div class="g">'+
'<label class="fld w" id="fsp"><small>Supplier</small><input id="isp" value="'+S.sup.replace(/"/g,'&quot;')+'" autocomplete="off"><span class="em">Pick a supplier</span></label>'+
'<label class="fld" id="fqt"><small>Quantity, multiples of 100</small><input id="iqt" value="'+S.qty+'" inputmode="numeric" autocomplete="off"><span class="em">Enter 800 or more, in hundreds</span></label>'+
'<div class="kv"><small>Unit price</small><b class="mono" style="padding:5px 0">'+m2(PRICE)+'</b></div></div>'+
'<div class="nt">Shortage 730, rounded up to the supplier multiple of 100. Lead time '+LEAD+' days, due 11/27.</div>'+
'<div class="sum"><span>Order total</span><b class="mono" id="pot">'+m2(tot)+'</b></div><div class="ft"><button type="button" class="bt pri" id="sfa">Send for approval</button></div></div>';}
else{d+='<div class="cd'+(S.anim?' in':'')+'"><div class="ct"><span>PO'+(S.rel?' <span class="mono">PO-1048</span>':' draft')+', '+S.sup+'</span><span class="ch '+(S.rel?'c-ok':'c-warn')+'">'+(S.rel?'Released':'Waiting')+'</span></div>'+
'<div class="sum"><span>'+S.sup+', <span class="mono">'+n0(S.qty)+' x '+m2(PRICE)+'</span></span><b class="mono" id="pot">'+m2(tot)+'</b></div>'+
'<div class="apv">'+(S.rel?'<p><b>Approved by R. Iyer, purchasing manager.</b> Sent to '+S.sup+', due 11/27, before MO-3110 needs it on 12/01.</p><p>MCU-STM32 now shows '+n0(S.qty)+' on order and '+sgn(avail(m))+' available.</p>':'<p><b>Over '+m2(LIMIT)+', so it needs the purchasing manager.</b> Orders up to '+m2(LIMIT)+' release on the buyer’s approval.</p><p class="mut">Rule: POs over '+m2(LIMIT)+' go to R. Iyer, purchasing manager.</p><div><button type="button" class="bt pri" id="apb">Approve as purchasing manager</button></div>')+'</div></div>';}}
dp.innerHTML=d;S.anim=false;}
$('flt').addEventListener('click',function(e){var b=e.target.closest&&e.target.closest('.fc');if(!b)return;S.f=b.getAttribute('data-f')==='short';S.anim=true;render();});
$('dp').addEventListener('input',function(e){if(e.target.id==='iqt'){var q=parseInt(e.target.value,10);if(q>0){S.qty=q;var t=$('pot');if(t)t.textContent=m2(q*PRICE);}}if(e.target.id==='isp')S.sup=e.target.value;});
function resetState(){S={f:false,sel:false,po:false,sent:false,rel:false,qty:800,sup:SUP,anim:false};render();}
function badPO(){var q=$('iqt'),s=$('isp');if(!q)return false;var v=parseInt(q.value,10),bq=!(String(q.value).trim()===String(v)&&v>=800&&v%100===0&&v<=5000),bs=!(s.value||'').trim();$('fqt').classList.toggle('err',bq);$('fsp').classList.toggle('err',bs);if(!bq)S.qty=v;if(!bs)S.sup=s.value.trim();return bq||bs;}
var CAPAT=function(hh){return{l:14,t:visH()-hh-14};};
var ST=[
{id:'short',target:function(){return $('fsh');},prompt:'Click Shortages only',where:'below',run:function(){S.f=true;S.anim=true;render();},after:['One filter shows every part that will stop a build','MCU-STM32 is short 730 and IC-PWR short 320, across all open builds.']},
{id:'mcu',target:function(){return $('rmcu');},prompt:'Click MCU-STM32',where:'below',run:function(){S.sel=true;S.anim=true;render();},after:['See which builds compete for the same part','On hand covers MO-3105 and MO-3102. MO-3110 is the first build to run short.']},
{id:'cpo',target:function(){return $('cpo');},prompt:'Click Create PO',where:'below',run:function(){S.po=true;S.anim=true;render();},after:function(){return['The shortage becomes a purchase order',n0(S.qty)+' from '+S.sup+' at '+m2(PRICE)+', '+m2(S.qty*PRICE)+', already filled in.'];}},
{id:'send',target:function(){return $('sfa');},prompt:'Click Send for approval',where:'below',ok:function(){return !badPO();},run:function(){badPO();S.sent=true;S.anim=true;render();},after:['Approval rules are built in','Over '+m2(LIMIT)+', so the order goes to the purchasing manager before release.']},
{id:'approve',target:function(){return $('apb');},prompt:'Click Approve as purchasing manager',where:'below',run:function(){S.rel=true;S.anim=true;render();},after:function(){return['Approved and on order','PO-1048 is out. MCU-STM32 shows '+n0(S.qty)+' on order and '+sgn(-730+S.qty)+' available.'];}}];
'''
