"""Electronics card 4: Serial Genealogy & RMA. Layout: a node graph (unit, board, sub assemblies on the left; lots, reels and the test record on the right), whose right side swaps for a customer list, an RMA card and a rework traveler, with a record panel below."""
SUMMARY = 'Serial Genealogy & RMA (trace a serial to its lots and reels, trace a lot forward to customers, open an RMA, rework, retest, close and ship)'
ARIA = 'Interactive product screen: trace serial SN-004187 to its board, components, lots and reels, open the capacitor lot and trace it forward to customers, then open an RMA, run rework, record the retest and close the RMA'
STEPS = 7
STUDIO = dict(lede='A typical serial trace and returns screen, built on your Sutton data with Studio. Want it different? Describe the change.',
              examples=['A warranty check by serial', 'Failure reason tags', 'A customer notice list', 'A repair history view'],
              built_on='Serials, lots, shipments and work orders', change='Fields, reasons and views')

CSS = (
 '.b4{display:flex;flex-direction:column;gap:10px;padding:12px 40px 0 16px;height:596px}'
 '.srch{display:flex;align-items:flex-end;gap:10px;padding:9px 11px}.srch .fld{width:150px}.srch .ship{margin-left:auto;text-align:right}'
 '.gr{position:relative;height:262px}.gr svg{position:absolute;inset:0;pointer-events:none}.gr path{fill:none;stroke:#D4D4D8;stroke-width:1.4;transition:opacity .4s ease}.gr path.hot{stroke:#18181B}'
 '.nd{position:absolute;border:1px solid #E4E4E7;border-radius:8px;background:#fff;padding:6px 9px;display:flex;flex-direction:column;gap:2px;opacity:0;transform:translateY(5px);transition:opacity .4s ease,transform .45s cubic-bezier(.22,.9,.28,1),border-color .25s,box-shadow .25s}'
 '.nd small{color:#71717A;font-size:8.6px}.nd b{font-family:"JetBrains Mono",ui-monospace,monospace;font-size:10px;font-weight:600}.nd span{font-size:9.2px;color:#3F3F46}'
 '.gr.on .nd{opacity:1;transform:none}.nd.u{border-color:#18181B;box-shadow:0 2px 6px rgba(0,0,0,.08)}button.nd{text-align:left;cursor:pointer;font:inherit}button.nd:hover{background:#FAFAFA}button.nd.sel{border-color:#18181B;box-shadow:inset 3px 0 0 #18181B}button.nd:focus-visible{outline:2px solid #18181B;outline-offset:2px}'
 '.rp4{position:absolute;left:366px;top:10px;width:286px;bottom:10px}.rp4 .cd{height:100%;display:flex;flex-direction:column}'
 '.cl .row{grid-template-columns:1fr 46px;min-height:30px}.cl .row.me{background:#FFFBEB}.cl .row.t{background:#FAFAFA;font-weight:600}'
 '.rm .pad,.pad{padding:9px 11px;display:flex;flex-direction:column;gap:8px}.g2{display:grid;grid-template-columns:1fr 1fr;gap:8px}'
 '.op .row{grid-template-columns:18px 1fr auto;min-height:28px}.op .n{width:16px;height:16px;border-radius:50%;display:grid;place-items:center;background:#F4F4F5;font-size:9px;font-weight:600}.op .n.ok{background:#DCFCE7;color:#166534}'
 '.cs .row{grid-template-columns:1fr auto;min-height:22px}.cs .row.t{font-weight:600;background:#FAFAFA}'
 '.bp{flex:1 1 0;min-height:0}.bp .frm2{display:flex;align-items:flex-end;gap:10px;padding:9px 11px}.bp .frm2 .fld{width:160px}.bp .frm2 .fld.sm{width:80px}'
 '.hi4 .row{grid-template-columns:40px 1fr auto;min-height:22px;font-size:9.4px}.hi4 .row.new{animation:exflash 1.4s ease}'
 '.seg{display:inline-flex;border:1px solid #E4E4E7;border-radius:6px;padding:2px;gap:2px}.seg button{font-size:9.4px;padding:3px 9px;border:0;border-radius:4px;background:transparent;color:#52525B;cursor:pointer}.seg button.on{background:#18181B;color:#fff}'
 '.bsum{display:grid;grid-template-columns:repeat(4,1fr);gap:8px;padding:9px 11px}'
)

