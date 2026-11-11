"""Automotive card 1: Component Genealogy & Containment (working title). Layout: genealogy graph.
Type a suspect supplier lot, follow it to the work orders that consumed it, the finished lots they built, the shipments
and the stock still on hand, then hold what is on hand. Every number is computed from the data arrays below."""
from frame_auto import header

SUMMARY = 'Component Genealogy & Containment (type a suspect supplier lot, see the work orders, finished lots and shipments built from it, then hold the stock on hand)'
ARIA = 'Interactive product screen: trace supplier lot SL-4471 of fastener FST-118 to three work orders, three finished lots of BA-5520 and their shipments, then hold the 900 assemblies still on hand'
STEPS = 5
STUDIO = dict(lede='A typical lot genealogy screen, built on your Sutton data with Studio. Want it different? Describe the change.',
              examples=['A supplier lot search by heat number', 'A customer notice for every affected plant', 'A hold that also blocks picking', 'A trace by VIN or serial range'],
              built_on='Lots, work orders, BOMs and shipments', change='Levels, fields and actions')

ICON = '<circle cx="3.5" cy="8" r="1.8"/><circle cx="12.5" cy="3.5" r="1.8"/><circle cx="12.5" cy="12.5" r="1.8"/><path d="M5.3 8h2.2M7.5 8c0-3 1.5-4.5 3.2-4.5M7.5 8c0 3 1.5 4.5 3.2 4.5"/>'

CSS = (
 '.g1{padding:10px 40px 0 16px;display:flex;flex-direction:column;gap:10px}'
 '.srch{height:44px;flex:none;display:flex;align-items:center;gap:8px;padding:0 10px}.srch .fld{flex-direction:row;align-items:center;gap:8px}.srch .fld small{font-size:10px;color:#18181B;font-weight:600;white-space:nowrap}'
 '.srch .fld input{width:150px;font-size:10.6px;padding:6px 8px}.srch .fld .em{position:absolute;left:96px;top:36px;white-space:nowrap}.srch .fld{position:relative}'
 '.smp{display:inline-flex;align-items:center;gap:6px;font-size:9.4px;color:#71717A;margin-left:4px}.smp .bt{font-family:"JetBrains Mono",ui-monospace,monospace;font-size:9.6px;padding:4px 8px}'
 '.gph{height:332px;flex:none}.gph .ct{gap:14px;justify-content:flex-start}.lvs{display:flex;gap:4px;margin-left:auto}.lv{font:inherit;font-size:9.4px;font-weight:500;padding:3px 8px;border:1px solid #E4E4E7;border-radius:999px;background:#fff;color:#A1A1AA;cursor:default}'
 '.lv.on{background:#18181B;border-color:#18181B;color:#fff}.lv.av{color:#18181B;cursor:pointer}.lv.av:hover,.lv.av.fakehover{background:#F4F4F5}.lv:focus-visible{outline:2px solid #18181B;outline-offset:2px}'
 '.cvs{position:relative;height:286px;margin:8px 10px}.cvs svg.ln{position:absolute;left:0;top:0;width:638px;height:286px;overflow:visible}.cvs svg.ln path{fill:none;stroke:#D4D4D8;stroke-width:1.3}.cvs svg.ln path.hl{stroke:#F87171}'
 '.cl{position:absolute;top:0;font-size:8.8px;font-weight:500;color:#71717A;white-space:nowrap}'
 '.nd{position:absolute;border:1px solid #E4E4E7;border-radius:7px;background:#fff;padding:6px 8px;display:flex;flex-direction:column;justify-content:center;gap:2px;font-size:9.4px;line-height:1.3;white-space:nowrap;box-shadow:0 1px 2px rgba(0,0,0,.04)}'
 '.nd .tp{display:flex;align-items:center;justify-content:space-between;gap:6px}.nd .id{font-family:"JetBrains Mono",ui-monospace,monospace;font-weight:600;font-size:9.8px}.nd.lot{border-color:#18181B;box-shadow:0 0 0 1px #18181B}'
 '.nd.hold{border-color:#FCA5A5;background:#FEF2F2}.nd .wu{align-self:flex-start;margin-top:3px;font-size:9.2px;padding:3px 8px}'
 '.sum{flex:none;height:150px}.sum .ct .ch{margin-left:auto}.tls{display:grid;grid-template-columns:repeat(4,1fr);gap:8px;padding:9px 10px 0}'
 '.tl{border:1px solid #F0F0F1;border-radius:7px;padding:7px 9px;height:58px;display:flex;flex-direction:column;justify-content:space-between;background:#FAFAFA}.tl small{font-size:8.9px;color:#71717A}.tl b{font-size:16px;font-weight:600;letter-spacing:-.01em}.tl em{font-style:normal;font-size:8.6px;color:#A1A1AA}.tl.hot{background:#FEF2F2;border-color:#FECACA}'
 '.act{display:flex;align-items:center;gap:8px;padding:9px 10px 0;height:44px;font-size:9.6px;color:#52525B;white-space:nowrap}'
 '.gph .empt,.sum .empt{margin:10px;height:calc(100% - 50px)}'
)

