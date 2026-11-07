"""Distribution card 4: Advanced Order Management. Layout: an order inbox with channel chips on the left, the order detail with its price list
in the middle, then a pick route with scanning and a shipping panel under it that stay empty until their steps."""
SUMMARY = 'Advanced Order Management (orders from every channel in one inbox, a contract price list applied, release to pick along a bin route, scan to pick with a wrong item flagged, packing slip and bill of lading at ship time)'
ARIA = 'Interactive product screen: show rep, portal, marketplace and EDI orders in one inbox, open SO-6201 for Calder Clinic with its contract price, release it to pick along bins A-04-2, B-11-4 and C-03-1, scan a wrong item, scan the right items and pack and ship it'
STEPS = 6
STUDIO = dict(lede='A typical order desk screen, built on your Sutton data with Studio. Want it different? Describe the change.',
              examples=['A customer price check', 'A pick wave planner', 'A carrier rate view', 'A channel stock reserve rule'],
              built_on='Orders, customers, price lists and bins', change='Rules, fields and views')

CSS = (
 '.b4{display:grid;grid-template-columns:196px 1fr;gap:12px;padding:12px 40px 0 16px;height:596px}'
 '.col{display:flex;flex-direction:column;gap:10px;min-height:0}'
 '.inb{flex:none}.chs{display:flex;flex-wrap:wrap;gap:5px;padding:8px 10px}.fc{border:1px solid #E4E4E7;border-radius:999px;background:#fff;padding:3px 8px;font-size:9.2px;cursor:pointer;transition:background-color .2s,border-color .2s,color .2s}.fc.on{background:#18181B;border-color:#18181B;color:#fff}'
 '.inb button.row{display:flex;flex-direction:column;align-items:stretch;gap:2px;padding:6px 10px;min-height:40px}.inb .l1{display:flex;align-items:center;gap:6px;font-size:9.8px}.inb .l2{font-size:9.2px;color:#71717A}'
 '.cn{display:inline-flex;align-items:center;padding:1px 5px;border-radius:4px;font-size:8.4px;font-weight:600;border:1px solid #E4E4E7;color:#3F3F46;background:#FAFAFA}'
 '.tdy{flex:1 1 0;min-height:0}.tdy .row{grid-template-columns:1fr auto;min-height:23px;font-size:9.6px}'
 '.b4>.col+.col{padding-bottom:34px}.ord{flex:1 1 0;min-height:0}.ord .pd{padding:10px 11px}.ord .kvs{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;padding:7px 11px;border-bottom:1px solid #F0F0F1}'
 '.ord .row{grid-template-columns:1fr 34px 50px 70px 54px;min-height:23px;font-size:9.6px;white-space:nowrap}.ord .row.t{font-weight:600;background:#FAFAFA}.ord .row .ok2{color:#166534;font-weight:600;margin-right:3px}'
 '.rec .row{grid-template-columns:1fr 78px 50px 44px}.prl{margin:7px 11px;border:1px solid #E4E4E7;border-radius:7px;overflow:hidden}.prl .ph{display:flex;align-items:center;gap:6px;padding:5px 9px;background:#FAFAFA;font-size:9.4px;font-weight:600}.prl .row{grid-template-columns:1fr 48px 56px 50px;min-height:21px;font-size:9.2px;padding:0 9px}'
 '.ord .ft{display:flex;align-items:center;gap:7px;padding:6px 11px;border-top:1px solid #F0F0F1}.ord .ft .nt{font-size:9px;color:#71717A}'
 '.two{display:grid;grid-template-columns:1fr 1fr;gap:10px;flex:none;height:170px}.two>.cd{display:flex;flex-direction:column}'
 '.rt{display:flex;align-items:center;gap:4px;padding:8px 10px 4px}.stop{flex:1;border:1px solid #E4E4E7;border-radius:6px;padding:4px 6px;display:flex;flex-direction:column;gap:1px;min-width:0;transition:border-color .3s,background-color .3s}.stop b{font-family:"JetBrains Mono",ui-monospace,monospace;font-size:9.2px}.stop span{font-size:8.6px;color:#71717A;white-space:nowrap}.stop.dn{border-color:#BBF7D0;background:#F0FDF4}.rt .ar{color:#A1A1AA;font-size:10px}'
 '.pk .g,.sh .g{display:flex;align-items:flex-end;gap:6px;padding:6px 10px}.pk .fld,.sh .fld{flex:1}.pk .ms{margin:2px 10px;font-size:9.2px;min-height:20px;display:flex;align-items:center}.pk .bt2{padding:2px 10px 8px}.pk .bt2 .bt,.sh .bw .bt{width:100%}.sh .bw{padding:2px 10px 6px}'
 '.sh .row{grid-template-columns:52px 1fr auto;min-height:23px;font-size:9.4px}.sh .pd,.pk .pd{padding:6px 10px 10px}'
 '.cap:not(.turn){max-width:204px}'
)

