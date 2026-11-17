"""Coffee roasting card 3: Blends & Bean Substitution.
Layout: list and detail. On the left the blend list and a substitution panel; on the right the blend record: the BOM by
origin with a batch size field, the cost per bag and the version history.
A blend is a BOM with percentages by origin that sum to 100. Resizing scales every line; when a bean runs out one swap
updates every blend and bag size that uses it, the cost per bag shows before it is saved, and v1 is kept for reference.
Costs are kept in cents per kg and weights in grams, so every number is exact."""
from frame_auto import header

SUMMARY = 'Blends & Bean Substitution (open a house blend and its origin percentages, resize a test roast to a production batch, swap one origin across every blend, see cost per bag change, keep the earlier version)'
ARIA = 'Interactive product screen: the Foundry espresso blend BOM, Brazil 50%, Colombia 30%, Ethiopia 20%; resize it from a 5 kg test roast to a 120 kg batch, swap Brazil for Honduras in every blend that uses it, compare cost per bag before and after, and save v2 while keeping v1'
STEPS = 5
STUDIO = dict(lede='A typical blend BOM screen, built on your Sutton data with Studio. Want it different? Describe the change.',
              examples=['Suggest a swap by cup profile', 'Add a decaf version', 'Lock a blend for a client', 'Show margin per bag'],
              built_on='BOMs, green lots and costs', change='Origins, bag sizes and rules')

ICON = '<circle cx="8" cy="8" r="5.5"/><path d="M8 2.5V8l4.6 3"/><path d="M8 8L3.4 11"/>'

CSS = (
 '.k3{padding:10px 40px 0 16px;display:grid;grid-template-columns:214px 436px;gap:10px;height:546px}'
 '.k3l,.k3r{display:flex;flex-direction:column;gap:8px;min-width:0}'
 '.bls{height:262px;flex:none}.bsub{flex:1 1 auto}.brec{height:216px;flex:none}.bcs{height:120px;flex:none}.bhi{flex:1 1 auto}'
 '.bsub .empt,.brec .empt,.bcs .empt,.bhi .empt{margin:8px 10px;height:calc(100% - 46px);padding:8px}.bsub .empt,.bhi .empt{padding-top:44px}'
 '.bls .row{grid-template-columns:1fr auto;min-height:54px;padding:0 10px}.bnm{display:flex;flex-direction:column;gap:2px;min-width:0}.bnm b{font-size:10px;font-weight:600}.bnm small{font-size:8.6px;color:#71717A;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}'
 '.bls .row.hit{background:#FFFBEB}.bls .row.hit.sel{background:#FEF3C7}'
 '.bfm{display:flex;align-items:center;gap:8px;padding:7px 11px;border-bottom:1px solid #F0F0F1;position:relative}.bfm .fld{flex-direction:row;align-items:center;gap:6px;position:relative}.bfm .fld small{font-size:9.4px;color:#18181B;font-weight:600;white-space:nowrap}'
 '#bsz{width:62px;font-size:10.4px;padding:5px 7px}.bfm .fld .em{position:absolute;left:0;top:28px;white-space:nowrap;background:#fff;padding:1px 4px;z-index:3}.bfm .bt{font-size:9.6px;padding:4px 9px}.bfm .note{font-size:8.8px;color:#71717A;margin-left:auto}'
 '.bom .row{grid-template-columns:1fr 70px 52px 72px;min-height:26px;font-size:9.4px}.bom .row.h{min-height:22px}.bom .row>span:not(:first-child){text-align:right;font-family:"JetBrains Mono",ui-monospace,monospace}'
 '.bo{display:flex;align-items:center;gap:7px;min-width:0}.bo i{width:9px;height:9px;border-radius:3px;flex:none}.bo small{font-family:"JetBrains Mono",ui-monospace,monospace;font-size:8.4px;color:#71717A}.bom .row.sw{background:#FFFBEB}.bom .row.tot{background:#FAFAFA;font-weight:600}'
 '.mix{display:flex;height:8px;margin:6px 11px 2px;border-radius:5px;overflow:hidden;gap:2px}.mix i{display:block;height:100%;transition:width .5s}'
 '.sal{margin:8px 9px 0;padding:7px 8px;border-radius:7px;background:#FEF2F2;border:1px solid #FECACA;font-size:8.8px;color:#7F1D1D;line-height:1.4}.sal b{font-family:"JetBrains Mono",ui-monospace,monospace}'
 '.sal.ok{background:#F0FDF4;border-color:#BBF7D0;color:#166534}.sbt{padding:7px 9px 0}.sbt .bt{width:100%;font-size:9.4px}'
 '.bsub .row{grid-template-columns:1fr auto;min-height:28px;font-size:8.8px;padding:0 9px}.bsub .row.hd2{min-height:22px;font-size:8.6px;color:#71717A;background:#FAFAFA;border-top:0;margin-top:8px}'
 '.cg{display:grid;grid-template-columns:1fr 1fr;gap:8px;padding:8px 11px}.cb{border:1px solid #F0F0F1;border-radius:7px;padding:6px 8px;display:flex;flex-direction:column;gap:2px}.cb small{font-size:8.6px;color:#71717A}'
 '.cb .vv{display:flex;align-items:baseline;gap:6px;font-family:"JetBrains Mono",ui-monospace,monospace}.cb .vv s{color:#A1A1AA;font-size:10px}.cb .vv b{font-size:14px}.cb .dl{font-size:8.8px;color:#B45309;font-family:"JetBrains Mono",ui-monospace,monospace}'
 '.cnote{padding:0 11px;font-size:8.6px;color:#71717A;line-height:1.35}'
 '.bhi .row{grid-template-columns:22px 1fr 40px 96px;min-height:32px;font-size:9px;gap:6px}.bhi .row>span:last-child{justify-self:end}.bhi .row .mono{font-weight:600}.bhi .row.cur{background:#F0FDF4}.bhi .bt{font-size:9px;padding:3px 8px}.hbt{padding:8px 11px 0;display:flex;align-items:center;gap:8px}'
)

