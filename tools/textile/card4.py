"""Textile card 4: Fiber to Fabric Traceability. Layout: two direction genealogy graph (nodes and lines).
Backward on the left, from the finished roll to the dye lot, its chemical batches, the greige batch and the yarn lots with
their suppliers. Forward on the right, from the dye lot to three shipments and the stock still on hand. The selected node
is highlighted and its record shows in the card below the graph.
Type R-48211, open the warp yarn lot and its attached files, follow the dye lot forward, package the record.
Every figure comes from tools/textile/data.py, where the brief's sums are asserted."""
import json
import data as D
from frame_textile import header

SUMMARY = 'Fiber to Fabric Traceability (trace a roll back to its dye lot, greige batch, yarn lots and suppliers, open the supplier files, follow the lot forward to shipments and package the record)'
ARIA = 'Interactive demo: trace a fabric roll back to its yarn lots and forward to customer shipments.'
STEPS = 4
STUDIO = dict(lede='A typical lot genealogy screen, built on your Sutton data with Studio. Want it different? Describe the change.',
              examples=['Certification scope fields on yarn lots', 'A brand audit pack template', 'A flag on lots missing a supplier certificate', 'A recall notice screen'],
              built_on='Lot genealogy, forward and backward tracing, attachments', change='Levels, fields and documents')

ICON = '<circle cx="8" cy="8" r="2"/><circle cx="2.5" cy="4" r="1.5"/><circle cx="2.5" cy="12" r="1.5"/><circle cx="13.5" cy="4" r="1.5"/><circle cx="13.5" cy="12" r="1.5"/><path d="M3.8 4.8L6.3 7M3.8 11.2L6.3 9M12.2 4.8L9.7 7M12.2 11.2L9.7 9"/>'

ROLLS = dict((i, q) for i, q, _ in D.AVAIL + D.HELD)

