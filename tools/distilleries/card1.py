"""Distilleries card 1: Mash bills, blends and cost per bottle. A BOM tree with a cost panel beside it, inside the app shell.
Start: an empty SKU search. Walkthrough: pick Barrel Rye 750 ml (sample or typed), the tree opens level by level
(SKU, blend, distillate, mash bill) while the cost rolls up in the panel, then the mash scales from 2,000 to 4,000 lb.
Money is held in cents so every sum is exact. Numbers are asserted in numbers_check.py."""
SUMMARY = 'Mash bills, blends and cost per bottle (a SKU picked from an empty search, its BOM opened level by level from SKU to blend, distillate and mash bill with the cost rolling up beside it, then the mash scaled from 2,000 to 4,000 lb)'
ARIA = 'Interactive product screen: pick the SKU Barrel Rye 750 ml, open its BOM from blend to distillate to mash bill while the bottle cost rolls up to $3.25, then scale the mash from 2,000 to 4,000 lb'
STEPS = 4
STUDIO = dict(lede='A typical BOM and cost roll up, built on your Sutton data with Studio. Want it different? Describe the change.',
              examples=['Add a proof gallon column', 'Change how a blend is costed', 'Add a mash type', 'Track yeast strain'],
              built_on='Items, BOMs, batches and costs', change='Fields, levels and cost rules')
# storyboard: screen where the target sits, module, target type, position (the variety test reads this)
STORY = [('SKU search', 'pro', 'sample chip', 'top left'), ('BOM tree', 'pro', 'tree row', 'center left'),
         ('BOM tree', 'pro', 'panel link', 'right'), ('BOM tree', 'pro', 'segmented toggle', 'top right')]

