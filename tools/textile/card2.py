"""Textile card 2: Production Stages & Outsourced Steps. Layout: stage board.
Five columns, Yarn, Weaving, Dyeing (outside processor), Finishing and Inspection, with the work order list at the left,
the outside processing record and the yield and cost panel under the board, and a summary strip at the bottom.
Pick WO-5520, see the work in process between stages, receive the dyed rolls back from the vendor, confirm the measured
yield at inspection. Every figure comes from tools/textile/data.py, where the brief's sums are asserted."""
import data as D
from frame_textile import header

SUMMARY = 'Production Stages & Outsourced Steps (follow WO-5520 from yarn through weaving, outside dyeing, finishing and inspection, receive from the vendor and confirm the measured yield)'
ARIA = 'Interactive demo: follow a work order from yarn through weaving, outside dyeing, finishing and inspection.'
STEPS = 4
STUDIO = dict(lede='A typical routing board with an outside step, built on your Sutton data with Studio. Want it different? Describe the change.',
              examples=['The dollar value of fabric held at each vendor', 'A shade approval gate after dyeing', 'A lab dip check before bulk dyeing', 'An alert when a vendor is late'],
              built_on='Routings, work orders and outsourced orders', change='Stages, fields and alerts')

ICON = '<rect x="1.8" y="2.5" width="3.2" height="11" rx=".8"/><rect x="6.4" y="2.5" width="3.2" height="7" rx=".8"/><rect x="11" y="2.5" width="3.2" height="9" rx=".8"/>'

