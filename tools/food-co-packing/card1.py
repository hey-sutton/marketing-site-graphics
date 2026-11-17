"""Food co-packing card 1: Client Inventory & Ownership.
Layout: list and detail. A lot list and a finished goods list on the left; on the right the lot record, the balance by owner
and the next runs for this item.
Every lot is tagged with its owner. Client supplied rice flour sits in three client balances beside the plant's own stock;
a run draws only from its owner, a shortage shows before the run, and a client's finished goods are held in their own bay.
Every number is computed from the data arrays below (grams), so sums are exact."""
from frame_auto import header

SUMMARY = 'Client Inventory & Ownership (search an item, open a lot and its owner, compare client supplied and plant purchased stock, release stock to a run, flag a shortage, hold a client\'s finished goods apart)'
ARIA = 'Interactive product screen: rice flour lots owned by three clients and the plant, 3,050.000 kg on hand; release 420.000 kg to run R-5108 from Brightfield Snacks only, flag a 150.000 kg shortage for Oakline Foods, and hold Kettlewood Brands finished goods in bay C3'
STEPS = 5
STUDIO = dict(lede='A typical client inventory screen, built on your Sutton data with Studio. Want it different? Describe the change.',
              examples=['Show stock by client portal', 'Bill storage by pallet day', 'Warn when a client lot ages', 'Split balances by site'],
              built_on='Lots, owners, runs and locations', change='Owners, columns and rules')

ICON = '<path d="M2.5 5L8 2.5 13.5 5v6L8 13.5 2.5 11z"/><path d="M2.5 5L8 7.5 13.5 5M8 7.5v6"/>'

CSS = (
 '.c1{padding:10px 40px 0 16px;display:flex;flex-direction:column;gap:10px}'
 '.c1s{height:44px;flex:none;display:flex;align-items:center;gap:8px;padding:0 10px}.c1s .fld{flex-direction:row;align-items:center;gap:8px;position:relative}.c1s .fld small{font-size:10px;color:#18181B;font-weight:600;white-space:nowrap}'
 '#qin{width:160px;font-size:10.4px;padding:6px 8px}.c1s .fld .em{position:absolute;left:0;top:30px;white-space:nowrap;background:#fff;padding:1px 4px;z-index:3}'
 '.qsm{display:inline-flex;align-items:center;gap:5px;font-size:9.4px;color:#71717A}.qsm .bt{font-size:9.6px;padding:4px 8px}'
 '.c1m{display:grid;grid-template-columns:292px 358px;gap:10px;height:482px;flex:none}.c1l,.c1r{display:flex;flex-direction:column;gap:8px;min-width:0}'
 '.qls{height:250px;flex:none}.qfg{flex:1 1 auto;display:flex;flex-direction:column}.qft{margin-top:auto;padding:6px 10px;border-top:1px solid #F0F0F1;font-size:8.8px;color:#71717A}.qls .empt,.qfg .empt{margin:8px 10px;height:calc(100% - 46px);padding:8px}'
 '.qls .row,.qfg .row{min-height:44px;padding:0 10px;grid-template-columns:1fr auto;font-size:9.6px}.qls button.row.sel{box-shadow:inset 3px 0 0 #18181B}'
 '.qn{display:flex;flex-direction:column;gap:2px;min-width:0}.qn b{font-family:"JetBrains Mono",ui-monospace,monospace;font-size:9.8px;font-weight:600}.qn small{font-size:8.8px;color:#71717A;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}'
 '.qv{display:flex;flex-direction:column;align-items:flex-end;gap:3px}.qv b{font-family:"JetBrains Mono",ui-monospace,monospace;font-size:9.8px;font-weight:600}'
 '.qrec{height:124px;flex:none}.qrec .empt,.qbal .empt,.qrun .empt{margin:8px 10px;height:calc(100% - 46px);padding:8px}'
 '.qrg{display:grid;grid-template-columns:repeat(3,1fr);gap:5px 10px;padding:6px 11px}.qrg .kv small{font-size:8.6px}.qrg .kv b{font-size:10px}.qrg .kv b.mono{font-size:10.2px}'
 '.qbal{height:172px;flex:none}.qb{display:grid;grid-template-columns:118px 1fr 84px;align-items:center;gap:8px;padding:3px 11px;font-size:9.4px}.qb .mono{text-align:right;font-weight:600;font-size:9.6px}'
 '.qbar{height:8px;border-radius:4px;background:#F4F4F5;position:relative;overflow:hidden}.qbar i{position:absolute;left:0;top:0;bottom:0;border-radius:4px;background:#52525B;transition:width .6s cubic-bezier(.22,.9,.28,1)}.qbar i.pl{background:#A1A1AA}.qb.hit{background:#FFFBEB}'
 '.qtot{display:flex;justify-content:space-between;padding:5px 11px;border-top:1px solid #F0F0F1;margin-top:3px;font-size:9.6px}.qtot b{font-family:"JetBrains Mono",ui-monospace,monospace}'
 '.qrun{flex:1 1 auto}.qrun .row{grid-template-columns:52px 1fr 70px 92px;min-height:28px;padding:0 11px;font-size:9.4px;gap:8px}.qrun .row>span:nth-child(3){text-align:right}.qrun .row>span:last-child{text-align:right}.qrun .bt{font-size:9px;padding:3px 7px}'
 '.qrun .row.bad{background:#FEF2F2}'
)

