"""Wineries card 3: Lots from Cork to Case. Layout: list and detail (left list of lots, right record panel).
Top: the read only lot field with Search. Left: the lots found (the cork lot, then the bottling runs that used it, then
the glass lot once an order is traced) and the distributor orders with Trace order. Right: the record: the cork lot with
received, used and remaining, then tabs for the bottling runs, the cases and accounts, and the dates, and finally the
trace of one distributor order back to its lots.
Corks used are cases times 12; each run's shipments add up to its cases."""
from frame_auto import header

SUMMARY = 'Lots from Cork to Case (cork lot CK-2410-77 from Alder Cork Supply, 16,000 received Oct 14, used in BT-0318 6,000, BT-0322 4,800 and BT-0327 3,600, 14,400 in total, 1,600 remain; 500, 400 and 300 cases to Harbor Wine Co, club release, Northside Distributors and web orders; SO-6120 traced to BT-0322, CK-2410-77 and GL-5532)'
ARIA = 'Interactive product screen: search a cork lot, see the bottling runs that used it, list the cases and accounts it reached, open the received and bottled dates of each lot, and trace one distributor order back to its lots'
STEPS = 5
STUDIO = dict(lede='A typical lot trace screen on your Sutton data. Want it different? Describe the change.',
              examples=['Barrel and tank lots', 'A recall letter by account', 'Label lots on every run', 'Trace by bottle code'],
              built_on='Lots, work orders, BOMs and shipments', change='Fields, links and views')

ICON = '<circle cx="5" cy="5" r="2.2"/><circle cx="11.5" cy="11" r="2.2"/><path d="M6.6 6.6l3.3 2.8"/><path d="M2 13.5h4"/>'

