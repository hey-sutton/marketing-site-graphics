"""Frozen food card 1: Lot Trace from Ingredient to Pallet. Layout: four column lineage board (ingredient lot, batches,
pallets, customers) with connector lines that light up as each column fills. Every number is computed from the arrays."""
from frame_auto import header

SUMMARY = 'Lot Trace from Ingredient to Pallet (type an ingredient lot, see the batches, pallets and customers it reached, then hold the pallets still in the freezer)'
ARIA = 'Interactive product screen: trace IQF broccoli lot HR-7731 to three batches of FE-2210, fifteen pallets and two customers, then hold the six pallets still in the freezer'
STEPS = 5
STUDIO = dict(lede='A typical lot trace screen, built on your Sutton data with Studio. Want it different? Describe the change.',
              examples=['A mock recall report with timings', 'A customer notice for each affected order', 'A trace that starts from a pallet label', 'A hold that blocks picking in every freezer'],
              built_on='Lots, batches, pallets and shipments', change='Columns, fields and actions')

ICON = '<rect x="1.8" y="3" width="3" height="10" rx=".8"/><rect x="6.5" y="3" width="3" height="10" rx=".8"/><rect x="11.2" y="3" width="3" height="10" rx=".8"/><path d="M4.8 6h1.7M9.5 6h1.7M9.5 10h1.7"/>'

CSS = (
 '.g1{padding:10px 40px 0 16px;display:flex;flex-direction:column;gap:10px}'
 '.srch{height:44px;flex:none;display:flex;align-items:center;gap:8px;padding:0 10px}.srch .fld{flex-direction:row;align-items:center;gap:8px;position:relative}.srch .fld small{font-size:10px;color:#18181B;font-weight:600;white-space:nowrap}'
 '.srch .fld input{width:150px;font-size:10.6px;padding:6px 8px}.srch .fld .em{position:absolute;left:84px;top:36px;white-space:nowrap}'
 '.smp{display:inline-flex;align-items:center;gap:6px;font-size:9.4px;color:#71717A;margin-left:4px}.smp .bt{font-family:"JetBrains Mono",ui-monospace,monospace;font-size:9.6px;padding:4px 8px}'
 '.brd{position:relative;height:348px;flex:none}.brd svg.ln{position:absolute;left:0;top:0;width:660px;height:348px;pointer-events:none;overflow:visible}'
 '.brd svg.ln path{fill:none;stroke:#E4E4E7;stroke-width:1.4;transition:stroke .4s}.brd svg.ln path.on{stroke:#2563EB}.brd svg.ln path.hd{stroke:#F87171}'
 '.cl{position:absolute;top:0;width:150px;height:348px;border:1px solid #E4E4E7;border-radius:8px;background:#FAFAFA}.cl .ch2{height:32px;display:flex;align-items:center;justify-content:space-between;gap:6px;padding:0 9px;border-bottom:1px solid #E4E4E7;font-size:10px;font-weight:600;background:#fff;border-radius:8px 8px 0 0}'
 '.cl .ch2 .bt{font-size:9px;padding:3px 7px}.ph{position:absolute;border:1px dashed #E4E4E7;border-radius:7px;display:grid;place-items:center;color:#A1A1AA;font-size:8.8px;text-align:center;padding:0 8px;line-height:1.3}'
 '.it{position:absolute;border:1px solid #E4E4E7;border-radius:7px;background:#fff;padding:7px 8px;display:flex;flex-direction:column;gap:3px;font-size:9.2px;line-height:1.3;white-space:nowrap;box-shadow:0 1px 2px rgba(0,0,0,.04)}'
 '.it .tp{display:flex;align-items:center;justify-content:space-between;gap:4px}.it .id{font-family:"JetBrains Mono",ui-monospace,monospace;font-weight:600;font-size:9.6px}.it.hd{border-color:#FCA5A5;background:#FEF2F2}'
 '.lot{gap:6px}.lot .kv{gap:1px}.lot .kv small{font-size:8.6px}.lot .kv b{font-size:9.4px;font-weight:500}.lot .bar{height:5px;border-radius:3px;background:#F0F0F1;overflow:hidden}.lot .bar i{display:block;height:100%;background:#2563EB;transition:width .5s}'
 '.tls{display:flex;gap:3px;flex-wrap:wrap}.tl{width:15px;height:15px;border-radius:3px;background:#E4E4E7;transition:background-color .35s}.tl.s{background:#2563EB}.tl.f{background:#F59E0B}.tl.h{background:#DC2626}'
 '.sb3{flex:none;height:118px;display:flex;flex-direction:column}.sb3 .ct .ch{margin-left:auto}.st{display:grid;grid-template-columns:repeat(4,1fr);gap:0;padding:8px 11px 0}.st .kv{padding-right:8px}.st .kv b{font-size:15px}.st .kv em{font-style:normal;font-size:8.6px;color:#A1A1AA}'
 '.ac{display:flex;align-items:center;gap:8px;margin-top:auto;padding:0 11px 11px;font-size:9.4px;color:#52525B;white-space:nowrap}.lgd2{display:flex;gap:10px;align-items:center;font-size:8.6px;color:#71717A}.lgd2 span{display:inline-flex;align-items:center;gap:4px}.lgd2 i{width:9px;height:9px;border-radius:2px;display:inline-block}'
)

