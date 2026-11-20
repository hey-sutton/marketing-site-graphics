"""Nut processing card 1: Raw Intake & Grade Records. Layout: a record form with a side summary panel.
Left: the read only truckload field with Receive truckload, then the truckload record (origin and grower, the scale
ticket, the grade at the scale with read only moisture and size fields, the lab result) and an Incoming lots tab.
Right: the lot summary (net weight, status, checks), the next truckload at the dock with its read only moisture
reading, and the put away list. A lot is held only when its moisture is above the 6.0 percent maximum, and a held
lot never counts toward put away."""
from frame_auto import header

SUMMARY = 'Raw Intake & Grade Records (receive truckload NP-0711 of almonds from Harlan Orchards, 42,000 minus 14,000 = 28,000 lb net, moisture 5.2 against a 6.0 maximum, attach the lab result, NP-0712 at 7.1 is held at the dock, incoming lots by grade and supplier)'
ARIA = 'Interactive product screen: receive a truckload with its origin and grower, record moisture and size grade at the scale, attach a lab result to the lot, hold a lot that is outside its moisture spec and see incoming lots by grade and supplier'
STEPS = 5
STUDIO = dict(lede='A typical receiving screen on your Sutton data. Want it different? Describe the change.',
              examples=['Spec limits by variety', 'A photo of each sample', 'Grower statements by crop year', 'A text when a lot is held'],
              built_on='Lots, suppliers, items and quality checks', change='Fields, limits and views')

ICON = '<path d="M1.5 4.5h8v6h-8zM9.5 6.5h3l2 2v2h-5"/><circle cx="4" cy="11.5" r="1.3"/><circle cx="12" cy="11.5" r="1.3"/>'