CSS = (
 '.fld input[readonly]{background:#F4F4F5;color:#3F3F46;cursor:default;pointer-events:none}'
 '.g3{display:grid;grid-template-columns:222px 424px;grid-template-rows:60px 470px;gap:10px;padding:10px 44px 0 16px;width:716px}'
 '.top{grid-column:1/3;display:flex;flex-direction:column;justify-content:center;gap:5px;padding:0 12px}.top .frm{display:flex;align-items:flex-end;gap:8px}.top .fld{width:120px}.top .ctx{font-size:8.9px;color:#71717A}.top .rs{margin-left:auto}'
 '.ls,.dt{display:flex;flex-direction:column}.ls>.empt,.dt>.empt{margin:9px;flex:1;padding:10px}'
 '.ls .row{grid-template-columns:20px 1fr auto;min-height:42px;font-size:9.2px}.ls .row b{font-family:"JetBrains Mono",ui-monospace,monospace;font-size:9.8px}.ls .row small{display:block;font-size:8.3px;color:#71717A;margin-top:1px}'
 '.ls .row .w{text-align:right;font-family:"JetBrains Mono",ui-monospace,monospace;font-size:9.2px}.ls .row.sel{background:#F4F4F5;box-shadow:inset 3px 0 0 #18181B}.ls .row.ch2{padding-left:20px}'
 '.ls .ic{width:18px;height:18px;border-radius:5px;display:grid;place-items:center;font-size:8px;font-weight:600;color:#fff}.ic.k{background:#78350F}.ic.r{background:#7F1D1D}.ic.g{background:#166534}.ic.o{background:#1E3A8A}'
 '.oq{margin-top:8px;border-top:1px solid #E4E4E7;border-bottom:1px solid #F0F0F1}.oq .lb{padding:6px 11px 2px;font-size:9.2px;font-weight:600;display:flex;justify-content:space-between}.oq .row{grid-template-columns:1fr auto;min-height:40px}.oq .bt{font-size:8.8px;padding:3px 8px}'
 '.ls .tot,.dt .tot{padding:8px 11px;border-top:1px solid #E4E4E7;font-size:9px;color:#52525B;line-height:1.4;background:#FAFAFA}.dt .tot{margin-top:auto;padding-right:90px}.ls .tot{margin-top:auto}'
 '.dh{padding:9px 11px 0;display:flex;justify-content:space-between;align-items:flex-start}.dh .kv b{font-size:15px;font-family:"JetBrains Mono",ui-monospace,monospace}.dh .r2{display:flex;gap:5px}'
 '.kg{display:grid;grid-template-columns:1fr 1fr 1fr;gap:6px 10px;padding:8px 11px 0}'
 '.bal{margin:8px 11px 0;display:grid;grid-template-columns:1fr 1fr 1fr;gap:6px}.bal div{border:1px solid #E4E4E7;border-radius:7px;padding:5px 8px}.bal div.g{border-color:#BBF7D0;background:#F0FDF4}.bal small{display:block;font-size:8.2px;color:#71717A}.bal b{font-family:"JetBrains Mono",ui-monospace,monospace;font-size:12px}'
 '.ub{margin:6px 11px 0;display:flex;height:12px;border-radius:4px;overflow:hidden;background:#F4F4F5}.ub i{height:100%;border-right:1px solid #fff}.ub .u0{background:#7F1D1D}.ub .u1{background:#B45353}.ub .u2{background:#E7A9A9}.ub .u3{background:#F4F4F5}'
 '.calc{margin:5px 11px 0;padding:4px 8px;border-radius:6px;background:#FAFAFA;border:1px solid #F0F0F1;font-family:"JetBrains Mono",ui-monospace,monospace;font-size:8.9px;text-align:center}'
 '.dt .tabs{margin-top:9px;height:28px;border-top:1px solid #F0F0F1}.tab:disabled{color:#A1A1AA;cursor:default}'
 '.pn{padding:8px 11px 0}.tb{border:1px solid #E4E4E7;border-radius:8px;overflow:hidden}.tb .row{font-size:9.1px;min-height:22px;padding:0 7px}.tb .row.h>span{font-family:inherit!important}.tb .row.sm{background:#FAFAFA;font-weight:600}.tb .row small{display:block;font-size:8px;color:#71717A}'
 '.tr1 .row{grid-template-columns:58px 1fr 56px 52px 60px}.tr1 .row>span:nth-child(n+3){text-align:right;font-family:"JetBrains Mono",ui-monospace,monospace}'
 '.tr2 .row{grid-template-columns:58px 1fr 62px 50px}.tr2 .row>span:nth-child(n+3){text-align:right;font-family:"JetBrains Mono",ui-monospace,monospace}.tr2 .row.rh{background:#FAFAFA;min-height:22px;font-weight:600}'
 '.tr3 .row{grid-template-columns:70px 1fr 74px 64px}.tr3 .row>span:nth-child(n+3){text-align:right}'
 '.tl{margin:9px 11px 0;position:relative;height:46px;border-top:1px solid #E4E4E7}.tl .mk{position:absolute;top:-5px;transform:translateX(-50%);display:flex;flex-direction:column;align-items:center;font-size:8px;color:#52525B;white-space:nowrap}.tl .mk i{width:9px;height:9px;border-radius:50%;margin-bottom:3px}.tl .mk b{font-family:"JetBrains Mono",ui-monospace,monospace;font-size:8.3px;color:#18181B}'
 '.acc{margin:8px 11px 0;display:grid;grid-template-columns:repeat(4,1fr);gap:5px}.acc div{border:1px solid #E4E4E7;border-radius:7px;padding:4px 7px}.acc small{display:block;font-size:8px;color:#71717A}.acc b{font-family:"JetBrains Mono",ui-monospace,monospace;font-size:10.5px}'
 '.ch3{padding:8px 11px 0;display:flex;flex-direction:column;gap:6px}.tn{display:flex;align-items:center;gap:7px;font-size:9px}.tn .bx{border:1px solid #E4E4E7;border-radius:7px;padding:5px 9px;background:#fff}.tn .bx b{font-family:"JetBrains Mono",ui-monospace,monospace;font-size:9.8px}.tn .bx small{display:block;font-size:8.2px;color:#71717A}'
 '.tn .bx.o{border-color:#BFDBFE;background:#EFF6FF}.tn .bx.k{border-color:#BBF7D0;background:#F0FDF4}.tn .ln{color:#A1A1AA;font-family:"JetBrains Mono",ui-monospace,monospace;font-size:10px}'
 '.sumr{margin:9px 11px 0;display:grid;grid-template-columns:1fr 1fr 1fr;gap:6px}.sumr div{border:1px solid #E4E4E7;border-radius:7px;padding:5px 8px;text-align:center}.sumr small{display:block;font-size:8.2px;color:#71717A}.sumr b{font-family:"JetBrains Mono",ui-monospace,monospace;font-size:14px}'
 '.note{margin:8px 11px 0;padding:6px 8px;border-radius:7px;font-size:8.9px;line-height:1.45;background:#FAFAFA;border:1px solid #F0F0F1;color:#52525B}'
)

WIN = (
 header(ICON, 'Lot trace', 'From dry goods lot to bottling run, case and account')
 + '<div class="g3"><div class="cd top"><div class="frm"><label class="fld"><small>Lot number</small>'
 '<input id="ilt" value="CK-2410-77" readonly tabindex="-1" autocomplete="off" spellcheck="false"></label>'
 '<button type="button" class="bt pri" id="srb">Search</button><span class="rs" id="rs"></span></div><div class="ctx">Natural cork, 44 mm, from Alder Cork Supply</div></div>'
 '<div class="cd ls" id="ls"></div><div class="cd dt" id="dt"></div></div>'
)

