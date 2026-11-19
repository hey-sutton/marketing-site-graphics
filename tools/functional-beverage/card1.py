"""Functional beverage card 1: Dosing & Label Claims. Layout: a record form with a side summary panel.
Left: the read only serving field, the formula list and the open formula's lines with dose per can, lot potency and
active per can, plus potency chips for the extract lot. Right: the label claim summary (claim, active, difference,
status) and the flag. Active per can = dose x potency, computed from the data below."""
from frame_auto import header

SUMMARY = 'Dosing & Label Claims (open Calm Adaptogen Tonic, 1,200 mg extract at 5.0% is 60 mg against a 60 mg claim, try the 4.5% chip for 54 mg, flag the formula)'
ARIA = 'Interactive product screen: open a functional beverage formula, see active per can from dose and lot potency, compare it with the label claim, try a lower potency and flag the formula when it no longer meets its claim'
STEPS = 5
STUDIO = dict(lede='A typical label claim screen on your Sutton data. Want it different? Describe the change.',
              examples=['Claims per serving and per bottle', 'An overage target per active', 'A claim check on every new lot', 'A label proof per formula version'],
              built_on='BOMs, lots and certificates', change='Claims, columns and views')

ICON = '<path d="M6 2h4v3l2.5 8a1.2 1.2 0 0 1-1.2 1.5H4.7A1.2 1.2 0 0 1 3.5 13L6 5z"/><path d="M4.6 10h6.8"/>'

CSS = (
 '.fld input[readonly]{background:#F4F4F5;color:#3F3F46;cursor:default;pointer-events:none}'
 '.g1{display:grid;grid-template-columns:420px 226px;grid-template-rows:62px 468px;gap:10px;padding:10px 44px 0 16px}'
 '.bf{display:flex;flex-direction:column;justify-content:center;gap:5px;padding:0 12px}.bf .frm{display:flex;align-items:flex-end;gap:8px}.bf .fld{width:150px}.bf .ctx{font-size:8.9px;color:#71717A}.bf .frm .rt{margin-left:auto}'
 '.fm{display:flex;flex-direction:column}.sm{grid-column:2;grid-row:1/3;display:flex;flex-direction:column}.sm>.empt{margin:10px;flex:1}'
 '.fl .row{grid-template-columns:62px 1fr auto;min-height:32px;font-size:9.6px}.fl .row small{color:#71717A;font-size:8.6px}'
 '.ln{border-top:1px solid #E4E4E7}.ln .sub{display:flex;align-items:center;justify-content:space-between;padding:6px 11px;font-size:9.4px;font-weight:600}.ln .sub .bt{font-size:9px;padding:3px 8px}'
 '.ln .row{grid-template-columns:1fr 60px 62px 52px 56px;font-size:9.3px;min-height:28px}.ln .row>span:nth-child(n+2){text-align:right;font-family:"JetBrains Mono",ui-monospace,monospace}.ln .row.h>span{font-family:inherit!important}'
 '.ln .row .nm small{display:block;font-size:8.2px;color:#71717A;font-family:inherit}.ln .row.act{background:#FEF9E7}'
 '.pc{display:flex;align-items:center;gap:6px;padding:8px 11px;border-top:1px solid #F0F0F1;font-size:9.2px}.pc .lb{color:#52525B;margin-right:auto}'
 '.pk{font:inherit;font-family:"JetBrains Mono",ui-monospace,monospace;font-size:9.2px;padding:3px 8px;border:1px solid #E4E4E7;border-radius:999px;background:#fff;cursor:pointer}.pk.on{background:#18181B;border-color:#18181B;color:#fff}.pk:focus-visible{outline:2px solid #18181B;outline-offset:2px}'
 '.tot{margin-top:auto;padding:9px 11px;border-top:1px solid #E4E4E7;font-size:9.1px;color:#52525B;line-height:1.4;background:#FAFAFA}.sm .tot{padding-right:90px}'
 '.sm .bx{padding:10px 11px 0}.sm .big{font-size:24px}.pair{display:grid;grid-template-columns:1fr 1fr;gap:8px;padding:9px 11px 0}.pair .kv b{font-size:12px;font-family:"JetBrains Mono",ui-monospace,monospace}'
 '.note{margin:10px 11px 0;padding:7px 9px;border-radius:7px;font-size:9px;line-height:1.45;background:#FAFAFA;border:1px solid #F0F0F1;color:#52525B}.note.w{background:#FEF2F2;border-color:#FECACA;color:#991B1B}.note.g{background:#F0FDF4;border-color:#BBF7D0;color:#166534}'
 '.sm .acts{padding:10px 11px 0}.sm .acts .bt{width:100%;font-size:9.6px;padding:5px 10px}'
 '.calc{margin:10px 11px 0;padding:6px 8px;border-radius:6px;background:#FAFAFA;border:1px solid #F0F0F1;font-family:"JetBrains Mono",ui-monospace,monospace;font-size:9.2px;text-align:center}'
)

