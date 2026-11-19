"""Functional beverage card 2: Ingredient Lots & Certificates. Layout: list and detail.
Left: the receiving list (two ashwagandha lots and an L-theanine lot), and the batches with the lot picker for the
next batch. Right: the lot record with its certificate, the certificate values beside the spec, Hold, and a
Suppliers tab with approved and not approved suppliers. A lot passes only when every certificate value is within its
spec; a held lot cannot be picked for a batch."""
from frame_auto import header

SUMMARY = 'Ingredient Lots & Certificates (receive ASH-2291 at 5.2% against a 5.0% minimum, hold ASH-2305 at 4.6%, open the certificate from batch FB-0412, see 2 approved suppliers and 1 not approved)'
ARIA = 'Interactive product screen: receive an active ingredient lot with its certificate, compare certificate values with the spec, hold a lot outside spec, open the certificate from the batch that used it, and see approved suppliers'
STEPS = 5
STUDIO = dict(lede='A typical lot receiving screen on your Sutton data. Want it different? Describe the change.',
              examples=['A retest date per lot', 'Spec limits by supplier', 'A photo of each drum label', 'An alert when a certificate is missing'],
              built_on='Lots, suppliers, specs and certificates', change='Specs, columns and views')

ICON = '<path d="M3 2.5h7l3 3v8H3z"/><path d="M10 2.5v3h3M5.5 8.5l1.5 1.5 3-3"/>'

CSS = (
 '.g2{display:grid;grid-template-columns:206px 440px;gap:10px;padding:10px 44px 0 16px;height:550px}'
 '.lc{display:flex;flex-direction:column;gap:10px;min-width:0}.rl{flex:none}.rl .row{grid-template-columns:1fr auto;min-height:44px;font-size:9.5px}.rl .l2{display:flex;flex-direction:column;gap:2px}.rl .l2 small{font-size:8.3px;color:#71717A}'
 '.bl{flex:1;display:flex;flex-direction:column}.bl .row{grid-template-columns:1fr auto;min-height:42px;font-size:9.4px}.bl .row .bt{font-size:8.9px;padding:2px 7px}.bl .l2{display:flex;flex-direction:column;gap:2px}.bl .l2 small{font-size:8.3px;color:#71717A}'
 '.bl .sub{padding:7px 11px 3px;font-size:8.9px;color:#71717A;font-weight:500;border-top:1px solid #E4E4E7}.pick{display:flex;flex-direction:column;gap:5px;padding:3px 9px 8px}'
 '.opt{display:flex;justify-content:space-between;align-items:center;border:1px solid #E4E4E7;border-radius:6px;padding:5px 7px;font-size:9px;background:#fff}.opt.off{background:#FAFAFA;color:#A1A1AA}.opt b{font-family:"JetBrains Mono",ui-monospace,monospace}'
 '.tot{margin-top:auto;padding:9px 11px;border-top:1px solid #E4E4E7;font-size:9px;color:#52525B;line-height:1.4;background:#FAFAFA}'
 '.dt{display:flex;flex-direction:column}.dt>.empt{margin:10px;flex:1}.pane{flex:1;display:flex;flex-direction:column;min-height:0}'
 '.facts{display:grid;grid-template-columns:1fr 1.4fr .8fr 1fr;gap:8px;padding:8px 11px;border-bottom:1px solid #E4E4E7;background:#FCFCFC}.facts .kv b{font-size:10px}'
 '.cert{margin:10px 11px 0;padding:8px 10px;border:1px solid #E4E4E7;border-radius:7px;display:flex;align-items:center;gap:9px;font-size:9.4px}.cert .ic{width:26px;height:32px;border-radius:4px;background:#F4F4F5;border:1px solid #E4E4E7;display:grid;place-items:center;flex:none;font-size:7.5px;color:#71717A;font-weight:600}'
 '.cert .grow small{display:block;color:#71717A;font-size:8.4px}.cert .bt{font-size:9px;padding:3px 8px}'
 '.sp{margin:10px 11px 0;border:1px solid #E4E4E7;border-radius:8px;overflow:hidden}.sp .row{grid-template-columns:1fr 70px 70px 66px;font-size:9.3px;min-height:26px}.sp .row span:nth-child(2),.sp .row span:nth-child(3){text-align:right;font-family:"JetBrains Mono",ui-monospace,monospace}.sp .row.h span{font-family:inherit!important}.sp .row span:last-child{text-align:right}'
 '.note{margin:10px 11px 0;padding:7px 9px;border-radius:7px;font-size:9px;line-height:1.45;background:#FAFAFA;border:1px solid #F0F0F1;color:#52525B}.note.w{background:#FEF2F2;border-color:#FECACA;color:#991B1B}.note.g{background:#F0FDF4;border-color:#BBF7D0;color:#166534}.note.i{background:#E8EEFC;border-color:#C7D2FE;color:#1E3A8A}'
 '.acts{display:flex;gap:6px;padding:10px 11px 0}.acts .bt{font-size:9.4px;padding:4px 10px}'
 '.lg{margin:10px 11px 10px;border:1px solid #E4E4E7;border-radius:8px;overflow:hidden;flex:1;display:flex;flex-direction:column}.lg .row{grid-template-columns:70px 1fr auto;font-size:9.1px;min-height:24px}.lg .row span:first-child{color:#71717A}.lg .ct{height:28px;font-size:10px}'
 '.su .row{grid-template-columns:1fr 92px 84px;font-size:9.4px;min-height:34px}.su .row span:last-child{text-align:right}.su .row small{display:block;color:#71717A;font-size:8.3px}'
)

