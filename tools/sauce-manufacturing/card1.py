"""Sauce manufacturing card 1: Batch Scaling & Conversions. Layout: a record form with a side summary panel.
Left: the batch form (read only kettle size and Scale), then the formula list and the open formula's lines by weight,
with an lb and gal toggle. Right: the kettle summary (total, scale factor, blend density), the soy sauce tote
conversion and the requirement against stock. Kettle lines are stored as gallons and density, so pounds = gallons x
density for every line, and the 20 lb test pot is the same formula divided by the scale factor."""
from frame_auto import header

SUMMARY = 'Batch Scaling & Conversions (open the TB-100 teriyaki base, scale a 20 lb test pot to a 500 gal kettle, show lb and gal, convert a 270 lb soy sauce tote to 30 gal, compare with the 40 gal requirement)'
ARIA = 'Interactive product screen: open a base sauce formula by weight, scale it from a 20 lb test pot to a 500 gallon kettle, show every line in pounds and gallons, convert a soy sauce tote to stocked gallons and compare the requirement with stock on hand'
STEPS = 5
STUDIO = dict(lede='A typical batch scaling screen on your Sutton data. Want it different? Describe the change.',
              examples=['Scale by kettle or by case count', 'Density by temperature', 'A tote fill check at receiving', 'Liters and kilograms side by side'],
              built_on='Items, BOMs, units and lots', change='Units, columns and views')

ICON = '<path d="M3 6.5h10l-1 6.2a1.5 1.5 0 0 1-1.5 1.3h-5A1.5 1.5 0 0 1 4 12.7z"/><path d="M2 6.5h12M6 4c0-1 .8-1.6 0-2.5M9.5 4c0-1 .8-1.6 0-2.5"/>'

CSS = (
 '.fld input[readonly]{background:#F4F4F5;color:#3F3F46;cursor:default;pointer-events:none}'
 '.g1{display:grid;grid-template-columns:420px 226px;grid-template-rows:62px 468px;gap:10px;padding:10px 44px 0 16px}'
 '.bf{display:flex;flex-direction:column;justify-content:center;gap:5px;padding:0 12px}.bf .frm{display:flex;align-items:flex-end;gap:8px}.bf .fld{width:150px}.bf .ctx{font-size:8.9px;color:#71717A}'
 '.bf .frm .grow{display:flex;justify-content:flex-end}'
 '.fm{display:flex;flex-direction:column}.sm{grid-column:2;grid-row:1/3;display:flex;flex-direction:column}.sm>.empt{margin:10px;flex:1}'
 '.fl .row{grid-template-columns:62px 1fr auto;min-height:32px;font-size:9.6px}.fl .row small{color:#71717A;font-size:8.6px}'
 '.seg{display:inline-flex;padding:2px;gap:2px;border:1px solid #E4E4E7;border-radius:7px;background:#FAFAFA}.seg button{font:inherit;font-size:9.2px;font-weight:500;padding:2px 8px;border:0;border-radius:5px;background:transparent;color:#52525B;cursor:pointer}.seg button.on{background:#18181B;color:#fff}.seg button:focus-visible{outline:2px solid #18181B;outline-offset:1px}'
 '.ln{border-top:1px solid #E4E4E7}.ln .sub{display:flex;align-items:center;justify-content:space-between;padding:6px 11px;font-size:9.4px;font-weight:600}'
 '.ln .row{grid-template-columns:1fr 62px 70px;font-size:9.5px;min-height:27px}.ln.g .row{grid-template-columns:1fr 62px 70px 62px}.ln .row>span:nth-child(n+2){text-align:right;font-family:"JetBrains Mono",ui-monospace,monospace}.ln .row.h>span{font-family:inherit!important}'
 '.ln .row.t{font-weight:600;background:#FAFAFA}.ln .row.soy{background:#FEF9E7}'
 '.tot{margin-top:auto;padding:9px 11px;border-top:1px solid #E4E4E7;font-size:9.1px;color:#52525B;line-height:1.4;background:#FAFAFA}'
 '.sm .bx{padding:10px 11px 0}.sm .big{font-size:22px}.pair{display:grid;grid-template-columns:1fr 1fr;gap:8px;padding:9px 11px 0}.pair .kv b{font-size:12px;font-family:"JetBrains Mono",ui-monospace,monospace}'
 '.tote{margin:10px 11px 0;border:1px solid #E4E4E7;border-radius:7px;overflow:hidden}.tote .th{display:flex;align-items:center;justify-content:space-between;padding:6px 9px;font-size:9.6px;font-weight:600;border-bottom:1px solid #F0F0F1}.tote .th .bt{font-size:9px;padding:3px 8px}'
 '.tote .tb{padding:7px 9px;font-size:9.2px;color:#52525B;line-height:1.5}.tote .tb b{font-family:"JetBrains Mono",ui-monospace,monospace;color:#18181B}.tote.ok{border-color:#BBF7D0}.tote.ok .tb{background:#F0FDF4}'
 '.cmp .row{grid-template-columns:1fr 50px 50px;font-size:9.2px;min-height:25px;padding:0 9px}.cmp .row span:nth-child(n+2){text-align:right;font-family:"JetBrains Mono",ui-monospace,monospace}.cmp .row.h span{font-family:inherit!important}.cmp .row.bad{background:#FEF2F2;color:#B91C1C;font-weight:600}'
)

