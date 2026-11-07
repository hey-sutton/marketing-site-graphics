"""Distribution card 1: Inventory Control & Planning. Layout: bin map of both warehouses with an item list and a movement log on the left,
a SKU panel (find, Locations, Availability and Plan tabs) and a stock actions panel (transfer, scan a delivery in) on the right."""
SUMMARY = 'Inventory Control & Planning (find a SKU on the bin map of both warehouses, available to sell, low stock against reorder points, a transfer, a delivery scanned in, suggested buys)'
ARIA = 'Interactive product screen: find SKU GL-210 on the Atlanta and Dallas bin map, see what is available to sell, filter the items below their reorder point, transfer stock from Dallas to Atlanta, scan delivery PO-4402 in and open the buying plan'
STEPS = 6
STUDIO = dict(lede='A typical stock by bin screen, built on your Sutton data with Studio. Want it different? Describe the change.',
              examples=['A cycle count planner', 'A transfer suggestion view', 'A slow mover report', 'A safety stock review'],
              built_on='Items, bins, warehouses and stock moves', change='Maps, fields and views')

CSS = (
 '.b1{display:grid;grid-template-columns:1fr 238px;gap:12px;padding:12px 40px 0 16px;height:596px}'
 '.col{display:flex;flex-direction:column;gap:10px;min-height:0}'
 '.map .wh{padding:7px 10px 8px}.map .wh+.wh{border-top:1px solid #F0F0F1}.whh{display:flex;align-items:center;gap:6px;font-size:9.8px;font-weight:600;margin-bottom:5px}.whh .mono{font-weight:500}.whh .q{margin-left:auto;font-weight:500;color:#71717A;font-size:9.4px}.whh .q b{color:#18181B;font-family:"JetBrains Mono",ui-monospace,monospace;font-weight:600}'
 '.ais{display:grid;grid-template-columns:14px repeat(8,1fr);gap:4px;align-items:center;margin-top:4px}.ais>i{font-style:normal;color:#A1A1AA;font-size:9px;font-weight:600}'
 '.bin{height:27px;border:1px solid #E4E4E7;border-radius:5px;background:#FAFAFA;display:flex;flex-direction:column;align-items:center;justify-content:center;line-height:1.05;transition:background-color .35s,border-color .35s,color .35s}'
 '.bin span{font-family:"JetBrains Mono",ui-monospace,monospace;font-size:7.4px;color:#A1A1AA}.bin b{font-family:"JetBrains Mono",ui-monospace,monospace;font-size:9.6px;font-weight:600;display:none}'
 '.bin.oth{background:#F4F4F5}.bin.lit{background:#18181B;border-color:#18181B}.bin.lit span{color:#D4D4D8}.bin.lit b{display:block;color:#fff}.bin.new{animation:exflash2 1.2s ease}@keyframes exflash2{0%{box-shadow:0 0 0 3px #FFB92B}100%{box-shadow:0 0 0 0 rgba(255,185,43,0)}}'
 '.lg{display:flex;align-items:center;gap:10px;font-size:8.8px;color:#71717A;font-weight:500}.lg i{display:inline-block;width:8px;height:8px;border-radius:2px;margin-right:4px;vertical-align:-1px}'
 '.flt{display:flex;align-items:center;gap:6px}.fc{border:1px solid #E4E4E7;border-radius:999px;background:#fff;padding:3px 9px;font-size:9.4px;cursor:pointer;transition:background-color .2s,border-color .2s,color .2s}.fc b{font-weight:600;margin-left:4px}.fc.on{background:#18181B;border-color:#18181B;color:#fff}'
 '.lst .row{grid-template-columns:52px 1fr 52px 64px;min-height:23px;font-size:9.6px}.lst .row.lo .av{color:#B91C1C;font-weight:600}'
 '.bar{height:4px;border-radius:2px;background:#F4F4F5;overflow:hidden;margin-top:2px}.bar i{display:block;height:100%;background:#F87171;border-radius:2px}'
 '.mov{flex:1 1 0;min-height:0}.mov .row{grid-template-columns:38px 58px 1fr;min-height:23px;font-size:9.4px}'
 '.fnd{display:flex;align-items:center;gap:6px;position:relative;margin-right:26px}.fnd .fld{width:86px}.fnd .fld .em{position:absolute;left:0;top:30px;white-space:nowrap;background:#fff;padding:1px 3px;border-radius:3px}'
 '.itm{flex:none;height:226px;display:flex;flex-direction:column}.itm .ih{padding:8px 11px 4px;display:flex;flex-direction:column;gap:1px}.itm .ih b{font-size:11px}.itm .ih span{font-size:9.2px;color:#71717A}'
 '.itm .pane{padding:6px 11px;display:flex;flex-direction:column;gap:5px}.itm .row{padding:0 2px;grid-template-columns:1fr auto;min-height:22px;font-size:9.6px}.itm .row.t{font-weight:600}.itm .pd{padding:9px 11px}'
 '.pl .row{grid-template-columns:44px 1fr 1fr 1fr 36px;gap:4px;font-size:9.2px}.pl .row span:not(:first-child){text-align:right}.pl .row.h{font-size:8.4px;padding:0 2px}'
 '.act{flex:none}.act .grp{padding:8px 10px 6px;display:flex;flex-direction:column;gap:5px}.act .nt{font-size:8.8px;color:#71717A;min-height:13px;line-height:13px}.act .grp+.grp{border-top:1px solid #F0F0F1}.act .gt{display:flex;align-items:center;justify-content:space-between;font-size:9.8px;font-weight:600}'
 '.act .fs{display:grid;grid-template-columns:40px 1fr 1fr;gap:5px}.act .fs.s{grid-template-columns:1fr 40px 1fr}.act .bt{width:100%}'
)