CSS = (
 '.sbar{display:flex;align-items:center;gap:8px}.srch{flex:1;position:relative;display:flex;flex-direction:column}.srch input{font:inherit;font-family:"JetBrains Mono",ui-monospace,monospace;font-size:11px;height:32px;padding:0 10px 0 30px;border:1px solid #D4D4D8;border-radius:7px;background:#fff;color:#18181B;width:100%}'
 '.srch input::placeholder{font-family:Inter,sans-serif;color:#A1A1AA}.srch input:focus-visible{outline:2px solid #18181B;outline-offset:1px}.srch svg{position:absolute;left:10px;top:10px}.srch.err input{border-color:#F87171;background:#FEF2F2}.srch .em{display:none;color:#B91C1C;font-size:8.8px;position:absolute;top:35px;left:2px}.srch.err .em{display:block}'
 '.smp{font-size:9.6px;color:#71717A;white-space:nowrap}.sc{height:28px;padding:0 11px;border:1px solid #E4E4E7;border-radius:999px;background:#fff;font-size:10.2px;font-weight:500;cursor:pointer;white-space:nowrap;transition:border-color .2s,background-color .2s}.sc:hover,.sc.fakehover{border-color:#18181B;background:#F4F4F5}.sc:focus-visible{outline:2px solid #18181B;outline-offset:1px}'
 '.empt.big{flex:1 1 0;padding-bottom:20px}.ghost{display:flex;flex-direction:column;gap:6px;margin-top:14px;width:240px}.ghost i{display:block;height:9px;border-radius:4px;background:#EDEDEF}.ghost i:nth-child(2){margin-left:18px}.ghost i:nth-child(3){margin-left:36px;width:70%}.ghost i:nth-child(4){margin-left:54px;width:50%}'
 '.tbr{display:flex;align-items:center;gap:10px}.tbr .nm{display:flex;flex-direction:column;gap:1px;line-height:1.25}.tbr .nm b{font-size:12px}.tbr .nm small{font-size:9px;color:#71717A}'
 '.bw{display:grid;grid-template-columns:1fr 190px;gap:10px}.bw>.cd{display:flex;flex-direction:column}'
 '.tr{display:grid;grid-template-columns:1fr 58px 66px;align-items:center;min-height:21px;padding:0 11px;border-top:1px solid #F0F0F1;gap:6px;font-size:9.9px;white-space:nowrap}.tr.h{min-height:22px;background:#FAFAFA;color:#71717A;font-size:9px;font-weight:500;border-top:0}'
 '.tr>span:nth-child(n+2){text-align:right;font-family:"JetBrains Mono",ui-monospace,monospace}.tr .nmc{display:flex;align-items:center;gap:5px;overflow:hidden;text-overflow:ellipsis}.tr .cv{width:12px;height:12px;flex:none;display:grid;place-items:center;color:#52525B;transition:transform .25s}.tr.op .cv{transform:rotate(90deg)}.tr .lf{width:12px;flex:none}'
 '.tr .lv{font-size:7.8px;font-weight:600;color:#71717A;background:#F4F4F5;border-radius:3px;padding:1px 4px;letter-spacing:.02em}.tr.l0{font-weight:600}.tr.bt0{background:#FAFAFA;color:#52525B;font-size:9.4px}'
 'button.tr{width:100%;border-left:0;border-right:0;border-bottom:0;background:#fff;text-align:left;cursor:pointer;font:inherit;font-size:9.9px;color:#18181B;transition:background-color .2s}button.tr:hover,button.tr.fakehover{background:#F4F4F5}button.tr:focus-visible{outline:2px solid #18181B;outline-offset:-2px}'
 '.tr.new{animation:exin .45s cubic-bezier(.22,.9,.28,1) both}.tr .pc{color:#71717A;font-size:8.6px;margin-left:2px}'
 '.seg{display:inline-flex;padding:2px;gap:2px;border:1px solid #E4E4E7;border-radius:7px;background:#FAFAFA}.sg{height:22px;padding:0 9px;border:0;border-radius:5px;background:transparent;font-family:"JetBrains Mono",ui-monospace,monospace;font-size:9.6px;color:#52525B;cursor:pointer;transition:background-color .2s,color .2s}.sg.on{background:#fff;color:#18181B;font-weight:600;box-shadow:0 0 0 1px #E4E4E7}.sg.fakehover,.sg:hover{color:#18181B}.sg:focus-visible{outline:2px solid #18181B;outline-offset:1px}'
 '.ct .seg{margin-left:auto}.ct .ms{font-weight:500;color:#71717A;font-size:9.4px;margin-left:auto}.ct .ms+.seg{margin-left:6px}'
 '.cp .sec{padding:6px 11px 7px;border-top:1px solid #F0F0F1}.cp .sec:first-of-type{border-top:0}.cp .sh{font-size:8.8px;font-weight:600;color:#71717A;margin-bottom:3px;display:flex;justify-content:space-between}'
 '.cl{display:flex;justify-content:space-between;gap:8px;font-size:9.6px;line-height:1.62;white-space:nowrap}.cl span:last-child{font-family:"JetBrains Mono",ui-monospace,monospace}.cl.tot{font-weight:600;border-top:1px dashed #E4E4E7;margin-top:2px;padding-top:2px}.cl.tot span:last-child{font-size:10.6px}'
 '.cp .sec.new{animation:exin .45s cubic-bezier(.22,.9,.28,1) both;background:#FFFCF2}.cp .hintline{color:#A1A1AA;font-size:9px;line-height:1.45;white-space:normal}'
 '.lk{display:flex;width:100%;justify-content:space-between;align-items:center;margin-top:4px;height:26px;padding:0 8px;border:1px solid #18181B;border-radius:6px;background:#fff;font-size:9.4px;font-weight:500;cursor:pointer;transition:background-color .2s}.lk:hover,.lk.fakehover{background:#F4F4F5}.lk:focus-visible{outline:2px solid #18181B;outline-offset:1px}.lk span:last-child{font-family:"JetBrains Mono",ui-monospace,monospace}'
 '.vr .row{grid-template-columns:86px 1fr 150px;font-size:9.6px;min-height:25px;white-space:nowrap}.vr .bl{font-family:"JetBrains Mono",ui-monospace,monospace;color:#1E3A8A;text-decoration:underline;text-decoration-color:#C7D2FE;text-underline-offset:2px;margin-left:6px}'
 '.ftn{margin-top:auto;padding:7px 11px;border-top:1px solid #F0F0F1;font-size:8.8px;color:#A1A1AA;background:#FCFCFC}'
 '.shot.ph .tr{grid-template-columns:1fr 66px;min-height:21px;padding:0 9px;font-size:10.2px}.shot.ph .tr>span:nth-child(2){display:none}.shot.ph button.tr{min-height:40px;font-size:10.4px}'
 '.shot.ph .sc{height:40px;padding:0 14px;font-size:11px}.shot.ph .srch input{height:40px}.shot.ph .srch svg{top:14px}.shot.ph .sg{height:36px;padding:0 12px;font-size:10.6px;flex:1}.shot.ph .seg{display:flex}'
 '.ptop{display:flex;justify-content:space-between;align-items:baseline;font-size:10.4px;padding:0 2px}.ptop b{font-family:"JetBrains Mono",ui-monospace,monospace;font-size:13px}.ptop small{color:#71717A;font-size:9.4px}'
 '.shot.ph .empt.big{padding:12px}.shot.ph.nar .xn{display:none}.shot.ph.nar .tr{min-height:19px}.shot.ph.nar .sg{height:34px}.rb .row{grid-template-columns:70px 1fr 90px 60px;font-size:9.6px;white-space:nowrap}.rb .row span:nth-child(n+3){text-align:right}.shot.ph .ghost{display:none}'
)

