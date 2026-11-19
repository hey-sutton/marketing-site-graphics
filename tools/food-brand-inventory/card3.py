"""Food brand inventory card 3: Shelf Life & Retailer Dating. Layout: a board.
Top: the order bar with the read only account and minimum remaining life fields and Apply. Below, three columns the
lots move between by click: Lots on hand (ranked FIFO by received date or FEFO by best before, with a remaining life bar
and the 120 day line), the pick list for the order, and On hold. Remaining days are computed from the best before
dates and the delivery date, so the ranking, the qualifying test and the pick come from the data."""
from frame_auto import header

SUMMARY = 'Shelf Life & Retailer Dating (rank lots FEFO, apply the Greenfield Grocers 120 day rule, see which lots qualify, flag short dated lots, hold LOT-B and the pick moves to LOT-C)'
ARIA = 'Interactive product screen: rank four lots by best before date, apply the account minimum of 120 days remaining life, see which lots qualify, flag the short dated lots and hold a lot so the pick list moves to the next qualifying lot'
STEPS = 5
STUDIO = dict(lede='A typical dating board on your Sutton data. Want it different? Describe the change.',
              examples=['A rule per retailer and channel', 'Days left at the store, not the dock', 'A markdown list for short lots', 'An alert before a lot turns short'],
              built_on='Lots, customers and sales orders', change='Rules, columns and views')

ICON = '<rect x="2" y="3" width="12" height="10.5" rx="1.5"/><path d="M2 6.5h12M5.5 1.8v2.4M10.5 1.8v2.4"/>'

CSS = (
 '.fld input[readonly]{background:#F4F4F5;color:#3F3F46;cursor:default;pointer-events:none}'
 '.g3{display:grid;grid-template-columns:252px 204px 180px;grid-template-rows:62px 468px;gap:10px;padding:10px 44px 0 16px}'
 '.ord{grid-column:1/4;display:flex;flex-direction:column;justify-content:center;gap:5px;padding:0 12px}.ord .frm{display:flex;align-items:flex-end;gap:8px}'
 '.ord .fld{width:190px}.ord .fld.d{width:140px}.ord .ctx{font-size:8.9px;color:#71717A}.ord .rl{margin-left:auto}'
 '.col{display:flex;flex-direction:column;min-width:0}.col .ct .bt{font-size:9.2px;padding:3px 8px}.col>.empt{margin:10px;flex:1}'
 '.seg{display:inline-flex;padding:2px;gap:2px;border:1px solid #E4E4E7;border-radius:7px;background:#FAFAFA}.seg button{font:inherit;font-size:9.2px;font-weight:500;padding:2px 8px;border:0;border-radius:5px;background:transparent;color:#52525B;cursor:pointer}.seg button.on{background:#18181B;color:#fff}.seg button:focus-visible{outline:2px solid #18181B;outline-offset:1px}'
 '.lots{display:flex;flex-direction:column;gap:7px;padding:9px}'
 '.lt{border:1px solid #E4E4E7;border-radius:7px;padding:7px 9px;background:#fff;display:flex;flex-direction:column;gap:4px;transition:background-color .35s,border-color .35s,opacity .35s}'
 '.lt .l1{display:flex;align-items:center;gap:5px}.lt .l1 b{font-family:"JetBrains Mono",ui-monospace,monospace;font-size:10.4px;margin-right:auto}.lt .l2{display:flex;justify-content:space-between;font-size:9px;color:#52525B}'
 '.lt .bar{position:relative;height:6px;border-radius:3px;background:#F4F4F5}.lt .bar i{position:absolute;left:0;top:0;bottom:0;border-radius:3px;background:#A1A1AA}.lt .bar u{position:absolute;top:-3px;bottom:-3px;width:2px;background:#18181B;border-radius:1px}'
 '.lt .l3{display:flex;justify-content:space-between;font-size:8.6px;color:#71717A}.lt .l3 b{font-family:"JetBrains Mono",ui-monospace,monospace;color:#18181B;font-weight:600}'
 '.lt.q{border-color:#86EFAC;background:#F0FDF4}.lt.q .bar i{background:#22C55E}.lt.n{background:#FAFAFA;color:#71717A}.lt.n .bar i{background:#D4D4D8}.lt.n .l1 b{color:#71717A}'
 '.lt .bt{font-size:8.8px;padding:2px 7px}.c-flag{background:#FEF3C7;color:#92400E}'
 '.fbar{margin-top:auto;display:flex;align-items:center;gap:6px;padding:8px 9px;border-top:1px solid #E4E4E7;background:#FAFAFA;font-size:9px;color:#52525B}.fbar .bt{margin-left:auto;font-size:9.2px;padding:3px 8px}'
 '.pl .row{grid-template-columns:1fr 52px;font-size:9.4px;min-height:40px}.pl .row span:last-child{text-align:right;font-family:"JetBrains Mono",ui-monospace,monospace}.pl .nm small{display:block;font-size:8.4px;color:#71717A}'
 '.pl .row.t{font-weight:600;background:#FAFAFA;min-height:28px}.pl .rule{margin:9px 9px 0;padding:7px 9px;border-radius:7px;background:#E8EEFC;color:#1E3A8A;font-size:9px;line-height:1.4}'
 '.pl .nx{padding:8px 11px;font-size:8.9px;color:#71717A;line-height:1.45}'
 '.acc{margin-top:auto;border-top:1px solid #E4E4E7}.acc .sub{padding:7px 11px 3px;font-size:9px;color:#71717A;font-weight:500}.acc .row{grid-template-columns:1fr 58px;font-size:9.2px;min-height:24px}.acc .row span:last-child{text-align:right;font-family:"JetBrains Mono",ui-monospace,monospace}.acc .row.on{background:#E8EEFC;color:#1E3A8A;font-weight:600}.acc+.tot{margin-top:0}'
 '.hn{margin:0 9px;padding:7px 9px;border-radius:7px;background:#FAFAFA;border:1px solid #F0F0F1;font-size:8.9px;color:#52525B;line-height:1.45}.hl .lots{padding-top:9px}.tot{margin-top:auto;padding:9px 11px;border-top:1px solid #E4E4E7;font-size:9px;color:#52525B;line-height:1.4;background:#FAFAFA}'
)

