"""Frozen food card 3: Multi-Level BOM & Cost Roll-Up. Layout: a BOM tree on the left with allergen chips carried up from
the ingredients, a cost table on the right, and price, batch size and output controls under it.
Quantities are kept in tenths of a pound and prices in cents, so every cost is an exact integer of cents."""
from frame_auto import header

SUMMARY = 'Multi-Level BOM & Cost Roll-Up (select FE-2210, open its sub-assemblies and the milk allergen, raise the chicken price, scale to a 400 lb run and compare expected and actual yield)'
ARIA = 'Interactive product screen: open the BOM for chicken broccoli entree FE-2210, see sub-assemblies SB-110 and SB-210 with the milk allergen, raise chicken from $2.10 to $2.40 a lb, scale to a 400 lb run and record 378 lb of actual output'
STEPS = 5
STUDIO = dict(lede='A typical BOM costing screen, built on your Sutton data with Studio. Want it different? Describe the change.',
              examples=['A nutrition panel rolled up from ingredients', 'A what if view for three price changes', 'An allergen matrix for every product', 'A yield report by line and shift'],
              built_on='Items, BOMs, costs and production output', change='Levels, fields and rules')

ICON = '<rect x="5.5" y="1.8" width="5" height="3" rx=".8"/><rect x="1.8" y="11.2" width="4" height="3" rx=".8"/><rect x="10.2" y="11.2" width="4" height="3" rx=".8"/><path d="M8 4.8v3M3.8 11.2V7.8h8.4v3.4"/>'

CSS = (
 '.g3{display:grid;grid-template-columns:232px 1fr;gap:10px;padding:10px 40px 0 16px}'
 '.col{display:flex;flex-direction:column;gap:10px;min-width:0}'
 '.bl .row{grid-template-columns:1fr auto;min-height:32px;padding:3px 10px;font-size:9.4px}.bl .row .t{display:flex;flex-direction:column;gap:1px;line-height:1.25;min-width:0}.bl .row .t span{color:#71717A;font-size:8.8px;white-space:nowrap}'
 '.tre{height:372px;flex:none;display:flex;flex-direction:column}.tre .ct .bt{font-size:9px;padding:3px 8px}'
 '.tn{display:flex;align-items:center;gap:6px;min-height:28px;padding:0 10px;border-top:1px solid #F4F4F5;font-size:9.4px;white-space:nowrap}.tn:first-of-type{border-top:0}.tn .ln{width:9px;height:10px;border-left:1px solid #D4D4D8;border-bottom:1px solid #D4D4D8;margin-top:-8px;flex:none}'
 '.tn .q{margin-left:auto;font-family:"JetBrains Mono",ui-monospace,monospace;color:#52525B;font-size:9px}.tn .ty{font-size:8.2px;color:#71717A;background:#F4F4F5;border-radius:4px;padding:1px 5px}.tn.sa{font-weight:600}'
 '.tft{margin-top:auto;padding:8px 10px 10px;border-top:1px solid #F0F0F1;font-size:8.8px;color:#71717A}'
 '.alg{display:inline-flex;align-items:center;gap:3px;padding:1px 5px;border-radius:999px;background:#FEF3C7;color:#92400E;font-size:8px;font-weight:600}'
 '.cst{height:276px;flex:none;display:flex;flex-direction:column}.cst .ct .ch{margin-left:auto}.cst .row{grid-template-columns:1fr 46px 50px 58px;min-height:22px;font-size:9.2px;white-space:nowrap;padding:0 11px}'
 '.cst .row span:nth-child(n+2){text-align:right;font-family:"JetBrains Mono",ui-monospace,monospace}.cst .row.h span{font-family:inherit}.cst .row.sa{font-weight:600}.cst .row.ig span:first-child{padding-left:14px;color:#52525B}.cst .row.t{font-weight:600;background:#FAFAFA;min-height:26px}.cst .row.up{background:#FFFBEB}'
 '.pbx{flex:none;height:260px;display:flex;flex-direction:column}.pbx .frm{display:flex;align-items:flex-end;gap:8px;padding:7px 11px 0}.pbx .fld{width:110px}.pbx .nt{font-size:8.8px;color:#71717A;padding-bottom:6px;white-space:nowrap}'
 '.yl{margin:9px 11px 0;display:grid;grid-template-columns:repeat(3,1fr);gap:8px;padding:8px 10px;border:1px solid #F0F0F1;border-radius:7px;background:#FAFAFA}.yl .kv b{font-size:13px}.yl .kv em{font-style:normal;font-size:8.6px;color:#71717A}'
 '.tre .empt,.cst .empt{margin:10px;flex:1}'
)

