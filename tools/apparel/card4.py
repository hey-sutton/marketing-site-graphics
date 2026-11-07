"""Apparel card 4: Wholesale & Online Orders. Layout: a status strip across the top, an order form with a size run grid on the left, a stock panel with online availability by size and a payment panel on the right."""
SUMMARY = 'Wholesale & Online Orders (an order by size run at the wholesale price, stock reserved away from online orders, a deposit synced to accounting, pick by scanning, pack and ship)'
ARIA = 'Interactive product screen: take wholesale order SO-6120 by size run, reserve the stock so online orders cannot sell it, record a deposit, pick by scanning, then pack and ship'
STEPS = 5
STUDIO = dict(lede='A typical wholesale order screen, built on your Sutton data with Studio. Want it different? Describe the change.',
              examples=['A size run template by retailer', 'A deposit tracker', 'A carton packing view', 'A wholesale price check'],
              built_on='Sales orders, stock, payments and shipments', change='Order fields, steps and views')

CSS = (
 '.stp4{display:flex;align-items:center;gap:0;padding:8px 40px 8px 16px;border-bottom:1px solid #E4E4E7;background:#FCFCFC}'
 '.sx{display:flex;align-items:center;gap:6px;font-size:9.8px;color:#71717A;flex:1}.sx i{width:16px;height:16px;border-radius:50%;border:1.5px solid #D4D4D8;display:grid;place-items:center;flex:none;font-style:normal;font-size:8.6px;font-weight:600;background:#fff;transition:background-color .3s,border-color .3s,color .3s}'
 '.sx.on{color:#18181B;font-weight:600}.sx.on i{background:#18181B;border-color:#18181B;color:#fff}.sx.dn i{background:#DCFCE7;border-color:#86EFAC;color:#166534}.sx.dn{color:#166534}.sx .bar{flex:1;height:1px;background:#E4E4E7;margin:0 6px}'
 '.b4{display:grid;grid-template-columns:392px 1fr;gap:12px;padding:12px 40px 0 16px;height:560px}'
 '.col{display:flex;flex-direction:column;gap:10px;min-height:0}'
 '.oh .g{display:grid;grid-template-columns:1fr 1fr;gap:7px 8px;padding:9px 11px}.oh .ft{display:flex;justify-content:flex-end;padding:0 11px 10px}'
 '.srun .row{grid-template-columns:44px 1fr 1fr 1fr 70px;min-height:27px}.srun .row.t{background:#FAFAFA;font-weight:600}.pk{display:inline-flex;align-items:center;gap:4px}.pk i{width:12px;height:12px;border-radius:50%;background:#DCFCE7;color:#166534;display:grid;place-items:center}.pk i svg{width:8px;height:8px}'
 '.ac .g{display:grid;grid-template-columns:1fr 1fr;gap:7px 8px;padding:9px 11px}.ac .ft{display:flex;justify-content:flex-end;align-items:center;gap:8px;padding:2px 11px 10px}.ac .nt{padding:8px 11px 0;color:#52525B;font-size:9.4px;line-height:1.4}'
 '.sk .row{grid-template-columns:36px 1fr 1fr 1fr;min-height:27px}.sk .row.h span{white-space:nowrap}.sk .lo{color:#B45309;font-weight:700}'
 '.py .row{grid-template-columns:1fr auto;min-height:26px}.py .row.t{font-weight:600;background:#FAFAFA}'
 '.oh.cmp .g,.oh.cmp .ft{display:none}.shp{flex:1 1 0;min-height:0}.shp .row{grid-template-columns:62px 1fr;min-height:24px;font-size:9.6px}.lg{flex:1 1 0;min-height:0}.lg .row{grid-template-columns:38px 1fr;min-height:23px;font-size:9.4px}.lg .row.new{animation:exflash 1.4s ease}'
)

