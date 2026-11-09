"""Plastics card 1: BOMs, Blends & Cost Roll-Up. Layout: a BOM tree on the left (carton, cap, compound, materials) with the runs on this BOM under it,
a detail panel on the right with Blend, Cost and Versions tabs.
Rounding: weights to 0.1 lb, money to cents (half up), cost per lb shown to five places with trailing zeros dropped."""
SUMMARY = 'BOMs, Blends & Cost Roll-Up (a BOM in levels from resin to carton, a blend by percentage scaled to a batch, cost rolled up per 1,000 caps, a resin price change, the runs it affects, a new BOM version)'
ARIA = 'Interactive product screen: open the BOM for cap CAP-38, scale compound BLK-PP-92 to a 1,000 lb batch, roll up its cost per 1,000 caps, apply a 10 percent rise on PP-100, see the scheduled runs it affects and save BOM version 4'
STEPS = 6
STUDIO = dict(lede='A typical BOM and costing screen, built on your Sutton data with Studio. Want it different? Describe the change.',
              examples=['A blend by percentage entry screen', 'A resin price impact view', 'A customer specific formulation list', 'A regrind percentage report'],
              built_on='Items, BOMs, costs and production runs', change='Levels, fields and views')

CSS = (
 '.b1{display:grid;grid-template-columns:262px 1fr;gap:12px;padding:12px 40px 0 16px;height:596px}'
 '.col{display:flex;flex-direction:column;gap:10px;min-height:0}'
 '.tre{flex:none}.tre .g{display:flex;align-items:flex-end;gap:7px;padding:8px 10px;border-bottom:1px solid #F0F0F1}.tre .fld{flex:1}.tre .pd{padding:10px}'
 '.nd{display:flex;align-items:center;gap:7px;min-height:30px;padding:0 10px;border-top:1px solid #F0F0F1;font-size:9.8px;white-space:nowrap}.nd:first-child{border-top:0}'
 '.nd .lv{font-family:"JetBrains Mono",ui-monospace,monospace;font-size:8.2px;color:#A1A1AA;width:14px}.nd .ln{width:10px;height:10px;border-left:1px solid #D4D4D8;border-bottom:1px solid #D4D4D8;margin-top:-8px;flex:none}'
 '.nd .ty{font-size:8.4px;color:#71717A;background:#F4F4F5;border-radius:4px;padding:1px 5px}.nd .q{margin-left:auto;font-family:"JetBrains Mono",ui-monospace,monospace;color:#52525B;font-size:9.2px}.nd.hl{background:#FAFAFA}'
 '.rns{flex:1 1 0;min-height:0}.rns .row{grid-template-columns:58px 1fr 44px 50px;min-height:24px;font-size:9.6px;white-space:nowrap}'
 '.det{flex:1 1 0;min-height:0;display:flex;flex-direction:column}.det .pd{padding:10px 11px}.pane{padding:8px 11px;display:flex;flex-direction:column;gap:7px}'
 '.bl .row,.cs .row{padding:0 2px;min-height:23px;font-size:9.6px;white-space:nowrap}.bl .row{grid-template-columns:1fr 50px 70px 74px}.cs .row{grid-template-columns:1fr 62px 58px 62px}.bl .row span:not(:first-child),.cs .row span:not(:first-child){text-align:right}'
 '.row.t{font-weight:600;background:#FAFAFA}.row.up{background:#FFFBEB}.sc{display:flex;align-items:flex-end;gap:7px}.sc .fld{width:96px}.sec{font-size:9px;font-weight:600;color:#71717A;margin-top:2px}'
 '.pk .row{grid-template-columns:1fr 70px 70px;padding:0 2px;min-height:23px;font-size:9.6px}.pk .row span:not(:first-child){text-align:right}'
 '.acts{display:flex;align-items:center;gap:7px;flex-wrap:wrap}.vr .row{grid-template-columns:42px 1fr 104px;padding:0 2px;min-height:26px;font-size:9.6px}'
 '.prc{flex:none}.prc .row{grid-template-columns:62px 1fr 50px;min-height:23px;font-size:9.6px;white-space:nowrap}.gy{font-size:9px;color:#71717A}'
)

