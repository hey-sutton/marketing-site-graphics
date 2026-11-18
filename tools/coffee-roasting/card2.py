"""Coffee roasting card 2: Green Lots & Roast Yield.
Layout: record form with a side summary panel. On the left the green lot record, the roast log form and the trace panel;
on the right a summary of green lots on hand, shrink by origin and roast level, and roasted lots.
A green lot keeps its origin, supplier, arrival date and bag count. Logging a 60.0 kg roast drops the lot balance by
exactly 60.0 kg, the roasted weight typed in gives the roast loss, shrink averages by origin and roast level, and a
roasted lot traces back to its green lots.
The README example said 60 kg in and 50.4 kg out is a 14.0% loss; that is 16.0%. This card keeps 14.0% and uses 51.6 kg.
All weights are kept in grams and percentages in tenths, so every number is exact."""
from frame_auto import header

SUMMARY = 'Green Lots & Roast Yield (open a green lot with origin, supplier and bags, log a roast and watch the balance drop, record roasted weight and read the roast loss, compare shrink by origin and roast level, trace a roasted lot to its green lots)'
ARIA = 'Interactive product screen: green lot GL-4471, Ethiopia Guji, 840.0 kg on hand; a 60.0 kg roast drops it to 780.0 kg, 51.6 kg roasted out is a 14.0% loss, shrink compares across Ethiopia, Colombia and Brazil and light, medium and dark roasts, and roasted lot RL-8820 traces back to three green lots'
STEPS = 5
STUDIO = dict(lede='A typical green lot and roast yield screen, built on your Sutton data with Studio. Want it different? Describe the change.',
              examples=['Warn when shrink runs high', 'Add moisture and density', 'Track cupping scores', 'Reorder green by forecast'],
              built_on='Green lots, roast batches and BOMs', change='Fields, roast levels and alerts')

ICON = '<path d="M8 2c3 0 5 2.6 5 6s-2 6-5 6-5-2.6-5-6 2-6 5-6z"/><path d="M8 2.5c-1.6 2-1.6 4 0 5.5s1.6 3.5 0 5.5"/>'

