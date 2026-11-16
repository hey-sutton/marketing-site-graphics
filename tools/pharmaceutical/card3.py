"""Pharmaceutical card 3: Formulas & Unit Conversion. Layout: a formula workbench. Top, the formula picker and the batch
size input with a unit converter. Left, the ingredient ledger (milligrams per capsule beside kilograms per batch, then
packaging per batch, then the assay adjustment). Right, a v3 and v4 comparison with a cost strip underneath.
Everything is computed from milligrams per capsule, the batch size and the certificate assay, so any batch size the
reader types scales correctly. Costs are rounded per line, then summed."""
from frame_auto import header

SUMMARY = 'Formulas & Unit Conversion (select CP-050, scale to 200,000 capsules, convert mg per capsule to kg per batch, adjust the active for a 98.0% assay, compare v3 and v4, roll the cost up to the bottle)'
ARIA = 'Interactive product screen: open formula CP-050, scale it to a batch size, convert milligrams per capsule into kilograms per batch, adjust the active for the certificate assay, compare versions 3 and 4, and roll up the cost per bottle'
STEPS = 5
STUDIO = dict(lede='A typical formula workbench, built on your Sutton data with Studio. Want it different? Describe the change.',
              examples=['An overage per ingredient', 'A potency field on every lot', 'A cost alert per bottle', 'A side by side of three versions'],
              built_on='Items, BOMs, lots and costs', change='Units, fields and rules')

ICON = '<path d="M6 2h4M6.8 2v4.2L3 12.6A1 1 0 0 0 3.9 14h8.2a1 1 0 0 0 .9-1.4L9.2 6.2V2"/><path d="M4.6 10h6.8"/>'

CSS = (
 '.fld input[readonly]{background:#FAFAFA;cursor:default;pointer-events:none}'
 '.g3{display:grid;grid-template-columns:392px 1fr;grid-template-rows:118px 412px;gap:10px;padding:10px 40px 0 16px}'
 '.top{grid-column:1/3;display:grid;grid-template-columns:186px 1fr;gap:10px}'
 '.fl{display:flex;flex-direction:column}.fl button.row{grid-template-columns:1fr auto;min-height:44px;font-size:9.8px}.fl .row b{display:block;font-size:10.4px}.fl .row small{color:#71717A;font-size:8.6px}.fl .ft2{margin-top:auto;padding:0 11px 8px;font-size:8.8px;color:#A1A1AA}'
 '.sc{display:grid;grid-template-columns:214px 1fr;min-width:0}.sc .lf2{display:flex;flex-direction:column;border-right:1px solid #E4E4E7}.sc .frm{display:flex;align-items:flex-end;gap:6px;padding:8px 10px 0}.sc .fld{flex:1}'
 '.sc .smp{display:flex;align-items:center;gap:6px;padding:6px 10px 0;font-size:8.8px;color:#71717A}.sc .smp .bt{font-family:"JetBrains Mono",ui-monospace,monospace;font-size:9px;padding:3px 7px}'
 '.cv2{display:flex;flex-direction:column;min-width:0}.cv2 .eq{padding:7px 11px 0;font-family:"JetBrains Mono",ui-monospace,monospace;font-size:10px;line-height:1.75;white-space:nowrap}.cv2 .eq b{font-weight:600}.cv2 .eq .mut{font-family:Inter,system-ui,sans-serif;font-size:8.8px}'
 '.sc .empt,.ldg .empt,.cmp .empt,.cst .empt{margin:8px 10px;flex:1;padding:8px}.ldg .empt{margin-bottom:10px}'
 '.ldg{display:flex;flex-direction:column}.ldg .row{grid-template-columns:1fr 62px 70px 54px;font-size:9.6px;min-height:28px}.ldg .row span:nth-child(n+2){text-align:right;font-family:"JetBrains Mono",ui-monospace,monospace}'
 '.ldg .row .nm small{display:block;color:#71717A;font-size:8.4px;font-family:Inter,system-ui,sans-serif}.ldg .row.t{font-weight:600;background:#FAFAFA}.ldg .sh2{padding:7px 11px 4px;font-size:9px;color:#71717A;font-weight:500;border-top:1px solid #E4E4E7}'
 '.lft2{padding:9px 11px;border-top:1px solid #E4E4E7;font-size:9.2px;color:#52525B;background:#FAFAFA}.ldg .empt+.lft2{margin-top:0}.ldg .up{color:#166534}.ldg .dn{color:#B45309}.ldg .row.chg{background:#FEF9E7}'
 '.asy{margin:auto 10px 10px;border:1px solid #E4E4E7;border-radius:7px;padding:8px 10px;display:flex;align-items:center;gap:10px;background:#FAFAFA}.asy .kv b{font-size:10.4px}.asy .bt{margin-left:auto}'
 '.rc{display:flex;flex-direction:column;gap:10px;min-width:0}.cmp{height:186px;flex:none;display:flex;flex-direction:column}.cst{flex:1;display:flex;flex-direction:column}'
 '.cmp .ct .bt,.cst .ct .bt{font-size:9.4px;padding:3px 8px}'
 '.cmp .row{grid-template-columns:1fr 56px 56px;font-size:9.4px;min-height:25px}.cmp .row span:nth-child(n+2){text-align:right;font-family:"JetBrains Mono",ui-monospace,monospace}.cmp .row.chg{background:#FEF9E7}.cmp .row.chg span:last-child{font-weight:600}'
 '.cmp .nt2{padding:6px 11px 0;font-size:8.8px;color:#71717A;line-height:1.35}'
 '.cl{display:grid;grid-template-columns:1fr 1fr;column-gap:12px;padding:6px 11px 0}.cl div{display:flex;justify-content:space-between;font-size:9.2px;min-height:19px;align-items:center;border-bottom:1px solid #F4F4F5}.cl div span:last-child{font-family:"JetBrains Mono",ui-monospace,monospace}'
 '.tbx{margin:8px 11px 0;padding:7px 10px;border-radius:7px;background:#F4F4F5;display:grid;grid-template-columns:auto 1fr;align-items:end;gap:2px 10px}.tbx b{font-size:18px;font-weight:600;letter-spacing:-.02em;grid-row:span 2}.tbx span{font-size:9.2px;text-align:right}.tbx .d{color:#B45309}'
 '.cst .nt2{padding:5px 11px 0;font-size:8.6px;color:#A1A1AA}'
)

