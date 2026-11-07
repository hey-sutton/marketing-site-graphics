"""Electronics card 3: Routing, Kitting & Test Steps. Layout: a station board with five lanes and a rework strip, a batch log, and a side panel for the kit scan and test forms."""
SUMMARY = 'Routing, Kitting & Test Steps (scan a reel to kit, release a batch, move through stations, record tests by serial, rework, close the batch)'
ARIA = 'Interactive product screen: scan a capacitor reel to finish the kit for build MO-3105, release batch B-01 to SMT, move it to test, record a pass and a fail by serial number, then close the batch'
STEPS = 6
STUDIO = dict(lede='A typical station board, built on your Sutton data with Studio. Want it different? Describe the change.',
              examples=['A test checklist per product', 'A rework reason list', 'A station dashboard', 'A kit shortage alert'],
              built_on='Manufacturing orders, routings, serials and stock', change='Stations, test fields and checks')

CSS = (
 '.b3{display:grid;grid-template-columns:428px 1fr;gap:12px;padding:12px 40px 0 16px;height:596px}'
 '.bc{display:flex;flex-direction:column;gap:10px;min-height:0}'
 '.lanes{display:grid;grid-template-columns:repeat(5,1fr);gap:0}.ln3{border-left:1px solid #F0F0F1;min-height:286px;display:flex;flex-direction:column}.ln3:first-child{border-left:0}'
 '.ln3 .lh{display:flex;justify-content:space-between;align-items:center;gap:4px;line-height:1.1;height:28px;padding:0 7px;background:#FAFAFA;border-bottom:1px solid #E4E4E7;font-size:9.6px;font-weight:600}.ln3 .lh span{color:#71717A;font-weight:500}'
 '.ln3 .lb{padding:7px 6px;display:flex;flex-direction:column;gap:6px}.ln3.act .lh{background:#F4F4F5}'
 '.bk{border:1px solid #D4D4D8;border-radius:7px;padding:6px 7px;background:#fff;display:flex;flex-direction:column;gap:3px;box-shadow:0 1px 2px rgba(0,0,0,.04)}.bk b{font-family:"JetBrains Mono",ui-monospace,monospace;font-size:10px}.bk small{color:#71717A;font-size:8.6px}'
 '.bk.cur{border-color:#18181B}.bk.ghost{border-style:dashed;background:#FAFAFA;box-shadow:none}'
 '.us{display:flex;flex-direction:column;gap:2px;margin-top:3px}.us div{display:flex;align-items:center;gap:5px;font-family:"JetBrains Mono",ui-monospace,monospace;font-size:8.6px;height:14px}.us i{width:6px;height:6px;border-radius:50%;background:#D4D4D8;flex:none}.us i.p{background:#16A34A}.us i.f{background:#DC2626}'
 '.rwk{display:flex;align-items:center;gap:10px;padding:8px 11px;min-height:40px}.rwk .bk{flex-direction:row;align-items:center;gap:8px}'
 '.lg3{flex:1 1 0;min-height:0}.lg3 .row{grid-template-columns:40px 1fr;min-height:22px;font-size:9.4px}.lg3 .row.new{animation:exflash 1.4s ease}'
 '.sd{display:flex;flex-direction:column;min-height:0}.sd .cd{flex:1 1 0;display:flex;flex-direction:column;min-height:0}'
 '.kl .row{grid-template-columns:1fr 38px 16px;min-height:22px;font-size:9.4px}.ok3{width:13px;height:13px;border-radius:50%;display:grid;place-items:center;background:#F4F4F5;color:#A1A1AA}.ok3.on{background:#DCFCE7;color:#166534}.ok3 svg{width:8px;height:8px}'
 '.frm .g{display:grid;grid-template-columns:1fr 1fr;gap:7px;padding:9px 11px}.frm .g .w{grid-column:1/-1}.frm .ft{display:flex;justify-content:flex-end;padding:4px 11px 10px}.frm .nt{padding:0 11px 6px;color:#71717A;font-size:8.9px;line-height:1.4}'
 '.seg{display:inline-flex;border:1px solid #E4E4E7;border-radius:6px;padding:2px;gap:2px}.seg button{font-size:9.4px;padding:3px 9px;border:0;border-radius:4px;background:transparent;color:#52525B;cursor:pointer}.seg button.on{background:#18181B;color:#fff}'
 '.tmr{font-family:"JetBrains Mono",ui-monospace,monospace;font-size:20px;font-weight:600;letter-spacing:-.02em}'
 '.pad{padding:10px 11px;display:flex;flex-direction:column;gap:9px}.kv3{display:grid;grid-template-columns:1fr 1fr;gap:8px}'
 '.dd .row{grid-template-columns:1fr 50px;min-height:21px;font-size:9.4px}.pos{color:#166534;font-weight:600}'
)

