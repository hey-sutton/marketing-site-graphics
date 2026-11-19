"""Sauce manufacturing card 4: Ingredient Lots & Allergen Control. Layout: a board.
Top: the read only ingredient lot field with Search. Middle: four columns the trace fills by click (the lot, the
batches that used it, the filled lots they made, the customers who received them). Bottom left: the allergen roll up
from ingredients through the base sauce and flavored sauce to the jar's Contains statement (the union of ingredient
allergens). Bottom right: the Kettle K-2 run order, where the next batch is checked against the previous allergen set
and a cleaning card is moved onto the board when the set changes."""
from frame_auto import header

SUMMARY = 'Ingredient Lots & Allergen Control (search spice lot SP-LOT-5530, trace 3 batches and 5 filled lots to 4 customers, roll soy and sesame up to the jar, check the peanut batch and log the cleaning)'
ARIA = 'Interactive product screen: search an ingredient lot, see every batch and filled lot that used it, list the customers who received them, roll the allergen flags up to the finished jar, and check the next batch against the previous allergen set and log the cleaning'
STEPS = 5
STUDIO = dict(lede='A typical lot and allergen screen on your Sutton data. Want it different? Describe the change.',
              examples=['A may contain line per plant', 'A swab result on each cleaning', 'Runs sorted by allergen set', 'A customer notice per lot'],
              built_on='Lots, BOMs, batches and shipments', change='Columns, allergens and views')

ICON = '<circle cx="7" cy="7" r="4.2"/><path d="M10.2 10.2L14 14"/>'

CSS = (
 '.fld input[readonly]{background:#F4F4F5;color:#3F3F46;cursor:default;pointer-events:none}'
 '.g4{display:grid;grid-template-rows:62px 248px 210px;gap:10px;padding:10px 44px 0 16px;width:716px}'
 '.sr2{display:flex;flex-direction:column;justify-content:center;gap:5px;padding:0 12px}.sr2 .frm{display:flex;align-items:flex-end;gap:8px}.sr2 .fld{width:170px}.sr2 .ctx{font-size:8.9px;color:#71717A}.sr2 .rs{margin-left:auto}'
 '.brd{display:grid;grid-template-columns:146px 150px 160px 170px;gap:10px}.col{display:flex;flex-direction:column;min-width:0}.col>.empt{margin:8px;flex:1;padding:10px}.col .ct .bt{font-size:9px;padding:2px 8px}'
 '.cds{display:flex;flex-direction:column;gap:5px;padding:7px}'
 '.k{border:1px solid #E4E4E7;border-radius:6px;padding:5px 7px;font-size:9px;line-height:1.35;background:#fff}.k b{font-family:"JetBrains Mono",ui-monospace,monospace;font-size:9.6px}.k small{display:block;color:#71717A;font-size:8.3px}'
 '.k.l{background:#FFFBEB;border-color:#FDE68A}.k .alg{display:flex;gap:3px;flex-wrap:wrap;margin-top:3px}'
 '.c-alg{background:#FEF3C7;color:#92400E}.c-new{background:#FEE2E2;color:#991B1B}'
 '.bot{display:grid;grid-template-columns:1fr 1fr;gap:10px}.bc{display:flex;flex-direction:column}.bc .ct .bt{font-size:9.2px;padding:3px 8px}'
 '.ru .row{grid-template-columns:86px 1fr auto;font-size:9.2px;min-height:30px;padding:0 9px}.ru .row small{display:block;font-size:8.2px;color:#71717A}.ru .row .alg{display:flex;gap:3px;justify-content:flex-end}'
 '.ru .row.on{background:#FFFBEB}.ctn{margin:7px 9px 0;padding:6px 8px;border-radius:6px;background:#FAFAFA;border:1px solid #F0F0F1;font-size:9.2px}.ctn.on{background:#FEF3C7;border-color:#FDE68A;color:#92400E;font-weight:600}'
 '.rn{display:flex;flex-direction:column;gap:6px;padding:7px 9px}.rk{border:1px solid #E4E4E7;border-radius:7px;padding:6px 8px;font-size:9.2px;display:grid;grid-template-columns:1fr auto;gap:3px 6px;align-items:center}.rk small{font-size:8.3px;color:#71717A}.rk .alg{grid-column:1/3;display:flex;gap:3px}'
 '.rk.cl{background:#F0FDF4;border-color:#BBF7D0}.rk.nx{border-style:dashed}.wn{margin:0 9px;padding:6px 8px;border-radius:6px;font-size:9px;line-height:1.4}.wn.w{background:#FEF2F2;border:1px solid #FECACA;color:#991B1B}.wn.g{background:#F0FDF4;border:1px solid #BBF7D0;color:#166534}'
 '.ft{margin-top:auto;padding:7px 10px;border-top:1px solid #F0F0F1;font-size:8.6px;color:#71717A;background:#FAFAFA}.acts{display:flex;gap:6px;padding:6px 9px 0}.acts .bt{font-size:9.2px;padding:3px 9px}'
)

