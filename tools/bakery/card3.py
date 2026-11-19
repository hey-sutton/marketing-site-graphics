"""Bakery card 3: Lot Trace & Allergen Response.
Layout: a search field on top, an allergen grid (four products by four allergens) with a batch strip under it, recipient
cards on the right (one per customer) and a hold panel along the bottom.
A supplier flags almond flour lot AF-1042: search it, see which products carry tree nut from it, which batches used it,
who received them, and hold what is still on site. Every number is computed from the data arrays below."""
from frame_auto import header

SUMMARY = 'Lot Trace & Allergen Response (search a flagged almond flour lot, light up the tree nut cells in the allergen grid, find the batches and the customers who received them, hold the stock still on site)'
ARIA = 'Interactive product screen: search almond flour lot AF-1042, see tree nut on Almond Croissant and Almond Cookie, batches B-4411 and B-4420, 280 cases shipped to two customers, then hold the 70 cases and 50.000 kg still on site'
STEPS = 5
STUDIO = dict(lede='A typical lot trace and allergen view, built on your Sutton data with Studio. Want it different? Describe the change.',
              examples=['Add sesame and soy columns', 'Draft a notice to each customer', 'Search by product lot', 'Hold stock at every shop too'],
              built_on='Ingredient lots, BOMs, batches and shipments', change='Columns, holds and notices')

ICON = '<circle cx="7" cy="7" r="4.2"/><path d="M10.2 10.2L13.5 13.5"/><path d="M5.2 7h3.6M7 5.2v3.6"/>'

CSS = (
 '.k3{padding:10px 40px 0 16px;display:flex;flex-direction:column;gap:10px}'
 '.k3s{height:72px;flex:none;padding:0 10px}.k3r{height:40px;display:flex;align-items:center;gap:8px}.k3s .fld{flex-direction:row;align-items:center;gap:8px;position:relative}.k3s .fld small{font-size:10px;color:#18181B;font-weight:600;white-space:nowrap}'
 '#kli{width:178px;font-size:10.4px;padding:6px 8px}.k3s .fld .em{position:absolute;left:0;top:30px;white-space:nowrap;background:#fff;padding:1px 4px;z-index:3}'
 '.k3sm{display:inline-flex;align-items:center;gap:5px;font-size:9.4px;color:#71717A}.k3sm .bt{font-family:"JetBrains Mono",ui-monospace,monospace;font-size:9.6px;padding:4px 8px}'
 '.k3h{height:28px;border-top:1px solid #F0F0F1;display:flex;align-items:center;gap:14px;font-size:9.6px;color:#52525B;white-space:nowrap;overflow:hidden}.k3h b{color:#18181B;font-weight:600}.k3h .mono{font-weight:600;color:#18181B}'
 '.k3m{display:grid;grid-template-columns:380px 270px;gap:10px;height:330px;flex:none}.k3l{display:flex;flex-direction:column;gap:10px;min-width:0}'
 '.kag{height:190px;flex:none}.kag .ct .mut{font-weight:400}'
 '.kgr{display:grid;grid-template-columns:1fr repeat(4,58px);column-gap:6px;padding:0 11px}.kgr>span{height:30px;display:flex;align-items:center;font-size:9.8px;border-top:1px solid #F4F4F5;transition:opacity .35s ease}'
 '.kgr>span.kh{height:24px;font-size:8.8px;color:#71717A;font-weight:500;border-top:0;justify-content:center}.kgr>span.kh:first-child{justify-content:flex-start}.kgr>span.kp{font-weight:500}'
 '.kgr>span.kc{justify-content:center}.kgr i{display:grid;place-items:center;width:46px;height:20px;border-radius:5px;background:#FAFAFA;border:1px solid #F0F0F1;font-style:normal;font-size:8.4px;color:#71717A;transition:background-color .35s,border-color .35s,color .35s}'
 '.kgr i.kyes{background:#F4F4F5;border-color:#E4E4E7;color:#3F3F46}.kgr i.klit{background:#FEF3C7;border-color:#F59E0B;color:#92400E;font-weight:600;box-shadow:0 0 0 2px rgba(245,158,11,.18)}.kgr>span.kdim{opacity:.35}'
 '.kbs{flex:1 1 auto}.kbs .empt,.kag .empt{margin:8px 10px;height:calc(100% - 46px);padding:8px}'
 '.kbt{display:grid;grid-template-columns:1fr 1fr;gap:8px;padding:8px 11px 0}.kbx{border:1px solid #F0F0F1;border-radius:7px;background:#FAFAFA;padding:6px 9px;display:flex;flex-direction:column;gap:2px;font-size:9.2px}'
 '.kbx .kbh{display:flex;justify-content:space-between;align-items:center}.kbx .mono{font-weight:600;font-size:10px}.kbx .mut{font-size:8.8px}.kbx .kbq{font-family:"JetBrains Mono",ui-monospace,monospace;font-size:9.4px}'
 '.kbf{padding:7px 11px 0;font-size:9.6px;color:#52525B}.kbf b{font-family:"JetBrains Mono",ui-monospace,monospace;color:#18181B}'
 '.krc .empt{margin:8px 10px;height:280px}.krl{padding:8px 11px 0;display:flex;flex-direction:column;gap:8px}'
 '.kcu{border:1px solid #E4E4E7;border-radius:7px;overflow:hidden}.kcu .kch{display:flex;justify-content:space-between;align-items:center;height:28px;padding:0 9px;background:#FAFAFA;border-bottom:1px solid #F0F0F1;font-size:10px;font-weight:600}.kcu .kch .mono{font-size:10.4px}'
 '.kcu .row{grid-template-columns:62px 50px 1fr 54px;min-height:22px;padding:0 9px;font-size:9.2px;gap:6px}.kcu .row>span:last-child{text-align:right}'
 '.kos{border:1px dashed #E4E4E7;border-radius:7px;padding:6px 9px;font-size:9.4px;color:#52525B;display:flex;justify-content:space-between;align-items:center}.kos b{font-family:"JetBrains Mono",ui-monospace,monospace;color:#18181B}'
 '.ksum{padding:2px 2px 0;font-size:9.8px;font-weight:600}'
 '.khp{height:124px;flex:none}.khp .empt{margin:8px 10px;height:74px;padding:8px}.khb{display:grid;grid-template-columns:420px 1fr;gap:12px;padding:6px 11px 0}'
 '.khb .row{grid-template-columns:62px 1fr 74px 50px;min-height:22px;padding:0 4px;font-size:9.4px;gap:6px}.khb .row>span:nth-child(3){text-align:right}.khb .row>span:last-child{text-align:right}'
 '.khs{display:flex;flex-direction:column;gap:2px;font-size:9.2px;color:#71717A;padding-top:0}.khs b{font-family:"JetBrains Mono",ui-monospace,monospace;font-size:14px;color:#B91C1C;font-weight:600}'
)

