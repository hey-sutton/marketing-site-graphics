"""Frozen food card 2: Cold Storage by Location. Layout: a top down freezer floor plan of four zones, each with a rack and
bin grid (one bin holds one pallet of 100 cases), plus a side panel with the scanned pallet and on hand, committed and
available stock. Quantities are computed from the bin map, so a move always keeps the total."""
from frame_auto import header

SUMMARY = 'Cold Storage by Location (scan pallet P-0912, see its zone and bin, move it to Holding freezer B, then watch available stock follow open orders and a quality hold)'
ARIA = 'Interactive product screen: scan pallet P-0912 in Blast freezer 1, see the zone lots and expiry dates, move it to Holding freezer B, check on hand, committed and available stock, and put the outside cold store on quality hold'
STEPS = 5
STUDIO = dict(lede='A typical cold storage screen, built on your Sutton data with Studio. Want it different? Describe the change.',
              examples=['A temperature log for each zone', 'A put away rule by expiry date', 'A first expired, first out pick list', 'A monthly bill from the outside cold store'],
              built_on='Locations, pallets, lots and sales orders', change='Zones, rules and views')

ICON = '<rect x="2" y="2" width="12" height="12" rx="1.2"/><path d="M8 2v12M2 8h12"/><path d="M4.3 4.3h1.4M10.3 10.3h1.4"/>'

CSS = (
 '.g2{display:grid;grid-template-columns:1fr 212px;gap:10px;padding:10px 40px 0 16px}'
 '.col{display:flex;flex-direction:column;gap:10px;min-width:0}'
 '.pln{height:540px;flex:none;display:flex;flex-direction:column}.pln .ct .ch{margin-left:auto}'
 '.zs{display:grid;grid-template-columns:1fr 1fr;gap:10px;padding:10px 10px 0}'
 '.zn{border:1px solid #E4E4E7;border-radius:8px;background:#fff;height:222px;display:flex;flex-direction:column;transition:border-color .3s,background-color .3s}.zn.off{border-style:dashed;background:#FCFCFC}'
 '.zn.lit{border-color:#2563EB;box-shadow:0 0 0 1px #2563EB}.zn.hd{border-color:#FCA5A5;background:#FEF2F2}'
 '.zh{display:flex;align-items:center;gap:6px;height:32px;padding:0 9px;border:0;border-bottom:1px solid #F0F0F1;background:none;width:100%;text-align:left;font:inherit;font-size:10px;font-weight:600;cursor:pointer;border-radius:8px 8px 0 0}.zh:hover,.zh.fakehover{background:#FAFAFA}.zh:focus-visible{outline:2px solid #18181B;outline-offset:-2px}.zh .ch{margin-left:auto}'
 '.rk{display:flex;flex-direction:column;gap:8px;padding:12px 9px 0}.rr{display:flex;align-items:center;gap:5px}.rr>span{width:18px;font-size:8.4px;color:#A1A1AA;font-family:"JetBrains Mono",ui-monospace,monospace}'
 '.bin{width:36px;height:40px;border:1px solid #E4E4E7;border-radius:4px;background:#fff;display:grid;place-items:center;font-size:7.8px;color:#A1A1AA;font-family:"JetBrains Mono",ui-monospace,monospace;transition:background-color .35s,border-color .35s,color .35s}'
 '.bin.f{background:#E4E4E7;border-color:#D4D4D8;color:#52525B}.bin.me{background:#2563EB;border-color:#1D4ED8;color:#fff}.bin.to{background:#DCFCE7;border-color:#22C55E;color:#166534}.bin.h{background:#FECACA;border-color:#F87171;color:#991B1B}'
 '.zf{margin-top:auto;display:flex;align-items:center;gap:6px;padding:0 9px 9px;font-size:8.8px;color:#71717A;white-space:nowrap}.zf .bt{margin-left:auto;font-size:8.8px;padding:3px 7px}'
 '.dk{margin:10px 10px 0;height:30px;border:1px solid #E4E4E7;border-radius:6px;display:flex;align-items:center;gap:8px;padding:0 10px;font-size:8.8px;color:#71717A;background:#FAFAFA}.dk i{width:26px;height:10px;border:1px solid #D4D4D8;border-radius:2px;background:#fff;display:inline-block}'
 '.scn{height:226px;flex:none;display:flex;flex-direction:column}.scn .frm{display:flex;align-items:flex-end;gap:6px;padding:9px 10px 0}.scn .fld{flex:1}.scn .smp{display:flex;align-items:center;gap:6px;padding:6px 10px 0;font-size:8.8px;color:#71717A}.scn .smp .bt{font-family:"JetBrains Mono",ui-monospace,monospace;font-size:9px;padding:3px 7px}'
 '.pi{padding:8px 10px 0;display:grid;grid-template-columns:1fr 1fr;gap:6px 8px}.pi .kv b{font-size:9.8px}.mv{display:flex;align-items:flex-end;gap:6px;padding:8px 10px 0}.mv .fld{flex:1}'
 '.zl{height:300px;flex:none;display:flex;flex-direction:column}.zl .row{grid-template-columns:1fr 46px;min-height:24px;font-size:9.2px;padding:0 10px;white-space:nowrap}.zl .row span:last-child{text-align:right;font-family:"JetBrains Mono",ui-monospace,monospace}'
 '.zl .sub{padding:7px 10px 4px;font-size:9px;color:#71717A}.zl .row.t{font-weight:600;background:#FAFAFA}.av{margin:8px 10px 0;padding:8px 10px;border-radius:7px;background:#F0FDF4;border:1px solid #BBF7D0;display:flex;align-items:baseline;justify-content:space-between}.av b{font-size:18px;font-weight:600;color:#14532D}.av span{font-size:9px;color:#166534}'
 '.av.lo{background:#FEF3C7;border-color:#FDE68A}.av.lo b{color:#92400E}.av.lo span{color:#92400E}'
 '.scn .empt,.zl .empt{margin:10px;flex:1}'
)

