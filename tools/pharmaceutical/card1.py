"""Pharmaceutical card 1: Supplier Lot to Batch Trace. Layout: a search row, a supplier lot card and a batch list on the
left (affected batches marked, an unaffected batch greyed out), and a batch dossier on the right with three tabs:
Inputs, Shipments and Status. Every quantity is computed from the data below (grams and bottle counts), so the sums hold."""
from frame_auto import header

SUMMARY = 'Supplier Lot to Batch Trace (type supplier lot EX-3307, find the batches that used it, open B-2611 inputs by supplier lot, follow the bottles to customers, hold what is on site)'
ARIA = 'Interactive product screen: trace supplier lot EX-3307 to batches B-2611 and B-2614, open the B-2611 dossier with every input by supplier lot, see shipments to customers, and hold the affected stock'
STEPS = 5
STUDIO = dict(lede='A typical lot trace screen, built on your Sutton data with Studio. Want it different? Describe the change.',
              examples=['A supplier notice log', 'A customer letter per shipment', 'A trace by capsule shell lot', 'A hold report for the quality team'],
              built_on='Lots, batches, BOMs and shipments', change='Columns, holds and views')

ICON = '<circle cx="5" cy="5" r="2.6"/><circle cx="11.5" cy="11.5" r="2.6"/><path d="M7 7l2.6 2.6"/>'

CSS = (
 '.fld input[readonly]{background:#FAFAFA;cursor:default;pointer-events:none}'
 '.g1{display:grid;grid-template-columns:236px 1fr;grid-template-rows:46px 484px;gap:10px;padding:10px 40px 0 16px}'
 '.srch{grid-column:1/3;display:flex;align-items:center;gap:12px;padding:0 12px}.srch .frm{display:flex;align-items:center;gap:8px;flex:none}'
 '.srch .fld{flex-direction:row;align-items:center;gap:8px;position:relative}.srch .fld small{white-space:nowrap}.srch .fld input{width:150px}.srch .fld .em{position:absolute;left:0;top:30px;white-space:nowrap}'
 '.srch .smp{display:flex;align-items:center;gap:6px;font-size:8.8px;color:#71717A}.srch .smp .bt{font-family:"JetBrains Mono",ui-monospace,monospace;font-size:9px;padding:3px 7px}.srch .nt{margin-left:auto;font-size:9px;color:#A1A1AA;white-space:nowrap}'
 '.lc{display:flex;flex-direction:column;gap:10px;min-width:0}.lot{height:206px;flex:none;display:flex;flex-direction:column}.bls{flex:1;display:flex;flex-direction:column}'
 '.lot .kg{display:grid;grid-template-columns:1fr 1fr;gap:7px 10px;padding:9px 11px 0}.lot .kg .kv b{font-size:10px}.lot .wide{grid-column:span 2}'
 '.lot .bal{margin:9px 11px 0;height:8px;border-radius:4px;background:#F4F4F5;overflow:hidden;display:flex}.lot .bal i{display:block;height:100%;background:#A1A1AA;transition:width .5s ease}.lot .bal i.u{background:#52525B}'
 '.lot .ft{margin-top:auto;display:flex;align-items:center;gap:6px;padding:0 11px 10px}.lot .ft .bt{margin-left:auto}'
 '.bls .row{grid-template-columns:1fr 64px 72px;font-size:9.6px}.bls button.row{min-height:46px}.bls .row span:nth-child(2){text-align:right;font-family:"JetBrains Mono",ui-monospace,monospace}.bls .row span:last-child{text-align:right}'
 '.bls .bn2{display:flex;flex-direction:column;gap:2px}.bls .bn2 small{font-size:8.6px;color:#71717A}.bls .row.na{color:#A1A1AA;background:#FAFAFA}.bls .row.na .ch{opacity:.8}'
 '.bls .tot{margin-top:auto;padding:9px 11px;border-top:1px solid #E4E4E7;font-size:9.2px;color:#52525B;line-height:1.4;background:#FAFAFA}'
 '.bls .empt{margin:10px 10px 0;flex:1}.bls .empt+.tot{margin-top:10px}.dos .empt{margin:10px;flex:1}'
 '.dos{display:flex;flex-direction:column}.dos .ct .ch{margin-left:6px}.dos .ct .grow{display:flex;align-items:center}.dos .ct .bt{font-size:9.6px;padding:3px 9px}'
 '.facts{display:grid;grid-template-columns:repeat(5,1fr);gap:8px;padding:9px 11px;border-bottom:1px solid #E4E4E7;background:#FCFCFC}.facts .kv b{font-size:10px}'
 '.pane{flex:1;display:flex;flex-direction:column;min-height:0}'
 '.inp .row{grid-template-columns:1fr 64px 72px 74px;font-size:9.6px;min-height:29px}.inp .row span:nth-child(3){text-align:right;font-family:"JetBrains Mono",ui-monospace,monospace}.inp .row span:last-child{text-align:right}'
 '.inp .row.tr{background:#FEF9E7;box-shadow:inset 3px 0 0 #F59E0B}.inp .row.t{font-weight:600;background:#FAFAFA}.inp .nm small{display:block;color:#71717A;font-size:8.4px}'
 '.shp .row{grid-template-columns:62px 52px 1fr 52px 70px;font-size:9.6px;min-height:28px}.shp .row span:nth-child(4){text-align:right;font-family:"JetBrains Mono",ui-monospace,monospace}.shp .row span:last-child{text-align:right}'
 '.sub{padding:8px 11px 4px;font-size:9px;color:#71717A;font-weight:500}'
 '.tiles{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;padding:10px 11px 0}.tile{border:1px solid #E4E4E7;border-radius:7px;padding:7px 9px;background:#FAFAFA}.tile small{display:block;font-size:8.8px;color:#71717A}.tile b{font-size:17px;font-weight:600;letter-spacing:-.02em}'
 '.sts .row{grid-template-columns:1fr 96px 80px 74px;font-size:9.6px;min-height:30px}.sts .row span:nth-child(2){text-align:right;font-family:"JetBrains Mono",ui-monospace,monospace}.sts .row span:nth-child(3),.sts .row span:last-child{text-align:right}'
 '.held{margin:10px 11px 0;padding:9px 11px;border-radius:7px;background:#FEF2F2;border:1px solid #FECACA;color:#991B1B;font-size:10.4px;font-weight:600}.held small{display:block;font-weight:400;font-size:9px;margin-top:2px}'
 '.cus{padding:0 0 4px}.cus .row{grid-template-columns:1fr 90px;font-size:9.6px}.cus .row span:last-child{text-align:right;font-family:"JetBrains Mono",ui-monospace,monospace}'
 '.c-hold{background:#FEE2E2;color:#991B1B}'
)