CSS = (
 '.g2{padding:10px 0 0 16px;display:flex;flex-direction:column;gap:10px}.g2>*{width:656px;flex:none}'
 '.top{display:grid;grid-template-columns:118px 1fr;gap:8px;height:240px}'
 '.wol{display:flex;flex-direction:column}.wol .row{grid-template-columns:1fr;min-height:46px;padding:5px 10px;gap:1px;line-height:1.3;font-size:9.2px}.wol .row b{font-family:"JetBrains Mono",ui-monospace,monospace;font-size:10px;font-weight:600}'
 '.wol .row span{color:#71717A;font-size:8.6px}.wol .nt{margin-top:auto;padding:8px 10px;font-size:8.6px;color:#71717A;border-top:1px solid #F0F0F1;line-height:1.35}'
 '.brd{display:grid;grid-template-columns:repeat(5,1fr);gap:6px;position:relative}'
 '.cl{border:1px solid #E4E4E7;border-radius:8px;background:#FAFAFA;display:flex;flex-direction:column;min-width:0;overflow:hidden}.cl.out{background:#FFFBEB;border-color:#FDE68A}'
 '.clh{padding:7px 8px 5px;display:flex;flex-direction:column;gap:3px;border-bottom:1px solid #F0F0F1;background:#fff;min-height:52px}.clh b{font-size:10.2px;font-weight:600;display:flex;align-items:center;justify-content:space-between;gap:4px}'
 '.clh small{font-size:8.4px;color:#71717A;white-space:nowrap}.cl.out .clh{background:#FFFBEB;border-color:#FDE68A}.vb{font-size:8px;padding:1px 5px}'
 'button.clh{border:0;border-bottom:1px solid #FDE68A;text-align:left;cursor:pointer;font:inherit;width:100%;transition:background-color .2s}button.clh:hover,button.clh.fakehover{background:#FEF3C7}button.clh:focus-visible{outline:2px solid #18181B;outline-offset:-2px}'
 '.cnt{font-family:"JetBrains Mono",ui-monospace,monospace;font-size:8.8px;color:#18181B;min-height:12px}.cnt.z{color:#A1A1AA}'
 '.wc{margin:6px;border:1px solid #E4E4E7;border-radius:7px;background:#fff;padding:6px 7px;display:flex;flex-direction:column;gap:4px;font-size:8.8px;line-height:1.3;box-shadow:0 1px 2px rgba(0,0,0,.04)}'
 '.wc .tp{display:flex;align-items:center;justify-content:space-between;gap:3px 4px;flex-wrap:wrap}.wc .id,.wc .nw{white-space:nowrap}.wc .id{font-family:"JetBrains Mono",ui-monospace,monospace;font-weight:600;font-size:9.2px}.wc .ch{font-size:8px;padding:1px 5px}.wc .q{font-weight:600;font-size:10px}.wc .s{color:#71717A;font-size:8.4px}'
 '.wc.wait{background:transparent;border-style:dashed;box-shadow:none;color:#A1A1AA}'
 '.rls{display:grid;grid-template-columns:repeat(3,1fr);gap:3px}.rl{font-family:"JetBrains Mono",ui-monospace,monospace;font-size:7.8px;text-align:center;border-radius:3px;padding:1px 0;background:#F4F4F5;color:#52525B}'
 '.rl.g{background:#F4F4F5}.rl.v{background:#FEF3C7;color:#92400E}.rl.d{background:#DBEAFE;color:#1E3A8A}.rl.m{background:#DCFCE7;color:#166534}'
 '.bpr{position:absolute;inset:52px 0 0 0;display:flex;align-items:center;justify-content:center;pointer-events:none}.bpr .empt{width:300px;background:#fff}'
 '.low{display:grid;grid-template-columns:248px 1fr;gap:10px;height:236px}'
 '.vp,.cp{display:flex;flex-direction:column;min-width:0}.vp .empt,.cp .empt,.sm2 .empt{margin:10px;flex:1;padding:10px}'
 '.kvl{display:grid;grid-template-columns:76px 1fr;font-size:9.4px;padding:0 11px}.kvl span{padding:4px 0;border-top:1px solid #F4F4F5;line-height:1.3}.kvl span:nth-child(-n+2){border-top:0}.kvl .k{color:#71717A}'
 '.vp .ac{margin-top:auto;padding:8px 11px 10px;display:flex;align-items:center;gap:8px;border-top:1px solid #F0F0F1;font-size:8.8px;color:#71717A}'
 '.ct2{display:grid;grid-template-columns:1fr 70px 62px 70px;padding:0 11px;font-size:9.3px;gap:6px}.ct2 span{padding:4px 0;border-top:1px solid #F4F4F5;white-space:nowrap}.ct2 .hh{color:#71717A;font-size:8.6px;border-top:0}.ct2 .tot{font-weight:600;border-top:1px solid #E4E4E7}'
 '.yl{margin-top:auto;border-top:1px solid #F0F0F1;padding:8px 11px 10px;display:grid;grid-template-columns:1fr 1fr;gap:10px;align-items:end}'
 '.yb{border:1px solid #F0F0F1;border-radius:7px;padding:6px 9px;display:flex;flex-direction:column;gap:2px;background:#FAFAFA;min-height:58px}.yb small{font-size:8.6px;color:#71717A}.yb b{font-size:15px;font-weight:600;letter-spacing:-.01em}.yb em{font-style:normal;font-size:8.6px;color:#71717A}'
 '.yb.ok{background:#F0FDF4;border-color:#BBF7D0}.yb.old b{color:#A1A1AA;text-decoration:line-through}'
 '.frm2{display:flex;align-items:flex-end;gap:6px}.frm2 .fld{width:74px;position:relative}.frm2 .fld .em{position:absolute;top:-14px;left:0;white-space:nowrap}'
 '.sm2{height:44px;display:flex;align-items:center;gap:10px;padding:0 11px;font-size:9.6px;white-space:nowrap}.sm2 .big2{font-size:13px;font-weight:600}.sm2 .sp{color:#D4D4D8}'
)

WIN = (
 header(ICON, 'Production', 'Routing board, woven fabric')
 + '<div class="g2"><div class="top"><div class="cd wol" id="wol"></div><div class="brd" id="brd"></div></div>'
 '<div class="low"><div class="cd vp" id="vp"></div><div class="cd cp" id="cp"></div></div><div class="cd sm2" id="sm2"></div></div>'
)