WIN = (
 header(ICON, 'Lot trace', 'Recall readiness, chicken broccoli entree FE-2210')
 + '<div class="g1"><div class="cd srch frm"><label class="fld" id="flin"><small>Ingredient lot</small><input id="lin" value="" placeholder="Ingredient lot number" autocomplete="off" spellcheck="false" aria-label="Ingredient lot"><span class="em" id="lem">No lot found. Try HR-7731</span></label>'
 '<button type="button" class="bt pri" id="trc">Trace</button><span class="smp">Sample<button type="button" class="bt" id="smp" data-sample>HR-7731</button></span><span class="grow"></span><span class="ch c-idle" id="sst">No lot traced</span></div>'
 '<div class="brd" id="brd"></div><div class="cd sb3" id="sb3"></div></div>'
)

JS = r'''
var FOC='.hd>*,.srch>*,.cl,.it,.sb3 .ct>*,.st,.ac>*';
var LOT={id:'HR-7731',item:'IQF broccoli',lb:3000,sup:'Harvest Ridge Farms',rcv:'Received Oct 28',loc:'Holding freezer A'};
var LBC=2,CPP=100;
var BAT=[['B-4412',1200],['B-4416',1000],['B-4421',800]];
var DEST=[[['SH-2201','Northfield Foods',4],['SH-2204','Coastal Grocers',2]],[['SH-2204','Coastal Grocers',3],['FRZ','Freezer',2]],[['FRZ','Freezer',4]]];
var CUS=['Northfield Foods','Coastal Grocers','Freezer'];
var CX=[0,170,340,510],CW=150,RT=44,RS=104,RH=84;
var S;
function sum(a){return a.reduce(function(x,y){return x+y;},0);}
function cases(i){return BAT[i][1]/LBC;}
function pallets(i){return cases(i)/CPP;}
function totPal(){return sum(BAT.map(function(b,i){return pallets(i);}));}
function toC(name){return sum(DEST.map(function(d){return sum(d.filter(function(x){return x[1]===name;}).map(function(x){return x[2];}));}));}
function shipped(){return toC('Northfield Foods')+toC('Coastal Grocers');}
function frozen(){return toC('Freezer');}
function shipIds(name){var o=[];DEST.forEach(function(d){d.forEach(function(x){if(x[1]===name&&o.indexOf(x[0])<0)o.push(x[0]);});});return o;}
function cy(i){return RT+i*RS+RH/2;}
function curve(x1,y1,x2,y2,cls){var m=(x1+x2)/2;return '<path class="'+cls+'" d="M'+x1+' '+y1+'C'+m+' '+y1+' '+m+' '+y2+' '+x2+' '+y2+'"/>';}
function box(cls,l,t,w,h,inner,an,d){return '<div class="'+cls+(an?' in':'')+'" style="left:'+l+'px;top:'+t+'px;width:'+w+'px;height:'+h+'px'+(an?';animation-delay:'+d+'ms':'')+'">'+inner+'</div>';}
function tiles(i){var o='',k=0;DEST[i].forEach(function(x){for(var j=0;j<x[2];j++){var c=!S.cu?'':x[0]==='FRZ'?(S.hold?' h':' f'):' s';o+='<i class="tl'+c+'" title="'+(x[0]==='FRZ'?'Freezer':x[0])+'"></i>';k++;}});return '<span class="tls">'+o+'</span>';}
function render(){
var h='',p='',n=['Ingredient lot','Batches','Pallets','Customers'];
var hdr=[S.lot?'<span class="ch c-info">1</span>':'',S.ba?'<span class="ch c-info" id="nba">'+BAT.length+'</span>':'',
S.pa?'<span class="ch c-info" id="npa">'+totPal()+'</span>':(S.ba?'<button type="button" class="bt" id="spa">Show pallets</button>':''),
S.cu?'<span class="ch c-info" id="ncu">2 + freezer</span>':(S.pa?'<button type="button" class="bt" id="tsh">Trace shipments</button>':'')];
n.forEach(function(t,i){h+='<div class="cl" style="left:'+CX[i]+'px"><div class="ch2"><span>'+t+'</span>'+hdr[i]+'</div></div>';});
var ph=['Enter a lot to start','Batches that used the lot','Pallets built from them','Where each pallet went'];
var shown=[S.lot,S.ba,S.pa,S.cu];
shown.forEach(function(v,i){if(!v){if(i===0)h+='<div class="ph" style="left:8px;top:44px;width:134px;height:292px">'+ph[0]+'</div>';else for(var r=0;r<3;r++)h+='<div class="ph" style="left:'+(CX[i]+8)+'px;top:'+(RT+r*RS)+'px;width:134px;height:'+RH+'px">'+(r===1?ph[i]:'')+'</div>';}});
if(S.lot){var used=S.ba?sum(BAT.map(function(b){return b[1];})):0;
h+=box('it lot',8,44,134,292,'<div class="tp"><span class="id">'+LOT.id+'</span><span class="ch '+(S.hold?'c-bad':'c-info')+'">'+(S.hold?'Quarantined':'Supplier lot')+'</span></div><b style="font-size:10.4px">'+LOT.item+'</b>'+
'<div class="kv"><small>Quantity</small><b class="mono">'+n0(LOT.lb)+' lb</b></div><div class="kv"><small>Supplier</small><b>'+LOT.sup+'</b></div><div class="kv"><small>Receipt</small><b>'+LOT.rcv+'</b></div><div class="kv"><small>Stored</small><b>'+LOT.loc+'</b></div>'+
'<div class="kv"><small>Used in batches</small><b class="mono" id="lused">'+(S.ba?n0(used)+' of '+n0(LOT.lb)+' lb':'None traced yet')+'</b></div><div class="bar"><i style="width:'+(used/LOT.lb*100)+'%"></i></div>'+
(S.ba?'':'<button type="button" class="bt" id="wu" style="align-self:flex-start;margin-top:auto">Where used</button>'),S.a1,0);}
if(S.ba)BAT.forEach(function(b,i){p+=curve(142,cy(i),CX[1]+8,cy(i),'on'+(S.hold&&i>0?' hd':''));h+=box('it',CX[1]+8,RT+i*RS,134,RH,'<div class="tp"><span class="id">'+b[0]+'</span><span class="ch c-idle">FE-2210</span></div><span id="bl'+i+'">'+n0(b[1])+' lb used</span><span class="mut" id="bc'+i+'">'+n0(cases(i))+' cases at '+LBC+' lb</span>',S.a2,i*90);});
if(S.pa)BAT.forEach(function(b,i){p+=curve(CX[1]+142,cy(i),CX[2]+8,cy(i),'on'+(S.hold&&i>0?' hd':''));h+=box('it',CX[2]+8,RT+i*RS,134,RH,'<div class="tp"><span class="id" id="pp'+i+'">'+pallets(i)+' pallets</span><span class="mut">'+b[0]+'</span></div><span class="mut">'+n0(cases(i))+' cases, '+CPP+' a pallet</span>'+tiles(i),S.a3,i*90);});
if(S.cu){DEST.forEach(function(d,i){d.forEach(function(x){var j=CUS.indexOf(x[1]);p+=curve(CX[2]+142,cy(i),CX[3]+8,cy(j),'on'+(S.hold&&x[0]==='FRZ'?' hd':''));});});
CUS.forEach(function(c,j){var fz=c==='Freezer',hd=fz&&S.hold;h+=box('it'+(hd?' hd':''),CX[3]+8,RT+j*RS,134,RH,'<b>'+(fz?'In the freezer':c)+'</b><div class="tp"><span class="mono" id="cp'+j+'">'+toC(c)+' pallets</span><span class="ch '+(hd?'c-bad':fz?'c-warn':'c-info')+'">'+(hd?'Held':fz?'On hand':'Shipped')+'</span></div><span class="mut">'+(fz?'Holding freezer A':shipIds(c).join(', '))+'</span>',S.a4,j*90);});}
$('brd').innerHTML='<svg class="ln" viewBox="0 0 660 348" aria-hidden="true">'+p+'</svg>'+h;
var s='<div class="ct"><span>Trace summary</span><span class="ch '+(S.hold?'c-bad':S.lot?'c-warn':'c-idle')+'" id="cst">'+(S.hold?'Quarantined':S.lot?'Open':'Not started')+'</span></div>';
var K=[['Batches',S.ba?BAT.length:'',S.ba?n0(sum(BAT.map(function(b){return b[1];})))+' lb used':'','sba'],['Pallets',S.pa?totPal():'',S.pa?n0(sum(BAT.map(function(b,i){return cases(i);})))+' cases':'','spa2'],
['Customers',S.cu?2:'',S.cu?shipped()+' pallets shipped':'','scu'],[S.hold?'Held':'In the freezer',S.cu?frozen():'',S.cu?(S.hold?'Pallets on hold':'Pallets on hand'):'','sfz']];
s+='<div class="st">'+K.map(function(k){return '<div class="kv"><small>'+k[0]+'</small><b id="'+k[3]+'">'+k[1]+'</b><em>'+k[2]+'</em></div>';}).join('')+'</div><div class="ac">';
if(!S.cu)s+='<span class="lgd2"><span><i style="background:#2563EB"></i>Shipped</span><span><i style="background:#F59E0B"></i>In the freezer</span><span><i style="background:#DC2626"></i>Held</span></span><span class="mut">Each pallet holds '+CPP+' cases.</span>';
else if(!S.hold)s+='<button type="button" class="bt pri" id="hld">Hold '+frozen()+' pallets in the freezer</button><span class="mut">Blocks picking for the pallets still on hand.</span>';
else s+='<span class="ch c-bad">Quarantined</span><span id="csum">'+BAT.length+' batches, '+totPal()+' pallets, 2 customers, '+frozen()+' held.</span>';
s+='</div>';$('sb3').innerHTML=s;
var st=$('sst');st.textContent=S.hold?LOT.id+' quarantined':S.lot?LOT.id+' traced':'No lot traced';st.className='ch '+(S.hold?'c-bad':S.lot?'c-info':'c-idle');
S.a1=S.a2=S.a3=S.a4=false;}
function val(){return String($('lin').value).trim().toUpperCase().replace(/\s/g,'');}
$('smp').addEventListener('click',function(){$('lin').value=LOT.id;$('flin').classList.remove('err');});
function typeLot(done){var t=LOT.id,i=0;(function k(){$('lin').value=t.slice(0,i);if(i<t.length){i++;later(k,60);}else done();})();}
function resetState(){S={lot:false,ba:false,pa:false,cu:false,hold:false};$('lin').value='';$('flin').classList.remove('err');render();}
var CAPAT=function(hh){return cur>=3?{l:visW()-cap.offsetWidth-14,t:visH()-hh-14}:{l:14,t:visH()-hh-14};};
var ST=[
{id:'lot',target:function(){return mode==='try'?$('trc'):$('lin');},prompt:'Type HR-7731 or pick the sample, then Trace',where:'below',
 ok:function(){var v=val(),b=!(v==='HR-7731'||v==='HR7731');$('lem').textContent=v?'No lot found. Try HR-7731':'Enter a lot, for example HR-7731';$('flin').classList.toggle('err',b);return !b;},
 run:function(quick){var go=function(){$('lin').value=LOT.id;$('flin').classList.remove('err');S.lot=true;S.a1=true;render();};if(mode==='watch'&&!quick)typeLot(go);else go();},
 after:function(){return['Type an ingredient lot and the trace starts there',LOT.id+' is '+n0(LOT.lb)+' lb of '+LOT.item+' from '+LOT.sup+'.'];}},
{id:'ba',target:function(){return $('wu');},prompt:'Click Where used',where:'right',run:function(){S.ba=true;S.a2=true;render();},
 after:function(){return['Every batch that used the lot, with the pounds it took',BAT.map(function(b){return b[0]+' '+n0(b[1])+' lb';}).join(', ')+'. All '+n0(LOT.lb)+' lb accounted for.'];}},
{id:'pa',target:function(){return $('spa');},prompt:'Show the pallets',where:'below',run:function(){S.pa=true;S.a3=true;render();},
 after:function(){return['Batches become cases, and cases become pallets',BAT.map(function(b,i){return b[0]+' '+pallets(i);}).join(', ')+'. '+totPal()+' pallets of '+CPP+' cases.'];}},
{id:'cu',target:function(){return $('tsh');},prompt:'Trace the shipments',where:'below',run:function(){S.cu=true;S.a4=true;render();},
 after:function(){return['Each pallet ends at a customer or in the freezer',shipped()+' pallets shipped to Northfield Foods and Coastal Grocers, '+frozen()+' still in the freezer.'];}},
{id:'hold',target:function(){return $('hld');},prompt:'Hold the pallets in the freezer',where:'above',run:function(){S.hold=true;render();},
 after:function(){return['Hold what is still in the freezer in one click','Quarantined: '+BAT.length+' batches, '+totPal()+' pallets, 2 customers, '+frozen()+' held.'];}}];
'''
