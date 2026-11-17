"""Coffee roasting card 4: Packing, Labels & Shipping.
Layout: stage chain. A horizontal chain of five boxes (Roasted, Packed, Labeled, Allocated, Shipped) with running totals,
and below it the pack form with its reconciliation, the label preview, the open wholesale orders and the carrier rates.
Pack roasted lot RL-1118-2 (36.000 kg) into 48 bags of 12 oz and 8 of 5 lb (34.473 kg packed, 1.527 kg left in the bin),
print the label with lot and roast date, see the three wholesale orders by bag size, compare two carrier rates from the
sales order, and book one so tracking lands on the order. Every weight is computed in milligrams."""
from frame_auto import header

SUMMARY = 'Packing, Labels & Shipping (pack a roasted lot into 12 ounce and 5 pound bags that reconcile to the roasted weight, print a label with lot and roast date, see wholesale orders by bag size, compare carrier rates, book the shipment with tracking)'
ARIA = 'Interactive product screen: roasted lot RL-1118-2 of 36.000 kg packs into 48 bags of 12 oz and 8 bags of 5 lb with 1.527 kg left, labels carry the lot and roast date, three wholesale orders take every bag, and booking Northline Freight writes tracking to SO-6101'
STEPS = 5
STUDIO = dict(lede='A typical packing and shipping flow, built on your Sutton data with Studio. Want it different? Describe the change.',
              examples=['Add a 2 lb bag size', 'Print a pallet label too', 'Pick the cheapest carrier', 'Email tracking to the buyer'],
              built_on='Roasted lots, sales orders and shipments', change='Bag sizes, labels and carriers')

ICON = '<path d="M3 5.5 8 3l5 2.5v5L8 13l-5-2.5z"/><path d="M3 5.5 8 8l5-2.5M8 8v5"/>'