WIN = (
 header(ICON, 'Lots and allergens', 'Ingredient lots traced forward, allergens rolled up to the jar')
 + '<div class="g4"><div class="cd sr2"><div class="frm"><label class="fld"><small>Ingredient lot</small>'
 '<input id="ilt" value="SP-LOT-5530" readonly tabindex="-1" autocomplete="off" spellcheck="false"></label>'
 '<button type="button" class="bt pri" id="srb">Search</button><span class="rs" id="rs"></span></div><div class="ctx">Sesame spice blend, received from Corvale Spice Co.</div></div>'
 '<div class="brd" id="brd"></div><div class="bot"><div class="cd bc ru" id="ru"></div><div class="cd bc" id="rn"></div></div></div>'
)

JS = r'''
var FOC='.hd>*,.sr2 .fld,.sr2 .ctx,#srb,.col>.ct,.col .k,.col>.empt,.bc>.ct,.bc>*:not(.ct)';
var LOT={id:'SP-LOT-5530',nm:'Sesame spice blend',alg:['sesame']};
var BAT=[['SP-2283','Teriyaki base','Nov 4'],['SP-2286','Teriyaki base','Nov 11'],['SP-2291','Teriyaki base','Nov 18']];
var FLS=[['FL-9088','SP-2283','Original, 12 oz','Harbor Market Co.'],['FL-9089','SP-2283','Spicy, 12 oz','Pine Street Co-op'],['FL-9094','SP-2286','Original, 32 oz','Harbor Market Co.'],['FL-9095','SP-2286','Spicy, 12 oz','Northway Foods'],['FL-9101','SP-2291','Original, 12 oz','Elm Grove Grocers']];
var ING=[['Soy sauce','SY-6120',['soy']],[LOT.nm,LOT.id,LOT.alg],['Rice vinegar','RV-3307',[]],['Brown sugar syrup','BS-1180',[]]];
var PREV={id:'SP-2295',nm:'Spicy teriyaki',alg:null},NEXT={id:'SP-2296',nm:'Peanut satay',add:['peanut']};
var S;
function uniq(a){var o=[];a.forEach(function(x){if(o.indexOf(x)<0)o.push(x);});return o;}
function contains(){return uniq(ING.reduce(function(a,i){return a.concat(i[2]);},[])).sort();}
function nextSet(){return uniq(contains().concat(NEXT.add)).sort();}
function differs(a,b){return a.slice().sort().join()!==b.slice().sort().join();}
function custs(){return uniq(FLS.map(function(f){return f[3];}));}
function ach(a,cls){return a.map(function(x){return '<span class="ch '+(cls||'c-alg')+'">'+x+'</span>';}).join('');}
function cap1(x){return x.charAt(0).toUpperCase()+x.slice(1);}
function render(){
var sb=$('srb');sb.className='bt '+(S.sr?'done':'pri');sb.textContent=S.sr?'Found':'Search';
$('rs').innerHTML=S.sr?'<span class="ch c-info in">'+(S.tr?BAT.length+' batches, '+FLS.length+' filled lots':'Lot found')+(S.cu?', '+custs().length+' customers':'')+'</span>':'';
var c=[];
c.push('<div class="cd col"><div class="ct"><span>Lot</span>'+(S.sr&&!S.tr?'<button type="button" class="bt pri" id="tfb">Trace</button>':'')+'</div>'+(S.sr?'<div class="cds"><div class="k l in"><b>'+LOT.id+'</b><small>'+LOT.nm+'</small><small>Received Oct 28, 220 lb</small><div class="alg">'+ach(LOT.alg)+'</div></div><div class="k in"><b>CoA</b><small>Attached at receiving</small></div></div>':'<div class="empt"><span>Search a lot to start the trace.</span></div>')+'</div>');
c.push('<div class="cd col"><div class="ct"><span>Batches</span>'+(S.tr?'<span class="ch c-idle" id="nb">'+BAT.length+'</span>':'')+'</div>'+(S.tr?'<div class="cds">'+BAT.map(function(b){return '<div class="k in" id="b-'+b[0]+'"><b>'+b[0]+'</b><small>'+b[1]+', '+b[2]+'</small></div>';}).join('')+'</div>':'<div class="empt"><span>Batches that used the lot.</span></div>')+'</div>');
c.push('<div class="cd col"><div class="ct"><span>Filled lots</span>'+(S.tr?'<span class="ch c-idle" id="nf">'+FLS.length+'</span>':'')+'</div>'+(S.tr?'<div class="cds">'+FLS.map(function(f){return '<div class="k in" id="f-'+f[0]+'"><b>'+f[0]+'</b><small>'+f[2]+', from '+f[1]+'</small></div>';}).join('')+'</div>':'<div class="empt"><span>Filled lots made from those batches.</span></div>')+'</div>');
c.push('<div class="cd col"><div class="ct"><span>Customers</span>'+(S.cu?'<span class="ch c-idle" id="nc">'+custs().length+'</span>':S.tr?'<button type="button" class="bt" id="cub">Customers</button>':'')+'</div>'+(S.cu?'<div class="cds">'+custs().map(function(c){var l=FLS.filter(function(f){return f[3]===c;}).map(function(f){return f[0];});return '<div class="k in cu"><b style="font-family:inherit">'+c+'</b><small>'+l.join(', ')+'</small></div>';}).join('')+'</div>':'<div class="empt"><span>Who received the filled lots.</span></div>')+'</div>');
$('brd').innerHTML=c.join('');
var u='<div class="ct"><span>Allergen roll up, TB-100</span>'+(S.ru?'<span class="ch c-ok">Rolled up</span>':S.sr?'<button type="button" class="bt" id="rub">Roll up</button>':'')+'</div>';
if(!S.sr)u+='<div class="empt" style="margin:8px;flex:1"><span>Allergens for the formula that used the lot show here.</span></div>';
else{var C=contains();u+='<div class="row in"><span>Ingredients</span><span>'+ING.filter(function(i){return i[2].length;}).map(function(i){return i[0];}).join(', ')+'<small>'+ING.length+' lines, '+ING.filter(function(i){return !i[2].length;}).length+' with none</small></span><span class="alg">'+ach(C)+'</span></div>'+
[['Base sauce','TB-100 teriyaki base'],['Flavored sauce','Spicy teriyaki'],['Jar','Spicy teriyaki, 12 oz']].map(function(l,i){return '<div class="row'+(S.ru?' on in':'')+'"><span>'+l[0]+'</span><span>'+l[1]+'</span><span class="alg" id="ra-'+i+'">'+(S.ru?ach(C):'<span class="ch c-idle">Not rolled up</span>')+'</span></div>';}).join('')+
'<div class="ctn'+(S.ru?' on':'')+'" id="ctn">'+(S.ru?'Contains: '+C.map(cap1).join(', '):'Label Contains statement waits for the roll up.')+'</div>';}
u+='<div class="ft">Flags roll up through every level of the BOM.</div>';
$('ru').innerHTML=u;
var C2=contains(),N=nextSet(),d=differs(C2,N);
var r='<div class="ct"><span>Kettle K-2 run order</span>'+(S.cl?'<span class="ch c-ok">Cleared</span>':'')+'</div><div class="rn">'+
'<div class="rk"><span><b class="mono">'+PREV.id+'</b> '+PREV.nm+'</span><span class="ch c-ok">Done</span><span class="alg">'+ach(C2)+'</span></div>'+
(S.cl?'<div class="rk cl in" id="clk"><span><b>Cleaning</b> <small>Wash, rinse and sanitize, logged 2:10 pm</small></span><span class="ch c-ok">Logged</span></div>':'')+
'<div class="rk nx"><span><b class="mono">'+NEXT.id+'</b> '+NEXT.nm+'</span><span class="ch '+(S.cl?'c-ok':S.nc?'c-bad':'c-idle')+'">'+(S.cl?'Cleared to run':S.nc?'Cleaning required':'Next')+'</span><span class="alg">'+(S.nc?N.map(function(x){return '<span class="ch '+(C2.indexOf(x)<0?'c-new':'c-alg')+'">'+x+'</span>';}).join(''):'<span class="ch c-idle">Not checked</span>')+'</span></div></div>';
if(S.nc&&!S.cl)r+=d?'<div class="wn w in" id="wn">Allergen set changes: adds '+N.filter(function(x){return C2.indexOf(x)<0;}).join(', ')+'. Log a cleaning before '+NEXT.id+'.</div>':'<div class="wn g in" id="wn">Same allergen set. No cleaning needed.</div>';
if(!S.cl&&S.ru)r+='<div class="acts">'+(S.nc?'':'<button type="button" class="bt" id="ncb" data-pick="1">Check next batch</button>')+(S.nc&&d?'<button type="button" class="bt pri" id="lcb">Log cleaning</button>':'')+'</div>';
r+='<div class="ft">Cleanings logged between allergen changes.</div>';
$('rn').innerHTML=r;
}
function resetState(){S={sr:false,tr:false,cu:false,ru:false,nc:false,cl:false};render();}
winEl.addEventListener('click',function(e){var b=e.target.closest&&e.target.closest('#ncb');if(b&&S.ru&&!S.nc){S.nc=true;render();}});
function capN(){var i=cap.querySelector('.m i');return i?+i.textContent:1;}
var CAPAT=function(hh){var w=cap.offsetWidth;return capN()>=4?{l:visW()-w-14,t:60}:{l:visW()-w-14,t:visH()-hh-14};};
var ST=[
{id:'sr',target:function(){return $('srb');},prompt:'Search SP-LOT-5530',where:'below',run:function(){S.sr=true;render();},
 after:function(){return['One ingredient lot','SP-LOT-5530, sesame spice blend. Its allergen flag: '+LOT.alg.join(', ')+'.'];}},
{id:'tr',target:function(){return $('tfb');},prompt:'Trace the lot forward',where:'below',run:function(){S.tr=true;render();},
 after:function(){return['Every batch and filled lot that used it',BAT.length+' batches made '+FLS.length+' filled lots: '+FLS.map(function(f){return f[0];}).join(', ')+'.'];}},
{id:'cu',target:function(){return $('cub');},prompt:'List the customers',where:'below',run:function(){S.cu=true;render();},
 after:function(){return['The customers who received those lots',custs().length+' customers: '+custs().join(', ')+'.'];}},
{id:'ru',target:function(){return $('rub');},prompt:'Roll up the allergens',where:'below',run:function(){S.ru=true;render();},
 after:function(){return['Allergens roll up to the finished jar','Soy from the soy sauce and sesame from SP-LOT-5530 reach the jar: Contains '+contains().join(', ')+'.'];}},
{id:'cl',target:function(){return $('lcb');},back:function(){return S.nc?null:[$('ncb'),'Check the next batch','above'];},prompt:'Log the cleaning',where:'above',
 run:function(){S.nc=true;S.cl=true;render();},
 after:function(){return['A changed allergen set needs a cleaning',NEXT.id+' adds peanut, so the cleaning is logged before it runs.'];}}];
'''