WIN = (
 '<div class="hd"><svg width="16" height="16" viewBox="0 0 16 16" fill="none" aria-hidden="true"><path d="M2.5 5L8 2l5.5 3v6L8 14l-5.5-3z M2.5 5L8 8l5.5-3M8 8v6" stroke="#18181B" stroke-width="1.2" stroke-linejoin="round"/></svg>'
 '<span class="tt">Inventory</span><span class="ch c-idle" id="hst">2 warehouses</span><span class="sb grow">Ridgeway Supply, stock by bin</span><span class="fnd frm"><label class="fld" id="fsk"><input id="isk" value="GL-210" aria-label="SKU" autocomplete="off" spellcheck="false"><span class="em">Use GL-210, the gloves</span></label><button type="button" class="bt pri" id="find">Find SKU</button></span></div>'
 '<div class="b1"><div class="col">'
 '<div class="cd map"><div class="ct">Bin map<span class="lg"><span><i style="background:#18181B"></i>Holds this SKU</span><span><i style="background:#F4F4F5;border:1px solid #E4E4E7"></i>Other stock</span></span></div><div id="wh"></div></div>'
 '<div class="cd lst" id="lst"></div>'
 '<div class="cd mov" id="mov"></div>'
 '</div><div class="col">'
 '<div class="cd itm" id="itm"></div>'
 '<div class="cd act" id="act"></div>'
 '</div></div>'
)

