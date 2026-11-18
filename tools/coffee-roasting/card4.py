"""Coffee roasting card 4: Packing, Labels & Shipping.
Layout: stage chain. A chain of five boxes (Roasted, Packed, Labeled, Allocated, Shipped) with running totals across the
top; under it the pack breakdown, the label, open wholesale orders by customer and bag size, and the sales order with
carrier rates and tracking.
A roasted lot packs into 12 oz and 5 lb bags whose weights plus the cupping retain reconcile to the roasted kg; labels
carry the lot and roast date; open orders draw on the packed bags; rates and the booking come from the same sales order.
Weights are kept in grams and money in cents, so every number is exact. 12 oz bags are filled to 340 g and 5 lb bags to
2,268 g. Carrier names are invented."""
from frame_auto import header

SUMMARY = 'Packing, Labels & Shipping (pack a roasted lot into 12 oz and 5 lb bags, print a label with lot and roast date, see open wholesale orders by customer and bag size, compare carrier rates on the sales order, book and see tracking)'
ARIA = 'Interactive product screen: roasted lot RL-8820, 43.000 kg, packs into 59 bags of 12 oz and 10 bags of 5 lb with 0.260 kg kept for cupping; 69 labels print with lot and roast date, three wholesale orders take 60 bags, sales order SO-7716 compares two carrier rates and booking writes tracking to the order'
STEPS = 5
STUDIO = dict(lede='A typical pack and ship screen, built on your Sutton data with Studio. Want it different? Describe the change.',
              examples=['Add a best by date to labels', 'Split a pallet by customer', 'Ship club orders in waves', 'Pick the cheapest rate'],
              built_on='Roasted lots, bags, sales orders and carriers', change='Bag sizes, label fields and rules')

ICON = '<path d="M2 5.5l6-3 6 3v5l-6 3-6-3z"/><path d="M2 5.5l6 3 6-3M8 8.5v5M5 4l6 3"/>'

