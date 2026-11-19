"""Food distributors card 2: Lot Tracking & Customer Traceability. Layout: list and detail.
Left: the read only lot field with Search, the search result, and the open orders with Trace order beside SO-3110.
Right: the lot record (where it is stored, received, shipped, remaining, expiry), the Shipments tab with every customer
that received the lot, the supplier document with its preview, and the order trace back to its lots.
Received = shipped + remaining, and shipped is the sum of the customer rows."""
from frame_auto import header

SUMMARY = 'Lot Tracking & Customer Traceability (search L-24-0817, 2,000 received, 1,300 shipped to three customers, 700 left in B-12-3, open the Rossi Imports certificate, trace SO-3110 to L-24-0817 and L-24-0822, 300 cases)'
ARIA = 'Interactive product screen: search a lot number to see where it is stored and how much is left, list every shipment and customer that received it, open the supplier document and trace a customer order back to its lots'
STEPS = 5
STUDIO = dict(lede='A typical lot record on your Sutton data. Want it different? Describe the change.',
              examples=['A recall list by customer', 'Expiry alerts by bin', 'Lot photos at receiving', 'A trace report per order'],
              built_on='Lots, bins, shipments and orders', change='Columns, tabs and views')

ICON = '<circle cx="7" cy="7" r="4.2"/><path d="M10.2 10.2L13.5 13.5M5.2 7h3.6M7 5.2v3.6"/>'

