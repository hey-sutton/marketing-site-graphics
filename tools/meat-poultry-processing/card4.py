"""Meat and poultry card 4: Raw to Ready to Eat Runs. Layout: a record form with a side summary panel.
Left: the read only order field with Open order, then the manufacturing order: its raw and ready to eat stages, the
meat issued by lot (read only lot field), the BOM components that deduct on their own at the start of the run, and
the output with the read only dehydrator weight and the bag and carton count. Right: stock movements, one line per
item with before and after, ending with the finished lot entering stock with its pack and use by dates."""
from frame_auto import header

SUMMARY = 'Raw to Ready to Eat Runs (jerky order JRK-3310 for 420 kg with a raw stage and a ready to eat stage, issue 1,000 kg of BEEF-24-0731 so the lot falls from 2,400 to 1,400 kg, spice blend 25 kg and cure 5 kg deduct at the start, 420 kg out of the dehydrator in 50 g bags is 8,400 bags and 70 cartons of 120, new lot FG-7701 packed Nov 2, use by Feb 2)'
ARIA = 'Interactive product screen: open a jerky order with raw and ready to eat stages, issue meat lots to it, see spices and packaging deduct on their own, record the weight out of the dehydrator and see the finished lot enter stock with its dates'
STEPS = 5
STUDIO = dict(lede='A typical run screen on your Sutton data. Want it different? Describe the change.',
              examples=['A temperature log per stage', 'Labels printed at finish', 'Issue by first expiry', 'A hold until lab release'],
              built_on='Work orders, BOMs, lots and stock', change='Stages, fields and views')

ICON = '<rect x="2.5" y="2" width="11" height="12" rx="1.5"/><path d="M5 5.5h6M5 8h6M5 10.5h3.5"/>'