CSS = (
 '.k4{padding:10px 40px 0 16px;display:flex;flex-direction:column;gap:10px}'
 '.k4s{height:44px;flex:none;display:flex;align-items:center;gap:8px;padding:0 10px}.k4s .fld{flex-direction:row;align-items:center;gap:8px;position:relative}.k4s .fld small{font-size:10px;color:#18181B;font-weight:600;white-space:nowrap}'
 '#pin{width:130px;font-size:10.4px;padding:6px 8px}.k4s .fld .em{position:absolute;left:0;top:30px;white-space:nowrap;background:#fff;padding:1px 4px;z-index:3}'
 '.psm{display:inline-flex;align-items:center;gap:5px;font-size:9.4px;color:#71717A}.psm .bt{font-size:9.6px;padding:4px 8px}.k4s .pnote{margin-left:auto;font-size:9px;color:#71717A}'
 '.chn{height:96px;flex:none;display:grid;grid-template-columns:repeat(5,1fr);gap:14px;padding:0 2px}'
 '.sb2{position:relative;border:1px solid #E4E4E7;border-radius:8px;background:#fff;padding:8px 9px;display:flex;flex-direction:column;gap:3px;transition:border-color .3s,background-color .3s}'
 '.sb2:not(:last-child)::after{content:"";position:absolute;right:-13px;top:50%;width:12px;height:2px;background:#D4D4D8}.sb2:not(:last-child)::before{content:"";position:absolute;right:-14px;top:calc(50% - 3px);border:4px solid transparent;border-left-color:#A1A1AA;border-right:0}'
 '.sb2 small{font-size:8.8px;color:#71717A;font-weight:500}.sb2 b{font-family:"JetBrains Mono",ui-monospace,monospace;font-size:15px;font-weight:600;letter-spacing:-.02em}.sb2 span{font-size:8.6px;color:#71717A;line-height:1.3}'
 '.sb2.on{border-color:#18181B;box-shadow:0 0 0 1px #18181B}.sb2.dn{background:#F0FDF4;border-color:#BBF7D0}.sb2 .wt{color:#A1A1AA;font-size:10px;font-family:inherit;font-weight:500}'
 '.k4m{display:grid;grid-template-columns:320px 330px;gap:10px;height:376px;flex:none}.k4l,.k4r{display:flex;flex-direction:column;gap:8px;min-width:0}'
 '.ppk{height:162px;flex:none}.plb{flex:1 1 auto}.pod{height:194px;flex:none}.pso{flex:1 1 auto}'
 '.ppk .empt,.plb .empt,.pod .empt,.pso .empt{margin:8px 10px;height:calc(100% - 46px);padding:8px}.plb .empt,.pso>.empt{padding-top:40px}'
 '.ppk .row{grid-template-columns:1fr 54px 70px;min-height:26px;font-size:9.4px}.ppk .row.h{min-height:22px}.ppk .row>span:not(:first-child){text-align:right;font-family:"JetBrains Mono",ui-monospace,monospace}.ppk .row.tot{background:#F0FDF4;font-weight:600}'
 '.lbw{display:grid;grid-template-columns:1fr 92px;gap:10px;padding:8px 11px}.lab{border:1px solid #D4D4D8;border-radius:7px;padding:8px 10px;display:flex;flex-direction:column;gap:3px;background:#FFFDF7}'
 '.lab .lt{font-size:11.6px;font-weight:600}.lab .ls{font-size:8.8px;color:#52525B}.lab .lk{display:grid;grid-template-columns:auto 1fr;gap:2px 8px;font-size:8.8px;margin-top:3px}.lab .lk b{font-family:"JetBrains Mono",ui-monospace,monospace;font-size:9.4px}'
 '.bc{height:22px;margin-top:4px;background:repeating-linear-gradient(90deg,#18181B 0 1px,transparent 1px 3px,#18181B 3px 5px,transparent 5px 6px,#18181B 6px 7px,transparent 7px 10px)}'
 '.lbs{display:flex;flex-direction:column;gap:6px;font-size:8.8px;color:#71717A}.lbs .bt{font-size:9.4px}.lbs b{font-family:"JetBrains Mono",ui-monospace,monospace;font-size:13px;color:#18181B}'
 '.pod .row{grid-template-columns:1fr 50px 44px 60px;min-height:27px;font-size:9.2px}.pod .row.h{min-height:22px}.pod .row>span:not(:first-child){text-align:right;font-family:"JetBrains Mono",ui-monospace,monospace}.pod .row.tot{background:#FAFAFA;font-weight:600}.pod .row.on{background:#FFFBEB}.pod .row.lf{color:#71717A}'
 '.pso .row{grid-template-columns:1fr 48px 60px 52px;min-height:30px;font-size:9.2px}.pso .row>span:nth-child(2),.pso .row>span:nth-child(3){text-align:right;font-family:"JetBrains Mono",ui-monospace,monospace}.pso .row>span:last-child{text-align:right}.pso .bt{font-size:9px;padding:3px 8px}.pso .row.bk{background:#F0FDF4}'
 '.soh{display:flex;justify-content:space-between;padding:6px 11px;font-size:9px;color:#71717A;border-bottom:1px solid #F0F0F1}.soh b{color:#18181B;font-family:"JetBrains Mono",ui-monospace,monospace}'
 '.trk{margin:6px 11px 4px;padding:6px 9px;border-radius:7px;background:#F0FDF4;border:1px solid #BBF7D0;font-size:9px;color:#166534;display:flex;justify-content:space-between}.trk b{font-family:"JetBrains Mono",ui-monospace,monospace}'
)

WIN = (
 header(ICON, 'Pack and ship', 'Roasted lots to bags, labels and shipments', '<span class="ch c-idle" id="pst">No lot open</span>')
 + '<div class="k4"><div class="cd k4s frm" id="psf"><label class="fld" id="pfl"><small>Roasted lot</small><input id="pin" value="" placeholder="Lot number" autocomplete="off" spellcheck="false" aria-label="Roasted lot number"><span class="em" id="pem">No roasted lot found. Try RL-8820</span></label>'
 '<button type="button" class="bt pri" id="pkb">Pack lot</button><span class="psm">Sample<button type="button" class="bt" id="psp" data-sample>RL-8820</button></span><span class="pnote">Packing line 2</span></div>'
 '<div class="chn" id="chn"></div>'
 '<div class="k4m"><div class="k4l"><div class="cd ppk" id="ppk"></div><div class="cd plb" id="plb"></div></div><div class="k4r"><div class="cd pod" id="pod"></div><div class="cd pso" id="pso"></div></div></div></div>'
)

