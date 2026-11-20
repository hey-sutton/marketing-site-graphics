"""Nut processing card 3: Bulk Bins & Lot Genealogy. Layout: list and detail (left list, right record panel).
Top: the read only bin field with Open bin. Left: bins and packs with their lots and weights, and the weight held in
the room (it stays 7,000 lb through the blend and the split). Right: the record of the selected bin or pack: the lots
it holds, the blend with its percentages, the split into retail and bulk, the trace back to the raw deliveries and the
customers who received the packed lot."""
from frame_auto import header

SUMMARY = 'Bulk Bins & Lot Genealogy (bin B-101 holds 4,000 lb of lot L-A, blend with B-102 3,000 lb of L-B into B-200, 7,000 lb at 57.1% and 42.9%, split into 1,000 retail 5 lb packs and 2,000 lb bulk, trace PK-5120 to NP-0711 and NP-0709, 3 customers)'
ARIA = 'Interactive product screen: open a bulk bin and see the lots it holds, blend two bins into a new lot, split a bin into retail and bulk packs, trace a packed lot to its raw deliveries and list the customers who received it'
STEPS = 5
STUDIO = dict(lede='A typical bin and lot screen on your Sutton data. Want it different? Describe the change.',
              examples=['Blend limits by grade', 'Tote labels with the lot', 'A recall list in one click', 'Bin weights from the scale'],
              built_on='Lots, bins, BOMs and shipments', change='Fields, rules and views')

ICON = '<path d="M3 3.5h10v3H3zM4 6.5v6h8v-6"/><path d="M6.5 9h3"/>'

