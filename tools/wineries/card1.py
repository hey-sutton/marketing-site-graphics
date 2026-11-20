"""Wineries card 1: Blends & Bottled Cost. Layout: a record form with a side summary panel.
Top: the read only blend field with Open blend. Left: the blend record: the component wine tree (ratio, liters, cost per
liter), the bottling run with its preset case chips and the liters to bottles to cases conversion, then the bottle BOM
costed line by line. Right: the summary: the blend ratio bar, the run totals, cost per bottle and per case, the closure
change and the saved versions.
Money is kept in units of 1/10,000 dollar so every figure is exact. The case cost is 12 times the unrounded bottle
cost ($4.4725, so $53.67) plus the carton; the bottle cost is shown rounded to the cent ($4.47)."""
from frame_auto import header

SUMMARY = 'Blends & Bottled Cost (Reserve Red: 75% Cabernet Sauvignon, 15% Merlot, 10% Cabernet Franc, scaled to 1,200 cases: 10,800 L, 14,400 bottles of 750 ml, blend $4.19 per liter, $4.47 per bottle, $55.07 per case, screwcap version 2 at $53.99 per case)'
ARIA = 'Interactive product screen: open a blend and its component wines, scale it to a bottling run, convert liters to bottles and cases, read the cost per bottle and per case, and save a closure change as a new version'
STEPS = 5
STUDIO = dict(lede='A typical blend and costing screen on your Sutton data. Want it different? Describe the change.',
              examples=['Cost by vintage and block', 'Magnums and half bottles', 'Excise per case', 'A margin check by channel'],
              built_on='Items, BOMs, lots and costs', change='Fields, costs and views')

ICON = '<path d="M5 1.8h6l-.4 4.2a2.6 2.6 0 0 1-5.2 0z"/><path d="M8 8.6v4.6M5.2 13.8h5.6"/>'