WIN = (
 header(ICON, 'Batch scaling', 'Formulas by weight, scaled to the kettle in use')
 + '<div class="g1"><div class="cd bf" id="bf"><div class="frm"><label class="fld"><small>Kettle size</small>'
 '<input id="iks" value="500 gal" readonly tabindex="-1" autocomplete="off" spellcheck="false"></label>'
 '<span id="sbw"></span><span class="grow"></span></div><div class="ctx">Kettle K-2, full batch on Line 1</div></div>'
 '<div class="cd fm" id="fm"></div><div class="cd sm" id="sm"></div></div>'
)

JS = r'''
var FOC='.hd>*,.bf .fld,.bf .ctx,#sbw,.fm .ct,.fl .row,.ln .sub,.ln .row,.fm .tot,.sm>*,.tote .th>*,.tote .tb';
var FORMS=[['TB-100','Teriyaki base','By weight, 20 lb test pot'],['BB-210','Smoky barbecue base','By weight, 25 lb test pot'],['GS-305','Garlic stir fry base','By weight, 20 lb test pot']];
var KG=500,POT=20;
var LN=[['Soy sauce',40,9.0],['Water',300,8.34],['Brown sugar syrup',90,11.0],['Rice vinegar',50,8.4],['Garlic puree',15,9.2],['Ginger puree',5,9.0]];
var TOTE={id:'T-0412',fill:270,lot:'SY-6120'};
var S;
function lb(l){return Math.round(l[1]*l[2]*100)/100;}
function klb(){return LN.reduce(function(a,l){return a+lb(l);},0);}
function kgal(){return LN.reduce(function(a,l){return a+l[1];},0);}
function F(){return klb()/POT;}
function d1(x){return x.toLocaleString('en-US',{minimumFractionDigits:1,maximumFractionDigits:1});}
function d2(x){return x.toLocaleString('en-US',{minimumFractionDigits:2,maximumFractionDigits:2});}
function SOY(){return LN[0];}
function toteGal(){return TOTE.fill/SOY()[2];}
function render(){
$('sbw').innerHTML=S.sc?'<button type="button" class="bt done" disabled>Scaled</button>':'<button type="button" class="bt pri" id="scb">Scale to '+KG+' gal</button>';
var f='<div class="ct"><span>Formulas</span>'+(S.op?'<span class="seg" role="group" aria-label="Units"><button type="button" id="u-lb" class="'+(S.gal?'':'on')+'" aria-pressed="'+(S.gal?'false':'true')+'">lb</button><button type="button" id="u-gal" class="'+(S.gal?'on':'')+'" aria-pressed="'+(S.gal?'true':'false')+'">lb and gal</button></span>':'')+'</div>';
f+='<div class="fl">'+FORMS.map(function(x,i){return '<button type="button" class="row'+(S.op&&i===0?' sel':'')+'" id="f-'+x[0]+'"><span class="mono"><b>'+x[0]+'</b></span><span>'+x[1]+' <small>'+x[2]+'</small></span><span class="ch '+(i===0?'c-info':'c-idle')+'">v'+(i===0?4:2)+'</span></button>';}).join('')+'</div>';
if(!S.op)f+='<div class="empt" style="margin:10px;flex:1"><b>No formula open</b><span>Open a base formula to see its lines by weight, then scale it to the kettle.</span></div>';
else{f+='<div class="ln in'+(S.gal?' g':'')+'"><div class="sub"><span>TB-100 lines, '+(S.sc?'scaled to '+KG+' gal':'base '+POT+' lb test pot')+'</span>'+(S.sc?'<span class="ch c-ok">Factor '+d2(F())+'</span>':'<span class="ch c-idle">Base</span>')+'</div>'+
'<div class="row h"><span>Ingredient</span><span>lb per gal</span><span>lb</span>'+(S.gal?'<span>gal</span>':'')+'</div>'+
LN.map(function(l,i){return '<div class="row'+(i===0&&S.cmp?' soy':'')+'"><span>'+l[0]+'</span><span>'+d2(l[2])+'</span><span id="lb-'+i+'">'+(S.sc?d1(lb(l)):d2(lb(l)/F()))+'</span>'+(S.gal?'<span id="ga-'+i+'">'+d1(S.sc?l[1]:l[1]/F())+'</span>':'')+'</div>';}).join('')+
'<div class="row t"><span>Total</span><span></span><span id="lbt">'+(S.sc?d1(klb()):d2(POT))+'</span>'+(S.gal?'<span id="gat">'+d1(S.sc?kgal():kgal()/F())+'</span>':'')+'</div></div>';}
f+='<div class="tot">Each line converts with its own density, so pounds and gallons always agree.</div>';
$('fm').innerHTML=f;
var m='<div class="ct"><span>Kettle summary</span>'+(S.sc?'<span class="ch c-ok">K-2</span>':'')+'</div>';
if(!S.op)m+='<div class="empt"><b>Nothing scaled yet</b><span>Totals, the scale factor and stock for the open formula show here.</span></div>';
else{m+=S.sc?'<div class="bx in"><div class="kv"><small>Kettle batch</small><b class="big mono" id="kgl">'+n0(kgal())+' gal</b></div></div><div class="pair in"><div class="kv"><small>Weight</small><b id="klb">'+n0(Math.round(klb()))+' lb</b></div><div class="kv"><small>Blend density</small><b id="kbd">'+d2(klb()/kgal())+'</b></div><div class="kv"><small>Scale factor</small><b id="ksf">'+d2(F())+'</b></div><div class="kv"><small>Test pot</small><b>'+POT+' lb</b></div></div>':
'<div class="bx in"><div class="kv"><small>Base formula</small><b class="big mono">'+POT+' lb</b></div><div class="kv" style="margin-top:6px"><small>Lines</small><b>'+LN.length+' ingredients, by weight</b></div></div>';
m+='<div class="tote'+(S.tote?' ok':'')+'"><div class="th"><span>Tote '+TOTE.id+', soy sauce</span>'+(S.tote?'<span class="ch c-ok">Stocked</span>':'<button type="button" class="bt" id="tcb">Convert tote</button>')+'</div><div class="tb">Lot '+TOTE.lot+', actual fill <b>'+TOTE.fill+' lb</b>'+(S.tote?'<br><b id="tgl">'+d1(toteGal())+' gal</b> stocked at '+d1(SOY()[2])+' lb per gal':'')+'</div></div>';
if(S.tote)m+='<div class="pair"><button type="button" class="bt'+(S.cmp?' done':'')+'" id="cpb"'+(S.cmp?' disabled':'')+'>'+(S.cmp?'Compared':'Compare')+'</button></div>';
if(S.cmp){var need=SOY()[1],sh=need-toteGal();m+='<div class="cmp in" style="margin-top:8px"><div class="row h"><span>Soy sauce</span><span>gal</span><span>lb</span></div><div class="row"><span>Required</span><span id="rqg">'+d1(need)+'</span><span id="rql">'+n0(lb(SOY()))+'</span></div><div class="row"><span>On hand</span><span id="ohg">'+d1(toteGal())+'</span><span>'+n0(TOTE.fill)+'</span></div><div class="row bad"><span>Shortfall</span><span id="sfg">'+d1(sh)+'</span><span id="sfl">'+n0(sh*SOY()[2])+'</span></div></div>';}}
m+='<div class="tot">One record per formula and kettle.</div>';
$('sm').innerHTML=m;
}
function resetState(){S={op:false,sc:false,gal:false,tote:false,cmp:false};render();}
var CAPAT=function(hh){return {l:14,t:visH()-hh-14};};
var ST=[
{id:'op',target:function(){return $('f-TB-100');},prompt:'Open the teriyaki base',where:'below',run:function(){S.op=true;render();},
 after:function(){return['A base formula, by weight','TB-100 for a '+POT+' lb test pot: '+LN.length+' lines, soy sauce '+d2(lb(SOY())/F())+' lb.'];}},
{id:'sc',target:function(){return $('scb');},prompt:'Scale to '+KG+' gal',where:'below',run:function(){S.sc=true;render();},
 after:function(){return['From test pot to full kettle','Every line times '+d2(F())+': '+n0(Math.round(klb()))+' lb for '+KG+' gal. Soy sauce '+n0(lb(SOY()))+' lb.'];}},
{id:'gal',target:function(){return $('u-gal');},prompt:'Show lb and gal',where:'below',run:function(){S.gal=true;render();},
 after:function(){return['Pounds and gallons from each density','Soy sauce '+d1(SOY()[1])+' gal at '+d1(SOY()[2])+' lb per gal is '+n0(lb(SOY()))+' lb. Lines total '+n0(kgal())+' gal.'];}},
{id:'tote',target:function(){return $('tcb');},prompt:'Convert the tote',where:'below',run:function(){S.tote=true;render();},
 after:function(){return['A tote becomes stocked gallons','Actual fill '+TOTE.fill+' lb divided by '+d1(SOY()[2])+' lb per gal is '+d1(toteGal())+' gal of soy sauce.'];}},
{id:'cmp',target:function(){return $('cpb');},prompt:'Compare with stock',where:'below',run:function(){S.cmp=true;render();},
 after:function(){return['Requirement against stock on hand',d1(SOY()[1])+' gal needed, '+d1(toteGal())+' gal on hand: short '+d1(SOY()[1]-toteGal())+' gal.'];}}];
'''