WIN = (
 '<div class="hd"><svg width="16" height="16" viewBox="0 0 16 16" fill="none" aria-hidden="true"><rect x="5.5" y="2" width="5" height="3" rx="1" stroke="#18181B" stroke-width="1.2"/><rect x="2" y="11" width="4.5" height="3" rx="1" stroke="#18181B" stroke-width="1.2"/><rect x="9.5" y="11" width="4.5" height="3" rx="1" stroke="#18181B" stroke-width="1.2"/><path d="M8 5v3M4.2 11V8h7.6v3" stroke="#18181B" stroke-width="1.2"/></svg>'
 '<span class="tt">BOMs</span><span class="ch c-idle" id="hst">No BOM open</span><span class="sb grow">Ridgeway Plastics, closures</span></div>'
 '<div class="b1"><div class="col"><div class="cd tre" id="tre"></div><div class="cd rns" id="rns"></div></div><div class="col"><div class="cd det" id="det"></div><div class="cd prc"><div class="ct">Material prices<span class="mut" style="font-weight:500">Per lb, last receipt</span></div><div class="row"><span class="mono">PP-100</span><span>Northfield Polymers, 1,000 lb gaylord</span><span class="mono r" id="mp">0.74</span></div><div class="row"><span class="mono">COL-BLK</span><span>Kestrel Color, 50 lb box</span><span class="mono r">2.15</span></div><div class="row"><span class="mono">UV-02</span><span>Kestrel Color, 25 lb bag</span><span class="mono r">4.10</span></div><div class="row"><span class="mono">REG-PP</span><span>Own regrind, ground in house</span><span class="mono r">0.30</span></div></div></div></div>'
)