CSS = (
 '.fld input[readonly]{background:#F4F4F5;color:#3F3F46;cursor:default;pointer-events:none}'
 '.g1{display:grid;grid-template-columns:420px 226px;grid-template-rows:62px 468px;gap:10px;padding:10px 44px 0 16px}'
 '.bf{display:flex;flex-direction:column;justify-content:center;gap:5px;padding:0 12px}.bf .frm{display:flex;align-items:flex-end;gap:8px}.bf .fld{width:150px}.bf .ctx{font-size:8.9px;color:#71717A}.bf .frm .rt{margin-left:auto}'
 '.rc{display:flex;flex-direction:column}.rc>.empt{margin:10px;flex:1}'
 '.sec{padding:7px 11px 0}.sec+.sec{border-top:1px solid #F0F0F1;margin-top:7px}.sec h4{margin:0 0 5px;font-size:9.6px;font-weight:600;display:flex;align-items:center;justify-content:space-between;gap:6px}.sec h4 .bt{font-size:9px;padding:2px 9px}'
 '.tre .row{grid-template-columns:16px 1fr 40px 54px 44px 44px;font-size:9.1px;min-height:23px;padding:0 6px}.tre .row>span:nth-child(n+3){text-align:right;font-family:"JetBrains Mono",ui-monospace,monospace}.tre .row.h>span{font-family:inherit!important}'
 '.tre .row small{display:block;font-size:8px;color:#71717A}.tre .row.rt0{background:#FAFAFA;font-weight:600}.tre .lnk{color:#A1A1AA;font-family:"JetBrains Mono",ui-monospace,monospace;font-size:10px}.tre .wh{color:#D4D4D8}'
 '.tre{border:1px solid #E4E4E7;border-radius:8px;overflow:hidden}'
 '.rn{display:flex;align-items:center;gap:6px}.rn .pc{border:1px solid #E4E4E7;border-radius:6px;padding:3px 8px;font-size:9px;color:#71717A;background:#fff}.rn .pc.on{border-color:#18181B;background:#18181B;color:#fff}.rn .rt{margin-left:auto}'
 '.cvs{display:grid;grid-template-columns:1fr 14px 1fr 14px 1fr;align-items:center;margin-top:6px}.cvs div{border:1px solid #E4E4E7;border-radius:7px;padding:4px 8px}.cvs div.ok{border-color:#BBF7D0;background:#F0FDF4}.cvs small{display:block;font-size:8.2px;color:#71717A}.cvs b{font-family:"JetBrains Mono",ui-monospace,monospace;font-size:11.5px}.cvs i{font-style:normal;color:#A1A1AA;text-align:center;font-size:10px}'
 '.calc{margin-top:5px;padding:4px 7px;border-radius:6px;background:#FAFAFA;border:1px solid #F0F0F1;font-family:"JetBrains Mono",ui-monospace,monospace;font-size:8.8px;text-align:center;white-space:nowrap}'
 '.lph{border:1px dashed #E4E4E7;border-radius:7px;background:#FAFAFA;padding:8px;font-size:8.8px;color:#A1A1AA;text-align:center}'
 '.bm .row{grid-template-columns:1fr 92px 54px;font-size:9px;min-height:20px;padding:0 6px}.bm .row>span:nth-child(n+2){text-align:right;font-family:"JetBrains Mono",ui-monospace,monospace}.bm .row.h>span{font-family:inherit!important}.bm .row.sm{background:#FAFAFA;font-weight:600}.bm .row.chg{background:#FFFBEB}'
 '.bm{border:1px solid #E4E4E7;border-radius:8px;overflow:hidden}'
 '.tot{margin-top:auto;padding:8px 11px;border-top:1px solid #E4E4E7;font-size:9px;color:#52525B;line-height:1.4;background:#FAFAFA}.sm .tot{padding-right:90px}'
 '.sm{grid-column:2;grid-row:1/3;display:flex;flex-direction:column}.sm>.empt{margin:10px;flex:1}'
 '.mx{margin:10px 11px 0}.mx .lb{font-size:8.6px;color:#71717A;margin-bottom:4px;display:flex;justify-content:space-between}.mx .br{display:flex;height:16px;border-radius:5px;overflow:hidden}.mx .br i{display:grid;place-items:center;font-style:normal;font-size:8.2px;color:#fff;font-family:"JetBrains Mono",ui-monospace,monospace}'
 '.mx .br .a{background:#7F1D1D}.mx .br .b{background:#B45353}.mx .br .c{background:#D6A3A3;color:#18181B}.mx .lg{display:flex;flex-direction:column;gap:2px;margin-top:5px;font-size:8.6px;color:#52525B}.mx .lg span{display:flex;align-items:center;gap:5px}.mx .lg i{width:8px;height:8px;border-radius:2px}'
 '.rs2{margin:9px 11px 0;display:grid;grid-template-columns:1fr 1fr 1fr;gap:5px}.rs2 div{border:1px solid #E4E4E7;border-radius:7px;padding:4px 6px}.rs2 small{display:block;font-size:7.9px;color:#71717A}.rs2 b{font-family:"JetBrains Mono",ui-monospace,monospace;font-size:9.6px}'
 '.cs{margin:9px 11px 0;display:flex;justify-content:space-between;align-items:flex-end}.cs .big{font-size:20px}'
 '.ck{margin:6px 11px 0;padding:6px 8px;border:1px solid #E4E4E7;border-radius:8px;display:flex;flex-direction:column;gap:3px;font-size:8.8px;color:#52525B}.ck div{display:flex;justify-content:space-between}.ck b{font-family:"JetBrains Mono",ui-monospace,monospace;color:#18181B}.ck .t{border-top:1px solid #F0F0F1;padding-top:3px;font-weight:600;color:#18181B}'
 '.chg2{margin:8px 11px 0;padding:7px 8px;border:1px solid #FDE68A;background:#FFFBEB;border-radius:8px;display:flex;flex-direction:column;gap:5px;font-size:8.8px;color:#78350F}.chg2 .t1{font-weight:600;font-size:9.2px;color:#18181B}.chg2 .bt{font-size:9px;padding:3px 8px;align-self:flex-start}'
 '.vs{margin:8px 11px 0}.vs .lb{font-size:9.2px;font-weight:600;margin-bottom:4px;display:flex;justify-content:space-between}.vs .row{grid-template-columns:22px 1fr 50px;font-size:8.9px;min-height:30px;padding:0 5px}.vs .row small{display:block;font-size:8px;color:#71717A}.vs .row>span:last-child{text-align:right;font-family:"JetBrains Mono",ui-monospace,monospace;font-weight:600}.vs .row.on{background:#F0FDF4}'
 '.note{margin:7px 11px 0;padding:5px 8px;border-radius:7px;font-size:8.8px;line-height:1.4;background:#F0FDF4;border:1px solid #BBF7D0;color:#166534}'
)

