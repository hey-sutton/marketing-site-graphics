"""Pharmaceutical card 2: Quarantine & Release. Layout: a three lane release board (Quarantine, In test, Released) holding
lot cards, a lot history log under the lanes, and on the right the receiving input, the availability panel for the
active ingredient and the B-2620 pick list. Availability is computed from the lanes: only released active lots count as
on hand, so a quarantined lot never counts toward available."""
from frame_auto import header

SUMMARY = 'Quarantine & Release (receive PO-4420 into quarantine, send the lots to test with the certificate, see a pick of untested material blocked, sign off the release, watch availability clear the shortage)'
ARIA = 'Interactive product screen: receive purchase order PO-4420 into quarantine, move lot AP-8842 to test with its certificate, try to pick it for batch B-2620, sign off its release, and see available stock update'
STEPS = 5
STUDIO = dict(lede='A typical release board, built on your Sutton data with Studio. Want it different? Describe the change.',
              examples=['A retest reminder 30 days out', 'A second sign off for actives', 'A sampling plan per material', 'A release queue by due date'],
              built_on='Lots, purchase orders, locations and work orders', change='Lanes, sign offs and rules')

ICON = '<rect x="2" y="3" width="3.4" height="10" rx=".8"/><rect x="6.3" y="3" width="3.4" height="7" rx=".8"/><rect x="10.6" y="3" width="3.4" height="4.5" rx=".8"/>'

CSS = (
 '.fld input[readonly]{background:#FAFAFA;cursor:default;pointer-events:none}'
 '.g2{display:grid;grid-template-columns:1fr 212px;gap:10px;padding:10px 40px 0 16px}'
 '.lft,.rgt{display:flex;flex-direction:column;gap:10px;min-width:0}'
 '.lns{height:376px;flex:none;display:grid;grid-template-columns:repeat(3,1fr);gap:8px}'
 '.ln{border:1px solid #E4E4E7;border-radius:8px;background:#FAFAFA;display:flex;flex-direction:column;min-width:0;overflow:hidden}'
 '.ln .lh{display:flex;align-items:center;gap:6px;height:30px;padding:0 9px;font-weight:600;font-size:10.2px;border-bottom:1px solid #E4E4E7;background:#fff}.ln .lh .ch{margin-left:auto}.ln .lh i{width:7px;height:7px;border-radius:50%;flex:none}'
 '.ln .lb{flex:1;display:flex;flex-direction:column;gap:7px;padding:8px}.ln .le{flex:1;display:grid;place-items:center;text-align:center;color:#A1A1AA;font-size:9.2px;border:1px dashed #E4E4E7;border-radius:7px;padding:8px}'
 '.ln .lf{height:28px;flex:none;display:flex;align-items:center;padding:0 9px;border-top:1px solid #E4E4E7;font-size:8.8px;color:#71717A;background:#fff;white-space:nowrap}.ln .lf .mono{margin-left:auto;color:#18181B}'
 '.lk{border:1px solid #E4E4E7;border-radius:7px;background:#fff;padding:7px 8px;display:flex;flex-direction:column;gap:3px;box-shadow:0 1px 0 rgba(0,0,0,.03)}.lk.me{border-color:#A1A1AA}'
 '.lk .l1{display:flex;align-items:baseline;justify-content:space-between;gap:4px}.lk .l1 b{font-size:10.4px}.lk .l1 span{font-size:9.6px}.lk small{font-size:8.6px;color:#71717A}'
 '.lk .ch{align-self:flex-start;margin-top:2px}.lk .bt{margin-top:4px;font-size:9.4px;padding:4px 8px;align-self:flex-start}'
 '.cert{margin-top:4px;border-top:1px dashed #E4E4E7;padding-top:5px;display:grid;grid-template-columns:auto 1fr;gap:2px 8px;font-size:8.8px}.cert span:nth-child(odd){color:#71717A}.cert span:nth-child(even){text-align:right;font-family:"JetBrains Mono",ui-monospace,monospace}.cert .ct2{grid-column:span 2;color:#166534!important;font-family:inherit!important;text-align:left!important}'
 '.so{margin-top:5px;border-radius:6px;background:#F4F4F5;padding:6px 7px;display:flex;align-items:center;flex-wrap:wrap;gap:6px;font-size:8.8px}.so .bt{margin:0;flex-basis:100%}.so>span:not(.av2){flex:1;min-width:0}'
 '.av2{width:20px;height:20px;border-radius:50%;background:#18181B;color:#fff;display:grid;place-items:center;font-size:8px;font-weight:600;flex:none;letter-spacing:.02em}.av2.g{background:#E4E4E7;color:#3F3F46}'
 '.his{flex:1;display:flex;flex-direction:column}.his .row{grid-template-columns:38px 26px 1fr;font-size:9.4px;min-height:26px}.his .row .mono{color:#71717A}.his .empt{margin:8px;flex:1}'
 '.rcv{height:120px;flex:none}.rcv .frm{display:flex;align-items:flex-end;gap:6px;padding:8px 10px 0}.rcv .fld{flex:1}.rcv .smp{display:flex;align-items:center;gap:6px;padding:6px 10px 0;font-size:8.8px;color:#71717A}.rcv .smp .bt{font-family:"JetBrains Mono",ui-monospace,monospace;font-size:9px;padding:3px 7px}'
 '.ava{height:216px;flex:none;display:flex;flex-direction:column}.ava .row{grid-template-columns:1fr 64px;font-size:9.4px;min-height:25px}.ava .row span:last-child{text-align:right;font-family:"JetBrains Mono",ui-monospace,monospace}'
 '.ava .row.s{color:#71717A;font-size:9px;min-height:21px;border-top:0;padding-left:20px}.ava .row.t{font-weight:600}'
 '.abx{margin:auto 10px 10px;padding:8px 10px;border-radius:7px;border:1px solid #E4E4E7;background:#FAFAFA;display:flex;flex-direction:column;gap:2px;transition:background-color .4s,border-color .4s}.abx small{font-size:9px;color:#71717A}.abx b{font-size:18px;font-weight:600;letter-spacing:-.02em}'
 '.abx.bad{background:#FEF2F2;border-color:#FECACA}.abx.bad b,.abx.bad small{color:#991B1B}.abx.ok{background:#F0FDF4;border-color:#BBF7D0}.abx.ok b,.abx.ok small{color:#166534}'
 '.pk{flex:1;display:flex;flex-direction:column}.pk .row{grid-template-columns:1fr 60px;font-size:9.4px}.pk .row span:last-child{text-align:right;font-family:"JetBrains Mono",ui-monospace,monospace}.pk .pa{display:flex;align-items:center;gap:6px;padding:8px 10px 0}'
 '.pk .msg{margin:8px 10px 0;padding:6px 8px;border-radius:6px;font-size:9.4px;font-weight:500}.pk .msg.bad{background:#FEE2E2;color:#991B1B}.pk .msg.ok{background:#DCFCE7;color:#166534}.pk .empt{margin:8px 10px 44px;flex:1}'
)