CSS = (
 '.fld input[readonly]{background:#F4F4F5;color:#3F3F46;cursor:default;pointer-events:none}'
 '.g3{display:grid;grid-template-columns:222px 424px;grid-template-rows:60px 470px;gap:10px;padding:10px 44px 0 16px;width:716px}'
 '.top{grid-column:1/3;display:flex;flex-direction:column;justify-content:center;gap:5px;padding:0 12px}.top .frm{display:flex;align-items:flex-end;gap:8px}.top .fld{width:120px}.top .ctx{font-size:8.9px;color:#71717A}.top .rs{margin-left:auto}'
 '.ls,.dt{display:flex;flex-direction:column}.ls>.empt,.dt>.empt{margin:9px;flex:1;padding:10px}'
 '.ls .row{grid-template-columns:1fr auto;min-height:44px;font-size:9.2px;transition:background-color .35s,opacity .35s}.ls .row b{font-family:"JetBrains Mono",ui-monospace,monospace;font-size:9.8px}.ls .row small{display:block;font-size:8.3px;color:#71717A;margin-top:1px}'
 '.ls .row .w{text-align:right;font-family:"JetBrains Mono",ui-monospace,monospace;font-size:9.4px}.ls .row .w small{font-family:inherit}.ls .row.gone{opacity:.55}.ls .row.sel{background:#F4F4F5;box-shadow:inset 3px 0 0 #18181B}'
 '.rm{margin:9px 9px 0;border:1px solid #E4E4E7;border-radius:8px;padding:7px 9px;display:flex;flex-direction:column;gap:4px;font-size:9px;color:#52525B}.rm b{font-family:"JetBrains Mono",ui-monospace,monospace;color:#18181B}.rm div{display:flex;justify-content:space-between}.rm .t{border-top:1px solid #F0F0F1;padding-top:4px;font-weight:600;color:#18181B}'
 '.ls .tot,.dt .tot{margin-top:9px;padding:8px 11px;border-top:1px solid #E4E4E7;font-size:9px;color:#52525B;line-height:1.4;background:#FAFAFA}.dt .tot{margin-top:auto;padding-right:90px}'
 '.dh{padding:9px 11px 0;display:flex;justify-content:space-between;align-items:flex-start}.dh .kv b{font-size:15px;font-family:"JetBrains Mono",ui-monospace,monospace}.dh .r2{display:flex;gap:5px}'
 '.kg{display:grid;grid-template-columns:1fr 1fr 1fr;gap:6px 10px;padding:8px 11px 0}'
 '.sec{padding:9px 11px 0}.sec h4{margin:0 0 5px;font-size:9.6px;font-weight:600;display:flex;justify-content:space-between;align-items:center}'
 '.lt .row{grid-template-columns:52px 1fr 60px 50px;font-size:9.2px;min-height:28px;padding:0 6px}.lt .row>span:nth-child(3),.lt .row>span:nth-child(4){text-align:right;font-family:"JetBrains Mono",ui-monospace,monospace}.lt .row.h>span{font-family:inherit!important}.lt .row small{display:block;font-size:8.2px;color:#71717A}.lt .row.sm{background:#FAFAFA;font-weight:600}'
 '.lt{border:1px solid #E4E4E7;border-radius:8px;overflow:hidden}'
 '.mix{display:flex;height:16px;border-radius:5px;overflow:hidden;margin-top:7px}.mix i{display:grid;place-items:center;font-style:normal;font-size:8.4px;color:#fff;font-family:"JetBrains Mono",ui-monospace,monospace}.mix .a{background:#18181B}.mix .b{background:#71717A}'
 '.act{margin:10px 11px 0;padding:8px 9px;border:1px solid #E4E4E7;border-radius:8px;background:#FAFAFA;display:flex;align-items:center;gap:8px;font-size:9px;color:#52525B}.act .rt{margin-left:auto}.act .chs{display:flex;gap:5px;flex-wrap:wrap}.act .chs span{border:1px solid #D4D4D8;background:#fff;border-radius:6px;padding:2px 7px;font-size:8.8px;color:#18181B}'
 '.calc{margin-top:6px;padding:5px 8px;border-radius:6px;background:#FAFAFA;border:1px solid #F0F0F1;font-family:"JetBrains Mono",ui-monospace,monospace;font-size:9.2px;text-align:center}'
 '.tr{padding:4px 11px 0;display:flex;flex-direction:column;gap:5px}.tn{display:flex;align-items:center;gap:7px;font-size:9px}.tn .bx{border:1px solid #E4E4E7;border-radius:7px;padding:4px 8px;background:#fff;min-width:0}.tn .bx b{font-family:"JetBrains Mono",ui-monospace,monospace;font-size:9.4px}.tn .bx small{display:block;font-size:8.2px;color:#71717A}'
 '.tn .bx.rw{border-color:#BBF7D0;background:#F0FDF4}.tn .ln{color:#A1A1AA;font-family:"JetBrains Mono",ui-monospace,monospace;font-size:9px;white-space:pre}'
 '.tl{display:grid;grid-template-columns:1fr 1fr 1fr;gap:6px;padding:9px 11px 0}.tl div{border:1px solid #E4E4E7;border-radius:7px;padding:5px 8px}.tl small{display:block;font-size:8.2px;color:#71717A}.tl b{font-size:10px;font-weight:600}.tl h4{grid-column:1/4;margin:0;font-size:9.6px;font-weight:600}'
 '.dl .row{grid-template-columns:58px 1fr 48px 50px 62px;font-size:9px;min-height:26px;padding:0 6px}.dl .row>span:nth-child(n+3){text-align:right;font-family:"JetBrains Mono",ui-monospace,monospace}.dl .row.h>span{font-family:inherit!important}.dl{border:1px solid #E4E4E7;border-radius:8px;overflow:hidden}'
 '.lg{margin:9px 9px 0;display:flex;flex-direction:column;gap:3px}.lg b{font-size:9.2px;font-weight:600;margin-bottom:2px}.lg div{display:grid;grid-template-columns:38px 1fr;gap:6px;font-size:8.6px;color:#52525B;line-height:1.3}.lg div span:first-child{color:#71717A;font-family:"JetBrains Mono",ui-monospace,monospace}'
 '.cu .row{grid-template-columns:1fr 54px 52px 58px;font-size:9.2px;min-height:26px;padding:0 6px}.cu .row>span:nth-child(n+3){text-align:right;font-family:"JetBrains Mono",ui-monospace,monospace}.cu .row.h>span{font-family:inherit!important}.cu .row.sm{background:#FAFAFA;font-weight:600}.cu{border:1px solid #E4E4E7;border-radius:8px;overflow:hidden}'
)

