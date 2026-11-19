"""Food distributors card 3: Quotes, Orders & Price Lists. Layout: a stage chain.
Top: the read only customer field with Start quote, then the quote lines (two preset lines). Middle: the chain Quote,
Sales order, Reserved, Status link with running totals. Bottom: the customer's price list with its quantity break
(Apply price list) and the stock for the two items (Reserve stock). Prices are kept in cents so every sum is exact."""
import json
from frame_auto import header

SUMMARY = 'Quotes, Orders & Price Lists (start a quote for Greenfield Market, apply the price list and the 100 case break, $6,700.00 + $4,400.00 = $11,100.00, convert to SO-3110, reserve 200 and 50 cases, send the status link)'
ARIA = 'Interactive product screen: build a quote for a customer, apply their price list and quantity break, convert the quote to a sales order, reserve stock against it and send the customer an order status link'
STEPS = 5
STUDIO = dict(lede='A typical quote to order screen on your Sutton data. Want it different? Describe the change.',
              examples=['Breaks by mixed case count', 'A margin floor per line', 'Quotes that expire in 14 days', 'Status links by text message'],
              built_on='Quotes, price lists, orders and stock', change='Prices, stages and views')

ICON = '<path d="M3 2.5h7l3 3v8H3z"/><path d="M10 2.5v3h3M5.5 8h5M5.5 10.5h3"/>'

CSS = (
 '.fld input[readonly]{background:#F4F4F5;color:#3F3F46;cursor:default;pointer-events:none}'
 '.g3c{display:grid;grid-template-rows:60px 150px 118px 180px;gap:10px;padding:10px 44px 0 16px;width:716px}'
 '.top{display:flex;flex-direction:column;justify-content:center;gap:5px;padding:0 12px}.top .frm{display:flex;align-items:flex-end;gap:8px}.top .fld{width:170px}.top .ctx{font-size:8.9px;color:#71717A}.top .rsc{margin-left:auto}'
 '.ql{display:flex;flex-direction:column}.ql>.empt{margin:9px;flex:1;padding:8px}.ql .ct .bt{font-size:9px;padding:2px 9px}.ql .ct .bt:disabled{opacity:.45;cursor:not-allowed}'
 '.ql .row{grid-template-columns:1fr 50px 62px 62px 118px 78px;font-size:9.4px;min-height:30px}.ql .row>span:nth-child(2),.ql .row>span:nth-child(3),.ql .row>span:nth-child(4),.ql .row>span:nth-child(6){text-align:right;font-family:"JetBrains Mono",ui-monospace,monospace}.ql .row.h>span{font-family:inherit!important}'
 '.ql .row .was{color:#A1A1AA;text-decoration:line-through;margin-right:4px;font-size:8.6px}.ql .row.sm{background:#FAFAFA;font-weight:600;min-height:28px}.ql .row small{display:block;color:#71717A;font-size:8.2px;font-family:inherit}'
 '.chain{display:grid;grid-template-columns:1fr 16px 1fr 16px 1fr 16px 1fr}.arw{display:grid;place-items:center;color:#A1A1AA}.arw svg{width:10px;height:10px}'
 '.stg{border:1px solid #E4E4E7;border-radius:8px;background:#fff;display:flex;flex-direction:column;overflow:hidden;transition:background-color .35s,border-color .35s}'
 '.stg .sh{display:flex;align-items:center;justify-content:space-between;gap:4px;padding:6px 9px;border-bottom:1px solid #F0F0F1;font-weight:600;font-size:10.2px}'
 '.stg .vol{padding:6px 9px 0}.stg .vol small{display:block;font-size:8.5px;color:#71717A}.stg .vol b{font-family:"JetBrains Mono",ui-monospace,monospace;font-size:13.5px;font-weight:600}'
 '.stg .lim{padding:3px 9px 0;font-size:8.6px;color:#52525B;line-height:1.35}.stg .lim .bt{font-size:9px;padding:2px 9px;margin-top:2px}'
 '.stg .run{margin-top:auto;padding:5px 9px;border-top:1px dashed #E4E4E7;font-size:8.5px;color:#52525B;display:flex;justify-content:space-between}.stg .run em{font-style:normal;font-family:"JetBrains Mono",ui-monospace,monospace;font-weight:600;color:#18181B}'
 '.stg.e{background:#FAFAFA}.stg.e .sh{color:#A1A1AA}.stg.ok{border-color:#BBF7D0}'
 '.lk{display:inline-flex;align-items:center;gap:4px;margin-top:3px;padding:2px 7px;border-radius:999px;background:#E8EEFC;color:#1E3A8A;font-size:8.8px;font-weight:500}.lk svg{width:10px;height:10px}'
 '.bot{display:grid;grid-template-columns:1fr 1fr;gap:10px}.bc{display:flex;flex-direction:column}.bc>.empt{margin:9px;flex:1;padding:8px}.bc .ct .bt{font-size:9px;padding:2px 9px}.bc .ct .bt:disabled{opacity:.45;cursor:not-allowed}'
 '.pl .row{grid-template-columns:1fr 50px 58px 100px;font-size:9.2px;min-height:30px}.pl .row>span:nth-child(n+2){text-align:right;font-family:"JetBrains Mono",ui-monospace,monospace}.pl .row.h>span{font-family:inherit!important}.pl .row small{display:block;color:#71717A;font-size:8.1px;font-family:inherit}'
 '.sk .row{grid-template-columns:1fr 54px 60px 66px;font-size:9.2px;min-height:30px}.sk .row>span:nth-child(n+2){text-align:right;font-family:"JetBrains Mono",ui-monospace,monospace}.sk .row.h>span{font-family:inherit!important}.sk .rv{color:#1E3A8A;font-weight:600}'
 '.ft{margin-top:auto;padding:7px 10px;border-top:1px solid #F0F0F1;font-size:8.6px;color:#71717A;background:#FAFAFA}.bot .bc:last-child .ft{padding-right:96px}'
)

