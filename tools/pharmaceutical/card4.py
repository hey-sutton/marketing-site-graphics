"""Pharmaceutical card 4: Digital Production Records. Layout: an operator tablet. Left, the order input and a step rail of
five large touch tiles (Weigh out, Blend, Encapsulate, In-process check, Package). Right, a record sheet laid out like a
page of a batch record that fills in line by line as steps are logged, each line with a time and the operator's
initials. Counts, yield and bottles are computed from the data below."""
from frame_auto import header

SUMMARY = 'Digital Production Records (open order MO-7210 for batch B-2620, log weigh out by lot scan, blend and encapsulate, an in-process fill weight check, then package and post the bottles to quarantine)'
ARIA = 'Interactive product screen: open manufacturing order MO-7210, log each step of batch B-2620 on an operator tablet with lots, times and initials, record a fill weight check, and post finished bottles to quarantine'
STEPS = 5
STUDIO = dict(lede='A typical operator screen, built on your Sutton data with Studio. Want it different? Describe the change.',
              examples=['A second check at the halfway point', 'A scale reading pulled into weigh out', 'A line clearance step', 'A printed record at the end'],
              built_on='Work orders, BOMs, lots and locations', change='Steps, checks and fields')

ICON = '<rect x="3" y="1.8" width="10" height="12.4" rx="1.4"/><path d="M5.5 5h5M5.5 7.6h5M5.5 10.2h3"/>'

CSS = (
 '.fld input[readonly]{background:#FAFAFA;cursor:default;pointer-events:none}'
 '.g4{display:grid;grid-template-columns:196px 1fr;gap:10px;padding:10px 40px 0 16px}'
 '.sr2{display:flex;flex-direction:column;gap:6px;min-width:0}'
 '.mo{height:118px;flex:none;margin-bottom:4px}.mo .frm{display:flex;align-items:flex-end;gap:6px;padding:8px 10px 0}.mo .fld{flex:1}.mo .smp{display:flex;align-items:center;gap:6px;padding:6px 10px 0;font-size:8.8px;color:#71717A}.mo .smp .bt{font-family:"JetBrains Mono",ui-monospace,monospace;font-size:9px;padding:3px 7px}'
 '.tl2{height:78px;flex:none;border:1px solid #E4E4E7;border-radius:9px;background:#fff;display:grid;grid-template-columns:30px 1fr;grid-template-rows:auto 1fr;column-gap:8px;padding:9px 10px;transition:border-color .3s,background-color .3s,box-shadow .3s}'
 '.tl2 .nb{grid-row:span 2;width:26px;height:26px;border-radius:50%;border:1.5px solid #D4D4D8;display:grid;place-items:center;font-size:10.5px;font-weight:600;color:#71717A;background:#fff}'
 '.tl2 b{font-size:11.4px;font-weight:600;align-self:center}.tl2 .st2{font-size:9px;color:#71717A;align-self:start;margin-top:2px}.tl2 .bt{justify-self:start;align-self:end;font-size:10px;padding:6px 11px;border-radius:7px}'
 '.tl2.now{border-color:#18181B;box-shadow:0 0 0 1px #18181B}.tl2.now .nb{border-color:#18181B;color:#18181B}.tl2.dn{background:#FAFAFA}.tl2.dn .nb{background:#22C55E;border-color:#22C55E;color:#fff}.tl2.off{opacity:.7}'
 '.sht{display:flex;flex-direction:column;background:#fff}.sht .ct .ch{margin-left:auto}'
 '.pg{flex:1;display:flex;flex-direction:column;margin:10px 12px 0;border:1px solid #E4E4E7;border-radius:4px;background:#FFFEFB;box-shadow:0 1px 2px rgba(0,0,0,.04)}'
 '.ph{display:grid;grid-template-columns:repeat(4,1fr);gap:7px 10px;padding:9px 11px;border-bottom:1.5px solid #18181B}.ph .kv b{font-size:10px}.ph .kv b:empty::after{content:"";display:block;height:12px;border-bottom:1px dotted #D4D4D8}'
 '.rl{display:grid;grid-template-columns:40px 74px 1fr 74px 24px;align-items:center;gap:8px;min-height:31px;padding:0 10px;border-bottom:1px solid #EFEDE6;font-size:9.4px}.rl.h{min-height:22px;color:#71717A;font-size:8.8px;font-weight:500;border-bottom:1px solid #D4D4D8}'
 '.rl span:nth-child(4){text-align:right;font-family:"JetBrains Mono",ui-monospace,monospace}.rl .mono{font-size:9.2px}.rl small{display:block;color:#71717A;font-size:8.4px}.rl.t{font-weight:600;background:#F7F6F1}.rl.bl{min-height:31px}'
 '.ini{width:22px;height:22px;border-radius:50%;background:#E4E4E7;color:#3F3F46;display:grid;place-items:center;font-size:8px;font-weight:600}'
 '.pf{margin-top:auto;display:flex;align-items:center;gap:8px;padding:8px 10px;border-top:1.5px solid #18181B;font-size:9.4px;min-height:38px}.pf .ch{font-size:9.6px;padding:3px 8px}'
 '.sht .ft3{height:40px;flex:none;display:flex;align-items:center;padding:0 12px;font-size:9px;color:#71717A}'
)