WIN = (
 header(ICON, 'Blend record', 'Component wines, bottling run and cost by version')
 + '<div class="g1"><div class="cd bf"><div class="frm"><label class="fld"><small>Blend</small>'
 '<input id="ibl" value="Reserve Red" readonly tabindex="-1" autocomplete="off" spellcheck="false"></label>'
 '<button type="button" class="bt pri" id="olb">Open blend</button><span class="rt" id="rst"></span></div><div class="ctx">Red blend, vintage 2024, bottling run in March</div></div>'
 '<div class="cd rc" id="rc"></div><div class="cd sm" id="sm"></div></div>'
)

JS = r'''
var FOC='.hd>*,.bf .fld,.bf .ctx,#olb,.rc .ct,.rc .sec,.rc .tot,.sm>*';
var CASES=1200,PER=12,ML=750,CAR=14000;
var CMP=[{nm:'Cabernet Sauvignon',tk:'Tank T-14, 2024',pc:75,cl:42000},{nm:'Merlot',tk:'Tank T-07, 2024',pc:15,cl:36000},{nm:'Cabernet Franc',tk:'Barrel lot B-22, 2024',pc:10,cl:50000}];
var DRY={glass:6200,cork:3800,screw:2900,cap:1200,label:2100};
var S;
function liters(){return CASES*PER*ML/1000;}
function bottles(){return liters()*1000/ML;}
function compL(c){return liters()*c.pc/100;}
function contrib(c){return c.cl*c.pc/100;}
function blendL(){return CMP.reduce(function(a,c){return a+contrib(c);},0);}
function wine(){return blendL()*ML/1000;}
function bottle(v){return wine()+DRY.glass+(v===2?DRY.screw:DRY.cork)+DRY.cap+DRY.label;}
function twelve(v){return bottle(v)*PER;}
function cse(v){return twelve(v)+CAR;}
function d2(x){return '$'+(Math.round(x/100)/100).toFixed(2);}
function d4(x){return '$'+(x/10000).toFixed(4);}
function render(){
var V=S.sv?2:1;
$('olb').className='bt '+(S.op?'done':'pri');$('olb').textContent=S.op?'Opened':'Open blend';
$('rst').innerHTML=!S.op?'':'<span class="ch '+(S.sv?'c-info':'c-idle')+'" id="ver">Version '+V+'</span>';
var r='<div class="ct"><span>'+(S.op?'Component wines':'Reserve Red')+'</span>'+(S.op?'<span class="ch c-idle mono">75 : 15 : 10</span>':'')+'</div>';
if(!S.op)r+='<div class="empt"><b>No blend open</b><span>Open a blend to see its component wines, scale it to a bottling run and cost it by the bottle and the case.</span></div>';
else{
r+='<div class="sec in"><div class="tre" id="tre"><div class="row h"><span></span><span>Wine</span><span>Ratio</span><span>Liters</span><span>Per L</span><span>In blend</span></div>'+
'<div class="row rt0"><span class="lnk">▾</span><span>Reserve Red<small>Blend, version '+V+'</small></span><span>100%</span><span id="ltot">'+(S.sc?n0(liters()):'<span class="wh">None</span>')+'</span><span></span><span id="bpl">'+(S.cs?d2(blendL()):'')+'</span></div>'+
CMP.map(function(c,i){return '<div class="row"><span class="lnk">'+(i===CMP.length-1?'└':'├')+'</span><span>'+c.nm+'<small>'+c.tk+'</small></span><span id="pc'+i+'">'+c.pc+'%</span><span id="cl'+i+'">'+(S.sc?n0(compL(c)):'<span class="wh">None</span>')+'</span><span>'+(S.cs?d2(c.cl):'')+'</span><span id="cb'+i+'">'+(S.cs?d2(contrib(c)):'')+'</span></div>';}).join('')+'</div></div>';
r+='<div class="sec in"><h4><span>Bottling run</span>'+(S.sc?'<button type="button" class="bt '+(S.cv?'done':'pri')+'" id="cvb">'+(S.cv?'Converted':'Convert')+'</button>':'')+'</h4><div class="rn"><span class="mut" style="font-size:8.6px">Cases</span><span class="pc">600</span><span class="pc'+(S.sc?' on':'')+'">1,200</span><span class="pc">2,400</span><span class="mut" style="font-size:8.6px">12 × 750 ml</span>'+
'<button type="button" class="bt '+(S.sc?'done':'pri')+' rt" id="scb">'+(S.sc?'Scaled to 1,200':'Scale to 1,200 cases')+'</button></div>'+
(S.cv?'<div class="cvs in" id="cvs"><div><small>Blend, liters</small><b id="cvl">'+n0(liters())+' L</b></div><i>→</i><div><small>750 ml bottles</small><b id="cvb2">'+n0(bottles())+'</b></div><i>→</i><div class="ok"><small>Cases of 12</small><b id="cvc">'+n0(bottles()/PER)+'</b></div></div>':'<div class="lph" style="margin-top:6px">Liters, bottles and cases show here once the run is converted.</div>')+'</div>';
r+='<div class="sec in"><h4><span>Cost per bottle'+(S.cs?', version '+V:'')+'</span>'+(S.cv?'<button type="button" class="bt '+(S.cs?'done':'pri')+'" id="csb">'+(S.cs?'Costed':'Cost')+'</button>':'')+'</h4>'+
(S.cs?'<div class="bm in" id="bm"><div class="row h"><span>BOM line</span><span>Qty and rate</span><span>Cost</span></div>'+
'<div class="row"><span>Wine, Reserve Red</span><span>0.75 L × '+d2(blendL())+'</span><span id="bwn">'+d4(wine())+'</span></div>'+
'<div class="row"><span>Glass, 750 ml Bordeaux</span><span>1 each</span><span>'+d2(DRY.glass)+'</span></div>'+
'<div class="row'+(S.sv?' chg':'')+'"><span id="bcl">'+(S.sv?'Screwcap, 30 × 60':'Natural cork, 44 mm')+'</span><span>1 each</span><span>'+d2(S.sv?DRY.screw:DRY.cork)+'</span></div>'+
'<div class="row"><span>Capsule</span><span>1 each</span><span>'+d2(DRY.cap)+'</span></div><div class="row"><span>Front and back label</span><span>1 set</span><span>'+d2(DRY.label)+'</span></div>'+
'<div class="row sm"><span>Per bottle</span><span class="mut">'+d4(bottle(V))+'</span><span id="bbt">'+d2(bottle(V))+'</span></div></div>':'<div class="lph">Each BOM line is costed once the run is converted.</div>')+'</div>';
r+='<div class="tot" id="cvcal">'+(S.cv?n0(liters())+' L ÷ 0.75 L = '+n0(bottles())+' bottles ÷ 12 = '+n0(bottles()/PER)+' cases.':'Component liters follow the ratio for any run size.')+'</div>';}
$('rc').innerHTML=r;
var m='<div class="ct"><span>Summary</span>'+(S.op?'<span class="ch c-idle">Version '+V+'</span>':'')+'</div>';
if(!S.op)m+='<div class="empt"><b>Nothing open yet</b><span>The blend, the run and the cost per bottle and case show here.</span></div>';
else{m+='<div class="mx in"><div class="lb"><span>Blend ratio</span><span class="mono">10,800 L run</span></div><div class="br"><i class="a" style="width:75%">75%</i><i class="b" style="width:15%">15%</i><i class="c" style="width:10%">10%</i></div>'+
'<div class="lg"><span><i style="background:#7F1D1D"></i>Cabernet Sauvignon</span><span><i style="background:#B45353"></i>Merlot</span><span><i style="background:#D6A3A3"></i>Cabernet Franc</span></div></div>';
m+='<div class="rs2 in"><div><small>Liters</small><b id="sl">'+(S.sc?n0(liters()):'None')+'</b></div><div><small>Bottles</small><b id="sb">'+(S.cv?n0(bottles()):'None')+'</b></div><div><small>Cases</small><b id="sc">'+(S.cv?n0(bottles()/PER):'None')+'</b></div></div>';
if(S.cs){m+='<div class="cs in"><div class="kv"><small>Per bottle</small><b class="big mono" id="spb">'+d2(bottle(V))+'</b></div><div class="kv" style="text-align:right"><small>Per case</small><b class="big mono" id="spc">'+d2(cse(V))+'</b></div></div>'+
'<div class="ck in" id="ck"><div><span>12 bottles at '+d4(bottle(V))+'</span><b id="s12">'+d2(twelve(V))+'</b></div><div><span>Carton</span><b>'+d2(CAR)+'</b></div><div class="t"><span>Per case</span><b>'+d2(cse(V))+'</b></div></div>';
if(!S.sv)m+='<div class="chg2 in"><span class="t1">Closure change</span><span>Natural cork '+d2(DRY.cork)+' to screwcap '+d2(DRY.screw)+'</span><button type="button" class="bt pri" id="svb">Save as version 2</button></div>';
else m+='<div class="vs in" id="vs"><div class="lb"><span>Versions</span><span class="ch c-idle">2</span></div>'+
'<div class="row" id="v1"><span class="mono">v1</span><span>Natural cork<small>Saved Feb 9</small></span><span id="v1c">'+d2(cse(1))+'</span></div>'+
'<div class="row on" id="v2"><span class="mono">v2</span><span>Screwcap<small>Saved today, active</small></span><span id="v2c">'+d2(cse(2))+'</span></div></div>'+
'<div class="note in" id="vnt">Version 2 costs <b id="vdf">'+d2(cse(1)-cse(2))+'</b> less per case. Version 1 is kept.</div>';}
else m+='<div class="lph in" style="margin:9px 11px 0">Cost per bottle and per case show here once costed.</div>';}
m+='<div class="tot">Every change is saved as a version.</div>';
$('sm').innerHTML=m;
}
function resetState(){S={op:false,sc:false,cv:false,cs:false,sv:false};render();}
var ST=[
{id:'op',target:function(){return $('olb');},prompt:'Open blend Reserve Red',where:'below',run:function(){S.op=true;render();},
 after:function(){return['A blend and its component wines','Reserve Red: 75% Cabernet Sauvignon, 15% Merlot and 10% Cabernet Franc.'];}},
{id:'sc',target:function(){return $('scb');},prompt:'Scale to 1,200 cases',where:'below',run:function(){S.sc=true;render();},
 after:function(){return['Scaled to a 1,200 case run',n0(compL(CMP[0]))+' + '+n0(compL(CMP[1]))+' + '+n0(compL(CMP[2]))+' = '+n0(liters())+' L of component wines.'];}},
{id:'cv',target:function(){return $('cvb');},prompt:'Convert to bottles and cases',where:'below',run:function(){S.cv=true;render();},
 after:function(){return['Liters to bottles and cases',n0(liters())+' L fills '+n0(bottles())+' bottles of 750 ml, packed in '+n0(bottles()/PER)+' cases of 12.'];}},
{id:'cs',target:function(){return $('csb');},prompt:'Cost the bottle and the case',where:'above',run:function(){S.cs=true;render();},
 after:function(){return['Cost per bottle and per case','Blend '+d2(blendL())+' per liter: '+d2(bottle(1))+' per bottle and '+d2(cse(1))+' per case with the carton.'];}},
{id:'sv',target:function(){return $('svb');},prompt:'Save the screwcap change as version 2',where:'above',run:function(){S.sv=true;render();},
 after:function(){return['A closure change saved as a new version','Version 2 with a screwcap costs '+d2(cse(2))+' per case. Version 1 stays at '+d2(cse(1))+'.'];}}];
'''