ARW = '<div class="arw" aria-hidden="true"><svg viewBox="0 0 10 10" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"><path d="M2 5h6M5.5 2.5L8 5 5.5 7.5"/></svg></div>'
LINK = '<svg viewBox="0 0 12 12" fill="none" stroke="currentColor" stroke-width="1.3" stroke-linecap="round"><path d="M5 7l2-2M4.2 5.8L3 7a1.8 1.8 0 0 0 2.5 2.5l1.2-1.2M7.8 6.2L9 5A1.8 1.8 0 0 0 6.5 2.5L5.3 3.7"/></svg>'

WIN = (
 header(ICON, 'Quote to order', 'Quotes priced from each customer\'s price list')
 + '<div class="g3c"><div class="cd top"><div class="frm"><label class="fld"><small>Customer</small>'
 '<input id="icu" value="Greenfield Market" readonly tabindex="-1" autocomplete="off" spellcheck="false"></label>'
 '<button type="button" class="bt pri" id="sqb">Start quote</button><span class="rsc" id="rsc"></span></div><div class="ctx">Ships from the main warehouse, terms net 30</div></div>'
 '<div class="cd ql" id="ql"></div><div class="chain" id="chn"></div><div class="bot"><div class="cd bc" id="plc"></div><div class="cd bc" id="skc"></div></div></div>'
)