CSS = (
 '.g4{padding:10px 0 0 16px;display:flex;flex-direction:column;gap:10px}.g4>*{width:656px;flex:none}'
 '.srch{height:44px;display:flex;align-items:center;gap:8px;padding:0 10px}.srch .fld{flex-direction:row;align-items:center;gap:8px;position:relative}'
 '.srch .fld input{width:178px;font-size:10.6px;padding:6px 8px}.srch .fld .em{position:absolute;left:0;top:30px;white-space:nowrap}'
 '.smp{display:inline-flex;align-items:center;gap:5px;font-size:9.4px;color:#71717A;margin-left:4px}.smp .bt{font-family:"JetBrains Mono",ui-monospace,monospace;font-size:9.6px;padding:4px 8px}'
 '.gph{height:286px}.gph .ct{justify-content:flex-start;gap:10px}.dir{display:flex;gap:4px;margin-left:auto}.dr{font-size:9.2px;font-weight:500;padding:3px 8px;border-radius:999px;border:1px solid #E4E4E7;color:#A1A1AA;background:#fff}'
 '.dr.on{background:#18181B;border-color:#18181B;color:#fff}.dr.fw.on{background:#1E3A8A;border-color:#1E3A8A}'
 '.cvs{position:relative;height:240px;margin:8px 10px}.cvs svg.ln{position:absolute;left:0;top:0;width:636px;height:240px;overflow:visible}.cvs svg.ln path{fill:none;stroke:#D4D4D8;stroke-width:1.3}'
 '.cvs svg.ln path.bk{stroke:#52525B}.cvs svg.ln path.fw{stroke:#3B5FB3}'
 '.cl{position:absolute;top:0;font-size:8.6px;font-weight:500;color:#71717A;white-space:nowrap}'
 '.nd{position:absolute;border:1px solid #E4E4E7;border-radius:7px;background:#fff;padding:5px 8px;display:flex;flex-direction:column;justify-content:center;gap:1px;font:inherit;font-size:8.9px;line-height:1.3;white-space:nowrap;text-align:left;color:#18181B;box-shadow:0 1px 2px rgba(0,0,0,.04)}'
 'button.nd{cursor:pointer;transition:background-color .2s,box-shadow .2s}button.nd:hover,button.nd.fakehover{background:#F4F4F5}button.nd:focus-visible{outline:2px solid #18181B;outline-offset:2px}'
 '.nd .id{font-family:"JetBrains Mono",ui-monospace,monospace;font-weight:600;font-size:9.6px;display:flex;align-items:center;justify-content:space-between;gap:6px}.nd .mut{font-size:8.5px}'
 '.nd.sel{border-color:#18181B;box-shadow:0 0 0 1px #18181B}.nd.start{background:#F4F4F5}.nd.ship{border-color:#C7D2FE;background:#F5F7FF}.nd.sm{padding:3px 8px}.nd .ch{font-size:7.8px;padding:1px 5px}'
 '.tot{position:absolute;right:0;bottom:0;font-size:8.8px;color:#1E3A8A;background:#EEF2FF;border:1px solid #C7D2FE;border-radius:6px;padding:3px 8px;white-space:nowrap}'
 '.rec{height:196px;display:flex;flex-direction:column}.rec .row{grid-template-columns:78px 92px 1fr 70px;font-size:9.3px;min-height:21px}.rec .row.tt{font-weight:600;border-top:1px solid #E4E4E7}'
 '.fl{display:grid;grid-template-columns:20px 1fr 54px 60px;align-items:center;gap:8px;padding:0 11px;min-height:26px;border-top:1px solid #F4F4F5;font-size:9.3px}.fl .fi{width:18px;height:20px;border-radius:3px;background:#FEE2E2;color:#B91C1C;font-size:6.4px;font-weight:700;display:grid;place-items:center}'
 '.kv3{display:grid;grid-template-columns:repeat(4,1fr);gap:6px 10px;padding:8px 11px}.kv3 .kv b{font-size:9.8px}'
 '.rac{margin-top:auto;padding:7px 11px 9px;border-top:1px solid #F0F0F1;display:flex;align-items:center;gap:8px;font-size:8.9px;color:#52525B;white-space:nowrap}'
 '.ap{display:flex;align-items:center;gap:8px}.ap .fi{width:18px;height:20px;border-radius:3px;background:#E0E7FF;color:#3730A3;font-size:6.4px;font-weight:700;display:grid;place-items:center}'
 '.gph .empt,.rec .empt{margin:10px;flex:1}.gph .empt{height:220px}'
)

WIN = (
 header(ICON, 'Lot genealogy', 'Traceability, fiber to fabric')
 + '<div class="g4"><div class="cd srch frm" id="srch"><label class="fld" id="flin"><input id="lin" value="" placeholder="Enter a roll or lot number" autocomplete="off" spellcheck="false" aria-label="Roll or lot number">'
 '<span class="em" id="lem">No record found. Try R-48211</span></label><button type="button" class="bt pri" id="trc">Trace</button>'
 '<span class="smp">Sample<button type="button" class="bt" data-sample data-v="R-48211">R-48211</button><button type="button" class="bt" data-sample data-v="DL-2611-B">DL-2611-B</button></span>'
 '<span class="grow"></span><span class="ch c-idle" id="sst">Nothing traced</span></div>'
 '<div class="cd gph" id="gph"></div><div class="cd rec" id="rec"></div></div>'
)