WIN = (
 header(ICON, 'Shelf life and dating', 'Remaining life checked against each account before picking')
 + '<div class="g3"><div class="cd ord" id="ord"><div class="frm"><label class="fld"><small>Account</small>'
 '<input id="iac" value="Greenfield Grocers" readonly tabindex="-1" autocomplete="off" spellcheck="false"></label>'
 '<label class="fld d"><small>Minimum remaining life</small><input id="imr" value="120 days" readonly tabindex="-1" autocomplete="off" spellcheck="false"></label>'
 '<span id="apw"></span><span class="rl" id="rls"></span></div>'
 '<div class="ctx">Order SO-4471, Trail Mix Case, delivers Dec 1, 2026</div></div>'
 '<div class="cd col" id="c1"></div><div class="cd col pl" id="c2"></div><div class="cd col hl" id="c3"></div></div>'
)

JS = r'''
var FOC='.hd>*,.ord .fld,.ord .ctx,#apb,.col>.ct,.lt,.fbar,.pl .row,.pl .rule,.pl .nx,.col>.empt,.tot';
function U(y,m,d){return Date.UTC(y,m-1,d);}
var DEL=U(2026,12,1),MIN=120,NEED=800,SO='SO-4471';
var LOTS=[{id:'LOT-A',bb:U(2027,3,6),rc:U(2026,9,22),q:600},{id:'LOT-B',bb:U(2027,4,20),rc:U(2026,10,6),q:800},{id:'LOT-C',bb:U(2027,5,30),rc:U(2026,9,8),q:1000},{id:'LOT-D',bb:U(2027,3,21),rc:U(2026,10,20),q:400}];
var ACC=[['Greenfield Grocers',MIN],['Northway Markets',90],['Pine Street Co-op',60]];
var S;
function dl(l){return Math.round((l.bb-DEL)/864e5);}
function fd(t){return new Date(t).toLocaleDateString('en-US',{month:'short',day:'numeric',year:'numeric',timeZone:'UTC'});}
function fs(t){return new Date(t).toLocaleDateString('en-US',{month:'short',day:'numeric',timeZone:'UTC'});}
function ranked(fefo){return LOTS.slice().sort(function(a,b){return fefo?a.bb-b.bb:a.rc-b.rc;});}
function ok(l){return dl(l)>=MIN;}
function pick(){var need=NEED,out=[];ranked(true).forEach(function(l){if(!ok(l)||l.id===S.hold||need<=0)return;var t=Math.min(need,l.q);need-=t;out.push([l,t]);});return out;}
function card(l,inHold){var q=S.chk&&ok(l),n=S.chk&&!ok(l),w=Math.min(100,dl(l)/200*100);
return '<div class="lt in'+(q&&!inHold?' q':'')+(n||inHold?' n':'')+'" id="l-'+l.id+'"><div class="l1"><b>'+l.id+'</b>'+(S.flag&&!ok(l)?'<span class="ch c-flag" id="fl-'+l.id+'">Short dated</span>':'')+
(inHold?'<span class="ch c-bad">On hold</span>':S.chk?(q?'<span class="ch c-ok">Qualifies</span>':'<span class="ch c-idle">Below '+MIN+'</span>'):'')+
(S.chk&&q&&!inHold?'<button type="button" class="bt" id="h-'+l.id+'">Hold</button>':'')+'</div>'+
'<div class="l2"><span>Best before '+(inHold?fs(l.bb):fd(l.bb))+'</span><span>'+n0(l.q)+' cases</span></div>'+
'<div class="bar"><i style="width:'+w.toFixed(1)+'%"></i>'+(S.rule?'<u style="left:'+(MIN/200*100)+'%"></u>':'')+'</div>'+
(inHold?'<div class="l3"><span><b>'+dl(l)+'</b> days at delivery</span></div></div>':'<div class="l3"><span>Received '+fs(l.rc)+'</span><span><b id="d-'+l.id+'">'+dl(l)+'</b> days at delivery</span></div></div>');}
function render(){
$('apw').innerHTML=S.rule?'<button type="button" class="bt done" disabled>Applied</button>':'<button type="button" class="bt pri" id="apb">Apply</button>';
$('rls').innerHTML=S.rule?'<span class="ch c-info in" id="rch">Rule on '+SO+': '+MIN+' days or more</span>':'';
var r=ranked(S.fefo).filter(function(l){return l.id!==S.hold;});
var c='<div class="ct"><span>Lots on hand</span><span class="seg" role="group" aria-label="Ranking"><button type="button" id="fifo" class="'+(S.fefo?'':'on')+'" aria-pressed="'+(S.fefo?'false':'true')+'">FIFO</button><button type="button" id="fefo" class="'+(S.fefo?'on':'')+'" aria-pressed="'+(S.fefo?'true':'false')+'">FEFO</button></span></div>'+
'<div class="lots" id="rank">'+r.map(function(l){return card(l,false);}).join('')+'</div>'+
'<div class="fbar"><span>'+(S.fefo?'By best before date':'By received date')+'. Next shipment '+fs(DEL)+'.</span>'+(S.flag?'<span class="ch c-flag">'+LOTS.filter(function(l){return !ok(l);}).length+' flagged</span>':'<button type="button" class="bt" id="flb">Flag</button>')+'</div>';
$('c1').innerHTML=c;
var p='<div class="ct"><span>Pick list <span class="mono mut">'+SO+'</span></span>'+(S.chk?'<span class="ch c-ok">Ready</span>':'<button type="button" class="bt" id="ckb">Check lots</button>')+'</div>';
if(S.rule)p+='<div class="rule in">Greenfield Grocers takes lots with '+MIN+' days or more of remaining life at delivery.</div>';
if(!S.chk)p+='<div class="empt"><b>No lots picked yet</b><span>'+(S.rule?'Check the lots against the rule to build the pick list.':'Apply the account rule, then check the lots to build the pick list.')+'</span></div>';
else{var pk=pick();p+='<div class="in" style="margin-top:9px">'+pk.map(function(x,i){return '<div class="row" id="p-'+i+'"><span class="nm"><b class="mono">'+x[0].id+'</b><small>'+dl(x[0])+' days, best before '+fs(x[0].bb)+'</small></span><span id="pq-'+i+'">'+n0(x[1])+'</span></div>';}).join('')+
'<div class="row t"><span>Order '+SO+'</span><span id="pqt">'+n0(pk.reduce(function(a,x){return a+x[1];},0))+'</span></div></div>'+
'<div class="nx" id="pnx">Qualifying, FEFO: '+ranked(true).filter(function(l){return ok(l);}).map(function(l){return l.id+(l.id===S.hold?' (held)':'');}).join(', ')+'. Not accepted: '+ranked(true).filter(function(l){return !ok(l);}).map(function(l){return l.id;}).join(', ')+'.</div>';}
p+='<div class="acc"><div class="sub">Account minimums at delivery</div>'+ACC.map(function(a){return '<div class="row'+(S.rule&&a[0]===ACC[0][0]?' on':'')+'"><span>'+a[0]+'</span><span>'+a[1]+' days</span></div>';}).join('')+'</div><div class="tot">Only lots the account accepts reach the pick list.</div>';
$('c2').innerHTML=p;
var h='<div class="ct"><span>On hold</span>'+(S.hold?'<span class="ch c-bad">1 lot</span>':'')+'</div>';
h+=S.hold?'<div class="lots">'+card(LOTS.filter(function(l){return l.id===S.hold;})[0],true)+'</div><div class="hn in">Held Nov 19 for a seal check. Release puts '+S.hold+' back in the FEFO line.</div>':'<div class="empt"><b>Nothing on hold</b><span>A held lot moves here and stays out of picking.</span></div>';
h+='<div class="tot">Held lots keep their dates.</div>';
$('c3').innerHTML=h;
}
function resetState(){S={fefo:false,rule:false,chk:false,flag:false,hold:null};render();}
function capN(){var i=cap.querySelector('.m i');return i?+i.textContent:1;}
var CAPAT=function(hh){var w=cap.offsetWidth;return capN()===3?{l:visW()-w-14,t:118}:{l:visW()-w-14,t:visH()-hh-14};};
var ST=[
{id:'fefo',target:function(){return $('fefo');},prompt:'Rank the lots FEFO',where:'below',run:function(){S.fefo=true;render();},
 after:function(){return['Lots ranked by best before date','FEFO: '+ranked(true).map(function(l){return l.id;}).join(', ')+'. By received date it was '+ranked(false).map(function(l){return l.id;}).join(', ')+'.'];}},
{id:'rule',target:function(){return $('apb');},prompt:'Apply the 120 day rule',where:'below',run:function(){S.rule=true;render();},
 after:function(){return['The account minimum goes on the order','Greenfield Grocers needs '+MIN+' days or more at delivery on '+fs(DEL)+'.'];}},
{id:'chk',target:function(){return $('ckb');},prompt:'Check the lots',where:'below',run:function(){S.chk=true;render();},
 after:function(){var q=ranked(true).filter(ok),n=ranked(true).filter(function(l){return !ok(l);});return['Only lots the retailer will accept',q.map(function(l){return l.id+' '+dl(l);}).join(' and ')+' days qualify. '+n.map(function(l){return l.id+' '+dl(l);}).join(' and ')+' do not. First pick '+pick()[0][0].id+'.'];}},
{id:'flag',target:function(){return $('flb');},prompt:'Flag short dated lots',where:'above',run:function(){S.flag=true;render();},
 after:function(){return['Short dated lots carry a flag',LOTS.filter(function(l){return !ok(l);}).map(function(l){return l.id;}).sort().join(' and ')+' fall under '+MIN+' days before the '+fs(DEL)+' shipment.'];}},
{id:'hold',target:function(){return $('h-LOT-B');},prompt:'Hold LOT-B',where:'below',run:function(){S.hold='LOT-B';render();},
 after:function(){var p=pick()[0];return['A held lot leaves the pick list','LOT-B moves to On hold. The pick list takes '+n0(p[1])+' cases from '+p[0].id+'.'];}}];
'''