WIN = (
 header(ICON, 'Label claims', 'Active per serving from the formula and the lot potency')
 + '<div class="g1"><div class="cd bf"><div class="frm"><label class="fld"><small>Serving</small>'
 '<input id="isv" value="12 oz can" readonly tabindex="-1" autocomplete="off" spellcheck="false"></label>'
 '<span class="rt" id="rst"></span></div><div class="ctx">One can is one serving on every label in this line</div></div>'
 '<div class="cd fm" id="fm"></div><div class="cd sm" id="sm"></div></div>'
)

JS = r'''
var FOC='.hd>*,.bf .fld,.bf .ctx,.fm .ct,.fl .row,.ln .sub,.ln .row,.pc,.fm .tot,.sm>*';
var FORMS=[['CAT-12','Calm Adaptogen Tonic','12 oz can, v7'],['FCS-12','Focus Citrus Sparkling','12 oz can, v3'],['RRB-16','Recovery Ginger Brew','16 oz can, v5']];
var DOSE=1200,LOT='ASH-2291',CLAIM=60,P0=5.0,CHIPS=[5.0,4.5,4.0];
var LN=[['Ashwagandha root extract',LOT,'1,200 mg'],['L-theanine','LT-0877','200 mg'],['Lemon balm extract','LB-1140','150 mg'],['Natural citrus flavor','NF-3302','0.8%'],['Cane sugar','CS-5521','24 g']];
var S;
function act(){return Math.round(DOSE*S.pot/100*10)/10;}
function d1(x){return x.toFixed(1);}
function short(){return Math.max(0,CLAIM-act());}
function meets(){return act()>=CLAIM;}
function render(){
$('rst').innerHTML=S.flag?'<span class="ch c-bad" id="fst">Flagged, below claim</span>':S.cmp?'<span class="ch '+(meets()?'c-ok':'c-warn')+'">'+(meets()?'Meets claim':'Below claim')+'</span>':'';
var f='<div class="ct"><span>Formulas</span>'+(S.op?'<span class="ch c-idle">'+LN.length+' lines</span>':'')+'</div>';
f+='<div class="fl">'+FORMS.map(function(x,i){var me=i===0;return '<button type="button" class="row'+(S.op&&me?' sel':'')+'" id="f-'+x[0]+'"><span class="mono"><b>'+x[0]+'</b></span><span>'+x[1]+' <small>'+x[2]+'</small></span><span class="ch '+(me&&S.flag?'c-bad':'c-ok')+'">'+(me&&S.flag?'Flagged':'In production')+'</span></button>';}).join('')+'</div>';
if(!S.op)f+='<div class="empt" style="margin:10px;flex:1"><b>No formula open</b><span>Open a formula to see its actives, the lots behind them and the label claim.</span></div>';
else{f+='<div class="ln in"><div class="sub"><span>Calm Adaptogen Tonic, per can</span>'+(S.calc?'<span class="ch c-info">Calculated</span>':'<button type="button" class="bt pri" id="clb">Calculate active</button>')+'</div>'+
'<div class="row h"><span>Ingredient</span><span>Lot</span><span>Per can</span><span>Potency</span><span>Active</span></div>'+
LN.map(function(l,i){var a=i===0;return '<div class="row'+(a&&S.calc?' act':'')+'"><span class="nm">'+l[0]+(a?'<small>Withanolides</small>':'')+'</span><span>'+l[1]+'</span><span>'+l[2]+'</span><span'+(a?' id="lpot"':'')+'>'+(a&&S.calc?d1(S.pot)+'%':'')+'</span><span'+(a?' id="lact"':'')+'>'+(a&&S.calc?d1(act())+' mg':'')+'</span></div>';}).join('')+'</div>';
if(S.cmp)f+='<div class="pc in"><span class="lb">Potency of '+LOT+'</span>'+CHIPS.map(function(c){return '<button type="button" class="pk'+(S.pot===c?' on':'')+'" data-p="'+c+'" id="p-'+String(c).replace('.','')+'" aria-pressed="'+(S.pot===c?'true':'false')+'">'+d1(c)+'%</button>';}).join('')+'</div>';}
f+='<div class="tot">Active per can is the dose times the potency on the lot certificate.</div>';
$('fm').innerHTML=f;
var m='<div class="ct"><span>Label claim</span>'+(S.op?'<span class="ch c-idle">Withanolides</span>':'')+'</div>';
if(!S.op)m+='<div class="empt"><b>No claim to check</b><span>The label claim and the active per can show here.</span></div>';
else{m+='<div class="bx in"><div class="kv"><small>Claim on the label, per can</small><b class="big mono" id="clm">'+CLAIM+' mg</b></div></div>';
if(S.calc)m+='<div class="pair in"><div class="kv"><small>Active per can</small><b id="sact">'+d1(act())+' mg</b></div><div class="kv"><small>Lot potency</small><b id="spot">'+d1(S.pot)+'%</b></div></div><div class="calc" id="scal">'+n0(DOSE)+' mg x '+d1(S.pot)+'% = '+d1(act())+' mg</div>';
if(S.calc&&!S.cmp)m+='<div class="acts"><button type="button" class="bt pri" id="cpb">Compare with claim</button></div>';
if(S.cmp)m+='<div class="pair in"><div class="kv"><small>Difference</small><b id="sdif">'+(meets()?'0.0 mg':'−'+d1(short())+' mg')+'</b></div><div class="kv"><small>Status</small><b id="sst">'+(meets()?'Meets':'Below')+'</b></div></div>'+
(S.pot!==P0?'<div class="note w in">Preview at '+d1(S.pot)+'% potency, not approved. '+d1(act())+' mg is '+d1(short())+' mg short of the claim.</div>':'<div class="note g in">'+d1(act())+' mg meets the '+CLAIM+' mg claim on the label.</div>');
if(S.cmp&&!meets()&&!S.flag)m+='<div class="acts"><button type="button" class="bt pri" id="flb">Flag formula</button></div>';
if(S.flag)m+='<div class="note w in" id="fnt">Calm Adaptogen Tonic flagged: no longer meets its '+CLAIM+' mg claim. Production stays on hold until it is reviewed.</div>';}
m+='<div class="tot">Claims checked on every lot.</div>';
$('sm').innerHTML=m;
}
function resetState(){S={op:false,calc:false,cmp:false,pot:P0,flag:false};render();}
winEl.addEventListener('click',function(e){var c=e.target.closest&&e.target.closest('[data-p]');if(c&&S.cmp&&!S.flag&&mode==='try'){S.pot=+c.getAttribute('data-p');render();}});
var CAPAT=function(hh){return {l:14,t:visH()-hh-14};};
var ST=[
{id:'op',target:function(){return $('f-CAT-12');},prompt:'Open Calm Adaptogen Tonic',where:'below',run:function(){S.op=true;render();},
 after:function(){return['A formula with its actives','Ashwagandha extract '+n0(DOSE)+' mg per can from lot '+LOT+', plus L-theanine and lemon balm.'];}},
{id:'calc',target:function(){return $('clb');},prompt:'Calculate active per can',where:'below',run:function(){S.calc=true;render();},
 after:function(){return['Active per serving from dose and potency',n0(DOSE)+' mg at '+d1(S.pot)+'% withanolides is '+d1(act())+' mg per can.'];}},
{id:'cmp',target:function(){return $('cpb');},prompt:'Compare with the label claim',where:'below',run:function(){S.cmp=true;render();},
 after:function(){return['Checked against the label claim',d1(act())+' mg against a '+CLAIM+' mg claim: meets.'];}},
{id:'pot',target:function(){return $('p-45');},prompt:'Try 4.5% potency',where:'above',run:function(){S.pot=4.5;render();},
 after:function(){return['A new lot potency, previewed before approval',n0(DOSE)+' mg at 4.5% is '+d1(act())+' mg, '+d1(short())+' mg short of the claim.'];}},
{id:'flag',target:function(){return $('flb');},prompt:'Flag the formula',where:'below',run:function(){S.flag=true;render();},
 after:function(){return['Flagged before it reaches a batch','Calm Adaptogen Tonic no longer meets its '+CLAIM+' mg claim at 4.5% potency.'];}}];
'''