WIN = (
 header(ICON, 'Lot trace', 'Ingredient lots, allergens and recipients', '<span class="ch c-idle" id="kst">No lot searched</span>')
 + '<div class="k3"><div class="cd k3s"><div class="k3r frm" id="ksf"><label class="fld" id="kfl"><small>Lot</small><input id="kli" value="" placeholder="Ingredient lot or product lot" autocomplete="off" spellcheck="false" aria-label="Ingredient lot or product lot"><span class="em" id="kle">No lot found. Try AF-1042</span></label>'
 '<button type="button" class="bt pri" id="ksb">Search</button><span class="k3sm">Sample<button type="button" class="bt" id="ksm" data-sample>AF-1042</button></span></div>'
 '<div class="k3h" id="k3h"></div></div>'
 '<div class="k3m"><div class="k3l"><div class="cd kag" id="kag"></div><div class="cd kbs" id="kbs"></div></div><div class="cd krc" id="krc"></div></div>'
 '<div class="cd khp" id="khp"></div></div>'
)

JS = r'''
var FOC='.hd>*,.k3s>*,.kag>*,.kbs>*,.krc>*,.khp>*';
var LOT={id:'AF-1042',ing:'Almond flour',g:100000,sup:'Harbor Mill Supply',rcv:'November 2',al:'T'};
var AL=[['W','Wheat'],['M','Milk'],['E','Egg'],['T','Tree nut']];
var PRD=[['Almond Croissant','WMET'],['Almond Cookie','WET'],['Plain Baguette','W'],['Brioche Bun','WME']];
var BAT=[{id:'B-4411',d:9,p:0,g:30000,pcs:2400,per:12},{id:'B-4420',d:12,p:1,g:20000,pcs:1800,per:12}];
var SHP=[{id:'SH-9301',d:10,b:0,c:120,to:'Eastside Cafe Group'},{id:'SH-9304',d:11,b:0,c:60,to:'Lakeview Markets'},{id:'SH-9312',d:13,b:1,c:100,to:'Eastside Cafe Group'}];
var S;
function kg(g){return (g/1000).toLocaleString('en-US',{minimumFractionDigits:3,maximumFractionDigits:3});}
function nov(d){return 'Nov '+d;}
function sum(a,f){return a.reduce(function(s,x){return s+f(x);},0);}
function cases(b){return b.pcs/b.per;}
function shipped(i){return sum(SHP.filter(function(s){return s.b===i;}),function(s){return s.c;});}
function onsite(i){return cases(BAT[i])-shipped(i);}
function used(){return sum(BAT,function(b){return b.g;});}
function made(){return sum(BAT,function(b){return cases(b);});}
function shipT(){return sum(SHP,function(s){return s.c;});}
function siteT(){return made()-shipT();}
function custs(){var o=[];SHP.forEach(function(s){var c=o.filter(function(x){return x.n===s.to;})[0];if(!c){c={n:s.to,sh:[]};o.push(c);}c.sh.push(s);});o.forEach(function(c){c.t=sum(c.sh,function(s){return s.c;});});return o;}
function usesLot(p){return BAT.some(function(b){return b.p===p;});}
function render(){
$('k3h').innerHTML=S.lot?'<span class="mono">'+LOT.id+'</span><span>'+LOT.ing+', <b>'+kg(LOT.g)+' kg</b></span><span>'+LOT.sup+'</span><span>Received '+LOT.rcv+'</span><span class="ch c-ok">Certificate attached</span>'+(S.hold?'<span class="ch c-bad" id="klh">'+kg(LOT.g-used())+' kg held</span>':'')
:'<span class="mut">Search a flagged lot to see the allergen, the batches and who received them.</span>';
var g='<div class="ct"><span>Allergen grid <span class="mut">'+(S.grid?'from ingredient lots':'products by allergen')+'</span></span>'+(S.lot&&!S.grid?'<button type="button" class="bt pri" id="kam">Map allergens</button>':S.grid?'<span class="ch c-warn">Tree nut, '+LOT.id+'</span>':'')+'</div><div class="kgr"><span class="kh">Product</span>'+AL.map(function(a){return '<span class="kh">'+a[1]+'</span>';}).join('');
PRD.forEach(function(p,i){var dim=S.grid&&!usesLot(i);g+='<span class="kp'+(dim?' kdim':'')+'">'+p[0]+'</span>'+AL.map(function(a){var has=p[1].indexOf(a[0])>=0,lit=S.grid&&has&&a[0]===LOT.al&&usesLot(i);
return '<span class="kc'+(dim?' kdim':'')+'"><i id="kx'+i+a[0]+'" class="'+(lit?'klit':S.grid&&has?'kyes':'')+'">'+(lit?LOT.id:S.grid&&has?'Contains':'')+'</i></span>';}).join('');});
$('kag').innerHTML=g+'</div>';
var b=$('kbs');
if(!S.bat)b.innerHTML='<div class="ct"><span>Batches</span>'+(S.grid?'<button type="button" class="bt pri" id="kfb">Find batches</button>':'')+'</div><div class="empt"><b>No batches yet</b><span>Every batch that used the lot shows here.</span></div>';
else b.innerHTML='<div class="ct"><span>Batches using '+LOT.id+'</span><span class="ch c-info">'+BAT.length+' batches</span></div><div class="kbt">'+BAT.map(function(x,i){var os=onsite(i);return '<div class="kbx'+(S.an?' in':'')+'" style="animation-delay:'+(i*90)+'ms"><div class="kbh"><span class="mono">'+x.id+'</span><span class="ch '+(S.hold?'c-bad':S.rcp?'c-warn':'c-idle')+'" id="kbc'+i+'">'+(S.hold?'Held '+os+' cases':S.rcp?os+' on site':nov(x.d))+'</span></div><span>'+PRD[x.p][0]+', '+nov(x.d)+'</span><span class="kbq" id="kbg'+i+'">'+kg(x.g)+' kg of '+LOT.id+'</span><span class="mut">'+n0(x.pcs)+' pieces, '+cases(x)+' cases of '+x.per+'</span></div>';}).join('')+'</div>'
+'<div class="kbf" id="kbf"><b>'+kg(used())+' kg</b> used, <b>'+kg(LOT.g-used())+' kg</b> on hand</div>';
var r=$('krc');
if(!S.rcp)r.innerHTML='<div class="ct"><span>Recipients</span>'+(S.bat?'<button type="button" class="bt pri" id="kts">Trace shipments</button>':'')+'</div><div class="empt"><b>No recipients yet</b><span>One card per customer that received an affected batch.</span></div>';
else r.innerHTML='<div class="ct"><span>Recipients</span><span class="ch c-warn">'+custs().length+' customers</span></div><div class="krl">'+custs().map(function(c,i){return '<div class="kcu'+(S.an?' in':'')+'" style="animation-delay:'+(i*90)+'ms"><div class="kch"><span>'+c.n+'</span><span class="mono" id="kct'+i+'">'+c.t+' cases</span></div>'
+c.sh.map(function(s){return '<div class="row"><span class="mono">'+s.id+'</span><span class="mut">'+nov(s.d)+'</span><span class="mono">'+BAT[s.b].id+'</span><span class="mono">'+s.c+'</span></div>';}).join('')+'</div>';}).join('')
+'<div class="kos"><span>On site, central bakery</span><b id="kon">'+siteT()+' cases</b></div><div class="ksum" id="ksum">'+shipT()+' shipped, '+siteT()+' on site</div></div>';
var h=$('khp');
if(!S.hold)h.innerHTML='<div class="ct"><span>Hold</span>'+(S.rcp?'<button type="button" class="bt pri" id="kho">Hold affected stock</button>':'')+'</div><div class="empt"><b>Nothing on hold</b><span>Cases still on site and the unused lot can be held in one step.</span></div>';
else h.innerHTML='<div class="ct"><span>Hold</span><span class="ch c-bad">Held, waiting for sign off</span></div><div class="khb"><div>'
+BAT.map(function(x,i){return '<div class="row"><span class="mono">'+x.id+'</span><span>'+PRD[x.p][0]+'</span><span class="mono" id="khq'+i+'">'+onsite(i)+' cases</span><span class="ch c-bad">Held</span></div>';}).join('')
+'<div class="row"><span class="mono">'+LOT.id+'</span><span>'+LOT.ing+', unused</span><span class="mono" id="khg">'+kg(LOT.g-used())+' kg</span><span class="ch c-bad">Held</span></div></div>'
+'<div class="khs"><b id="kht">'+siteT()+' cases</b><span>and '+kg(LOT.g-used())+' kg of '+LOT.id+'</span></div></div>';
var st=$('kst');st.textContent=S.hold?LOT.id+' on hold':S.lot?LOT.id+' flagged':'No lot searched';st.className='ch '+(S.hold?'c-bad':S.lot?'c-warn':'c-idle');
S.an=false;}
function val(){return String($('kli').value).trim().toUpperCase().replace(/\s/g,'');}
$('ksm').addEventListener('click',function(){$('kli').value=LOT.id;$('kfl').classList.remove('err');});
function typeLot(done){var t=LOT.id,i=0;(function k(){$('kli').value=t.slice(0,i);if(i<t.length){i++;later(k,70);}else done();})();}
function resetState(){S={lot:false,grid:false,bat:false,rcp:false,hold:false,an:false};$('kli').value='';$('kfl').classList.remove('err');render();}
var CAPAT=function(hh){return cur<=3?{l:14,t:visH()-hh-14}:{l:14,t:136};};
var ST=[
{id:'lot',target:function(){return mode==='try'?$('ksb'):$('kli');},prompt:'Click Search to find lot AF-1042',where:'below',
 ok:function(){if(!val())$('kli').value='AF-1042';var v=val(),b=!(v==='AF-1042'||v==='AF1042');$('kle').textContent=v?'No lot found. Try AF-1042':'Enter a lot, for example AF-1042';$('kfl').classList.toggle('err',b);return !b;},
 run:function(quick){var go=function(){$('kli').value=LOT.id;$('kfl').classList.remove('err');S.lot=true;render();};if(mode==='watch'&&!quick)typeLot(go);else go();},
 after:function(){return['Search the flagged lot',LOT.id+', '+LOT.ing.toLowerCase()+', '+kg(LOT.g)+' kg from '+LOT.sup+', received '+LOT.rcv+', certificate attached.'];}},
{id:'grid',target:function(){return $('kam');},prompt:'Click Map allergens',where:'below',run:function(){S.grid=true;render();},
 after:function(){return['See which products carry the allergen','Tree nut lights up on '+PRD.filter(function(p,i){return usesLot(i);}).map(function(p){return p[0];}).join(' and ')+'. '+PRD.filter(function(p,i){return !usesLot(i);}).map(function(p){return p[0];}).join(' and ')+' do not use '+LOT.id+'.'];}},
{id:'bat',target:function(){return $('kfb');},prompt:'Click Find batches',where:'above',run:function(){S.bat=true;S.an=true;render();},
 after:function(){return['Find every batch that used the lot',BAT.map(function(b){return b.id+' used '+kg(b.g)+' kg';}).join(' and ')+': '+kg(used())+' kg used, '+kg(LOT.g-used())+' kg on hand.'];}},
{id:'rcp',target:function(){return $('kts');},prompt:'Click Trace shipments',where:'below',run:function(){S.rcp=true;S.an=true;render();},
 after:function(){var c=custs();return['See who received them',c.map(function(x){return x.n+' '+x.t+' cases on '+x.sh.map(function(s){return s.id;}).join(' and ');}).join(', ')+'. '+shipT()+' shipped, '+siteT()+' on site.'];}},
{id:'hold',target:function(){return $('kho');},prompt:'Click Hold affected stock',where:'above',run:function(){S.hold=true;render();},
 after:function(){return['Hold what is still on site',siteT()+' cases and '+kg(LOT.g-used())+' kg of '+LOT.id+' are on hold, waiting for sign off.'];}}];
'''
