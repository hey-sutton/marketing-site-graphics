"""Food brand inventory card 1: Stock at Every Location. Layout: a record form with a side summary panel.
Left: the read only item field with Look up, then the stock record by location (brand owned stock counted, partner owned
stock kept apart), the co-packer's lots with best before dates, a transfer with preset quantity chips, the Committed
toggle and the partner report comparison. Right: the summary panel (total, by location, committed, available, open
differences). Every number is computed from the data below."""
from frame_auto import header

SUMMARY = 'Stock at Every Location (look up Trail Mix Case, open the co-packer lots, transfer 1,000 cases to the 3PL, show committed and available, compare with the partner report)'
ARIA = 'Interactive product screen: look up Trail Mix Case, see on hand at the brand warehouse, the co-packer and the 3PL, open the co-packer lots by best before date, transfer cases to the 3PL, see committed and available stock, and compare on hand with the partner report'
STEPS = 5
STUDIO = dict(lede='A typical stock screen on your Sutton data. Want it different? Describe the change.',
              examples=['A column per sales channel', 'Cases and pallets side by side', 'A weekly partner count reminder', 'A low stock alert per location'],
              built_on='Items, locations, lots and orders', change='Columns, owners and views')

ICON = '<path d="M2.5 5.2L8 2.5l5.5 2.7v5.6L8 13.5l-5.5-2.7z M2.5 5.2L8 8l5.5-2.8M8 8v5.5"/>'

CSS = (
 '.fld input[readonly]{background:#F4F4F5;color:#3F3F46;cursor:default;pointer-events:none}'
 '.g1{display:grid;grid-template-columns:420px 226px;grid-template-rows:62px 468px;gap:10px;padding:10px 44px 0 16px}'
 '.srch{display:flex;flex-direction:column;justify-content:center;gap:5px;padding:0 12px}.srch .frm{display:flex;align-items:flex-end;gap:8px}.srch .fld{flex:1}'
 '.srch .ctx{font-size:8.9px;color:#71717A}'
 '.stk{display:flex;flex-direction:column}.stk .empt{margin:10px;flex:1}.sum{grid-column:2;grid-row:1/3;display:flex;flex-direction:column}.sum .empt{margin:10px;flex:1}'
 '.sw{display:inline-flex;align-items:center;gap:6px;font-size:9.4px;font-weight:500;border:1px solid #E4E4E7;border-radius:6px;padding:3px 8px;background:#fff;cursor:pointer}'
 '.sw i{width:20px;height:11px;border-radius:6px;background:#D4D4D8;position:relative;transition:background .2s}.sw i::after{content:"";position:absolute;left:1px;top:1px;width:9px;height:9px;border-radius:50%;background:#fff;transition:left .2s}'
 '.sw.on i{background:#18181B}.sw.on i::after{left:10px}.sw:focus-visible{outline:2px solid #18181B;outline-offset:2px}.ct .acts{display:flex;align-items:center;gap:6px}.ct .acts .bt{font-size:9.4px;padding:3px 8px}'
 '.loc .row{grid-template-columns:1fr 64px 62px;font-size:9.6px;min-height:34px}.loc.c5 .row{grid-template-columns:1fr 64px 54px 62px 62px}.loc .row>span:nth-child(n+3){text-align:right;font-family:"JetBrains Mono",ui-monospace,monospace}'
 '.loc .row.h{min-height:24px}.loc .row.h>span{font-family:inherit!important}.loc .nm b{display:block;font-weight:600}.loc .nm small{display:block;color:#71717A;font-size:8.4px}'
 '.loc .row.pt{color:#71717A;background:#FAFAFA;min-height:30px}.loc .row.t{font-weight:600;background:#FAFAFA;min-height:28px}.loc button.row.sel{background:#F4F4F5}'
 '.lots{border-top:1px solid #E4E4E7}.lots .sub{display:flex;justify-content:space-between;padding:7px 11px 3px;font-size:9px;color:#71717A;font-weight:500}'
 '.lots .row{grid-template-columns:1fr 112px 70px;font-size:9.6px;min-height:27px}.lots .row span:last-child{text-align:right;font-family:"JetBrains Mono",ui-monospace,monospace}'
 '.xf{display:flex;align-items:center;gap:6px;padding:7px 11px;border-top:1px solid #F0F0F1;font-size:9.4px}.xf .lb{color:#52525B;margin-right:auto}'
 '.pk{font:inherit;font-family:"JetBrains Mono",ui-monospace,monospace;font-size:9.4px;padding:3px 8px;border:1px solid #E4E4E7;border-radius:999px;background:#fff;cursor:pointer}.pk.on{background:#18181B;border-color:#18181B;color:#fff}.pk:focus-visible{outline:2px solid #18181B;outline-offset:2px}'
 '.xf .bt{font-size:9.4px;padding:4px 9px}.xf.ok{background:#F0FDF4}'
 '.dif{margin:9px 11px 0;padding:8px 10px;border-radius:7px;background:#FFFBEB;border:1px solid #FDE68A;display:grid;grid-template-columns:1fr 1fr 74px;gap:8px;align-items:end}.dif .kv b{font-size:12px}.dif .kv small{font-size:8.4px}'
 '.tot{margin-top:auto;padding:9px 11px;border-top:1px solid #E4E4E7;font-size:9.1px;color:#52525B;line-height:1.4;background:#FAFAFA}'
 '.sum .tot{padding-right:90px}.sum .bx{padding:10px 11px 0}.sum .big{font-size:24px}.sum .kv small{font-size:8.8px}'
 '.bars{padding:8px 11px 0;display:flex;flex-direction:column;gap:7px}.bar{display:grid;grid-template-columns:1fr auto;gap:3px 6px;font-size:9.2px}.bar b{font-family:"JetBrains Mono",ui-monospace,monospace;font-weight:500}'
 '.bar i{grid-column:1/3;display:block;height:6px;border-radius:3px;background:#F4F4F5;overflow:hidden}.bar i em{display:block;height:100%;background:#52525B;transition:width .5s ease}'
 '.pair{display:grid;grid-template-columns:1fr 1fr;gap:8px;padding:10px 11px 0}.pair .kv b{font-size:13px;font-family:"JetBrains Mono",ui-monospace,monospace;font-weight:600}'
 '.note{margin:10px 11px 0;padding:7px 9px;border-radius:7px;font-size:9px;line-height:1.4;background:#FAFAFA;border:1px solid #F0F0F1;color:#52525B}.note.w{background:#FFFBEB;border-color:#FDE68A;color:#92400E}'
)