WIN = (
 '<div class="hd"><svg width="16" height="16" viewBox="0 0 16 16" fill="none" aria-hidden="true"><rect x="1.5" y="3" width="3.5" height="10" rx="1" stroke="#18181B" stroke-width="1.2"/><rect x="6.25" y="3" width="3.5" height="10" rx="1" stroke="#18181B" stroke-width="1.2"/><rect x="11" y="3" width="3.5" height="10" rx="1" stroke="#18181B" stroke-width="1.2"/></svg>'
 '<span class="tt"><span class="mono">MO-3105</span> PCS-200 motor controller</span><span class="ch c-info" id="hst">Kitting</span><span class="sb grow">120 units, batch B-01 of 10</span></div>'
 '<div class="b3"><div class="bc">'
 '<div class="cd"><div class="lanes" id="lanes"></div></div>'
 '<div class="cd"><div class="ct">Rework<span class="mut" style="font-weight:500" id="rwn">No units</span></div><div class="rwk" id="rwk"></div></div>'
 '<div class="cd lg3"><div class="ct">Batch log<span class="mut" style="font-weight:500">B-01, L. Chen</span></div><div id="lg"></div></div>'
 '</div><div class="sd" id="sd"></div></div>'
)

JS = r'''
var FOC='.hd>*,.ln3,.rwk,.lg3,.sd .ct,.sd .kl,.sd .fld,.sd .kv,.sd .kv3,.sd .nt,.sd .bt,.sd .seg,.sd .dd,.sd .pad>p';
var KIT=[['PCB-210',1],['MCU-STM32',1],['CAP-1006',18],['RES-0402',64],['IC-PWR',2],['CON-J12',3]],BATCH=10;
var UNITS=[];for(var u=4208;u<=4217;u++)UNITS.push('SN-00'+u);
var LANES=['Kit','SMT','Through hole','Test','Pack'];
var okSvg='<svg viewBox="0 0 10 10" fill="none"><path d="M2.2 5.2l1.9 1.9 3.8-4" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>';
var S,tick=null;
function res(sn){return S.res[sn]||'';}
function good(){return UNITS.filter(function(s){return res(s)==='p';}).length;}
function renderBoard(){var lanes='';LANES.forEach(function(L,i){var here=S.stage===i,cards='';
if(here){var st=S.stage===0?(S.kitted?'Kitted, 6 of 6':'Kit 5 of 6 lines'):S.stage===1?'SMT line 1':S.stage===3?(S.closed?'':'Testing '+UNITS.filter(function(x){return res(x);}).length+' of 10'):S.stage===4?'To stock':'';
var n=S.stage===4?good()+' units':(S.stage===3&&res('SN-004213')==='f'?'9 units':'10 units');
var us='';if(S.stage===3){us='<div class="us">'+UNITS.filter(function(x){return res(x)!=='f';}).map(function(x){var r=res(x);return '<div><i class="'+r+'"></i>'+x.slice(3)+'</div>';}).join('')+'</div>';}
cards+='<div class="bk cur'+(S.anim?' in':'')+'"><b>B-01</b><small>'+n+'</small>'+(st?'<span class="ch '+(S.stage===4?'c-ok':S.kitted||S.stage>0?'c-info':'c-warn')+'">'+st+'</span>':'')+us+'</div>';}
if(i===0)cards+='<div class="bk ghost"><b>B-02</b><small>10 units, kit next</small></div>';
if(i===4&&!here)cards+='<div class="bk ghost"><b>MO-3098</b><small>Packed 10/02</small></div>';
lanes+='<div class="ln3'+(here?' act':'')+'"><div class="lh">'+L+'<span>'+((here?1:0)+(i===0?1:0)+(i===4&&!here?1:0))+'</span></div><div class="lb">'+cards+'</div></div>';});
$('lanes').innerHTML=lanes;
var f=res('SN-004213')==='f';$('rwn').textContent=f?'1 unit':'No units';
$('rwk').innerHTML=f?'<div class="bk'+(S.anim?' in':'')+'"><b>SN-004213</b><small>No boot, from test</small><span class="ch c-bad">Rework</span></div><span class="mut">Serial and reason travel with the unit</span>':'<span class="mut">Failed units land here with their serial and reason.</span>';
var hs2=$('hst');hs2.textContent=S.closed?'Batch closed':['Kitting','In SMT','','In test','Packed'][S.stage];hs2.className='ch '+(S.closed?'c-ok':'c-info');
$('lg').innerHTML=S.log.slice().reverse().map(function(l,i){return '<div class="row'+(i===0&&S.anim&&S.log.length>1?' new':'')+'"><span class="mut mono">'+l[0]+'</span><span>'+l[1]+'</span></div>';}).join('');}
function kitList(){return '<div class="kl">'+KIT.map(function(k,i){var ok=k[0]!=='CAP-1006'||S.kitted;return '<div class="row"><span><span class="mono">'+k[0]+'</span>'+(k[0]==='CAP-1006'&&S.kitted?' <span class="mut">lot 2631, R-0457</span>':'')+'</span><span class="mono r">'+n0(k[1]*BATCH)+'</span><span class="ok3'+(ok?' on':'')+'">'+(ok?okSvg:'')+'</span></div>';}).join('')+'</div>';}
function fld(id,label,val,err,extra){return '<label class="fld'+(extra||'')+'" id="f'+id+'"><small>'+label+'</small><input id="'+id+'" value="'+val+'" autocomplete="off" spellcheck="false"><span class="em">'+err+'</span></label>';}
function renderSide(){var d='',sd=$('sd');
if(S.stage===0){var n=S.kitted?6:5;d='<div class="cd frm'+(S.anim?' in':'')+'"><div class="ct">Kit B-01<span class="ch '+(S.kitted?'c-ok':'c-warn')+'">'+n+' of 6 lines</span></div>'+kitList()+
(S.kitted?'<div class="pad"><p class="mut" style="margin:0;font-size:9.4px;line-height:1.45">Lot 2631 and reel R-0457 are tied to MO-3105. Every unit in B-01 will carry them.</p></div><div class="ft"><button type="button" class="bt pri" id="rel">Release batch to SMT</button></div>':
'<div class="g">'+fld('kp','Part','CAP-1006','Scan a part on the kit')+fld('kl','Lot','2631','Lot is required')+fld('kr','Reel','R-0457','Reel is required','')+'</div><div class="ft"><button type="button" class="bt pri" id="scn">Scan reel</button></div>')+'</div>';}
else if(S.stage===1){var sec=Math.floor((Date.now()-S.t0)/1000);d='<div class="cd'+(S.anim?' in':'')+'"><div class="ct">SMT line 1<span class="ch c-info">Running</span></div><div class="pad"><div class="kv3"><div class="kv"><small>Operator</small><b>L. Chen</b></div><div class="kv"><small>Started</small><b>9:42 AM</b></div></div><div class="kv"><small>Labor on B-01</small><span class="tmr" id="tmr">0:'+('0'+Math.min(sec,59)).slice(-2)+'</span></div><p class="mut" style="margin:0;font-size:9.4px;line-height:1.45">Through hole picks the batch up next, then test.</p></div><div class="ft" style="display:flex;justify-content:flex-end;padding:4px 11px 10px;margin-top:auto"><button type="button" class="bt pri" id="mvt">Move to test</button></div></div>';}
else if(S.stage===3&&!S.done2){var sn=S.done1?'SN-004213':'SN-004212',fail=S.done1;
d='<div class="cd frm'+(S.anim?' in':'')+'"><div class="ct">Test <span class="mono">'+sn+'</span><span class="ch c-idle">'+(10-UNITS.filter(function(x){return res(x);}).length)+' left</span></div>'+
'<div class="nt" style="padding-top:8px">Fixture results imported for 8 units, all passed.</div><div class="g">'+fld('sv','Supply, V',fail?'5.01':'5.02','Enter a reading inside 4.90 to 5.10')+'<div class="kv"><small>Limit</small><b class="mono" style="padding:5px 0">4.90 to 5.10</b></div>'+
'<div class="kv w"><small>Boot check</small><span class="seg" id="boot"><button type="button" data-v="p" class="'+(S.boot==='p'?'on':'')+'">Pass</button><button type="button" data-v="f" class="'+(S.boot==='f'?'on':'')+'">Fail</button></span></div>'+
(fail?fld('rr','Reason','No boot','Add the failure reason',' w'):'')+'</div><div class="ft"><button type="button" class="bt pri" id="'+(fail?'rt2':'rt1')+'">Record test</button></div></div>';}
else if(S.stage===3&&S.done2){d='<div class="cd'+(S.anim?' in':'')+'"><div class="ct">B-01 test results<span class="ch c-ok">10 of 10</span></div><div class="pad"><div class="kv3"><div class="kv"><small>Passed</small><b class="mono">9</b></div><div class="kv"><small>In rework</small><b class="mono">1</b></div></div><p class="mut" style="margin:0;font-size:9.4px;line-height:1.45">Every result is saved on its serial number. SN-004213 waits in rework with its reason.</p></div><div class="ft" style="display:flex;justify-content:flex-end;padding:4px 11px 10px;margin-top:auto"><button type="button" class="bt pri" id="clb">Close batch</button></div></div>';}
else{d='<div class="cd'+(S.anim?' in':'')+'"><div class="ct">B-01 closed<span class="ch c-ok">Posted</span></div><div class="pad"><div class="kv3"><div class="kv"><small>Finished goods</small><b class="mono pos" id="fg">+'+good()+'</b></div><div class="kv"><small>Rework</small><b class="mono">1</b></div></div></div>'+
'<div class="dd"><div class="row h"><span>Components deducted</span><span class="r">Qty</span></div>'+KIT.map(function(k){return '<div class="row"><span class="mono">'+k[0]+'</span><span class="mono r">'+n0(k[1]*BATCH)+'</span></div>';}).join('')+'</div></div>';}
sd.innerHTML=d;}
function render(){renderBoard();renderSide();S.anim=false;}
$('sd').addEventListener('click',function(e){var b=e.target.closest&&e.target.closest('#boot button');if(!b)return;S.boot=b.getAttribute('data-v');[].forEach.call($('boot').children,function(x){x.classList.toggle('on',x===b);});});
function runTimer(){if(S.stage!==1)return;var t=$('tmr');if(t){var sec=Math.floor((Date.now()-S.t0)/1000);t.textContent='0:'+('0'+Math.min(sec,59)).slice(-2);}later(runTimer,1000);}
function resetState(){S={stage:0,kitted:false,done1:false,done2:false,closed:false,res:{},boot:'p',t0:0,anim:false,log:[['8:50','MO-3105 released, 120 units in 12 batches of 10'],['9:05','Routing set: kit, SMT, through hole, test, pack'],['9:18','MCU-STM32 lot L-88213, reel R-0311 picked to kit'],['9:30','Kit started for B-01, 5 of 6 lines picked']]};render();}
function val(id){var e=$(id);return e?String(e.value).trim():'';}
function bad(id,cond){var f=$('f'+id);if(f)f.classList.toggle('err',cond);return cond;}
function vSupply(){var v=parseFloat(val('sv'));return bad('sv',!(v>=4.9&&v<=5.1&&/^\d+(\.\d+)?$/.test(val('sv'))));}
var CAPAT=function(hh){return{l:14,t:visH()-hh-14};};
var ST=[
{id:'scan',target:function(){return $('scn');},prompt:'Click Scan reel',where:'below',ok:function(){var a=bad('kp',val('kp').toUpperCase()!=='CAP-1006'),b=bad('kl',!val('kl')),c=bad('kr',!val('kr'));return !(a||b||c);},
 run:function(){S.kitted=true;S.anim=true;S.log.push(['9:41','CAP-1006 lot 2631, reel R-0457 scanned to MO-3105']);render();},after:['Scan to kit, and the reel is tied to the build','Kit is 6 of 6 lines. Lot 2631 and reel R-0457 belong to MO-3105 from the first move.']},
{id:'release',target:function(){return $('rel');},prompt:'Click Release batch to SMT',where:'below',run:function(q){S.stage=1;S.t0=Date.now();S.anim=true;S.log.push(['9:42','B-01 released to SMT line 1, labor started']);render();if(!q)later(runTimer,1000);},after:['Each station sees its own queue','B-01 is on SMT line 1, and labor for L. Chen is recorded as work starts.']},
{id:'move',target:function(){return $('mvt');},prompt:'Click Move to test',where:'below',run:function(){S.stage=3;S.boot='p';UNITS.forEach(function(x){if(x!=='SN-004212'&&x!=='SN-004213')S.res[x]='p';});S.anim=true;S.log.push(['10:58','Through hole done, B-01 at test, 8 fixture results imported']);render();},after:['Builds move station by station','B-01 went through through hole to test. You always see where a batch sits.']},
{id:'test1',target:function(){return $('rt1');},prompt:'Click Record test',where:'below',ok:function(){var a=vSupply();if(S.boot!=='p'){a=true;bad('sv',true);}return !a;},
 run:function(){S.res['SN-004212']='p';S.done1=true;S.boot='f';S.anim=true;S.log.push(['11:03','SN-004212 passed, supply 5.02 V, boot check pass']);render();},after:['Test results are saved on the serial','SN-004212 passed at 5.02 V. Every unit has its own record.']},
{id:'test2',target:function(){return $('rt2');},prompt:'Click Record test',where:'below',ok:function(){var a=bad('rr',!val('rr'));if(S.boot!=='f'){a=true;bad('rr',true);}return !a;},
 run:function(){S.res['SN-004213']='f';S.done2=true;S.anim=true;S.log.push(['11:05','SN-004213 failed, '+(val('rr')||'No boot')+', sent to rework']);render();},after:['A failed unit goes to rework with its reason','SN-004213 moved to rework with its serial and reason, so nothing slips through.']},
{id:'close',target:function(){return $('clb');},prompt:'Click Close batch',where:'below',run:function(){S.stage=4;S.closed=true;S.anim=true;S.log.push(['11:10','B-01 closed, 9 to finished goods, components deducted']);render();},after:['Good units in stock, components deducted','Finished goods +9, 1 in rework. MCU-STM32 10 and CAP-1006 180 came out of stock.']}];
'''
