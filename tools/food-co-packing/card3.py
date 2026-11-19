"""Food co-packing card 3: Cross Client Traceability.
Layout: stage chain. A vertical chain of four stage boxes (ingredient lot, runs, finished lots, shipments) with a running
total in each, a stage detail panel beside it and a recall scope panel split by brand.
Search a sesame seed lot, see the runs it fed for two brands, open a finished lot back to its ingredient lots, list the
shipments and customers by brand, and export the recall scope for one client. Every number is computed from the data."""
from frame_auto import header

SUMMARY = 'Cross Client Traceability (search an ingredient lot, see the runs it fed across brands, open a finished lot with its ingredient lots, list shipments and customers by brand, export a recall scope for one client)'
ARIA = 'Interactive product screen: sesame seed lot SE-3318 fed three runs for two brands, 2,800 cases in three finished lots, 2,200 shipped on four shipments, and the Brightfield Snacks recall scope exported'
STEPS = 5
STUDIO = dict(lede='A typical cross client trace, built on your Sutton data with Studio. Want it different? Describe the change.',
              examples=['Trace from a customer complaint', 'Email each brand its own scope', 'Add supplier certificates', 'Hold stock on site in one step'],
              built_on='Ingredient lots, runs, finished lots and shipments', change='Stages, columns and exports')

ICON = '<circle cx="4" cy="3.5" r="1.6"/><circle cx="4" cy="12.5" r="1.6"/><circle cx="12" cy="8" r="1.6"/><path d="M4 5.1v5.8M5.4 4.3l5.2 3M5.4 11.7l5.2-3"/>'

CSS = (
 '.c3{padding:10px 40px 0 16px;display:flex;flex-direction:column;gap:10px}'
 '.c3s{height:44px;flex:none;display:flex;align-items:center;gap:8px;padding:0 10px}.c3s .fld{flex-direction:row;align-items:center;gap:8px;position:relative}.c3s .fld small{font-size:10px;color:#18181B;font-weight:600;white-space:nowrap}'
 '#tin{width:150px;font-size:10.4px;padding:6px 8px}.c3s .fld .em{position:absolute;left:0;top:30px;white-space:nowrap;background:#fff;padding:1px 4px;z-index:3}'
 '.tsm{display:inline-flex;align-items:center;gap:5px;font-size:9.4px;color:#71717A}.tsm .bt{font-family:"JetBrains Mono",ui-monospace,monospace;font-size:9.6px;padding:4px 8px}'
 '.c3m{display:grid;grid-template-columns:200px 450px;gap:10px;height:482px;flex:none}'
 '.chn{display:flex;flex-direction:column;gap:0}.sg{position:relative;height:104px;flex:none;border:1px solid #E4E4E7;border-radius:8px;background:#fff;padding:9px 11px;display:flex;flex-direction:column;gap:3px;text-align:left;cursor:pointer;font:inherit;color:inherit;width:100%;transition:border-color .3s,background-color .3s}'
 '.sg:disabled{cursor:default}.sg .sn{display:flex;justify-content:space-between;font-size:9.2px;color:#71717A;font-weight:500}.sg .sv{font-family:"JetBrains Mono",ui-monospace,monospace;font-size:16px;font-weight:600;letter-spacing:-.01em;height:20px}'
 '.sg .ss{font-size:9px;color:#52525B;line-height:1.35}.sg.on{border-color:#18181B;box-shadow:0 0 0 1px #18181B}.sg.dn{background:#FAFAFA}.sg.fakehover{border-color:#A1A1AA}.sg:focus-visible{outline:2px solid #18181B;outline-offset:2px}'
 '.sg .sv:empty::before{content:"";display:inline-block;width:60px;height:14px;border-radius:4px;background:#F4F4F5;vertical-align:middle}'
 '.ar{height:22px;flex:none;display:grid;place-items:center;color:#A1A1AA}'
 '.c3r{display:flex;flex-direction:column;gap:8px;min-width:0}.tdt{height:290px;flex:none}.trs{flex:1 1 auto}.tdt .empt,.trs .empt{margin:8px 10px;height:calc(100% - 46px);padding:8px}'
 '.tdt .row{grid-template-columns:64px 1fr 92px 70px;min-height:30px;padding:0 11px;font-size:9.4px;gap:8px}.tdt .row>span:nth-child(3),.tdt .row>span:nth-child(4){text-align:right}.tdt .row.h{min-height:22px}'
 '.tdt .row.sel{background:#F4F4F5;box-shadow:inset 3px 0 0 #18181B}.tbk{margin:4px 11px 0 28px;border-left:2px solid #E4E4E7;padding:2px 0 2px 10px;font-size:9px;color:#52525B;line-height:1.55}.tbk b{font-family:"JetBrains Mono",ui-monospace,monospace;color:#18181B;font-weight:600}'
 '.tgh{padding:6px 11px 2px;font-size:9.2px;font-weight:600;color:#18181B;display:flex;justify-content:space-between}.tgh .mono{color:#52525B;font-weight:500}'
 '.trg{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;padding:10px 11px}.trg .kv small{font-size:8.6px}.trg .kv b{font-size:10.2px}'
 '.tb2{display:grid;grid-template-columns:130px 1fr 1fr 1fr;gap:6px;align-items:center;padding:5px 11px;font-size:9.4px}.tb2.h{font-size:8.6px;color:#71717A;padding-top:8px}.tb2 .mono{text-align:right;font-weight:600}.tb2.hit{background:#FFFBEB}'
 '.tex{display:flex;align-items:center;gap:8px;padding:8px 11px 0;font-size:9.2px;color:#52525B}.tex .mono{font-size:9px;color:#1E3A8A}'
)