WIN = (
 header(ICON, 'Cold storage', 'Pallet locations, chicken broccoli entree FE-2210')
 + '<div class="g2"><div class="cd pln" id="pln"></div><div class="col"><div class="cd scn" id="scn">'
 '<div class="ct">Scan pallet</div><div class="frm"><label class="fld" id="fsc"><small>Pallet label</small><input id="isc" value="" placeholder="Scan or type a pallet" autocomplete="off" spellcheck="false"><span class="em" id="sem">No pallet found. Try P-0912</span></label><button type="button" class="bt pri" id="scb">Scan</button></div>'
 '<div class="smp">Sample<button type="button" class="bt" id="smp" data-sample>P-0912</button></div><div id="pin"></div></div><div class="cd zl" id="zl"></div></div></div>'
)

JS = r'''
var FOC='.hd>*,.pln .ct>*,.zn,.dk,.scn .ct,.scn .frm>*,.scn .smp,.pi,.mv>*,.zl .ct,.zl .tabs,.zl .row,.zl .sub,.av';
var Z=[['bf1','Blast freezer 1','BF1','Set point minus 30 F',false],['ha','Holding freezer A','HA','Set point minus 10 F',false],['ob','Outside cold store','OC','Third party, 2 miles',true],['hb','Holding freezer B','HB','Set point minus 10 F',false]];
var START={bf1:['R1-B1','R1-B2','R2-B3'],ha:'all',hb:['R1-B1','R1-B2','R1-B3','R2-B1','R2-B2','R2-B3','R2-B4','R3-B1'],ob:['R1-B1','R1-B2','R1-B3','R1-B4','R2-B1','R2-B2','R2-B3']};
var CPP=100,PAL='P-0912',FROM=['bf1','R2-B3'],TO=['hb','R1-B4'];
var LOTS={bf1:[['LT-5101',200,'Apr 12, 2027'],['LT-5108',100,'May 3, 2027']],ha:[['LT-4980',700,'Jan 20, 2027'],['LT-5022',500,'Feb 14, 2027']],hb:[['LT-5044',500,'Mar 2, 2027'],['LT-5060',300,'Mar 18, 2027']],ob:[['LT-4890',400,'Nov 30, 2026'],['LT-4931',300,'Dec 22, 2026']]};
var SO=[['SO-3318','Northfield Foods',1000],['SO-3322','Coastal Grocers',600]];
var S;
function allBins(){var o=[];for(var r=1;r<=3;r++)for(var b=1;b<=4;b++)o.push('R'+r+'-B'+b);return o;}
function fresh(){var m={};Z.forEach(function(z){var s=START[z[0]];m[z[0]]=(s==='all'?allBins():s).slice();});return m;}
function qty(k){return S.bins[k].length*CPP;}
function onhand(){return Z.reduce(function(a,z){return a+qty(z[0]);},0);}
function held(){return S.hold?qty('ob'):0;}
function committed(){return SO.reduce(function(a,s){return a+s[2];},0);}
function avail(){return onhand()-held()-committed();}
function lots(k){var L=LOTS[k].slice();if(S.moved){if(k===FROM[0])L=L.filter(function(l){return l[0]!=='LT-5108';});if(k===TO[0])L.push(['LT-5108',CPP,'May 3, 2027']);}return L;}
function zname(k){for(var i=0;i<Z.length;i++)if(Z[i][0]===k)return Z[i][1];}
function render(){
var p='<div class="ct"><span>Plant 2 cold storage</span>'+(S.scan?'<span class="ch c-info" id="tot">'+n0(onhand())+' cases on hand</span>':'<span class="ch c-idle">Scan a pallet</span>')+'</div><div class="zs">';
Z.forEach(function(z){var k=z[0],hd=S.hold&&k==='ob',lit=S.scan&&((!S.moved&&k===FROM[0])||(S.moved&&k===TO[0]));
p+='<div class="zn'+(z[4]?' off':'')+(hd?' hd':'')+(lit?' lit':'')+'" id="zn-'+k+'"><button type="button" class="zh" id="z-'+k+'">'+z[1]+(S.scan?'<span class="ch '+(hd?'c-bad':'c-idle')+'" id="q-'+k+'">'+n0(qty(k))+' cases</span>':'')+'</button><div class="rk">';
for(var r=1;r<=3;r++){p+='<div class="rr"><span>R'+r+'</span>';for(var b=1;b<=4;b++){var id='R'+r+'-B'+b,has=S.scan&&S.bins[k].indexOf(id)>-1,me=S.scan&&!S.moved&&k===FROM[0]&&id===FROM[1],to=S.moved&&k===TO[0]&&id===TO[1];
p+='<span class="bin'+(me?' me':to?' to':hd&&has?' h':has?' f':'')+'">'+(me||to?PAL.slice(2):'B'+b)+'</span>';}p+='</div>';}
p+='</div><div class="zf"><span>'+z[3]+'</span>'+(k==='ob'&&S.st&&!S.hold?'<button type="button" class="bt" id="qh">Quality hold</button>':hd?'<span class="ch c-bad" style="margin-left:auto">Quality hold</span>':'')+'</div></div>';});
p+='</div><div class="dk"><span>Dock</span><i></i><i></i><i></i><span class="mut">Doors 1 to 3, receiving and shipping</span></div>';
$('pln').innerHTML=p;
var pi='';if(S.scan){var loc=S.moved?zname(TO[0])+', '+TO[1].replace('-',', ').replace('R','rack ').replace('B','bin '):zname(FROM[0])+', rack 2, bin 3';
pi='<div class="pi in"><div class="kv"><small>Pallet</small><b class="mono">'+PAL+'</b></div><div class="kv"><small>Cases</small><b class="mono">'+CPP+'</b></div><div class="kv"><small>Lot</small><b class="mono">LT-5108</b></div><div class="kv"><small>Expires</small><b>May 3, 2027</b></div><div class="kv" style="grid-column:span 2"><small>Location</small><b id="ploc">'+loc+'</b></div></div>';
pi+='<div class="mv frm"><label class="fld" id="fmv"><small>Move to bin</small><input id="imv" value="'+S.v+'" autocomplete="off" spellcheck="false"><span class="em">Use a bin like HB-R1-B4</span></label>'+(S.moved?'<button type="button" class="bt done" disabled>Moved</button>':'<button type="button" class="bt" id="mvb">Move</button>')+'</div>';}
$('pin').innerHTML=pi;
var t='<div class="ct">'+(S.tab==='st'?'Stock, all zones':S.tab==='zl'?'Zone lots':'Zone and stock')+'</div>';
if(!S.scan)t+='<div class="empt"><b>Nothing scanned yet</b><span>Lots by zone and available stock show once a pallet is scanned.</span></div>';
else{t+='<div class="tabs"><button type="button" class="tab'+(S.tab==='zl'?' on':'')+'" id="t-zl">Zone lots</button><button type="button" class="tab'+(S.tab==='st'?' on':'')+'" id="t-st">Stock</button></div>';
if(S.tab==='zl'&&S.zone){var L=lots(S.zone);t+='<div class="sub in">'+zname(S.zone)+', '+n0(qty(S.zone))+' cases</div><div class="row h"><span>Lot, expires</span><span>Cases</span></div>'+
L.map(function(l){return '<div class="row in"><span><span class="mono">'+l[0]+'</span> <span class="mut">'+l[2]+'</span></span><span>'+n0(l[1])+'</span></div>';}).join('')+'<div class="row t"><span>Total</span><span id="zlt">'+n0(L.reduce(function(a,l){return a+l[1];},0))+'</span></div>';}
else if(S.tab==='zl')t+='<div class="sub">Pick a zone on the plan to see its lots and expiry dates.</div>';
else{t+='<div class="av'+(S.hold?' lo':'')+' in"><span>Available to promise</span><b id="sav">'+n0(avail())+'</b></div><div class="row" style="margin-top:6px"><span>On hand</span><span id="soh">'+n0(onhand())+'</span></div><div class="row"><span>On quality hold</span><span id="shd">'+n0(held())+'</span></div>'+
SO.map(function(s){return '<div class="row"><span><span class="mono">'+s[0]+'</span> <span class="mut">'+s[1]+'</span></span><span>'+n0(s[2])+'</span></div>';}).join('')+'<div class="row t"><span>Committed</span><span id="scm">'+n0(committed())+'</span></div>';}}
$('zl').innerHTML=t;
}
$('scn').addEventListener('input',function(e){if(e.target.id==='imv')S.v=e.target.value;});
$('smp').addEventListener('click',function(){$('isc').value=PAL;$('fsc').classList.remove('err');});
function sval(){return String($('isc').value).trim().toUpperCase().replace(/\s/g,'');}
function typeIt(done){var t=PAL,i=0;(function k(){$('isc').value=t.slice(0,i);if(i<t.length){i++;later(k,60);}else done();})();}
function resetState(){S={scan:false,zone:null,tab:'zl',moved:false,st:false,hold:false,bins:fresh(),v:'HB-R1-B4'};$('isc').value='';$('fsc').classList.remove('err');render();}
var CAPAT=function(hh){return cur===2||cur===3?{l:14,t:visH()-hh-14}:{l:14,t:96};};
var ST=[
{id:'scan',target:function(){return mode==='try'?$('scb'):$('isc');},prompt:'Type P-0912 or pick the sample, then Scan',where:'below',
 ok:function(){var v=sval(),b=!(v==='P-0912'||v==='P0912');$('sem').textContent=v?'No pallet found. Try P-0912':'Scan a pallet, for example P-0912';$('fsc').classList.toggle('err',b);return !b;},
 run:function(quick){var go=function(){$('isc').value=PAL;$('fsc').classList.remove('err');S.scan=true;render();};if(mode==='watch'&&!quick)typeIt(go);else go();},
 after:function(){return['Every pallet has a place, down to the bin',PAL+': '+CPP+' cases in Blast freezer 1, rack 2, bin 3. '+n0(onhand())+' cases across four zones.'];}},
{id:'zone',target:function(){return $('z-bf1');},prompt:'Open Blast freezer 1',where:'below',run:function(){S.zone='bf1';S.tab='zl';render();},
 after:function(){return['Each zone lists its lots with expiry dates','Blast freezer 1 holds LT-5101, 200 cases, and LT-5108, 100 cases. '+n0(qty('bf1'))+' in all.'];}},
{id:'move',target:function(){return $('mvb');},prompt:'Move the pallet to HB-R1-B4',where:'below',
 ok:function(){var v=String(S.v).trim().toUpperCase(),b=v!=='HB-R1-B4';$('fmv').classList.toggle('err',b);return !b;},
 run:function(){var a=S.bins[FROM[0]];a.splice(a.indexOf(FROM[1]),1);S.bins[TO[0]].push(TO[1]);S.moved=true;S.zone=TO[0];render();},
 after:function(){return['A scan moves the pallet, and both zones update','Blast freezer 1 '+n0(qty('bf1'))+', Holding freezer B '+n0(qty('hb'))+'. Total still '+n0(onhand())+'.'];}},
{id:'st',target:function(){return $('t-st');},prompt:'Open the Stock tab',where:'below',run:function(){S.tab='st';S.st=true;render();},
 after:function(){return['Available follows open orders and holds',n0(onhand())+' on hand, '+n0(committed())+' committed to SO-3318 and SO-3322, '+n0(avail())+' available.'];}},
{id:'hold',target:function(){return $('qh');},prompt:'Put the outside cold store on hold',where:'above',run:function(){S.hold=true;render();},
 after:function(){return['A quality hold comes off available straight away','Outside cold store '+n0(qty('ob'))+' cases held. Available drops to '+n0(avail())+'.'];}}];
'''