WIN = (
 header(ICON, 'Ingredient lots', 'Actives and botanicals received with supplier, potency and certificate')
 + '<div class="g2"><div class="lc"><div class="cd rl" id="rl"></div><div class="cd bl" id="bl"></div></div><div class="cd dt" id="dt"></div></div>'
)

JS = r'''
var FOC='.hd>*,.rl .ct,.rl .row,.bl .ct,.bl .row,.bl .sub,.pick,.bl .tot,.dt>.ct,.tabs,.pane>*';
var LOTS={'ASH-2291':{item:'Ashwagandha root extract',sup:'Verdant Botanicals',qty:'25 kg',coa:'COA-7731',v:[5.2,0.2,4.1]},'ASH-2305':{item:'Ashwagandha root extract',sup:'Sunmere Extracts',qty:'20 kg',coa:'COA-7790',v:[4.6,0.3,5.0]},'LT-0877':{item:'L-theanine',sup:'Coastline Nutrients',qty:'10 kg',coa:'COA-7702',v:null}};
var SPEC=[['Withanolides','%','min',5.0],['Lead','ppm','max',0.5],['Moisture','%','max',8.0]];
var SUP=[['Verdant Botanicals','Ashwagandha root extract','Approved','c-ok','Audited Mar 2026'],['Sunmere Extracts','Ashwagandha root extract','Approved','c-ok','Audited Jan 2026'],['Halcyon Herb Co.','Ashwagandha root extract','Not approved','c-bad','No audit on file']];
var S;
function pass(id,i){var v=LOTS[id].v[i],s=SPEC[i];return s[2]==='min'?v>=s[3]:v<=s[3];}
function lotOk(id){return LOTS[id].v.every(function(_,i){return pass(id,i);});}
function fmt(i,v){return (i===1?v.toFixed(1):v.toFixed(1))+(SPEC[i][1]==='%'?'%':' ppm');}
function st(id){if(id==='LT-0877')return ['Received','c-ok'];if(id==='ASH-2291')return S.rc?(S.c1?['Passed','c-ok']:['Received','c-info']):['Arrived','c-idle'];return S.hold?['On hold','c-bad']:['Arrived','c-idle'];}
function render(){
$('rl').innerHTML='<div class="ct"><span>Receiving</span><span class="ch c-idle">Today</span></div>'+['ASH-2291','ASH-2305','LT-0877'].map(function(id){var L=LOTS[id],s=st(id);return '<button type="button" class="row'+(S.cur===id&&S.view==='lot'?' sel':'')+'" id="l-'+id+'"'+(id==='ASH-2305'?' data-pick="1"':'')+'><span class="l2"><b class="mono">'+id+'</b><small>'+L.item+', '+L.sup+'</small></span><span class="ch '+s[1]+'">'+s[0]+'</span></button>';}).join('');
var b='<div class="ct"><span>Batches</span></div><div class="row"><span class="l2"><b class="mono">FB-0412</b><small>Calm Adaptogen Tonic, used ASH-2291</small></span>'+(S.c1?'<button type="button" class="bt" id="bcb">Certificate</button>':'<span class="ch c-idle">Filled</span>')+'</div>';
b+=[['FB-0410','Recovery Ginger Brew, used GN-3318'],['FB-0409','Focus Citrus Sparkling, used LT-0877']].map(function(x){return '<div class="row"><span class="l2"><b class="mono">'+x[0]+'</b><small>'+x[1]+'</small></span><span class="ch c-idle">Shipped</span></div>';}).join('');
b+='<div class="sub">Pick a lot for FB-0415</div><div class="pick">'+(S.c1?['ASH-2291','ASH-2305'].map(function(id){var off=id==='ASH-2305'&&S.hold;return '<div class="opt'+(off?' off':'')+'" id="o-'+id+'"><b>'+id+'</b><span class="ch '+(off?'c-bad':'c-ok')+'">'+(off?'Held, not selectable':'Selectable')+'</span></div>';}).join(''):'<div class="opt off"><span>Lots appear once received and checked</span></div>')+'</div>';
b+='<div class="tot">Only released lots can be picked for a batch.</div>';
$('bl').innerHTML=b;
var d='<div class="ct"><span>'+(S.cur?'Lot <span class="mono">'+S.cur+'</span>':'Lot record')+'</span>'+(S.cur?'<span class="ch '+st(S.cur)[1]+'">'+st(S.cur)[0]+'</span>':'')+'</div>';
if(!S.cur){d+='<div class="empt"><b>No lot open</b><span>Receive a lot to attach its certificate and check it against the spec.</span></div>';}
else{d+='<div class="tabs"><button type="button" class="tab'+(S.view==='lot'?' on':'')+'" id="t-lot">Lot and certificate</button><button type="button" class="tab'+(S.view==='sup'?' on':'')+'" id="t-sup">Approved suppliers</button></div><div class="pane">';
if(S.view==='sup'){var a=SUP.filter(function(s){return s[2]==='Approved';}).length;d+='<div class="su in"><div class="row h"><span>Supplier</span><span>Status</span><span>Audit</span></div>'+SUP.map(function(s){return '<div class="row"><span>'+s[0]+'<small>'+s[1]+'</small></span><span><span class="ch '+s[3]+'">'+s[2]+'</span></span><span>'+s[4]+'</span></div>';}).join('')+'</div><div class="note i in" id="sno">'+a+' approved, '+(SUP.length-a)+' not approved for ashwagandha root extract. Purchase orders only go to approved suppliers.</div>'+'<div class="lg in"><div class="ct"><span>Lots received this year</span></div>'+[['Verdant Botanicals','6 lots','All passed'],['Sunmere Extracts','4 lots',S.hold?'1 on hold':'All passed'],['Halcyon Herb Co.','0 lots','Not approved']].map(function(x){return '<div class="row"><span>'+x[1]+'</span><span>'+x[0]+'</span><span class="ch c-idle">'+x[2]+'</span></div>';}).join('')+'</div>';}
else{var id=S.cur,L=LOTS[id];
d+='<div class="facts in"><div class="kv"><small>Item</small><b>'+L.item.replace(' root extract','')+'</b></div><div class="kv"><small>Supplier</small><b>'+L.sup+'</b></div><div class="kv"><small>Quantity</small><b class="mono">'+L.qty+'</b></div><div class="kv"><small>Received</small><b>Nov 19, 2026</b></div></div>'+
'<div class="cert in"><span class="ic">PDF</span><span class="grow"><b class="mono" id="coa">'+L.coa+'</b><small>'+(S.fromBatch&&id==='ASH-2291'?'Opened from batch FB-0412':'Certificate of analysis, attached at receiving')+'</small></span><span class="ch c-ok">Attached</span></div>';
var shown=(id==='ASH-2291'&&S.c1)||id==='ASH-2305';
if(shown)d+='<div class="sp in"><div class="row h"><span>Test</span><span>Certificate</span><span>Spec</span><span>Result</span></div>'+SPEC.map(function(s,i){var ok=pass(id,i);return '<div class="row"><span>'+s[0]+'</span><span id="cv-'+i+'">'+fmt(i,L.v[i])+'</span><span>'+s[2]+' '+fmt(i,s[3])+'</span><span><span class="ch '+(ok?'c-ok':'c-bad')+'" id="cr-'+i+'">'+(ok?'Pass':'Fail')+'</span></span></div>';}).join('')+'</div>';
if(id==='ASH-2291'&&!S.c1)d+='<div class="acts"><button type="button" class="bt pri" id="cmb">Compare with spec</button></div>';
if(id==='ASH-2291'&&S.c1)d+='<div class="note g in">All values within spec. '+id+' is released for use.</div>';
if(id==='ASH-2305'){d+=S.hold?'<div class="note w in" id="hno">'+id+' is on hold: withanolides 4.6% is below the 5.0% minimum. It cannot be picked for a batch.</div>':'<div class="note w in">Withanolides 4.6% is below the 5.0% minimum.</div><div class="acts"><button type="button" class="bt pri" id="hdb">Hold lot</button></div>';}}
if(S.view==='lot'){var A=[['9:10','Received, '+LOTS[S.cur].qty,'Lot created'],['9:12','Certificate '+LOTS[S.cur].coa+' attached','Attached']];if(S.cur==='ASH-2291'&&S.c1)A.push(['9:20','Spec check, 3 of 3 within spec','Passed']);if(S.cur==='ASH-2305')A.push(['9:25','Spec check, withanolides below minimum','Failed']);if(S.cur==='ASH-2305'&&S.hold)A.push(['9:26','Placed on hold, blocked from batches','On hold']);if(S.cur==='ASH-2291'&&S.fromBatch)A.push(['Nov 12','Used in batch FB-0412','Used']);
d+='<div class="lg in"><div class="ct"><span>Lot activity</span></div>'+A.map(function(a){return '<div class="row"><span>'+a[0]+'</span><span>'+a[1]+'</span><span class="ch c-idle">'+a[2]+'</span></div>';}).join('')+'</div>';}
d+='</div>';}
$('dt').innerHTML=d;
}
function resetState(){S={cur:null,rc:false,c1:false,hold:false,fromBatch:false,view:'lot'};render();}
winEl.addEventListener('click',function(e){var r=e.target.closest&&e.target.closest('#l-ASH-2305');if(r&&S.c1&&!S.hold&&mode==='try'){S.cur='ASH-2305';S.view='lot';render();}});
function capN(){var i=cap.querySelector('.m i');return i?+i.textContent:1;}
var CAPAT=function(hh){var w=cap.offsetWidth;return capN()>=4?{l:visW()-w-14,t:visH()-hh-14}:{l:visW()-w-14,t:visH()-hh-14};};
var ST=[
{id:'rc',target:function(){return $('l-ASH-2291');},prompt:'Receive ASH-2291',where:'right',run:function(){S.rc=true;S.cur='ASH-2291';S.view='lot';render();},
 after:function(){return['A lot received with its certificate','ASH-2291 from Verdant Botanicals, 25 kg, certificate COA-7731 attached.'];}},
{id:'c1',target:function(){return $('cmb');},prompt:'Compare with the spec',where:'below',run:function(){S.c1=true;render();},
 after:function(){return['Certificate values beside the spec','Withanolides 5.2% against a 5.0% minimum: passes, with lead and moisture in spec.'];}},
{id:'hold',target:function(){return $('hdb');},back:function(){return S.cur==='ASH-2305'?null:[$('l-ASH-2305'),'Open ASH-2305','right'];},prompt:'Hold the lot',where:'below',
 run:function(){S.cur='ASH-2305';S.view='lot';S.hold=true;render();},
 after:function(){return['An out of spec lot goes on hold','ASH-2305 at 4.6% is below the 5.0% minimum. It cannot be picked for batch FB-0415.'];}},
{id:'cb',target:function(){return $('bcb');},prompt:'Open the certificate from FB-0412',where:'right',run:function(){S.cur='ASH-2291';S.view='lot';S.fromBatch=true;render();},
 after:function(){return['The certificate, from the batch that used it','Batch FB-0412 used ASH-2291, so COA-7731 opens from the batch record.'];}},
{id:'sup',target:function(){return $('t-sup');},prompt:'See approved suppliers',where:'below',run:function(){S.view='sup';render();},
 after:function(){return['Approved suppliers for the ingredient','2 approved, 1 not approved for ashwagandha root extract.'];}}];
'''