WIN = (
 '<div class="hd"><svg width="16" height="16" viewBox="0 0 16 16" fill="none" aria-hidden="true"><circle cx="3.5" cy="8" r="2" stroke="#18181B" stroke-width="1.3"/><circle cx="12.5" cy="3.5" r="2" stroke="#18181B" stroke-width="1.3"/><circle cx="12.5" cy="12.5" r="2" stroke="#18181B" stroke-width="1.3"/><path d="M5.4 7.2l5.2-2.8M5.4 8.8l5.2 2.8" stroke="#18181B" stroke-width="1.2"/></svg>'
 '<span class="tt">Serial trace</span><span class="ch c-idle" id="hst">No serial</span><span class="sb grow">PCS-200 motor controller</span></div>'
 '<div class="b4">'
 '<div class="cd frm"><div class="srch"><label class="fld" id="fsn"><small>Serial number</small><input id="isn" value="SN-004187" spellcheck="false" autocomplete="off"><span class="em">No unit found. Try SN-004187</span></label>'
 '<button type="button" class="bt pri" id="trs">Trace serial</button></div></div>'
 '<div class="cd"><div class="ct">Genealogy<span class="mut" style="font-weight:500" id="gsub">Unit, board, sub assemblies, lots and reels</span></div><div class="gr" id="gr"><svg id="wr" viewBox="0 0 660 262" preserveAspectRatio="none"></svg><div id="nds"></div><div class="rp4" id="rp4"></div></div></div>'
 '<div class="cd bp" id="bp"></div>'
 '</div>'
)

