"""Coffee roasting card 3: Blends & Bean Substitution.
Layout: list and detail. A list of blends on the left, the open blend's BOM lines on the right, and below them a bean
substitution panel and a cost and version panel.
Open the house blend (origin percentages that sum to 100), resize it from a 5 kg test roast to a 120 kg batch, swap
Brazil for Honduras across every blend that uses it, see cost per bag change before saving, and keep v1 beside v2.
Every number is computed in cents and grams."""
from frame_auto import header

SUMMARY = 'Blends & Bean Substitution (open a house blend BOM with origin percentages, resize it from a test roast to a production batch, swap one origin across every blend, see cost per bag change, keep the earlier version)'
ARIA = 'Interactive product screen: Harbor House blend is Brazil 45%, Colombia 35%, Ethiopia 20%; resizing from 5 kg to 120 kg scales every line, swapping Brazil for Honduras updates two blends and four bag sizes, the 12 oz bag drops from $2.84 to $2.79, and v1 is kept beside v2'
STEPS = 5
STUDIO = dict(lede='A typical blend BOM screen, built on your Sutton data with Studio. Want it different? Describe the change.',
              examples=['Suggest a swap by cup score', 'Lock a blend for a customer', 'Show margin per bag', 'Ask approval before a swap'],
              built_on='Blend BOMs, green lots and costs', change='Lines, bag sizes and rules')

ICON = '<circle cx="8" cy="8" r="5.6"/><path d="M8 2.4V8l4.6 3.2M8 8 3.4 11.2"/>'

CSS = (
 '.q3{padding:10px 40px 0 16px;display:flex;flex-direction:column;gap:10px}'
 '.q3t{display:grid;grid-template-columns:200px 450px;gap:10px;height:268px;flex:none}.q3b{display:grid;grid-template-columns:290px 360px;gap:10px;height:240px;flex:none}.qsub{display:flex;flex-direction:column}.qft9{margin-top:auto;padding:6px 11px;border-top:1px solid #F0F0F1;font-size:8.8px;color:#71717A}'
 '.qbl{display:flex;flex-direction:column}.qbl .ct{height:30px}.qbll{padding:6px;display:flex;flex-direction:column;gap:5px}'
 '.qbi{font:inherit;text-align:left;border:1px solid #E4E4E7;border-radius:7px;background:#fff;padding:7px 9px;display:flex;flex-direction:column;gap:3px;cursor:pointer;font-size:9px;color:#52525B;transition:background-color .2s,box-shadow .2s}'
 '.qbi b{font-size:10.4px;color:#18181B}.qbi .qtg{display:flex;gap:4px;flex-wrap:wrap}.qbi .qtg span{font-size:8.4px;padding:1px 5px;border-radius:4px;background:#F4F4F5;color:#52525B}.qbi .qtg span.qhn{background:#FEF3C7;color:#92400E}'
 '.qbi.sel{background:#F4F4F5;box-shadow:inset 3px 0 0 #18181B}.qbi.fakehover{background:#FAFAFA}.qbi:focus-visible{outline:2px solid #18181B;outline-offset:2px}'
 '.qbl .qlt{margin-top:auto;padding:7px 9px;border-top:1px solid #F0F0F1;font-size:8.6px;color:#71717A;line-height:1.4}'
 '.qdt .empt,.qsub .empt,.qcost .empt{margin:8px 10px;height:calc(100% - 48px);padding:8px}'
 '.qdt .row{grid-template-columns:1fr 64px 44px 76px 54px;min-height:28px;font-size:9.6px;gap:8px}.qdt .row>span:nth-child(n+3){text-align:right}.qdt .row.qsw{background:#FFFBEB}.qdt .row.qtot{font-weight:600;background:#FAFAFA}'
 '.qdt .row .mono{font-size:9.4px}.qdt .qsw .qold{text-decoration:line-through;color:#A1A1AA;margin-right:5px}'
 '.qrs{display:flex;align-items:center;gap:7px;padding:8px 11px;border-top:1px solid #F0F0F1;font-size:9.4px;color:#52525B}.qrs .fld{flex-direction:row;align-items:center;gap:6px;position:relative}.qrs .fld input{width:60px;text-align:right;font-size:10px;padding:4px 6px}.qrs .fld .em{position:absolute;left:0;top:26px;white-space:nowrap;background:#fff;padding:1px 4px;z-index:3}'
 '.qrs .qsc{margin-left:auto;font-family:"JetBrains Mono",ui-monospace,monospace;font-size:9.2px;color:#71717A}'
 '.qsf{display:flex;align-items:flex-end;gap:7px;padding:8px 11px 0}.qsf label{display:flex;flex-direction:column;gap:3px;font-size:8.8px;color:#71717A}.qsf select{font:inherit;font-size:9.8px;padding:4px 6px;border:1px solid #D4D4D8;border-radius:6px;background:#fff;color:#18181B}.qsf select:disabled{background:#FAFAFA;color:#A1A1AA}.qsf .bt:disabled{opacity:.4;cursor:default}'
 '.qaf{padding:8px 11px 0;display:flex;flex-direction:column;gap:5px}.qaf .qar{display:flex;justify-content:space-between;align-items:center;padding:5px 8px;border:1px solid #F0F0F1;border-radius:6px;font-size:9.4px}.qaf .qar b{font-weight:600}.qaf .qar .mono{font-size:9.2px}'
 '.qaf .qnt{font-size:9px;color:#71717A}'
 '.qcost table{width:100%;border-collapse:collapse;font-size:9.4px;margin-top:2px}.qcost th{font-size:8.6px;color:#71717A;font-weight:500;height:20px;text-align:right;padding:0 8px}.qcost td{height:24px;border-top:1px solid #F4F4F5;text-align:right;padding:0 8px;font-family:"JetBrains Mono",ui-monospace,monospace}'
 '.qcost td:first-child,.qcost th:first-child{text-align:left;font-family:inherit}.qcost .qdn{color:#166534}'
 '.qvh{padding:6px 11px 0;display:flex;flex-direction:column;gap:4px}.qvr{display:grid;grid-template-columns:28px 52px 1fr auto;gap:8px;align-items:center;font-size:9.2px;padding:4px 7px;border-radius:6px;border:1px solid #F0F0F1}.qvr b{font-family:"JetBrains Mono",ui-monospace,monospace}.qvr.qcur{border-color:#BBF7D0;background:#F0FDF4}'
)

