"""Food distributors card 1: Stock Available to Sell. Layout: a record form with a side summary panel.
Left: the read only item field with Look up, the stock position by bin for the chosen warehouse (Main warehouse or
Cold room), the warehouse total row that turns red when available falls under the reorder point, and the purchase
orders list. Right: the available to sell summary (in stock + expected minus committed), the preset 300 case order with
Place order, the shortage and Create PO. Available is computed per row from the data below, never typed in."""
from frame_auto import header

SUMMARY = 'Stock Available to Sell (look up Penne Pasta 20 lb Case, 1,200 + 600 minus 900 = 900 available in the main warehouse, switch to the cold room, a 300 case order drops available to 600, under the 800 reorder point, PO for 1,000 cases from Rossi Imports)'
ARIA = 'Interactive product screen: look up an item to see in stock, expected, committed and available by warehouse and bin, place an order and watch available drop, see the shortage flagged against the reorder point and raise a supplier purchase order'
STEPS = 5
STUDIO = dict(lede='A typical stock position screen on your Sutton data. Want it different? Describe the change.',
              examples=['Reorder points by season', 'Available to sell by customer', 'A daily shortage email', 'Expected stock by due date'],
              built_on='Items, bins, orders and purchase orders', change='Columns, rules and views')

ICON = '<path d="M2.5 5L8 2.5 13.5 5v6L8 13.5 2.5 11z"/><path d="M2.5 5L8 7.5 13.5 5M8 7.5v6"/>'

CSS = (
 '.fld input[readonly]{background:#F4F4F5;color:#3F3F46;cursor:default;pointer-events:none}'
 '.g1{display:grid;grid-template-columns:420px 226px;grid-template-rows:62px 468px;gap:10px;padding:10px 44px 0 16px}'
 '.bf{display:flex;flex-direction:column;justify-content:center;gap:5px;padding:0 12px}.bf .frm{display:flex;align-items:flex-end;gap:8px}.bf .fld{width:190px}.bf .ctx{font-size:8.9px;color:#71717A}.bf .frm .rt{margin-left:auto}'
 '.fm{display:flex;flex-direction:column}.fm>.empt{margin:10px;flex:1}.sm{grid-column:2;grid-row:1/3;display:flex;flex-direction:column}.sm>.empt{margin:10px;flex:1}'
 '.seg{display:inline-flex;padding:2px;gap:2px;border:1px solid #E4E4E7;border-radius:7px;background:#FAFAFA}.seg button{font:inherit;font-size:9px;font-weight:500;padding:2px 8px;border:0;border-radius:5px;background:transparent;color:#52525B;cursor:pointer}.seg button.on{background:#18181B;color:#fff}.seg button:focus-visible{outline:2px solid #18181B;outline-offset:1px}'
 '.bn .row{grid-template-columns:1fr 60px 60px 66px 64px;font-size:9.3px;min-height:29px}.bn .row>span:nth-child(n+2){text-align:right;font-family:"JetBrains Mono",ui-monospace,monospace}.bn .row.h>span{font-family:inherit!important}'
 '.bn .row small{display:block;font-size:8.2px;color:#71717A}.bn .row.cm span.ch2{color:#B45309;font-weight:600}'
 '.bn .row.tr{background:#FAFAFA;font-weight:600;border-top:1px solid #E4E4E7;transition:background-color .35s,box-shadow .35s}.bn button.row.tr{width:100%;text-align:left;font:inherit;font-weight:600;border-left:0;border-right:0;border-bottom:0;cursor:pointer}'
 '.bn .row.tr.bad{background:#FEF2F2;color:#991B1B;box-shadow:inset 3px 0 0 #DC2626}.bn .row.tr.sel.bad{background:#FEE2E2}'
 '.sub{display:flex;align-items:center;justify-content:space-between;padding:7px 11px;font-size:9.4px;font-weight:600;border-top:1px solid #E4E4E7}'
 '.pol .row{grid-template-columns:62px 1fr 64px 56px;font-size:9.2px;min-height:28px}.pol .row span:nth-child(3){text-align:right;font-family:"JetBrains Mono",ui-monospace,monospace}.pol .row span:last-child{text-align:right}.pol .none{padding:9px 11px;font-size:9px;color:#A1A1AA}'
 '.ol .row{grid-template-columns:62px 1fr 64px 60px;font-size:9.2px;min-height:26px}.ol .row span:nth-child(3){text-align:right;font-family:"JetBrains Mono",ui-monospace,monospace}.ol .row span:last-child{text-align:right}.ol .row.nw{background:#FFFBEB}'
 '.br{margin:10px 11px 0}.br small{display:block;font-size:8.4px;color:#71717A;margin-bottom:5px}.br .tk{position:relative;height:12px;border-radius:4px;background:#F4F4F5;overflow:visible}.br .fl{position:absolute;left:0;top:0;bottom:0;border-radius:4px;background:#16A34A;transition:width .5s cubic-bezier(.22,.9,.28,1),background-color .35s}.br .fl.bad{background:#DC2626}.br .mk{position:absolute;top:-3px;bottom:-3px;width:2px;background:#18181B}.br .lb{display:flex;justify-content:space-between;font-size:8.2px;color:#71717A;margin-top:4px;font-family:"JetBrains Mono",ui-monospace,monospace}'
 '.nr{margin:9px 11px 0;padding:6px 8px;border-radius:7px;background:#FAFAFA;border:1px solid #F0F0F1;font-size:8.8px;line-height:1.45;color:#52525B}.nr b{color:#18181B}'
 '.tot{margin-top:auto;padding:9px 11px;border-top:1px solid #E4E4E7;font-size:9.1px;color:#52525B;line-height:1.4;background:#FAFAFA}.sm .tot{padding-right:90px}'
 '.sm .bx{padding:10px 11px 0}.sm .big{font-size:24px}.pair{display:grid;grid-template-columns:1fr 1fr 1fr;gap:6px;padding:9px 11px 0}.pair .kv b{font-size:11px;font-family:"JetBrains Mono",ui-monospace,monospace}'
 '.calc{margin:9px 11px 0;padding:6px 8px;border-radius:6px;background:#FAFAFA;border:1px solid #F0F0F1;font-family:"JetBrains Mono",ui-monospace,monospace;font-size:9.2px;text-align:center}'
 '.rop{display:flex;justify-content:space-between;align-items:center;margin:9px 11px 0;font-size:9.2px;color:#52525B}.rop b{font-family:"JetBrains Mono",ui-monospace,monospace;color:#18181B}'
 '.od{margin:9px 11px 0;padding:7px 8px;border:1px solid #E4E4E7;border-radius:7px;font-size:9px;line-height:1.45}.od small{display:block;color:#71717A;font-size:8.4px}.od b{font-family:"JetBrains Mono",ui-monospace,monospace}'
 '.note{margin:9px 11px 0;padding:7px 9px;border-radius:7px;font-size:9px;line-height:1.45;background:#FAFAFA;border:1px solid #F0F0F1;color:#52525B}.note.w{background:#FEF2F2;border-color:#FECACA;color:#991B1B}.note.g{background:#F0FDF4;border-color:#BBF7D0;color:#166534}'
 '.sm .acts{padding:8px 11px 0}.sm .acts .bt{width:100%;font-size:9.6px;padding:5px 10px}.sm .acts .bt:disabled{opacity:.45;cursor:not-allowed}'
)