WIN = (
 header(ICON, 'Formulas', 'Formula workbench, capsules')
 + '<div class="g3"><div class="top"><div class="cd fl" id="fl"></div><div class="cd sc" id="sc"></div></div>'
 '<div class="cd ldg" id="ldg"></div><div class="rc"><div class="cd cmp" id="cmp"></div><div class="cd cst" id="cst"></div></div></div>'
)

JS = r'''
var FOC='.hd>*,.fl,.sc .ct,.sc .frm>*,.sc .smp,.cv2,.ldg .ct,.ldg .row,.ldg .sh2,.asy,.cmp,.cst';
var ING=[['act','Active ingredient','Active, label claim',50,480],['mgs','Magnesium stearate','Lubricant',4,9],['mcc','Microcrystalline cellulose','Filler, the balance',0,6.5]];
var PKG=[['Capsule shells','1 per capsule',1,0.012],['Bottles','1 per 100 capsules',0.01,0.18],['Caps','1 per bottle',0.01,0.04],['Labels','1 per bottle',0.01,0.03]];
var FILL=400,ASSAY=0.98,V3MGS=2;
var S;
function k3(x){return x.toLocaleString('en-US',{minimumFractionDigits:3,maximumFractionDigits:3});}
function m2(x){return x.toLocaleString('en-US',{minimumFractionDigits:2,maximumFractionDigits:2});}
function r2(x){return Math.round(x*100+1e-9)/100;}
function kg(mg){return mg*S.n/1e6;}
function qty(mgs){var a=kg(50)/(S.asy?ASSAY:1),m=kg(mgs);return {act:a,mgs:m,mcc:kg(FILL)-a-m};}
function mgcap(q,k){return q[k]*1e6/S.n;}
function costs(mgs){var q=qty(mgs),L=ING.map(function(i){return [i[1],r2(q[i[0]]*i[4])];});PKG.forEach(function(p){L.push([p[0],r2(S.n*p[2]*p[3])]);});return L;}
function total(L){return r2(L.reduce(function(a,l){return a+l[1];},0));}
function bottles(){return S.n/100;}
function render(){
var f='<div class="ct"><span>Select a formula</span>'+(S.sel?'<span class="ch c-ok">Approved</span>':'')+'</div><button type="button" class="row'+(S.sel?' sel':'')+'" id="f-cp"><span><b class="mono">CP-050</b><small>Capsule 50 mg, bottles of 100</small></span><span class="ch '+(S.sel?'c-info':'c-idle')+'">v4</span></button><div class="ft2">'+(S.sel?'v4 current, v3 kept for comparison':'One formula on file for capsules')+'</div>';
$('fl').innerHTML=f;
var c='';if(!S.sel)c='<div class="empt" style="grid-column:1/3"><b>No formula open</b><span>Select a formula to scale it to a batch and convert its units.</span></div>';
else{c='<div class="lf2"><div class="ct">Batch size</div><div class="frm"><label class="fld" id="fbs"><small>Capsules per batch</small><input id="ibs" value="'+n0(S.n)+'" readonly tabindex="-1"></label><button type="button" class="bt pri" id="scb">Scale</button></div>'+
'<div class="smp">Standard batch for CP-050 v4</div></div><div class="cv2"><div class="ct">Unit converter</div>';
if(!S.sc)c+='<div class="empt"><b>Nothing converted yet</b><span>Scale to a batch to convert mg per capsule into kg per batch.</span></div>';
else{var q=qty(4);c+='<div class="eq in" id="eq1"><span id="eqa"><b>50 mg</b> × '+n0(S.n)+' = <b>'+k3(kg(50))+' kg</b></span><br>'+(S.asy?'<span class="in" id="eq2">'+k3(kg(50))+' kg ÷ '+(ASSAY*100).toFixed(1)+'% = <b>'+k3(q.act)+' kg</b></span>':'<span>'+FILL+' mg × '+n0(S.n)+' = '+k3(kg(FILL))+' kg</span>')+'<br><span class="mut">1,000,000 mg make 1 kg</span></div>';}
c+='</div>';}
$('sc').innerHTML=c;
var l='<div class="ct"><span>Ingredient ledger'+(S.sel?', CP-050 v4':'')+'</span>'+(S.asy?'<span class="ch c-info">Assay adjusted</span>':'')+'</div>';
if(!S.sel)l+='<div class="empt"><b>Ledger is empty</b><span>Ingredients, milligrams per capsule and kilograms per batch show once a formula is open.</span></div><div class="lft2">Quantities scale from milligrams per capsule. Kilograms show three decimals.</div>';
else{var q=qty(4),q0=(function(){var a=S.asy;S.asy=false;var r=qty(4);S.asy=a;return r;})();
l+='<div class="row h"><span>Ingredient</span><span>mg/capsule</span><span>kg/batch</span><span>Change</span></div>'+ING.map(function(i){var k=i[0],d=q[k]-q0[k],ch=S.asy&&Math.abs(d)>1e-9;
return '<div class="row in'+(ch?' chg':'')+'"><span class="nm">'+i[1]+'<small>'+i[2]+'</small></span><span id="mg-'+k+'">'+m2(mgcap(q,k))+'</span><span id="kg-'+k+'">'+(S.sc?k3(q[k]):'')+'</span><span id="dl-'+k+'" class="'+(d>0?'up':'dn')+'">'+(ch?(d>0?'+':'')+k3(d):'')+'</span></div>';}).join('')+
'<div class="row t"><span>Fill weight</span><span>'+m2(FILL)+'</span><span id="kg-fill">'+(S.sc?k3(q.act+q.mgs+q.mcc):'')+'</span><span></span></div><div class="sh2">Packaging per batch</div>'+
PKG.map(function(p){return '<div class="row"><span class="nm">'+p[0]+'<small>'+p[1]+'</small></span><span></span><span id="pk-'+p[0].slice(0,3)+'">'+(S.sc?n0(S.n*p[2]):'')+'</span><span></span></div>';}).join('')+
'<div class="asy"><div class="kv"><small>Certificate, lot AP-8842</small><b>Assay '+(ASSAY*100).toFixed(1)+'%</b></div><div class="kv"><small>Adjusts</small><b>Active up, cellulose down</b></div>'+(S.asy?'<button type="button" class="bt done" disabled>Assay applied</button>':'<button type="button" class="bt" id="asb">Apply assay</button>')+'</div>';}
$('ldg').innerHTML=l;
var m='<div class="ct"><span>Compare versions</span>'+(S.asy&&!S.cmp?'<button type="button" class="bt" id="cmb">Compare with v3</button>':S.cmp?'<span class="ch c-idle">v3 and v4</span>':'')+'</div>';
if(!S.cmp)m+='<div class="empt"><b>No comparison open</b><span>Compare v4 with an earlier version, line by line.</span></div>';
else{var a=qty(V3MGS),b=qty(4);m+='<div class="row h"><span>Line</span><span>v3</span><span>v4</span></div>'+
'<div class="row chg in"><span>Lubricant, mg / capsule</span><span>'+m2(V3MGS)+'</span><span>'+m2(4)+'</span></div><div class="row chg in"><span>Magnesium stearate, kg</span><span id="c3m">'+k3(a.mgs)+'</span><span id="c4m">'+k3(b.mgs)+'</span></div>'+
'<div class="row chg in"><span>Cellulose, kg</span><span id="c3c">'+k3(a.mcc)+'</span><span id="c4c">'+k3(b.mcc)+'</span></div><div class="row in"><span>Active, kg</span><span>'+k3(a.act)+'</span><span>'+k3(b.act)+'</span></div>'+
'<div class="nt2">v4 doubles the lubricant. Cellulose fills the balance, so the fill stays at '+k3(kg(FILL))+' kg.</div>';}
$('cmp').innerHTML=m;
var t='<div class="ct"><span>Cost per batch, v4</span>'+(S.cmp&&!S.cost?'<button type="button" class="bt" id="cub">Roll up cost</button>':'')+'</div>';
if(!S.cost)t+='<div class="empt"><b>No cost yet</b><span>Roll ingredient and packaging costs up to the bottle.</span></div>';
else{var L=costs(4),T=total(L),T3=total(costs(V3MGS)),pb=r2(T/bottles());
t+='<div class="cl in">'+L.map(function(x){return '<div><span>'+x[0].replace('Microcrystalline cellulose','Cellulose').replace('Magnesium stearate','Mg stearate').replace('Active ingredient','Active').replace('Capsule shells','Shells')+'</span><span>'+m2(x[1])+'</span></div>';}).join('')+'</div>'+
'<div class="tbx in"><b id="ctot">$'+m2(T)+'</b><span id="cpb">$'+m2(pb)+' per bottle</span><span class="d" id="cdf">'+(T-T3>=0?'+':'')+'$'+m2(r2(T-T3))+' against v3</span></div><div class="nt2">Costed on exact quantities</div>';}
$('cst').innerHTML=t;
}
function resetState(){S={sel:false,sc:false,asy:false,cmp:false,cost:false,n:200000};render();}
function capN(){var i=cap.querySelector('.m i');return i?+i.textContent:1;}
var CAPAT=function(hh){var w=cap.offsetWidth,k=capN();return k===2?{l:visW()-w-14,t:196}:k<=3?{l:visW()-w-14,t:visH()-hh-58}:{l:14,t:visH()-hh-14};};
var ST=[
{id:'sel',target:function(){return $('f-cp');},prompt:'Select formula CP-050',where:'below',run:function(){S.sel=true;render();},
 after:function(){return['Formula v4 opens in milligrams per capsule','Active 50 mg, lubricant 4 mg, cellulose the balance, '+FILL+' mg fill.'];}},
{id:'sc',target:function(){return $('scb');},prompt:'Click Scale for 200,000 capsules',where:'below',
 run:function(){S.sc=true;render();},
 after:function(){var q=qty(4);return['Milligrams per capsule become kilograms per batch','50 mg × '+n0(S.n)+' = '+k3(kg(50))+' kg active, '+k3(q.mgs)+' kg lubricant, '+k3(q.mcc)+' kg cellulose.'];}},
{id:'asy',target:function(){return $('asb');},prompt:'Apply the 98.0% assay from the certificate',where:'above',run:function(){S.asy=true;render();},
 after:function(){var q=qty(4);return['The active is adjusted for the assay',k3(kg(50))+' ÷ 0.98 = '+k3(q.act)+' kg active. Cellulose drops to '+k3(q.mcc)+' kg.'];}},
{id:'cmp',target:function(){return $('cmb');},prompt:'Compare v4 with v3',where:'below',run:function(){S.cmp=true;render();},
 after:function(){var a=qty(V3MGS),b=qty(4);return['Two versions, line by line','Lubricant 2 mg to 4 mg, '+k3(a.mgs)+' to '+k3(b.mgs)+' kg. Cellulose '+k3(a.mcc)+' to '+k3(b.mcc)+' kg.'];}},
{id:'cost',target:function(){return $('cub');},prompt:'Roll the cost up to the bottle',where:'above',run:function(){S.cost=true;render();},
 after:function(){var T=total(costs(4)),T3=total(costs(V3MGS));return['Cost rolls up to the bottle','$'+m2(T)+' a batch, $'+m2(r2(T/bottles()))+' a bottle, '+(T-T3>=0?'+':'')+'$'+m2(r2(T-T3))+' against v3.'];}}];
'''
