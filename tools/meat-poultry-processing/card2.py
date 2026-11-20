"""Meat and poultry card 2: Lot Traceability to the Customer. Layout: list and detail (left list, right record panel).
Top: the read only supplier lot field with Search. Left: the lot's genealogy as a list (the supplier lot, the runs that
used it, the finished lots and the customer orders, each order with Trace order beside it). Right: the record panel
with Runs, Customers and Dates tabs, and the reverse trace of a customer order. Every quantity below adds up: runs to
the used weight, shipments to each finished lot, and customers to their totals."""
from frame_auto import header

SUMMARY = 'Lot Traceability to the Customer (supplier lot BEEF-24-0731 from Prairie Ridge Beef, 2,400 kg received, used in JRK-3310 1,000, GRD-3314 600 and SAU-3318 400, 2,000 used and 400 left, finished lots to Lakeside Market 630 and Ridge Foods 740, pack Oct 28 and use by Nov 27, SO-8841 traced back to two runs and one supplier lot)'
ARIA = 'Interactive product screen: search a supplier lot, see the runs that used it, list the customers and shipments it reached, open its pack and use by dates and trace a customer order back to its supplier lots'
STEPS = 5
STUDIO = dict(lede='A typical trace screen on your Sutton data. Want it different? Describe the change.',
              examples=['A recall list in one click', 'Use by alerts by customer', 'Supplier certificates on the lot', 'A mock recall timer'],
              built_on='Lots, work orders, BOMs and shipments', change='Fields, rules and views')

ICON = '<circle cx="4" cy="4" r="1.8"/><circle cx="12" cy="8" r="1.8"/><circle cx="4" cy="12" r="1.8"/><path d="M5.6 4.8L10.4 7.2M5.6 11.2L10.4 8.8"/>'