WIN = (
 header(ICON, 'Production record', 'Operator station, encapsulation room 2')
 + '<div class="g4"><div class="sr2"><div class="cd mo"><div class="ct">Work order</div><div class="frm"><label class="fld" id="fmo"><small>Manufacturing order</small>'
 '<input id="imo" value="MO-7210" readonly tabindex="-1" autocomplete="off" spellcheck="false"></label><button type="button" class="bt pri" id="mob">Open</button></div><div class="smp">Encapsulation room 2, day shift</div>'
 '</div><div id="rl2" class="sr2"></div></div>'
 '<div class="cd sht" id="sht"></div></div>'
)

JS = r'''
var FOC='.hd>*,.mo .ct,.mo .frm>*,.tl2,.sht .ct,.ph,.rl,.pf,.ft3';
var PLAN=200000,PER=100,ISSUED=2000;
var WEIGH=[['07:52','AP-8842','Active ingredient',10204],['07:55','EX-4410','Magnesium stearate',800],['07:58','EX-3190','Microcrystalline cellulose',68996]];
var FILLED=198400,REJ=1600,CHK={avg:399.6,n:20,lo:380,hi:420};
var NAMES=['Weigh out','Blend','Encapsulate','In-process check','Package'];
var S;
function k3(g){return (g/1000).toLocaleString('en-US',{minimumFractionDigits:3,maximumFractionDigits:3});}
function bottles(){return Math.floor(FILLED/PER);}
function pass(){return CHK.avg>=CHK.lo&&CHK.avg<=CHK.hi;}
function yieldPct(){return (FILLED/PLAN*100).toFixed(1);}
function wsum(){return WEIGH.reduce(function(a,w){return a+w[3];},0);}
function render(){
var r='';NAMES.forEach(function(n,i){var dn=S.done>i,now=S.mo&&S.done===i&&!S.closed,btn='';
if(now){btn=i===0?'<button type="button" class="bt pri" id="a-w">Scan lot labels</button>':i===1?'<button type="button" class="bt pri" id="a-b">Log blend and fill</button>':i===3?'<button type="button" class="bt pri" id="a-c">Enter fill weights</button>':i===4?'<button type="button" class="bt pri" id="a-p">Package and post</button>':'';}
var st=!S.mo?'No order selected':dn?['Done 07:58, MK','Done 08:40, MK','Done 11:20, RD','Pass 11:35, RD','Done 14:10, RD'][i]:now?'Next on this order':i===2&&S.done===1?'Logs with blend':'Waiting';
r+='<div class="tl2'+(dn?' dn':now?' now':S.mo?'':' off')+'" id="tl-'+i+'"><span class="nb">'+(dn?'✓':i+1)+'</span><b>'+n+'</b>'+(btn||'<span class="st2">'+st+'</span>')+'</div>';});
$('rl2').innerHTML=r;
var e=function(v){return S.mo?v:'';};
var h='<div class="ct"><span>Batch record'+(S.mo?', B-2620':'')+'</span>'+(S.closed?'<span class="ch c-warn" id="rst">Waiting for release</span>':S.mo?'<span class="ch c-info">In progress</span>':'<span class="ch c-idle">No order</span>')+'</div><div class="pg">'+
'<div class="ph"><div class="kv"><small>Order</small><b class="mono">'+e('MO-7210')+'</b></div><div class="kv"><small>Batch</small><b class="mono">'+e('B-2620')+'</b></div><div class="kv"><small>Product</small><b>'+e('CP-050, 50 mg')+'</b></div><div class="kv"><small>Formula</small><b>'+e('v4')+'</b></div>'+
'<div class="kv"><small>Capsules planned</small><b class="mono" id="pcp">'+e(n0(PLAN))+'</b></div><div class="kv"><small>Bottles planned</small><b class="mono" id="pbt">'+e(n0(PLAN/PER))+'</b></div><div class="kv"><small>Fill weight</small><b>'+e('400 mg')+'</b></div><div class="kv"><small>Room</small><b>'+e('Encapsulation 2')+'</b></div></div>'+
'<div class="rl h"><span>Time</span><span>Step</span><span>Entry</span><span>Quantity</span><span>By</span></div>';
var L=[];
if(S.done>0){WEIGH.forEach(function(w,i){L.push(['<span class="mono">'+w[0]+'</span>','Weigh out','<span class="mono">'+w[1]+'</span> '+w[2]+'<small>Lot label scanned</small>','<span id="w'+i+'">'+k3(w[3])+' kg</span>','MK',i]);});
L.push(['','','Weighed into the blend','<span id="wt">'+k3(wsum())+' kg</span>','','t']);}
if(S.done>1){L.push(['<span class="mono">08:40</span>','Blend','Blended 08:10 to 08:40<small>30 minutes</small>','','MK']);
L.push(['<span class="mono">11:20</span>','Encapsulate','<span id="enc">'+n0(FILLED)+' filled of '+n0(PLAN)+' planned</span><small id="rej">'+n0(REJ)+' rejected</small>','<span>'+n0(FILLED)+'</span>','RD']);}
if(S.done>3)L.push(['<span class="mono">11:35</span>','Check','<span id="chk">Average fill weight '+CHK.avg.toFixed(1)+' mg over '+CHK.n+' capsules</span><small>Limit '+CHK.lo+' to '+CHK.hi+' mg</small>','<span class="ch '+(pass()?'c-ok':'c-bad')+'" id="chr">'+(pass()?'Pass':'Fail')+'</span>','RD']);
if(S.done>4){L.push(['<span class="mono">14:05</span>','Package','<span id="pkt">'+n0(FILLED)+' ÷ '+PER+' = '+n0(bottles())+' bottles</span><small id="pki">'+n0(ISSUED)+' issued, '+n0(ISSUED-bottles())+' returned to stock</small>','<span>'+n0(bottles())+'</span>','RD']);
L.push(['<span class="mono">14:10</span>','Post','<span id="pst">'+n0(bottles())+' bottles to QA-01, quarantine</span><small>Expiry 2028-11-30</small>','','RD']);}
h+=L.map(function(x){return '<div class="rl in'+(x[5]==='t'?' t':'')+'"'+(typeof x[5]==='number'?' style="animation-delay:'+(x[5]*0.15)+'s"':'')+'><span>'+x[0]+'</span><span>'+x[1]+'</span><span>'+x[2]+'</span><span>'+x[3]+'</span><span>'+(x[4]?'<span class="ini">'+x[4]+'</span>':'')+'</span></div>';}).join('');
for(var k=L.length;k<9;k++)h+='<div class="rl bl"><span></span><span></span><span></span><span></span><span></span></div>';
h+='<div class="pf">'+(S.closed?'<span class="ch c-warn" id="pfs">Record complete, waiting for release</span><span class="mut" id="yld">Yield '+yieldPct()+'%</span>':S.mo?'<span class="mut">'+S.done+' of 5 steps logged</span>':'<span class="mut">Lines fill in as each step is logged</span>')+'</div></div><div class="ft3">'+(S.mo?'Every line keeps its time, lot and initials':'Pick an order to start its record')+'</div>';
$('sht').innerHTML=h;
}
function resetState(){S={mo:false,done:0,closed:false};render();}
function capN(){var i=cap.querySelector('.m i');return i?+i.textContent:1;}
var CAPAT=function(hh){var w=cap.offsetWidth;return capN()<=4?{l:visW()-w-14,t:visH()-hh-58}:{l:14,t:visH()-hh-14};};
var ST=[
{id:'mo',target:function(){return $('mob');},prompt:'Click Open for MO-7210',where:'below',
 run:function(quick){var go=function(){S.mo=true;render();};go();},
 after:function(){return['The order brings its steps and a blank record','MO-7210 makes B-2620: '+n0(PLAN)+' capsules, '+n0(PLAN/PER)+' bottles planned.'];}},
{id:'w',target:function(){return $('a-w');},prompt:'Scan the three lot labels',where:'right',run:function(){S.done=1;render();},
 after:function(){return['Each scan writes a line with lot, time and initials','Three lots weighed by MK: '+k3(wsum())+' kg into the blend.'];}},
{id:'b',target:function(){return $('a-b');},prompt:'Log blend and encapsulation',where:'right',run:function(){S.done=3;render();},
 after:function(){return['Blend and encapsulation log in order',n0(FILLED)+' filled of '+n0(PLAN)+' planned, '+n0(REJ)+' rejected.'];}},
{id:'c',target:function(){return $('a-c');},prompt:'Enter the fill weights',where:'right',run:function(){S.done=4;render();},
 after:function(){return['The check records its result against the limit','Average '+CHK.avg.toFixed(1)+' mg over '+CHK.n+' capsules, limit '+CHK.lo+' to '+CHK.hi+' mg: Pass.'];}},
{id:'p',target:function(){return $('a-p');},prompt:'Package and post the bottles',where:'right',run:function(){S.done=5;S.closed=true;render();},
 after:function(){return['Finished bottles post to quarantine',n0(bottles())+' bottles to QA-01, '+n0(ISSUED-bottles())+' returned. Yield '+yieldPct()+'%.'];}}];
'''