WIN = (
 '<div class="hd"><svg width="16" height="16" viewBox="0 0 16 16" fill="none" aria-hidden="true"><path d="M2.5 4.5h11v8h-11z" stroke="#18181B" stroke-width="1.2" stroke-linejoin="round"/><path d="M2.5 4.5L8 9l5.5-4.5" stroke="#18181B" stroke-width="1.2" stroke-linejoin="round"/></svg>'
 '<span class="tt">Orders</span><span class="ch c-idle" id="hst">Rep view</span><span class="sb grow">Ridgeway Supply, order desk</span></div>'
 '<div class="b4"><div class="col"><div class="cd inb" id="inb"></div>'
 '<div class="cd tdy"><div class="ct">Today by channel<span class="mut" style="font-weight:500">Orders</span></div><div class="row"><span><span class="cn">Rep</span></span><span class="mono">6</span></div><div class="row"><span><span class="cn">Portal</span></span><span class="mono">9</span></div><div class="row"><span><span class="cn">Marketplace</span></span><span class="mono">14</span></div><div class="row"><span><span class="cn">EDI</span></span><span class="mono">3</span></div><div class="row"><span class="mut">Shipped today</span><span class="mono">18</span></div><div class="row"><span class="mut">On backorder</span><span class="mono">2</span></div><div class="row"><span class="mut">Waiting on payment</span><span class="mono">1</span></div><div class="row"><span class="mut">Same day cut off</span><span class="mono">15:00</span></div></div></div>'
 '<div class="col"><div class="cd ord" id="ord"></div><div class="two"><div class="cd pk" id="pk"></div><div class="cd sh" id="sh"></div></div></div></div>'
)