CSS = (
 '.q4{padding:10px 40px 0 16px;display:flex;flex-direction:column;gap:10px}'
 '.qch4{height:96px;flex:none;display:grid;grid-template-columns:repeat(5,1fr);gap:14px;position:relative}'
 '.qsg{position:relative;border:1px solid #E4E4E7;border-radius:8px;background:#fff;padding:8px 9px;display:flex;flex-direction:column;gap:2px;transition:border-color .4s,background-color .4s}'
 '.qsg:not(:last-child)::after{content:"";position:absolute;right:-12px;top:42px;width:10px;height:2px;background:#A1A1AA}.qsg:not(:last-child)::before{content:"";position:absolute;right:-13px;top:39px;border:4px solid transparent;border-left-color:#A1A1AA}'
 '.qsg .qsn{font-size:9px;color:#71717A;font-weight:500;display:flex;justify-content:space-between}.qsg .qsv{font-family:"JetBrains Mono",ui-monospace,monospace;font-size:17px;font-weight:600;height:22px;color:#18181B}.qsg .qss{font-size:8.6px;color:#52525B;line-height:1.3}'
 '.qsg.qon{border-color:#18181B}.qsg.qok{border-color:#BBF7D0;background:#F0FDF4}.qsg .qsv:empty::before{content:"";display:inline-block;width:30px;height:15px;border-radius:4px;background:#F4F4F5;vertical-align:middle}'
 '.q4m{display:grid;grid-template-columns:360px 290px;gap:10px;height:226px;flex:none}.q4b{display:grid;grid-template-columns:360px 290px;gap:10px;height:188px;flex:none}.qod{display:flex;flex-direction:column}.qft9{margin-top:auto;padding:6px 11px;border-top:1px solid #F0F0F1;font-size:8.8px;color:#71717A}'
 '.qpk .qpf{display:flex;align-items:center;gap:7px;padding:8px 11px 0;flex-wrap:wrap}.qpk .fld{flex-direction:row;align-items:center;gap:5px;position:relative}.qpk .fld small{font-size:9.4px;color:#18181B;font-weight:600}.qpk .fld input{width:46px;text-align:right;font-size:10px;padding:4px 6px}'
 '.qpk .qsp{display:inline-flex;align-items:center;gap:5px;font-size:9px;color:#71717A}.qpk .qsp .bt{font-size:9px;padding:3px 7px}.qpk .qerr{display:none;color:#B91C1C;font-size:8.8px;padding:3px 11px 0}.qpk.err .qerr{display:block}.qpk.err input{border-color:#F87171;background:#FEF2F2}'
 '.qrc{padding:6px 11px 0}.qrc .row{grid-template-columns:1fr 92px 76px;min-height:23px;padding:0 4px;font-size:9.4px}.qrc .row>span:not(:first-child){text-align:right}.qrc .row.qt{font-weight:600;background:#FAFAFA}.qrc .row.qlft{color:#92400E}'
 '.qpk .empt,.qlb .empt,.qod .empt,.qcr .empt{margin:8px 10px;height:calc(100% - 48px);padding:8px}'
 '.qlbl{margin:10px auto 0;width:220px;border:1px solid #D4D4D8;border-radius:8px;padding:9px 11px;background:#FFFDF8;display:flex;flex-direction:column;gap:3px;font-size:9.2px;color:#3F3F46;box-shadow:0 2px 6px rgba(0,0,0,.05)}'
 '.qlbl .qln{font-size:12px;font-weight:700;color:#18181B}.qlbl .qlr{display:flex;justify-content:space-between}.qlbl .qlr b{font-family:"JetBrains Mono",ui-monospace,monospace;font-size:9.4px;color:#18181B}'
 '.qlbl .qbc{height:20px;margin-top:4px;background:repeating-linear-gradient(90deg,#18181B 0 1px,transparent 1px 3px,#18181B 3px 5px,transparent 5px 6px,#18181B 6px 7px,transparent 7px 9px)}.qlb .qlc{text-align:center;font-size:8.8px;color:#71717A;margin-top:6px}'
 '.qod .row{grid-template-columns:62px 1fr 42px 36px 62px;min-height:24px;font-size:9.2px;gap:6px}.qod .row>span:nth-child(3),.qod .row>span:nth-child(4){text-align:right}.qod .row.qt{font-weight:600;background:#FAFAFA}.qod .row .qtk{font-family:"JetBrains Mono",ui-monospace,monospace;font-size:8.4px;color:#166534}'
 '.qrt{padding:6px 11px 0;display:flex;flex-direction:column;gap:6px}.qrr{display:grid;grid-template-columns:1fr auto auto;gap:8px;align-items:center;border:1px solid #E4E4E7;border-radius:7px;padding:6px 8px;font-size:9.2px}.qrr b{font-weight:600;display:block}.qrr .mono{font-weight:600;font-size:10px}.qrr.qbk{border-color:#BBF7D0;background:#F0FDF4}'
 '.qrt .qnt{font-size:8.8px;color:#71717A}.qrt .qtr{font-family:"JetBrains Mono",ui-monospace,monospace;font-size:9.4px;color:#166534}'
)

WIN = (
 header(ICON, 'Pack and ship', 'Roasted lot RL-1118-2, Harbor House blend', '<span class="ch c-idle" id="qst">Not packed</span>')
 + '<div class="q4"><div class="qch4" id="qchn"></div>'
 '<div class="q4m"><div class="cd qpk" id="qpk"><div class="ct"><span>Pack</span><span class="ch c-info">36.000 kg roasted</span></div>'
 '<div class="qpf frm" id="qpff"><label class="fld"><small>12 oz bags</small><input id="qn12" value="" inputmode="numeric" placeholder="0" autocomplete="off" aria-label="Number of 12 ounce bags"></label>'
 '<label class="fld"><small>5 lb bags</small><input id="qn5" value="" inputmode="numeric" placeholder="0" autocomplete="off" aria-label="Number of 5 pound bags"></label><button type="button" class="bt pri" id="qpb">Pack</button>'
 '<span class="qsp">Sample<button type="button" class="bt" id="qsm" data-sample>Open orders</button></span></div><span class="qerr" id="qpe">Enter whole bags that fit in 36.000 kg</span><div id="qrcb"></div></div>'
 '<div class="cd qlb" id="qlb"></div></div>'
 '<div class="q4b"><div class="cd qod" id="qod"></div><div class="cd qcr" id="qcr"></div></div></div>'
)