JS = r'''
var FOC='.hd>*,.map .ct,.wh,.lst .ct,.flt>*,.lst .row,.mov,.fnd .fld,.fnd .bt,.itm .ih,.itm .tab,.itm .pane,.act .ct,.act .gt,.act .nt,.act .fs,.act .bt';
var IT=[['GL-210','Nitrile gloves, box of 100',220,150,100],['TW-330','Shop towels, case of 12',340,110,120],['BT-118','Hex bolt kit, 24 piece',60,20,80],['LB-502','Shipping labels, roll',900,300,250],['PK-077','Pallet wrap, roll',48,30,40]];
var FC={'BT-118':160,'PK-077':90};
var WH=[['Atlanta','WH-ATL',[['A',['A-01-1','A-02-3','A-03-1','A-04-2','A-05-2','A-06-1','A-07-1','A-08-3']],['B',['B-04-1','B-06-2','B-08-1','B-09-3','B-10-2','B-11-4','B-12-1','B-13-2']],['C',['C-01-2','C-02-1','C-03-1','C-04-4','C-05-1','C-06-2','C-07-3','C-08-1']]]],
['Dallas','WH-DAL',[['D',['D-01-1','D-02-3','D-03-2','D-04-1','D-05-1','D-06-3','D-07-2','D-08-1']],['E',['E-01-2','E-02-1','E-03-3','E-04-1','E-05-2','E-06-1','E-07-1','E-08-2']]]]];
var EMPTY={'A-03-1':1,'B-09-3':1,'C-04-4':1,'C-08-1':1,'D-05-1':1,'E-03-3':1,'E-07-1':1,'A-08-3':1};
var B0={'A-04-2':120,'A-07-1':60,'D-02-3':40},RES=150;
var S;
function it(k){for(var i=0;i<IT.length;i++)if(IT[i][0]===k)return IT[i];return null;}
function onh(){return S.oh['GL-210'];}
function avl(k){var x=it(k);return S.oh[k]-x[3];}
function isLow(k){return avl(k)<it(k)[4];}
function nLow(){return IT.filter(function(x){return isLow(x[0]);}).length;}
function whq(w){var t=0;Object.keys(S.b).forEach(function(k){if(k.charAt(0)===(w==='Atlanta'?'A':'D'))t+=S.b[k];});return t;}
function val(i){return String($(i).value).trim();}
function int(v){return /^\d{1,4}$/.test(v)?parseInt(v,10):-1;}
function fld(i,bad){$(i).classList.toggle('err',bad);return !bad;}
function render(){var h='';
WH.forEach(function(w){h+='<div class="wh"><div class="whh">'+w[0]+' <span class="mono mut">'+w[1]+'</span>'+(S.found?'<span class="q">GL-210 <b id="q-'+w[0]+'">'+whq(w[0])+'</b></span>':'')+'</div>';
w[2].forEach(function(a){h+='<div class="ais"><i>'+a[0]+'</i>'+a[1].map(function(b){var q=S.found?S.b[b]:0;return '<div class="bin'+(q?' lit':EMPTY[b]?'':' oth')+(S.fl[b]?' new':'')+'" id="b-'+b+'"><span>'+b+'</span><b>'+(q||'')+'</b></div>';}).join('')+'</div>';});h+='</div>';});
$('wh').innerHTML=h;
var rows=IT.filter(function(x){return !S.low||isLow(x[0]);});
var l='<div class="ct">Items<span class="flt"><button type="button" class="fc'+(S.low?'':' on')+'">All<b>5</b></button><button type="button" class="fc'+(S.low?' on':'')+'" id="flow">Low stock'+(S.low?'<b>'+nLow()+'</b>':'')+'</button></span></div>';
l+='<div class="row h"><span>SKU</span><span>Item</span><span class="r">'+(S.low?'Available':'On hand')+'</span><span class="r">'+(S.low?'vs point':'Reorder point')+'</span></div>';
rows.forEach(function(x){var a=avl(x[0]);l+='<div class="row'+(S.low?' lo in':'')+'"><span class="mono">'+x[0]+'</span><span>'+x[1]+'</span>'+(S.low?'<span class="mono r av">'+a+'</span><span><span class="mono" style="display:block;text-align:right">'+a+' / '+x[4]+'</span><span class="bar"><i style="width:'+Math.round(a/x[4]*100)+'%"></i></span></span>':'<span class="mono r">'+S.oh[x[0]]+'</span><span class="mono r">'+x[4]+'</span>')+'</div>';});
$('lst').innerHTML=l;
var mv=S.mv.map(function(m,i){return '<div class="row'+(m[3]?' in':'')+'"><span class="mono mut">'+m[0]+'</span><span class="mono">'+m[1]+'</span><span>'+m[2]+'</span></div>';}).join('');
$('mov').innerHTML='<div class="ct">Stock moves<span class="mut" style="font-weight:500">Both warehouses</span></div>'+mv;
var g=$('find');g.disabled=S.found;g.className='bt '+(S.found?'done':'pri');g.textContent=S.found?'Found':'Find SKU';
var x=it('GL-210'),m='';
if(!S.found)m='<div class="ct">Item</div><div class="pd"><div class="empt"><b>No item open</b><span>Find a SKU to see its bins, what is available to sell and what to buy next.</span></div></div>';
else{m='<div class="ih"><b><span class="mono">GL-210</span> '+x[1]+'</b><span>Boxes, reorder point '+x[4]+'</span></div><div class="tabs">'+[['loc','Locations'],['av','Availability'],['pl','Plan']].map(function(t){return '<button type="button" class="tab'+(S.tab===t[0]?' on':'')+'" id="t-'+t[0]+'">'+t[1]+'</button>';}).join('')+'</div><div class="pane'+(S.anim?' in':'')+'">';
if(S.tab==='loc'){Object.keys(S.b).forEach(function(k){m+='<div class="row"><span><span class="mono">'+k+'</span> <span class="mut">'+(k.charAt(0)==='A'?'Atlanta':'Dallas')+'</span></span><span class="mono">'+S.b[k]+'</span></div>';});m+='<div class="row t"><span>On hand</span><span class="mono" id="loh">'+onh()+'</span></div>';}
if(S.tab==='av'){var a=onh()-RES,lo=a<x[4];m+='<div class="row"><span>On hand</span><span class="mono" id="aoh">'+onh()+'</span></div><div class="row"><span>Reserved by open orders</span><span class="mono">'+RES+'</span></div><div class="row t"><span>Available to sell</span><span class="mono" id="aav">'+a+'</span></div>'+
'<div class="row"><span class="mut">Atlanta, '+RES+' reserved</span><span class="mono">'+whq('Atlanta')+'</span></div><div class="row"><span class="mut">Dallas, none reserved</span><span class="mono">'+whq('Dallas')+'</span></div>'+
'<span class="ch '+(lo?'c-bad':'c-ok')+'" id="aflag" style="align-self:flex-start">'+(lo?'Below reorder point of '+x[4]:'Above reorder point of '+x[4])+'</span>';}
if(S.tab==='pl'){var p='<div class="pl"><div class="row h"><span>SKU</span><span>Forecast</span><span>+ point</span><span>− avail.</span><span>Buy</span></div>',n=0;
IT.forEach(function(y){if(!isLow(y[0]))return;n++;p+='<div class="row in"><span class="mono">'+y[0]+'</span><span class="mono">'+FC[y[0]]+'</span><span class="mono">'+y[4]+'</span><span class="mono">'+avl(y[0])+'</span><b class="mono" id="buy-'+y[0]+'">'+(FC[y[0]]+y[4]-avl(y[0]))+'</b></div>';});
m+='<span class="mut" style="font-size:9.2px;line-height:1.4">Suggested buys for items under their reorder point, from 30 day demand, the point and what is available.</span>'+p+'</div><span class="ch c-info" style="align-self:flex-start">'+n+' suggestions sent to purchasing</span>';}
m+='</div>';}
$('itm').innerHTML=m;
var c='<div class="grp frm"><div class="gt"><span>Transfer <span class="mono mut" style="font-weight:500">GL-210</span></span>'+(S.xf?'<span class="ch c-ok">TO-0931 done</span>':'')+'</div><div class="fs">'+
'<label class="fld" id="fxq"><small>Boxes</small><input id="ixq" value="'+S.v.xq+'" inputmode="numeric" autocomplete="off"></label><label class="fld" id="fxf"><small>From</small><input id="ixf" value="'+S.v.xf+'" autocomplete="off" spellcheck="false"></label><label class="fld" id="fxt"><small>To</small><input id="ixt" value="'+S.v.xt+'" autocomplete="off" spellcheck="false"></label></div>'+
'<span class="fld" id="fxe" style="margin-top:-3px"><span class="em">Up to 40 boxes, from D-02-3 to an Atlanta bin</span></span>'+
'<button type="button" class="bt '+(S.xf?'done':'pri')+'" id="xfer"'+(S.xf?' disabled':'')+'>'+(S.xf?'Transferred':'Transfer')+'</button><span class="nt">'+(S.xf?'Atlanta '+whq('Atlanta')+', Dallas '+whq('Dallas'):'Atlanta orders need more, Dallas has spare')+'</span></div>';
c+='<div class="grp frm"><div class="gt">Scan delivery in'+(S.sc?'<span class="ch c-ok">PO-4402 received</span>':'')+'</div><div class="fs s">'+
'<label class="fld" id="fsp"><small>PO</small><input id="isp" value="'+S.v.sp+'" autocomplete="off" spellcheck="false"></label><label class="fld" id="fsq"><small>Boxes</small><input id="isq" value="'+S.v.sq+'" inputmode="numeric" autocomplete="off"></label><label class="fld" id="fsb"><small>Bin</small><input id="isb" value="'+S.v.sb+'" autocomplete="off" spellcheck="false"></label></div>'+
'<span class="fld" id="fse" style="margin-top:-3px"><span class="em">Use PO-4402, whole boxes, an Atlanta A bin</span></span>'+
'<button type="button" class="bt '+(S.sc?'done':'pri')+'" id="scan"'+(S.sc?' disabled':'')+'>'+(S.sc?'Scanned in':'Scan delivery in')+'</button><span class="nt">'+(S.sc?'On hand '+onh()+', available '+(onh()-RES):'At dock 2, arrived 09:40')+'</span></div>';
$('act').innerHTML=c;
$('hst').textContent=S.found?'GL-210 open':'2 warehouses';$('hst').className='ch '+(S.found?'c-info':'c-idle');
S.anim=false;S.fl={};}
$('act').addEventListener('input',function(e){var k={ixq:'xq',ixf:'xf',ixt:'xt',isp:'sp',isq:'sq',isb:'sb'}[e.target.id];if(k)S.v[k]=e.target.value;});
function okX(){var q=int(val('ixq')),f=val('ixf').toUpperCase(),t=val('ixt').toUpperCase();var bad=!(q>0&&q<=S.b['D-02-3']&&f==='D-02-3'&&/^A-0[1-8]-[1-4]$/.test(t));$('fxe').classList.toggle('err',bad);['fxq','fxf','fxt'].forEach(function(i){$(i).classList.toggle('err',bad);});return !bad;}
function okS(){var q=int(val('isq')),p=val('isp').toUpperCase(),b=val('isb').toUpperCase();var bad=!(q>0&&p==='PO-4402'&&/^A-0[1-8]-[1-4]$/.test(b));$('fse').classList.toggle('err',bad);['fsp','fsq','fsb'].forEach(function(i){$(i).classList.toggle('err',bad);});return !bad;}
function resetState(){var oh={};IT.forEach(function(x){oh[x[0]]=x[2];});
S={found:false,tab:'loc',low:false,xf:false,sc:false,anim:false,oh:oh,b:{'A-04-2':120,'A-07-1':60,'D-02-3':40},fl:{},v:{xq:'30',xf:'D-02-3',xt:'A-07-1',sp:'PO-4402',sq:'120',sb:'A-04-2'},
mv:[['11/06','SO-6188','Picked TW-330, 8 cases from B-11-4'],['11/06','PO-4396','Received LB-502, 400 rolls into C-02-1'],['11/05','TO-0927','BT-118, 20 kits Dallas to Atlanta'],['11/05','SO-6174','Picked PK-077, 6 rolls from C-06-2'],['11/04','CC-0112','Cycle count aisle D, no changes']]};
$('isk').value='GL-210';$('fsk').classList.remove('err');render();}
function addMv(m){S.mv.unshift(m.concat([1]));S.mv=S.mv.slice(0,5);}
var CAPAT=function(hh){return{l:14,t:visH()-hh-14};};
var ST=[
{id:'find',target:function(){return $('find');},prompt:'Click Find SKU',where:'below',ok:function(){return fld('fsk',val('isk').toUpperCase()!=='GL-210');},
 run:function(){S.found=true;S.anim=true;S.tab='loc';Object.keys(S.b).forEach(function(k){S.fl[k]=1;});render();},after:['Find any SKU and see every bin that holds it, in both warehouses','GL-210 is in A-04-2 (120), A-07-1 (60) and D-02-3 (40), 220 boxes in all.']},
{id:'av',target:function(){return $('t-av');},prompt:'Click the Availability tab',where:'below',run:function(){S.tab='av';S.anim=true;render();},after:['Available to sell is what is on the shelf minus what open orders have reserved','220 on hand, 150 reserved, so 70 boxes are free to sell.']},
{id:'low',target:function(){return $('flow');},prompt:'Click Low stock',where:'below',run:function(){S.low=true;render();},after:['Three of five items are under their reorder point','GL-210 70 of 100, BT-118 40 of 80 and PK-077 18 of 40.']},
{id:'xfer',target:function(){return $('xfer');},prompt:'Click Transfer',where:'below',ok:okX,
 run:function(){okX();var q=int(val('ixq')),t=val('ixt').toUpperCase();S.b['D-02-3']-=q;S.b[t]=(S.b[t]||0)+q;S.fl['D-02-3']=1;S.fl[t]=1;S.xf=true;S.q=q;addMv(['Now','TO-0931','GL-210, '+q+' boxes D-02-3 to '+t]);render();},
 after:function(){return['Move stock to where the orders are, and both counts change together','Atlanta now holds '+whq('Atlanta')+' and Dallas '+whq('Dallas')+'. Transfer order TO-0931, '+(whq('Atlanta')+whq('Dallas'))+' boxes in all.'];}},
{id:'scan',target:function(){return $('scan');},prompt:'Click Scan delivery in',where:'below',ok:okS,
 run:function(){okS();var q=int(val('isq')),b=val('isb').toUpperCase();S.b[b]=(S.b[b]||0)+q;S.oh['GL-210']+=q;S.fl[b]=1;S.sc=true;addMv(['Now','PO-4402','Received GL-210, '+q+' boxes into '+b]);render();},
 after:function(){return['A scan updates the bin, the count and the low stock flag at once','On hand '+onh()+', available '+(onh()-RES)+(onh()-RES>=100?'. GL-210 is no longer low.':'.')];}},
{id:'pl',target:function(){return $('t-pl');},prompt:'Click the Plan tab',where:'below',run:function(){S.tab='pl';S.anim=true;render();},after:['The plan suggests what to buy from demand, stock and reorder points','BT-118 160 + 80 − 40 = 200 kits. PK-077 90 + 40 − 18 = 112 rolls.']}];
'''