WIN = (
 header(ICON, 'Lot genealogy', 'Traceability, bracket assembly BA-5520')
 + '<div class="g1"><div class="cd srch frm" id="srch"><label class="fld" id="flin"><small>Suspect lot</small><input id="lin" value="" placeholder="Supplier lot number" autocomplete="off" spellcheck="false" aria-label="Suspect lot"><span class="em" id="lem">No lot found. Try SL-4471</span></label>'
 '<button type="button" class="bt pri" id="trc">Trace</button><span class="smp">Sample<button type="button" class="bt" id="smp" data-sample>SL-4471</button></span><span class="grow"></span><span class="ch c-idle" id="sst">No lot traced</span></div>'
 '<div class="cd gph" id="gph"></div><div class="cd sum" id="sum"></div></div>'
)

JS = r'''
var FOC='.hd>*,.srch>*,.gph .ct>*,.lv,.cl,.nd,.sum .ct>*,.tl,.act>*';
var LOT={id:'SL-4471',part:'FST-118',desc:'Zinc plated fastener',qty:12000,sup:'Ridgefield Fasteners'};
var PER=2;
var WO=[['WO-7102',4800,'FGL-0912'],['WO-7108',4200,'FGL-0913'],['WO-7115',3000,'FGL-0914']];
var SH=[[['SH-5521','Plant North',2400]],[['SH-5530','Plant North',1800]],[['SH-5534','Plant South',900]]];
var X=[0,160,320,480],W=[118,118,118,158],LT=[21,102,210],LEAF=46,STEP=54;
var S;
function sum(a){return a.reduce(function(x,y){return x+y;},0);}
function built(i){return WO[i][1]/PER;}
function shipped(i){return sum(SH[i].map(function(s){return s[2];}));}
function onhand(i){return built(i)-shipped(i);}
function totBuilt(){return sum(WO.map(function(w,i){return built(i);}));}
function totShip(){return sum(WO.map(function(w,i){return shipped(i);}));}
function totHand(){return sum(WO.map(function(w,i){return onhand(i);}));}
function leaves(){var out=[];WO.forEach(function(w,i){SH[i].forEach(function(s){out.push({ch:i,id:s[0],to:s[1],q:s[2],k:'sh'});});if(onhand(i)>0)out.push({ch:i,id:w[2],to:'Finished goods',q:onhand(i),k:'oh'});});return out;}
function node(cls,l,t,w,h,inner,an,d){return '<div class="nd '+cls+(an?' in':'')+'" style="left:'+l+'px;top:'+t+'px;width:'+w+'px;height:'+h+'px'+(an?';animation-delay:'+d+'ms':'')+'">'+inner+'</div>';}
function curve(x1,y1,x2,y2,hl){var m=(x1+x2)/2;return '<path'+(hl?' class="hl"':'')+' d="M'+x1+' '+y1+'C'+m+' '+y1+' '+m+' '+y2+' '+x2+' '+y2+'"/>';}
function lvl(){return S.sh?4:S.fg?3:S.wo?2:1;}
function render(){
var g='<div class="ct"><span>Genealogy</span><span class="mut" style="font-weight:500">'+(S.lot?LOT.id+', '+LOT.part:'')+'</span><span class="lvs">'+
[['lv-lot','Supplier lot',1],['lv-wo','Work orders',2],['lv-fg','Finished lots',3],['lv-sh','Shipments',4]].map(function(x){var L=lvl(),on=S.lot&&x[2]<=L,av=S.lot&&x[2]===L+1&&x[2]===3&&S.wo;return '<button type="button" class="lv'+(on?' on':av?' av':'')+'" id="'+x[0]+'"'+(on||av?'':' tabindex="-1"')+'>'+x[1]+'</button>';}).join('')+'</span></div>';
if(!S.lot){g+='<div class="empt"><svg width="26" height="26" viewBox="0 0 16 16" fill="none" stroke="#A1A1AA" stroke-width="1.1" stroke-linecap="round">'+'<circle cx="3.5" cy="8" r="1.8"/><circle cx="12.5" cy="3.5" r="1.8"/><circle cx="12.5" cy="12.5" r="1.8"/><path d="M5.3 8h2.2M7.5 8c0-3 1.5-4.5 3.2-4.5M7.5 8c0 3 1.5 4.5 3.2 4.5"/>'+'</svg><b>No lot traced</b><span>Enter a suspect lot to see every work order, finished lot and shipment built from it.</span></div>';$('gph').innerHTML=g;}
else{var lv=leaves(),lc=155,p='',n='';
n+='<span class="cl" style="left:0">Supplier lot</span>';
n+=node('lot',X[0],117,W[0],76,'<div class="tp"><span class="id">'+LOT.id+'</span></div><span>'+LOT.part+', '+n0(LOT.qty)+' pcs</span><span class="mut">'+LOT.sup+'</span>'+(S.wo?'':'<button type="button" class="bt wu" id="wu">Where used</button>'),S.a1,0);
if(S.wo){n+='<span class="cl" style="left:'+X[1]+'px" id="wol">Work orders, '+n0(sum(WO.map(function(w){return w[1];})))+' of '+n0(LOT.qty)+' used</span>';
WO.forEach(function(w,i){var c=LT[i]+26;p+=curve(X[0]+W[0],lc,X[1],c,S.hold&&onhand(i)>0);n+=node('',X[1],LT[i],W[1],52,'<span class="id">'+w[0]+'</span><span class="mut" id="wq'+i+'">'+n0(w[1])+' fasteners</span>',S.a2,i*90);});}
if(S.fg){n+='<span class="cl" style="left:'+X[2]+'px" id="fgl">Finished lots, '+n0(totBuilt())+' built</span>';
WO.forEach(function(w,i){var c=LT[i]+26;p+=curve(X[1]+W[1],c,X[2],c,S.hold&&onhand(i)>0);n+=node('',X[2],LT[i],W[2],52,'<span class="id">'+w[2]+'</span><span class="mut" id="fq'+i+'">'+n0(built(i))+' assemblies</span>',S.a3,i*90);});}
if(S.sh){n+='<span class="cl" style="left:'+X[3]+'px" id="shl">Shipments and stock</span>';
lv.forEach(function(x,j){var t=24+j*STEP,c=t+LEAF/2,pc=LT[x.ch]+26,oh=x.k==='oh',hd=oh&&S.hold;p+=curve(X[2]+W[2],pc,X[3],c,hd);
n+=node(hd?'hold':'',X[3],t,W[3],LEAF,'<div class="tp"><span class="id">'+x.id+'</span><span class="ch '+(hd?'c-bad':oh?'c-warn':'c-info')+'">'+(hd?'Held':oh?'On hand':'Shipped')+'</span></div><span class="mut" id="lf'+j+'">'+x.to+', '+n0(x.q)+'</span>',S.a4,j*80);});}
g+='<div class="cvs"><svg class="ln" viewBox="0 0 638 286" aria-hidden="true">'+p+'</svg>'+n+'</div>';$('gph').innerHTML=g;}
var s='<div class="ct"><span>Containment</span><span class="ch '+(S.hold?'c-bad':S.lot?'c-warn':'c-idle')+'" id="cst">'+(S.hold?'Quarantined':S.lot?'Open':'Not started')+'</span></div>';
if(!S.lot)s+='<div class="empt"><b>Nothing to contain yet</b><span>Totals and the hold appear once a lot is traced.</span></div>';
else{var T=[['Fasteners in lot',S.lot?n0(LOT.qty):'',LOT.part,'t-lot'],['Assemblies built',S.fg?n0(totBuilt()):'',S.fg?'3 finished lots':'Open finished lots','t-blt'],
['Shipped',S.sh?n0(totShip()):'',S.sh?'Plant North and Plant South':'Trace shipments','t-shp'],['On hand',S.sh?n0(totHand()):'',S.hold?'Held, FGL-0913 and FGL-0914':S.sh?'FGL-0913 and FGL-0914':'Trace shipments','t-oh']];
s+='<div class="tls">'+T.map(function(t,i){return '<div class="tl'+(i===3&&S.hold?' hot':'')+'"><small>'+t[0]+'</small><b id="'+t[3]+'">'+t[1]+'</b><em>'+t[2]+'</em></div>';}).join('')+'</div><div class="act">';
if(!S.sh)s+='<button type="button" class="bt" id="tsh"'+(S.fg?'':' disabled')+'>Trace shipments</button><span class="mut">Follow every finished lot to its shipments and stock.</span>';
else if(!S.hold)s+='<button type="button" class="bt pri" id="hld">Hold '+n0(totHand())+' on hand</button><span class="mut">Blocks picking and shipping for the stock still in the plant.</span>';
else s+='<span class="ch c-bad">Quarantined</span><span id="csum">'+n0(totBuilt())+' built, '+n0(totShip())+' shipped, '+n0(totHand())+' held.</span><span class="mut">Notice drafted for Plant North and Plant South.</span>';
s+='</div>';}
$('sum').innerHTML=s;
var st=$('sst');st.textContent=S.hold?LOT.id+' quarantined':S.lot?LOT.id+' traced':'No lot traced';st.className='ch '+(S.hold?'c-bad':S.lot?'c-info':'c-idle');
S.a1=S.a2=S.a3=S.a4=false;}
function val(){return String($('lin').value).trim().toUpperCase().replace(/\s/g,'');}
$('smp').addEventListener('click',function(){$('lin').value=LOT.id;$('flin').classList.remove('err');});
var typing=null;
function typeLot(done){var t=LOT.id,i=0;(function k(){$('lin').value=t.slice(0,i);if(i<t.length){i++;typing=later(k,60);}else done();})();}
function resetState(){S={lot:false,wo:false,fg:false,sh:false,hold:false};$('lin').value='';$('flin').classList.remove('err');render();}
var CAPAT=function(hh){return cur>=3?{l:14,t:96}:{l:14,t:visH()-hh-14};};
var ST=[
{id:'lot',target:function(){return mode==='try'?$('trc'):$('lin');},prompt:'Type SL-4471 or pick the sample, then Trace',where:'below',
 ok:function(){var v=val(),b=!(v==='SL-4471'||v==='SL4471');$('lem').textContent=v?'No lot found. Try SL-4471':'Enter a lot, for example SL-4471';$('flin').classList.toggle('err',b);return !b;},
 run:function(quick){var go=function(){$('lin').value=LOT.id;$('flin').classList.remove('err');S.lot=true;S.a1=true;render();};if(mode==='watch'&&!quick)typeLot(go);else go();},
 after:function(){return['Type a suspect lot and the trace starts at the supplier lot',LOT.id+' is '+n0(LOT.qty)+' zinc plated fasteners '+LOT.part+' from '+LOT.sup+'.'];}},
{id:'wo',target:function(){return $('wu');},prompt:'Click Where used',where:'below',run:function(){S.wo=true;S.a2=true;render();},
 after:function(){return['See every work order that consumed the lot',WO.map(function(w){return w[0]+' used '+n0(w[1]);}).join(', ')+'. All '+n0(sum(WO.map(function(w){return w[1];})))+' accounted for.'];}},
{id:'fg',target:function(){return $('lv-fg');},prompt:'Open the finished lots level',where:'below',run:function(){S.fg=true;S.a3=true;render();},
 after:function(){return['Each work order leads to the finished lots it built','At '+PER+' fasteners per BA-5520: '+WO.map(function(w,i){return w[2]+' '+n0(built(i));}).join(', ')+'. '+n0(totBuilt())+' in all.'];}},
{id:'sh',target:function(){return $('tsh');},prompt:'Click Trace shipments',where:'above',run:function(){S.sh=true;S.a4=true;render();},
 after:function(){return['Then to every shipment, and what is still on the shelf',n0(totShip())+' shipped to Plant North and Plant South, '+n0(totHand())+' still on hand.'];}},
{id:'hold',target:function(){return $('hld');},prompt:'Hold the stock on hand',where:'above',run:function(){S.hold=true;render();},
 after:function(){return['Hold what is still in the plant in one click','Quarantined: '+n0(totBuilt())+' built, '+n0(totShip())+' shipped, '+n0(totHand())+' held.'];}}];
'''