JS = r'''
var FOC='.hd>*,.srch>*,.ct,.nd,.rp4 .cd,.bp .ct,.bp .frm2>*,.bp .pad>*,.bp .bsum,.bp .hi4,.bp .row';
var LEFT=[{k:'u',x:10,y:100,w:140,s:'Unit',b:'SN-004187',t:'Rev C, PCS-200'},{k:'b',x:180,y:14,w:160,s:'Board',b:'SN-B-1127',t:'PCBA-210 rev C, MO-3098'},{k:'h',x:180,y:104,w:160,s:'Cable harness',b:'H-0914',t:'HAR-220 rev A lot'},{k:'e',x:180,y:186,w:160,s:'Enclosure kit',b:'E-3321',t:'ENC-230 rev A lot'}];
var RIGHT=[{k:'m',y:10,s:'MCU-STM32',b:'L-88213',t:'Reel R-0311'},{k:'c',y:72,s:'CAP-1006 capacitor',b:'Lot 2631',t:'Reel R-0457, date code 2631'},{k:'p',y:134,s:'IC-PWR regulator',b:'P-5502',t:'Lot, 2 a board'},{k:'t',y:196,s:'Functional test',b:'Passed 09/30',t:'Supply 5.03 V, boot pass'}];
var CUST=[['Halden Robotics',6],['Marlow Instruments',5],['Tern Audio',3]];
var RATE=42,PART=0.12;
var S;
function wires(){var p='';LEFT.slice(1).forEach(function(n){p+='<path d="M150 '+(100+25)+' C165 125 165 '+(n.y+25)+' 180 '+(n.y+25)+'"/>';});
if(S.right==='nodes')RIGHT.forEach(function(n){p+='<path class="'+(S.lot&&n.k==='c'?'hot':'')+'" d="M340 39 C352 39 352 '+(n.y+35)+' 366 '+(n.y+35)+'"/>';});else p+='<path class="hot" d="M340 39 C352 39 352 140 366 140"/>';$('wr').innerHTML=S.traced?p:'';}
function node(n,x,cls,tag){return '<'+tag+(tag==='button'?' type="button"':'')+' class="nd '+(cls||'')+'" id="n'+n.k+'" style="left:'+x+'px;top:'+n.y+'px;width:'+(n.w||286)+'px"><small>'+n.s+'</small><b>'+n.b+'</b><span>'+n.t+'</span></'+tag+'>';}
function render(){var gr=$('gr');gr.classList.toggle('on',S.traced);
var uSt={none:'',shipped:'Shipped 10/09',rma:'Returned, RMA-0071',rework:'In rework',fixed:'Retest passed',closed:'Shipped back 11/06'}[S.unit];
var hs2=$('hst');hs2.textContent=S.traced?uSt:'No serial';hs2.className='ch '+(!S.traced?'c-idle':S.unit==='closed'||S.unit==='fixed'?'c-ok':S.unit==='shipped'?'c-idle':'c-warn');

var h='';LEFT.forEach(function(n){var t=n.t;if(n.k==='u')t=uSt||t;h+=node({k:n.k,y:n.y,w:n.w,s:n.s,b:n.b,t:t},n.x,n.k==='u'?'u':'','div');});
if(!S.traced)h='';$('nds').innerHTML=h;
var r='';if(S.traced){if(S.right==='nodes'){RIGHT.forEach(function(n){var t=n.t;if(n.k==='c'&&S.unit==='closed')t='C14 replaced with lot 2640 on 11/05';r+=node({k:n.k,y:n.y,s:n.s,b:n.b,t:t},0,(n.k==='c'&&S.lot?'sel':''),n.k==='c'?'button':'div').replace('left:0px;','left:0;');});r='<div style="position:relative;height:100%">'+r+'</div>';}
else if(S.right==='cust'){var tot=0,rows='';CUST.forEach(function(c){tot+=c[1];rows+='<div class="row'+(c[0]==='Halden Robotics'?' me':'')+'"><span>'+c[0]+(c[0]==='Halden Robotics'?' <span class="mut">incl. SN-004187</span>':'')+'</span><span class="mono r">'+c[1]+'</span></div>';});
r='<div class="cd cl in"><div class="ct">Lot 2631, traced forward<span class="ch c-info">'+tot+' units</span></div><div class="row h"><span>Customer</span><span class="r">Units</span></div>'+rows+'<div class="row t"><span>'+CUST.length+' customers</span><span class="mono r" id="ctot">'+tot+'</span></div><div class="pad"><span class="mut" style="font-size:9.2px;line-height:1.4">Every unit built with reel R-0457, found from the lot record.</span></div></div>';}
else if(S.right==='rma'){r='<div class="cd rm in"><div class="ct"><span class="mono">RMA-0071</span><span class="ch '+(S.unit==='closed'?'c-ok':'c-warn')+'">'+(S.unit==='closed'?'Closed':'Received')+'</span></div><div class="pad"><div class="g2"><div class="kv"><small>Serial</small><b class="mono">SN-004187</b></div><div class="kv"><small>Customer</small><b>Halden Robotics</b></div><div class="kv"><small>Shipped</small><b>10/09/2026</b></div><div class="kv"><small>Warranty</small><b>12 months</b></div><div class="kv"><small>Valid to</small><b>10/09/2027</b></div><div class="kv"><small>Reason</small><b>'+S.reason.replace(/</g,'&lt;')+'</b></div></div><span class="ch c-ok" style="align-self:flex-start">Warranty valid</span></div></div>';}
else{var done=S.unit==='fixed'||S.unit==='closed',lab=S.hrs*RATE,tot2=lab+PART;
r='<div class="cd op in"><div class="ct"><span>Rework <span class="mono">RW-0215</span></span><span class="ch '+(done?'c-ok':'c-info')+'">'+(done?'Complete':'Open')+'</span></div>'+
'<div class="row"><span class="n'+(done?' ok':'')+'">1</span><span>Replace C14 with CAP-1006 lot 2640</span><span class="mono mut">'+m2(PART)+'</span></div><div class="row"><span class="n'+(done?' ok':'')+'">2</span><span>Retest supply and boot</span><span class="mono mut">'+(done?S.sv+' V':'Waiting')+'</span></div>'+
(done?'<div class="cs"><div class="row"><span>Labor, '+S.hrs+' h at '+m2(RATE)+'</span><span class="mono">'+m2(lab)+'</span></div><div class="row"><span>Part, CAP-1006 lot 2640</span><span class="mono">'+m2(PART)+'</span></div><div class="row t"><span>Added to RMA-0071</span><span class="mono" id="rtot">'+m2(tot2)+'</span></div></div>':'<div class="pad"><span class="mut" style="font-size:9.2px;line-height:1.4">The unit keeps serial SN-004187 and its history through rework.</span></div>')+'</div>';}}
$('rp4').innerHTML=r;wires();
var b='';
if(!S.traced)b='<div class="ct">Record</div><div class="pad"><div class="empt" style="padding:12px"><b>Trace a serial</b><span>See the board, components, lots and reels behind a unit, and its test record.</span></div></div><div class="hi4"><div class="row h"><span>Date</span><span>Recent traces</span><span></span></div><div class="row"><span class="mut mono">11/04</span><span><span class="mono">SN-004150</span>, field check for Marlow Instruments</span><span></span></div><div class="row"><span class="mut mono">10/28</span><span>Lot <span class="mono">L-88213</span>, supplier notice reviewed</span><span></span></div><div class="row"><span class="mut mono">10/21</span><span><span class="mono">SN-003982</span>, warranty check</span><span></span></div></div>';
else if(S.step===1)b='<div class="ct">Unit SN-004187<span class="ch c-ok">Test passed 09/30</span></div><div class="bsum"><div class="kv"><small>Built</small><b>09/30 on MO-3098</b></div><div class="kv"><small>Revision</small><b>Rev C</b></div><div class="kv"><small>Shipped</small><b>10/09, SO-7731</b></div><div class="kv"><small>Customer</small><b>Halden Robotics</b></div></div><div class="pad"><span class="mut" style="font-size:9.4px">Open any node to see its record.</span></div>';
else if(S.step===2)b='<div class="ct">CAP-1006 lot 2631<span class="ch c-info">Used in 14 units</span></div><div class="bsum"><div class="kv"><small>Reel</small><b class="mono">R-0457</b></div><div class="kv"><small>Date code</small><b class="mono">2631</b></div><div class="kv"><small>Received</small><b class="mono">PO-1012</b></div><div class="kv"><small>Used in</small><b>14 units</b></div></div><div class="frm2"><button type="button" class="bt pri" id="tfw">Trace forward</button><span class="mut">Find every unit and customer that got this lot</span></div>';
else if(S.step===3)b='<div class="ct">Return for SN-004187<span class="mut" style="font-weight:500">Halden Robotics</span></div><div class="frm2 frm"><label class="fld" id="frs"><small>Reason</small><input id="irs" value="'+S.reason.replace(/"/g,'&quot;')+'" autocomplete="off"><span class="em">Add a return reason</span></label><button type="button" class="bt pri" id="orm">Open RMA</button></div>';
else if(S.step===4)b='<div class="ct">RMA-0071<span class="mut" style="font-weight:500">Warranty checked from the serial</span></div><div class="frm2"><button type="button" class="bt pri" id="crw">Create rework order</button><span class="mut">Runs as its own order, the unit keeps its serial</span></div>';
else if(S.step===5)b='<div class="ct">Retest SN-004187<span class="mut" style="font-weight:500">Limit 4.90 to 5.10 V</span></div><div class="frm2 frm"><label class="fld sm" id="fsv"><small>Supply, V</small><input id="isv" value="5.01" autocomplete="off"><span class="em">4.90 to 5.10</span></label><div class="kv"><small>Result</small><span class="seg" id="rres"><button type="button" class="on">Pass</button></span></div><label class="fld sm" id="fhr"><small>Labor, h</small><input id="ihr" value="0.5" autocomplete="off"><span class="em">0.1 to 8</span></label><button type="button" class="bt pri" id="rrt">Record retest</button></div>';
else if(S.step===7)b='<div class="ct">RMA-0071 closed<span class="ch c-ok">Shipped back 11/06</span></div>';
else if(S.step===6)b='<div class="ct">RMA-0071 ready to ship<span class="ch c-ok">Retest passed</span></div><div class="frm2"><button type="button" class="bt pri" id="cls">Close RMA and ship</button><span class="mut">'+m2(S.hrs*RATE+PART)+' recorded against the unit</span></div>';
if(S.step>=6||S.unit==='closed'){var H=[['09/30','Built on MO-3098, functional test passed'],['10/09','Shipped to Halden Robotics, SO-7731'],['11/03','Returned on RMA-0071, '+S.reason],['11/05','Rework RW-0215, C14 lot 2640, retest '+S.sv+' V pass']];if(S.unit==='closed')H.push(['11/06','RMA-0071 closed, shipped back to Halden Robotics']);
b+='<div class="hi4"><div class="row h"><span>Date</span><span>Unit history, SN-004187</span><span></span></div>'+H.map(function(x,i){return '<div class="row'+(i===H.length-1&&S.anim?' new':'')+'"><span class="mut mono">'+x[0]+'</span><span>'+x[1]+'</span><span></span></div>';}).join('')+'</div>';}
$('bp').innerHTML=b;S.anim=false;}
function resetState(){S={traced:false,lot:false,right:'nodes',unit:'none',step:0,reason:'Intermittent reset',hrs:0.5,sv:'5.01',anim:false};$('isn').value='SN-004187';$('fsn').classList.remove('err');render();}
function val(id){var e=$(id);return e?String(e.value).trim():'';}
function bad(id,c){var f=$(id);if(f)f.classList.toggle('err',c);return c;}
var CAPAT=function(hh){return{l:300,t:58};};
var ST=[
{id:'trace',target:function(){return $('trs');},prompt:'Click Trace serial',where:'below',ok:function(){return !bad('fsn',val('isn').toUpperCase()!=='SN-004187');},run:function(){S.traced=true;S.unit='shipped';S.step=1;S.anim=true;render();},after:['Any serial, and exactly what went into it','Board SN-B-1127, its lots and reels, and the test record from 09/30.']},
{id:'lot',target:function(){return $('nc');},prompt:'Click the CAP-1006 lot 2631 node',where:'below',run:function(){S.lot=true;S.step=2;S.anim=true;render();},after:['Down to the reel and the date code','Reel R-0457, date code 2631, received on PO-1012, used in 14 units.']},
{id:'forward',target:function(){return $('tfw');},prompt:'Click Trace forward',where:'below',run:function(){S.right='cust';S.step=3;S.anim=true;render();},after:['Going the other way, every customer','14 units of lot 2631 went to 3 customers: Halden Robotics 6, Marlow Instruments 5, Tern Audio 3.']},
{id:'rma',target:function(){return $('orm');},prompt:'Click Open RMA',where:'below',ok:function(){var r=val('irs');if(r)S.reason=r;return !bad('frs',!r);},run:function(){var r=val('irs');if(r)S.reason=r;S.right='rma';S.unit='rma';S.step=4;S.anim=true;render();},after:['The return starts from the serial','RMA-0071 is received. Shipped 10/09, so the warranty runs to 10/09/2027.']},
{id:'rework',target:function(){return $('crw');},prompt:'Click Create rework order',where:'below',run:function(){S.right='rw';S.unit='rework';S.step=5;S.anim=true;render();},after:['Rework runs as its own order','Replace C14 with lot 2640, then retest. The unit keeps its serial and history.']},
{id:'retest',target:function(){return $('rrt');},prompt:'Click Record retest',where:'below',ok:function(){var v=parseFloat(val('isv')),h=parseFloat(val('ihr')),a=bad('fsv',!(v>=4.9&&v<=5.1&&/^\d+(\.\d+)?$/.test(val('isv')))),b=bad('fhr',!(h>=0.1&&h<=8&&/^\d+(\.\d+)?$/.test(val('ihr'))));if(!a)S.sv=val('isv');if(!b)S.hrs=h;return !(a||b);},
 run:function(){S.unit='fixed';S.step=6;S.anim=true;render();},after:function(){return['The repair is on the unit record','Retest passed at '+S.sv+' V. Labor '+m2(S.hrs*RATE)+' plus the part '+m2(PART)+', '+m2(S.hrs*RATE+PART)+' on RMA-0071.'];}},
{id:'close',target:function(){return $('cls');},prompt:'Click Close RMA and ship',where:'below',run:function(){S.right='rma';S.unit='closed';S.step=7;S.anim=true;render();},after:['One record from first build to repair','RMA-0071 is closed and SN-004187 shipped back, with its history extended.']}];
'''