WIN = (
 '<div class="hd"><svg width="16" height="16" viewBox="0 0 16 16" fill="none" aria-hidden="true"><rect x="3" y="1.8" width="10" height="12.4" rx="1.5" stroke="#18181B" stroke-width="1.2"/><path d="M5.5 5h5M5.5 7.8h5M5.5 10.6h3" stroke="#18181B" stroke-width="1.2" stroke-linecap="round"/></svg>'
 '<span class="tt">Sales order <span class="mono">SO-6120</span></span><span class="ch c-idle" id="hst">New</span><span class="sb grow">Wholesale, crew tee ST-210</span></div>'
 '<div class="stp4" id="stp4"></div>'
 '<div class="b4"><div class="col">'
 '<div class="cd oh frm" id="oh"><div class="ct"><span id="ohs">Order</span><span class="mut" style="font-weight:500">Wholesale price list</span></div><div class="g">'
 '<label class="fld" id="fcu"><small>Customer</small><input id="icu" value="Pinegate Outfitters" autocomplete="off"><span class="em">Pick a customer</span></label>'
 '<label class="fld" id="fsy"><small>Style</small><input id="isy" value="ST-210" autocomplete="off" spellcheck="false"><span class="em">Use ST-210</span></label>'
 '<label class="fld" id="fcl"><small>Color</small><input id="icl" value="Navy" autocomplete="off"><span class="em">Use Black, Navy or Sand</span></label>'
 '<div class="kv"><small>Price list</small><b class="mono" style="padding:5px 0">Wholesale, $11.50</b></div></div>'
 '<div class="ft"><button type="button" class="bt pri" id="nwo">New wholesale order</button></div></div>'
 '<div class="cd srun" id="sr"></div><div id="ac"></div>'
 '<div class="cd shp"><div class="ct">Ship to<span class="mut" style="font-weight:500">Pinegate Outfitters</span></div><div class="row"><span class="mut">Address</span><span>Pinegate DC, 410 Harbor Way, Tacoma WA</span></div><div class="row"><span class="mut">Requested</span><span>11/10, ground</span></div><div class="row"><span class="mut">Terms</span><span>30% deposit, balance net 30</span></div><div class="row"><span class="mut">Labels</span><span>Carton labels with order and size run</span></div></div>'
 '</div><div class="col">'
 '<div class="cd sk" id="sk"></div><div class="cd py" id="py"></div>'
 '<div class="cd lg"><div class="ct">Activity<span class="mut" style="font-weight:500">Pinegate Outfitters</span></div><div id="lg"></div></div>'
 '</div></div>'
)