WIN = ''

JS = r'''
var FOC='.rail .ni,.bc,.phd>*,.bn .bi,.pg .tr,.pg .ct,.pg .sec,.pg .row,.pg .empt,.pg .smp,.pg .srch,.pg .tbr .nm,.pg .seg,.pg .sc,.pg .ftn,.pg .ptop';
var MASH=[['Corn',1400,14],['Rye',400,22],['Malted barley',200,31]];
var DRY=[['Glass bottle, 750 ml',92],['Closure, bar top cork',18],['Front label',9],['Back label',4],['Bottling labor',22]];
var DIST=180,CARTON=85,YEAST=2400,LABOR=163000,BATCHL=500,DISTML=450;
var S;
function k(){return S.mash/2000;}
function lb(i){return MASH[i][1]*k();}
function gc(i){return lb(i)*MASH[i][2];}
function grain(){return gc(0)+gc(1)+gc(2);}
function batch(){return grain()+YEAST*k()+LABOR*k();}
function liters(){return BATCHL*k();}
function perL(){return Math.round(batch()/liters());}
function dry(){var t=0;DRY.forEach(function(d){t+=d[1];});return t;}
function bottle(){return DIST+dry();}
function c(v){return m2(v/100);}
function pct(i){return Math.round(MASH[i][1]*100/2000);}
var CV='<span class="cv"><svg width="9" height="9" viewBox="0 0 10 10" fill="none" aria-hidden="true"><path d="M3.5 2l3 3-3 3" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg></span>';
function lvl(n){return '<span class="lv">L'+n+'</span>';}
function tr(o){var pad='padding-left:'+(11+o.l*14)+'px';var inner='<span class="nmc">'+(o.btn?CV:'<span class="lf"></span>')+(o.tag?lvl(o.l):'')+'<span>'+o.n+'</span></span><span>'+(o.q||'')+'</span><span>'+(o.v===undefined?'':o.v)+'</span>';
 var cls='tr l'+o.l+(o.open?' op':'')+(o.cls?' '+o.cls:'')+(o.anim?' new':'');
 return o.btn?'<button type="button" class="'+cls+'" id="'+o.id+'" style="'+pad+'" aria-expanded="'+(!!o.open)+'">'+inner+'</button>':'<div class="'+cls+'" style="'+pad+'">'+inner+'</div>';}
function seg(){return '<div class="seg" role="group" aria-label="Mash size">'+[2000,4000].map(function(x){return '<button type="button" class="sg'+(S.mash===x?' on':'')+'" id="m-'+x+'" aria-pressed="'+(S.mash===x)+'">'+n0(x)+' lb</button>';}).join('')+'</div>';}
function mashRows(P,a){var h=tr({l:3,n:'Mash bill v3',q:n0(S.mash)+' lb',v:c(grain()),tag:!P,open:1,anim:a,cls:'mb'});
 MASH.forEach(function(m,i){h+=tr({l:4,n:m[0]+(P?'':' <span class="pc">'+pct(i)+'%</span>'),q:n0(lb(i))+' lb',v:P?'<span id="g'+i+'">'+n0(lb(i))+' lb</span>':'<span id="g'+i+'">'+c(gc(i))+'</span>',anim:a});});return h;}
function tree(){var a=S.anim,h=tr({l:0,n:'Barrel Rye 750 ml',q:'1 bottle',v:c(bottle()),tag:1});
 h+=tr({l:1,n:'Blend BL-RYE-07',q:'750 ml',v:c(DIST),btn:!S.bl,id:'r-bl',open:S.bl,tag:1});
 if(S.bl){h+=tr({l:2,n:'Distillate DS-0412',q:DISTML+' ml',v:c(DIST),tag:1,open:S.ds,anim:a===2});
  if(S.ds){h+=tr({l:3,n:'Batch DS-0412, '+n0(liters())+' L',q:n0(liters())+' L',v:'<span id="bt">'+c(batch())+'</span>',cls:'bt0',anim:a===3})+mashRows(false,a===3)+tr({l:3,n:'Yeast and enzymes',q:'',v:c(YEAST*k()),anim:a===3})+tr({l:3,n:'Labor, energy, still time',q:'',v:c(LABOR*k()),anim:a===3});}
  h+=tr({l:2,n:'Water, proofing',q:'300 ml',v:c(0),anim:a===2});}
 if(S.ds)h+=tr({l:1,n:'Dry goods, 5 lines',q:'',v:c(dry())});else DRY.forEach(function(d){h+=tr({l:1,n:d[0],q:'1',v:c(d[1])});});return h;}
function line(a,b,t,id){return '<div class="cl'+(t?' tot':'')+'"><span>'+a+'</span><span'+(id?' id="'+id+'"':'')+'>'+b+'</span></div>';}
function panel(){var a=S.anim,h='<div class="ct">Cost roll up<span class="mut" style="font-weight:500">USD</span></div>';
 h+='<div class="sec"><div class="sh">Bottle</div>'+line('Blend',c(DIST))+(S.ds?line('Dry goods',c(dry())):DRY.map(function(d){return line(d[0].split(',')[0],c(d[1]));}).join(''))+line('Bottle cost',c(bottle()),1,'p-btl')+'</div>';
 h+='<div class="sec"><div class="sh">Case of 6</div>'+line('6 bottles',c(bottle()*6),0,'p-6')+line('Carton',c(CARTON))+line('Case cost',c(bottle()*6+CARTON),1,'p-case')+'</div>';
 if(!S.bl)h+='<div class="sec"><div class="hintline">Open the blend to see where its '+c(DIST)+' comes from.</div></div>';
 else{h+='<div class="sec'+(a===2?' new':'')+'"><div class="sh">Blend, 750 ml</div>'+line('Distillate '+DISTML+' ml',c(DIST))+line('Water 300 ml',c(0))+(S.ds?'':'<button type="button" class="lk" id="lk-pl"><span>Distillate per liter</span><span>'+c(perL())+'</span></button>')+'</div>';}
 if(S.ds)h+='<div class="sec'+(a===3?' new':'')+'"><div class="sh"><span>Batch, '+n0(liters())+' L</span></div>'+line('Grain',c(grain()),0,'p-gr')+line('Yeast and enzymes',c(YEAST*k()))+line('Labor, energy, still',c(LABOR*k()))+line('Batch cost',c(batch()),1,'p-bt')+line('Per liter',c(perL()),0,'p-pl')+'</div>';
 return h;}
function render(){var P=ph(),h='';
if(S.scr==='search'){setNav({m:'pro',bc:['Production','BOMs'],t:'BOMs and costs',scr:'SKU search'});
 h='<div class="frm sbar"><label class="srch" id="fs"><svg width="13" height="13" viewBox="0 0 14 14" fill="none" aria-hidden="true"><circle cx="6" cy="6" r="4.2" stroke="#A1A1AA" stroke-width="1.4"/><path d="M9.2 9.2l3 3" stroke="#A1A1AA" stroke-width="1.4" stroke-linecap="round"/></svg><input id="iq" placeholder="Search a SKU" value="'+S.v.q+'" autocomplete="off" aria-label="Search a SKU"><span class="em">No SKU matches. Try Barrel Rye 750 ml.</span></label>'+(P?'':'<span class="smp">Sample</span>')+'<button type="button" class="sc" id="smp">Barrel Rye 750 ml</button></div>';
 h+='<div class="empt big"><b>Pick a SKU to open its BOM</b><span>'+(P?'See every level and what each one costs.':'Every level from the bottle down to the blend, the distillate and the mash bill, with the cost of each level rolled up to the bottle and the case.')+'</span><div class="ghost" aria-hidden="true"><i></i><i></i><i></i><i></i></div></div>'+(P?'':'<div class="cd rb"><div class="ct">Recently opened BOMs<span class="mut" style="font-weight:500">Production</span></div>'+[['DG-750','Dry gin 750 ml','4 levels','Nov 21'],['SB-750','Single Barrel Bourbon 750 ml','4 levels','Nov 18'],['BR-375','Barrel Rye 375 ml','4 levels','Nov 12']].map(function(x){return '<div class="row"><span class="mono">'+x[0]+'</span><span>'+x[1]+'</span><span class="mut">'+x[2]+'</span><span class="mono mut">'+x[3]+'</span></div>';}).join('')+'</div>');}
else{setNav({m:'pro',bc:['Production',['BOMs','cb-b'],'BR-750'],t:'Barrel Rye 750 ml',chip:['c-ok','Active'],scr:'BOM tree',back:1,pa:'<span class="ch c-info" id="ver">Mash bill v3</span>'});
 if(P){if(!S.bl){h='<div class="ptop"><span><b id="p-btl">'+c(bottle())+'</b> <small>per bottle</small></span><small>Case of 6 <b style="font-size:11px" id="p-case">'+c(bottle()*6+CARTON)+'</b></small></div><div class="cd">'+tr({l:0,n:'Barrel Rye 750 ml',v:c(bottle())})+tr({l:1,n:'Blend BL-RYE-07',v:c(DIST),btn:1,id:'r-bl'})+tr({l:1,n:'Glass bottle',v:c(92)})+tr({l:1,n:'Closure and labels',v:c(31),cls:'xn'})+tr({l:1,n:'Bottling labor',v:c(22)})+'</div>';}
  else if(!S.ds){h='<div class="ptop"><span><b id="p-btl">'+c(bottle())+'</b> <small>per bottle</small></span><small>Blend <b style="font-size:11px">'+c(DIST)+'</b></small></div><div class="cd">'+tr({l:0,n:'Barrel Rye 750 ml',v:c(bottle())})+tr({l:1,n:'Blend, 750 ml',v:c(DIST),open:1})+tr({l:2,n:'Distillate, 450 ml',v:c(DIST),btn:1,id:'r-ds',anim:S.anim===2})+tr({l:2,n:'Water, 300 ml',v:c(0),anim:S.anim===2})+tr({l:1,n:'Dry goods',v:c(dry()),cls:'xn'})+'</div>';}
  else{h=seg()+'<div class="cd">'+tr({l:0,n:'Distillate, '+n0(liters())+' L',v:'<span id="bt">'+c(batch())+'</span>',open:1})+mashRows(true,S.anim===3).replace(/padding-left:(\d+)px/g,function(_,x){return 'padding-left:'+(x-28)+'px';}).replace(/ l3/g,' l1').replace(/ l4/g,' l2')+'</div>';}}
 else{h='<div class="tbr"><label class="srch" style="max-width:170px"><svg width="13" height="13" viewBox="0 0 14 14" fill="none" aria-hidden="true"><circle cx="6" cy="6" r="4.2" stroke="#A1A1AA" stroke-width="1.4"/><path d="M9.2 9.2l3 3" stroke="#A1A1AA" stroke-width="1.4" stroke-linecap="round"/></svg><input value="Barrel Rye 750 ml" aria-label="SKU" readonly></label><span class="nm grow"><b>BR-750, Barrel Rye 750 ml</b><small>Sold by the case of 6, bottled from blend BL-RYE-07</small></span></div>';
  h+='<div class="bw"><div class="cd tc"><div class="ct">BOM<span class="ms">'+(S.ds?'Mash size':'Per bottle')+'</span>'+(S.ds?seg():'')+'</div><div class="tr h"><span>Item</span><span>Quantity</span><span>Cost</span></div>'+tree()+(S.ds?'':'<div class="ftn">Rows with an arrow open the next level. Costs are per bottle.</div>')+'</div><div class="cd cp">'+panel()+'</div></div>';
  h+='<div class="cd vr"><div class="ct">Mash bill versions<span class="mut" style="font-weight:500">Linked to the batches that used them</span></div><div class="row"><span><span class="ch c-ok">v3 current</span></span><span>Corn 70%, rye 20%, malted barley 10%</span><span>Batches<span class="bl">DS-0412</span><span class="bl">DS-0418</span></span></div><div class="row"><span><span class="ch c-idle">v2</span></span><span>Corn 75%, rye 15%, malted barley 10%</span><span>Batches<span class="bl">DS-0371</span><span class="bl">DS-0388</span></span></div>'+(S.ds?'':'<div class="row"><span><span class="ch c-idle">v1</span></span><span>Corn 80%, rye 10%, malted barley 10%</span><span>Batches<span class="bl">DS-0322</span></span></div>')+'</div>';}}
if(P&&S.scr!=='search')h+=xw(!S.bl?[['Case of 6, with carton',c(bottle()*6+CARTON)],['Carton',c(CARTON)],['BOM version','Mash bill v3']]:!S.ds?[['Distillate per liter',c(perL())],['Bottle cost',c(bottle())],['Case of 6',c(bottle()*6+CARTON)]]:[['Yeast and enzymes',c(YEAST*k())],['Labor, energy, still time',c(LABOR*k())],['Per liter',c(perL())]]);
$('pg').innerHTML=h;}
$('pg').addEventListener('input',function(e){if(e.target.id==='iq'){S.v.q=e.target.value;$('fs').classList.remove('err');}});
function resetState(){S={scr:'search',bl:false,ds:false,mash:2000,anim:0,v:{q:''}};render();}
var OKQ=/^(barrel rye( 750( ?ml)?)?|br-?750)$/i;
function okQ(){var v=$('iq').value.trim(),b=v!==''&&!OKQ.test(v);$('fs').classList.toggle('err',b);return !b;}
function typeIn(done){var inp=$('iq'),s='Barrel Rye 750 ml',i=0;if(!inp||OKQ.test(inp.value.trim())){done();return;}(function t(){inp.value=s.slice(0,++i);if(i<s.length)later(t,38);else later(done,120);})();}
var CAPAT=function(hh){return ph()?{l:8,t:5}:{l:14,t:visH()-hh-40};};
var ST=[
{id:'sku',target:function(){return $('smp');},prompt:'Click the sample, or type Barrel Rye 750 ml and press Enter',where:'below',ok:okQ,run:function(q){var go=function(){S.v.q='Barrel Rye 750 ml';S.scr='tree';S.anim=1;render();};if(q)go();else typeIn(go);},
 after:['The BOM opens at the bottle','Barrel Rye 750 ml costs $3.25 a bottle and $20.35 a case of 6. The blend is the biggest line at $1.80.'],pc:'The bottle costs $3.25'},
{id:'blend',target:function(){return $('r-bl');},prompt:'Open the blend',where:'below',run:function(){S.bl=true;S.anim=2;render();},
 after:['The blend opens to its distillate','750 ml is 450 ml of distillate and 300 ml of water. The distillate share is $1.80.'],pc:'450 ml of distillate is $1.80'},
{id:'still',target:function(){return ph()?$('r-ds'):$('lk-pl');},prompt:function(){return ph()?'Open the distillate':'See where $4.00 per liter comes from';},where:'below',run:function(){S.ds=true;S.anim=3;render();},
 after:['The distillate opens to its batch and mash bill','Grain $346.00, yeast and enzymes $24.00, labor, energy and still time $1,630.00: $2,000.00 for 500 L, $4.00 per liter.'],pc:'$2,000.00 a batch, $4.00 per liter'},
{id:'scale',target:function(){return $('m-4000');},prompt:'Scale the mash to 4,000 lb',where:'below',run:function(){S.mash=4000;S.anim=0;render();},
 after:['Every quantity scales with the mash','Corn 2,800 lb, rye 800 lb, malted barley 400 lb. Grain $692.00 for 1,000 L, still $4.00 per liter.'],pc:'Grain is now $692.00 for 1,000 L'}];
ST.forEach(function(s){if(typeof s.prompt==='function'){var f=s.prompt;Object.defineProperty(s,'prompt',{get:f});}});
'''