CSS = (
 '.fld input[readonly]{background:#F4F4F5;color:#3F3F46;cursor:default;pointer-events:none}'
 '.g1{display:grid;grid-template-columns:416px 230px;grid-template-rows:62px 468px;gap:10px;padding:10px 44px 0 16px;width:716px}'
 '.bf{display:flex;flex-direction:column;justify-content:center;gap:5px;padding:0 12px}.bf .frm{display:flex;align-items:flex-end;gap:8px}.bf .fld{width:196px}.bf .ctx{font-size:8.9px;color:#71717A}.bf .frm .rt{margin-left:auto}'
 '.rc{display:flex;flex-direction:column}.rc>.empt{margin:10px;flex:1}'
 '.sec{padding:6px 11px 0}.sec+.sec{border-top:1px solid #F0F0F1;margin-top:6px}.sec h4{margin:0 0 5px;font-size:9.6px;font-weight:600;display:flex;align-items:center;justify-content:space-between;gap:6px}.sec h4 .bt{font-size:9px;padding:2px 9px}.bt:disabled{opacity:.45;cursor:not-allowed}'
 '.stg{display:grid;grid-template-columns:1fr 18px 1fr;align-items:stretch}.stg .ar{display:grid;place-items:center;color:#A1A1AA}.stg .ar svg{width:10px;height:10px}'
 '.sx{border:1px solid #E4E4E7;border-radius:8px;padding:5px 8px;display:flex;flex-direction:column;gap:2px;transition:background-color .35s,border-color .35s}.sx .t1{display:flex;justify-content:space-between;align-items:center;font-size:9.6px;font-weight:600}.sx small{font-size:8.3px;color:#71717A;line-height:1.35}'
 '.sx.raw{box-shadow:inset 3px 0 0 #DC2626}.sx.rte{box-shadow:inset 3px 0 0 #16A34A}.sx.on{background:#FAFAFA}'
 '.qf{display:flex;align-items:flex-end;gap:8px}.qf .fld{width:110px}.qf .rt{margin-left:auto}.qf .ctx{font-size:8.5px;color:#71717A;padding-bottom:6px}'
 '.cl .row{grid-template-columns:1fr 60px 62px 72px;font-size:9.1px;min-height:20px;padding:0 6px}.cl .row>span:nth-child(2),.cl .row>span:nth-child(3){text-align:right;font-family:"JetBrains Mono",ui-monospace,monospace}.cl .row.h>span{font-family:inherit!important}.cl .row>span:last-child{text-align:right}.cl{border:1px solid #E4E4E7;border-radius:8px;overflow:hidden}.cl .row small{font-size:8px;color:#71717A}'
 '.pk{display:grid;grid-template-columns:1fr 1fr;gap:6px;margin-top:5px}.pk div{border:1px solid #E4E4E7;border-radius:7px;padding:5px 8px;background:#FAFAFA;font-family:"JetBrains Mono",ui-monospace,monospace;font-size:9.2px}.pk div small{display:block;font-family:Inter,system-ui,sans-serif;font-size:8.1px;color:#71717A}.pk div b{font-size:11px}'
 '.lph{margin-top:5px;border:1px dashed #E4E4E7;border-radius:7px;background:#FAFAFA;padding:7px;font-size:8.8px;color:#A1A1AA;text-align:center}'
 '.tot{margin-top:auto;padding:8px 11px;border-top:1px solid #E4E4E7;font-size:9px;color:#52525B;line-height:1.4;background:#FAFAFA}.sm .tot{padding-right:90px}'
 '.sm{grid-column:2;grid-row:1/3;display:flex;flex-direction:column}.sm>.empt{margin:10px;flex:1}'
 '.mv{padding:7px 9px 0;display:flex;flex-direction:column;gap:6px}.mi{border:1px solid #E4E4E7;border-radius:8px;padding:6px 8px;display:flex;flex-direction:column;gap:3px}.mi .t1{display:flex;justify-content:space-between;align-items:center;font-size:9.2px;font-weight:600}.mi .t1 .mono{font-weight:500;font-size:8.6px;color:#52525B}'
 '.mi .ba{display:flex;align-items:center;gap:5px;font-family:"JetBrains Mono",ui-monospace,monospace;font-size:9.6px}.mi .ba s{color:#A1A1AA}.mi .ba .d{margin-left:auto;font-size:8.8px;color:#B91C1C}.mi .ba .d.p{color:#166534}.mi.nw{border-color:#BBF7D0;background:#F0FDF4}'
 '.mi .dts{display:flex;gap:10px;font-size:8.6px;color:#166534}.mi .dts b{color:#18181B}'
 '.mvh{padding:8px 11px 0;font-size:8.6px;color:#71717A;display:flex;justify-content:space-between}'
)

WIN = (
 header(ICON, 'Manufacturing order', 'Raw and ready to eat stages with lots and stock')
 + '<div class="g1"><div class="cd bf"><div class="frm"><label class="fld"><small>Order</small>'
 '<input id="iod" value="JRK-3310, Beef Jerky 420 kg" readonly tabindex="-1" autocomplete="off" spellcheck="false"></label>'
 '<button type="button" class="bt pri" id="oob">Open order</button><span class="rt" id="rst"></span></div><div class="ctx">Released to production, BOM BJ-07</div></div>'
 '<div class="cd rc" id="rc"></div><div class="cd sm" id="sm"></div></div>'
)