JS = r'''
var FOC='.hd>*,.prc,.tre .ct,.tre .g>*,.tre .pd,.nd,.rns,.det .ct,.det .tab,.det .pd,.sc>*,.pane .row,.pane .sec,.pane .gy,.acts>*';
var MAT=[['PP-100','Polypropylene',92.5,0.74],['COL-BLK','Black masterbatch',2.5,2.15],['UV-02','UV additive',0.5,4.10],['REG-PP','Regrind',4.5,0.30]];
var PER=0.0275,PACK=6.10,LAB=9.00,GAY=1000;
var RUNS=[['RUN-7655','Completed 09/09',0,'v2'],['RUN-7690','Completed 10/02',0,'v3'],['RUN-7701','Completed 10/19',0,'v3'],['RUN-7712','Scheduled 11/12',20000,'v3'],['RUN-7716','Scheduled 11/18',30000,'v3']];
var S;
function r2(n){return Math.round((n+1e-9)*100)/100;}
function f2(n){return n.toLocaleString('en-US',{minimumFractionDigits:2,maximumFractionDigits:2});}
function f1(n){return n.toLocaleString('en-US',{minimumFractionDigits:1,maximumFractionDigits:1});}
function fp(n){return n.toLocaleString('en-US',{minimumFractionDigits:2,maximumFractionDigits:5});}
function pr(i){return i===0?S.pp:MAT[i][3];}
function wt(i){return Math.round(MAT[i][2]*S.w/100*10)/10;}
function perLb(){return Math.round(MAT.reduce(function(a,m,i){return a+m[2]*pr(i);},0)*1e5/100)/1e5;}
function batch(){return r2(MAT.reduce(function(a,m,i){return a+r2(wt(i)*pr(i));},0));}
function comp(){return r2(1000*PER*perLb());}
function per1k(){return r2(comp()+PACK+LAB);}
function val(i){return String($(i).value).trim().replace(/,/g,'');}
function render(){
var t='<div class="ct">BOM tree'+(S.open?'<span class="ch c-info">Version '+(S.ver?'4':'3')+'</span>':'')+'</div><div class="g frm"><label class="fld" id="fit"><small>Item</small><input id="iit" value="'+S.v.it+'" autocomplete="off" spellcheck="false"><span class="em">Use CAP-38, the 38 mm cap</span></label>'+
(S.open?'<button type="button" class="bt done" disabled>Open</button>':'<button type="button" class="bt pri" id="obom">Open BOM</button>')+'</div>';
if(!S.open)t+='<div class="pd"><div class="empt"><b>No BOM open</b><span>Open a part to see every level from resin to the shipping carton.</span></div></div>';
else{var N=[[0,'CTN-1000','Carton of 1,000 caps','Packaged','1 carton'],[1,'CAP-38','38 mm black closure cap','Molded','1,000 x 0.0275 lb'],[2,'BLK-PP-92','Black PP compound','Compound','27.5 lb'],
[3,'PP-100','Polypropylene','Resin','92.5%'],[3,'COL-BLK','Black masterbatch','Colorant','2.5%'],[3,'UV-02','UV additive','Additive','0.5%'],[3,'REG-PP','Regrind','Regrind','4.5%'],[1,'PKG-38','Carton, bag and label','Packaging','1 set']];
t+='<div>'+N.map(function(n,i){var lvl=n[0];return '<div class="nd'+(S.anim?' in':'')+(lvl===3&&S.pp!==0.74&&n[1]==='PP-100'?' hl':'')+'" style="animation-delay:'+((3-Math.min(lvl,3))*110+i*20)+'ms;padding-left:'+(10+lvl*14)+'px">'+(lvl?'<span class="ln"></span>':'')+'<span class="mono">'+n[1]+'</span><span class="mut" style="overflow:hidden;text-overflow:ellipsis">'+n[2]+'</span><span class="q">'+n[4]+'</span></div>';}).join('')+'</div>';}
$('tre').innerHTML=t;
var r='<div class="ct">Runs on this BOM<span class="mut" style="font-weight:500">CAP-38</span></div><div class="row h"><span>Run</span><span>Status</span><span>Version</span><span class="r">Change</span></div>';
var tot=0;RUNS.forEach(function(x){var sch=x[2]>0,d=S.runs&&sch?r2(x[2]/1000*S.dl):0;tot=r2(tot+d);var v=sch&&S.ver?'v4':x[3];
r+='<div class="row'+(S.runs&&sch?' up':'')+'"><span class="mono">'+x[0]+'</span><span class="mut">'+x[1]+(sch?', '+n0(x[2]):'')+'</span><span><span class="ch '+(v==='v4'?'c-info':'c-idle')+'">'+v+'</span></span><span class="mono r" id="d-'+x[0]+'">'+(S.runs&&sch?'+'+f2(d):'')+'</span></div>';});
if(S.runs)r+='<div class="row t"><span>Scheduled</span><span></span><span></span><span class="mono r" id="dtot">+'+f2(tot)+'</span></div>';
$('rns').innerHTML=r;
var d='';
if(!S.open)d='<div class="ct">Details</div><div class="pd"><div class="empt"><b>Nothing open</b><span>Open a BOM to set its blend, roll up its cost and see its versions.</span></div></div>';
else{d='<div class="ct"><span>Compound <span class="mono">BLK-PP-92</span></span><span class="mut" style="font-weight:500">Blend by percentage</span></div><div class="tabs">'+[['bl','Blend'],['cs','Cost'],['vr','Versions']].map(function(x){return '<button type="button" class="tab'+(S.tab===x[0]?' on':'')+'" id="t-'+x[0]+'">'+x[1]+'</button>';}).join('')+'</div><div class="pane'+(S.anim2?' in':'')+'">';
if(S.tab==='bl'){d+='<div class="sc frm"><label class="fld" id="fw"><small>Batch weight, lb</small><input id="iw" value="'+S.v.w+'" inputmode="decimal" autocomplete="off"><span class="em">A weight in lb</span></label>'+(S.sc?'<button type="button" class="bt done" disabled>Scaled</button>':'<button type="button" class="bt pri" id="scl">Scale to batch</button>')+'</div>';
d+='<div class="bl"><div class="row h"><span>Material</span><span>Share</span><span>Weight</span><span>Buying unit</span></div>'+MAT.map(function(m,i){return '<div class="row"><span><span class="mono">'+m[0]+'</span> <span class="mut">'+m[1]+'</span></span><span class="mono">'+m[2].toFixed(1)+'%</span><span class="mono" id="w-'+m[0]+'">'+(S.sc?f1(wt(i))+' lb':'')+'</span><span class="mono mut">'+(S.sc&&i===0?(Math.round(wt(0)/GAY*1000)/1000)+' gaylord':'')+'</span></div>';}).join('')+
'<div class="row t"><span>Total</span><span class="mono">100.0%</span><span class="mono" id="wtot">'+(S.sc?f1(MAT.reduce(function(a,m,i){return a+wt(i);},0))+' lb':'')+'</span><span></span></div></div>';
d+='<span class="gy">Set the shares once. Any batch weight scales from them, and PP-100 is bought in 1,000 lb gaylords.</span>';}
if(S.tab==='cs'){d+='<div class="cs"><div class="row h"><span>Material, batch of '+n0(S.w)+' lb</span><span>Weight</span><span>Per lb</span><span>Cost</span></div>'+MAT.map(function(m,i){return '<div class="row'+(i===0&&S.pp!==0.74?' up':'')+'"><span><span class="mono">'+m[0]+'</span></span><span class="mono">'+f1(wt(i))+'</span><span class="mono" id="p-'+m[0]+'">'+fp(pr(i))+'</span><span class="mono">'+f2(r2(wt(i)*pr(i)))+'</span></div>';}).join('')+
'<div class="row t"><span>Batch</span><span class="mono">'+f1(S.w)+'</span><span class="mono" id="plb">'+fp(perLb())+'</span><span class="mono" id="btot">'+f2(batch())+'</span></div></div>';
d+='<div class="sec">Per 1,000 caps, 27.5 lb of compound</div><div class="pk"><div class="row"><span>Compound</span><span class="mono mut">'+(S.pp!==0.74?f2(S.c0):'')+'</span><span class="mono" id="cmp">'+f2(comp())+'</span></div><div class="row"><span>Packaging</span><span></span><span class="mono">'+f2(PACK)+'</span></div><div class="row"><span>Labor and press time</span><span></span><span class="mono">'+f2(LAB)+'</span></div>'+
'<div class="row t"><span>Cost per 1,000 caps</span><span class="mono mut">'+(S.pp!==0.74?f2(S.t0):'')+'</span><span class="mono" id="k1">'+f2(per1k())+'</span></div></div>';
d+='<div class="acts">';if(S.pp===0.74)d+='<span class="sc frm"><label class="fld" id="fpc" style="width:70px"><small>PP-100 change</small><input id="ipc" value="'+S.v.pc+'" inputmode="decimal" autocomplete="off"><span class="em">Like +10%</span></label><button type="button" class="bt pri" id="apc">Apply +10%</button></span>';
else{d+='<span class="ch c-warn" id="upc">Up '+f2(S.dl)+' per 1,000 caps</span>';if(!S.runs)d+='<button type="button" class="bt pri" id="orn">Open runs affected</button>';else if(!S.ver)d+='<button type="button" class="bt pri" id="sav">Save as new version</button>';}
d+='</div>';}
if(S.tab==='vr'){d+='<div class="vr"><div class="row h"><span>Version</span><span>Change</span><span class="r">Runs</span></div>'+
'<div class="row in"><span><span class="ch c-info">v4</span></span><span>PP-100 at '+fp(S.pp)+' a lb, '+f2(per1k())+' per 1,000</span><span class="r mono">RUN-7712, 7716</span></div>'+
'<div class="row"><span><span class="ch c-idle">v3</span></span><span>Regrind share 4.5%, '+f2(S.t0)+' per 1,000</span><span class="r mono">RUN-7690, 7701</span></div>'+
'<div class="row"><span><span class="ch c-idle">v2</span></span><span>UV-02 added at 0.5%</span><span class="r mono">RUN-7655</span></div><div class="row"><span><span class="ch c-idle">v1</span></span><span>First release</span><span class="r mono">RUN-7610</span></div></div>'+
'<span class="ch c-ok" style="align-self:flex-start">Version 4 saved, earlier runs stay on version 3</span>';}
d+='</div>';}
$('det').innerHTML=d;
$('mp').textContent=fp(S.pp);$('mp').parentNode.classList.toggle('up',S.pp!==0.74);
$('hst').textContent=S.open?'CAP-38, version '+(S.ver?'4':'3'):'No BOM open';$('hst').className='ch '+(S.open?'c-info':'c-idle');
S.anim=false;S.anim2=false;}
$('tre').addEventListener('input',function(e){if(e.target.id==='iit')S.v.it=e.target.value;});
$('det').addEventListener('input',function(e){if(e.target.id==='iw')S.v.w=e.target.value;if(e.target.id==='ipc')S.v.pc=e.target.value;});
function resetState(){S={open:false,sc:false,tab:'bl',runs:false,ver:false,anim:false,anim2:false,w:1000,pp:0.74,dl:0,c0:0,t0:0,v:{w:'1,000',pc:'+10%',it:'CAP-38'}};render();}
var CAPAT=function(hh){return{l:visW()-cap.offsetWidth-14,t:visH()-hh-40};};
var ST=[
{id:'open',target:function(){return $('obom');},prompt:'Click Open BOM',where:'below',ok:function(){var b=val('iit').toUpperCase()!=='CAP-38';$('fit').classList.toggle('err',b);return !b;},
 run:function(){S.open=true;S.anim=true;S.anim2=true;render();},after:['A part builds in levels, and each level is stocked and costed on its own','Four materials make compound BLK-PP-92, which molds CAP-38, packed 1,000 to carton CTN-1000.']},
{id:'scl',target:function(){return $('scl');},prompt:'Click Scale to batch',where:'below',ok:function(){var w=parseFloat(val('iw')),b=!(/^\d{1,6}(\.\d)?$/.test(val('iw'))&&w>0);$('fw').classList.toggle('err',b);return !b;},
 run:function(){S.w=parseFloat(val('iw'));S.sc=true;render();},after:function(){return['Set the blend once as percentages, then scale it to any batch weight',MAT.map(function(m,i){return f1(wt(i));}).join(', ')+' lb. PP-100 is '+(Math.round(wt(0)/GAY*1000)/1000)+' of a 1,000 lb gaylord.'];}},
{id:'cs',target:function(){return $('t-cs');},prompt:'Click the Cost tab',where:'below',run:function(){S.tab='cs';S.anim2=true;S.c0=comp();S.t0=per1k();render();},
 after:function(){return['Resin, colorant, additive, regrind, packaging and labor roll up to a true cost per part','Batch '+f2(batch())+'. Compound '+f2(comp())+' per 1,000 caps, '+f2(per1k())+' with packaging and labor.'];}},
{id:'apc',target:function(){return $('apc');},prompt:'Click Apply +10%',where:'below',ok:function(){var m=val('ipc').replace(/\s/g,'').match(/^\+?(\d{1,2}(\.\d)?)%?$/),b=!m;$('fpc').classList.toggle('err',b);return !b;},
 run:function(){var m=val('ipc').replace(/\s/g,'').match(/^\+?(\d{1,2}(\.\d)?)%?$/),p=parseFloat(m[1]);S.pp=Math.round(0.74*(100+p)*10)/1000;S.dl=r2(per1k()-S.t0);render();},
 after:function(){return['See what a resin price rise does to every part before you reprice','PP-100 at '+fp(S.pp)+'. Compound '+f2(comp())+' per 1,000 caps, total '+f2(per1k())+', up '+f2(S.dl)+'.'];}},
{id:'orn',target:function(){return $('orn');},prompt:'Click Open runs affected',where:'below',run:function(){S.runs=true;render();},
 after:function(){var a=r2(20*S.dl),b=r2(30*S.dl);return['The runs already scheduled show their extra cost straight away','RUN-7712 up '+f2(a)+' and RUN-7716 up '+f2(b)+', '+f2(r2(a+b))+' together.'];}},
{id:'sav',target:function(){return $('sav');},prompt:'Click Save as new version',where:'below',run:function(){S.ver=true;S.tab='vr';S.anim2=true;render();},after:['Every version is kept, and each run stays linked to the one it used','BOM version 4 saved. RUN-7712 and RUN-7716 move to it, earlier runs stay on version 3.']}];
'''