WIN = (
 header(ICON, 'Lot trace', 'Supplier lots to batches, CP-050 capsules 50 mg')
 + '<div class="g1"><div class="cd srch" id="srch"><div class="frm"><label class="fld" id="flt"><small>Supplier lot or batch number</small>'
 '<input id="ilt" value="EX-3307" readonly tabindex="-1" autocomplete="off" spellcheck="false"></label>'
 '<button type="button" class="bt pri" id="trb">Trace</button></div>'
 '<span class="nt">Lots and batches</span></div>'
 '<div class="lc"><div class="cd lot" id="lot"></div><div class="cd bls" id="bls"></div></div><div class="cd dos" id="dos"></div></div>'
)

JS = r'''
var FOC='.hd>*,.srch>*,.lot,.bls .ct,.bls .row,.bls .tot,.dos .ct,.facts,.tabs,.pane>*,.dos .ct>*';
var LOT={id:'EX-3307',mat:'Microcrystalline cellulose',sup:'Alder Ridge Supply',rec:150000,recd:'Sep 30, 2026'};
var BAT=[{id:'B-2611',lot:'EX-3307',g:68996,caps:200000,bot:2000,made:'Oct 14, 2026'},{id:'B-2614',lot:'EX-3307',g:34498,caps:100000,bot:1000,made:'Oct 21, 2026'},{id:'B-2609',lot:'EX-3190',g:0,caps:200000,bot:2000,made:'Oct 8, 2026'}];
var SHIP=[['SH-3101','B-2611','Kestrel Wellness',800,'Oct 20'],['SH-3104','B-2611','Bayline Compounding',400,'Oct 23'],['SH-3109','B-2614','Kestrel Wellness',600,'Oct 28']];
var SITE=[['B-2611',800,'Released'],['B-2614',400,'Quarantine']];
var INP=[['Active ingredient','AP-8841',10204,'kg','Assay 98.0%'],['Microcrystalline cellulose','EX-3307',68996,'kg','Alder Ridge Supply'],['Magnesium stearate','EX-4410',800,'kg','Lubricant'],
['Capsule shells','CS-1192',200000,'ea','Size 1'],['Bottles','PK-7720',2000,'ea','100 count'],['Caps','PK-7731',2000,'ea','Child resistant'],['Labels','LB-5503',2000,'ea','CP-050 label']];
var S;
function k3(g){return (g/1000).toLocaleString('en-US',{minimumFractionDigits:3,maximumFractionDigits:3});}
function hit(){return BAT.filter(function(b){return b.lot===LOT.id;});}
function used(){return hit().reduce(function(a,b){return a+b.g;},0);}
function made(){return hit().reduce(function(a,b){return a+b.bot;},0);}
function shipped(){return SHIP.reduce(function(a,s){return a+s[3];},0);}
function onsite(){return SITE.reduce(function(a,s){return a+s[1];},0);}
function cust(){var m={},o=[];SHIP.forEach(function(s){if(!(s[2]in m)){m[s[2]]=0;o.push(s[2]);}m[s[2]]+=s[3];});return o.map(function(c){return [c,m[c]];});}
function blendKg(){return INP.filter(function(i){return i[3]==='kg';}).reduce(function(a,i){return a+i[2];},0);}
function render(){
var l='<div class="ct"><span>Supplier lot</span>'+(S.lot?'<span class="ch '+(S.hold?'c-hold':'c-ok')+'" id="lst">'+(S.hold?'On hold':'Released')+'</span>':'<span class="ch c-idle">Waiting</span>')+'</div>';
if(!S.lot)l+='<div class="empt" style="margin:10px;flex:1"><b>No lot selected</b><span>Type a supplier lot or a batch number to start a trace.</span></div>';
else{l+='<div class="kg in"><div class="kv"><small>Lot</small><b class="mono">'+LOT.id+'</b></div><div class="kv"><small>Received</small><b class="mono" id="lrc">'+k3(LOT.rec)+' kg</b></div>'+
'<div class="kv wide"><small>Material</small><b>'+LOT.mat+'</b></div><div class="kv wide"><small>Supplier</small><b>'+LOT.sup+', '+LOT.recd+'</b></div>'+
(S.wu?'<div class="kv"><small>Consumed</small><b class="mono" id="lcs">'+k3(used())+' kg</b></div><div class="kv"><small>On hand</small><b class="mono" id="loh">'+k3(LOT.rec-used())+' kg</b></div>':'<div class="kv wide"><small>Certificate</small><b>Attached, received with the lot</b></div>')+'</div>'+
(S.wu?'<div class="bal"><i class="u" style="width:'+(used()/LOT.rec*100).toFixed(1)+'%"></i><i style="width:0"></i></div>':'')+
'<div class="ft">'+(S.wu?'<span class="mut" style="font-size:9px">'+hit().length+' batches used this lot</span>':'')+(S.wu?'<button type="button" class="bt done" disabled>Where used</button>':'<button type="button" class="bt" id="wu">Where used</button>')+'</div>';}
$('lot').innerHTML=l;
var b='<div class="ct"><span>CP-050 batches</span>'+(S.wu?'<span class="ch c-warn">'+hit().length+' affected</span>':'')+'</div>';
if(!S.wu)b+='<div class="empt"><b>'+(S.lot?'Batches not checked yet':'Nothing traced yet')+'</b><span>'+(S.lot?'Where used lists every batch that took this lot.':'Batches that used the lot show here.')+'</span></div><div class="tot">The trace covers every CP-050 batch, released or in quarantine.</div>';
else{b+='<div class="row h"><span>Batch</span><span>Used</span><span>Trace</span></div>'+BAT.map(function(x){var a=x.lot===LOT.id,on=S.bat===x.id;
return '<button type="button" class="row'+(a?'':' na')+(on?' sel':'')+' in" id="b-'+x.id+'"><span class="bn2"><b class="mono">'+x.id+'</b><small>Lot '+x.lot+'</small></span><span id="bu-'+x.id+'">'+(a?k3(x.g)+' kg':'0.000 kg')+'</span><span>'+(a?(S.hold?'<span class="ch c-hold">On hold</span>':'<span class="ch c-warn">Affected</span>'):'<span class="ch c-idle">Not affected</span>')+'</span></button>';}).join('')+
'<div class="tot">'+k3(BAT[0].g)+' kg plus '+k3(BAT[1].g)+' kg is '+k3(used())+' kg consumed. B-2609 used lot EX-3190.</div>';}
$('bls').innerHTML=b;
var d='<div class="ct"><span class="grow">Batch dossier'+(S.bat?'<span class="ch c-info mono">'+S.bat+'</span><span class="ch c-idle mono">Supplier lot '+LOT.id+'</span>':'')+'</span>'+(S.bat?(S.hold?'<span class="ch c-hold">Stock on hold</span>':'<button type="button" class="bt pri" id="hold">Hold affected stock</button>'):'')+'</div>';
if(!S.bat)d+='<div class="empt"><b>No batch open</b><span>'+(S.wu?'Open a batch to see every input by supplier lot, its shipments and its status.':'Run a trace, then open a batch to see its inputs, shipments and status.')+'</span></div>';
else{var x=BAT[0];d+='<div class="facts in"><div class="kv"><small>Product</small><b>CP-050</b></div><div class="kv"><small>Formula</small><b>v4</b></div><div class="kv"><small>Capsules</small><b class="mono">'+n0(x.caps)+'</b></div><div class="kv"><small>Bottles</small><b class="mono">'+n0(x.bot)+'</b></div><div class="kv"><small>Made</small><b>'+x.made+'</b></div></div>'+
'<div class="tabs"><button type="button" class="tab'+(S.tab==='in'?' on':'')+'" id="t-in">Inputs</button><button type="button" class="tab'+(S.tab==='sh'?' on':'')+'" id="t-sh">Shipments</button><button type="button" class="tab'+(S.tab==='st'?' on':'')+'" id="t-st">Status</button></div><div class="pane">';
if(S.tab==='in'){d+='<div class="inp"><div class="row h"><span>Input</span><span>Supplier lot</span><span>Quantity</span><span>Certificate</span></div>'+INP.map(function(i){var cert=i[3]==='kg'?'<span class="ch c-ok">Attached</span>':'<span class="ch c-idle">Count checked</span>';
return '<div class="row in'+(i[1]===LOT.id?' tr':'')+'"><span class="nm">'+i[0]+'<small>'+i[4]+'</small></span><span class="mono">'+i[1]+'</span><span>'+(i[3]==='kg'?k3(i[2])+' kg':n0(i[2]))+'</span><span>'+cert+'</span></div>';}).join('')+
'<div class="row t"><span>Weighed into the blend</span><span></span><span id="bkg">'+k3(blendKg())+' kg</span><span></span></div></div><div class="sub">Traced lot '+LOT.id+' is marked. Every input carries its supplier lot and its certificate status.</div>';}
else if(S.tab==='sh'){var c=cust();d+='<div class="shp"><div class="row h"><span>Shipment</span><span>Batch</span><span>Customer</span><span>Bottles</span><span>Status</span></div>'+SHIP.map(function(s){return '<div class="row in"><span class="mono">'+s[0]+'</span><span class="mono">'+s[1]+'</span><span>'+s[2]+'</span><span>'+n0(s[3])+'</span><span><span class="ch c-info">Shipped '+s[4]+'</span></span></div>';}).join('')+
SITE.map(function(s){return '<div class="row in"><span class="mut">On site</span><span class="mono">'+s[0]+'</span><span class="mut">'+(s[2]==='Released'?'Released, in stock':'Awaiting release testing')+'</span><span>'+n0(s[1])+'</span><span><span class="ch '+(s[2]==='Released'?'c-ok':'c-warn')+'">'+s[2]+'</span></span></div>';}).join('')+'</div>'+
'<div class="tiles"><div class="tile"><small>Bottles made</small><b id="smd">'+n0(made())+'</b></div><div class="tile"><small>Shipped</small><b id="ssh">'+n0(shipped())+'</b></div><div class="tile"><small>On site</small><b id="sos">'+n0(onsite())+'</b></div></div>'+
'<div class="sub">Customers who received affected bottles</div><div class="cus">'+c.map(function(x){return '<div class="row"><span>'+x[0]+'</span><span>'+n0(x[1])+' bottles</span></div>';}).join('')+'</div>';}
else{d+='<div class="sts"><div class="row h"><span>Stock</span><span>Quantity</span><span>Was</span><span>Now</span></div>'+
SITE.map(function(s){return '<div class="row in"><span><span class="mono">'+s[0]+'</span> <span class="mut">bottles</span></span><span>'+n0(s[1])+' bottles</span><span>'+s[2]+'</span><span><span class="ch '+(S.hold?'c-hold':s[2]==='Released'?'c-ok':'c-warn')+'">'+(S.hold?'On hold':s[2])+'</span></span></div>';}).join('')+
'<div class="row in"><span><span class="mono">'+LOT.id+'</span> <span class="mut">cellulose</span></span><span id="rkg">'+k3(LOT.rec-used())+' kg</span><span>Released</span><span><span class="ch '+(S.hold?'c-hold':'c-ok')+'">'+(S.hold?'On hold':'Released')+'</span></span></div></div>'+
(S.hold?'<div class="held in" id="hsum">'+hit().length+' batches, '+cust().length+' customers, '+n0(onsite())+' bottles held.<small>'+k3(LOT.rec-used())+' kg of '+LOT.id+' held at the warehouse. Shipped bottles: '+n0(shipped())+', listed by customer below.</small></div>':'<div class="sub">Nothing is on hold yet.</div>')+
'<div class="sub">Customers to contact</div><div class="cus">'+cust().map(function(x){return '<div class="row"><span>'+x[0]+'</span><span>'+n0(x[1])+' bottles</span></div>';}).join('')+'</div>';}
d+='</div>';}
$('dos').innerHTML=d;
}
function resetState(){S={lot:false,wu:false,bat:null,tab:'in',hold:false};render();}
function capN(){var i=cap.querySelector('.m i');return i?+i.textContent:1;}
var CAPAT=function(hh){var w=cap.offsetWidth;return capN()<=2?{l:visW()-w-14,t:visH()-hh-58}:{l:14,t:visH()-hh-14};};
var ST=[
{id:'lot',target:function(){return $('trb');},prompt:'Click Trace to look up EX-3307',where:'below',
 run:function(quick){var go=function(){S.lot=true;render();};go();},
 after:function(){return['A supplier notice names one lot','EX-3307, microcrystalline cellulose from Alder Ridge Supply. '+k3(LOT.rec)+' kg received.'];}},
{id:'wu',target:function(){return $('wu');},prompt:'Find every batch that used it',where:'below',run:function(){S.wu=true;render();},
 after:function(){return['Every batch that used the lot, with the kilograms','B-2611 took '+k3(BAT[0].g)+' kg and B-2614 '+k3(BAT[1].g)+' kg. '+k3(LOT.rec-used())+' kg still on hand.'];}},
{id:'bat',target:function(){return $('b-B-2611');},prompt:'Open batch B-2611',where:'right',run:function(){S.bat='B-2611';S.tab='in';render();},
 after:function(){return['The dossier lists every input by supplier lot','Seven inputs, each with its supplier lot and certificate. Blend total '+k3(blendKg())+' kg.'];}},
{id:'sh',target:function(){return $('t-sh');},prompt:'Open Shipments',where:'below',run:function(){S.tab='sh';render();},
 after:function(){return['Follow the bottles to customers',n0(made())+' bottles made, '+n0(shipped())+' shipped, '+n0(onsite())+' still on site.'];}},
{id:'hold',target:function(){return $('hold');},prompt:'Hold the affected stock',where:'below',run:function(){S.hold=true;S.tab='st';render();},
 after:function(){return['One click holds what is still on site',n0(onsite())+' bottles and '+k3(LOT.rec-used())+' kg of EX-3307 now on hold.'];}}];
'''