CSS = (
 '.fld input[readonly]{background:#F4F4F5;color:#3F3F46;cursor:default;pointer-events:none}'
 '.g1{display:grid;grid-template-columns:420px 226px;grid-template-rows:62px 468px;gap:10px;padding:10px 44px 0 16px}'
 '.bf{display:flex;flex-direction:column;justify-content:center;gap:5px;padding:0 12px}.bf .frm{display:flex;align-items:flex-end;gap:8px}.bf .fld{width:150px}.bf .ctx{font-size:8.9px;color:#71717A}.bf .frm .rt{margin-left:auto}'
 '.rc{display:flex;flex-direction:column}.rc>.empt{margin:10px;flex:1}.rc .ct{padding:0 11px 0 4px}.rc .ct .tabs{border:0;height:30px;padding:0 8px;gap:14px}.rc .tab:disabled{color:#A1A1AA;cursor:default}'
 '.sec{padding:7px 11px 0}.sec+.sec{border-top:1px solid #F0F0F1;margin-top:7px}.sec h4{margin:0 0 5px;font-size:9.6px;font-weight:600;display:flex;align-items:center;justify-content:space-between;gap:6px}'
 '.kg{display:grid;grid-template-columns:1.15fr 1fr 1fr;gap:6px 10px}.kg .kv b{font-size:9.8px}.kg .kv b.mono{font-size:9.6px}'
 '.wt{display:grid;grid-template-columns:1fr 1fr 1fr 1.3fr;gap:8px;align-items:end}.wt .kv b{font-family:"JetBrains Mono",ui-monospace,monospace;font-size:11.5px}'
 '.calc{padding:4px 7px;border-radius:6px;background:#FAFAFA;border:1px solid #F0F0F1;font-family:"JetBrains Mono",ui-monospace,monospace;font-size:9px;text-align:center;white-space:nowrap}'
 '.qf{display:flex;align-items:flex-end;gap:8px}.qf .fld{width:84px}.qf .rt{margin-left:auto}'
 '.mb{margin-top:7px}.mb .tk{position:relative;height:11px;border-radius:4px;background:#F4F4F5}.mb .fl{position:absolute;left:0;top:0;bottom:0;border-radius:4px;background:#16A34A;transition:width .5s cubic-bezier(.22,.9,.28,1)}.mb .fl.bad{background:#DC2626}'
 '.mb .mk{position:absolute;top:-3px;bottom:-3px;width:2px;background:#18181B}.mb .lb{display:flex;justify-content:space-between;font-size:8.2px;color:#71717A;margin-top:3px;font-family:"JetBrains Mono",ui-monospace,monospace}'
 '.lab{display:grid;grid-template-columns:1fr 1fr 1fr;gap:6px;margin-top:6px}.lab div{border:1px solid #BBF7D0;background:#F0FDF4;border-radius:7px;padding:5px 7px;font-size:8.6px;color:#166534}.lab div b{display:block;color:#18181B;font-size:9.4px;font-weight:600}'
 '.lph{margin-top:6px;border:1px dashed #E4E4E7;border-radius:7px;background:#FAFAFA;padding:8px;font-size:8.8px;color:#A1A1AA;text-align:center}'
 '.il .row{grid-template-columns:62px 1fr 52px 56px 60px;font-size:9.2px;min-height:30px}.il .row>span:nth-child(3),.il .row>span:nth-child(4){text-align:right;font-family:"JetBrains Mono",ui-monospace,monospace}.il .row.h>span{font-family:inherit!important}.il .row>span:last-child{text-align:right}'
 '.il .row small{display:block;font-size:8.2px;color:#71717A}.il .gr{display:flex;justify-content:space-between;align-items:center;padding:6px 11px;background:#FAFAFA;border-top:1px solid #E4E4E7;font-size:9.2px;font-weight:600}.il .gr span:last-child{font-family:"JetBrains Mono",ui-monospace,monospace;font-weight:500;color:#52525B}'
 '.il .row.hd2{background:#FEF2F2}.ilsum{margin:10px 11px 0;display:grid;grid-template-columns:1fr 1fr;gap:8px}.ilsum div{border:1px solid #E4E4E7;border-radius:8px;padding:7px 9px}.ilsum div.w{border-color:#FECACA;background:#FEF2F2}.ilsum small{display:block;font-size:8.4px;color:#71717A}.ilsum b{font-family:"JetBrains Mono",ui-monospace,monospace;font-size:13px}'
 '.bs{margin:12px 11px 0;border:1px solid #E4E4E7;border-radius:8px;padding:8px 10px;display:flex;flex-direction:column;gap:7px}.bs .lb{display:flex;justify-content:space-between;font-size:9.4px;font-weight:600}.bs .lb .mono{font-weight:500;color:#52525B}'
 '.sr2{display:grid;grid-template-columns:110px 1fr 44px;gap:8px;align-items:center;font-size:9px}.sr2 .mono{text-align:right}.sr2 .bar{height:10px;border-radius:3px;background:#F4F4F5;overflow:hidden}.sr2 .bar i{display:block;height:100%;background:#18181B;border-radius:3px}.sr2 .bar i.bad{background:#DC2626}'
 '.tot{margin-top:auto;padding:9px 11px;border-top:1px solid #E4E4E7;font-size:9.1px;color:#52525B;line-height:1.4;background:#FAFAFA}.sm .tot{padding-right:90px}'
 '.sm{grid-column:2;grid-row:1/3;display:flex;flex-direction:column}.sm>.empt{margin:10px;flex:1}'
 '.sm .bx{padding:10px 11px 0;display:flex;justify-content:space-between;align-items:flex-end}.sm .big{font-size:22px}'
 '.chk{padding:8px 11px 0;display:flex;flex-direction:column;gap:4px}.chk div{display:flex;align-items:center;justify-content:space-between;font-size:9.1px;color:#3F3F46}'
 '.dk{margin:9px 11px 0;padding:7px 8px;border:1px solid #E4E4E7;border-radius:8px;display:flex;flex-direction:column;gap:5px}.dk .t1{display:flex;justify-content:space-between;align-items:center;font-size:9.4px;font-weight:600}.dk .ctx{font-size:8.5px;color:#71717A;line-height:1.35}'
 '.dk .qf .fld{width:70px}.dk.held{border-color:#FCA5A5;background:#FEF2F2;box-shadow:inset 3px 0 0 #DC2626}'
 '.note{margin:8px 11px 0;padding:6px 8px;border-radius:7px;font-size:8.9px;line-height:1.45;background:#FAFAFA;border:1px solid #F0F0F1;color:#52525B}.note.w{background:#FEF2F2;border-color:#FECACA;color:#991B1B}.note.g{background:#F0FDF4;border-color:#BBF7D0;color:#166534}'
 '.pa{margin:9px 11px 0}.pa .lb{display:flex;justify-content:space-between;font-size:9.2px;font-weight:600;margin-bottom:4px}.pa .row{grid-template-columns:1fr 54px 42px;font-size:9px;min-height:24px;padding:0 4px}.pa .row span:nth-child(2){text-align:right;font-family:"JetBrains Mono",ui-monospace,monospace}.pa .row span:last-child{text-align:right}'
 '.pa .row.x{color:#A1A1AA;text-decoration:line-through}.pa .row.x span:last-child{text-decoration:none}.pa .sum{display:flex;justify-content:space-between;font-size:9.2px;font-weight:600;padding:5px 4px 0;border-top:1px solid #E4E4E7;margin-top:2px}.pa .sum b{font-family:"JetBrains Mono",ui-monospace,monospace}'
)