JS = r'''
var FOC='.hd>*,.bf .fld,.bf .ctx,#oob,.rc .ct,.rc .sec,.rc .tot,.sm>*';
var MI=String.fromCharCode(8722),DV='÷';
var LOT={id:'BEEF-24-0731',on:2400,iss:1000},OUT=420,BAG=50,CTN=120;
var COMP=[{id:'sb',nm:'Jerky spice blend',lot:'SB-1107',q:25,u:'kg',on:180},{id:'cu',nm:'Cure',lot:'CU-0215',q:5,u:'kg',on:40},{id:'bg',nm:'Bags, 50 g',lot:'PK-5050',q:0,u:'ea',on:20000},{id:'ct',nm:'Cartons of 120',lot:'PK-1120',q:0,u:'ea',on:500}];
var S;
function bags(){return OUT*1000/BAG;}
function ctns(){return bags()/CTN;}
function cq(c){return c.id==='bg'?bags():c.id==='ct'?ctns():c.q;}
var ARR='<svg viewBox="0 0 10 10" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"><path d="M2 5h6M5.5 2.5L8 5 5.5 7.5"/></svg>';
function render(){
$('oob').className='bt '+(S.op?'done':'pri');$('oob').textContent=S.op?'Opened':'Open order';
$('rst').innerHTML=!S.op?'':S.fn?'<span class="ch c-ok">Finished</span>':S.st?'<span class="ch c-info">Running</span>':'<span class="ch c-idle">Released</span>';
var r='<div class="ct"><span>Order JRK-3310</span>'+(S.op?'<span class="ch c-idle">Beef jerky, 420 kg</span>':'')+'</div>';
if(!S.op)r+='<div class="empt"><b>No order open</b><span>Open an order to see its stages, the meat lots issued and the components it uses.</span></div>';
else{
r+='<div class="sec in"><h4><span>Stages</span><span class="ch c-idle" id="nst">2 stages</span></h4><div class="stg" id="stg"><div class="sx raw'+(S.st&&!S.wt?' on':'')+'"><div class="t1"><span>1. Raw</span><span class="ch '+(S.wt?'c-ok':S.st?'c-info':'c-idle')+'">'+(S.wt?'Done':S.st?'Running':'Ready')+'</span></div><small>Marinate and slice, line R2</small></div><div class="ar">'+ARR+'</div>'+
'<div class="sx rte'+(S.wt&&!S.fn?' on':'')+'"><div class="t1"><span>2. Ready to eat</span><span class="ch '+(S.fn?'c-ok':S.wt?'c-info':'c-idle')+'">'+(S.fn?'Done':S.wt?'Packing':'Waiting')+'</span></div><small>Dehydrate and pack, dehydrator 3</small></div></div></div>';
r+='<div class="sec in"><h4><span>Meat issued</span>'+(S.is?'<span class="ch c-ok" id="isd">'+n0(LOT.iss)+' kg issued</span>':'<span class="ch c-idle">Nothing issued</span>')+'</h4><div class="qf"><label class="fld"><small>Lot</small><input id="ilt" value="'+LOT.id+'" readonly tabindex="-1"></label><span class="ctx">Prairie Ridge Beef, cooler 2</span>'+
'<button type="button" class="bt '+(S.is?'done':'pri')+' rt" id="isb">'+(S.is?'Issued':'Issue meat')+'</button></div></div>';
r+='<div class="sec in"><h4><span>BOM components</span><button type="button" class="bt '+(S.st?'done':'pri')+'" id="srb"'+(S.is?'':' disabled')+'>'+(S.st?'Run started':'Start run')+'</button></h4><div class="cl" id="cl"><div class="row h"><span>Component</span><span>Qty</span><span>Lot</span><span>Status</span></div>'+
COMP.map(function(c){return '<div class="row"><span>'+c.nm+'</span><span>'+n0(cq(c))+' <small>'+c.u+'</small></span><span class="mono">'+c.lot+'</span><span><span class="ch '+(S.st?'c-ok':'c-idle')+'">'+(S.st?'Deducted':'At start')+'</span></span></div>';}).join('')+'</div></div>';
r+='<div class="sec in"><h4><span>Output</span>'+(S.fn?'<span class="ch c-ok">Lot FG-7701</span>':'')+'</h4><div class="qf"><label class="fld"><small>Dehydrator weight, kg</small><input id="iwt" value="420" readonly tabindex="-1"></label>'+
'<button type="button" class="bt '+(S.wt?'done':'pri')+'" id="rwb"'+(S.st?'':' disabled')+'>'+(S.wt?'Recorded':'Record weight')+'</button><button type="button" class="bt '+(S.fn?'done':'pri')+' rt" id="fnb"'+(S.wt?'':' disabled')+'>'+(S.fn?'Finished':'Finish')+'</button></div>'+
(S.wt?'<div class="pk in"><div id="pbg"><small>Bags</small>'+n0(OUT*1000)+' g '+DV+' '+BAG+' g = <b>'+n0(bags())+'</b></div><div id="pct"><small>Cartons</small>'+n0(bags())+' '+DV+' '+CTN+' = <b>'+n0(ctns())+'</b></div></div>':'<div class="lph">Bags and cartons count from the weight out of the dehydrator.</div>')+'</div>';
}
$('rc').innerHTML=r;
var m='<div class="ct"><span>Stock movements</span>'+(S.op?'<span class="ch c-idle" id="mvn">'+((S.is?1:0)+(S.st?COMP.length:0)+(S.fn?1:0))+'</span>':'')+'</div>';
if(!S.op)m+='<div class="empt"><b>No movements</b><span>Every lot that leaves or enters stock shows here.</span></div>';
else if(!S.is)m+='<div class="empt in"><b>No movements yet</b><span>Issue meat to the order to move stock.</span></div>';
else{var a=[];
if(S.fn)a.push('<div class="mi nw in" id="fg"><div class="t1"><span>Beef jerky, 50 g</span><span class="ch c-ok">New lot</span></div><div class="ba"><span class="mono" id="fgl">FG-7701</span><span class="d p">+'+n0(OUT)+' kg</span></div><div class="dts"><span>Pack <b id="fpk">Nov 2</b></span><span>Use by <b id="fub">Feb 2</b></span></div><div class="dts" style="color:#52525B">'+n0(bags())+' bags in '+n0(ctns())+' cartons</div></div>');
if(S.st)COMP.slice().reverse().forEach(function(c){a.push('<div class="mi in" id="m-'+c.id+'"><div class="t1"><span>'+c.nm+'</span><span class="mono">'+c.lot+'</span></div><div class="ba"><s>'+n0(c.on)+'</s><span>→</span><span>'+n0(c.on-cq(c))+'</span><span class="d">'+MI+n0(cq(c))+' '+c.u+'</span></div></div>');});
a.push('<div class="mi in" id="m-lot"><div class="t1"><span>Beef, raw</span><span class="mono">'+LOT.id+'</span></div><div class="ba"><s id="lb">'+n0(LOT.on)+'</s><span>→</span><span id="la">'+n0(LOT.on-LOT.iss)+'</span><span class="d">'+MI+n0(LOT.iss)+' kg</span></div></div>');
m+='<div class="mvh"><span>Newest first</span><span>kg or each</span></div><div class="mv">'+a.slice(0,S.fn?6:5).join('')+'</div>';}
m+='<div class="tot">Stock moves with the order, by lot.</div>';
$('sm').innerHTML=m;
}
function resetState(){S={op:false,is:false,st:false,wt:false,fn:false};render();}
var ST=[
{id:'op',target:function(){return $('oob');},prompt:'Open order JRK-3310',where:'below',run:function(){S.op=true;render();},
 after:function(){return['A jerky order with two stages','A raw stage to marinate and slice, then a ready to eat stage to dehydrate and pack.'];}},
{id:'is',target:function(){return $('isb');},prompt:'Issue meat',where:'below',run:function(){S.is=true;render();},
 after:function(){return['Meat issued by lot',n0(LOT.iss)+' kg of '+LOT.id+': the lot falls from '+n0(LOT.on)+' to '+n0(LOT.on-LOT.iss)+' kg.'];}},
{id:'st',target:function(){return $('srb');},prompt:'Start the run',where:'below',run:function(){S.st=true;render();},
 after:function(){return['Spices and packaging deduct on their own','Spice blend 25 kg, cure 5 kg, '+n0(bags())+' bags and '+n0(ctns())+' cartons come off stock.'];}},
{id:'wt',target:function(){return $('rwb');},prompt:'Record the dehydrator weight',where:'above',run:function(){S.wt=true;render();},
 after:function(){return['Weight out of the dehydrator',n0(OUT)+' kg in 50 g bags is '+n0(bags())+' bags, '+n0(ctns())+' cartons of '+CTN+'.'];}},
{id:'fn',target:function(){return $('fnb');},prompt:'Finish the order',where:'above',run:function(){S.fn=true;render();},
 after:function(){return['The finished lot enters stock','New lot FG-7701, '+n0(OUT)+' kg, packed Nov 2 and use by Feb 2.'];}}];
'''