WIN = (
 header(ICON, 'Blend BOMs', 'Roastery blends and substitutions', '<span class="ch c-idle" id="qst">No blend open</span>')
 + '<div class="q3"><div class="q3t"><div class="cd qbl" id="qbl"></div><div class="cd qdt" id="qdt"></div></div>'
 '<div class="q3b"><div class="cd qsub"><div class="ct"><span>Substitute a bean</span><span class="ch c-idle" id="qsc">Every blend</span></div>'
 '<div class="qsf frm"><label>Replace<select id="qfr" aria-label="Origin to replace" disabled><option>Brazil</option><option>Colombia</option><option>Ethiopia</option><option>Guatemala</option></select></label>'
 '<label>With<select id="qto" aria-label="Replacement origin" disabled><option>Honduras</option><option>Guatemala</option><option>Colombia</option></select></label><button type="button" class="bt pri" id="qpw" disabled>Preview swap</button></div><div id="qaf"></div><div class="qft9">A swap changes every blend and bag size that uses the bean.</div></div>'
 '<div class="cd qcost" id="qcost"></div></div></div>'
)

JS = r'''
var FOC='.hd>*,.qbl,.qdt,.qsub,.qcost';
var PR={Brazil:620,Colombia:740,Ethiopia:860,Guatemala:710,Honduras:590};
var LOT={Brazil:'GL-2214',Colombia:'GL-2211',Ethiopia:'GL-2207',Guatemala:'GL-2209',Honduras:'GL-2219'};
var BL=[{id:'HB',n:'Harbor House',l:[['Brazil',45],['Colombia',35],['Ethiopia',20]]},{id:'NO',n:'Night Owl Espresso',l:[['Brazil',60],['Guatemala',40]]},{id:'SL',n:'Sunrise Light',l:[['Ethiopia',70],['Colombia',30]]}];
var BAG=[['12 oz',400],['5 lb',2668]];
var TEST=5000;
var S;
function kg(g){return (g/1000).toLocaleString('en-US',{minimumFractionDigits:3,maximumFractionDigits:3});}
function lines(b,sw){return b.l.map(function(x){return [sw&&S.swap&&x[0]===S.fr?S.to:x[0],x[1],x[0]];});}
function pctSum(b){return b.l.reduce(function(s,x){return s+x[1];},0);}
function perKg(b,sw){return lines(b,sw).reduce(function(s,x){return s+x[1]*PR[x[0]];},0);}
function bagC(b,g,sw){return Math.round(perKg(b,sw)*g/100000);}
function usd(c){return '$'+(c/100).toFixed(2);}
function hit(){return S.swap?BL.filter(function(b){return b.l.some(function(x){return x[0]===S.fr;});}):[];}
function cur3(){return BL[0];}
function render(){
var l=$('qbl');l.innerHTML='<div class="ct"><span>Blends</span><span class="ch c-idle">'+BL.length+'</span></div><div class="qbll">'+BL.map(function(b,i){var hn=S.saved&&hit().indexOf(b)>=0;
return '<button type="button" class="qbi'+(S.open&&i===0?' sel':'')+'" id="qb'+i+'"><b>'+b.n+'</b><span class="qtg">'+lines(b,S.saved).map(function(x){return '<span class="'+(hn&&x[0]===S.to?'qhn':'')+'">'+x[0]+' '+x[1]+'%</span>';}).join('')+'</span></button>';}).join('')+'</div><div class="qlt">Percentages are by green weight. Cost uses each origin\'s current lot.</div>';
var d=$('qdt'),b=cur3();
if(!S.open)d.innerHTML='<div class="ct"><span>Blend BOM</span></div><div class="empt"><b>No blend open</b><span>Open a blend to see its origins, lots and batch weights.</span></div>';
else{var ls=lines(b,true),tot=0;
d.innerHTML='<div class="ct"><span>'+b.n+' <span class="mut" style="font-weight:400">BOM</span></span><span class="ch '+(S.saved?'c-ok':S.swap?'c-warn':'c-info')+'" id="qvc">'+(S.saved?'v2 current':S.swap?'v2 not saved':'v1 current')+'</span></div>'
+'<div class="row h"><span>Origin</span><span>Green lot</span><span>Share</span><span>Batch kg</span><span>$ per kg</span></div>'
+ls.map(function(x,i){var g=S.size*x[1]/100;tot+=g;var sw=S.swap&&x[2]===S.fr;return '<div class="row'+(sw?' qsw':'')+'"><span>'+(sw?'<span class="qold">'+x[2]+'</span>':'')+x[0]+'</span><span class="mono">'+LOT[x[0]]+'</span><span class="mono">'+x[1]+'%</span><span class="mono" id="qk'+i+'">'+kg(g)+'</span><span class="mono">'+(PR[x[0]]/100).toFixed(2)+'</span></div>';}).join('')
+'<div class="row qtot"><span>Total</span><span></span><span class="mono" id="qps">'+pctSum(b)+'%</span><span class="mono" id="qkt">'+kg(tot)+'</span><span class="mono">'+(perKg(b,true)/10000).toFixed(2)+'</span></div>'
+'<div class="qrs frm" id="qfz"><span>Batch</span><label class="fld" id="qfs"><input id="qbs" value="'+(S.typed||'')+'" inputmode="decimal" placeholder="kg" autocomplete="off" aria-label="Batch size in kg"><span class="em">Enter 1 to 500 kg</span></label><span>kg green</span><button type="button" class="bt" id="qrz">Resize</button><span class="qsc" id="qsz">'+(S.size===TEST?'Test roast '+kg(TEST)+' kg':'Production batch '+kg(S.size)+' kg')+'</span></div>';}
['qfr','qto','qpw'].forEach(function(id){$(id).disabled=!S.resized||S.saved;});
var a=$('qaf');if(!S.swap)a.innerHTML='<div class="empt" style="margin:8px 10px;height:118px"><b>No swap yet</b><span>Pick a bean to replace and Sutton lists every blend and bag size that uses it.</span></div>';
else{var h=hit();a.innerHTML='<div class="qaf">'+h.map(function(x){var p=x.l.filter(function(y){return y[0]===S.fr;})[0][1];return '<div class="qar"><b>'+x.n+'</b><span class="mono">'+S.fr+' '+p+'% to '+S.to+'</span></div>';}).join('')+'<span class="qnt" id="qaff">'+h.length+' blends and '+(h.length*BAG.length)+' bag sizes change. '+(BL.length-h.length)+' blend unchanged.</span></div>';}
var sc=$('qsc');sc.textContent=S.swap?hit().length+' blends affected':'Every blend';sc.className='ch '+(S.swap?'c-warn':'c-idle');
var c=$('qcost');
if(!S.cost)c.innerHTML='<div class="ct"><span>Cost per bag</span>'+(S.swap?'<button type="button" class="bt pri" id="qcs">Show cost</button>':'')+'</div><div class="empt"><b>No change to cost yet</b><span>Cost per bag before and after a swap shows here before you save.</span></div>';
else{var h2=hit(),rows='';h2.forEach(function(x){BAG.forEach(function(z,j){var o=bagC(x,z[1],false),n=bagC(x,z[1],true);rows+='<tr><td>'+x.n+', '+z[0]+'</td><td>'+usd(o)+'</td><td id="qc-'+x.id+j+'">'+usd(n)+'</td><td class="qdn">'+(n<o?'down ':'up ')+usd(Math.abs(n-o))+'</td></tr>';});});
c.innerHTML='<div class="ct"><span>Cost per bag</span>'+(S.saved?'<span class="ch c-ok">Saved</span>':'<button type="button" class="bt pri" id="qsv">Save as v2</button>')+'</div><table><tr><th>Blend, bag</th><th>v1</th><th>v2</th><th>Change</th></tr>'+rows+'</table>'
+(S.saved?'<div class="qvh"><div class="qvr qcur"><b>v2</b><span>Nov 17</span><span>'+S.to+' replaces '+S.fr+'</span><span class="ch c-ok">Current</span></div><div class="qvr" id="qv1"><b>v1</b><span>Nov 2</span><span>'+S.fr+' in '+h2.length+' blends</span><span class="ch c-idle">Kept for reference</span></div></div>':'');}
var st=$('qst');st.textContent=S.saved?'v2 saved':S.open?b.n:'No blend open';st.className='ch '+(S.saved?'c-ok':S.open?'c-info':'c-idle');}
function bsz(){var v=String($('qbs').value).replace(/,/g,'').trim();return /^\d+(\.\d{1,3})?$/.test(v)?Math.round(parseFloat(v)*1000):NaN;}
function typeIn(id,t,done){var i=0;(function k(){$(id).value=t.slice(0,i);if(i<t.length){i++;later(k,90);}else done();})();}
winEl.addEventListener('input',function(e){if(e.target.id==='qbs')S.typed=e.target.value;});
function resetState(){S={open:false,size:TEST,resized:false,swap:false,cost:false,saved:false,fr:'Brazil',to:'Honduras',typed:''};$('qfr').value='Brazil';$('qto').value='Honduras';render();}
var CAPAT=function(hh){return cur<=1?{l:14,t:visH()-hh-14}:{l:220,t:56};};
var ST=[
{id:'open',target:function(){return $('qb0');},prompt:'Open Harbor House',where:'right',run:function(){S.open=true;S.typed='120';render();},
 after:function(){var b=cur3();return['Open a house blend and read its origin percentages',b.n+' is '+b.l.map(function(x){return x[0]+' '+x[1]+'%';}).join(', ')+': '+pctSum(b)+'% in all, at a '+kg(TEST)+' kg test roast.'];}},
{id:'size',target:function(){return mode==='try'?$('qrz'):$('qbs');},prompt:'Type 120 as the batch, then Resize',where:'above',
 ok:function(){var v=bsz(),b=!(v>=1000&&v<=500000);$('qfs').classList.toggle('err',b);return !b;},
 run:function(quick){var go=function(){var v=mode==='watch'||!(bsz()>0)?120000:bsz();S.size=v;S.typed=String(v/1000);S.resized=true;render();};if(mode==='watch'&&!quick)typeIn('qbs','120',go);else{if(!$('qbs').value){S.typed='120';$('qbs').value='120';}go();}},
 after:function(){var b=cur3();return['Resize the blend from a test roast to a production batch',kg(TEST)+' kg becomes '+kg(S.size)+' kg: '+b.l.map(function(x){return x[0]+' '+kg(S.size*x[1]/100);}).join(', ')+' kg.'];}},
{id:'swap',target:function(){return $('qpw');},prompt:'Replace Brazil with Honduras, then Preview swap',where:'above',
 ok:function(){return $('qfr').value!==$('qto').value;},
 run:function(){S.fr=$('qfr').value;S.to=$('qto').value;S.swap=true;render();},
 after:function(){var h=hit();return['Swap one origin across every blend',S.to+' replaces '+S.fr+' in '+h.map(function(x){return x.n;}).join(' and ')+': '+h.length+' blends, '+(h.length*BAG.length)+' bag sizes.'];}},
{id:'cost',target:function(){return $('qcs');},prompt:'Click Show cost',where:'above',run:function(){S.cost=true;render();},
 after:function(){var b=cur3();return['See cost per bag change with the new bean',b.n+' 12 oz goes from '+usd(bagC(b,400,false))+' to '+usd(bagC(b,400,true))+', 5 lb from '+usd(bagC(b,2668,false))+' to '+usd(bagC(b,2668,true))+'. Not saved yet.'];}},
{id:'save',target:function(){return $('qsv');},prompt:'Save as v2',where:'above',run:function(){S.saved=true;render();},
 after:function(){return['Keep the earlier version for reference','v2 with '+S.to+' is current. v1 with '+S.fr+' stays in the history.'];}}];
'''