WIN = (
 header(ICON, 'Stock position', 'Available to sell by warehouse and bin')
 + '<div class="g1"><div class="cd bf"><div class="frm"><label class="fld"><small>Item</small>'
 '<input id="iit" value="Penne Pasta 20 lb Case" readonly tabindex="-1" autocomplete="off" spellcheck="false"></label>'
 '<button type="button" class="bt pri" id="lkb">Look up</button><span class="rt" id="rst"></span></div><div class="ctx">Item PP-20, sold by the case from both warehouses</div></div>'
 '<div class="cd fm" id="fm"></div><div class="cd sm" id="sm"></div></div>'
)

JS = r'''
var FOC='.hd>*,.bf .fld,.bf .ctx,#lkb,.fm>.ct,.bn .row,.fm .sub,.pol,.fm .tot,.sm>*';
var MI=String.fromCharCode(8722);
var WH={main:{nm:'Main warehouse',bins:[['B-12-3','Aisle B, rack 12',700,0,500,200],['B-14-1','Aisle B, rack 14',500,0,400,100],['DK-2','Inbound, dock 2',0,600,0,0]]},
cold:{nm:'Cold room',bins:[['C-01-2','Cold room, rack 1',250,0,60,0],['C-03-1','Cold room, rack 3',150,0,40,0]]}};
var OPEN={main:[['SO-3110','Greenfield Market',300,'Nov 20'],['SO-3102','Corner Pantry',250,'Nov 21'],['SO-3108','Bayview Grocers',350,'Nov 24']],cold:[['SO-3101','Harbor Deli',100,'Nov 20']]};
var ORD={id:'SO-3124',cust:'Harbor Deli',q:300},ROP=800,PO={id:'PO-4471',ven:'Rossi Imports',q:1000,due:'Dec 2'};
var S;
function bins(w){return WH[w].bins.map(function(b){var c=b[4]+(w==='main'&&S.ord?b[5]:0);return {id:b[0],loc:b[1],ins:b[2],exp:b[3],com:c,add:w==='main'&&S.ord?b[5]:0,av:b[2]+b[3]-c};});}
function tot(w){return bins(w).reduce(function(a,b){a.ins+=b.ins;a.exp+=b.exp;a.com+=b.com;a.av+=b.av;return a;},{ins:0,exp:0,com:0,av:0});}
function short(w){return w==='main'&&tot('main').av<ROP;}
function render(){
var T=tot(S.wh),M=tot('main');
$('lkb').className='bt '+(S.lk?'done':'pri');$('lkb').textContent=S.lk?'Found':'Look up';
$('rst').innerHTML=!S.lk?'':short('main')?'<span class="ch c-bad" id="fst">Below reorder point</span>':'<span class="ch c-ok" id="fst">In stock</span>';
var f='<div class="ct"><span>Stock by bin</span>'+(S.lk?'<span class="seg" role="group" aria-label="Warehouse"><button type="button" id="w-main" class="'+(S.wh==='main'?'on':'')+'" aria-pressed="'+(S.wh==='main')+'">Main warehouse</button><button type="button" id="w-cold" class="'+(S.wh==='cold'?'on':'')+'" aria-pressed="'+(S.wh==='cold')+'">Cold room</button></span>':'')+'</div>';
if(!S.lk)f+='<div class="empt"><b>No item open</b><span>Look up an item to see its stock position in every warehouse and bin.</span></div>';
else{f+='<div class="bn in" id="bn"><div class="row h"><span>Bin</span><span>In stock</span><span>Expected</span><span>Committed</span><span>Available</span></div>'+
bins(S.wh).map(function(b){return '<div class="row'+(b.add?' cm':'')+'" id="r-'+b.id+'"><span><b class="mono">'+b.id+'</b><small>'+b.loc+'</small></span><span>'+n0(b.ins)+'</span><span>'+n0(b.exp)+'</span><span'+(b.add?' class="ch2"':'')+'>'+n0(b.com)+'</span><span>'+n0(b.av)+'</span></div>';}).join('')+
'<button type="button" class="row tr'+(short(S.wh)?' bad':'')+(S.sh&&S.wh==='main'?' sel':'')+'" id="trw"><span>'+WH[S.wh].nm+' total</span><span id="t-ins">'+n0(T.ins)+'</span><span id="t-exp">'+n0(T.exp)+'</span><span id="t-com">'+n0(T.com)+'</span><span id="t-av">'+n0(T.av)+'</span></button></div>';
var ol=OPEN[S.wh].slice();if(S.wh==='main'&&S.ord)ol.push([ORD.id,ORD.cust,ORD.q,'Nov 25',1]);
f+='<div class="sub"><span>Orders committing stock, '+(S.wh==='main'?'main warehouse':'cold room')+'</span><span class="ch c-idle" id="olc">'+n0(ol.reduce(function(a,o){return a+o[2];},0))+' cases</span></div><div class="ol">'+ol.map(function(o){return '<div class="row'+(o[4]?' nw in':'')+'"><span class="mono"><b>'+o[0]+'</b></span><span>'+o[1]+', ships '+o[3]+'</span><span>'+n0(o[2])+'</span><span><span class="ch '+(o[4]?'c-warn':'c-idle')+'">'+(o[4]?'New':'Open')+'</span></span></div>';}).join('')+'</div>';
f+='<div class="sub"><span>Purchase orders, Penne Pasta 20 lb Case</span><span class="ch c-idle">'+(S.po?'1 draft':'None open')+'</span></div><div class="pol">'+(S.po?'<div class="row h"><span>PO</span><span>Vendor</span><span>Cases</span><span>Status</span></div><div class="row in" id="por"><span class="mono"><b>'+PO.id+'</b></span><span>'+PO.ven+', due '+PO.due+'</span><span id="poq">'+n0(PO.q)+'</span><span><span class="ch c-info">Draft</span></span></div>':'<div class="none">No open purchase orders for this item.</div>')+'</div>';}
f+='<div class="tot">Available is in stock plus expected, minus committed, for every bin.</div>';
$('fm').innerHTML=f;
var m='<div class="ct"><span>Available to sell</span>'+(S.lk?'<span class="ch c-idle">'+(S.wh==='main'?'Main':'Cold room')+'</span>':'')+'</div>';
if(!S.lk)m+='<div class="empt"><b>Nothing to show</b><span>Available to sell and the reorder point show here.</span></div>';
else{m+='<div class="bx in"><div class="kv"><small>'+WH[S.wh].nm+', cases</small><b class="big mono" id="sav">'+n0(T.av)+'</b></div></div>'+
'<div class="pair in"><div class="kv"><small>In stock</small><b id="sin">'+n0(T.ins)+'</b></div><div class="kv"><small>Expected</small><b id="sex">'+n0(T.exp)+'</b></div><div class="kv"><small>Committed</small><b id="scm">'+n0(T.com)+'</b></div></div>'+
'<div class="calc" id="scal">'+n0(T.ins)+' + '+n0(T.exp)+' '+MI+' '+n0(T.com)+' = '+n0(T.av)+'</div>';
if(S.wh==='main')m+='<div class="br in"><small>Available against the reorder point</small><div class="tk"><div class="fl'+(T.av<ROP?' bad':'')+'" style="width:'+(T.av/1200*100).toFixed(1)+'%"></div><div class="mk" style="left:'+(ROP/1200*100).toFixed(1)+'%"></div></div><div class="lb"><span>0</span><span>'+n0(ROP)+'</span><span>1,200</span></div></div><div class="nr">Next receipt: <b>600</b> cases into DK-2 on PO-4398, due Nov 21.</div>';
if(S.wh==='main')m+='<div class="rop"><span>Reorder point</span><b id="srp">'+n0(ROP)+'</b></div>';
if(!S.ord)m+='<div class="od in"><small>Next order to place</small>'+ORD.id+', '+ORD.cust+', <b>'+n0(ORD.q)+'</b> cases from the main warehouse</div><div class="acts"><button type="button" class="bt pri" id="pob">Place order</button></div>';
else m+='<div class="od in"><small>Order placed</small>'+ORD.id+', '+ORD.cust+', <b>'+n0(ORD.q)+'</b> cases committed</div>';
if(S.ord&&!S.sh)m+='<div class="note w in">'+n0(M.av)+' available is under the reorder point of '+n0(ROP)+'.</div>';
if(S.sh)m+='<div class="note w in" id="snt">Short by <b>'+n0(ROP-M.av)+'</b> against the reorder point. Usual vendor: '+PO.ven+', '+n0(PO.q)+' case pallet lot.</div>'+(S.po?'<div class="note g in" id="pnt">'+PO.id+' raised for '+n0(PO.q)+' cases from '+PO.ven+'.</div>':'<div class="acts"><button type="button" class="bt pri" id="cpo">Create PO, '+n0(PO.q)+' cases</button></div>');}
m+='<div class="tot">Every warehouse on the same live numbers.</div>';
$('sm').innerHTML=m;
}
function resetState(){S={lk:false,wh:'main',ord:false,sh:false,po:false};render();}
winEl.addEventListener('click',function(e){var t=e.target.closest&&e.target.closest('#w-main,#w-cold');if(t&&S.lk&&mode==='try'&&cur!==1){S.wh=t.id==='w-cold'?'cold':'main';render();}});
var CAPAT=function(hh){return {l:14,t:visH()-hh-14};};
var ST=[
{id:'lk',target:function(){return $('lkb');},prompt:'Look up Penne 20 lb',where:'below',run:function(){S.lk=true;S.wh='main';render();},
 after:function(){var T=tot('main');return['One item, its whole stock position','Main warehouse: '+n0(T.ins)+' in stock, '+n0(T.exp)+' expected, '+n0(T.com)+' committed, '+n0(T.av)+' available.'];}},
{id:'wh',target:function(){return $('w-cold');},prompt:'Switch to the Cold room',where:'below',run:function(){S.wh='cold';render();},
 after:function(){var T=tot('cold');return['Each warehouse and bin','Cold room: '+n0(T.ins)+' in stock, '+n0(T.com)+' committed, '+n0(T.av)+' available across 2 bins.'];}},
{id:'ord',target:function(){return $('pob');},prompt:'Place the 300 case order',where:'above',run:function(){S.ord=true;S.wh='main';render();},
 after:function(){return['Available drops with the order',ORD.id+' commits '+n0(ORD.q)+' cases: committed 900 to '+n0(tot('main').com)+', available 900 to '+n0(tot('main').av)+'.'];}},
{id:'sh',target:function(){return $('trw');},prompt:'Open the flagged total',where:'above',run:function(){S.wh='main';S.sh=true;render();},
 after:function(){return['A shortage, flagged on the item',n0(tot('main').av)+' available is '+n0(ROP-tot('main').av)+' under the reorder point of '+n0(ROP)+'.'];}},
{id:'po',target:function(){return $('cpo');},prompt:'Create the purchase order',where:'above',run:function(){S.po=true;render();},
 after:function(){return['A purchase order from the shortage',PO.id+' to '+PO.ven+' for '+n0(PO.q)+' cases, as a draft.'];}}];
'''