WIN = (
 header(ICON, 'BOMs and costing', 'Frozen entrees, per 100 lb batch')
 + '<div class="g3"><div class="col"><div class="cd bl" id="bl"></div><div class="cd tre" id="tre"></div></div>'
 '<div class="col"><div class="cd cst" id="cst"></div><div class="cd pbx" id="pbx"></div></div></div>'
)

JS = r'''
var FOC='.hd>*,.bl .ct,.bl .row,.tre .ct>*,.tn,.cst .ct>*,.cst .row,.pbx .ct,.pbx .frm>*,.yl';
var LIST=[['FE-2210','Chicken broccoli entree'],['FE-2230','Beef and pepper bowl'],['FE-2245','Cheese ravioli bake'],['FE-2260','Turkey pot pie']];
/* [id, name, tenths of lb per 100 lb batch, cents per lb, allergen] ; sub-assemblies hold their ingredients */
var SUB=[{id:'SB-110',name:'Seasoned chicken',q:400,ing:[['CK-01','Chicken',380,210,''],['SP-04','Seasoning',20,300,'']]},
{id:'IQF-30',name:'IQF broccoli',q:300,price:85},
{id:'SB-210',name:'Cream sauce',q:300,ing:[['DY-11','Cream',180,160,'Milk'],['DY-12','Butter',45,400,'Milk'],['DY-14','Parmesan',30,500,'Milk'],['ST-02','Stabilizer',45,100,'']]}];
var YLD=96,S;
function lineC(q,p){return q*p*S.k/10;}
function subC(s){return s.ing?s.ing.reduce(function(a,g){return a+lineC(g[2],price(g));},0):lineC(s.q,s.price);}
function price(g){return g[0]==='CK-01'?S.ck:g[3];}
function total(){return SUB.reduce(function(a,s){return a+subC(s);},0);}
function perLb(s){return subC(s)*10/(s.q*S.k);}
function usd(c){return '$'+(Math.round(c)/100).toLocaleString('en-US',{minimumFractionDigits:2,maximumFractionDigits:2});}
function usd3(c){var v=c/100,s=v.toFixed(3);return '$'+(s.slice(-1)==='0'?v.toFixed(2):s);}
function lb(t){return (t/10).toLocaleString('en-US',{maximumFractionDigits:1});}
function alg(s){return s.ing&&s.ing.some(function(g){return g[4];})?'<span class="alg">Milk</span>':'';}
function batchLb(){return 100*S.k;}
function expOut(){return batchLb()*YLD/100;}
function render(){
$('bl').innerHTML='<div class="ct">Select a BOM<span class="mut" style="font-weight:500">'+LIST.length+'</span></div>'+LIST.map(function(x,i){return '<button type="button" class="row'+(S.sel&&i===0?' sel':'')+'" id="b-'+x[0]+'"><span class="t"><b class="mono">'+x[0]+'</b><span>'+x[1]+'</span></span><span class="ch c-idle">BOM</span></button>';}).join('');
var t='<div class="ct"><span>BOM tree</span>'+(S.sel&&!S.exp?'<button type="button" class="bt" id="exp">Expand all</button>':S.exp?'<span class="alg" id="talg">Contains milk</span>':'')+'</div>';
if(!S.sel)t+='<div class="empt"><b>No BOM selected</b><span>Pick a product to see its sub-assemblies, ingredients and allergens.</span></div>';
else{t+='<div class="tn sa in"><span class="mono">FE-2210</span><span>Entree, '+lb(batchLb()*10)+' lb</span>'+(S.exp?'<span class="alg">Milk</span>':'')+'</div>';
SUB.forEach(function(s,i){t+='<div class="tn'+(s.ing?' sa':'')+' in" style="padding-left:20px;animation-delay:'+(i*80)+'ms"><span class="ln"></span><span class="mono">'+s.id+'</span><span>'+s.name+'</span>'+(S.exp?alg(s):'')+'<span class="q">'+lb(s.q*S.k)+' lb</span></div>';
if(S.exp&&s.ing)s.ing.forEach(function(g,j){t+='<div class="tn in" style="padding-left:36px;animation-delay:'+(i*80+j*50+120)+'ms"><span class="ln"></span><span class="mono">'+g[0]+'</span><span>'+g[1]+'</span>'+(g[4]?'<span class="alg">'+g[4]+'</span>':'')+'<span class="q">'+lb(g[2]*S.k)+' lb</span></div>';});});}
$('tre').innerHTML=t+'<div class="tft">Costs use the last receipt price for each ingredient.</div>';
var c='<div class="ct"><span>Cost roll up'+(S.sel?', FE-2210':'')+'</span>'+(S.sel?'<span class="ch c-info" id="bsz">'+n0(batchLb())+' lb batch</span>':'')+'</div>';
if(!S.sel)c+='<div class="empt"><b>No costs yet</b><span>Costs roll up from every ingredient once a BOM is selected.</span></div>';
else{c+='<div class="row h"><span>Item</span><span>Lb</span><span>Per lb</span><span>Cost</span></div>';
SUB.forEach(function(s){c+='<div class="row'+(s.ing?' sa':'')+(s.id==='SB-110'&&S.pr?' up':'')+'"><span><span class="mono">'+s.id+'</span> '+s.name+'</span><span>'+lb(s.q*S.k)+'</span><span>'+usd3(s.ing?perLb(s):s.price)+'</span><span id="c-'+s.id+'">'+usd(subC(s))+'</span></div>';
if(S.exp&&s.ing)s.ing.forEach(function(g){c+='<div class="row ig'+(g[0]==='CK-01'&&S.pr?' up':'')+'"><span>'+g[1]+'</span><span>'+lb(g[2]*S.k)+'</span><span>'+usd(price(g))+'</span><span>'+usd(lineC(g[2],price(g)))+'</span></div>';});});
c+='<div class="row t"><span>Batch total'+(S.pr?' <span class="ch c-warn" id="dlt">+'+usd(total()/S.k-S.t0)+' a batch</span>':'')+'</span><span>'+n0(batchLb())+'</span><span></span><span id="btot">'+usd(total())+'</span></div>';}
$('cst').innerHTML=c;
var k='<div class="ct">Price, batch and yield</div>';
if(!S.sel)k+='<div class="empt" style="margin:10px;flex:1"><b>Nothing to change yet</b><span>Price, batch size and yield open with the BOM.</span></div>';
else{k+='<div class="frm"><label class="fld" id="fck"><small>Chicken, per lb</small><input id="ick" value="'+S.v.ck+'" inputmode="decimal" autocomplete="off"><span class="em">A price like 2.40</span></label>'+(S.pr?'<button type="button" class="bt done" disabled>Applied</button>':'<button type="button" class="bt" id="apr"'+(S.exp?'':' disabled')+'>Apply price</button>')+'<span class="nt">Was $2.10</span></div>';
k+='<div class="frm"><label class="fld" id="fbt"><small>Run size, lb</small><input id="ibt" value="'+S.v.bt+'" inputmode="numeric" autocomplete="off"><span class="em">A size like 400</span></label>'+(S.k>1?'<button type="button" class="bt done" disabled>Scaled</button>':'<button type="button" class="bt" id="scl"'+(S.pr?'':' disabled')+'>Scale run</button>')+'<span class="nt">Every line scales with it</span></div>';
k+='<div class="frm"><label class="fld" id="fout"><small>Actual output, lb</small><input id="iout" value="'+S.v.out+'" inputmode="numeric" autocomplete="off"><span class="em">Up to '+n0(batchLb())+' lb</span></label>'+(S.out?'<button type="button" class="bt done" disabled>Recorded</button>':'<button type="button" class="bt'+(S.k>1?' pri':'')+'" id="rec"'+(S.k>1?'':' disabled')+'>Record output</button>')+'<span class="nt">Expected '+YLD+'%, '+n0(expOut())+' lb</span></div>';
if(S.out)k+='<div class="yl in"><div class="kv"><small>Output, '+n0(expOut()-S.out)+' lb under</small><b id="yout">'+n0(S.out)+' lb</b></div><div class="kv"><small>Expected per lb</small><b id="yexp">'+usd(total()/expOut())+'</b></div><div class="kv"><small>Actual per lb</small><b id="yact">'+usd(total()/S.out)+'</b></div></div>';}
$('pbx').innerHTML=k;}
$('pbx').addEventListener('input',function(e){if(e.target.id==='ick')S.v.ck=e.target.value;if(e.target.id==='ibt')S.v.bt=e.target.value;if(e.target.id==='iout')S.v.out=e.target.value;});
function num(v){v=String(v).trim().replace(/[$,]/g,'');return /^\d+(\.\d{1,2})?$/.test(v)?parseFloat(v):null;}
function resetState(){S={sel:false,exp:false,pr:false,k:1,out:0,ck:210,t0:0,v:{ck:'2.40',bt:'400',out:'378'}};render();}
var CAPAT=function(hh){return cur>=2?{l:14,t:visH()-hh-14}:{l:visW()-cap.offsetWidth-14,t:visH()-hh-14};};
var ST=[
{id:'sel',target:function(){return $('b-FE-2210');},prompt:'Select FE-2210',where:'right',run:function(){S.sel=true;render();},
 after:function(){return['Pick a product and its BOM costs roll up','FE-2210 per 100 lb: SB-110 '+usd(subC(SUB[0]))+', broccoli '+usd(subC(SUB[1]))+', SB-210 '+usd(subC(SUB[2]))+'. '+usd(total())+' a batch.'];}},
{id:'exp',target:function(){return $('exp');},prompt:'Expand the whole tree',where:'below',run:function(){S.exp=true;render();},
 after:function(){return['Sub-assemblies open to every ingredient, and allergens carry up','Cream, butter and parmesan make SB-210 contain milk, so FE-2210 does too.'];}},
{id:'pr',target:function(){return $('apr');},prompt:'Apply the new chicken price',where:'above',ok:function(){var v=num(S.v.ck),b=v===null||v<=0||v>99;$('fck').classList.toggle('err',b);return !b;},
 run:function(){S.t0=total();S.ck=Math.round(num(S.v.ck)*100);S.pr=true;render();},
 after:function(){return['A price change rolls up through every level','Chicken at '+usd(S.ck)+' makes SB-110 '+usd3(perLb(SUB[0]))+' a lb. Batch '+usd(total())+', up '+usd(total()-S.t0)+'.'];}},
{id:'scl',target:function(){return $('scl');},prompt:'Scale to a 400 lb run',where:'above',ok:function(){var v=num(S.v.bt),b=v===null||v%100!==0||v<100||v>2000;$('fbt').classList.toggle('err',b);return !b;},
 run:function(){S.k=num(S.v.bt)/100;render();},
 after:function(){return['Scale the run and every quantity follows','Chicken '+lb(SUB[0].q*S.k)+' lb, broccoli '+lb(SUB[1].q*S.k)+' lb, sauce '+lb(SUB[2].q*S.k)+' lb. '+usd(total())+' for the run.'];}},
{id:'rec',target:function(){return $('rec');},prompt:'Record the actual output',where:'above',ok:function(){var v=num(S.v.out),b=v===null||v!==Math.round(v)||v<=0||v>batchLb();$('fout').classList.toggle('err',b);return !b;},
 run:function(){S.out=num(S.v.out);render();},
 after:function(){return['Expected and actual yield set the true cost per pound',n0(S.out)+' lb out against '+n0(expOut())+' expected. '+usd(total()/expOut())+' a lb planned, '+usd(total()/S.out)+' actual.'];}}];
'''