WIN = (
 header(ICON, 'Client inventory', 'Owned stock by client, rice flour line', '<span class="ch c-idle" id="qst">No item searched</span>')
 + '<div class="c1"><div class="cd c1s frm" id="qsf"><label class="fld" id="qfl"><small>Item</small><input id="qin" value="" placeholder="Item name or lot" autocomplete="off" spellcheck="false" aria-label="Item name or lot"><span class="em" id="qem">No item found. Try Rice flour</span></label>'
 '<button type="button" class="bt pri" id="qsb">Search</button><span class="qsm">Sample<button type="button" class="bt" id="qsm" data-sample>Rice flour</button></span></div>'
 '<div class="c1m"><div class="c1l"><div class="cd qls" id="qls"></div><div class="cd qfg" id="qfg"></div></div>'
 '<div class="c1r"><div class="cd qrec" id="qrec"></div><div class="cd qbal" id="qbal"></div><div class="cd qrun" id="qrun"></div></div></div></div>'
)

JS = r'''
var FOC='.hd>*,.c1s>*,.qls,.qfg,.qrec,.qbal,.qrun';
/* rice flour lots in grams; owner P is the plant's own purchased stock */
var OWN={B:'Brightfield Snacks',O:'Oakline Foods',K:'Kettlewood Brands',P:'Plant purchased'};
var LOTS=[{id:'RF-2201',o:'B',g:1200000,rc:'Nov 4',loc:'Bay A2'},{id:'RF-2202',o:'O',g:800000,rc:'Nov 6',loc:'Bay A3'},{id:'RF-2203',o:'K',g:450000,rc:'Nov 9',loc:'Bay A4'},{id:'RF-2204',o:'P',g:600000,rc:'Nov 10',loc:'Bay B1'}];
var RUNS=[{id:'R-5108',o:'B',p:'Puffed rice bites',g:420000,d:'Nov 18'},{id:'R-5112',o:'O',p:'Rice crackers',g:950000,d:'Nov 19'},{id:'R-5115',o:'K',p:'Granola clusters',g:300000,d:'Nov 20'}];
var FG=[{id:'FG-7721',o:'B',p:'Puffed rice bites',c:120},{id:'FG-7730',o:'K',p:'Granola clusters',c:64},{id:'FG-7734',o:'O',p:'Rice crackers',c:90}];
var HOLD='Client hold, bay C3';
var S;
function kg(g){return (g/1000).toLocaleString('en-US',{minimumFractionDigits:3,maximumFractionDigits:3});}
function bal(o){return LOTS.filter(function(l){return l.o===o;}).reduce(function(s,l){return s+l.g;},0)-(S.rel&&o==='B'?RUNS[0].g:0);}
function client(){return ['B','O','K'].reduce(function(s,o){return s+bal(o);},0);}
function plant(){return bal('P');}
function total(){return client()+plant();}
function lotLeft(l){return l.g-(S.rel&&l.id==='RF-2201'?RUNS[0].g:0);}
function short(r){return Math.max(0,r.g-bal(r.o));}
function render(){
var L=$('qls');
if(!S.q)L.innerHTML='<div class="ct"><span>Lots</span></div><div class="empt"><b>No item searched</b><span>Search an item to list every lot with its owner.</span></div>';
else L.innerHTML='<div class="ct"><span>Rice flour lots</span><span class="ch c-info">'+LOTS.length+' lots</span></div>'+LOTS.map(function(l,i){return '<button type="button" class="row'+(S.sel===i?' sel':'')+(S.an?' in':'')+'" id="ql'+i+'" style="animation-delay:'+(i*70)+'ms"><span class="qn"><b>'+l.id+'</b><small>'+OWN[l.o]+'</small></span><span class="qv"><b id="qg'+i+'">'+kg(lotLeft(l))+' kg</b><span class="ch '+(l.o==='P'?'c-idle':'c-info')+'">'+(l.o==='P'?'Plant':'Client')+'</span></span></button>';}).join('');
var F=$('qfg');
if(!S.q)F.innerHTML='<div class="ct"><span>Finished goods held for clients</span></div><div class="empt"><b>Nothing listed yet</b><span>Finished goods made for each brand show here with their location.</span></div>';
else F.innerHTML='<div class="ct"><span>Finished goods held for clients</span></div>'+FG.map(function(f,i){var h=S.hold&&f.id==='FG-7730';return '<div class="row'+(h?' sel':'')+'"><span class="qn"><b>'+f.id+'</b><small>'+OWN[f.o]+', '+f.p+'</small></span><span class="qv"><b>'+f.c+' cases</b>'+(f.id==='FG-7730'&&!S.hold?'<button type="button" class="bt'+(S.flag?' pri':'')+'" id="qhd">Hold in client bay</button>':'<span class="ch '+(h?'c-bad':'c-idle')+'" id="qfc'+i+'">'+(h?'Held, bay C3':'Dock staging')+'</span>')+'</span></div>';}).join('');
F.insertAdjacentHTML('beforeend','<div class="qft">Bays A2 to A4 hold client stock, B1 plant stock, C3 client holds.</div>');
var R=$('qrec');
if(!S.q)R.innerHTML='<div class="ct"><span>Lot record</span></div><div class="empt"><b>No lot open</b><span>The owner, type and location of a lot show here.</span></div>';
else{var l=LOTS[S.sel],kv=[['Lot',l.id,1],['Owner',OWN[l.o]],['Type',l.o==='P'?'Plant purchased':'Client supplied'],['On hand',kg(lotLeft(l))+' kg',1],['Received',l.rc],['Location',l.loc]];
R.innerHTML='<div class="ct"><span>Lot record</span><span class="ch '+(l.o==='P'?'c-idle':'c-info')+'" id="qow">'+OWN[l.o]+'</span></div><div class="qrg">'+kv.map(function(x){return '<span class="kv"><small>'+x[0]+'</small><b'+(x[2]?' class="mono"':'')+'>'+x[1]+'</b></span>';}).join('')+'</div>';}
var B=$('qbal');
if(!S.cmp)B.innerHTML='<div class="ct"><span>Balance by owner</span>'+(S.q?'<button type="button" class="bt pri" id="qcm">Compare owners</button>':'')+'</div><div class="empt"><b>Not compared yet</b><span>Client supplied and plant purchased stock, side by side.</span></div>';
else{var mx=LOTS[0].g,rows=['B','O','K','P'].map(function(o){var v=bal(o);return '<div class="qb'+(S.rel&&o==='B'?' hit':'')+'"><span>'+OWN[o]+'</span><span class="qbar"><i class="'+(o==='P'?'pl':'')+'" style="width:'+(v/mx*100).toFixed(1)+'%"></i></span><span class="mono" id="qb'+o+'">'+kg(v)+' kg</span></div>';}).join('');
B.innerHTML='<div class="ct"><span>Balance by owner</span><span class="mut" style="font-weight:400;font-size:9.2px" id="qsplit">Client '+kg(client())+' kg, plant '+kg(plant())+' kg</span></div><div style="padding-top:4px">'+rows+'</div><div class="qtot"><span>Total on hand</span><b id="qtt">'+kg(total())+' kg</b></div>';}
var U=$('qrun');
if(!S.q)U.innerHTML='<div class="ct"><span>Next runs</span></div><div class="empt"><b>No runs listed</b><span>Runs that need this item, and whose stock they draw from.</span></div>';
else U.innerHTML='<div class="ct"><span>Next runs using rice flour</span>'+(S.rel&&!S.flag?'<button type="button" class="bt pri" id="qck">Check next runs</button>':S.flag?'<span class="ch c-bad">1 short</span>':'')+'</div>'+RUNS.map(function(r,i){var sh=S.flag&&short(r)>0,act;
if(i===0)act=S.rel?'<span class="ch c-ok" id="qr0">Released</span>':'<button type="button" class="bt'+(S.cmp?' pri':'')+'" id="qrl">Release '+kg(r.g)+'</button>';
else act=S.flag?(sh?'<span class="ch c-bad" id="qr'+i+'">Short '+kg(short(r))+'</span>':'<span class="ch c-ok" id="qr'+i+'">Covered</span>'):'<span class="ch c-idle">'+r.d+'</span>';
return '<div class="row'+(sh?' bad':'')+'"><span class="mono">'+r.id+'</span><span>'+OWN[r.o]+'</span><span class="mono">'+kg(r.g)+'</span><span>'+act+'</span></div>';}).join('');
var st=$('qst');st.textContent=S.hold?'Finished goods held':S.flag?'1 shortage flagged':S.q?'Rice flour, 4 owners':'No item searched';st.className='ch '+(S.flag?'c-warn':S.q?'c-info':'c-idle');
S.an=false;}
function val(){return String($('qin').value).trim().toLowerCase().replace(/\s+/g,' ');}
$('qsm').addEventListener('click',function(){$('qin').value='Rice flour';$('qfl').classList.remove('err');});
function typeIt(t,done){var i=0;(function k(){$('qin').value=t.slice(0,i);if(i<t.length){i++;later(k,60);}else done();})();}
function resetState(){S={q:false,sel:0,cmp:false,rel:false,flag:false,hold:false,an:false};$('qin').value='';$('qfl').classList.remove('err');render();}
var CAPAT=function(hh){return cur>=4?{l:14,t:110}:{l:14,t:visH()-hh-14};};
var ST=[
{id:'lot',target:function(){return mode==='try'?$('qsb'):$('qin');},prompt:'Type Rice flour or pick the sample, then Search',where:'below',
 ok:function(){var v=val(),b=!(v==='rice flour'||v.indexOf('rf-22')===0);$('qem').textContent=v?'No item found. Try Rice flour':'Enter an item, for example Rice flour';$('qfl').classList.toggle('err',b);return !b;},
 run:function(quick){var go=function(){$('qin').value='Rice flour';$('qfl').classList.remove('err');S.q=true;S.sel=0;S.an=true;render();};if(mode==='watch'&&!quick)typeIt('Rice flour',go);else go();},
 after:function(){var l=LOTS[0];return['Every lot carries its owner',l.id+' is rice flour supplied by '+OWN[l.o]+', '+kg(l.g)+' kg in '+l.loc.toLowerCase()+'.'];}},
{id:'cmp',target:function(){return $('qcm');},prompt:'Click Compare owners',where:'above',run:function(){S.cmp=true;render();},
 after:function(){return['Client and plant stock side by side','Client supplied '+kg(client())+' kg across 3 clients, plant purchased '+kg(plant())+' kg, '+kg(total())+' kg on hand.'];}},
{id:'rel',target:function(){return $('qrl');},prompt:'Release stock to run R-5108',where:'above',run:function(){S.rel=true;render();},
 after:function(){var r=RUNS[0];return['A run draws only from its owner',r.id+' takes '+kg(r.g)+' kg from '+OWN[r.o]+': '+kg(LOTS[0].g)+' to '+kg(bal('B'))+' kg. Plant stock stays at '+kg(plant())+' kg.'];}},
{id:'flag',target:function(){return $('qck');},prompt:'Click Check next runs',where:'above',run:function(){S.flag=true;render();},
 after:function(){var r=RUNS[1];return['Shortages show before the run',r.id+' needs '+kg(r.g)+' kg of '+OWN[r.o]+' rice flour and '+kg(bal(r.o))+' kg is on hand: short '+kg(short(r))+' kg.'];}},
{id:'hold',target:function(){return $('qhd');},prompt:'Hold the Kettlewood Brands finished goods',where:'above',run:function(){S.hold=true;render();},
 after:function(){var f=FG[1];return['Finished goods held apart',f.id+', '+f.c+' cases of '+OWN[f.o]+' '+f.p.toLowerCase()+', moved to the client hold in bay C3.'];}}];
'''