JS = r'''
var FOC='.hd>*,.srch>*,.gph .ct>*,.cl,.nd,.tot,.rec .ct,.rec .row,.fl,.kv3,.rac>*';
var LOT='@LOT@',SH='@SHADE@',LYD=@LYD@,LROLLS=@LROLLS@,GR='@GR@',GYD=@GYD@,STK=@STK@,STKR=@STKR@;
var YL=@YL@,SHIP=@SHIP@,ROLLS=@ROLLS@;
var X=[0,130,260,396,528],W=[118,112,122,120,106];
var S;
function sum(a){return a.reduce(function(x,y){return x+y;},0);}
function fwd(){return sum(SHIP.map(function(s){return s[2];}))+STK;}
function nd(id,cls,l,t,w,h,inner,btn,d){var tag=btn?'button type="button"':'div';return '<'+tag+' class="nd '+cls+(S.an?' in':'')+(S.sel===id?' sel':'')+'" id="n-'+id+'" style="left:'+l+'px;top:'+t+'px;width:'+w+'px;height:'+h+'px'+(S.an?';animation-delay:'+d+'ms':'')+'">'+inner+'</'+(btn?'button':'div')+'>';}
function cv(x1,y1,x2,y2,c){var m=(x1+x2)/2;return '<path class="'+(c||'')+'" d="M'+x1+' '+y1+'C'+m+' '+y1+' '+m+' '+y2+' '+x2+' '+y2+'"/>';}
function render(){
var g='<div class="ct"><span>Genealogy</span><span class="mut" style="font-weight:500">'+(S.q?S.q:'')+'</span><span class="dir"><span class="dr'+(S.q?' on':'')+'">Backward</span><span class="dr fw'+(S.fw?' on':'')+'">Forward</span></span></div>';
if(!S.q)g+='<div class="empt"><svg width="26" height="26" viewBox="0 0 16 16" fill="none" stroke="#A1A1AA" stroke-width="1.1" stroke-linecap="round">@ICON@</svg><b>No roll or lot traced</b><span>Enter a roll or lot number to see where it came from and where it went.</span></div>';
else{var p='',n='',roll=S.q!==LOT,dyc=128;
n+='<span class="cl" style="left:'+X[0]+'px">Yarn lots and suppliers</span><span class="cl" style="left:'+X[1]+'px">Greige and chemicals</span><span class="cl" style="left:'+X[2]+'px">Dye lot</span>';
n+=nd(YL[0][0],'',X[0],38,W[0],62,'<span class="id">'+YL[0][0]+'</span><span>'+YL[0][1]+', '+YL[0][2]+' kg</span><span class="mut">'+YL[0][3]+'</span>',true,0);
n+=nd(YL[1][0],'',X[0],128,W[0],62,'<span class="id">'+YL[1][0]+'</span><span>'+YL[1][1]+', '+YL[1][2]+' kg</span><span class="mut">'+YL[1][3]+'</span>',true,60);
n+=nd(GR,'',X[1],44,W[1],50,'<span class="id">'+GR+'</span><span class="mut">Greige, '+n0(GYD)+' yd</span>',false,120);
n+=nd('CH-0931','sm',X[1],128,W[1],38,'<span class="id">CH-0931</span><span class="mut">Dye batch</span>',false,160);
n+=nd('CH-0944','sm',X[1],176,W[1],38,'<span class="id">CH-0944</span><span class="mut">Auxiliary batch</span>',false,200);
n+=nd(LOT,(roll?'':'start'),X[2],dyc-34,W[2],68,'<span class="id">'+LOT+'</span><span>Shade '+SH+'</span><span class="mut">'+n0(LYD)+' yd, '+LROLLS+' rolls</span>',true,240);
p+=cv(X[0]+W[0],69,X[1],69,'bk')+cv(X[0]+W[0],159,X[1],69,'bk')+cv(X[1]+W[1],69,X[2],dyc,'bk')+cv(X[1]+W[1],147,X[2],dyc,'bk')+cv(X[1]+W[1],195,X[2],dyc,'bk');
if(S.fw){n+='<span class="cl" style="left:'+X[3]+'px">Shipments and stock</span>';
SHIP.forEach(function(s,i){var t=16+i*50;n+=nd(s[0],'ship',X[3],t,W[3],44,'<span class="id">'+s[0]+'<span class="ch c-info">Shipped</span></span><span class="mut">'+s[1]+'</span><span class="mut" id="fq'+i+'">'+n0(s[2])+' yd</span>',false,i*90);p+=cv(X[2]+W[2],dyc,X[3],t+22,'fw');});
n+=nd('STK','ship',X[3],166,W[3],44,'<span class="id">In stock<span class="ch c-ok">'+STKR+' rolls</span></span><span class="mut" id="fq3">'+n0(STK)+' yd</span>',false,270);p+=cv(X[2]+W[2],dyc,X[3],188,'fw');
n+='<span class="tot" id="ftot">Forward '+SHIP.map(function(s){return n0(s[2]);}).join(' + ')+' + '+n0(STK)+' = '+n0(fwd())+' yd</span>';}
if(roll){n+='<span class="cl" style="left:'+X[4]+'px">Finished roll</span>';n+=nd(S.q,'start',X[4],166,W[4],44,'<span class="id">'+S.q+'</span><span class="mut">'+ROLLS[S.q]+' yd, '+LOT+'</span>',false,0);
p+=S.fw?cv(X[3]+W[3],188,X[4],188,'fw'):cv(X[2]+W[2],dyc,X[4],188,'bk');}
g+='<div class="cvs"><svg class="ln" viewBox="0 0 636 240" aria-hidden="true">'+p+'</svg>'+n+'</div>';}
$('gph').innerHTML=g;
var r='<div class="ct"><span id="rtt">'+(S.pk?'Audit pack':S.sel===YL[0][0]?'Yarn lot '+YL[0][0]:S.fw?'Forward trace, '+LOT:S.q?'Backward trace, '+S.q:'Record')+'</span>'+(S.q?'<span class="ch '+(S.pk?'c-ok':'c-info')+'">'+(S.pk?'Ready':S.sel===YL[0][0]?'2 files':S.fw?'Balanced':'Complete')+'</span>':'')+'</div>';
if(!S.q)r+='<div class="empt"><b>Nothing traced yet</b><span>The record for the selected node shows here, with its files.</span></div><div class="rac"><span class="mut">Trace a roll, dye lot, greige batch or yarn lot, in either direction.</span></div>';
else if(S.sel===YL[0][0]){r+='<div class="kv3"><span class="kv"><small>Supplier</small><b>'+YL[0][3]+'</b></span><span class="kv"><small>Use</small><b>'+YL[0][1]+' yarn</b></span><span class="kv"><small>Quantity</small><b class="mono">'+YL[0][2]+' kg</b></span><span class="kv"><small>Received</small><b>Oct 2</b></span></div>'
+[['PDF','YL-7702 test report','Oct 2','214 KB'],['PDF','Calder Fiber scope certificate','Jan 15','388 KB']].map(function(f,i){return '<div class="fl in" style="animation-delay:'+(i*90)+'ms" id="fl'+i+'"><span class="fi">'+f[0]+'</span><span>'+f[1]+'</span><span class="mut">'+f[2]+'</span><span class="mut r">'+f[3]+'</span></div>';}).join('');}
else if(S.fw){r+='<div class="row h"><span>Order</span><span>Customer</span><span></span><span class="r">Yards</span></div>'+SHIP.map(function(s){return '<div class="row"><span class="mono">'+s[0]+'</span><span style="grid-column:2/4">'+s[1]+'</span><span class="mono r">'+n0(s[2])+' yd</span></div>';}).join('')
+'<div class="row"><span>In stock</span><span style="grid-column:2/4">'+STKR+' rolls, R-48211 among them</span><span class="mono r">'+n0(STK)+' yd</span></div>';}
else{r+='<div class="row h"><span>Level</span><span>Record</span><span>Detail</span><span class="r">Quantity</span></div>'
+'<div class="row"><span>Dye lot</span><span class="mono">'+LOT+'</span><span>Shade '+SH+', CH-0931 and CH-0944</span><span class="mono r">'+n0(LYD)+' yd</span></div>'
+'<div class="row"><span>Greige batch</span><span class="mono">'+GR+'</span><span>Woven on WO-5520</span><span class="mono r">'+n0(GYD)+' yd</span></div>'
+YL.map(function(y){return '<div class="row"><span>Yarn lot</span><span class="mono">'+y[0]+'</span><span>'+y[1]+', '+y[3]+'</span><span class="mono r">'+y[2]+' kg</span></div>';}).join('');}
if(S.q){r+='<div class="rac">';if(S.pk)r+='<span class="ap in" id="apk"><span class="fi">ZIP</span><span><b class="mono">AP-2611-B</b> generated: '+(S.q===LOT?6:7)+' records, 4 forward links, 2 files</span></span>';
else r+='<button type="button" class="bt pri" id="pkg"'+(S.fw?'':' disabled')+'>Package the record</button><span id="rtot">'+(S.fw?'Total '+n0(fwd())+' yd, matches the dye lot':'Trace forward first')+'</span>';r+='</div>';}
$('rec').innerHTML=r;
var st=$('sst');st.textContent=S.q?S.q+' traced':'Nothing traced';st.className='ch '+(S.q?'c-info':'c-idle');
S.an=false;}
function norm(v){v=String(v).trim().toUpperCase().replace(/\s/g,'');if(/^R?\d{5}$/.test(v))v='R-'+v.replace(/^R/,'');if(/^DL?2611B$/.test(v.replace(/-/g,'')))v=LOT;return v;}
function known(v){return v===LOT||!!ROLLS[v];}
[].forEach.call(root.querySelectorAll('[data-sample]'),function(b){b.addEventListener('click',function(){$('lin').value=b.getAttribute('data-v');$('flin').classList.remove('err');});});
function typeIn(inp,t,done){var i=0;(function k(){inp.value=t.slice(0,i);if(i<t.length){i++;later(k,60);}else done();})();}
function resetState(){S={q:null,sel:null,fw:false,pk:false,an:false};$('lin').value='';$('flin').classList.remove('err');render();}
var CAPAT=function(hh){return {l:14,t:52};};
var ST=[
{id:'q',target:function(){return mode==='try'?$('trc'):$('lin');},prompt:'Type R-48211 or pick a sample, then Trace',where:'below',
 ok:function(){var v=norm($('lin').value),b=!known(v);$('lem').textContent=v?'No record found. Try R-48211':'Enter a roll or lot, for example R-48211';$('flin').classList.toggle('err',b);return !b;},
 run:function(quick){var v=mode==='try'&&known(norm($('lin').value))?norm($('lin').value):'R-48211';S.q=v;S.sel=v;var go=function(){$('lin').value=v;$('flin').classList.remove('err');S.an=true;render();};if(mode==='watch'&&!quick)typeIn($('lin'),v,go);else go();},
 after:function(){return['Type or scan any roll',(S.q===LOT?LOT:S.q+' comes from '+LOT+', which')+' used greige '+GR+', woven from '+YL[0][0]+' and '+YL[1][0]+'.'];}},
{id:'yl',target:function(){return $('n-'+YL[0][0]);},prompt:'Open warp yarn lot '+YL[0][0],where:'right',run:function(){S.sel=YL[0][0];render();},
 after:function(){return['Attach supplier test reports and certificates',YL[0][0]+' from '+YL[0][3]+' carries its test report and scope certificate.'];}},
{id:'fw',target:function(){return $('n-'+LOT);},prompt:'Follow dye lot '+LOT+' forward',where:'below',run:function(){S.sel=LOT;S.fw=true;S.an=true;render();},
 after:function(){return['Follow the lot forward','Three shipments and the stock on hand: '+SHIP.map(function(s){return n0(s[2]);}).join(' + ')+' + '+n0(STK)+' = '+n0(fwd())+' yd.'];}},
{id:'pk',target:function(){return $('pkg');},prompt:'Package the record',where:'above',run:function(){S.pk=true;render();},
 after:function(){return['Package the record','One audit pack with every level, link and file, ready for a brand or an auditor.'];}}];
'''

for k, v in {'@LOT@': D.LOT, '@SHADE@': D.SHADE, '@LYD@': D.LOT_YD, '@LROLLS@': D.LOT_ROLLS, '@GR@': D.GREIGE_BATCH, '@GYD@': D.GREIGE_YD,
             '@STK@': D.STOCK_YD, '@STKR@': D.STOCK_ROLLS, '@YL@': json.dumps(D.YARN_LOTS), '@SHIP@': json.dumps(D.SHIP),
             '@ROLLS@': json.dumps(ROLLS), '@ICON@': ICON}.items():
    JS = JS.replace(k, str(v))
assert '@' not in JS