JS = r'''
var FOC='.hd>*,.top .fld,.top .ctx,#srb,.ls .ct,.ls .row,.ls .oq .lb,.ls .tot,.dt .ct,.dt>*:not(.ct):not(.tabs),.dt .tab';
var LOT={id:'CK-2410-77',sup:'Alder Cork Supply',rc:16000,d:'Oct 14, 2024',x:3};
var GL={id:'GL-5532',sup:'Ridgeline Glass Co',d:'Feb 3, 2025',x:65};
var RUNS=[{id:'BT-0318',w:'Reserve Red',cs:500,d:'Mar 18, 2025',x:79,sh:[['Harbor Wine Co','SO-6104',300],['Club release','CL-0325',200]]},
{id:'BT-0322',w:'Reserve Red',cs:400,d:'Mar 22, 2025',x:88,sh:[['Northside Distributors','SO-6120',400]]},
{id:'BT-0327',w:'Estate Rose',cs:300,d:'Mar 27, 2025',x:97,sh:[['Harbor Wine Co','SO-6131',100],['Web orders','WEB',200]]}];
var ORD={id:'SO-6120',acc:'Northside Distributors',run:'BT-0322',cs:400};
var S;
function corks(r){return r.cs*12;}
function used(){return RUNS.reduce(function(a,r){return a+corks(r);},0);}
function left(){return LOT.rc-used();}
function cases(){return RUNS.reduce(function(a,r){return a+r.cs;},0);}
function shipped(r){return r.sh.reduce(function(a,s){return a+s[2];},0);}
function accts(){var o={};RUNS.forEach(function(r){r.sh.forEach(function(s){o[s[0]]=(o[s[0]]||0)+s[2];});});return o;}
function traceRuns(){return RUNS.filter(function(r){return r.id===ORD.run;});}
function render(){
$('srb').className='bt '+(S.op?'done':'pri');$('srb').textContent=S.op?'Found':'Search';
$('rs').innerHTML=S.op?'<span class="ch c-ok">1 lot found</span>':'';
var l='<div class="ct"><span>Lots</span>'+(S.op?'<span class="ch c-idle">'+(1+(S.ru?3:0)+(S.tr?1:0))+'</span>':'')+'</div>';
if(!S.op)l+='<div class="empt"><b>No lot found yet</b><span>Search a lot number to see where it went.</span></div>';
else{l+='<div class="row in'+(S.tr?'':' sel')+'" id="l-'+LOT.id+'"><span class="ic k">C</span><span><b>'+LOT.id+'</b><small>Cork lot, '+LOT.sup+'</small></span><span class="w">'+n0(LOT.rc)+'</span></div>';
if(S.ru)l+=RUNS.map(function(r){var on=S.tr&&r.id===ORD.run;return '<div class="row in ch2'+(on?' sel':'')+'" id="l-'+r.id+'"><span class="ic r">B</span><span><b>'+r.id+'</b><small>'+r.w+', '+r.cs+' cases</small></span><span class="w">'+n0(corks(r))+'</span></div>';}).join('');
if(S.tr)l+='<div class="row in" id="l-'+GL.id+'"><span class="ic g">G</span><span><b>'+GL.id+'</b><small>Glass lot, '+GL.sup+'</small></span><span class="w">'+n0(ORD.cs*12)+'</span></div>';
if(S.ca)l+='<div class="oq in"><div class="lb"><span>Distributor orders</span><span class="ch c-idle">1</span></div><div class="row'+(S.tr?' sel':'')+'" id="l-'+ORD.id+'"><span><b>'+ORD.id+'</b><small>'+ORD.acc+', '+ORD.cs+' cases</small></span>'+(S.tr?'<span class="ch c-ok">Traced</span>':'<button type="button" class="bt '+(S.dt?'pri':'')+'" id="tob">Trace order</button>')+'</div></div>';
l+='<div class="tot">'+(S.ru?'Indented runs used this lot.':'Every lot links to what it went into.')+'</div>';}
$('ls').innerHTML=l;
var d='<div class="ct"><span>'+(S.tr?'Order trace':'Lot record')+'</span>'+(S.op?'<span class="ch c-idle mono">'+(S.tr?ORD.id:LOT.id)+'</span>':'')+'</div>';
if(!S.op)d+='<div class="empt"><b>Nothing selected</b><span>A lot record shows what was received, the runs that used it and the accounts it reached.</span></div>';
else if(S.tr){var tr=traceRuns()[0];
d+='<div class="dh in"><div class="kv"><small>Distributor order</small><b>'+ORD.id+'</b></div><div class="r2"><span class="ch c-info">'+ORD.acc+'</span><span class="ch c-ok">Shipped</span></div></div>'+
'<div class="kg in"><div class="kv"><small>Wine</small><b>'+tr.w+'</b></div><div class="kv"><small>Cases</small><b class="mono">'+ORD.cs+'</b></div><div class="kv"><small>Shipped</small><b>Apr 2, 2025</b></div></div>'+
'<div class="pn in" style="padding-bottom:0"><b style="font-size:9.6px">Back to its lots</b></div><div class="ch3 in" id="trc">'+
'<div class="tn"><span class="bx o"><b>'+ORD.id+'</b><small>'+ORD.cs+' cases</small></span><span class="ln">←</span><span class="bx" id="tr-run"><b>'+tr.id+'</b><small>'+tr.w+', '+tr.d+'</small></span><span class="ln">←</span><span class="bx k" id="tr-ck"><b>'+LOT.id+'</b><small>Cork, '+n0(corks(tr))+' used</small></span></div>'+
'<div class="tn"><span style="width:166px;flex:none"></span><span class="ln">↖</span><span class="bx k" id="tr-gl"><b>'+GL.id+'</b><small>Glass, '+n0(corks(tr))+' bottles, received Feb 3</small></span></div></div>'+
'<div class="sumr in"><div><small>Bottling runs</small><b id="trn">'+traceRuns().length+'</b></div><div><small>Cork lots</small><b id="tck">1</b></div><div><small>Glass lots</small><b id="tgl">1</b></div></div>'+
'<div class="pn in"><div class="tb tr3" id="tlr"><div class="row h"><span>Lot</span><span>Record</span><span>Date</span><span>Status</span></div>'+
'<div class="row"><span class="mono"><b>'+tr.id+'</b></span><span>Bottled, '+tr.cs+' cases</span><span>Mar 22</span><span><span class="ch c-ok">Released</span></span></div>'+
'<div class="row"><span class="mono"><b>'+LOT.id+'</b></span><span>Received, '+n0(left())+' left</span><span>Oct 14</span><span><span class="ch c-ok">Released</span></span></div>'+
'<div class="row"><span class="mono"><b>'+GL.id+'</b></span><span>Received, '+GL.sup+'</span><span>Feb 3</span><span><span class="ch c-ok">Released</span></span></div></div></div>';}
else{d+='<div class="dh in"><div class="kv"><small>Cork lot</small><b>'+LOT.id+'</b></div><div class="r2"><span class="ch c-idle">Natural, 44 mm</span><span class="ch c-ok">Released</span></div></div>'+
'<div class="kg in"><div class="kv"><small>Supplier</small><b>'+LOT.sup+'</b></div><div class="kv"><small>Received</small><b>'+LOT.d+'</b></div><div class="kv"><small>Location</small><b>Dry store, bay 2</b></div></div>'+
'<div class="bal in"><div><small>Received</small><b id="brc">'+n0(LOT.rc)+'</b></div><div><small>Used</small><b id="bus">'+(S.ru?n0(used()):'Open')+'</b></div><div class="g"><small>Remaining</small><b id="brm">'+(S.ru?n0(left()):'Open')+'</b></div></div>';
if(S.ru)d+='<div class="ub in" aria-hidden="true">'+RUNS.map(function(r,i){return '<i class="u'+i+'" style="width:'+(corks(r)/LOT.rc*100).toFixed(1)+'%"></i>';}).join('')+'<i class="u3" style="width:'+(left()/LOT.rc*100).toFixed(1)+'%"></i></div><div class="calc in" id="bcal">'+n0(LOT.rc)+' received = '+n0(used())+' used + '+n0(left())+' left</div>';
var tab=S.dt?'dt':S.ca?'ca':S.ru?'ru':'';
d+='<div class="tabs in" role="tablist"><button type="button" class="tab'+(tab==='ru'?' on':'')+'" id="t-ru">Bottling runs</button><button type="button" class="tab'+(tab==='ca'?' on':'')+'" id="t-ca"'+(S.ru?'':' disabled')+'>Cases and accounts</button><button type="button" class="tab'+(tab==='dt'?' on':'')+'" id="t-dt"'+(S.ca?'':' disabled')+'>Dates</button></div>';
if(!tab)d+='<div class="pn in"><div class="empt" style="padding:26px 14px"><b>Pick a view</b><span>Runs, cases and accounts, and dates for this lot.</span></div></div>';
else if(tab==='ru')d+='<div class="pn in"><div class="tb tr1" id="tru"><div class="row h"><span>Run</span><span>Wine</span><span>Cases</span><span>Bottles</span><span>Corks used</span></div>'+
RUNS.map(function(r){return '<div class="row"><span class="mono"><b>'+r.id+'</b></span><span>'+r.w+'<small>Line 1, 750 ml</small></span><span>'+r.cs+'</span><span>'+n0(r.cs*12)+'</span><span id="cu-'+r.id+'">'+n0(corks(r))+'</span></div>';}).join('')+
'<div class="row sm"><span>Total</span><span></span><span id="rcs">'+n0(cases())+'</span><span>'+n0(cases()*12)+'</span><span id="rck">'+n0(used())+'</span></div></div></div>';
else if(tab==='ca'){var A=accts();d+='<div class="pn in"><div class="tb tr2" id="tca"><div class="row h"><span>Run</span><span>Account</span><span>Order</span><span>Cases</span></div>'+
RUNS.map(function(r){return r.sh.map(function(s,j){return '<div class="row"><span class="mono">'+(j?'':'<b>'+r.id+'</b>')+'</span><span>'+s[0]+(j?'':'<small>'+r.w+'</small>')+'</span><span>'+s[1]+'</span><span>'+s[2]+'</span></div>';}).join('');}).join('')+'</div></div>'+
'<div class="acc in" id="prun">'+RUNS.map(function(r){return '<div><small>'+r.id+' shipped</small><b id="rs-'+r.id+'">'+shipped(r)+' of '+r.cs+'</b></div>';}).join('')+'<div><small>All runs</small><b id="cst">'+n0(cases())+'</b></div></div>';}
else{var M=[[LOT.id,'Received',LOT.d,'#78350F',LOT.x],[GL.id,'Received',GL.d,'#166534',GL.x]].concat(RUNS.map(function(r){return [r.id,'Bottled',r.d,'#7F1D1D',r.x];}));
d+='<div class="pn in"><div class="tb tr3" id="tdt"><div class="row h"><span>Lot</span><span>Kind</span><span>Event</span><span>Date</span></div>'+
M.map(function(m){return '<div class="row" id="dt-'+m[0]+'"><span class="mono"><b>'+m[0]+'</b></span><span>'+(m[1]==='Bottled'?'Bottling run':m[0]===LOT.id?'Cork lot':'Glass lot')+'</span><span>'+m[1]+'</span><span class="mono">'+m[2].replace(', 2025','').replace(', 2024','')+'</span></div>';}).join('')+'</div></div>'+
'<div class="note in">The cork lot was in stock five months before the first run used it.</div>';}}
d+='<div class="tot">'+(S.tr?'Order traced in one click.':'Every case keeps the lots that went into it.')+'</div>';
$('dt').innerHTML=d;
}
function resetState(){S={op:false,ru:false,ca:false,dt:false,tr:false};render();}
var ST=[
{id:'op',target:function(){return $('srb');},prompt:'Search cork lot CK-2410-77',where:'below',run:function(){S.op=true;render();},
 after:function(){return['A cork lot and where it came from',LOT.id+' from '+LOT.sup+': '+n0(LOT.rc)+' corks received '+LOT.d+'.'];}},
{id:'ru',target:function(){return $('t-ru');},prompt:'See the bottling runs',where:'above',run:function(){S.ru=true;render();},
 after:function(){return['The bottling runs that used it',RUNS.map(function(r){return r.id+' '+n0(corks(r));}).join(', ')+': '+n0(used())+' used, '+n0(left())+' left.'];}},
{id:'ca',target:function(){return $('t-ca');},prompt:'List cases and accounts',where:'above',run:function(){S.ca=true;render();},
 after:function(){return['Cases and accounts it reached',n0(cases())+' cases to Harbor Wine Co, the club release, Northside Distributors and web orders.'];}},
{id:'dt',target:function(){return $('t-dt');},prompt:'Open the dates',where:'above',run:function(){S.dt=true;render();},
 after:function(){return['Received and bottled dates','Cork received Oct 14, glass Feb 3, runs bottled Mar 18, Mar 22 and Mar 27.'];}},
{id:'tr',target:function(){return $('tob');},prompt:'Trace order SO-6120',where:'above',run:function(){S.tr=true;render();},
 after:function(){return['One order traced back to its lots',ORD.id+' goes back to run '+ORD.run+', cork lot '+LOT.id+' and glass lot '+GL.id+'.'];}}];
'''