WIN = (
 header(ICON, 'Blends', 'Blend BOMs by origin, all bag sizes', '<span class="ch c-idle" id="bst">No blend open</span>')
 + '<div class="k3"><div class="k3l"><div class="cd bls" id="bls"></div><div class="cd bsub" id="bsub"></div></div>'
 '<div class="k3r"><div class="cd brec frm" id="brec"></div><div class="cd bcs" id="bcs"></div><div class="cd bhi" id="bhi"></div></div></div>'
)

JS = r'''
var FOC='.hd>*,.bls,.bsub,.brec,.bcs,.bhi';
/* origins: name, green lot, cost in cents per kg, color */
var OR={BR:['Brazil Cerrado','GL-4510',520,'#A16207'],CO:['Colombia Huila','GL-4502',640,'#52525B'],ET:['Ethiopia Guji','GL-4471',760,'#A1A1AA'],
HN:['Honduras Marcala','GL-4533',580,'#0F766E'],DC:['Colombia decaf','GL-4519',790,'#D4D4D8']};
var BL=[{n:'Foundry espresso',k:'House blend',m:[['BR',50],['CO',30],['ET',20]]},{n:'Daybreak roast',k:'Breakfast blend',m:[['CO',60],['BR',40]]},
{n:'Mesa decaf',k:'Decaf',m:[['DC',100]]},{n:'Ridgeline cold brew',k:'Cold brew blend',m:[['BR',70],['CO',30]]}];
/* green grams per bag (allows for roast loss) and bag plus label cost in cents */
var BAG=[['12 oz',400,38],['5 lb',2650,95]];
var TEST=5000,S;
function mix(b,sw){return b.m.map(function(x){return [sw&&x[0]==='BR'?'HN':x[0],x[1]];});}
function pctSum(m){return m.reduce(function(s,x){return s+x[1];},0);}
function cpk(m){return m.reduce(function(s,x){return s+x[1]*OR[x[0]][2];},0)/100;}
function bagC(m,i){return Math.round(BAG[i][1]*cpk(m)/1000+BAG[i][2]);}
function usd(c){return '$'+(c/100).toFixed(2);}
function kgs(g){return (g/1000).toFixed(1);}
function uses(){return BL.filter(function(b){return b.m.some(function(x){return x[0]==='BR';});});}
function sw(){return S.sw;}
function render(){
var L=$('bls'),U=uses();
L.innerHTML='<div class="ct"><span>Blends</span><span class="ch c-idle">'+BL.length+' BOMs</span></div>'+BL.map(function(b,i){var hit=S.sw&&U.indexOf(b)>=0;return '<button type="button" class="row'+(S.open&&i===0?' sel':'')+(hit?' hit':'')+'" id="bl'+i+'"><span class="bnm"><b>'+b.n+'</b><small>'+mix(b,S.sw).map(function(x){return OR[x[0]][0].split(' ')[0]+' '+x[1]+'%';}).join(', ')+'</small></span><span class="ch '+(hit?'c-warn':'c-idle')+'">'+(hit?(S.saved?'v2':'Updated'):'v1')+'</span></button>';}).join('');
var B=BL[0],m=mix(B,S.sw),R=$('brec');
if(!S.open)R.innerHTML='<div class="ct"><span>Blend BOM</span></div><div class="empt"><b>No blend open</b><span>Pick a blend to see its origins, percentages and batch quantities.</span></div>';
else R.innerHTML='<div class="ct"><span>'+B.n+', '+B.k.toLowerCase()+'</span><span class="ch '+(S.saved?'c-ok':S.sw?'c-warn':'c-idle')+'">'+(S.saved?'v2 saved':S.sw?'v2 draft':'v1')+'</span></div>'
+'<div class="bfm"><label class="fld" id="bfl"><small>Resize to, kg</small><input id="bsz" value="'+(S.typed)+'" inputmode="numeric" autocomplete="off" aria-label="Batch size in kilograms"><span class="em" id="bem">Enter 1 to 200 kg</span></label><button type="button" class="bt'+(S.g===TEST?' pri':'')+'" id="brz">Resize</button><span class="note" id="bnt">'+'Now: '+(S.g===TEST?'test roast':'production batch')+', '+kgs(S.g)+' kg</span></div>'
+'<div class="mix">'+m.map(function(x){return '<i style="width:'+x[1]+'%;background:'+OR[x[0]][3]+'"></i>';}).join('')+'</div>'
+'<div class="bom"><div class="row h"><span>Origin</span><span>Green lot</span><span>Share</span><span>Batch kg</span></div>'+m.map(function(x,i){return '<div class="row'+(S.sw&&x[0]==='HN'?' sw':'')+'"><span class="bo"><i style="background:'+OR[x[0]][3]+'"></i>'+OR[x[0]][0]+'</span><span>'+OR[x[0]][1]+'</span><span id="bp'+i+'">'+x[1]+'%</span><span id="bk'+i+'">'+kgs(S.g*x[1]/100)+'</span></div>';}).join('')
+'<div class="row tot"><span>Total</span><span></span><span id="bpt">'+pctSum(m)+'%</span><span id="bkt">'+kgs(m.reduce(function(s,x){return s+S.g*x[1]/100;},0))+'</span></div></div>';
var W=$('bsub');
if(!S.rs)W.innerHTML='<div class="ct"><span>Substitution</span></div><div class="empt"><b>No swaps pending</b><span>When a green lot runs out, swap it in every blend at once.</span></div>';
else if(!S.sw)W.innerHTML='<div class="ct"><span>Substitution</span><span class="ch c-bad">Running out</span></div><div class="sal"><b>GL-4510</b> Brazil Cerrado has 1 bag left. '+U.length+' blends use it.</div><div class="sal ok" style="margin-top:6px">Suggested: <b>GL-4533</b> Honduras Marcala, 32 bags on hand.</div><div class="sbt"><button type="button" class="bt pri" id="bsw">Swap Brazil for Honduras</button></div>';
else W.innerHTML='<div class="ct"><span>Substitution</span><span class="ch c-ok">Applied</span></div><div class="sal ok">Honduras Marcala replaces Brazil Cerrado in <b id="bsn">'+U.length+'</b> blends and <b id="bsb">'+U.length*BAG.length+'</b> bag sizes.</div><div class="row hd2"><span>Blend</span><span>Honduras share</span></div>'+U.map(function(b,i){var x=b.m.filter(function(y){return y[0]==='BR';})[0];return '<div class="row"><span>'+b.n+'</span><span class="mono" id="bu'+i+'">'+x[1]+'%</span></div>';}).join('');
var C=$('bcs'),old=mix(B,false),nw=mix(B,true);
if(!S.sw)C.innerHTML='<div class="ct"><span>Cost per bag</span></div><div class="empt"><b>No change to cost</b><span>Swap an origin to see cost per bag before you save.</span></div>';
else if(!S.cost)C.innerHTML='<div class="ct"><span>Cost per bag</span><button type="button" class="bt pri" id="bcp">Show cost per bag</button></div><div class="empt"><b>Draft not costed</b><span>Green cost at '+usd(cpk(old))+' per kg before the swap.</span></div>';
else C.innerHTML='<div class="ct"><span>Cost per bag, '+B.n+'</span><span class="mut" style="font-weight:400;font-size:9px" id="bck">Green '+usd(cpk(old))+' to '+usd(cpk(nw))+' per kg</span></div><div class="cg">'+BAG.map(function(g,i){var a=bagC(old,i),z=bagC(nw,i);return '<div class="cb"><small>'+g[0]+' bag</small><span class="vv"><s id="bco'+i+'">'+usd(a)+'</s><b id="bcn'+i+'">'+usd(z)+'</b></span><span class="dl" id="bcd'+i+'">+'+usd(z-a)+' per bag</span></div>';}).join('')+'</div>';
var H=$('bhi');
if(!S.open)H.innerHTML='<div class="ct"><span>Versions</span></div><div class="empt"><b>No history yet</b><span>Every saved version of the BOM is kept here.</span></div>';
else H.innerHTML='<div class="ct"><span>Versions</span>'+(S.saved?'<span class="ch c-ok">2 versions</span>':'')+'</div><div class="row h"><span>Ver</span><span>Change</span><span>Date</span><span>Status</span></div>'
+(S.saved?'<div class="row cur"><span class="mono">v2</span><span>Honduras Marcala for Brazil Cerrado</span><span>Nov 18</span><span class="ch c-ok" id="bv2">Current</span></div>':'')
+'<div class="row"><span class="mono">v1</span><span>Brazil 50, Colombia 30, Ethiopia 20</span><span>Nov 2</span><span class="ch '+(S.saved?'c-idle':'c-ok')+'" id="bv1">'+(S.saved?'Kept for reference':'Current')+'</span></div>'
+(S.cost&&!S.saved?'<div class="hbt"><button type="button" class="bt pri" id="bsv">Save as v2</button><span class="mut" style="font-size:8.8px">v1 stays for reference</span></div>':'');
var st=$('bst');st.textContent=S.saved?'v2 saved':S.sw?'Swap drafted':S.open?'Blend open':'No blend open';st.className='ch '+(S.saved?'c-ok':S.sw?'c-warn':S.open?'c-info':'c-idle');}
function szVal(){var e=$('bsz');if(!e)return NaN;var v=String(e.value).trim();return /^\d{1,3}$/.test(v)&&+v>=1&&+v<=200?(+v)*1000:NaN;}
winEl.addEventListener('input',function(e){if(e.target&&e.target.id==='bsz')S.typed=e.target.value;});
function typeIn(id,t,done){var i=0;(function k(){var e=$(id);if(e)e.value=t.slice(0,i);if(i<t.length){i++;later(k,90);}else done();})();}
function resetState(){S={open:false,g:TEST,typed:'120',rs:false,sw:false,cost:false,saved:false};render();}
var CAPAT=function(hh){return cur<=1||cur>=4?{l:14,t:visH()-hh-14}:{l:236,t:visH()-hh-14};};
var ST=[
{id:'open',target:function(){return $('bl0');},prompt:'Open the Foundry espresso house blend',where:'right',run:function(){S.open=true;render();},
 after:function(){var m=BL[0].m;return['A blend is a BOM by origin',BL[0].n+': '+m.map(function(x){return OR[x[0]][0].split(' ')[0]+' '+x[1]+'%';}).join(', ')+', '+pctSum(m)+'% in total.'];}},
{id:'size',target:function(){return $('brz');},prompt:'Resize to a 120 kg production batch',where:'below',
 ok:function(){var b=isNaN(szVal())||szVal()===TEST;var f=$('bfl');if(f)f.classList.toggle('err',b);return !b;},
 run:function(quick){var go=function(g){S.g=g;S.typed=String(g/1000);S.rs=true;render();};if(mode==='watch'&&!quick){var e=$('bsz');if(e)e.value='';typeIn('bsz','120',function(){go(120000);});S.g=120000;S.rs=true;}else go(quick?120000:szVal());},
 after:function(){var m=BL[0].m;return['From test roast to production',kgs(TEST)+' kg test roast to a '+kgs(S.g)+' kg batch: '+m.map(function(x){return kgs(S.g*x[1]/100)+' kg '+OR[x[0]][0].split(' ')[0];}).join(', ')+'.'];}},
{id:'swap',target:function(){return $('bsw');},prompt:'Swap Brazil for Honduras in every blend',where:'above',run:function(){S.sw=true;S.rs=true;render();},
 after:function(){var U=uses();return['One swap, every blend','Honduras Marcala replaces Brazil Cerrado in '+U.length+' blends and '+U.length*BAG.length+' bag sizes. Each blend still adds up to 100%.'];}},
{id:'cost',target:function(){return $('bcp');},prompt:'Show the cost per bag',where:'below',run:function(){S.cost=true;render();},
 after:function(){var o=mix(BL[0],false),n=mix(BL[0],true);return['Cost per bag before you save',BL[0].n+' '+BAG[0][0]+' goes from '+usd(bagC(o,0))+' to '+usd(bagC(n,0))+', '+BAG[1][0]+' from '+usd(bagC(o,1))+' to '+usd(bagC(n,1))+'.'];}},
{id:'save',target:function(){return $('bsv');},prompt:'Save the BOM as v2',where:'above',run:function(){S.saved=true;render();},
 after:function(){return['The earlier version stays','v2 with Honduras Marcala is current. v1 with Brazil Cerrado is kept for reference.'];}}];
'''
