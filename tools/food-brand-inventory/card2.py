"""Food brand inventory card 2: Outsourced Production Orders. Layout: list and detail.
Left: the outsourced order list with New order, and the co-packer's component balance under it. Right: the order record
for OP-1190 (2,000 Trail Mix Case preset): components from the BOM with Send components, the two purchase orders the
order generates (co-packer fee, packaging vendor), the order cost with Log fee, and the receipt with preset quantity
chips, yield variance and cost per case. Every number is computed from the data below (whole dollars)."""
from frame_auto import header

SUMMARY = 'Outsourced Production Orders (new order for 2,000 Trail Mix Case, send components, generate the co-packer and packaging POs, log the fee, receive 1,950 cases at $7.69 a case)'
ARIA = 'Interactive product screen: create an outsourced order for 2,000 cases of Trail Mix Case, send components to the co-packer, generate the co-packer and packaging purchase orders, log the co-packer fee and receive 1,950 cases with the yield variance and cost per case'
STEPS = 5
STUDIO = dict(lede='A typical outsourced order screen on your Sutton data. Want it different? Describe the change.',
              examples=['A fee per case or per run', 'A co-packer scorecard', 'Freight split by shipment', 'A yield alert over 3 percent'],
              built_on='BOMs, orders, POs and lots', change='Cost lines, statuses and views')

ICON = '<path d="M2.5 4h7v8h-7zM9.5 6.5h2.6L14 8.6V12H9.5"/><circle cx="5" cy="12.4" r="1.2"/><circle cx="11.8" cy="12.4" r="1.2"/>'

CSS = (
 '.g2{display:grid;grid-template-columns:196px 450px;gap:10px;padding:10px 44px 0 16px;height:550px}'
 '.lc{display:flex;flex-direction:column;gap:10px;min-width:0}.ol{flex:none;display:flex;flex-direction:column}.ol .ct .bt{font-size:9.4px;padding:3px 8px}'
 '.ol .row{grid-template-columns:1fr auto;min-height:44px;font-size:9.6px}.ol .on2{display:flex;flex-direction:column;gap:2px}.ol .on2 small{font-size:8.4px;color:#71717A}'
 '.bal{flex:1;display:flex;flex-direction:column}.bal .bx{padding:9px 11px 7px}.bal .big{font-size:20px}.bal .dl{font-size:9px;color:#52525B;margin-top:3px;line-height:1.4}'
 '.bal .row{grid-template-columns:1fr 50px 44px;font-size:9px;min-height:24px;padding:0 9px}.bal .row span:nth-child(n+2){text-align:right;font-family:"JetBrains Mono",ui-monospace,monospace}.bal .row.up span:nth-child(n+2){color:#166534}'
 '.tot{margin-top:auto;padding:9px 11px;border-top:1px solid #E4E4E7;font-size:9.1px;color:#52525B;line-height:1.4;background:#FAFAFA}'
 '.dt{display:flex;flex-direction:column}.dt>.empt{margin:10px;flex:1}'
 '.facts{display:grid;grid-template-columns:1.2fr 1.3fr .9fr 1fr;gap:8px;padding:8px 11px;border-bottom:1px solid #E4E4E7;background:#FCFCFC}.facts .kv b{font-size:10px}'
 '.dg{display:grid;grid-template-columns:1fr 1fr;gap:10px;padding:10px}'
 '.log{margin:0 10px 10px;flex:1;display:flex;flex-direction:column}.log .row{grid-template-columns:44px 1fr auto;font-size:9.2px;min-height:25px}.log .row span:first-child{color:#71717A}.log .wait{margin-top:auto}'
 '.dcol{display:flex;flex-direction:column;gap:10px;min-width:0}'
 '.sec{border:1px solid #E4E4E7;border-radius:8px;overflow:hidden;background:#fff}.sec .ct{height:28px;font-size:10px}.sec .ct .bt{font-size:9.2px;padding:3px 8px}'
 '.sec .row{font-size:9.3px;min-height:25px;padding:0 9px}.sec .row .nm small{display:block;font-size:8.2px;color:#71717A}'
 '.cmp .row{grid-template-columns:1fr 56px 52px}.cmp .row span:nth-child(n+2),.cst .row span:last-child,.po .row span:last-child{text-align:right;font-family:"JetBrains Mono",ui-monospace,monospace}'
 '.cst .row{grid-template-columns:1fr 60px}.po .row{grid-template-columns:1fr 50px;min-height:33px}.row.t{font-weight:600;background:#FAFAFA}'
 '.wait{padding:9px;font-size:9px;color:#A1A1AA;line-height:1.4}'
 '.rcv .pks{display:flex;align-items:center;gap:5px;padding:8px 9px;font-size:9.2px}.rcv .pks .lb{color:#52525B;margin-right:auto}'
 '.pk{font:inherit;font-family:"JetBrains Mono",ui-monospace,monospace;font-size:9.2px;padding:3px 7px;border:1px solid #E4E4E7;border-radius:999px;background:#fff;cursor:pointer}.pk.on{background:#18181B;border-color:#18181B;color:#fff}.pk:focus-visible{outline:2px solid #18181B;outline-offset:2px}'
 '.rcv .act{display:flex;justify-content:flex-end;padding:0 9px 8px}.rcv .act .bt{font-size:9.2px;padding:4px 10px}'
 '.res{display:grid;grid-template-columns:1fr 1fr;gap:7px 8px;padding:8px 9px;border-top:1px solid #F0F0F1;background:#F0FDF4}.res .kv b{font-size:12px;font-family:"JetBrains Mono",ui-monospace,monospace}.res .wide{grid-column:span 2}'
)