JS = r'''
var FOC='.hd>*,.inb .ct,.chs .fc,.inb .row,.tdy,.ord .ct,.ord .kvs,.ord .row,.ord .pd,.rec,.prl,.ord .ft>*,.pk .ct,.rt,.pk .g>*,.pk .ms,.pk .bt2,.pk .pd,.sh .ct,.sh .g>*,.sh .bw,.sh .row,.sh .pd';
var ORD=[['SO-6201','Calder Clinic','Rep','Due 11/10'],['SO-6202','Eastside Dental','Portal','Due 11/11'],['SO-6203','Online buyer','Marketplace','Due 11/10'],['SO-6204','Northgate Retail','EDI','Due 11/12']];
var LN=[['GL-210','Nitrile gloves',24,'A-04-2',7.40,8.50],['TW-330','Shop towels',12,'B-11-4',18.00,18.00],['BT-118','Hex bolt kit',6,'C-03-1',9.50,9.50]];
var S;
function f2(n){return n.toLocaleString('en-US',{minimumFractionDigits:2,maximumFractionDigits:2});}
function r2(n){return Math.round(n*100)/100;}
function pcs(){return LN.reduce(function(a,x){return a+x[2];},0);}
function amt(x){return r2(x[2]*x[4]);}
function total(){return r2(LN.reduce(function(a,x){return a+amt(x);},0));}
function saving(){return r2(LN.reduce(function(a,x){return a+x[2]*(x[5]-x[4]);},0));}
function picked(){return LN.reduce(function(a,x){return a+(S.pk[x[0]]?x[2]:0);},0);}
function val(i){return String($(i).value).trim();}
function render(){
var rows=ORD.filter(function(o){return S.all||o[2]==='Rep';});
var h='<div class="ct">Inbox<span class="mut" style="font-weight:500">'+rows.length+' open</span></div><div class="chs"><button type="button" class="fc'+(S.all?' on':'')+'" id="call">All channels</button>'+['Rep','Portal','Marketplace','EDI'].map(function(c){return '<button type="button" class="fc'+(!S.all&&c==='Rep'?' on':'')+'">'+c+'</button>';}).join('')+'</div>';
rows.forEach(function(o,i){var st=o[0]==='SO-6201'&&S.ship?'<span class="ch c-ok">Shipped</span>':o[0]==='SO-6201'&&S.rel?'<span class="ch c-info">Picking</span>':'';
h+='<button type="button" class="row'+(S.open&&o[0]==='SO-6201'?' sel':'')+(S.anim&&S.all?' in':'')+'" style="animation-delay:'+(i*60)+'ms" id="o-'+o[0]+'"><span class="l1"><span class="mono">'+o[0]+'</span><span class="cn">'+o[2]+'</span><span class="grow"></span>'+st+'</span><span class="l2">'+o[1]+', '+o[3]+'</span></button>';});
$('inb').innerHTML=h;
var d='<div class="ct">Order'+(S.open?'<span class="ch '+(S.ship?'c-ok':S.rel?'c-info':'c-idle')+'" id="ost">'+(S.ship?'Shipped':S.rel?'Released to pick':'Open')+'</span>':'')+'</div>';
if(!S.open)d+='<div class="pd"><div class="empt"><b>No order open</b><span>Open an order from the inbox to see its lines, prices and bins.</span></div></div><div class="rec"><div class="row h"><span>Shipped this week</span><span>Channel</span><span>Carrier</span><span class="r">Shipped</span></div>'+
[['SO-6198','Kestrel Dental','EDI','LTL','11/06'],['SO-6196','Marlow Health','Rep','Parcel','11/06'],['SO-6193','Online buyer','Marketplace','Parcel','11/05'],['SO-6190','Eastside Dental','Portal','Parcel','11/05'],['SO-6188','Calder Clinic','Rep','LTL','11/04'],['SO-6185','Northgate Retail','EDI','LTL','11/03'],['SO-6181','Online buyer','Marketplace','Parcel','11/03']].map(function(x){return '<div class="row"><span><span class="mono">'+x[0]+'</span> '+x[1]+'</span><span><span class="cn">'+x[2]+'</span></span><span class="mut">'+x[3]+'</span><span class="mono r mut">'+x[4]+'</span></div>';}).join('')+'</div>';
else{d+='<div class="kvs'+(S.anim?' in':'')+'"><div class="kv"><small>Order</small><b class="mono">SO-6201</b></div><div class="kv"><small>Customer</small><b>Calder Clinic</b></div><div class="kv"><small>Channel</small><b>Rep, J. Ortiz</b></div></div>'+
'<div class="row h"><span>Item</span><span class="r">Qty</span><span>Bin</span><span class="r">Price</span><span class="r">Amount</span></div>'+
LN.map(function(x){return '<div class="row"><span>'+(S.pk[x[0]]?'<span class="ok2">&#10003;</span>':'')+'<span class="mono">'+x[0]+'</span> '+x[1]+'</span><span class="mono r">'+x[2]+'</span><span class="mono">'+x[3]+'</span><span class="mono r">'+f2(x[4])+'</span><span class="mono r">'+f2(amt(x))+'</span></div>';}).join('')+
'<div class="row t"><span>Total</span><span class="mono r" id="opc">'+pcs()+'</span><span></span><span></span><span class="mono r" id="otot">'+f2(total())+'</span></div>'+
'<div class="prl'+(S.anim?' in':'')+'"><div class="ph">Price list<span class="mono mut" style="font-weight:500">CPL-CALDER</span><span class="grow"></span><span class="ch c-ok">Contract applied</span></div><div class="row h" style="padding:0 9px"><span>Item</span><span class="r">List</span><span class="r">Contract</span><span class="r">Saving</span></div>'+
LN.map(function(x){var c=x[4]<x[5];return '<div class="row"><span class="mono">'+x[0]+'</span><span class="mono r">'+f2(x[5])+'</span><span class="mono r">'+(c?f2(x[4]):'<span class="mut">List</span>')+'</span><span class="mono r">'+(c?f2(r2(x[2]*(x[5]-x[4]))):'')+'</span></div>';}).join('')+'</div>'+
'<div class="ft">'+(S.rel?'<span class="ch c-info">Wave W-118</span><span class="nt">'+(S.ship?'Shipped with BL-3301':'Picking in Atlanta')+'</span>':'<button type="button" class="bt pri" id="rel">Release to pick</button><span class="nt">Atlanta, ships today</span>')+'</div>';}
$('ord').innerHTML=d;
var p='<div class="ct">Pick route'+(S.rel?'<span class="ch c-info" id="pkc">'+picked()+' of '+pcs()+' picked</span>':'')+'</div>';
if(!S.rel)p+='<div class="pd"><div class="empt"><b>Nothing to pick</b><span>Release an order to plan its bin route.</span></div></div>';
else{p+='<div class="rt'+(S.anim?' in':'')+'">'+LN.map(function(x,i){return (i?'<span class="ar">&#8594;</span>':'')+'<div class="stop'+(S.pk[x[0]]?' dn':'')+'"><b>'+x[3]+'</b><span>'+x[0]+' x '+x[2]+'</span></div>';}).join('')+'</div>'+
(S.done?'<div class="pd"><span class="ch c-ok">All '+pcs()+' pieces scanned against SO-6201</span></div>':
'<div class="g frm"><label class="fld" id="fsc"><small>Scan</small><input id="isc" value="'+S.v.sc+'" autocomplete="off" spellcheck="false"><span class="em">Scan a SKU like TW-330</span></label><button type="button" class="bt pri" id="scn">Scan item</button></div>'+
'<div class="ms" id="msg">'+(S.msg||'<span class="mut">'+LN.length+' stops, '+pcs()+' pieces, shortest route</span>')+'</div><div class="bt2"><button type="button" class="bt" id="scok">Scan correct items</button></div>');}
$('pk').innerHTML=p;
var s='<div class="ct">Shipping'+(S.ship?'<span class="ch c-ok">Shipped</span>':'')+'</div><div class="g frm"><label class="fld" id="fpk"><small>Packages</small><input id="ipk" value="'+S.v.pk+'" autocomplete="off" spellcheck="false"><span class="em">Like 1 pallet</span></label><label class="fld" id="fmd"><small>Mode</small><input id="imd" value="'+S.v.md+'" autocomplete="off" spellcheck="false"><span class="em">LTL, FTL or parcel</span></label></div>'+
'<div class="bw">'+(S.ship?'<button type="button" class="bt done" disabled>Packed and shipped</button>':'<button type="button" class="bt pri" id="shp">Pack and ship</button>')+'</div>';
if(!S.ship)s+='<div class="pd"><span class="mut" style="font-size:9.2px;line-height:1.4">The packing slip and bill of lading print from the order at ship time.</span></div>';
else s+='<div class="row in"><span class="mono">PS-3301</span><span>Packing slip</span><span class="ch c-ok">Printed</span></div><div class="row in"><span class="mono">BL-3301</span><span>Bill of lading, '+S.mode+'</span><span class="ch c-ok">Printed</span></div>';
$('sh').innerHTML=s;
$('hst').textContent=S.all?'All channels':'Rep view';$('hst').className='ch '+(S.all?'c-info':'c-idle');
S.anim=false;}
$('pk').addEventListener('input',function(e){if(e.target.id==='isc')S.v.sc=e.target.value;});
$('sh').addEventListener('input',function(e){var k={ipk:'pk',imd:'md'}[e.target.id];if(k)S.v[k]=e.target.value;});
function resetState(){S={all:false,open:false,rel:false,done:false,ship:false,anim:false,pk:{},msg:'',v:{sc:'TW-331',pk:'1 pallet',md:'LTL'}};render();}
function okScan(){var b=!/^[A-Z]{2}-\d{3}$/.test(val('isc').toUpperCase());$('fsc').classList.toggle('err',b);return !b;}
function okShip(){var a=!/^\d{1,2} (pallet|pallets|carton|cartons)$/i.test(val('ipk')),b=!/^(LTL|FTL|parcel)$/i.test(val('imd'));$('fpk').classList.toggle('err',a);$('fmd').classList.toggle('err',b);return !(a||b);}
function lineOf(k){for(var i=0;i<LN.length;i++)if(LN[i][0]===k)return LN[i];return null;}
var CAPAT=function(hh){return{l:14,t:visH()-hh-14};};
var ST=[
{id:'all',target:function(){return $('call');},prompt:'Click All channels',where:'below',run:function(){S.all=true;S.anim=true;render();},after:['Rep, portal, marketplace and EDI orders land in one inbox','Four orders from four channels, each with its channel chip.']},
{id:'open',target:function(){return $('o-SO-6201');},prompt:'Click order SO-6201',where:'right',run:function(){S.open=true;S.anim=true;render();},
 after:function(){return['The customer\'s own price list is applied before anyone touches the order','GL-210 at 7.40 contract against 8.50 list saves '+f2(saving())+'. Total '+f2(total())+'.'];}},
{id:'rel',target:function(){return $('rel');},prompt:'Click Release to pick',where:'right',run:function(){S.rel=true;S.anim=true;render();},after:function(){return['The order releases to pick along the shortest bin route','A-04-2, B-11-4, C-03-1: '+pcs()+' pieces in '+LN.length+' stops.'];}},
{id:'scn',target:function(){return $('scn');},prompt:'Click Scan item',where:'below',ok:okScan,
 run:function(){var k=val('isc').toUpperCase(),x=lineOf(k);S.last=k;if(x){S.pk[k]=1;S.msg='<span class="ch c-ok">'+k+' matches, '+x[2]+' picked from '+x[3]+'</span>';}else S.msg='<span class="ch c-bad" id="flag">'+k+' is not on this order, nothing picked</span>';render();},
 after:function(){return lineOf(S.last)?['A scan that matches the order is picked',S.last+' is on SO-6201, so its line is ticked.']:['A scan that does not match the order is flagged before it is packed',S.last+' looks like TW-330 but is not on SO-6201. Nothing was picked.'];}},
{id:'scok',target:function(){return $('scok');},prompt:'Click Scan correct items',where:'below',run:function(){LN.forEach(function(x){S.pk[x[0]]=1;});S.done=true;S.msg='';render();},after:function(){return['The right items go in, line by line, until the pick is complete',picked()+' of '+pcs()+' picked. Each line is ticked.'];}},
{id:'shp',target:function(){return $('shp');},prompt:'Click Pack and ship',where:'below',ok:okShip,run:function(){okShip();S.pkg=val('ipk').toLowerCase();S.mode=val('imd').toUpperCase()==='PARCEL'?'parcel':val('imd').toUpperCase();S.ship=true;render();},
 after:['The packing slip and bill of lading come from the order at ship time','Packing slip PS-3301 and bill of lading BL-3301 are printed. SO-6201 is shipped.']}];
'''