WIN = (
 header(ICON, 'Raw intake', 'Truckloads, grade and lab records by lot')
 + '<div class="g1"><div class="cd bf"><div class="frm"><label class="fld"><small>Truckload</small>'
 '<input id="itk" value="NP-0711" readonly tabindex="-1" autocomplete="off" spellcheck="false"></label>'
 '<button type="button" class="bt pri" id="rcv">Receive truckload</button><span class="rt" id="rst"></span></div><div class="ctx">In shell almonds at scale 1, arrived 7:42 am</div></div>'
 '<div class="cd rc" id="rc"></div><div class="cd sm" id="sm"></div></div>'
)

JS = r'''
var FOC='.hd>*,.bf .fld,.bf .ctx,#rcv,.rc .ct,.rc .sec,.rc .il,.rc .ilsum,.rc .tot,.sm>*';
var MI=String.fromCharCode(8722),SPEC=6.0;
var TK={NP0711:{id:'NP-0711',lot:'L-0711',gr:'Harlan Orchards',org:'Merced County, block 14',grade:'Nonpareil 23/25',gross:42000,tare:14000,m:5.2,st:'ST-5521',lab:'VAL-3318'},
NP0712:{id:'NP-0712',lot:'L-0712',gr:'Tule Bend Farms',grade:'Carmel 25/27',gross:40500,tare:13800,m:7.1},
NP0709:{id:'NP-0709',lot:'L-0709',gr:'Delmar Ranch',grade:'Nonpareil 23/25',gross:38200,tare:13800,m:5.6}};
function net(t){return t.gross-t.tare;}
function held(t){return t.m>SPEC;}
var S;
function lotsIn(){var a=[TK.NP0709];if(S.rc)a.push(TK.NP0711);if(S.hm)a.push(TK.NP0712);return a;}
function ready(t){return t===TK.NP0711?S.lab&&!held(t):t===TK.NP0712?(S.hm&&!held(t)):!held(t);}
function putAway(){return lotsIn().filter(ready);}
function render(){
var A=TK.NP0711,B=TK.NP0712;
$('rcv').className='bt '+(S.rc?'done':'pri');$('rcv').textContent=S.rc?'Received':'Receive truckload';
$('rst').innerHTML=!S.rc?'':S.lab?'<span class="ch c-ok" id="lst">Accepted</span>':'<span class="ch c-warn" id="lst">Grading</span>';
var r='<div class="ct"><div class="tabs" role="tablist"><button type="button" class="tab'+(S.view==='rec'?' on':'')+'" id="t-rec"'+(S.rc?'':' disabled')+'>Truckload record</button><button type="button" class="tab'+(S.view==='inc'?' on':'')+'" id="t-inc"'+(S.rc?'':' disabled')+'>Incoming lots</button></div>'+(S.rc?'<span class="ch c-idle mono">'+A.lot+'</span>':'')+'</div>';
if(!S.rc)r+='<div class="empt"><b>No truckload open</b><span>Receive a truckload to start its lot record: origin, grower, scale ticket, grade and lab results.</span></div>';
else if(S.view==='rec'){
r+='<div class="sec in"><h4><span>Origin and grower</span><span class="ch c-idle">Crop year 2026</span></h4><div class="kg"><div class="kv"><small>Grower</small><b id="rgr">'+A.gr+'</b></div><div class="kv"><small>Origin</small><b>'+A.org+'</b></div><div class="kv"><small>Variety and grade</small><b id="rgd">'+A.grade+'</b></div>'+
'<div class="kv"><small>Lot</small><b class="mono">'+A.lot+'</b></div><div class="kv"><small>Product</small><b>Almonds, in shell</b></div><div class="kv"><small>Received</small><b>Oct 28, 7:42 am</b></div></div></div>';
r+='<div class="sec in"><h4><span>Scale ticket '+A.st+'</span><span class="ch c-ok">Weighed</span></h4><div class="wt"><div class="kv"><small>Gross, lb</small><b id="wgr">'+n0(A.gross)+'</b></div><div class="kv"><small>Tare, lb</small><b id="wta">'+n0(A.tare)+'</b></div><div class="kv"><small>Net, lb</small><b id="wnt">'+n0(net(A))+'</b></div><div class="calc" id="wcal">'+n0(A.gross)+' '+MI+' '+n0(A.tare)+' = '+n0(net(A))+'</div></div></div>';
r+='<div class="sec in"><h4><span>Grade at the scale</span>'+(S.mo?'<span class="ch c-ok" id="mst">Within spec</span>':'<span class="ch c-idle">Not recorded</span>')+'</h4><div class="qf"><label class="fld"><small>Moisture %</small><input id="imo" value="5.2" readonly tabindex="-1"></label><label class="fld"><small>Size grade</small><input id="isz" value="23/25" readonly tabindex="-1"></label>'+
'<button type="button" class="bt '+(S.mo?'done':'pri')+'" id="rmb">'+(S.mo?'Recorded':'Record moisture')+'</button><span class="rt mut" style="font-size:8.6px">Spec max '+SPEC.toFixed(1)+'%</span></div>'+
(S.mo?'<div class="mb in"><div class="tk"><div class="fl" style="width:'+(A.m/8*100).toFixed(1)+'%"></div><div class="mk" style="left:'+(SPEC/8*100).toFixed(1)+'%"></div></div><div class="lb"><span>0%</span><span id="mrd">'+A.m.toFixed(1)+'% read</span><span>'+SPEC.toFixed(1)+'% max</span><span>8%</span></div></div>':'<div class="lph">Moisture and size grade show here once recorded.</div>')+'</div>';
r+='<div class="sec in"><h4><span>Lab result</span>'+(S.lab?'<span class="ch c-ok">Attached</span>':'<span class="ch c-idle">None attached</span>')+'</h4><div class="qf"><label class="fld" style="width:110px"><small>Lab report</small><input id="ilb" value="'+A.lab+'" readonly tabindex="-1"></label><span class="mut" style="font-size:8.6px;padding-bottom:6px">Valley Ag Labs, sample from bin 3</span>'+
'<button type="button" class="bt '+(S.lab?'done':'pri')+' rt" id="atb"'+(S.mo?'':' disabled')+'>'+(S.lab?'Attached':'Attach result')+'</button></div>'+
(S.lab?'<div class="lab in" id="lbr"><div><b>Aflatoxin</b>Not detected</div><div><b>Salmonella</b>Negative</div><div><b>Insect damage</b>0.4%, under 1.0%</div></div>':'<div class="lph">Attach the lab report to keep it on the lot.</div>')+'</div>';
r+='<div class="tot">Net is gross minus tare on the scale ticket. Every reading stays on lot '+A.lot+'.</div>';}
else{var G={};lotsIn().forEach(function(t){(G[t.grade]=G[t.grade]||[]).push(t);});
r+='<div class="il in" id="il"><div class="row h"><span>Truckload</span><span>Supplier</span><span>Net, lb</span><span>Moisture</span><span>Status</span></div>'+
Object.keys(G).sort().reverse().map(function(g){return '<div class="gr"><span>'+g+'</span><span>'+G[g].length+(G[g].length>1?' lots':' lot')+'</span></div>'+G[g].map(function(t){var h=held(t);return '<div class="row'+(h?' hd2':'')+'" id="i-'+t.id+'"><span class="mono"><b>'+t.id+'</b></span><span>'+t.gr+'<small>'+t.lot+'</small></span><span>'+n0(net(t))+'</span><span>'+t.m.toFixed(1)+'%</span><span><span class="ch '+(h?'c-bad':'c-ok')+'">'+(h?'Held':'Accepted')+'</span></span></div>';}).join('');}).join('')+'</div>';
var P=putAway(),H=lotsIn().filter(held);
r+='<div class="ilsum in"><div><small>To put away</small><b id="ipa">'+n0(P.reduce(function(a,t){return a+net(t);},0))+' lb</b><small>'+P.length+' lots</small></div><div class="w"><small>Held at the dock</small><b id="iho">'+n0(H.reduce(function(a,t){return a+net(t);},0))+' lb</b><small>'+H.map(function(t){return t.id;}).join(', ')+', not put away</small></div></div>';
var L=lotsIn(),TT=L.reduce(function(a,t){return a+net(t);},0);
r+='<div class="bs in" id="bs"><div class="lb"><span>By supplier</span><span class="mono" id="itot">'+n0(TT)+' lb in</span></div>'+L.slice().sort(function(a,b){return a.gr<b.gr?-1:1;}).map(function(t){var h=held(t);return '<div class="sr2"><span>'+t.gr+'</span><span class="bar"><i class="'+(h?'bad':'')+'" style="width:'+(net(t)/TT*100).toFixed(1)+'%"></i></span><span class="mono">'+(net(t)/TT*100).toFixed(1)+'%</span></div>';}).join('')+'</div>';
r+='<div class="tot">'+L.length+' lots in today, grouped by grade with the supplier on each.</div>';}
$('rc').innerHTML=r;
var m='<div class="ct"><span>Lot summary</span>'+(S.rc?'<span class="ch c-idle mono">'+A.lot+'</span>':'')+'</div>';
if(!S.rc)m+='<div class="empt"><b>Nothing received yet</b><span>Net weight, grade checks and put away show here.</span></div>';
else{m+='<div class="bx in"><div class="kv"><small>Net weight, lb</small><b class="big mono" id="snt">'+n0(net(A))+'</b></div>'+(S.lab?'<span class="ch c-ok">Accepted</span>':'<span class="ch c-warn">Grading</span>')+'</div>'+
'<div class="chk in"><div><span>Scale ticket</span><span class="ch c-ok">Done</span></div><div><span>Moisture and size</span><span class="ch '+(S.mo?'c-ok':'c-idle')+'">'+(S.mo?A.m.toFixed(1)+'%, 23/25':'Open')+'</span></div><div><span>Lab result</span><span class="ch '+(S.lab?'c-ok':'c-idle')+'">'+(S.lab?A.lab:'Open')+'</span></div></div>';
m+='<div class="dk in'+(S.hm?' held':'')+'" id="dk"><div class="t1"><span>Next at the dock</span><span class="mono">'+B.id+'</span></div><div class="ctx">'+B.gr+', '+B.grade+', scale 2</div>'+
'<div class="qf"><label class="fld"><small>Moisture %</small><input id="ibm" value="7.1" readonly tabindex="-1"></label><button type="button" class="bt '+(S.hm?'done':'pri')+'" id="hmb">'+(S.hm?'Recorded':'Record')+'</button>'+(S.hm?'<span class="ch c-bad rt" id="hst">Held</span>':'')+'</div></div>';
if(S.hm)m+='<div class="note w in" id="hnt">Held at the dock: '+B.m.toFixed(1)+'% is above the '+SPEC.toFixed(1)+'% maximum. Put away is blocked for '+B.lot+'.</div>';
var P2=putAway();
m+='<div class="pa in" id="pa"><div class="lb"><span>Put away</span><span class="ch c-idle">Silo bay 3</span></div>'+lotsIn().map(function(t){var ok=ready(t),h=held(t);return '<div class="row'+(h?' x':'')+'" id="p-'+t.id+'"><span class="mono">'+t.id+'</span><span>'+n0(net(t))+'</span><span><span class="ch '+(ok?'c-ok':h?'c-bad':'c-idle')+'">'+(ok?'Ready':h?'Held':'Open')+'</span></span></div>';}).join('')+
'<div class="sum"><span>Ready, lb</span><b id="ptot">'+n0(P2.reduce(function(a,t){return a+net(t);},0))+'</b></div></div>';}
m+='<div class="tot">Lots out of spec stay at the dock.</div>';
$('sm').innerHTML=m;
}
function resetState(){S={rc:false,mo:false,lab:false,hm:false,view:'rec'};render();}
var ST=[
{id:'rc',target:function(){return $('rcv');},prompt:'Receive truckload NP-0711',where:'below',run:function(){S.rc=true;S.view='rec';render();},
 after:function(){var A=TK.NP0711;return['A truckload with its origin and grower',A.gr+', '+A.grade+': '+n0(A.gross)+' gross '+MI+' '+n0(A.tare)+' tare = '+n0(net(A))+' lb net on lot '+A.lot+'.'];}},
{id:'mo',target:function(){return $('rmb');},prompt:'Record moisture and size grade',where:'below',run:function(){S.rc=true;S.view='rec';S.mo=true;render();},
 after:function(){return['Moisture and size grade at the scale','5.2% moisture against the 6.0% maximum, size 23/25: within spec.'];}},
{id:'lab',target:function(){return $('atb');},prompt:'Attach the lab result',where:'above',run:function(){S.view='rec';S.lab=true;render();},
 after:function(){return['A lab result on the lot','VAL-3318 is attached to L-0711 and the lot is accepted for put away.'];}},
{id:'hm',target:function(){return $('hmb');},prompt:'Record moisture for NP-0712',where:'below',run:function(){S.hm=true;render();},
 after:function(){return['A lot outside its spec is held','NP-0712 reads 7.1%, above the 6.0% maximum, so it stays at the dock and is left out of put away.'];}},
{id:'inc',target:function(){return $('t-inc');},prompt:'See incoming lots',where:'below',run:function(){S.view='inc';render();},
 after:function(){return['Incoming lots by grade and supplier',lotsIn().length+' lots today: '+n0(putAway().reduce(function(a,t){return a+net(t);},0))+' lb to put away, NP-0712 held.'];}}];
'''