CSS = (
 '.k2{padding:10px 40px 0 16px;display:flex;flex-direction:column;gap:10px}'
 '.k2s{height:44px;flex:none;display:flex;align-items:center;gap:8px;padding:0 10px}.k2s .fld{flex-direction:row;align-items:center;gap:8px;position:relative}.k2s .fld small{font-size:10px;color:#18181B;font-weight:600;white-space:nowrap}'
 '#gin{width:150px;font-size:10.4px;padding:6px 8px}.k2s .fld .em,.glog .fld .em{position:absolute;left:0;top:30px;white-space:nowrap;background:#fff;padding:1px 4px;z-index:3}'
 '.gsm{display:inline-flex;align-items:center;gap:5px;font-size:9.4px;color:#71717A}.gsm .bt{font-size:9.6px;padding:4px 8px}'
 '.k2m{display:grid;grid-template-columns:392px 258px;gap:10px;height:482px;flex:none}.k2l,.k2r{display:flex;flex-direction:column;gap:8px;min-width:0}'
 '.grec{height:170px;flex:none}.glog{height:166px;flex:none}.gtr{flex:1 1 auto}.glots{height:178px;flex:none}.gshr{height:152px;flex:none}.grl{flex:1 1 auto}'
 '.grec .empt,.glog .empt,.gtr .empt,.glots .empt,.gshr .empt,.grl .empt{margin:8px 10px;height:calc(100% - 46px);padding:8px}'
 '.gg{display:grid;grid-template-columns:repeat(3,1fr);gap:7px 12px;padding:8px 11px}.gg .kv small{font-size:8.6px}.gg .kv b{font-size:10.2px}.gg .kv b.mono{font-size:10.4px}.gg .kv.hit b{color:#B45309}'
 '.gbar{margin:0 11px;height:8px;border-radius:4px;background:#F4F4F5;overflow:hidden}.gbar i{display:block;height:100%;background:#52525B;border-radius:4px;transition:width .6s cubic-bezier(.22,.9,.28,1)}.gbn{display:flex;justify-content:space-between;padding:4px 11px 0;font-size:8.6px;color:#71717A}'
 '.lg{display:grid;grid-template-columns:repeat(4,1fr);gap:7px 10px;padding:8px 11px 4px;align-items:end}.lg .kv small{font-size:8.6px}.lg .kv b{font-size:10.4px;font-family:"JetBrains Mono",ui-monospace,monospace}'
 '.glog .fld{position:relative}.glog .fld input{width:78px;font-size:10.4px}.glog .fld small{font-size:8.6px}'
 '.lsr{display:flex;align-items:center;gap:8px;padding:6px 11px 0}.lsr .bt{font-size:9.6px}.lres{margin:8px 11px 0;padding:6px 9px;border-radius:7px;background:#FAFAFA;border:1px solid #F0F0F1;display:flex;justify-content:space-between;align-items:center;font-size:9.4px}.lres b{font-family:"JetBrains Mono",ui-monospace,monospace;font-size:13px}.lres.ok{background:#F0FDF4;border-color:#BBF7D0}'
 '.glots .row{grid-template-columns:1fr 42px 70px;min-height:31px;font-size:9.2px;padding:0 10px}.glots .row.h{min-height:20px}.glots .row>span:not(:first-child){text-align:right;font-family:"JetBrains Mono",ui-monospace,monospace}'
 '.gn{display:flex;flex-direction:column;gap:1px;min-width:0}.gn b{font-weight:600;white-space:nowrap}.gn small{font-family:"JetBrains Mono",ui-monospace,monospace;font-size:8.4px;color:#71717A}.glots .row.on{background:#FFFBEB}.gtot{display:flex;justify-content:space-between;padding:5px 10px;border-top:1px solid #F0F0F1;font-size:9.2px}.gtot b{font-family:"JetBrains Mono",ui-monospace,monospace}'
 '.gshr .row{grid-template-columns:62px repeat(4,1fr);min-height:20px;font-size:9px;padding:0 10px;gap:4px}.gshr .row.h{min-height:20px}.gshr .row>span:not(:first-child){text-align:right;font-family:"JetBrains Mono",ui-monospace,monospace}.gshr .row.al{background:#FAFAFA;font-weight:600}.gshr .hi{color:#B45309;font-weight:600}'
 '.grl .empt{justify-content:flex-start;height:auto;padding:10px 8px}.grl .row{grid-template-columns:54px 1fr auto;min-height:30px;font-size:9px;padding:0 10px}.grl .row .mono{font-weight:600}.grl .bt{font-size:9px;padding:3px 8px}'
 '.tw{display:grid;grid-template-columns:118px 1fr;gap:10px;padding:8px 11px}.tn{border:1px solid #D4D4D8;border-radius:7px;padding:7px 8px;display:flex;flex-direction:column;gap:2px;font-size:8.6px;color:#71717A;align-self:start}.tn b{font-family:"JetBrains Mono",ui-monospace,monospace;font-size:10px;color:#18181B}'
 '.tl{display:flex;flex-direction:column;gap:5px}.tr{display:grid;grid-template-columns:96px 1fr 50px;gap:6px;align-items:center;font-size:8.8px}.tr .mono{font-weight:600}.tr .b{height:7px;border-radius:4px;background:#F4F4F5;overflow:hidden}.tr .b i{display:block;height:100%;background:#A1A1AA;border-radius:4px}.tr>span:last-child{text-align:right;font-family:"JetBrains Mono",ui-monospace,monospace}'
 '.tsum{grid-column:1/3;margin-top:-4px;display:flex;justify-content:space-between;padding:5px 8px;border-radius:6px;background:#FAFAFA;font-size:9px}.tsum b{font-family:"JetBrains Mono",ui-monospace,monospace}'
)