JS = r'''
var FOC='.hd>*,.wol .row,.wol .nt,.cl,.vp .ct,.kvl,.vp .ac>*,.cp .ct,.ct2,.yb,.frm2,.sm2>*';
var WARP=@WARP@,WEFT=@WEFT@,GR=@GR@,GRP=@GRP@,DY=@DY@,DYP=@DYP@,FL=@FL@,BOMP=@BOMP@;
var RY=@RY@,RD=@RD@,RF=@RF@;
var S;
function kg(){return WARP+WEFT;}
function gyd(){return GR*GRP;}
function dyd(){return DY*DYP;}
function cYarn(){return Math.round(kg()*RY*100);}
function cDye(){return Math.round(gyd()*RD*100);}
function cFin(){return Math.round(dyd()*RF*100);}
function cTot(){return cYarn()+cDye()+cFin();}
function bomYd(){return gyd()*(100-BOMP)/100;}
function c2(x){return m2(x/100);}
function per(y){return m2(Math.round(cTot()/y)/100);}
function pills(n,v,cls){var o='';for(var i=0;i<n;i++)o+='<span class="rl '+cls+'">'+(Array.isArray(v)?v[i]:v)+'</span>';return '<div class="rls">'+o+'</div>';}
function split6(v){var b=Math.floor(v/6),r=v-b*6,a=[];for(var i=0;i<6;i++)a.push(b+(i<r?1:0));return a;}
function render(){
var w='<div class="ct"><span>Work orders</span></div>'+[['WO-5520','Navy twill TW-5810','2,400 yd greige'],['WO-5524','Canvas duck CD-1210','1,800 yd greige']].map(function(x){var on=S.wo&&x[0]==='WO-5520';
return '<button type="button" class="row'+(on?' sel':'')+'" id="w-'+x[0]+'"><b>'+x[0]+'</b><span>'+x[1]+'</span><span>'+x[2]+'</span></button>';}).join('')+'<div class="nt">Pick a work order to place it on the routing.</div>';
$('wol').innerHTML=w;
var C=[['Yarn','In house'],['Weaving','In house'],['Dyeing','Outside processor'],['Finishing','In house'],['Inspection','In house']];
var my=S.my||0,cn=[],cards=[];
if(S.wo){
cn=[[0,'0 kg left'],[0,'0 rolls, 0 yd'],S.rc?[0,'0 rolls out']:[1,GR+' rolls, '+n0(gyd())+' yd out'],S.cf?[0,'0 rolls, 0 yd']:S.rc?[1,DY+' rolls, '+n0(dyd())+' yd']:[0,'0 rolls, 0 yd'],S.cf?[1,DY+' rolls, '+n0(my)+' yd']:[0,'0 rolls, 0 yd']];
cards=['<div class="wc in"><div class="tp"><span class="id">WO-5520</span><span class="ch c-ok">Done</span></div><span class="q">'+n0(kg())+' kg issued</span><span class="s">Warp '+WARP+' kg, <span class="nw">YL-7702</span></span><span class="s">Weft '+WEFT+' kg, <span class="nw">YL-7715</span></span></div>',
'<div class="wc in" style="animation-delay:80ms"><div class="tp"><span class="id">WO-5520</span><span class="ch c-ok">Done</span></div><span class="q">'+n0(gyd())+' yd greige</span><span class="s">'+GR+' rolls of '+GRP+' yd</span>'+pills(GR,GRP,'g')+'</div>',
S.rc?'<div class="wc'+(S.fr?' flash':'')+'"><div class="tp"><span class="id">WO-5520</span><span class="ch c-ok">Received</span></div><span class="q">'+n0(dyd())+' yd back</span><span class="ch c-warn" id="var">−'+(gyd()-dyd())+' yd, '+((gyd()-dyd())*100/gyd()).toFixed(1)+'%</span>'+pills(DY,DYP,'d')+'</div>'
:'<div class="wc in" style="animation-delay:160ms"><div class="tp"><span class="id">WO-5520</span><span class="ch c-warn">At vendor</span></div><span class="q">'+n0(gyd())+' yd out</span><span class="s">Sent Nov 3, due Nov 14</span>'+pills(GR,GRP,'v')+'</div>',
S.cf?'<div class="wc"><div class="tp"><span class="id">WO-5520</span><span class="ch c-ok">Done</span></div><span class="q">'+n0(dyd())+' yd in</span><span class="s" id="fls">'+n0(dyd()-my)+' yd lost at finishing</span>'+pills(DY,DYP,'d')+'</div>'
:S.rc?'<div class="wc in"><div class="tp"><span class="id">WO-5520</span><span class="ch c-info">In process</span></div><span class="q">'+n0(dyd())+' yd in</span><span class="s">Heat set and compacted</span>'+pills(DY,DYP,'d')+'</div>'
:'<div class="wc wait">Waiting for dyed rolls</div>',
S.cf?'<div class="wc in"><div class="tp"><span class="id">WO-5520</span><span class="ch c-ok">Done</span></div><span class="q" id="iq">'+n0(my)+' yd measured</span><span class="s">To stock as <span class="nw mono">DL-2611-B</span></span>'+pills(DY,split6(my),'m')+'</div>'
:'<div class="wc wait">'+(S.rc?'Measure after finishing':'Waiting')+'</div>'];}
var b=C.map(function(c,i){var out=i===2,hd=(out?'<button type="button" class="clh" id="dyh">':'<div class="clh">')+'<b>'+c[0]+(out?'<span class="ch c-warn vb">'+(S.wo?(S.rc?'0':'1')+' out':'Vendor')+'</span>':'')+'</b><small>'+(out?'Bayside Dye Works':c[1])+'</small>'
+'<span class="cnt'+(cn[i]&&cn[i][0]?'':' z')+'" id="cn'+i+'">'+(S.wip&&cn[i]?cn[i][1]:'')+'</span>'+(out?'</button>':'</div>');
return '<div class="cl'+(out?' out':'')+'" id="col'+i+'">'+hd+(cards[i]||'')+'</div>';}).join('');
if(!S.wo)b+='<div class="bpr"><div class="empt"><b>Select a work order</b><span>Its yarn, greige and dyed rolls take their place in each stage.</span></div></div>';
$('brd').innerHTML=b;
var v='<div class="ct"><span>Outside processing</span>'+(S.wip?'<span class="ch '+(S.rc?'c-ok':'c-warn')+'">'+(S.rc?'Received':'At vendor')+'</span>':'')+'</div>';
if(!S.wip)v+='<div class="empt"><b>No outside step open</b><span>'+(S.wo?'Open the Dyeing column to see what sits at the vendor.':'The vendor record shows once a work order is picked.')+'</span></div>';
else{v+='<div class="kvl'+(S.fv?' in':'')+'"><span class="k">Vendor</span><span>Bayside Dye Works</span><span class="k">Order</span><span class="mono">OP-2207, WO-5520</span><span class="k">Sent</span><span class="mono">'+n0(gyd())+' yd, '+GR+' rolls</span><span class="k">Due</span><span>Nov 14</span>'
+'<span class="k">Returned</span><span class="mono" id="vret">'+(S.rc?n0(dyd())+' yd, '+DY+' rolls':'Not yet')+'</span><span class="k">Variance</span><span class="mono" id="vvar">'+(S.rc?'−'+(gyd()-dyd())+' yd, '+((gyd()-dyd())*100/gyd()).toFixed(1)+'%':'Open')+'</span></div>';
v+='<div class="ac">'+(S.rc?'<span class="ch c-ok">Back in routing</span><span>Next: finishing</span>':'<button type="button" class="bt pri" id="rcv">Receive from vendor</button><span>Dyeing is step 3 of 5</span>')+'</div>';}
$('vp').innerHTML=v;
var c='<div class="ct"><span>Yield and cost per yard'+(S.wo?', WO-5520':'')+'</span>'+(S.cf?'<span class="ch c-ok">Measured</span>':S.wo?'<span class="ch c-idle">BOM estimate</span>':'')+'</div>';
if(!S.wo)c+='<div class="empt"><b>No work order picked</b><span>Inputs, yield and cost per yard fill in from the work order.</span></div>';
else{c+='<div class="ct2"><span class="hh">Input</span><span class="hh r">Quantity</span><span class="hh r">Rate</span><span class="hh r">Cost</span>'
+'<span>Yarn, warp and weft</span><span class="mono r">'+n0(kg())+' kg</span><span class="mono r">'+m2(RY)+'</span><span class="mono r" id="cy">'+c2(cYarn())+'</span>'
+'<span>Dyeing, Bayside</span><span class="mono r">'+n0(gyd())+' yd</span><span class="mono r">'+m2(RD)+'</span><span class="mono r" id="cd">'+c2(cDye())+'</span>'
+'<span>Finishing</span><span class="mono r">'+(S.rc?n0(dyd())+' yd':'')+'</span><span class="mono r">'+m2(RF)+'</span><span class="mono r" id="cf">'+(S.rc?c2(cFin()):'After receipt')+'</span>'
+'<span class="tot">Total</span><span class="tot"></span><span class="tot"></span><span class="mono r tot" id="ctot">'+(S.rc?c2(cTot()):'')+'</span></div>';
c+='<div class="yl"><div class="yb'+(S.cf?' old':'')+'"><small>BOM estimate, '+BOMP+'% loss</small><b class="mono" id="pbom">'+(S.rc?per(bomYd())+' per yd':n0(bomYd())+' yd')+'</b><em>'+n0(bomYd())+' yd expected</em></div>';
if(S.cf)c+='<div class="yb ok in"><small>Measured at inspection</small><b class="mono" id="pact">'+per(my)+' per yd</b><em id="pem">'+n0(my)+' yd, replaces the estimate</em></div>';
else c+='<div class="frm2 frm" id="cfr"><label class="fld" id="fmy"><small>Measured yd</small><input id="myd" value="'+(S.rc?(S.mv||''):'')+'" inputmode="numeric" autocomplete="off" aria-label="Measured yards"'+(S.rc?'':' disabled')+'><span class="em" id="mem">Enter 1 to '+n0(dyd())+'</span></label><button type="button" class="bt pri" id="cfm"'+(S.rc?'':' disabled')+'>Confirm yield</button></div>';
c+='</div>';}
$('cp').innerHTML=c;
var st=S.cf?5:S.rc?3:S.wo?2:0;
$('sm2').innerHTML=S.wo?'<span class="ch '+(S.cf?'c-ok':'c-info')+'" id="stg">'+st+' of 5 stages complete</span><span>WO-5520</span><span class="sp">|</span><span>In</span><span class="big2 mono" id="sin">'+n0(kg())+' kg</span><span class="mut">yarn</span><span class="sp">|</span><span>Out</span><span class="big2 mono" id="sout">'+(S.cf?n0(my)+' yd':'Open')+'</span><span class="mut">'+(S.cf?'finished fabric':'until inspection')+'</span>'
:'<span class="mut">Totals show once a work order is picked.</span>';
S.fv=S.fr=false;}
function myVal(){var v=String($('myd').value).replace(/[,\s]/g,'');return /^\d+$/.test(v)?+v:NaN;}
$('cp').addEventListener('input',function(e){if(e.target&&e.target.id==='myd')S.mv=e.target.value;});
function resetState(){S={wo:false,wip:false,rc:false,cf:false,my:0,mv:''};render();}
var CAPAT=function(hh){return cur===1||cur===2?{l:290,t:420}:cur===3?{l:14,t:52}:{l:14,t:420};};
var ST=[
{id:'wo',target:function(){return $('w-WO-5520');},prompt:'Pick work order WO-5520',where:'right',run:function(){S.wo=true;render();},
 after:function(){return['Pick a work order','WO-5520: '+n0(kg())+' kg of yarn in, '+n0(gyd())+' yd woven, now at the dye house.'];}},
{id:'wip',target:function(){return $('dyh');},prompt:'Open the Dyeing column',where:'below',run:function(){S.wip=true;S.fv=true;render();},
 after:function(){return['Work in process between stages','Weaving 0 yd left, '+n0(gyd())+' yd out at Bayside Dye Works, Finishing 0 yd.'];}},
{id:'rcv',target:function(){return $('rcv');},prompt:'Receive the dyed rolls from the vendor',where:'above',run:function(){S.rc=true;S.fr=true;S.mv=String(@MEAS@);render();},
 after:function(){return['Steps at an outside processor sit in the routing',DY+' dyed rolls of '+DYP+' yd back: '+n0(dyd())+' yd. Shrink '+(gyd()-dyd())+' yd, '+((gyd()-dyd())*100/gyd()).toFixed(1)+' percent.'];}},
{id:'cfm',target:function(){return $('cfm');},prompt:'Confirm the measured yards',where:'above',
 ok:function(){var v=myVal(),b=!(v>=1&&v<=dyd());$('mem').textContent=isNaN(v)?'Enter a number of yards':'Enter 1 to '+n0(dyd());$('fmy').classList.toggle('err',b);return !b;},
 run:function(){var v=mode==='try'?myVal():NaN;S.my=v>=1&&v<=dyd()?v:@MEAS@;S.cf=true;render();},
 after:function(){return['Measured yield replaces the BOM estimate',n0(S.my)+' yd measured, '+n0(dyd()-S.my)+' yd lost at finishing. Cost per yard '+per(bomYd())+' estimated, '+per(S.my)+' actual.'];}}];
'''

for k, v in {'@WARP@': D.WARP_KG, '@WEFT@': D.WEFT_KG, '@GR@': D.GREIGE_ROLLS, '@GRP@': D.GREIGE_PER, '@DY@': D.DYED_ROLLS, '@DYP@': D.DYED_PER,
             '@FL@': D.FINISH_LOSS, '@BOMP@': D.BOM_SHRINK_PCT, '@RY@': D.YARN_RATE, '@RD@': D.DYE_RATE, '@RF@': D.FIN_RATE, '@MEAS@': D.MEASURED}.items():
    JS = JS.replace(k, str(v))
assert '@' not in JS