CSS = (
 '.fld input[readonly]{background:#F4F4F5;color:#3F3F46;cursor:default;pointer-events:none}'
 '.g2{display:grid;grid-template-columns:216px 430px;gap:10px;padding:10px 44px 0 16px;height:550px}'
 '.lc{display:flex;flex-direction:column;gap:10px;min-width:0}'
 '.lks{flex:none;padding:9px 11px;display:flex;flex-direction:column;gap:5px}.lks .frm{display:flex;align-items:flex-end;gap:6px}.lks .fld{flex:1}.lks .ctx{font-size:8.7px;color:#71717A}'
 '.rsl{flex:none}.rsl .row{grid-template-columns:1fr auto;min-height:46px;font-size:9.4px}.rsl .l2{display:flex;flex-direction:column;gap:2px}.rsl .l2 small{font-size:8.3px;color:#71717A}.rsl .none{padding:10px 11px;font-size:9px;color:#A1A1AA}'
 '.ob{flex:1;display:flex;flex-direction:column}.ob .row{grid-template-columns:1fr auto;min-height:44px;font-size:9.3px}.ob .l2{display:flex;flex-direction:column;gap:2px}.ob .l2 small{font-size:8.3px;color:#71717A}.ob .row .bt{font-size:8.9px;padding:2px 7px}'
 '.tot{margin-top:auto;padding:9px 11px;border-top:1px solid #E4E4E7;font-size:9px;color:#52525B;line-height:1.4;background:#FAFAFA}'
 '.dt{display:flex;flex-direction:column}.dt>.empt{margin:10px;flex:1}.pane{flex:1;display:flex;flex-direction:column;min-height:0}'
 '.facts{display:grid;grid-template-columns:1.5fr 1fr 1fr 1fr;gap:8px;padding:8px 11px;border-bottom:1px solid #E4E4E7;background:#FCFCFC}.facts .kv b{font-size:10px}'
 '.qty{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;padding:10px 11px 0}.qty .kv b{font-family:"JetBrains Mono",ui-monospace,monospace;font-size:15px}'
 '.bar{margin:8px 11px 0;height:10px;border-radius:4px;background:#E4E4E7;display:flex;overflow:hidden}.bar i{display:block;height:100%}.bar .s1{background:#18181B}.bar .s2{background:#52525B}.bar .s3{background:#A1A1AA}.bar .rm{background:#BBF7D0}'
 '.bl{display:flex;gap:12px;margin:5px 11px 0;font-size:8.3px;color:#71717A}.bl span{display:inline-flex;align-items:center;gap:4px}.bl i{width:9px;height:7px;border-radius:2px;display:inline-block}'
 '.tabs{display:flex;gap:2px;padding:10px 11px 0;border-bottom:1px solid #E4E4E7}.tab{font:inherit;font-size:9.4px;font-weight:500;padding:5px 10px;border:0;border-bottom:2px solid transparent;background:none;color:#71717A;cursor:pointer}.tab.on{color:#18181B;border-bottom-color:#18181B}.tab:focus-visible{outline:2px solid #18181B;outline-offset:-2px}'
 '.tb .row{grid-template-columns:1fr 1.1fr 64px 60px;font-size:9.3px;min-height:25px}.tb .row span:nth-child(3){font-family:"JetBrains Mono",ui-monospace,monospace}.tb .row span:last-child{text-align:right;font-family:"JetBrains Mono",ui-monospace,monospace}.tb .row.h span{font-family:inherit!important}.tb .row.sm{background:#FAFAFA;font-weight:600}'
 '.wh .row{grid-template-columns:1fr 1fr 70px;font-size:9.3px;min-height:27px}.wh .row span:last-child{text-align:right;font-family:"JetBrains Mono",ui-monospace,monospace}.wh .row.h span{font-family:inherit!important}'
 '.dt>.tot{padding-right:96px}.dc{margin:10px 11px 10px;border:1px solid #E4E4E7;border-radius:8px;overflow:hidden;margin-top:auto}.dc .ct{height:28px;font-size:10px}'
 '.dr{display:flex;align-items:center;gap:9px;width:100%;padding:5px 11px;border:0;background:#fff;font:inherit;font-size:9.4px;text-align:left;cursor:pointer}.dr:hover{background:#FAFAFA}.dr.sel{background:#F4F4F5;box-shadow:inset 3px 0 0 #18181B}.dr .ic{width:22px;height:28px;border-radius:4px;background:#F4F4F5;border:1px solid #E4E4E7;display:grid;place-items:center;flex:none;font-size:7px;color:#71717A;font-weight:600}.dr .grow small{display:block;color:#71717A;font-size:8.3px}'
 '.pv{margin:10px 11px 0;border:1px solid #E4E4E7;border-radius:8px;background:#FCFCFC;padding:10px 12px;font-size:9px;line-height:1.5}.pv h4{margin:0 0 6px;font-size:10.6px;font-weight:600}.pv .gr{display:grid;grid-template-columns:96px 1fr;gap:3px 8px}.pv .gr span:nth-child(odd){color:#71717A}.pv .sg{margin-top:8px;padding-top:6px;border-top:1px dashed #E4E4E7;color:#52525B}'
 '.tr .row{grid-template-columns:76px 1fr 66px 74px 54px;font-size:9.3px;min-height:26px}.tr .row span:nth-child(1),.tr .row span:nth-child(3){font-family:"JetBrains Mono",ui-monospace,monospace}.tr .row span:last-child{text-align:right;font-family:"JetBrains Mono",ui-monospace,monospace}.tr .row.h span{font-family:inherit!important}.tr .row.hit{background:#FEF9E7}.tr .row.sm{background:#FAFAFA;font-weight:600}'
 '.act{margin:10px 11px 0;border:1px solid #E4E4E7;border-radius:8px;overflow:hidden}.act .ct{height:26px;font-size:9.8px}.act .row{grid-template-columns:44px 1fr auto;font-size:9px;min-height:23px}.act .row span:first-child{color:#71717A}.act .row span:last-child{font-family:"JetBrains Mono",ui-monospace,monospace;text-align:right}'
 '.note{margin:10px 11px 0;padding:7px 9px;border-radius:7px;font-size:9px;line-height:1.45;background:#FAFAFA;border:1px solid #F0F0F1;color:#52525B}.note.g{background:#F0FDF4;border-color:#BBF7D0;color:#166534}'
)

WIN = (
 header(ICON, 'Lot trace', 'Where every lot is, how much is left and who received it')
 + '<div class="g2"><div class="lc"><div class="cd lks"><div class="frm"><label class="fld"><small>Lot number</small>'
 '<input id="ilt" value="L-24-0817" readonly tabindex="-1" autocomplete="off" spellcheck="false"></label>'
 '<button type="button" class="bt pri" id="sch">Search</button></div><div class="ctx">Lot received from Rossi Imports in October</div></div>'
 '<div class="cd rsl" id="rs"></div><div class="cd ob" id="ob"></div></div><div class="cd dt" id="dt"></div></div>'
)