JS = r'''
var FOC='.hd>*,.sx,.oh .ct,.oh .fld,.oh .kv,.oh .bt,.srun .row,.srun .ct,#ac .ct,#ac .fld,#ac .kv,#ac .nt,#ac .bt,#ac .ft>span,.sk .row,.sk .ct,.py .row,.py .ct,.lg';
var SZ=['XS','S','M','L','XL'],QTY=[6,12,24,8,6],NAVY=[18,44,70,9,31],PRICE=11.50;
var okSvg='<svg viewBox="0 0 10 10" fill="none"><path d="M2.2 5.2l1.9 1.9 3.8-4" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>';
var S;
function m(n){return '$'+n.toLocaleString('en-US',{minimumFractionDigits:2,maximumFractionDigits:2});}
function tot(){return QTY.reduce(function(a,b){return a+b;},0);}
function val(){return Math.round(tot()*PRICE*100)/100;}
function render(){var st=S.step;
var L=['Draft','Reserved','Deposit','Picked','Shipped'];$('stp4').innerHTML=L.map(function(x,i){var c=st>i+1||st===5&&i===4?'dn':st===i+1?'on':'';return '<span class="sx '+c+'"><i>'+(c==='dn'?'✓':(i+1))+'</i>'+x+(i<4?'<span class="bar"></span>':'')+'</span>';}).join('');
$('hst').textContent=st?L[st-1]:'New';$('hst').className='ch '+(st===5?'c-ok':st?'c-info':'c-idle');
$('oh').classList.toggle('cmp',st>0);$('ohs').innerHTML=st>0?'Pinegate Outfitters, <span class="mono">ST-210</span>, Navy, $11.50':'Order';var nb=$('nwo');nb.disabled=st>0;nb.className='bt '+(st>0?'done':'pri');nb.textContent=st>0?'Order SO-6120':'New wholesale order';
if(!st)$('sr').innerHTML='<div class="ct">Size run</div><div style="padding:10px 11px"><div class="empt"><b>No order lines yet</b><span>Start the order to take it by size run at the wholesale price.</span></div></div>';
else{var r='<div class="row h"><span>Size</span><span class="r">Qty</span><span class="r">Price</span><span class="r">Line</span><span class="r">Picked</span></div>';SZ.forEach(function(s,i){r+='<div class="row'+(S.anim&&st===1?' in':'')+'" style="animation-delay:'+(i*60)+'ms"><span>'+s+'</span><span class="mono r">'+QTY[i]+'</span><span class="mono r">'+m(PRICE)+'</span><span class="mono r">'+m(QTY[i]*PRICE)+'</span><span class="r">'+(st>=4?'<span class="pk mono">'+QTY[i]+' of '+QTY[i]+' <i>'+okSvg+'</i></span>':'<span class="mut mono">0 of '+QTY[i]+'</span>')+'</span></div>';});
r+='<div class="row t"><span>Total</span><span class="mono r" id="qt">'+tot()+'</span><span></span><span class="mono r" id="ov">'+m(val())+'</span><span class="mono r">'+(st>=4?tot():0)+' picked</span></div>';$('sr').innerHTML='<div class="ct">Size run, Navy<span class="ch c-idle">'+tot()+' pieces</span></div>'+r;}
var a='';
if(st===1)a='<div class="cd ac frm"><div class="ct">Next<span class="mut" style="font-weight:500">Draft</span></div><div class="nt">Hold the 56 pieces for Pinegate Outfitters so online orders cannot sell them.</div><div class="ft"><button type="button" class="bt pri" id="rsv">Reserve stock</button></div></div>';
else if(st===2)a='<div class="cd ac frm"><div class="ct">Deposit<span class="mut" style="font-weight:500">Terms: 30% to release</span></div><div class="g"><label class="fld" id="fdp"><small>Deposit, %</small><input id="idp" value="30" inputmode="numeric" autocomplete="off"><span class="em">10 to 100</span></label><div class="kv"><small>Amount</small><b class="mono" style="padding:5px 0" id="dam">'+m(Math.round(val()*30)/100)+'</b></div></div><div class="ft"><button type="button" class="bt pri" id="dep">Record deposit</button></div></div>';
else if(st===3)a='<div class="cd ac frm"><div class="ct">Pick<span class="mut" style="font-weight:500">Bin B-14, Navy tees</span></div><div class="g"><label class="fld" id="fsc"><small>Scan</small><input id="isc" value="Scan all 56" autocomplete="off"><span class="em">Scan all 56 pieces</span></label><div class="kv"><small>To pick</small><b class="mono" style="padding:5px 0">56 pieces, 5 sizes</b></div></div><div class="ft"><button type="button" class="bt pri" id="pks">Pick with scanning</button></div></div>';
else if(st===4)a='<div class="cd ac frm"><div class="ct">Pack and ship<span class="mut" style="font-weight:500">56 picked</span></div><div class="g"><label class="fld" id="fcn"><small>Cartons</small><input id="icn" value="2" inputmode="numeric" autocomplete="off"><span class="em">1 to 8, split evenly</span></label><div class="kv"><small>A carton</small><b class="mono" style="padding:5px 0" id="pcc">28 pieces</b></div></div><div class="ft"><button type="button" class="bt pri" id="shp">Pack and ship</button></div></div>';
else if(st===5)a='<div class="cd ac'+(S.anim?' in':'')+'"><div class="ct">Shipped<span class="ch c-ok">Packing slip PS-6120</span></div><div class="nt">'+S.cart+' cartons of '+(tot()/S.cart)+' left on 11/07 with tracking on the order. The invoice shows the deposit and the balance due.</div><div class="ft"></div></div>';
$('ac').innerHTML=a;
var k='<div class="ct">Stock, ST-210 Navy<span class="mut" style="font-weight:500">Pieces</span></div><div class="row h"><span>Size</span><span class="r">On hand</span><span class="r">Reserved</span><span class="r">Online</span></div>';
SZ.forEach(function(s,i){var rv=st>=2&&st<5?QTY[i]:0,oh=st>=5?NAVY[i]-QTY[i]:NAVY[i],on=NAVY[i]-(st>=2?QTY[i]:0);k+='<div class="row"><span>'+s+'</span><span class="mono r">'+oh+'</span><span class="mono r">'+(st>=2&&st<5?rv:'')+'</span><span class="mono r'+(st>=2&&on<=1?' lo':'')+'">'+on+'</span></div>';});
k+='<div class="row"><span></span><span class="mut" style="grid-column:2/-1;font-size:9px">'+(st<2?'No reservations on ST-210 Navy':st<5?'SO-6120 holds 56, hidden from online orders':'Shipped, on hand reduced by 56')+'</span></div>';$('sk').innerHTML=k;
var dep=S.dep,bal=Math.round((val()-dep)*100)/100;
$('py').innerHTML='<div class="ct">Payments<span class="ch '+(st>=3?'c-ok':'c-idle')+'">'+(st>=3?'Synced to accounting':'Not started')+'</span></div><div class="row"><span>Order value</span><span class="mono">'+(st?m(val()):'')+'</span></div><div class="row"><span>Deposit'+(st>=3?', '+S.pct+'%':'')+'</span><span class="mono" id="dpv">'+(st>=3?m(dep):'')+'</span></div><div class="row t"><span>'+(st>=5?'Balance due, invoiced':'Balance')+'</span><span class="mono" id="bal">'+(st>=3?m(bal):'')+'</span></div>';
$('lg').innerHTML=S.log.slice().reverse().map(function(l,i){return '<div class="row'+(i===0&&S.flash?' new':'')+'"><span class="mut mono">'+l[0]+'</span><span>'+l[1]+'</span></div>';}).join('');
S.anim=false;S.flash=false;}
$('ac').addEventListener('input',function(e){if(e.target.id==='idp'){var p=parseFloat(e.target.value);if(p>0&&p<=100)$('dam').textContent=m(Math.round(val()*p)/100);}if(e.target.id==='icn'){var c=parseInt(e.target.value,10);if(c>0&&tot()%c===0)$('pcc').textContent=(tot()/c)+' pieces';}});
function resetState(){S={step:0,dep:0,pct:30,cart:2,anim:false,flash:false,log:[['09/18','Pinegate Outfitters, spring order shipped, SO-5874'],['10/02','Price list Wholesale 2026 applied, $11.50 for ST-210'],['10/21','Size run template for Pinegate saved'],['11/04','Buyer asked for Navy, 56 pieces']]};$('icu').value='Pinegate Outfitters';$('isy').value='ST-210';$('icl').value='Navy';['fcu','fsy','fcl'].forEach(function(i){$(i).classList.remove('err');});render();}
function v(id){var e=$(id);return e?String(e.value).trim():'';}
function bad(id,c){var f=$(id);if(f)f.classList.toggle('err',c);return c;}
var CAPAT=function(hh){return{l:14,t:visH()-hh-14};};
var ST=[
{id:'nwo',target:function(){return $('nwo');},prompt:'Click New wholesale order',where:'below',ok:function(){var a=bad('fcu',!v('icu')),b=bad('fsy',v('isy').toUpperCase()!=='ST-210'),c=bad('fcl',v('icl').toLowerCase()!=='navy');return !(a||b||c);},
 run:function(){S.step=1;S.anim=true;S.flash=true;S.log.push(['11/06','SO-6120 drafted, 56 pieces, '+m(val())]);render();},after:['Taken by size run, at the wholesale price','56 pieces of Navy ST-210 at $11.50, '+m(Math.round(56*11.5*100)/100)+'.']},
{id:'rsv',target:function(){return $('rsv');},prompt:'Click Reserve stock',where:'below',run:function(){S.step=2;S.flash=true;S.log.push(['11/06','56 pieces reserved for SO-6120']);render();},after:['Reserved, so nothing sells twice','Online orders no longer see these pieces. Size L is down to 1 for online.']},
{id:'dep',target:function(){return $('dep');},prompt:'Click Record deposit',where:'below',ok:function(){var p=parseFloat(v('idp'));return !bad('fdp',!(p>=10&&p<=100&&/^\d+(\.\d+)?$/.test(v('idp'))));},
 run:function(){var p=parseFloat(v('idp'));if(!(p>0))p=30;S.pct=p;S.dep=Math.round(val()*p)/100;S.step=3;S.flash=true;S.log.push(['11/06','Deposit '+m(S.dep)+' recorded, synced to accounting, order released']);render();},after:function(){return['The deposit syncs to accounting',m(S.dep)+' recorded and the order is released for picking.'];}},
{id:'pks',target:function(){return $('pks');},prompt:'Click Pick with scanning',where:'below',ok:function(){return !bad('fsc',!/^(scan all 56|56)$/i.test(v('isc')));},run:function(){S.step=4;S.flash=true;S.log.push(['11/07','56 pieces picked by scan from bin B-14']);render();},after:['Every piece scanned against the order','All 56 picked, size by size, so the right sizes ship.']},
{id:'shp',target:function(){return $('shp');},prompt:'Click Pack and ship',where:'below',ok:function(){var c=parseInt(v('icn'),10);return !bad('fcn',!(/^\d+$/.test(v('icn'))&&c>=1&&c<=8&&tot()%c===0));},
 run:function(){S.cart=parseInt(v('icn'),10)||2;S.step=5;S.anim=true;S.flash=true;S.log.push(['11/07','Shipped in '+S.cart+' cartons, packing slip PS-6120, invoice sent']);render();},after:function(){return['Packed, shipped and invoiced',S.cart+' cartons of '+(tot()/S.cart)+'. Balance due '+m(Math.round((val()-S.dep)*100)/100)+' after the deposit.'];}}];
'''