WIN = (
 header(ICON, 'Outsourced orders', 'Components out to the co-packer, finished cases back')
 + '<div class="g2"><div class="lc"><div class="cd ol" id="ol"></div><div class="cd bal" id="bal"></div></div><div class="cd dt" id="dt"></div></div>'
)

JS = r'''
var FOC='.hd>*,.ol .ct,.ol .row,.ol .tot,.bal,.dt>.ct,.facts,.sec';
var OLD=[['OP-1188','Fruit Crisp Case','Lakeview Packers','In production','c-info'],['OP-1186','Trail Mix Case','Ridgeway Co-Pack','Received','c-ok'],['OP-1182','Granola Bite Case','Ridgeway Co-Pack','Closed','c-idle']];
var ORD={id:'OP-1190',item:'Trail Mix Case',cp:'Ridgeway Co-Pack',q:2000,due:'Dec 8, 2026'};
var CMP=[['Peanuts',6000,3600,500,300],['Raisins',4500,2700,500,300],['Sunflower seeds',4250,1700,1375,550]];
var FREIGHT=500,PACK=2500,FEE=4000,BAL0=CMP.reduce(function(a,c){return a+c[4];},0);
var POS=[['PO-7741','Ridgeway Co-Pack','co-packer fee',FEE],['PO-7742','Brightfold Packaging','pouches and cases',PACK]];
var CHIPS=[1900,1950,2000];
var S;
function ing(){return CMP.reduce(function(a,c){return a+c[2];},0);}
function lines(){var L=[];if(S.sent){L.push(['Ingredients','Sent from the BOM',ing(),'cl-ing']);L.push(['Freight','To Ridgeway',FREIGHT,'cl-frt']);}
if(S.pos)L.push(['Packaging','PO-7742',PACK,'cl-pak']);if(S.fee)L.push(['Co-packer fee','PO-7741',FEE,'cl-fee']);return L;}
function cost(){return lines().reduce(function(a,l){return a+l[2];},0);}
function bal(){return BAL0+(S.sent&&!S.rcv?ing():0);}
function varq(){return ORD.q-S.rcv;}
function st(){return S.rcv?['Received','c-ok']:S.fee?['Fee logged','c-info']:S.pos?['POs sent','c-info']:S.sent?['Components sent','c-info']:['Draft','c-idle'];}
function render(){
var o='<div class="ct"><span>Orders</span>'+(S.nw?'':'<button type="button" class="bt pri" id="nwb">New order</button>')+'</div>';
var rows=OLD.slice();if(S.nw)rows.unshift([ORD.id,ORD.item,ORD.cp].concat(st()));
o+=rows.map(function(x,i){var me=S.nw&&i===0;return '<button type="button" class="row'+(me?' sel in':'')+'" id="o-'+x[0]+'"><span class="on2"><b class="mono">'+x[0]+'</b><small>'+x[1]+', '+x[2]+'</small></span><span class="ch '+x[4]+'"'+(me?' id="ost"':'')+'>'+x[3]+'</span></button>';}).join('');
$('ol').innerHTML=o;
var up=S.sent&&!S.rcv;
$('bal').innerHTML='<div class="ct"><span>At Ridgeway Co-Pack</span></div><div class="bx"><div class="kv"><small>Components held, at cost</small><b class="big mono" id="bv">$'+n0(bal())+'</b></div><div class="dl" id="bdl">'+
(S.rcv?'Used on '+ORD.id+'. Back to the $'+n0(BAL0)+' left from earlier runs.':S.sent?'Up $'+n0(ing())+' with the '+ORD.id+' components.':'Left over from earlier runs.')+'</div></div>'+
'<div class="row h"><span>Component</span><span>Held</span><span>Value</span></div>'+CMP.map(function(x,i){return '<div class="row'+(up?' up':'')+'"><span>'+x[0]+'</span><span id="bl-'+i+'">'+n0(x[3]+(up?x[1]:0))+' lb</span><span>$'+n0(x[4]+(up?x[2]:0))+'</span></div>';}).join('')+
'<div class="tot">Components stay yours while the co-packer holds them.</div>';
var d='<div class="ct"><span>'+(S.nw?'Outsourced order <span class="mono">'+ORD.id+'</span>':'Order')+'</span>'+(S.nw?'<span class="ch '+st()[1]+'">'+st()[0]+'</span>':'')+'</div>';
if(!S.nw)d+='<div class="empt"><b>No order open</b><span>Start an outsourced order to send components, raise the POs and receive finished cases.</span></div>';
else{var c=cost();
d+='<div class="facts in"><div class="kv"><small>Item</small><b>'+ORD.item+'</b></div><div class="kv"><small>Co-packer</small><b>'+ORD.cp+'</b></div><div class="kv"><small>Planned</small><b class="mono" id="pq">'+n0(ORD.q)+'</b></div><div class="kv"><small>Due</small><b>'+ORD.due+'</b></div></div><div class="dg in"><div class="dcol">';
d+='<div class="sec cmp"><div class="ct"><span>Components</span>'+(S.sent?'<span class="ch c-ok">Sent Nov 19</span>':'<button type="button" class="bt pri" id="snd">Send components</button>')+'</div><div class="row h"><span>From the BOM</span><span>Qty</span><span>Cost</span></div>'+
CMP.map(function(x){return '<div class="row"><span>'+x[0]+'</span><span>'+n0(x[1])+' lb</span><span>$'+n0(x[2])+'</span></div>';}).join('')+'<div class="row t"><span>Ingredients</span><span></span><span id="ingt">$'+n0(ing())+'</span></div></div>';
d+='<div class="sec po"><div class="ct"><span>Purchase orders</span>'+(S.pos?'<span class="ch c-ok">2 sent</span>':'<button type="button" class="bt" id="gpo">Generate POs</button>')+'</div>'+
(S.pos?POS.map(function(p){return '<div class="row in"><span class="nm"><b class="mono">'+p[0]+'</b> '+p[2]+'<small>'+p[1]+'</small></span><span id="pa-'+p[0]+'">$'+n0(p[3])+'</span></div>';}).join(''):'<div class="wait">The co-packer fee PO and the packaging PO come from this order, with its quantity.</div>')+'</div>';
d+='</div><div class="dcol"><div class="sec cst"><div class="ct"><span>Order cost</span>'+(S.fee?'<span class="ch c-ok">Fee logged</span>':'<button type="button" class="bt" id="lfe">Log fee</button>')+'</div>'+
(lines().length?lines().map(function(l){return '<div class="row in"><span class="nm">'+l[0]+'<small>'+l[1]+'</small></span><span id="'+l[3]+'">$'+n0(l[2])+'</span></div>';}).join('')+'<div class="row t"><span>Total</span><span id="ctot">$'+n0(c)+'</span></div>':'<div class="wait">Cost lines book as components ship, POs go out and the fee is logged.</div>')+'</div>';
d+='<div class="sec rcv"><div class="ct"><span>Receive cases</span>'+(S.rcv?'<span class="ch c-ok">Received</span>':'')+'</div>';
if(!S.rcv)d+='<div class="pks" id="pks"><span class="lb">Cases back</span>'+CHIPS.map(function(q){return '<button type="button" class="pk'+(S.qty===q?' on':'')+'" data-pick="1" data-q="'+q+'" id="q-'+q+'" aria-pressed="'+(S.qty===q?'true':'false')+'">'+n0(q)+'</button>';}).join('')+'</div><div class="act"><button type="button" class="bt pri" id="rcb">Receive</button></div>';
else d+='<div class="res in"><div class="kv"><small>Received</small><b id="rq">'+n0(S.rcv)+'</b></div><div class="kv"><small>Yield variance</small><b id="rv">'+n0(varq())+' ('+(varq()/ORD.q*100).toFixed(1)+'%)</b></div><div class="kv wide"><small>Cost per case, $'+n0(c)+' over '+n0(S.rcv)+' cases</small><b id="rpc">'+m2(c/S.rcv)+'</b></div></div>';
d+='</div></div></div>';
var A=[['Nov 19','Order created for '+n0(ORD.q)+' cases','Draft']];if(S.sent)A.push(['Nov 19','Components shipped, freight $'+n0(FREIGHT),'Sent']);if(S.pos)A.push(['Nov 19','PO-7741 and PO-7742 sent','2 POs']);if(S.fee)A.push(['Nov 20','Co-packer fee logged on PO-7741','$'+n0(FEE)]);if(S.rcv)A.push(['Dec 8','Lot TM-2624 received, '+n0(S.rcv)+' cases','Closed']);
d+='<div class="sec log in"><div class="ct"><span>Order activity</span><span class="ch c-idle">'+A.length+' events</span></div>'+A.map(function(a){return '<div class="row in"><span>'+a[0]+'</span><span>'+a[1]+'</span><span class="ch c-idle">'+a[2]+'</span></div>';}).join('')+'<div class="wait">Every event stays on the order, from components out to cases back.</div></div>';}
$('dt').innerHTML=d;
}
function resetState(){S={nw:false,sent:false,pos:false,fee:false,qty:0,rcv:0};render();}
winEl.addEventListener('click',function(e){var c=e.target.closest&&e.target.closest('[data-q]');if(c&&!S.rcv){S.qty=+c.getAttribute('data-q');render();}});
function capN(){var i=cap.querySelector('.m i');return i?+i.textContent:1;}
var CAPAT=function(hh){var w=cap.offsetWidth;return capN()===2?{l:visW()-w-14,t:visH()-hh-14}:{l:14,t:visH()-hh-14};};
var ST=[
{id:'new',target:function(){return $('nwb');},prompt:'Click New order',where:'below',run:function(){S.nw=true;render();},
 after:function(){return['A new outsourced order opens',ORD.id+' for '+n0(ORD.q)+' cases of '+ORD.item+' at '+ORD.cp+', due '+ORD.due+'.'];}},
{id:'send',target:function(){return $('snd');},prompt:'Send the components',where:'below',run:function(){S.sent=true;render();},
 after:function(){return['Components go out, the co-packer balance rises','$'+n0(ing())+' of ingredients now held at Ridgeway: $'+n0(BAL0)+' to $'+n0(bal())+'. Freight $'+n0(FREIGHT)+'.'];}},
{id:'pos',target:function(){return $('gpo');},prompt:'Generate the POs',where:'below',run:function(){S.pos=true;render();},
 after:function(){return['Two POs from the same order','PO-7741 to Ridgeway for the $'+n0(FEE)+' fee. PO-7742 to Brightfold Packaging for $'+n0(PACK)+'.'];}},
{id:'fee',target:function(){return $('lfe');},prompt:'Log the co-packer fee',where:'below',run:function(){S.fee=true;render();},
 after:function(){return['The fee books against the order','Ingredients, freight, packaging and fee: $'+n0(cost())+' in total.'];}},
{id:'rcv',target:function(){return $('rcb');},back:function(){return S.qty?null:[$('q-1950'),'Pick 1,950 cases','above'];},prompt:'Receive the cases',where:'below',
 run:function(){if(!S.qty)S.qty=1950;S.rcv=S.qty;render();},
 after:function(){return['Cases back, with yield and cost per case',n0(S.rcv)+' of '+n0(ORD.q)+' received, '+n0(varq())+' short ('+(varq()/ORD.q*100).toFixed(1)+'%). $'+n0(cost())+' over '+n0(S.rcv)+' is '+m2(cost()/S.rcv)+' a case.'];}}];
'''