WIN = (
 header(ICON, 'Quarantine and release', 'Incoming lots, location QA-01')
 + '<div class="g2"><div class="lft"><div class="lns" id="lns"></div><div class="cd his" id="his"></div></div>'
 '<div class="rgt"><div class="cd rcv"><div class="ct">Receiving</div><div class="frm"><label class="fld" id="fpo"><small>Receive against purchase order</small>'
 '<input id="ipo" value="PO-4420" readonly tabindex="-1" autocomplete="off" spellcheck="false"></label><button type="button" class="bt pri" id="rcb">Receive</button></div><div class="smp">Alder Ridge Supply, 2 lines, due today</div>'
 '</div>'
 '<div class="cd ava" id="ava"></div><div class="cd pk" id="pk"></div></div></div>'
)

JS = r'''
var FOC='.hd>*,.ln,.his,.rcv .ct,.rcv .frm>*,.ava,.pk .ct,.pk .row,.pk .pa,.pk .msg';
var NEED=[['B-2620',10204],['B-2622',10204]];
var BASE=[{id:'AP-8790',mat:'Active ingredient',g:18000,act:true,lane:'rel',po:'PO-4391',so:['JL','Oct 2, 09:15']}];
var RX=[{id:'AP-8842',mat:'Active ingredient',g:30000,act:true,po:'PO-4420',cert:[['Assay','98.0%'],['Expiry','2028-10-31'],['Retest','2027-10-31']]},{id:'EX-3312',mat:'Microcrystalline cellulose',g:150000,act:false,po:'PO-4420'}];
var LANES=[['q','Quarantine','#F59E0B'],['t','In test','#2563EB'],['rel','Released','#22C55E']];
var S;
function k3(g){return (g/1000).toLocaleString('en-US',{minimumFractionDigits:3,maximumFractionDigits:3});}
function lots(){return S.lots;}
function onhand(){return lots().filter(function(l){return l.act&&l.lane==='rel';}).reduce(function(a,l){return a+l.g;},0);}
function quar(){return lots().filter(function(l){return l.act&&l.lane!=='rel';}).reduce(function(a,l){return a+l.g;},0);}
function comm(){return NEED.reduce(function(a,n){return a+n[1];},0);}
function avail(){return onhand()-comm();}
function lot(id){for(var i=0;i<S.lots.length;i++)if(S.lots[i].id===id)return S.lots[i];}
function log(t,who,txt){S.log.push([t,who,txt]);}
function card(l){var h='<div class="lk in'+(l.id==='AP-8842'?' me':'')+'" id="k-'+l.id+'"><div class="l1"><b class="mono">'+l.id+'</b><span class="mono">'+k3(l.g)+' kg</span></div><small>'+l.mat+'</small><small>'+(l.lane==='rel'&&!l.po.match(/4420/)?'Released stock, '+l.po:'QA-01, '+l.po)+'</small>';
var chip=l.lane==='q'?'<span class="ch c-warn">Quarantine</span>':l.lane==='t'?'<span class="ch c-info">In test, quarantined</span>':'<span class="ch c-ok">Released</span>';h+=chip;
if(l.lane==='t'||(l.lane==='rel'&&l.cert)){if(l.cert)h+='<div class="cert"><span class="ct2">Certificate attached</span>'+l.cert.map(function(c){return '<span>'+c[0]+'</span><span>'+c[1]+'</span>';}).join('')+'</div>';else h+='<div class="cert"><span class="ct2" style="color:#71717A!important">Identity test running</span></div>';}
if(l.id==='AP-8842'&&l.lane==='t'){h+=S.rev?'<div class="so"><span class="av2">JL</span><span>Sign as JL<br>Nov 16, 10:42</span><button type="button" class="bt pri" id="sgn">Sign off</button></div>':'<button type="button" class="bt" id="rel">Release</button>';}
if(l.so)h+='<div class="so"><span class="av2 g">'+l.so[0]+'</span><span>Signed off<br>'+l.so[1]+'</span></div>';
return h+'</div>';}
function render(){
var h='';LANES.forEach(function(L){var ls=S.got?lots().filter(function(l){return l.lane===L[0];}):[];
h+='<div class="ln" id="ln-'+L[0]+'"><div class="lh"><i style="background:'+L[2]+'"></i>'+L[1]+'<span class="ch c-idle">'+ls.length+'</span></div><div class="lb">'+(ls.length?ls.map(card).join(''):'<div class="le">'+(S.got?'No lots here':'Receive an order to see its lots')+'</div>')+
(L[0]==='q'&&S.got&&!S.test?'<button type="button" class="bt" id="tst" style="align-self:flex-start;font-size:9.4px">Sample and send to test</button>':'')+'</div>'+
'<div class="lf">'+(S.got?'Total<span class="mono">'+k3(ls.reduce(function(a,l){return a+l.g;},0))+' kg</span>':'Empty')+'</div></div>';});
$('lns').innerHTML=h;
var g='<div class="ct"><span>Lot history</span>'+(S.log.length?'<span class="ch c-idle">'+S.log.length+' entries</span>':'')+'</div>';
g+=S.log.length?S.log.slice(-5).map(function(e){return '<div class="row in"><span class="mono">'+e[0]+'</span>'+(e[1]?'<span class="av2 g">'+e[1]+'</span>':'<span class="av2 g">SY</span>')+'<span>'+e[2]+'</span></div>';}).join(''):'<div class="empt"><b>No activity yet</b><span>Receipts, tests, blocked picks and sign offs are logged here with time and initials.</span></div>';
$('his').innerHTML=g;
var a='<div class="ct"><span>Active ingredient</span>'+(S.got?(avail()<0?'<span class="ch c-bad" id="shc">Shortage</span>':'<span class="ch c-ok" id="shc">Covered</span>'):'')+'</div>';
var v=function(x){return S.got?k3(x)+' kg':'';};
a+='<div class="row"><span>Released on hand</span><span id="aoh">'+v(onhand())+'</span></div><div class="row"><span>Quarantined, not usable</span><span id="aqu">'+v(quar())+'</span></div>'+
'<div class="row t"><span>Committed</span><span id="acm">'+v(comm())+'</span></div>'+NEED.map(function(n){return '<div class="row s"><span>'+n[0]+'</span><span>'+v(n[1])+'</span></div>';}).join('')+
'<div class="abx'+(S.got?(avail()<0?' bad':' ok'):'')+'"><small>Available</small><b id="aav">'+v(avail())+'</b><small id="asm">'+(S.got?(avail()<0?'Shortage of '+k3(-avail())+' kg':'Shortage cleared'):'On hand less committed')+'</small></div>';
$('ava').innerHTML=a;
var p='<div class="ct"><span>Pick list B-2620</span>'+(S.got?'<span class="ch c-idle">Open</span>':'')+'</div>';
if(!S.got)p+='<div class="empt"><b>No picks yet</b><span>Picks check the lot status before material leaves.</span></div>';
else{p+='<div class="row"><span>Active ingredient</span><span>'+k3(NEED[0][1])+' kg</span></div><div class="row"><span>Lot</span><span>AP-8842</span></div>';
var r=lot('AP-8842').lane==='rel';p+='<div class="pa">'+(r?'<button type="button" class="bt done" disabled>Ready to pick</button>':'<button type="button" class="bt" id="pkb">Pick AP-8842</button>')+'</div>';
if(S.blk&&!r)p+='<div class="msg bad in" id="pmsg">Lot is in quarantine</div>';else if(r)p+='<div class="msg ok in" id="pmsg">Released, pick allowed</div>';}
$('pk').innerHTML=p;
}
function resetState(){S={got:false,test:false,blk:false,rev:false,lots:BASE.map(function(l){var o={};for(var k in l)o[k]=l[k];return o;}),log:[]};render();}
var ST=[
{id:'rcv',target:function(){return $('rcb');},prompt:'Click Receive for PO-4420',where:'below',
 run:function(quick){var go=function(){S.got=true;RX.forEach(function(l){var o={};for(var k in l)o[k]=l[k];o.lane='q';S.lots.push(o);});
 log('10:05','SR','Received PO-4420 into QA-01: AP-8842 '+k3(30000)+' kg, EX-3312 '+k3(150000)+' kg');render();};go();},
 after:function(){return['Received lots wait in quarantine','Two lots in QA-01. Available active ingredient is '+k3(avail())+' kg, a shortage of '+k3(-avail())+' kg.'];}},
{id:'tst',target:function(){return $('tst');},prompt:'Send both lots to test',where:'below',run:function(){S.test=true;S.lots.forEach(function(l){if(l.lane==='q')l.lane='t';});log('10:12','TB','Sampled both lots, certificate attached to AP-8842');render();},
 after:function(){return['The certificate rides with the lot','AP-8842: assay 98.0%, expiry 2028-10-31, retest 2027-10-31.'];}},
{id:'pk',target:function(){return $('pkb');},prompt:'Try to pick AP-8842 for B-2620',where:'below',run:function(){S.blk=true;log('10:20','','Pick of AP-8842 for B-2620 blocked, lot is in quarantine');render();},
 after:function(){return['Untested material cannot be picked','Lot is in quarantine. Available stays at '+k3(avail())+' kg.'];}},
{id:'rel',target:function(){return $('rel');},prompt:'Release AP-8842',where:'below',run:function(){S.rev=true;render();},
 after:function(){return['A release needs a named sign off','Initials and time go on the record: JL, Nov 16, 10:42.'];}},
{id:'sgn',target:function(){return $('sgn');},prompt:'Sign off the release',where:'below',run:function(){var l=lot('AP-8842');l.lane='rel';l.so=['JL','Nov 16, 10:42'];S.rev=false;log('10:42','JL','Released AP-8842, signed off');render();},
 after:function(){return['Released stock counts at once',k3(onhand())+' kg on hand, '+k3(comm())+' kg committed, '+k3(avail())+' kg available.'];}}];
'''