JS = r'''
var FOC='.hd>*,.lks .fld,.lks .ctx,#sch,.rsl .ct,.rsl .row,.ob .ct,.ob .row,.ob .tot,.dt>.ct,.facts,.qty,.bar,.bl,.tabs,.pane>*,.dc';
var LOT={id:'L-24-0817',item:'Penne Pasta 20 lb Case',bin:'B-12-3',wh:'Main warehouse',rec:2000,recd:'Oct 14, 2026',exp:'Mar 15, 2027',sup:'Rossi Imports',po:'PO-4398'};
var SHP=[['SH-7702','Greenfield Market',600,'Oct 28'],['SH-7715','Harbor Deli',450,'Nov 6'],['SH-7731','Corner Pantry',250,'Nov 13']];
var ORDS=[['SO-3110','Greenfield Market','Picking',1],['SO-3102','Corner Pantry','Open'],['SO-3108','Bayview Grocers','Open'],['SO-3112','Harbor Deli','Open'],['SO-3115','Maple Row Cafe','Open']];
var ACT=[['Oct 14','Received from Rossi Imports, PO-4398','+2,000'],['Oct 14','Put away to B-12-3',''],['Oct 28','Shipped to Greenfield Market, SH-7702','600'],['Nov 6','Shipped to Harbor Deli, SH-7715','450'],['Nov 13','Shipped to Corner Pantry, SH-7731','250']];
var ALC=[['SO-3110','Greenfield Market, ships Nov 20','200'],['SO-3112','Harbor Deli, ships Nov 24','120']];
var PKS=[['Nov 19','Picked from B-12-3, L-24-0817','200'],['Nov 19','Picked from B-12-4, L-24-0822','100'],['Nov 20','Ships on SH-7740 to Greenfield Market','300']];
function actl(t,a){return '<div class="act in"><div class="ct"><span>'+t+'</span></div>'+a.map(function(x){return '<div class="row"><span>'+x[0]+'</span><span>'+x[1]+'</span><span>'+x[2]+'</span></div>';}).join('')+'</div>';}
var TRC=[['L-24-0817','B-12-3','Mar 15, 2027',200],['L-24-0822','B-12-4','Apr 2, 2027',100]];
var S;
function shipped(){return SHP.reduce(function(a,s){return a+s[2];},0);}
function left(){return LOT.rec-shipped();}
function tq(){return TRC.reduce(function(a,t){return a+t[3];},0);}
function render(){
var sb=$('sch');sb.className='bt '+(S.sr?'done':'pri');sb.textContent=S.sr?'Found':'Search';
var r='<div class="ct"><span>Results</span>'+(S.sr?'<span class="ch c-idle">1 lot</span>':'')+'</div>';
r+=S.sr?'<button type="button" class="row in'+(S.op&&S.view!=='trace'?' sel':'')+'" id="r-'+LOT.id+'"><span class="l2"><b class="mono">'+LOT.id+'</b><small>'+LOT.item+'</small></span><span class="ch c-ok">In stock</span></button>':'<div class="none">Search a lot number to find it.</div>';
$('rs').innerHTML=r;
var o='<div class="ct"><span>Open orders, Penne Pasta</span><span class="ch c-idle">'+ORDS.length+'</span></div>'+ORDS.map(function(x){return '<div class="row'+(S.view==='trace'&&x[3]?' sel':'')+'"><span class="l2"><b class="mono">'+x[0]+'</b><small>'+x[1]+', '+x[2].toLowerCase()+'</small></span>'+(x[3]?'<button type="button" class="bt'+(S.view==='trace'?' done':'')+'" id="trb">'+(S.view==='trace'?'Traced':'Trace order')+'</button>':'<span class="ch c-idle">'+x[2]+'</span>')+'</div>';}).join('')+'<div class="tot">Every order line keeps the lots it shipped from.</div>';
$('ob').innerHTML=o;
var d;
if(S.view==='trace'){d='<div class="ct"><span>Trace, order <span class="mono">SO-3110</span></span><span class="ch c-ok" id="tch">'+TRC.length+' lots</span></div><div class="facts in"><div class="kv"><small>Customer</small><b>Greenfield Market</b></div><div class="kv"><small>Item</small><b>Penne 20 lb</b></div><div class="kv"><small>Ships</small><b>Nov 20</b></div><div class="kv"><small>Status</small><b>Picking</b></div></div>'+
'<div class="pane"><div class="tr in" id="trc"><div class="row h"><span>Lot</span><span>Item</span><span>Bin</span><span>Expiry</span><span>Cases</span></div>'+TRC.map(function(t,i){return '<div class="row'+(i===0?' hit':'')+'" id="t-'+t[0]+'"><span>'+t[0]+'</span><span>Penne Pasta 20 lb Case</span><span>'+t[1]+'</span><span>'+t[2]+'</span><span>'+n0(t[3])+'</span></div>';}).join('')+'<div class="row sm"><span>Total</span><span></span><span></span><span></span><span id="ttq">'+n0(tq())+'</span></div></div>'+
'<div class="note g in">SO-3110 traces back to '+TRC.length+' lots, '+n0(tq())+' cases. '+LOT.id+' is the lot searched above.</div>'+actl('Picks and shipment, SO-3110',PKS)+
'<div class="dc"><div class="ct"><span>Supplier documents on these lots</span></div><div class="dr"><span class="ic">PDF</span><span class="grow">Certificates of analysis, '+LOT.id+' and L-24-0822<small>'+LOT.sup+', 2 files</small></span><span class="ch c-idle">2</span></div></div></div>';}
else if(!S.op){d='<div class="ct"><span>Lot record</span></div><div class="empt"><b>No lot open</b><span>Search a lot number to see where it is stored, how much is left and every customer that received it.</span></div>';}
else{d='<div class="ct"><span>Lot <span class="mono">'+LOT.id+'</span></span><span class="ch c-ok">'+n0(left())+' left</span></div>'+
'<div class="facts in"><div class="kv"><small>Item</small><b>'+LOT.item+'</b></div><div class="kv"><small>Stored in</small><b id="fbin">'+LOT.bin+'</b></div><div class="kv"><small>Received</small><b>'+LOT.recd.replace(', 2026','')+'</b></div><div class="kv"><small>Expiry</small><b id="fexp">'+LOT.exp+'</b></div></div>'+
'<div class="qty in"><div class="kv"><small>Received, cases</small><b id="qrc">'+n0(LOT.rec)+'</b></div><div class="kv"><small>Shipped</small><b id="qsh">'+n0(shipped())+'</b></div><div class="kv"><small>Remaining</small><b id="qrm">'+n0(left())+'</b></div></div>'+
'<div class="bar in">'+SHP.map(function(s,i){return '<i class="s'+(i+1)+'" style="width:'+(s[2]/LOT.rec*100)+'%"></i>';}).join('')+'<i class="rm" style="width:'+(left()/LOT.rec*100)+'%"></i></div><div class="bl"><span><i style="background:#18181B"></i>Shipped</span><span><i style="background:#BBF7D0"></i>Remaining in '+LOT.bin+'</span></div>'+
'<div class="tabs" role="tablist"><button type="button" class="tab'+(S.view==='stock'?' on':'')+'" id="t-stk" role="tab" aria-selected="'+(S.view==='stock')+'">Stock</button><button type="button" class="tab'+(S.view!=='stock'?' on':'')+'" id="t-shp" role="tab" aria-selected="'+(S.view!=='stock')+'">Shipments</button></div><div class="pane">';
if(S.view==='doc')d+='<div class="pv in" id="pvw"><h4>Certificate of analysis</h4><div class="gr"><span>Supplier</span><span>'+LOT.sup+'</span><span>Lot</span><span class="mono">'+LOT.id+'</span><span>Product</span><span>'+LOT.item+'</span><span>Quantity</span><span>'+n0(LOT.rec)+' cases</span><span>Best before</span><span>'+LOT.exp+'</span><span>Moisture</span><span>Within spec</span></div><div class="sg">Attached at receiving on '+LOT.recd+' against '+LOT.po+'.</div></div>';
else if(S.view==='shp')d+='<div class="tb in" id="shp"><div class="row h"><span>Customer</span><span>Shipment</span><span>Date</span><span>Cases</span></div>'+SHP.map(function(s){return '<div class="row"><span>'+s[1]+'</span><span class="mono">'+s[0]+'</span><span>'+s[3]+'</span><span>'+n0(s[2])+'</span></div>';}).join('')+'<div class="row sm"><span>Total shipped</span><span>3 customers</span><span></span><span id="tsh">'+n0(shipped())+'</span></div></div>'+actl('Allocated to open orders',ALC.concat([['','Free to allocate in B-12-3',n0(left()-320)]]));
else d+='<div class="wh in"><div class="row h"><span>Warehouse</span><span>Bin</span><span>Cases</span></div><div class="row"><span>'+LOT.wh+'</span><span class="mono">'+LOT.bin+'</span><span id="wbq">'+n0(left())+'</span></div></div><div class="note">Received on '+LOT.recd+' against '+LOT.po+'. FEFO picks this lot before L-24-0822.</div>'+actl('Lot activity',ACT);
d+='<div class="dc"><div class="ct"><span>Supplier documents</span><span class="ch c-idle">1</span></div><button type="button" class="dr'+(S.view==='doc'?' sel':'')+'" id="dcr"><span class="ic">PDF</span><span class="grow">Certificate of analysis, '+LOT.id+'<small>'+LOT.sup+', attached '+LOT.recd.replace(', 2026','')+'</small></span><span class="ch '+(S.view==='doc'?'c-info':'c-idle')+'">'+(S.view==='doc'?'Open':'View')+'</span></button></div></div>';}
d+='<div class="tot">Lot records kept from receipt to the last shipment.</div>';
$('dt').innerHTML=d;
}
function resetState(){S={sr:false,op:false,view:'stock'};render();}
winEl.addEventListener('click',function(e){var t=e.target.closest&&e.target.closest('#t-stk,#t-shp');if(t&&S.op&&S.view!=='trace'&&mode==='try'&&cur!==2){S.view=t.id==='t-stk'?'stock':'shp';render();}});
var CAPAT=function(hh){return {l:14,t:visH()-hh-14};};
var ST=[
{id:'sr',target:function(){return $('sch');},prompt:'Search L-24-0817',where:'below',run:function(){S.sr=true;render();},
 after:function(){return['The lot, found by its number',LOT.id+', '+LOT.item+', received from '+LOT.sup+'.'];}},
{id:'op',target:function(){return $('r-'+LOT.id);},prompt:'Open the lot',where:'below',run:function(){S.sr=true;S.op=true;S.view='stock';render();},
 after:function(){return['Where it is stored, how much is left',n0(left())+' of '+n0(LOT.rec)+' cases left in bin '+LOT.bin+', best before '+LOT.exp+'.'];}},
{id:'shp',target:function(){return $('t-shp');},prompt:'Open the Shipments tab',where:'below',run:function(){S.view='shp';render();},
 after:function(){return['Every customer that received the lot',SHP.map(function(s){return s[1]+' '+n0(s[2]);}).join(', ')+': '+n0(shipped())+' shipped, '+n0(left())+' left.'];}},
{id:'doc',target:function(){return $('dcr');},prompt:'Open the supplier document',where:'above',run:function(){S.view='doc';render();},
 after:function(){return['The supplier document on the lot','Certificate of analysis from '+LOT.sup+', attached when the lot was received.'];}},
{id:'tr',target:function(){return $('trb');},prompt:'Trace order SO-3110',where:'above',run:function(){S.view='trace';render();},
 after:function(){return['From a customer order back to its lots','SO-3110 shipped from '+TRC.map(function(t){return t[0]+' ('+n0(t[3])+')';}).join(' and ')+', '+n0(tq())+' cases.'];}}];
'''