WIN = (
 header(ICON, 'Bins and lots', 'Blends, splits and traces by lot')
 + '<div class="g3"><div class="cd top"><div class="frm"><label class="fld"><small>Bulk bin</small>'
 '<input id="ibn" value="B-101" readonly tabindex="-1" autocomplete="off" spellcheck="false"></label>'
 '<button type="button" class="bt pri" id="obb">Open bin</button><span class="rs" id="rs"></span></div><div class="ctx">Blanched almonds, bulk bin in room 2</div></div>'
 '<div class="cd ls" id="ls"></div><div class="cd dt" id="dt"></div></div>'
)

JS = r'''
var FOC='.hd>*,.top .fld,.top .ctx,#obb,.ls .ct,.ls .row,.ls .rm,.ls .lg,.ls .tot,.dt .ct,.dt>*:not(.ct),.dt .act>*';
var BINS={'B-101':{lot:'L-A',lb:4000,dl:'NP-0711',gr:'Harlan Orchards'},'B-102':{lot:'L-B',lb:3000,dl:'NP-0709',gr:'Delmar Ranch'}};
var BL={id:'B-200',lot:'L-C'},RP={id:'PK-5120',n:1000,each:5},BK={id:'BK-2210',lb:2000};
var CUS=[['Pinecrest Snack Co.','SO-6610',400],['Morning Trail Granola','SO-6618',350],['Sunbank Grocers','SO-6623',250]];
var S;
function blendLb(){return BINS['B-101'].lb+BINS['B-102'].lb;}
function share(k){return BINS[k].lb/blendLb()*100;}
function retailLb(){return RP.n*RP.each;}
function traceDl(){return ['B-101','B-102'].map(function(k){return BINS[k].dl;});}
function items(){var a=[];
['B-101','B-102'].forEach(function(k){a.push({id:k,sub:'Lot '+BINS[k].lot+', from '+BINS[k].dl,lb:S.bl?0:BINS[k].lb,gone:S.bl,st:S.bl?'Emptied':'In bin'});});
if(S.bl)a.push({id:BL.id,sub:'Lot '+BL.lot+', blend of L-A and L-B',lb:S.sp?0:blendLb(),gone:S.sp,st:S.sp?'Split':'In bin'});
if(S.sp){a.push({id:RP.id,sub:n0(RP.n)+' retail packs, '+RP.each+' lb each',lb:retailLb(),st:'Packed'});a.push({id:BK.id,sub:'Bulk tote, lot '+BL.lot,lb:BK.lb,st:'Packed'});}
return a;}
function held(){return items().reduce(function(a,x){return a+x.lb;},0);}
function tiles(t,a){return '<div class="tl in"><h4>'+t+'</h4>'+a.map(function(x){return '<div><small>'+x[0]+'</small><b>'+x[1]+'</b></div>';}).join('')+'</div>';}
function log(){var a=[['Nov 6','B-101 filled with lot L-A'],['Nov 6','B-102 filled with lot L-B']];if(S.bl)a.push(['Nov 8','B-101 and B-102 blended into B-200']);if(S.sp)a.push(['Nov 9','B-200 split into PK-5120 and BK-2210']);if(S.tr)a.push(['Today','PK-5120 traced']);return a.slice(-3);}
function render(){
$('obb').className='bt '+(S.op?'done':'pri');$('obb').textContent=S.op?'Opened':'Open bin';
$('rs').innerHTML=S.op?'<span class="ch c-idle">Room 2</span>':'';
var sel=S.cu||S.tr?RP.id:S.sp?RP.id:S.bl?BL.id:'B-101';
var l='<div class="ct"><span>Bins and packs</span>'+(S.op?'<span class="ch c-idle">'+items().length+'</span>':'')+'</div>';
if(!S.op)l+='<div class="empt"><b>No bin open</b><span>Open a bin to see the lots inside it.</span></div>';
else{l+=items().map(function(x){return '<div class="row in'+(x.gone?' gone':'')+(x.id===sel?' sel':'')+'" id="b-'+x.id+'"><span><b>'+x.id+'</b><small>'+x.sub+'</small></span><span class="w">'+(x.gone?'<span class="ch c-idle">'+x.st+'</span>':n0(x.lb)+'<small>lb</small>')+'</span></div>';}).join('');
var bins=items().filter(function(x){return /^B-/.test(x.id);}).reduce(function(a,x){return a+x.lb;},0),pk=held()-bins;
l+='<div class="rm in"><div><span>In bins, lb</span><b id="rbin">'+n0(bins)+'</b></div><div><span>Packed, lb</span><b id="rpk">'+n0(pk)+'</b></div><div class="t"><span>Held in room 2</span><b id="rheld">'+n0(held())+'</b></div></div>'+
'<div class="lg in" style="margin-top:auto"><b>Recent moves</b>'+log().map(function(e){return '<div><span>'+e[0]+'</span><span>'+e[1]+'</span></div>';}).join('')+'</div>';}
l+='<div class="tot">Weight follows the lot through every blend and split.</div>';
$('ls').innerHTML=l;
var d='<div class="ct"><span>Record</span>'+(S.op?'<span class="ch c-idle mono">'+sel+'</span>':'')+'</div>';
if(!S.op)d+='<div class="empt"><b>Nothing selected</b><span>The lots in a bin, its blends and splits, and where the product went show here.</span></div>';
else if(!S.bl){var b=BINS['B-101'];
d+='<div class="dh in"><div class="kv"><small>Bulk bin</small><b>B-101</b></div><div class="r2"><span class="ch c-ok">Released</span><span class="ch c-idle">Nonpareil 23/25</span></div></div>'+
'<div class="kg in"><div class="kv"><small>Product</small><b>Blanched almonds</b></div><div class="kv"><small>Location</small><b>Room 2, rack 4</b></div><div class="kv"><small>Filled</small><b>Nov 6</b></div></div>'+
'<div class="sec in"><h4><span>Lots in this bin</span><span class="ch c-idle">1 lot</span></h4><div class="lt" id="lt"><div class="row h"><span>Lot</span><span>Raw delivery</span><span>lb</span><span>Share</span></div><div class="row"><span class="mono"><b>'+b.lot+'</b></span><span>'+b.dl+'<small>'+b.gr+'</small></span><span id="ltl">'+n0(b.lb)+'</span><span>100%</span></div></div></div>'+
tiles('Bin checks',[['Moisture','4.1%'],['Temperature','58 F'],['Allergen group','Tree nut']])+
'<div class="act in"><span>Next: blend with <b class="mono">B-102</b>, lot L-B, '+n0(BINS['B-102'].lb)+' lb</span><button type="button" class="bt pri rt" id="blb">Blend bins</button></div>';}
else if(!S.sp){
d+='<div class="dh in"><div class="kv"><small>New bin, new lot</small><b>'+BL.id+', '+BL.lot+'</b></div><div class="r2"><span class="ch c-info">Blend</span><span class="ch c-ok">Released</span></div></div>'+
'<div class="sec in"><h4><span>Lots in this bin</span><span class="ch c-idle">2 lots</span></h4><div class="lt" id="lt"><div class="row h"><span>Lot</span><span>From bin</span><span>lb</span><span>Share</span></div>'+
['B-101','B-102'].map(function(k){var b=BINS[k];return '<div class="row"><span class="mono"><b>'+b.lot+'</b></span><span>'+k+'<small>'+b.dl+', '+b.gr+'</small></span><span>'+n0(b.lb)+'</span><span id="sh-'+b.lot+'">'+share(k).toFixed(1)+'%</span></div>';}).join('')+
'<div class="row sm"><span>Total</span><span></span><span id="bt">'+n0(blendLb())+'</span><span>100%</span></div></div>'+
'<div class="mix"><i class="a" style="width:'+share('B-101').toFixed(1)+'%">L-A</i><i class="b" style="width:'+share('B-102').toFixed(1)+'%">L-B</i></div>'+
'<div class="calc" id="bcal">'+n0(BINS['B-101'].lb)+' + '+n0(BINS['B-102'].lb)+' = '+n0(blendLb())+' lb</div></div>'+
tiles('Blend record',[['Blended on','Line 3, Nov 8'],['Moisture','4.2%'],['Allergen group','Tree nut']])+
'<div class="act in"><span class="chs"><span>'+n0(RP.n)+' retail packs, '+RP.each+' lb</span><span>'+n0(BK.lb)+' lb bulk tote</span></span><button type="button" class="bt pri rt" id="spb">Split bin</button></div>';}
else if(!S.tr){
d+='<div class="dh in"><div class="kv"><small>Split of '+BL.id+', lot '+BL.lot+'</small><b>'+n0(blendLb())+' lb</b></div><div class="r2"><span class="ch c-ok">Packed</span></div></div>'+
'<div class="sec in"><h4><span>Packs from this bin</span><span class="ch c-idle">2 lots</span></h4><div class="lt" id="lt"><div class="row h"><span>Lot</span><span>Pack</span><span>lb</span><span>Share</span></div>'+
'<div class="row"><span class="mono"><b>'+RP.id+'</b></span><span>Retail<small>'+n0(RP.n)+' packs \u00d7 '+RP.each+' lb</small></span><span id="rlb">'+n0(retailLb())+'</span><span>'+(retailLb()/blendLb()*100).toFixed(1)+'%</span></div>'+
'<div class="row"><span class="mono"><b>'+BK.id+'</b></span><span>Bulk<small>1 tote</small></span><span id="klb">'+n0(BK.lb)+'</span><span>'+(BK.lb/blendLb()*100).toFixed(1)+'%</span></div>'+
'<div class="row sm"><span>Total</span><span></span><span id="stl">'+n0(retailLb()+BK.lb)+'</span><span>100%</span></div></div>'+
'<div class="calc" id="scal">'+n0(retailLb())+' + '+n0(BK.lb)+' = '+n0(retailLb()+BK.lb)+' lb, all of '+BL.id+'</div></div>'+
tiles('Labels',[['Retail labels','1,000 printed'],['Tote label','1 printed'],['Best by','Nov 2027']])+
'<div class="act in"><span>Both packs carry lot '+BL.lot+' and its two raw deliveries.</span><button type="button" class="bt pri rt" id="trb">Trace '+RP.id+'</button></div>';}
else{
d+='<div class="dh in"><div class="kv"><small>Packed lot</small><b>'+RP.id+'</b></div><div class="r2"><span class="ch c-idle">'+n0(RP.n)+' packs</span><span class="ch c-ok">Traced</span></div></div>'+
'<div class="sec in" style="padding-bottom:0"><h4><span>Back to the raw deliveries</span><span class="ch c-idle">'+traceDl().length+' deliveries</span></h4></div><div class="tr in" id="tr">'+
'<div class="tn"><span class="bx"><b>'+RP.id+'</b><small>Retail, 5 lb</small></span><span class="ln">←</span><span class="bx"><b>'+BL.id+'</b><small>Lot '+BL.lot+'</small></span><span class="ln">←</span><span class="bx"><b>B-101</b><small>Lot L-A</small></span><span class="ln">←</span><span class="bx rw" id="d0"><b>'+BINS['B-101'].dl+'</b><small>'+BINS['B-101'].gr+'</small></span></div>'+
'<div class="tn"><span style="width:150px;flex:none"></span><span class="ln">↖</span><span class="bx"><b>B-102</b><small>Lot L-B</small></span><span class="ln">←</span><span class="bx rw" id="d1"><b>'+BINS['B-102'].dl+'</b><small>'+BINS['B-102'].gr+'</small></span></div></div>';
if(!S.cu)d+='<div class="sec in"><h4><span>Raw delivery records</span></h4><div class="dl" id="dl"><div class="row h"><span>Delivery</span><span>Grower</span><span>Net lb</span><span>Moisture</span><span>Lab</span></div><div class="row"><span class="mono">NP-0711</span><span>Harlan Orchards, Oct 28</span><span>28,000</span><span>5.2%</span><span class="mono">VAL-3318</span></div><div class="row"><span class="mono">NP-0709</span><span>Delmar Ranch, Oct 27</span><span>24,400</span><span>5.6%</span><span class="mono">VAL-3301</span></div></div></div>'+'<div class="act in"><span>Who received '+RP.id+'?</span><button type="button" class="bt pri rt" id="cub">List customers</button></div>';
else{var tq=CUS.reduce(function(a,c){return a+c[2];},0);
d+='<div class="sec in"><h4><span>Customers who received '+RP.id+'</span><span class="ch c-info">'+CUS.length+' customers</span></h4><div class="cu" id="cu"><div class="row h"><span>Customer</span><span>Order</span><span>Packs</span><span>lb</span></div>'+
CUS.map(function(c){return '<div class="row"><span>'+c[0]+'</span><span class="mono">'+c[1]+'</span><span>'+n0(c[2])+'</span><span>'+n0(c[2]*RP.each)+'</span></div>';}).join('')+
'<div class="row sm"><span>Shipped</span><span></span><span id="cq">'+n0(tq)+'</span><span id="clb">'+n0(tq*RP.each)+'</span></div></div></div>';}}
d+='<div class="tot">Every bin, blend and pack keeps its lot history.</div>';
$('dt').innerHTML=d;
}
function resetState(){S={op:false,bl:false,sp:false,tr:false,cu:false};render();}
var ST=[
{id:'op',target:function(){return $('obb');},prompt:'Open bin B-101',where:'below',run:function(){S.op=true;render();},
 after:function(){return['A bulk bin and the lots it holds','B-101 holds '+n0(BINS['B-101'].lb)+' lb of lot L-A from delivery NP-0711.'];}},
{id:'bl',target:function(){return $('blb');},prompt:'Blend B-101 with B-102',where:'above',run:function(){S.bl=true;render();},
 after:function(){return['A blend forms a new lot',BL.id+' holds '+n0(blendLb())+' lb of lot '+BL.lot+': '+share('B-101').toFixed(1)+'% L-A and '+share('B-102').toFixed(1)+'% L-B.'];}},
{id:'sp',target:function(){return $('spb');},prompt:'Split B-200 into packs',where:'above',run:function(){S.sp=true;render();},
 after:function(){return['A split into retail and bulk',n0(RP.n)+' retail packs of 5 lb ('+n0(retailLb())+' lb) plus '+n0(BK.lb)+' lb bulk = '+n0(retailLb()+BK.lb)+' lb.'];}},
{id:'tr',target:function(){return $('trb');},prompt:'Trace PK-5120',where:'above',run:function(){S.tr=true;render();},
 after:function(){return['A packed lot traced to its deliveries',RP.id+' goes back through '+BL.id+' to raw deliveries '+traceDl().join(' and ')+'.'];}},
{id:'cu',target:function(){return $('cub');},prompt:'List the customers',where:'above',run:function(){S.cu=true;render();},
 after:function(){return['Every customer who received the lot',CUS.length+' customers took '+n0(CUS.reduce(function(a,c){return a+c[2];},0))+' packs of '+RP.id+'.'];}}];
'''