JS = r'''
var FOC='.hd>*,.k4s>*,.chn,.ppk,.plb,.pod,.pso';
var LOT={id:'RL-8820',p:'Foundry espresso',rd:'Nov 17',lv:'Medium roast',g:43000};
/* bag sizes: label, fill grams, bags packed */
var BAGS=[['12 oz',340,59],['5 lb',2268,10]],RET=260;
/* open wholesale orders: sales order, customer, 12 oz bags, 5 lb bags */
var ORD=[['SO-7716','Larkspur Cafe Group',24,4],['SO-7721','Juniper Street Coffee',12,2],['SO-7730','Copperline Market',18,0]];
var CART=2,CARTG=900;
var RATES=[['Northwind Freight','Ground, 2 days',3840,'NW 4418 2093 77'],['Cascade Parcel','Express, next day',6125,'CP 7730 1186 04']];
var S;
function kg3(g){return (g/1000).toLocaleString('en-US',{minimumFractionDigits:3,maximumFractionDigits:3});}
function kg1(g){return (g/1000).toFixed(1);}
function usd(c){return '$'+(c/100).toFixed(2);}
function bagsN(){return BAGS.reduce(function(s,b){return s+b[2];},0);}
function packedG(){return BAGS.reduce(function(s,b){return s+b[1]*b[2];},0);}
function ordT(i){return ORD.reduce(function(s,o){return s+o[i+2];},0);}
function allocN(){return ordT(0)+ordT(1);}
function soG(){var o=ORD[0];return o[2]*BAGS[0][1]+o[3]*BAGS[1][1]+CART*CARTG;}
function soBags(){return ORD[0][2]+ORD[0][3];}
function render(){
var on=S.bk?3:S.od?2:S.lb?1:S.pk?0:-2;
var box=function(i,t,big,sub){var dn=i<=on;return '<div class="sb2'+(dn?' dn':'')+(i===on+1&&S.pk?' on':'')+'" id="sb'+i+'"><small>'+t+'</small>'+(big?'<b id="sv'+i+'">'+big+'</b><span id="ss'+i+'">'+sub+'</span>':'<b class="wt">Not started</b><span>&nbsp;</span>')+'</div>';};
$('chn').innerHTML=box(-1,'Roasted',S.pk?kg3(LOT.g)+' kg':'',S.pk?LOT.id+', '+LOT.rd:'')
+box(0,'Packed',S.pk?bagsN()+' bags':'',S.pk?kg3(packedG())+' kg in bags':'')
+box(1,'Labeled',S.lb?bagsN()+' labels':'',S.lb?'Lot and roast date on each':'')
+box(2,'Allocated',S.od?allocN()+' bags':'',S.od?ORD.length+' wholesale orders':'')
+box(3,'Shipped',S.bk?soBags()+' bags':'',S.bk?'1 order, tracking on it':'');
var P=$('ppk');
if(!S.pk)P.innerHTML='<div class="ct"><span>Pack</span></div><div class="empt"><b>Nothing packed</b><span>Pack a roasted lot into bag sizes.</span></div>';
else P.innerHTML='<div class="ct"><span>Pack '+LOT.id+', '+LOT.p+'</span><span class="ch c-ok">Reconciled</span></div><div class="row h"><span>Bag size</span><span>Bags</span><span>kg</span></div>'+BAGS.map(function(b,i){return '<div class="row"><span>'+b[0]+', '+n0(b[1])+' g fill</span><span id="pb'+i+'">'+b[2]+'</span><span id="pg'+i+'">'+kg3(b[1]*b[2])+'</span></div>';}).join('')
+'<div class="row"><span>Kept for cupping</span><span></span><span id="prt">'+kg3(RET)+'</span></div><div class="row tot"><span>Total, equals roasted</span><span id="pbn">'+bagsN()+'</span><span id="ptt">'+kg3(packedG()+RET)+'</span></div>';
var L=$('plb');
if(!S.pk)L.innerHTML='<div class="ct"><span>Label</span></div><div class="empt"><b>No label yet</b><span>Labels show the lot number and roast date.</span></div>';
else L.innerHTML='<div class="ct"><span>Label</span>'+(S.lb?'<span class="ch c-ok">Printed</span>':'<span class="ch c-idle">Preview</span>')+'</div><div class="lbw"><div class="lab"><span class="lt">'+LOT.p+'</span><span class="ls">'+LOT.lv+', 12 oz (340 g)</span><span class="lk"><span>Lot</span><b id="plt">'+LOT.id+'</b><span>Roasted</span><b id="prd">'+LOT.rd+', 2026</b></span><span class="bc"></span></div>'
+'<div class="lbs">'+(S.lb?'<span>Printed</span><b id="pln">'+bagsN()+'</b><span>'+BAGS.map(function(b){return b[2]+' for '+b[0];}).join(', ')+'</span>':'<span>One label per bag, '+bagsN()+' in all</span><button type="button" class="bt pri" id="plb1">Print labels</button>')+'</div></div>';
var O=$('pod');
if(!S.lb)O.innerHTML='<div class="ct"><span>Open wholesale orders</span></div><div class="empt"><b>No orders shown</b><span>Open orders by customer and bag size draw on packed stock.</span></div>';
else if(!S.od)O.innerHTML='<div class="ct"><span>Open wholesale orders</span><button type="button" class="bt pri" id="pob">Show open orders</button></div><div class="empt"><b>'+ORD.length+' orders waiting</b><span>Match them to the packed bags by size.</span></div>';
else O.innerHTML='<div class="ct"><span>Open wholesale orders</span><span class="ch c-info">'+ORD.length+' orders</span></div><div class="row h"><span>Customer</span><span>12 oz</span><span>5 lb</span><span>Order</span></div>'
+ORD.map(function(o,i){return '<div class="row'+(i===0&&S.rt?' on':'')+'"><span>'+o[1]+'</span><span id="po'+i+'a">'+o[2]+'</span><span id="po'+i+'b">'+o[3]+'</span><span>'+o[0]+'</span></div>';}).join('')
+'<div class="row tot"><span>Wholesale</span><span id="pota">'+ordT(0)+'</span><span id="potb">'+ordT(1)+'</span><span></span></div><div class="row lf"><span>Left for retail and web orders</span><span id="pla">'+(BAGS[0][2]-ordT(0))+'</span><span id="plb2">'+(BAGS[1][2]-ordT(1))+'</span><span></span></div>';
var R=$('pso'),o=ORD[0];
if(!S.od)R.innerHTML='<div class="ct"><span>Sales order</span></div><div class="empt"><b>No order open</b><span>Rates and labels come from the sales order.</span></div>';
else R.innerHTML='<div class="ct"><span>'+o[0]+', '+o[1]+'</span>'+(S.bk?'<span class="ch c-ok">Shipped</span>':S.rt?'<span class="ch c-warn">Pick a rate</span>':'<button type="button" class="bt pri" id="prb">Compare rates</button>')+'</div>'
+'<div class="soh"><span>'+o[2]+' x 12 oz, '+o[3]+' x 5 lb</span><span><b id="pcw">'+CART+' cartons, '+kg1(soG())+' kg</b></span></div>'
+(S.bk?'<div class="trk"><span>Tracking on '+o[0]+'</span><b id="ptk">'+RATES[0][3]+'</b></div>':'')+(S.rt?RATES.map(function(r,i){var bk=S.bk&&i===0;return '<div class="row'+(bk?' bk':'')+'"><span><b>'+r[0]+'</b><br><span class="mut">'+r[1]+'</span></span><span></span><span id="pr'+i+'">'+usd(r[2])+'</span><span>'+(S.bk?(bk?'<span class="ch c-ok">Booked</span>':''):i===0?'<button type="button" class="bt pri" id="pbk">Book</button>':'<button type="button" class="bt" id="pbk2">Book</button>')+'</span></div>';}).join(''):'<div class="empt" style="height:70px"><b>No rates yet</b><span>Rates come back for this order\'s weight.</span></div>')
;
var st=$('pst');st.textContent=S.bk?'Shipment booked':S.od?'Orders matched':S.lb?'Labels printed':S.pk?'Lot packed':'No lot open';st.className='ch '+(S.bk?'c-ok':S.pk?'c-info':'c-idle');}
function val(){return String($('pin').value).trim().toLowerCase().replace(/\s+/g,'');}
$('psp').addEventListener('click',function(){$('pin').value=LOT.id;$('pfl').classList.remove('err');});
function typeIn(id,t,done){var i=0;(function k(){$(id).value=t.slice(0,i);if(i<t.length){i++;later(k,60);}else done();})();}
function resetState(){S={pk:false,lb:false,od:false,rt:false,bk:false};$('pin').value='';$('pfl').classList.remove('err');render();}
var CAPAT=function(hh){return cur>=2?{l:14,t:visH()-hh-14}:{l:350,t:visH()-hh-14};};
var ST=[
{id:'pack',target:function(){return mode==='try'?$('pkb'):$('pin');},prompt:'Click Pack lot to pack roasted lot RL-8820',where:'below',
 ok:function(){if(!val())$('pin').value='RL-8820';var v=val(),b=!(v==='rl-8820'||v==='rl8820'||v==='8820');$('pem').textContent=v?'No roasted lot found. Try RL-8820':'Enter a lot, for example RL-8820';$('pfl').classList.toggle('err',b);return !b;},
 run:function(quick){var go=function(){$('pin').value=LOT.id;$('pfl').classList.remove('err');S.pk=true;render();};if(mode==='watch'&&!quick){S.pk=true;typeIn('pin',LOT.id,go);}else go();},
 after:function(){return['Packed into two bag sizes',LOT.id+', '+kg3(LOT.g)+' kg roasted: '+BAGS.map(function(b){return b[2]+' bags of '+b[0];}).join(' and ')+' hold '+kg3(packedG())+' kg, with '+kg3(RET)+' kg kept for cupping.'];}},
{id:'label',target:function(){return $('plb1');},prompt:'Print the labels',where:'above',run:function(){S.lb=true;render();},
 after:function(){return['Labels carry lot and roast date',bagsN()+' labels print with lot '+LOT.id+' and roast date '+LOT.rd+', one for every bag.'];}},
{id:'orders',target:function(){return $('pob');},prompt:'Show the open wholesale orders',where:'below',run:function(){S.od=true;render();},
 after:function(){return['Open orders by customer and size',ORD.length+' wholesale orders take '+ordT(0)+' bags of 12 oz and '+ordT(1)+' of 5 lb. '+(BAGS[0][2]-ordT(0))+' and '+(BAGS[1][2]-ordT(1))+' stay for retail and subscriptions.'];}},
{id:'rates',target:function(){return $('prb');},prompt:'Compare carrier rates for SO-7716',where:'below',run:function(){S.rt=true;render();},
 after:function(){return['Rates from the sales order',ORD[0][0]+' ships '+CART+' cartons, '+kg1(soG())+' kg: '+RATES[0][0]+' '+usd(RATES[0][2])+' in 2 days, '+RATES[1][0]+' '+usd(RATES[1][2])+' next day.'];}},
{id:'book',target:function(){return $('pbk');},prompt:'Book Northwind Freight',where:'above',run:function(){S.bk=true;render();},
 after:function(){return['Tracking lands on the order','Booked with '+RATES[0][0]+'. Tracking '+RATES[0][3]+' is on '+ORD[0][0]+', and '+soBags()+' bags show as shipped.'];}}];
'''