WIN = (
 header(ICON, 'Item stock', 'Finished goods at the warehouse, co-packer and 3PL')
 + '<div class="g1"><div class="cd srch" id="srch"><div class="frm"><label class="fld"><small>Item</small>'
 '<input id="iit" value="Trail Mix Case" readonly tabindex="-1" autocomplete="off" spellcheck="false"></label>'
 '<button type="button" class="bt pri" id="lkb">Look up</button></div><div class="ctx">Finished case, 12 bags of 10 oz</div></div>'
 '<div class="cd stk" id="stk"></div><div class="cd sum" id="sum"></div></div>'
)

JS = r'''
var FOC='.hd>*,.srch,.stk .ct,.loc .row,.lots .sub,.lots .row,.xf,.dif,.stk .tot,.sum>*';
var LOC=[{id:'wh',nm:'Fernhill warehouse',ty:'Brand warehouse',oh:1200,cm:400},{id:'cp',nm:'Ridgeway Co-Pack',ty:'Co-packer',oh:3400,cm:0},{id:'tp',nm:'Harbor 3PL East',ty:'3PL',oh:5000,cm:2500}];
var PART={nm:'Ridgeway Co-Pack',q:450};
var LOT0=[{id:'TM-2611',bb:'Mar 14, 2027',q:1400},{id:'TM-2618',bb:'Apr 2, 2027',q:2000}];
var CHIPS=[500,1000,1500],REP={q:3100,d:'Nov 17'},TR='TR-3302';
var S,LOTS,MV;
function L(id){return LOC.filter(function(x){return x.id===id;})[0];}
function oh(id){var x=L(id);return x.oh+(id==='cp'?-MV:id==='tp'?MV:0);}
function tot(){return LOC.reduce(function(a,x){return a+oh(x.id);},0);}
function cmt(){return LOC.reduce(function(a,x){return a+x.cm;},0);}
function av(id){return oh(id)-L(id).cm;}
function snap(){return LOT0.reduce(function(a,l){return a+l.q;},0);}
function move(q){var left=q;MV=q;LOTS=LOT0.map(function(l){var t=Math.min(l.q,left);left-=t;return {id:l.id,bb:l.bb,q:l.q-t,mv:t};});}
function render(){
var s='<div class="ct"><span>Stock by location</span>'+(S.look?'<span class="acts"><button type="button" class="sw'+(S.cmt?' on':'')+'" id="cmt" aria-pressed="'+(S.cmt?'true':'false')+'"><i></i>Committed</button>'+(S.cmp?'<button type="button" class="bt done" disabled>Compared</button>':'<button type="button" class="bt" id="cmp">Compare</button>')+'</span>':'')+'</div>';
if(!S.look)s+='<div class="empt"><b>No item selected</b><span>Look up an item to see its quantity at every location, with the lots behind each number.</span></div>';
else{s+='<div class="loc'+(S.cmt?' c5':'')+'"><div class="row h"><span>Location</span><span>Owner</span><span>On hand</span>'+(S.cmt?'<span>Committed</span><span>Available</span>':'')+'</div>'+
LOC.map(function(x){return '<button type="button" class="row in'+(S.open&&x.id==='cp'?' sel':'')+'" id="r-'+x.id+'"><span class="nm"><b>'+x.nm+'</b><small>'+x.ty+'</small></span><span><span class="ch c-info">Brand</span></span><span id="oh-'+x.id+'">'+n0(oh(x.id))+'</span>'+(S.cmt?'<span id="cm-'+x.id+'">'+n0(x.cm)+'</span><span id="av-'+x.id+'"><b>'+n0(av(x.id))+'</b></span>':'')+'</button>';}).join('')+
'<div class="row pt"><span class="nm"><b>'+PART.nm+'</b><small>Partner owned, kept apart</small></span><span><span class="ch c-idle">Partner</span></span><span id="ohp">'+n0(PART.q)+'</span>'+(S.cmt?'<span></span><span></span>':'')+'</div>'+
'<div class="row t"><span>Brand owned total</span><span></span><span id="oht">'+n0(tot())+'</span>'+(S.cmt?'<span id="cmtt">'+n0(cmt())+'</span><span id="avt">'+n0(tot()-cmt())+'</span>':'')+'</div></div>';
if(S.open){s+='<div class="lots in"><div class="sub"><span>Ridgeway Co-Pack lots</span><span>Best before</span></div>'+LOTS.map(function(l){return '<div class="row"><span><b class="mono">'+l.id+'</b>'+(l.mv?' <span class="ch c-ok">'+n0(l.mv)+' moved</span>':'')+'</span><span>'+l.bb+'</span><span id="lq-'+l.id+'">'+n0(l.q)+'</span></div>';}).join('');
if(!S.moved)s+='<div class="xf" id="xf"><span class="lb">Transfer to Harbor 3PL East</span>'+CHIPS.map(function(q){return '<button type="button" class="pk'+(S.qty===q?' on':'')+'" data-pick="1" data-q="'+q+'" id="q-'+q+'" aria-pressed="'+(S.qty===q?'true':'false')+'">'+n0(q)+'</button>';}).join('')+'<button type="button" class="bt pri" id="tfb">Transfer</button></div>';
else s+='<div class="xf ok in" id="xf"><span class="ch c-ok">'+TR+' posted</span><span class="lb" id="xfm">'+n0(MV)+' cases to Harbor 3PL East, oldest best before first</span></div>';
s+='</div>';}
if(S.cmp)s+='<div class="dif in" id="dif"><div class="kv"><small>Ridgeway report, '+REP.d+'</small><b class="mono" id="rep">'+n0(REP.q)+'</b></div><div class="kv"><small>On hand in Sutton, '+REP.d+'</small><b class="mono" id="ohs">'+n0(snap())+'</b></div><div class="kv"><small>Difference</small><b class="mono" id="dfq">'+n0(snap()-REP.q)+'</b></div></div>';}
s+='<div class="tot">Brand owned stock is counted at every location. Partner owned stock stays apart from your total.</div>';
$('stk').innerHTML=s;
var m='<div class="ct"><span>Summary</span>'+(S.look?'<span class="ch c-idle">Trail Mix Case</span>':'')+'</div>';
if(!S.look)m+='<div class="empt"><b>Nothing to sum yet</b><span>Totals, committed stock and partner differences show here.</span></div>';
else{var T=tot();m+='<div class="bx in"><div class="kv"><small>Brand owned on hand</small><b class="big mono" id="sto">'+n0(T)+'</b></div></div>'+
'<div class="bars in">'+LOC.map(function(x){return '<div class="bar"><span>'+x.nm+'</span><b id="sb-'+x.id+'">'+n0(oh(x.id))+'</b><i><em style="width:'+(oh(x.id)/T*100).toFixed(1)+'%"></em></i></div>';}).join('')+'</div>'+
(S.cmt?'<div class="pair in"><div class="kv"><small>Committed</small><b id="scm">'+n0(cmt())+'</b></div><div class="kv"><small>Available</small><b id="sav">'+n0(T-cmt())+'</b></div></div>':'<div class="note">Turn on Committed to see open orders by location.</div>')+
'<div class="note">'+PART.nm+' also holds <b>'+n0(PART.q)+'</b> partner owned cases. They are not in your total.</div>'+
(S.cmp?'<div class="note w in" id="snt">1 open difference: '+n0(snap()-REP.q)+' cases at Ridgeway Co-Pack.</div>':'');}
m+='<div class="tot">One record per item.</div>';
$('sum').innerHTML=m;
}
function resetState(){S={look:false,open:false,qty:0,moved:false,cmt:false,cmp:false};LOTS=LOT0.map(function(l){return {id:l.id,bb:l.bb,q:l.q,mv:0};});MV=0;render();}
winEl.addEventListener('click',function(e){var c=e.target.closest&&e.target.closest('[data-q]');if(c&&!S.moved){S.qty=+c.getAttribute('data-q');render();}});
function capN(){var i=cap.querySelector('.m i');return i?+i.textContent:1;}
var CAPAT=function(hh){return {l:14,t:visH()-hh-14};};
var ST=[
{id:'look',target:function(){return $('lkb');},prompt:'Click Look up for Trail Mix Case',where:'below',run:function(){S.look=true;render();},
 after:function(){return['One screen, every location',LOC.map(function(x){return x.nm+' '+n0(oh(x.id));}).join(', ')+'. Total '+n0(tot())+'.'];}},
{id:'open',target:function(){return $('r-cp');},prompt:'Open Ridgeway Co-Pack',where:'below',run:function(){S.open=true;render();},
 after:function(){return['The lots behind the number',LOT0.map(function(l){return l.id+' '+n0(l.q)+' cases, best before '+l.bb;}).join('. ')+'.'];}},
{id:'xfer',target:function(){return $('tfb');},back:function(){return S.qty?null:[$('q-1000'),'Pick 1,000 cases','above'];},prompt:'Transfer to Harbor 3PL East',where:'above',
 run:function(){if(!S.qty)S.qty=1000;move(S.qty);S.moved=true;render();},
 after:function(){return['Move finished cases to the 3PL','Ridgeway Co-Pack '+n0(oh('cp'))+', Harbor 3PL East '+n0(oh('tp'))+'. Total still '+n0(tot())+'.'];}},
{id:'cmt',target:function(){return $('cmt');},prompt:'Turn on Committed',where:'below',run:function(){S.cmt=true;render();},
 after:function(){return['Committed to open orders at each location','Available: warehouse '+n0(av('wh'))+', co-packer '+n0(av('cp'))+', 3PL East '+n0(av('tp'))+' ('+n0(oh('tp'))+' less '+n0(L('tp').cm)+').'];}},
{id:'cmp',target:function(){return $('cmp');},prompt:'Compare with the partner report',where:'below',run:function(){S.cmp=true;render();},
 after:function(){return['On hand against what the partner reported','Ridgeway reported '+n0(REP.q)+' on '+REP.d+' when Sutton showed '+n0(snap())+'. Difference '+n0(snap()-REP.q)+'.'];}}];
'''