CSS = (
 '.fld input[readonly]{background:#F4F4F5;color:#3F3F46;cursor:default;pointer-events:none}'
 '.g3{display:grid;grid-template-columns:226px 420px;grid-template-rows:60px 470px;gap:10px;padding:10px 44px 0 16px;width:716px}'
 '.top{grid-column:1/3;display:flex;flex-direction:column;justify-content:center;gap:5px;padding:0 12px}.top .frm{display:flex;align-items:flex-end;gap:8px}.top .fld{width:130px}.top .ctx{font-size:8.9px;color:#71717A}.top .rs{margin-left:auto}'
 '.ls,.dt{display:flex;flex-direction:column}.ls>.empt,.dt>.empt{margin:9px;flex:1;padding:10px}'
 '.gh{padding:5px 11px;background:#FAFAFA;border-top:1px solid #E4E4E7;font-size:8.6px;font-weight:600;color:#71717A;display:flex;justify-content:space-between}.gh:first-of-type{border-top:0}'
 '.ls .row{grid-template-columns:1fr auto;min-height:31px;font-size:9px;padding:0 9px 0 11px}.ls .row b{font-family:"JetBrains Mono",ui-monospace,monospace;font-size:9.4px}.ls .row small{display:block;font-size:8.1px;color:#71717A}'
 '.ls .row .w{text-align:right;font-family:"JetBrains Mono",ui-monospace,monospace;font-size:9.2px}.ls .row.sel{background:#F4F4F5;box-shadow:inset 3px 0 0 #18181B}.ls .row.hl{background:#FFFBEB;box-shadow:inset 3px 0 0 #F59E0B}.ls .row .bt{font-size:8.8px;padding:2px 7px}'
 '.ls .ph{padding:6px 11px;font-size:8.5px;color:#A1A1AA;border-top:1px solid #F0F0F1}'
 '.ls .tot,.dt .tot{margin-top:auto;padding:8px 11px;border-top:1px solid #E4E4E7;font-size:9px;color:#52525B;line-height:1.4;background:#FAFAFA}.dt .tot{padding-right:90px}'
 '.dh{padding:9px 11px 0;display:flex;justify-content:space-between;align-items:flex-start}.dh .kv b{font-size:15px;font-family:"JetBrains Mono",ui-monospace,monospace}.dh .r2{display:flex;gap:5px}'
 '.kg{display:grid;grid-template-columns:1fr 1fr 1fr;gap:6px 10px;padding:8px 11px 0}'
 '.dt .tabs{margin-top:9px;height:28px}.dt .tab{font-size:10px}'
 '.sec{padding:9px 11px 0}.sec h4{margin:0 0 5px;font-size:9.6px;font-weight:600;display:flex;justify-content:space-between;align-items:center}'
 '.tb{border:1px solid #E4E4E7;border-radius:8px;overflow:hidden}.tb .row{font-size:9.1px;min-height:26px;padding:0 8px}.tb .row small{display:block;font-size:8px;color:#71717A}.tb .row.sm{background:#FAFAFA;font-weight:600}.tb .r{text-align:right;font-family:"JetBrains Mono",ui-monospace,monospace}.tb .row.h .r{font-family:inherit}'
 '.ru .row{grid-template-columns:70px 1fr 64px 50px}.fg .row{grid-template-columns:62px 1fr 1fr 52px;min-height:22px}.rcl .row{grid-template-columns:22px 84px 1fr;min-height:22px}.fg .row.g{background:#FAFAFA;font-weight:600}'
 '.use{display:flex;height:16px;border-radius:5px;overflow:hidden;margin-top:7px;background:#F4F4F5}.use i{display:grid;place-items:center;font-style:normal;font-size:8.2px;color:#fff;font-family:"JetBrains Mono",ui-monospace,monospace}.use .a{background:#18181B}.use .b{background:#52525B}.use .c{background:#A1A1AA}.use .d{color:#52525B}'
 '.calc{margin-top:7px;padding:5px 8px;border-radius:6px;background:#FAFAFA;border:1px solid #F0F0F1;font-family:"JetBrains Mono",ui-monospace,monospace;font-size:9.2px;text-align:center}'
 '.ct2{display:grid;grid-template-columns:1fr 1fr;gap:8px;padding:9px 11px 0}.ct2 div{border:1px solid #E4E4E7;border-radius:8px;padding:6px 9px}.ct2 small{display:block;font-size:8.3px;color:#71717A}.ct2 b{font-family:"JetBrains Mono",ui-monospace,monospace;font-size:13px}'
 '.dts{display:grid;grid-template-columns:1fr 1fr 1fr;gap:6px;padding:9px 11px 0}.dts div{border:1px solid #E4E4E7;border-radius:8px;padding:6px 9px}.dts div.k{border-color:#BBF7D0;background:#F0FDF4}.dts small{display:block;font-size:8.3px;color:#71717A}.dts b{font-size:12px;font-weight:600}'
 '.tln{margin:12px 11px 0;position:relative;height:74px}.tln .ax{position:absolute;left:0;right:0;top:30px;height:8px;border-radius:4px;background:linear-gradient(90deg,#DCFCE7,#FEF3C7 70%,#FEE2E2)}'
 '.tln .mk{position:absolute;top:22px;width:2px;height:24px;background:#18181B}.tln .lb{position:absolute;font-size:8.2px;color:#52525B;white-space:nowrap;transform:translateX(-50%)}.tln .lb b{display:block;font-family:"JetBrains Mono",ui-monospace,monospace;font-size:8.6px;color:#18181B}.tln .up{top:0}.tln .dn{top:50px}'
 '.tr{padding:4px 11px 0;display:flex;flex-direction:column;gap:7px}.tn{display:flex;align-items:center;gap:6px;font-size:9px}.tn .bx{border:1px solid #E4E4E7;border-radius:7px;padding:4px 8px;background:#fff;min-width:0}.tn .bx b{font-family:"JetBrains Mono",ui-monospace,monospace;font-size:9.4px}.tn .bx small{display:block;font-size:8.1px;color:#71717A}'
 '.tn .bx.so{border-color:#BFDBFE;background:#EFF6FF}.tn .bx.sl{border-color:#BBF7D0;background:#F0FDF4}.tn .ln{color:#A1A1AA;font-family:"JetBrains Mono",ui-monospace,monospace;font-size:9px}'
 '.sum3{display:grid;grid-template-columns:1fr 1fr 1fr;gap:6px;padding:9px 11px 0}.sum3 div{border:1px solid #E4E4E7;border-radius:8px;padding:5px 8px}.sum3 small{display:block;font-size:8.2px;color:#71717A}.sum3 b{font-family:"JetBrains Mono",ui-monospace,monospace;font-size:13px}'
)