WIN = (
 header(ICON, 'Lot trace', 'Ingredient lots across client brands', '<span class="ch c-idle" id="tst">No lot searched</span>')
 + '<div class="c3"><div class="cd c3s frm" id="tsf"><label class="fld" id="tfl"><small>Lot</small><input id="tin" value="" placeholder="Ingredient lot number" autocomplete="off" spellcheck="false" aria-label="Ingredient lot number"><span class="em" id="tem">No lot found. Try SE-3318</span></label>'
 '<button type="button" class="bt pri" id="tsb">Search</button><span class="tsm">Sample<button type="button" class="bt" id="tsm" data-sample>SE-3318</button></span></div>'
 '<div class="c3m"><div class="chn" id="chn"></div><div class="c3r"><div class="cd tdt" id="tdt"></div><div class="cd trs" id="trs"></div></div></div></div>'
)

JS = r'''
var FOC='.hd>*,.c3s>*,.sg,.tdt,.trs';
var BR={B:'Brightfield Snacks',O:'Oakline Foods'};
var LOT={id:'SE-3318',ing:'Sesame seed',g:2000000,sup:'Pinecrest Ingredients',rc:'Nov 3',own:'Plant purchased'};
var RUNS=[{id:'R-5202',b:'B',p:'Seeded crackers',g:600000,d:'Nov 5',fl:'FL-8802',cs:1200},{id:'R-5207',b:'O',p:'Sesame bars',g:450000,d:'Nov 7',fl:'FL-8807',cs:900},{id:'R-5211',b:'B',p:'Everything bagel chips',g:350000,d:'Nov 10',fl:'FL-8811',cs:700}];
var BACK={'FL-8807':[['SE-3318','Sesame seed',450000],['OF-2290','Oat flour',820000],['HN-1175','Honey',160000]]};
var SHP=[{id:'SH-4401',fl:'FL-8802',to:'Northgate Grocers',c:700,d:'Nov 8'},{id:'SH-4405',fl:'FL-8802',to:'Lakeside Market',c:500,d:'Nov 9'},{id:'SH-4409',fl:'FL-8807',to:'Northgate Grocers',c:600,d:'Nov 11'},{id:'SH-4412',fl:'FL-8811',to:'Pinewood Foodservice',c:400,d:'Nov 13'}];
var S;
function kg(g){return (g/1000).toLocaleString('en-US',{minimumFractionDigits:3,maximumFractionDigits:3});}
function sum(a,f){return a.reduce(function(s,x){return s+f(x);},0);}
function used(){return sum(RUNS,function(r){return r.g;});}
function made(rs){return sum(rs||RUNS,function(r){return r.cs;});}
function runOf(fl){return RUNS.filter(function(r){return r.fl===fl;})[0];}
function shipsOf(b){return SHP.filter(function(s){return !b||runOf(s.fl).b===b;});}
function shipped(b){return sum(shipsOf(b),function(s){return s.c;});}
function runsOf(b){return RUNS.filter(function(r){return r.b===b;});}
function custs(b){var o=[];shipsOf(b).forEach(function(s){if(o.indexOf(s.to)<0)o.push(s.to);});return o;}
function brands(){var o=[];RUNS.forEach(function(r){if(o.indexOf(r.b)<0)o.push(r.b);});return o;}
var chev='<svg width="12" height="12" viewBox="0 0 12 12" fill="none" aria-hidden="true"><path d="M3 4.5L6 7.5 9 4.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>';
function render(){
var st=[['Ingredient lot',S.lot?kg(LOT.g)+' kg':'',S.lot?(S.runs?kg(used())+' kg used, '+kg(LOT.g-used())+' kg on hand':LOT.ing+', received '+LOT.rc):'Search a lot to start'],
['Runs',S.runs?RUNS.length+' runs':'',S.runs?brands().length+' brands, '+kg(used())+' kg used':'Runs that used the lot'],
['Finished lots',S.fl?RUNS.length+' lots':'',S.fl?n0(made())+' cases made':'Lots those runs produced'],
['Shipments',S.sh?SHP.length+' shipments':'',S.sh?n0(shipped())+' cases shipped, '+n0(made()-shipped())+' on site':'Who received them']];
var lv=S.sh?3:S.fl?2:S.runs?1:S.lot?0:-1;
$('chn').innerHTML=st.map(function(x,i){return (i?'<div class="ar">'+chev+'</div>':'')+'<button type="button" class="sg'+(i===lv?' on':i<lv?' dn':'')+'" id="sg'+i+'"'+(S.lot&&i<=lv+1?'':' disabled')+'><span class="sn"><span>'+x[0]+'</span><span>'+(i+1)+' of 4</span></span><span class="sv" id="sv'+i+'">'+x[1]+'</span><span class="ss" id="ss'+i+'">'+x[2]+'</span></button>';}).join('');
var D=$('tdt'),h;
if(lv<0)h='<div class="ct"><span>Stage detail</span></div><div class="empt"><b>No lot searched</b><span>Start from an ingredient lot and follow it to every run, finished lot and customer.</span></div>';
else if(lv===0)h='<div class="ct"><span>'+LOT.id+' <span class="mut" style="font-weight:400">'+LOT.ing+'</span></span><span class="ch c-info">'+LOT.own+'</span></div><div class="trg">'+[['Supplier',LOT.sup],['Received',LOT.rc],['Quantity',kg(LOT.g)+' kg'],['Owner',LOT.own],['Location','Bay B4'],['Certificate','Attached']].map(function(x){return '<span class="kv"><small>'+x[0]+'</small><b>'+x[1]+'</b></span>';}).join('')+'</div>';
else if(lv===1)h='<div class="ct"><span>Runs that used '+LOT.id+'</span><span class="ch c-warn">'+brands().length+' brands</span></div><div class="row h"><span>Run</span><span>Brand and product</span><span>Sesame used</span><span>Date</span></div>'+RUNS.map(function(r,i){return '<div class="row"><span class="mono">'+r.id+'</span><span>'+BR[r.b]+', '+r.p+'</span><span class="mono" id="tu'+i+'">'+kg(r.g)+' kg</span><span>'+r.d+'</span></div>';}).join('');
else if(lv===2)h='<div class="ct"><span>Finished lots</span><span class="ch c-info">'+n0(made())+' cases</span></div><div class="row h"><span>Lot</span><span>Brand and product</span><span>Cases</span><span>From</span></div>'+RUNS.map(function(r,i){var o=r.fl==='FL-8807';return '<div class="row'+(o?' sel':'')+'"><span class="mono">'+r.fl+'</span><span>'+BR[r.b]+', '+r.p+'</span><span class="mono" id="tc'+i+'">'+n0(r.cs)+'</span><span class="mono">'+r.id+'</span></div>'+(o?'<div class="tbk" id="tbk">Back to ingredient lots: '+BACK[r.fl].map(function(b){return '<b>'+b[0]+'</b> '+b[1].toLowerCase()+' '+kg(b[2])+' kg';}).join(', ')+'</div>':'');}).join('');
else h='<div class="ct"><span>Shipments and customers by brand</span><span class="ch c-warn">'+n0(shipped())+' cases shipped</span></div>'+brands().map(function(b){return '<div class="tgh"><span>'+BR[b]+'</span><span class="mono" id="tgs'+b+'">'+n0(shipped(b))+' of '+n0(made(runsOf(b)))+' cases</span></div>'+shipsOf(b).map(function(s){return '<div class="row"><span class="mono">'+s.id+'</span><span>'+s.to+', '+s.fl+'</span><span class="mono">'+n0(s.c)+'</span><span>'+s.d+'</span></div>';}).join('');}).join('');
D.innerHTML=h;
var R=$('trs');
if(!S.sh)R.innerHTML='<div class="ct"><span>Recall scope</span></div><div class="empt"><b>No scope yet</b><span>Trace to shipments to see the scope for each client brand.</span></div>';
else R.innerHTML='<div class="ct"><span>Recall scope by brand</span>'+(S.ex?'<span class="ch c-ok" id="tex">Exported</span>':'<button type="button" class="bt pri" id="txb">Export Brightfield Snacks scope</button>')+'</div><div class="tb2 h"><span>Brand</span><span class="r">Made</span><span class="r">Shipped</span><span class="r">On site</span></div>'
+brands().map(function(b){var m=made(runsOf(b)),s=shipped(b);return '<div class="tb2'+(S.ex&&b==='B'?' hit':'')+'"><span>'+BR[b]+'</span><span class="mono">'+n0(m)+'</span><span class="mono" id="tsh'+b+'">'+n0(s)+'</span><span class="mono" id="tos'+b+'">'+n0(m-s)+'</span></div>';}).join('')
+(S.ex?'<div class="tex" id="txs">Brightfield Snacks: '+runsOf('B').length+' runs, '+runsOf('B').length+' finished lots, '+n0(made(runsOf('B')))+' cases, '+n0(shipped('B'))+' shipped to '+custs('B').length+' customers. <span class="mono">SE-3318 Brightfield scope.csv</span></div>':'<div class="tex">The export lists runs, lots, shipments and customers for one brand only.</div>');
var t=$('tst');t.textContent=S.ex?'Scope exported':S.lot?LOT.id+' traced':'No lot searched';t.className='ch '+(S.ex?'c-ok':S.lot?'c-warn':'c-idle');}
function val(){return String($('tin').value).trim().toUpperCase().replace(/\s/g,'');}
$('tsm').addEventListener('click',function(){$('tin').value=LOT.id;$('tfl').classList.remove('err');});
function typeLot(done){var t=LOT.id,i=0;(function k(){$('tin').value=t.slice(0,i);if(i<t.length){i++;later(k,70);}else done();})();}
function resetState(){S={lot:false,runs:false,fl:false,sh:false,ex:false};$('tin').value='';$('tfl').classList.remove('err');render();}
var CAPAT=function(hh){return cur<=1?{l:14,t:visH()-hh-14}:{l:226,t:visH()-hh-14};};
var ST=[
{id:'lot',target:function(){return mode==='try'?$('tsb'):$('tin');},prompt:'Click Search to find lot SE-3318',where:'below',
 ok:function(){if(!val())$('tin').value='SE-3318';var v=val(),b=!(v==='SE-3318'||v==='SE3318');$('tem').textContent=v?'No lot found. Try SE-3318':'Enter a lot, for example SE-3318';$('tfl').classList.toggle('err',b);return !b;},
 run:function(quick){var go=function(){$('tin').value=LOT.id;$('tfl').classList.remove('err');S.lot=true;render();};if(mode==='watch'&&!quick)typeLot(go);else go();},
 after:function(){return['Search an ingredient lot',LOT.id+', '+LOT.ing.toLowerCase()+', '+kg(LOT.g)+' kg from '+LOT.sup+', received '+LOT.rc+'.'];}},
{id:'runs',target:function(){return $('sg1');},prompt:'Open the Runs stage',where:'right',run:function(){S.runs=true;render();},
 after:function(){return['One lot, runs for more than one brand',RUNS.length+' runs for '+brands().map(function(b){return BR[b];}).join(' and ')+' used '+kg(used())+' kg. '+kg(LOT.g-used())+' kg is still on hand.'];}},
{id:'fl',target:function(){return $('sg2');},prompt:'Open the Finished lots stage',where:'right',run:function(){S.fl=true;render();},
 after:function(){return['Open a finished lot back to its ingredients','FL-8807 sesame bars for Oakline Foods came from SE-3318 and two other lots. '+n0(made())+' cases across '+RUNS.length+' finished lots.'];}},
{id:'sh',target:function(){return $('sg3');},prompt:'Open the Shipments stage',where:'right',run:function(){S.sh=true;render();},
 after:function(){return['Shipments and customers by brand',SHP.length+' shipments, '+n0(shipped())+' cases to '+custs().length+' customers. '+n0(made()-shipped())+' cases are still on site.'];}},
{id:'ex',target:function(){return $('txb');},prompt:'Export the Brightfield Snacks scope',where:'above',run:function(){S.ex=true;render();},
 after:function(){return['Export the recall scope for one client','Brightfield Snacks only: '+n0(made(runsOf('B')))+' cases, '+n0(shipped('B'))+' shipped to '+custs('B').length+' customers, '+n0(made(runsOf('B'))-shipped('B'))+' on site.'];}}];
'''