JS = r'''
var FOC='.hd>*,.top .fld,.top .ctx,#sqb,.ql .ct,.ql .row,.ql>.empt,.stg,.bc .ct,.bc .row,.bc>.empt,.bc .ft';
var LINES=[{sku:'PP-20',nm:'Penne Pasta 20 lb Case',sh:'Penne',q:200,list:3800,pl:3500,brk:[100,3350],av:900},
{sku:'OO-4G',nm:'Olive Oil 4 x 1 gal',sh:'Olive Oil',q:50,list:9200,pl:8800,brk:null,av:180}];
var S;
function mc(c){return m2(c/100);}
function brk(l){return l.brk&&l.q>=l.brk[0];}
function price(l){return !S.ap?l.list:brk(l)?l.brk[1]:l.pl;}
function lt(l){return l.q*price(l);}
function qt(){return LINES.reduce(function(a,l){return a+lt(l);},0);}
function cases(){return LINES.reduce(function(a,l){return a+l.q;},0);}
function rsv(l){return S.rs?l.q:0;}
function stg(nm,cls,stc,vol,vl,lim,run){return '<div class="stg'+(cls?' '+cls:'')+'"><div class="sh"><span>'+nm+'</span>'+stc+'</div><div class="vol"><small>'+vl+'</small><b>'+vol+'</b></div><div class="lim">'+lim+'</div><div class="run"><span>Running</span><em>'+run+'</em></div></div>';}
function render(){
var sq=$('sqb');sq.className='bt '+(S.st?'done':'pri');sq.textContent=S.st?'Started':'Start quote';
$('rsc').innerHTML=!S.st?'':S.ln?'<span class="ch c-ok" id="ost">Link sent</span>':S.rs?'<span class="ch c-ok" id="ost">Reserved</span>':S.cv?'<span class="ch c-info" id="ost">Order SO-3110</span>':'<span class="ch c-idle" id="ost">Quote Q-2207</span>';
var q='<div class="ct"><span>Quote <span class="mono">Q-2207</span>'+(S.cv?', now order <span class="mono">SO-3110</span>':'')+'</span>'+(S.st?'<button type="button" class="bt '+(S.cv?'done':'pri')+'" id="cvb"'+(!S.ap&&!S.cv?' disabled':'')+'>'+(S.cv?'Converted':'Convert to order')+'</button>':'')+'</div>';
if(!S.st)q+='<div class="empt"><b>No quote yet</b><span>Start a quote for the customer above. Their price list and breaks apply in one click.</span></div>';
else{q+='<div class="row h"><span>Item</span><span>Cases</span><span>List</span><span>Price</span><span>Priced from</span><span>Line total</span></div>'+
LINES.map(function(l,i){var p=price(l),src=!S.ap?'<span class="ch c-idle">List price</span>':brk(l)?'<span class="ch c-ok" id="src'+i+'">Break, '+l.brk[0]+' or more</span>':'<span class="ch c-info" id="src'+i+'">Price list</span>';
return '<div class="row in" id="l-'+l.sku+'"><span>'+l.nm+'<small>'+l.sku+'</small></span><span>'+n0(l.q)+'</span><span>'+mc(l.list)+'</span><span id="p'+i+'">'+mc(p)+'</span><span>'+src+'</span><span id="t'+i+'">'+mc(lt(l))+'</span></div>';}).join('')+
'<div class="row sm"><span>Quote total, '+n0(cases())+' cases</span><span></span><span></span><span></span><span></span><span id="qtt">'+mc(qt())+'</span></div>';}
$('ql').innerHTML=q;
var c;
if(!S.st)c=['Quote','Sales order','Reserved','Status link'].map(function(n){return '<div class="stg e"><div class="sh"><span>'+n+'</span></div><div class="lim" style="padding-top:8px">Start a quote to follow it through this stage.</div></div>';});
else{var nr=LINES.reduce(function(a,l){return a+rsv(l);},0);
c=[stg('Quote',S.cv?'ok':'',S.cv?'<span class="ch c-ok">Converted</span>':'<span class="ch '+(S.ap?'c-info':'c-idle')+'">'+(S.ap?'Priced':'Draft')+'</span>','<span id="cq">'+mc(qt())+'</span>','Quote total',S.ap?'Price list and break applied':'At list price',n0(cases())+' cases'),
stg('Sales order',S.cv?'ok':'e',S.cv?'<span class="ch c-ok">Open</span>':'',S.cv?'<span id="co">'+mc(qt())+'</span>':'$0.00','SO-3110 total',S.cv?'Same total as the quote':'Converts from the quote',S.cv?n0(cases())+' cases':'0'),
stg('Reserved',S.rs?'ok':'e',S.rs?'<span class="ch c-ok">Done</span>':'','<span id="cr">'+n0(nr)+' of '+n0(cases())+'</span>','Cases reserved',S.rs?'Held for SO-3110 in the main warehouse':'Reserves once the order exists',n0(nr)+' cases'),
stg('Status link',S.ln?'ok':'e',S.ln?'<span class="ch c-ok">Sent</span>':'',S.ln?'Sent':'Not sent','To Greenfield Market',S.ln?'<span class="lk" id="lnk">'+LINK+'SO-3110 order status</span>':S.rs?'<button type="button" class="bt pri" id="slb">Send link</button>':'Sends once stock is reserved',S.ln?'1 link':'0')];}
$('chn').innerHTML=c.join(ARW);
var p='<div class="ct"><span>Price list, Greenfield Market</span>'+(S.st?'<button type="button" class="bt '+(S.ap?'done':'pri')+'" id="apb">'+(S.ap?'Applied':'Apply price list')+'</button>':'')+'</div>';
if(!S.st)p+='<div class="empt"><span>The customer\'s price list and quantity breaks show here.</span></div>';
else p+='<div class="pl in"><div class="row h"><span>Item</span><span>List</span><span>Customer</span><span>Break</span></div>'+LINES.map(function(l){return '<div class="row"><span>'+l.sh+'<small>'+l.sku+'</small></span><span>'+mc(l.list)+'</span><span>'+mc(l.pl)+'</span><span>'+(l.brk?mc(l.brk[1])+'<small>'+l.brk[0]+' or more</small>':'<small>No break</small>')+'</span></div>';}).join('')+'</div>';
p+='<div class="ft">Price list 2026, valid to Dec 31.</div>';
$('plc').innerHTML=p;
var k='<div class="ct"><span>Stock, main warehouse</span>'+(S.cv?'<button type="button" class="bt '+(S.rs?'done':'pri')+'" id="rsb">'+(S.rs?'Reserved':'Reserve stock')+'</button>':'')+'</div>';
if(!S.st)k+='<div class="empt"><span>Available stock for each line shows here.</span></div>';
else k+='<div class="sk in"><div class="row h"><span>Item</span><span>Ordered</span><span>Reserved</span><span>Available</span></div>'+LINES.map(function(l,i){return '<div class="row"><span>'+l.sh+'</span><span>'+n0(l.q)+'</span><span id="r'+i+'" class="'+(S.rs?'rv':'')+'">'+n0(rsv(l))+'</span><span id="a'+i+'">'+n0(l.av-rsv(l))+'</span></div>';}).join('')+'</div>';
k+='<div class="ft">Reserved stock is held for the order.</div>';
$('skc').innerHTML=k;
}
function resetState(){S={st:false,ap:false,cv:false,rs:false,ln:false};render();}
function capN(){var i=cap.querySelector('.m i');return i?+i.textContent:1;}
var CAPAT=function(hh){var w=cap.offsetWidth;return capN()>=4?{l:visW()-w-14,t:56}:{l:visW()-w-14,t:visH()-hh-14};};
var ST=[
{id:'st',target:function(){return $('sqb');},prompt:'Start a quote',where:'below',run:function(){S.st=true;render();},
 after:function(){return['A quote with two lines','Greenfield Market: '+LINES.map(function(l){return n0(l.q)+' cases of '+l.sh;}).join(' and ')+', '+mc(qt())+' at list.'];}},
{id:'ap',target:function(){return $('apb');},prompt:'Apply the price list',where:'above',run:function(){S.ap=true;render();},
 after:function(){return['Customer price list and a quantity break','Penne breaks to '+mc(LINES[0].brk[1])+' at 100 cases or more. Olive Oil is '+mc(LINES[1].pl)+'. Total '+mc(qt())+'.'];}},
{id:'cv',target:function(){return $('cvb');},prompt:'Convert to a sales order',where:'below',run:function(){S.cv=true;render();},
 after:function(){return['Quote converted to a sales order','SO-3110 for '+mc(qt())+', the same total as the quote.'];}},
{id:'rs',target:function(){return $('rsb');},prompt:'Reserve the stock',where:'above',run:function(){S.rs=true;render();},
 after:function(){return['Stock reserved against the order',LINES.map(function(l){return n0(l.q)+' '+l.sh;}).join(' and ')+' reserved. Available falls to '+LINES.map(function(l){return n0(l.av-l.q);}).join(' and ')+'.'];}},
{id:'ln',target:function(){return $('slb');},prompt:'Send the status link',where:'above',run:function(){S.ln=true;render();},
 after:function(){return['Order status link sent','Greenfield Market can follow SO-3110 from picking to delivery.'];}}];
'''
JS = 'var ARW=' + json.dumps(ARW) + ';var LINK=' + json.dumps(LINK) + ';' + JS