WIN = (
 header(ICON, 'Lot trace', 'Supplier lots to runs, finished lots and customers')
 + '<div class="g3"><div class="cd top"><div class="frm"><label class="fld"><small>Supplier lot</small>'
 '<input id="ilt" value="BEEF-24-0731" readonly tabindex="-1" autocomplete="off" spellcheck="false"></label>'
 '<button type="button" class="bt pri" id="srb">Search</button><span class="rs" id="rs"></span></div><div class="ctx">Lot number from the supplier label on the combo bin</div></div>'
 '<div class="cd ls" id="ls"></div><div class="cd dt" id="dt"></div></div>'
)

JS = r'''
var FOC='.hd>*,.top .fld,.top .ctx,#srb,.ls .ct,.ls>*:not(.ct),.dt .ct,.dt>*:not(.ct)';
var LOT={id:'BEEF-24-0731',sup:'Prairie Ridge Beef',rec:2400,item:'Beef chuck and round, boneless',pack:'Oct 28',use:'Nov 27',recd:'Oct 30'};
var RUNS=[{id:'JRK-3310',nm:'Beef jerky',kg:1000,dt:'Oct 31'},{id:'GRD-3314',nm:'Ground beef',kg:600,dt:'Nov 1'},{id:'SAU-3318',nm:'Beef sausage',kg:400,dt:'Nov 3'}];
var FG=[{id:'FG-7701',nm:'Beef jerky',run:'JRK-3310',kg:420,sh:[['Lakeside Market',250],['Ridge Foods',170]]},{id:'FG-7704',nm:'Ground beef',run:'GRD-3314',kg:570,sh:[['Ridge Foods',570]]},{id:'FG-7708',nm:'Beef sausage',run:'SAU-3318',kg:380,sh:[['Lakeside Market',380]]}];
var SO=[{id:'SO-8841',cu:'Ridge Foods',ln:[['FG-7701',170],['FG-7704',570]]},{id:'SO-8838',cu:'Lakeside Market',ln:[['FG-7701',250],['FG-7708',380]]}];
var S;
function used(){return RUNS.reduce(function(a,r){return a+r.kg;},0);}
function left(){return LOT.rec-used();}
function shp(f){return f.sh.reduce(function(a,s){return a+s[1];},0);}
function cust(c){return FG.reduce(function(a,f){return a+f.sh.filter(function(s){return s[0]===c;}).reduce(function(x,s){return x+s[1];},0);},0);}
function fgBy(id){return FG.filter(function(f){return f.id===id;})[0];}
function traceRuns(o){var a=[];o.ln.forEach(function(l){var r=fgBy(l[0]).run;if(a.indexOf(r)<0)a.push(r);});return a;}
function render(){
$('srb').className='bt '+(S.op?'done':'pri');$('srb').textContent=S.op?'Found':'Search';
$('rs').innerHTML=S.op?'<span class="ch c-ok">1 lot found</span>':'';
var hl=S.tr?['SO-8841','FG-7701','FG-7704','JRK-3310','GRD-3314','BEEF-24-0731']:[];
function rw(id,sub,w,sel){return '<div class="row in'+(sel?' sel':'')+(hl.indexOf(id)>=0?' hl':'')+'" id="l-'+id+'"><span><b>'+id+'</b><small>'+sub+'</small></span><span class="w">'+w+'</span></div>';}
var l='<div class="ct"><span>Genealogy</span>'+(S.op?'<span class="ch c-idle mono">'+LOT.id+'</span>':'')+'</div>';
if(!S.op)l+='<div class="empt"><b>No lot found yet</b><span>Search a supplier lot to list everything made from it.</span></div>';
else{l+='<div class="gh"><span>Supplier lot</span><span>kg</span></div>'+rw(LOT.id,LOT.sup,n0(LOT.rec),!S.tr);
l+='<div class="gh"><span>Runs</span><span>'+(S.rn?RUNS.length:'')+'</span></div>'+(S.rn?RUNS.map(function(r){return rw(r.id,r.nm,n0(r.kg));}).join(''):'<div class="ph">Runs list once opened</div>');
l+='<div class="gh"><span>Finished lots</span><span>'+(S.cu?FG.length:'')+'</span></div>'+(S.cu?FG.map(function(f){return rw(f.id,f.nm+', from '+f.run,n0(f.kg));}).join(''):'<div class="ph">Finished lots list with customers</div>');
l+='<div class="gh"><span>Customer orders</span><span>'+(S.cu?SO.length:'')+'</span></div>'+(S.cu?SO.map(function(o){return '<div class="row in'+(S.tr&&o.id==='SO-8841'?' sel':'')+'" id="l-'+o.id+'"><span><b>'+o.id+'</b><small>'+o.cu+'</small></span><span>'+(o.id==='SO-8841'?'<button type="button" class="bt '+(S.tr?'done':'pri')+'" id="trb">'+(S.tr?'Traced':'Trace order')+'</button>':'<span class="w">'+n0(o.ln.reduce(function(a,x){return a+x[1];},0))+'</span>')+'</span></div>';}).join(''):'<div class="ph">Orders list with customers</div>');}
l+='<div class="tot">One lot, every run, finished lot and order it touched.</div>';
$('ls').innerHTML=l;
var d='<div class="ct"><span>Record</span>'+(S.op?'<span class="ch c-idle mono">'+(S.tr?'SO-8841':LOT.id)+'</span>':'')+'</div>';
if(!S.op)d+='<div class="empt"><b>Nothing to show</b><span>The supplier, the runs, the customers and the dates for a lot show here.</span></div>';
else if(S.tr){var o=SO[0],rr=traceRuns(o),q=o.ln.reduce(function(a,x){return a+x[1];},0);
d+='<div class="dh in"><div class="kv"><small>Customer order, '+o.cu+'</small><b>'+o.id+'</b></div><div class="r2"><span class="ch c-ok">Shipped Nov 5</span><span class="ch c-info">Traced</span></div></div>';
d+='<div class="sec in"><h4><span>Order lines</span><span class="ch c-idle">'+o.ln.length+' lines</span></h4><div class="tb fg" id="sol"><div class="row h"><span>Lot</span><span>Product</span><span>Run</span><span class="r">kg</span></div>'+
o.ln.map(function(x){var f=fgBy(x[0]);return '<div class="row"><span class="mono">'+f.id+'</span><span>'+f.nm+'</span><span class="mono">'+f.run+'</span><span class="r">'+n0(x[1])+'</span></div>';}).join('')+'<div class="row sm"><span>Total</span><span></span><span></span><span class="r" id="soq">'+n0(q)+'</span></div></div></div>';
d+='<div class="sec in" style="padding-bottom:0"><h4><span>Back to the supplier lots</span></h4></div><div class="tr in" id="tr">'+
o.ln.map(function(x){var f=fgBy(x[0]);return '<div class="tn"><span class="bx so"><b>'+o.id+'</b><small>'+n0(x[1])+' kg</small></span><span class="ln">←</span><span class="bx"><b>'+f.id+'</b><small>'+f.nm+'</small></span><span class="ln">←</span><span class="bx tr-run"><b>'+f.run+'</b><small>Run</small></span><span class="ln">←</span><span class="bx sl tr-lot"><b>'+LOT.id+'</b><small>'+LOT.sup+'</small></span></div>';}).join('')+'</div>';
d+='<div class="sum3 in"><div><small>Runs</small><b id="trn">'+rr.length+'</b></div><div><small>Supplier lots</small><b id="trl">1</b></div><div><small>Use by</small><b style="font-family:inherit;font-size:12px">'+LOT.use+'</b></div></div>'+
'<div class="sec in"><h4><span>If '+LOT.id+' were recalled</span></h4><div class="tb rcl"><div class="row"><span class="mono">'+RUNS.length+'</span><span>Runs</span><span>'+RUNS.map(function(r){return r.id;}).join(', ')+'</span></div><div class="row"><span class="mono">'+FG.length+'</span><span>Finished lots</span><span>'+FG.map(function(f){return f.id;}).join(', ')+'</span></div><div class="row"><span class="mono">2</span><span>Customers</span><span>Lakeside Market, Ridge Foods</span><span></span></div></div></div>';}
else{d+='<div class="dh in"><div class="kv"><small>Supplier lot</small><b>'+LOT.id+'</b></div><div class="r2"><span class="ch c-ok">Released</span><span class="ch c-idle">Cooler 2</span></div></div>'+
'<div class="kg in"><div class="kv"><small>Supplier</small><b id="dsp">'+LOT.sup+'</b></div><div class="kv"><small>Item</small><b>'+LOT.item+'</b></div><div class="kv"><small>Received</small><b class="mono" id="drc">'+n0(LOT.rec)+' kg</b></div></div>';
var tab=S.vw;d+='<div class="tabs in" role="tablist"><button type="button" class="tab'+(tab==='rn'?' on':'')+'" id="t-rn">Runs</button><button type="button" class="tab'+(tab==='cu'?' on':'')+'" id="t-cu">Customers</button><button type="button" class="tab'+(tab==='dt'?' on':'')+'" id="t-dt">Dates</button></div>';
if(tab==='none')d+='<div class="empt in" style="margin:10px 11px 0;flex:1"><b>Pick a view</b><span>Runs, customers and dates for '+LOT.id+' each open in their own tab.</span></div>';
else if(tab==='rn'){d+='<div class="sec in"><h4><span>Runs that used this lot</span><span class="ch c-idle">'+RUNS.length+' runs</span></h4><div class="tb ru" id="ru"><div class="row h"><span>Run</span><span>Product</span><span class="r">kg used</span><span class="r">Share</span></div>'+
RUNS.map(function(r){return '<div class="row"><span class="mono"><b>'+r.id+'</b></span><span>'+r.nm+'<small>'+r.dt+'</small></span><span class="r" id="ru-'+r.id+'">'+n0(r.kg)+'</span><span class="r">'+(r.kg/LOT.rec*100).toFixed(1)+'%</span></div>';}).join('')+
'<div class="row sm"><span>Used</span><span></span><span class="r" id="ruu">'+n0(used())+'</span><span class="r">'+(used()/LOT.rec*100).toFixed(1)+'%</span></div><div class="row"><span>Remaining</span><span>Cooler 2</span><span class="r" id="rul">'+n0(left())+'</span><span class="r">'+(left()/LOT.rec*100).toFixed(1)+'%</span></div></div>'+
'<div class="use">'+RUNS.map(function(r,i){return '<i class="'+'abc'[i]+'" style="width:'+(r.kg/LOT.rec*100).toFixed(2)+'%">'+n0(r.kg)+'</i>';}).join('')+'<i class="d" style="width:'+(left()/LOT.rec*100).toFixed(2)+'%">'+n0(left())+'</i></div>'+
'<div class="calc" id="rcal">'+n0(used())+' used + '+n0(left())+' left = '+n0(LOT.rec)+' kg received</div></div>';}
else if(tab==='cu'){d+='<div class="sec in"><h4><span>Finished lots and shipments</span><span class="ch c-idle">'+FG.length+' lots</span></h4><div class="tb fg" id="fg"><div class="row h"><span>Lot</span><span>Product</span><span>Customer</span><span class="r">kg</span></div>'+
FG.map(function(f){return '<div class="row g"><span class="mono">'+f.id+'</span><span>'+f.nm+'</span><span class="mut" style="font-weight:400">From '+f.run+'</span><span class="r" id="fk-'+f.id+'">'+n0(f.kg)+'</span></div>'+f.sh.map(function(s,j){return '<div class="row"><span></span><span class="mut">Shipment '+(j+1)+'</span><span>'+s[0]+'</span><span class="r sh-'+f.id+'">'+n0(s[1])+'</span></div>';}).join('');}).join('')+'</div></div>'+
'<div class="ct2 in"><div><small>Lakeside Market</small><b id="cl">'+n0(cust('Lakeside Market'))+' kg</b></div><div><small>Ridge Foods</small><b id="cr">'+n0(cust('Ridge Foods'))+' kg</b></div></div>';}
else{d+='<div class="dts in" id="dts"><div class="k"><small>Pack date</small><b id="dpk">'+LOT.pack+'</b></div><div class="k"><small>Use by</small><b id="dub">'+LOT.use+'</b></div><div><small>Received</small><b>'+LOT.recd+'</b></div></div>'+
'<div class="tln in" id="tln"><div class="ax"></div>'+
[['Oct 28','Packed',0,'up',6],['Oct 31','',10,'',0],['Nov 1','',13.3,'',0],['Nov 3','',20,'dn',13],['Nov 27','Use by',100,'up',92]].map(function(p){var lft=p[2]*0.94+2;return '<div class="mk" style="left:'+lft+'%"></div>'+(p[3]?'<div class="lb '+p[3]+'" style="left:'+p[4]+'%">'+(p[3]==='dn'?'<b>Oct 31, Nov 1, Nov 3</b>Runs JRK, GRD, SAU':'<b>'+p[0]+'</b>'+p[1])+'</div>':'');}).join('')+'</div>'+
'<div class="sec in"><h4><span>Shelf life</span><span class="ch c-idle">30 days from pack</span></h4><div class="tb fg"><div class="row h"><span>Lot</span><span>Product</span><span>Made</span><span class="r">Use by</span></div>'+
'<div class="row"><span class="mono">'+LOT.id+'</span><span>Raw beef</span><span>Packed '+LOT.pack+'</span><span class="r">'+LOT.use+'</span></div>'+RUNS.map(function(r){return '<div class="row"><span class="mono">'+r.id+'</span><span>'+r.nm+'</span><span>'+r.dt+'</span><span class="r"><span class="ch c-ok">In date</span></span></div>';}).join('')+'</div></div>';}}
d+='<div class="tot">Every record stays on the lot, from receiving to the customer.</div>';
$('dt').innerHTML=d;
}
function resetState(){S={op:false,vw:'none',rn:false,cu:false,tr:false};render();}
var ST=[
{id:'op',target:function(){return $('srb');},prompt:'Search lot BEEF-24-0731',where:'below',run:function(){S.op=true;render();},
 after:function(){return['A supplier lot found',LOT.id+' from '+LOT.sup+', '+n0(LOT.rec)+' kg received.'];}},
{id:'rn',target:function(){return $('t-rn');},prompt:'See the runs that used it',where:'below',run:function(){S.rn=true;S.vw='rn';render();},
 after:function(){return['The runs that used it',RUNS.map(function(r){return r.id;}).join(', ')+': '+n0(used())+' kg used, '+n0(left())+' kg left.'];}},
{id:'cu',target:function(){return $('t-cu');},prompt:'List the customers',where:'below',run:function(){S.cu=true;S.vw='cu';render();},
 after:function(){return['Customers and shipments it reached','Lakeside Market '+n0(cust('Lakeside Market'))+' kg and Ridge Foods '+n0(cust('Ridge Foods'))+' kg across 3 finished lots.'];}},
{id:'dt',target:function(){return $('t-dt');},prompt:'Open the dates',where:'below',run:function(){S.vw='dt';render();},
 after:function(){return['Pack and use by dates','Packed '+LOT.pack+', use by '+LOT.use+'. Every run sits inside that window.'];}},
{id:'tr',target:function(){return $('trb');},prompt:'Trace order SO-8841',where:'right',run:function(){S.tr=true;render();},
 after:function(){return['A customer order traced back','SO-8841 goes back through runs JRK-3310 and GRD-3314 to one supplier lot, '+LOT.id+'.'];}}];
'''