WIN = (
 header(ICON, 'Green lots and roast yield', 'Green coffee in, roasted coffee out', '<span class="ch c-idle" id="gst">No lot open</span>')
 + '<div class="k2"><div class="cd k2s frm" id="gsf"><label class="fld" id="gfl"><small>Green lot</small><input id="gin" value="" placeholder="Lot or origin" autocomplete="off" spellcheck="false" aria-label="Green lot number or origin"><span class="em" id="gem">No lot found. Try GL-4471</span></label>'
 '<button type="button" class="bt pri" id="gsb">Open lot</button><span class="gsm">Sample<button type="button" class="bt" id="gsm" data-sample>GL-4471</button></span></div>'
 '<div class="k2m"><div class="k2l"><div class="cd grec" id="grec"></div><div class="cd glog frm" id="glog"></div><div class="cd gtr" id="gtr"></div></div>'
 '<div class="k2r"><div class="cd glots" id="glots"></div><div class="cd gshr" id="gshr"></div><div class="cd grl" id="grl"></div></div></div></div>'
)

JS = r'''
var FOC='.hd>*,.k2s>*,.grec,.glog,.gtr,.glots,.gshr,.grl';
/* green lots, weights in grams */
var LOTS=[{id:'GL-4471',o:'Ethiopia',r:'Guji, washed',sup:'Highland Trade Partners',arr:'Oct 28',bags:20,bw:60000,bal:840000},
{id:'GL-4502',o:'Colombia',r:'Huila, washed',sup:'Cordillera Green Imports',arr:'Oct 14',bags:25,bw:70000,bal:980000},
{id:'GL-4510',o:'Brazil',r:'Cerrado, natural',sup:'Serra Alta Trading',arr:'Sep 30',bags:30,bw:60000,bal:1260000}];
var NEW={id:'RB-5120',lot:0,lv:'Medium',g:60000};
/* earlier batches: origin index, roast level, green in, roasted out (grams) */
var HIST=[[0,'Light',60000,52500],[0,'Light',40000,35000],[0,'Medium',60000,51000],[0,'Dark',30000,25200],
[1,'Light',60000,52800],[1,'Medium',60000,52200],[1,'Dark',60000,50400],[2,'Light',60000,52200],[2,'Medium',60000,51300],[2,'Dark',60000,49800]];
var LV=['Light','Medium','Dark'];
var RL=[{id:'RL-8820',p:'Foundry espresso',d:'Nov 17',out:43000,use:[[0,20000],[1,18000],[2,12000]]},{id:'RL-8807',p:'Guji single origin',d:'Nov 16',out:25800,use:[[0,30000]]}];
var S;
function kg(g){return (g/1000).toLocaleString('en-US',{minimumFractionDigits:1,maximumFractionDigits:1});}
function p1(lossG,inG){return (Math.round(lossG*1000/inG)/10).toFixed(1)+'%';}
function bal(i){return LOTS[i].bal-(S.log&&i===NEW.lot?NEW.g:0);}
function bagsLeft(i){return Math.floor(bal(i)/LOTS[i].bw);}
function allBal(){return LOTS.reduce(function(s,l,i){return s+bal(i);},0);}
function batches(){var b=HIST.slice();if(S.out)b.push([NEW.lot,NEW.lv,NEW.g,S.out]);return b;}
function shr(fo,fl){var a=0,z=0;batches().forEach(function(x){if((fo<0||x[0]===fo)&&(!fl||x[1]===fl)){a+=x[2];z+=x[3];}});return a?p1(a-z,a):'';}
function render(){
var L=LOTS[0],R=$('grec');
if(!S.open)R.innerHTML='<div class="ct"><span>Green lot</span></div><div class="empt"><b>No lot open</b><span>Open a green lot to see its origin, supplier, arrival and bags.</span></div>';
else{var kv=[['Lot',L.id,1],['Origin',L.o+' '+L.r],['Supplier',L.sup],['Arrived',L.arr],['Bags',bagsLeft(0)+' of '+L.bags+', '+kg(L.bw)+' kg',0,'gbg'],['Balance',kg(bal(0))+' kg',1,'gbl']];
R.innerHTML='<div class="ct"><span>Green lot '+L.id+'</span><span class="ch c-info">'+L.o+'</span></div><div class="gg">'+kv.map(function(x){return '<span class="kv'+(S.log&&x[3]?' hit':'')+'"><small>'+x[0]+'</small><b'+(x[2]?' class="mono"':'')+(x[3]?' id="'+x[3]+'"':'')+'>'+x[1]+'</b></span>';}).join('')+'</div><div class="gbar"><i style="width:'+(bal(0)/(L.bags*L.bw)*100).toFixed(1)+'%"></i></div><div class="gbn"><span>Received '+kg(L.bags*L.bw)+' kg</span><span>'+kg(L.bags*L.bw-bal(0))+' kg roasted</span></div>';}
var G=$('glog');
if(!S.open)G.innerHTML='<div class="ct"><span>Roast log</span></div><div class="empt"><b>No roast logged</b><span>Log a batch against this lot to draw down its balance.</span></div>';
else if(!S.log)G.innerHTML='<div class="ct"><span>Roast log</span><span class="ch c-idle">Roaster 1</span></div><div class="lg"><span class="kv"><small>Batch</small><b>'+NEW.id+'</b></span><span class="kv"><small>Roast level</small><b>'+NEW.lv+'</b></span><span class="kv"><small>Green in</small><b>'+kg(NEW.g)+' kg</b></span><span class="kv"><small>From lot</small><b>'+L.id+'</b></span></div><div class="lsr"><button type="button" class="bt pri" id="glb">Log roast batch</button><span class="mut" style="font-size:8.8px">Draws '+kg(NEW.g)+' kg from '+L.id+'</span></div>';
else{var done=!!S.out;G.innerHTML='<div class="ct"><span>Roast log '+NEW.id+'</span><span class="ch '+(done?'c-ok':'c-warn')+'">'+(done?'Recorded':'Scale read, check it')+'</span></div><div class="lg"><span class="kv"><small>Roast level</small><b>'+NEW.lv+'</b></span><span class="kv"><small>Green in</small><b id="ggi">'+kg(NEW.g)+' kg</b></span>'
+'<label class="fld" id="gofl"><small>Roasted out, kg</small><input id="gout" value="'+(done?kg(S.out):S.typed)+'" placeholder="0.0" inputmode="decimal" autocomplete="off" aria-label="Roasted weight out in kilograms"'+(done?' readonly':'')+'><span class="em" id="goem">Enter 40.0 to 59.9 kg</span></label>'
+'<span class="kv"><small>Weight lost</small><b id="glw">'+(done?kg(NEW.g-S.out)+' kg':'')+'</b></span></div>'
+'<div class="lsr">'+(done?'':'<button type="button" class="bt pri" id="gsv">Record weight</button><span class="mut" style="font-size:8.8px">Read from the roaster scale. Edit it if needed.</span>')+'</div>'
+(done?'<div class="lres ok"><span>Roast loss for '+NEW.id+'</span><b id="gls">'+p1(NEW.g-S.out,NEW.g)+'</b></div>':'');}
var O=$('glots');
if(!S.open)O.innerHTML='<div class="ct"><span>Green on hand</span></div><div class="empt"><b>Nothing listed yet</b><span>Every green lot by origin, with bags and kg left.</span></div>';
else O.innerHTML='<div class="ct"><span>Green on hand</span><span class="ch c-info">3 origins</span></div><div class="row h"><span>Origin, lot</span><span>Bags</span><span>Balance</span></div>'+LOTS.map(function(l,i){return '<div class="row'+(i===0?' on':'')+'"><span class="gn"><b>'+l.o+'</b><small>'+l.id+'</small></span><span id="gb'+i+'">'+bagsLeft(i)+'</span><span id="gk'+i+'">'+kg(bal(i))+'</span></div>';}).join('')+'<div class="gtot"><span>Total green</span><b id="gtt">'+kg(allBal())+' kg</b></div>';
var H=$('gshr');
if(!S.cmp)H.innerHTML='<div class="ct"><span>Shrink by origin and level</span>'+(S.out?'<button type="button" class="bt pri" id="gcb">Compare shrink</button>':'')+'</div><div class="empt"><b>Not compared yet</b><span>Average roast loss by origin and by light, medium and dark.</span></div>';
else{var hd='<div class="row h"><span>Origin</span>'+LV.map(function(v){return '<span>'+v+'</span>';}).join('')+'<span>All</span></div>';
var rows=LOTS.map(function(l,i){return '<div class="row"><span>'+l.o+'</span>'+LV.map(function(v){return '<span'+(i===0&&v===NEW.lv?' class="hi"':'')+' id="gx'+i+v[0]+'">'+shr(i,v)+'</span>';}).join('')+'<span id="gx'+i+'A">'+shr(i)+'</span></div>';}).join('');
H.innerHTML='<div class="ct"><span>Shrink by origin and level</span><span class="ch c-idle">'+batches().length+' batches</span></div>'+hd+rows+'<div class="row al"><span>All origins</span>'+LV.map(function(v){return '<span id="gxA'+v[0]+'">'+shr(-1,v)+'</span>';}).join('')+'<span id="gxAA">'+shr(-1)+'</span></div>';}
var U=$('grl');
if(!S.open)U.innerHTML='<div class="ct"><span>Roasted lots</span></div><div class="empt"><b>No roasted lots</b><span>Roasted lots made from this coffee.</span></div>';
else U.innerHTML='<div class="ct"><span>Roasted lots from '+L.id+'</span></div>'+RL.map(function(r,i){return '<div class="row"><span class="mono">'+r.id+'</span><span>'+r.p+', '+r.d+'</span><span>'+(i===0&&S.cmp&&!S.tr?'<button type="button" class="bt pri" id="gtb">Trace</button>':i===0&&S.tr?'<span class="ch c-ok">Traced</span>':'<span class="ch c-idle">'+kg(r.out)+' kg</span>')+'</span></div>';}).join('');
var T=$('gtr');
if(!S.tr)T.innerHTML='<div class="ct"><span>Trace</span></div><div class="empt"><b>Nothing traced yet</b><span>Pick a roasted lot to see the green lots it used.</span></div>';
else{var r=RL[0],tin=r.use.reduce(function(s,u){return s+u[1];},0),mx=Math.max.apply(null,r.use.map(function(u){return u[1];}));
T.innerHTML='<div class="ct"><span>Trace '+r.id+'</span><span class="ch c-info">'+r.use.length+' green lots</span></div><div class="tw"><div class="tn"><b>'+r.id+'</b><span>'+r.p+'</span><span>Roasted '+r.d+'</span><span>'+kg(r.out)+' kg roasted</span></div><div class="tl">'+r.use.map(function(u,i){var l=LOTS[u[0]];return '<div class="tr"><span><span class="mono">'+l.id+'</span> <span class="mut">'+l.o+'</span></span><span class="b"><i style="width:'+(u[1]/mx*100).toFixed(0)+'%"></i></span><span id="gt'+i+'">'+kg(u[1])+' kg</span></div>';}).join('')+'</div><div class="tsum"><span id="gts">'+kg(tin)+' kg green in, '+kg(r.out)+' kg out</span><b id="gtl">'+p1(tin-r.out,tin)+' loss</b></div></div>';}
var st=$('gst');st.textContent=S.tr?'Lot traced':S.out?'Roast recorded':S.log?'Roast logged':S.open?'Lot open':'No lot open';st.className='ch '+(S.out?'c-ok':S.open?'c-info':'c-idle');}
function val(){return String($('gin').value).trim().toLowerCase().replace(/\s+/g,' ');}
function outVal(){var e=$('gout');if(!e)return NaN;var v=String(e.value).trim().replace(',','.');return /^\d{2}(\.\d)?$/.test(v)?Math.round(parseFloat(v)*1000):NaN;}
$('gsm').addEventListener('click',function(){$('gin').value='GL-4471';$('gfl').classList.remove('err');});
winEl.addEventListener('input',function(e){if(e.target&&e.target.id==='gout')S.typed=e.target.value;});
function typeIn(id,t,done){var i=0;(function k(){$(id).value=t.slice(0,i);if(i<t.length){i++;later(k,70);}else done();})();}
function resetState(){S={open:false,log:false,out:0,typed:'51.6',cmp:false,tr:false};$('gin').value='';$('gfl').classList.remove('err');render();}
var CAPAT=function(hh){return cur===2?{l:14,t:visH()-hh-14}:cur>=3?{l:14,t:150}:{l:14,t:visH()-hh-14};};
var ST=[
{id:'lot',target:function(){return mode==='try'?$('gsb'):$('gin');},prompt:'Click Open lot to open green lot GL-4471',where:'below',
 ok:function(){if(!val())$('gin').value='GL-4471';var v=val(),b=!(v==='gl-4471'||v==='gl 4471'||v==='4471'||v==='ethiopia');$('gem').textContent=v?'No lot found. Try GL-4471':'Enter a lot, for example GL-4471';$('gfl').classList.toggle('err',b);return !b;},
 run:function(quick){var go=function(){$('gin').value='GL-4471';$('gfl').classList.remove('err');S.open=true;render();};if(mode==='watch'&&!quick)typeIn('gin','GL-4471',go);else go();},
 after:function(){var l=LOTS[0];return['Every green lot keeps its source',l.id+', '+l.o+' '+l.r.split(',')[0]+' from '+l.sup+', arrived '+l.arr+': '+bagsLeft(0)+' of '+l.bags+' bags left, '+kg(bal(0))+' kg.'];}},
{id:'log',target:function(){return $('glb');},prompt:'Log a roast batch against this lot',where:'below',run:function(){S.log=true;render();},
 after:function(){var l=LOTS[0];return['A roast draws down the lot',NEW.id+' takes '+kg(NEW.g)+' kg of green: '+l.id+' drops from '+kg(l.bal)+' to '+kg(bal(0))+' kg, '+bagsLeft(0)+' bags.'];}},
{id:'out',target:function(){return $('gsv');},prompt:'Check the roasted weight, 51.6 kg, then Record weight',where:'below',
 ok:function(){var g=outVal(),b=!(g>=40000&&g<60000);$('gofl').classList.toggle('err',b);return !b;},
 run:function(quick){var g=quick||mode==='watch'?51600:outVal();S.out=g>=40000&&g<60000?g:51600;render();},
 after:function(){return['Roast loss from the scale',kg(NEW.g)+' kg in, '+kg(S.out)+' kg out: '+kg(NEW.g-S.out)+' kg lost, a roast loss of '+p1(NEW.g-S.out,NEW.g)+'.'];}},
{id:'cmp',target:function(){return $('gcb');},prompt:'Click Compare shrink',where:'below',run:function(){S.cmp=true;render();},
 after:function(){return['Shrink by origin and roast level',LOTS.map(function(l,i){return l.o+' '+shr(i);}).join(', ')+'. Light roasts lose '+shr(-1,'Light')+', dark '+shr(-1,'Dark')+'.'];}},
{id:'tr',target:function(){return $('gtb');},prompt:'Trace roasted lot RL-8820',where:'above',run:function(){S.tr=true;render();},
 after:function(){var r=RL[0],tin=r.use.reduce(function(s,u){return s+u[1];},0);return['Every roasted lot traces back',r.id+' used '+r.use.map(function(u){return kg(u[1])+' kg from '+LOTS[u[0]].id;}).join(', ')+': '+kg(tin)+' kg of green.'];}}];
'''