JS = r'''
var FOC='.hd>*,.qch4,.qpk,.qlb,.qod,.qcr';
var LOTMG=36000000,OZ12=340194,LB5=2267960;
var LOT={id:'RL-1118-2',blend:'Harbor House blend',roast:'Nov 18, 2026',best:'Feb 16, 2027'};
var ORDS=[{id:'SO-6101',c:'Harbor Lane Cafe',n12:24,n5:4},{id:'SO-6102',c:'Copperleaf Bakery',n12:16,n5:2},{id:'SO-6103',c:'Fieldstone Office Coffee',n12:8,n5:2}];
var RATES=[{c:'Northline Freight',s:'Ground, 2 days',p:1840,tk:'NLF 7714 2093 18'},{c:'Parcel Express',s:'Next day',p:3175,tk:'PXP 55 0918 4402'}];
var S;
function kgm(mg){var g=Math.round(mg/1000);return (g/1000).toLocaleString('en-US',{minimumFractionDigits:3,maximumFractionDigits:3});}
function mg(n12,n5){return n12*OZ12+n5*LB5;}
function packed(){return mg(S.n12,S.n5);}
function bagsT(){return S.n12+S.n5;}
function ordT(k){return ORDS.reduce(function(s,o){return s+o[k];},0);}
function usd(c){return '$'+(c/100).toFixed(2);}
function box(i,name,v,sub,on,ok){return '<div class="qsg'+(ok?' qok':on?' qon':'')+'" id="qg'+i+'"><span class="qsn"><span>'+name+'</span><span>'+(i+1)+'</span></span><span class="qsv" id="qv'+i+'">'+v+'</span><span class="qss" id="qs'+i+'">'+sub+'</span></div>';}
function render(){
var al=S.ord?Math.min(bagsT(),ordT('n12')+ordT('n5')):0,sh=S.book?ORDS[0].n12+ORDS[0].n5:0;
$('qchn').innerHTML=box(0,'Roasted',kgm(LOTMG),'kg, '+LOT.id,!S.pk,true)
+box(1,'Packed',S.pk?String(bagsT()):'',S.pk?kgm(packed())+' kg in bags':'Waiting',S.pk&&!S.lab,S.pk)
+box(2,'Labeled',S.lab?String(bagsT()):'',S.lab?'Lot and roast date':'Waiting',S.lab&&!S.ord,S.lab)
+box(3,'Allocated',S.ord?String(al):'',S.ord?al+' of '+bagsT()+' bags, '+ORDS.length+' orders':'Waiting',S.ord&&!S.book,S.ord)
+box(4,'Shipped',S.book?String(sh):'',S.book?'1 of '+ORDS.length+' orders':'Waiting',false,S.book);
var r=$('qrcb');
if(!S.pk)r.innerHTML='<div class="empt" style="margin:8px 10px;height:128px"><b>Nothing packed yet</b><span>Enter bag counts and the packed weight reconciles to the roasted lot.</span></div>';
else r.innerHTML='<div class="qrc"><div class="row h"><span>Line</span><span>Weight each</span><span>kg</span></div>'
+'<div class="row"><span>'+S.n12+' bags of 12 oz</span><span class="mono">340.194 g</span><span class="mono" id="qk12">'+kgm(S.n12*OZ12)+'</span></div>'
+'<div class="row"><span>'+S.n5+' bags of 5 lb</span><span class="mono">2,267.960 g</span><span class="mono" id="qk5">'+kgm(S.n5*LB5)+'</span></div>'
+'<div class="row qt"><span>Packed</span><span></span><span class="mono" id="qkp">'+kgm(packed())+'</span></div>'
+'<div class="row qlft"><span>Left in the bin</span><span></span><span class="mono" id="qkl">'+kgm(LOTMG-packed())+'</span></div>'
+'<div class="row qt"><span>Roasted lot</span><span></span><span class="mono" id="qkr">'+kgm(LOTMG)+'</span></div></div>';
var l=$('qlb');
if(!S.lab)l.innerHTML='<div class="ct"><span>Label</span>'+(S.pk?'<button type="button" class="bt pri" id="qlp">Print labels</button>':'')+'</div><div class="empt"><b>No labels printed</b><span>Each bag gets the blend, lot number and roast date.</span></div>';
else l.innerHTML='<div class="ct"><span>Label</span><span class="ch c-ok" id="qlc">'+bagsT()+' printed</span></div><div class="qlbl" id="qlbl"><span class="qln">'+LOT.blend+'</span><span class="qlr"><span>Lot</span><b id="qll">'+LOT.id+'</b></span><span class="qlr"><span>Roasted</span><b id="qlr">'+LOT.roast+'</b></span><span class="qlr"><span>Best by</span><b>'+LOT.best+'</b></span><span class="qlr"><span>Net weight</span><b>12 oz (340 g)</b></span><span class="qbc"></span></div><div class="qlc">'+S.n12+' of 12 oz and '+S.n5+' of 5 lb, same lot and date</div>';
var o=$('qod');
if(!S.ord)o.innerHTML='<div class="ct"><span>Open wholesale orders</span>'+(S.lab?'<button type="button" class="bt pri" id="qos">Show orders</button>':'')+'</div><div class="empt"><b>No orders shown</b><span>Wholesale orders by customer and bag size.</span></div><div class="qft9">Wholesale orders due to ship November 19.</div>';
else o.innerHTML='<div class="ct"><span>Open wholesale orders</span><span class="ch c-ok">All bags allocated</span></div><div class="row h"><span>Order</span><span>Customer</span><span>12 oz</span><span>5 lb</span><span>Status</span></div>'
+ORDS.map(function(x,i){var b=S.book&&i===0;return '<div class="row" id="qor'+i+'"><span class="mono">'+x.id+'</span><span>'+x.c+'</span><span class="mono">'+x.n12+'</span><span class="mono">'+x.n5+'</span><span>'+(b?'<span class="qtk" id="qtk">'+RATES[S.rate].tk+'</span>':'<span class="ch c-idle">Allocated</span>')+'</span></div>';}).join('')
+'<div class="row qt"><span>Total</span><span></span><span class="mono" id="qo12">'+ordT('n12')+'</span><span class="mono" id="qo5">'+ordT('n5')+'</span><span></span></div><div class="qft9">Wholesale orders due to ship November 19.</div>';
var c=$('qcr'),w=mg(ORDS[0].n12,ORDS[0].n5);
if(!S.rt)c.innerHTML='<div class="ct"><span>Carrier rates</span>'+(S.ord?'<button type="button" class="bt pri" id="qcm">Compare rates</button>':'')+'</div><div class="empt"><b>No rates yet</b><span>Rates come from the sales order weight and address.</span></div>';
else c.innerHTML='<div class="ct"><span>Rates for '+ORDS[0].id+'</span><span class="mut" style="font-weight:400" id="qwt">'+kgm(w)+' kg</span></div><div class="qrt">'
+RATES.map(function(x,i){var bk=S.book&&S.rate===i;return '<div class="qrr'+(bk?' qbk':'')+'"><span><b>'+x.c+'</b><span class="mut">'+x.s+'</span></span><span class="mono" id="qrp'+i+'">'+usd(x.p)+'</span>'+(S.book?(bk?'<span class="ch c-ok">Booked</span>':'<span></span>'):'<button type="button" class="bt'+(i===0?' pri':'')+'" id="qbk'+i+'">Book</button>')+'</div>';}).join('')
+(S.book?'<span class="qtr">Tracking '+RATES[S.rate].tk+' on '+ORDS[0].id+'</span>':'<span class="qnt">Saves '+usd(RATES[1].p-RATES[0].p)+' against next day.</span>')+'</div>';
var st=$('qst');st.textContent=S.book?ORDS[0].id+' shipped':S.ord?'Allocated':S.lab?'Labeled':S.pk?'Packed':'Not packed';st.className='ch '+(S.book?'c-ok':S.pk?'c-info':'c-idle');}
function iv(id){var v=String($(id).value).trim();return /^\d+$/.test(v)?parseInt(v,10):NaN;}
function typeIn(id,t,done){var i=0;(function k(){$(id).value=t.slice(0,i);if(i<t.length){i++;later(k,90);}else done();})();}
winEl.addEventListener('click',function(e){var t=e.target.closest&&e.target.closest('#qsm');if(!t)return;$('qn12').value=String(ordT('n12'));$('qn5').value=String(ordT('n5'));$('qpk').classList.remove('err');});
function resetState(){S={pk:false,lab:false,ord:false,rt:false,book:false,n12:0,n5:0,rate:0};$('qn12').value='';$('qn5').value='';$('qpk').classList.remove('err');render();}
var CAPAT=function(hh){return cur<=1?{l:380,t:visH()-hh-14}:{l:14,t:visH()-hh-14};};
var ST=[
{id:'pack',target:function(){return mode==='try'?$('qpb'):$('qn12');},prompt:'Enter 48 and 8, or pick Open orders, then Pack',where:'below',
 ok:function(){var a=iv('qn12'),b=iv('qn5'),bad=!(a>=0&&b>=0&&a+b>0&&mg(a,b)<=LOTMG);$('qpk').classList.toggle('err',bad);return !bad;},
 run:function(quick){var go=function(){var a=iv('qn12'),b=iv('qn5');if(mode==='watch'||!(a+b>0)){a=48;b=8;}$('qn12').value=a;$('qn5').value=b;S.n12=a;S.n5=b;S.pk=true;render();};
 if(mode==='watch'&&!quick)typeIn('qn12','48',function(){typeIn('qn5','8',go);});else{if(!$('qn12').value){$('qn12').value='48';$('qn5').value='8';}go();}},
 after:function(){return['Pack a roasted lot into 12 ounce and 5 pound bags',S.n12+' × 12 oz is '+kgm(S.n12*OZ12)+' kg, '+S.n5+' × 5 lb is '+kgm(S.n5*LB5)+' kg. '+kgm(packed())+' kg packed, '+kgm(LOTMG-packed())+' kg left of '+kgm(LOTMG)+'.'];}},
{id:'lab',target:function(){return $('qlp');},prompt:'Click Print labels',where:'below',run:function(){S.lab=true;render();},
 after:function(){return['Print a label with the lot number and roast date',bagsT()+' labels for '+LOT.id+', roasted '+LOT.roast+', best by '+LOT.best+'.'];}},
{id:'ord',target:function(){return $('qos');},prompt:'Click Show orders',where:'above',run:function(){S.ord=true;render();},
 after:function(){return['See open wholesale orders by customer and bag size',ORDS.length+' orders take '+ordT('n12')+' × 12 oz and '+ordT('n5')+' × 5 lb, every bag packed.'];}},
{id:'rt',target:function(){return $('qcm');},prompt:'Click Compare rates',where:'above',run:function(){S.rt=true;render();},
 after:function(){return['Compare carrier rates from the sales order',ORDS[0].id+', '+kgm(mg(ORDS[0].n12,ORDS[0].n5))+' kg: '+RATES.map(function(x){return x.c+' '+usd(x.p);}).join(', ')+'.'];}},
{id:'book',target:function(){return $('qbk0');},prompt:'Book Northline Freight',where:'above',run:function(){S.rate=0;S.book=true;render();},
 after:function(){return['Book the shipment and see tracking on the order',RATES[0].c+' booked for '+usd(RATES[0].p)+'. Tracking '+RATES[0].tk+' is on '+ORDS[0].id+'.'];}}];
'''
