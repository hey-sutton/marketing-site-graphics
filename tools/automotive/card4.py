"""Automotive card 4: Quality, Non Conformance & Audit Records (working title). Layout: measurement chart, record panel and
an 8D timeline, with the audit record checklist beside them. Readings are kept in microns so the tolerance check is exact.
The card shows the records Sutton keeps. It makes no claim about certification or compliance status."""
from frame_auto import header

SUMMARY = 'Quality, Non Conformance & Audit Records (a failed in process bore inspection on WO-7108 opens NCR-0318, the disposition splits rework and scrap, the corrective action is tracked D1 to D8 and the audit record completes)'
ARIA = 'Interactive product screen: open the WO-7108 bore diameter inspection, check 20 readings against 12.00 plus or minus 0.05 mm, open NCR-0318 for 140 pieces of lot FGL-0913, record 90 rework and 50 scrap, and complete the audit record'
STEPS = 5
STUDIO = dict(lede='A typical inspection and NCR screen, built on your Sutton data with Studio. Want it different? Describe the change.',
              examples=['A control chart with run rules', 'A customer 8D report as a PDF', 'A gauge calibration due list', 'A layered process audit checklist'],
              built_on='Inspections, lots, work orders and NCRs', change='Fields, checks and sign offs')

ICON = '<path d="M8 1.8l5 2v4c0 3.2-2.2 5.3-5 6.4-2.8-1.1-5-3.2-5-6.4v-4z"/><path d="M5.6 8.1l1.7 1.7 3.2-3.4"/>'

CSS = (
 '.g4{display:grid;grid-template-columns:206px 1fr;gap:10px;padding:10px 40px 0 16px}'
 '.col{display:flex;flex-direction:column;gap:10px;min-width:0}'
 '.ins .row{grid-template-columns:1fr auto;min-height:34px;padding:3px 10px;font-size:9.5px}.ins .row .t{display:flex;flex-direction:column;gap:1px;line-height:1.25;min-width:0}.ins .row .t span{color:#71717A;font-size:8.8px;white-space:nowrap}'
 '.aud{height:300px;flex:none;display:flex;flex-direction:column}.aud .pg{height:5px;border-radius:3px;background:#F0F0F1;margin:9px 10px 2px;overflow:hidden}.aud .pg i{display:block;height:100%;background:#16A34A;border-radius:3px;transition:width .45s ease}'
 '.ci{display:grid;grid-template-columns:18px 1fr;gap:7px;padding:5px 10px;border-top:1px solid #F7F7F8;font-size:9.6px;line-height:1.3}.ci:first-of-type{border-top:0}.ci .bx{width:16px;height:16px;border-radius:4px;border:1px solid #D4D4D8;display:grid;place-items:center;background:#fff;transition:background-color .3s}'
 '.ci.ok .bx{background:#16A34A;border-color:#16A34A}.ci span{display:block;color:#71717A;font-size:8.8px}.aud .ft{margin-top:auto;padding:8px 10px 10px;border-top:1px solid #F0F0F1;display:flex;flex-direction:column;gap:6px;font-size:9px;color:#52525B}'
 '.chr{height:200px;flex:none;display:flex;flex-direction:column}.chr .ct .bt{font-size:9.4px;padding:4px 9px}.chr .pl{position:relative;height:150px;margin:8px 10px 0 10px}.chr svg{position:absolute;left:0;top:0;overflow:visible}'
 '.chr .yl{font-size:8.2px;fill:#A1A1AA;font-family:"JetBrains Mono",ui-monospace,monospace}.chr .bd{fill:#DCFCE7;opacity:0;transition:opacity .4s}.chr.on .bd{opacity:1}.chr .lm{stroke:#86EFAC;stroke-width:1;opacity:0;transition:opacity .4s}.chr.on .lm{opacity:1}'
 '.chr .nm{stroke:#A1A1AA;stroke-dasharray:3 3;stroke-width:1}.chr .pt{fill:#71717A;transition:fill .4s}.chr.on .pt.in{fill:#16A34A}.chr.on .pt.out{fill:#DC2626}.chr .ol{font-size:8.4px;font-weight:600;fill:#B91C1C;font-family:"JetBrains Mono",ui-monospace,monospace}.chr .tr{stroke:#D4D4D8;stroke-width:1;fill:none}'
 '.ncr{height:290px;flex:none;display:flex;flex-direction:column}.fg{display:grid;grid-template-columns:repeat(4,1fr);gap:8px 10px;padding:9px 11px;border-bottom:1px solid #F0F0F1}.fg .kv b{font-size:10px}'
 '.dsp{display:flex;align-items:flex-end;gap:8px;padding:8px 11px;border-bottom:1px solid #F0F0F1}.dsp .fld{width:62px}.dsp .sb2{flex:1;display:flex;flex-direction:column;gap:4px;font-size:8.8px;color:#71717A;min-width:0}'
 '.spb{display:flex;height:16px;border-radius:4px;overflow:hidden;background:#F4F4F5}.spb i{display:grid;place-items:center;font-style:normal;font-size:8.4px;font-weight:600;color:#fff;transition:width .5s ease}.spb .rw{background:#2563EB}.spb .sc{background:#DC2626}'
 '.d8{padding:9px 11px 0;display:flex;flex-direction:column;gap:6px}.d8 .tl{display:grid;grid-template-columns:repeat(8,1fr);position:relative}.d8 .tl::before{content:"";position:absolute;left:6%;right:6%;top:8px;height:1px;background:#E4E4E7}'
 '.dp{display:flex;flex-direction:column;align-items:center;gap:3px;font-size:8.4px;color:#71717A;position:relative;text-align:center;line-height:1.2}.dp i{width:17px;height:17px;border-radius:50%;border:1px solid #D4D4D8;background:#fff;display:grid;place-items:center;font-style:normal;font-size:7.8px;font-weight:600;color:#71717A}'
 '.dp.ok i{background:#16A34A;border-color:#16A34A;color:#fff}.dp.nw i{border-color:#18181B;color:#18181B;box-shadow:0 0 0 3px #F4F4F5}.d8 .cs{display:flex;gap:14px;font-size:9.2px;color:#52525B;white-space:nowrap}.d8 .cs b{color:#18181B;font-weight:600}'
 '.nte{font-size:9px;color:#71717A;padding:2px 2px 0;white-space:nowrap}'
 '.chr .empt,.ncr .empt,.aud .empt{margin:10px;flex:1}'
)

WIN = (
 header(ICON, 'Quality', 'Inspection records, bracket assembly BA-5520')
 + '<div class="g4"><div class="col"><div class="cd ins" id="ins"></div><div class="cd aud" id="aud"></div></div>'
 '<div class="col"><div class="cd chr" id="chr"></div><div class="cd ncr" id="ncr"></div><div class="nte" id="nte"></div></div></div>'
)

JS = r'''
var FOC='.hd>*,.ins .ct,.ins .row,.aud .ct,.aud .pg,.ci,.aud .ft>*,.chr .ct>*,.chr .pl,.ncr .ct,.fg,.dsp>*,.d8,.nte';
var INS=[['WO-7108','Bore diameter, in process','Review'],['WO-7102','Flange flatness','Passed'],['WO-7115','Hole position','Passed'],['RCV-2291','FST-121 thread gauge','Passed'],['WO-7096','Weld pull test','Passed']];
var NOM=12000,TOL=50,AFF=140;
var RD=[12000,11990,12010,12000,12020,11980,12010,12020,12010,12030,12020,12040,12030,12070,12040,12030,12080,12040,12060,12040];
var CHK=[['Inspection plan','IP-5520-04, rev 3, 20 per lot'],['Measurements','20 readings, bore gauge BG-12'],['Disposition','Recorded on NCR-0318'],['Corrective action','8D with cause and owner'],['Sign off','Quality manager']];
var D8=['Team','Problem','Contain','Cause','Fix','Verify','Prevent','Close'];
var S;
function isIn(v){return Math.abs(v-NOM)<=TOL;}
function nIn(){return RD.filter(isIn).length;}
function outs(){return RD.filter(function(v){return !isIn(v);});}
function mm(v){return (v/1000).toFixed(2);}
function done(){return [S.sel,S.chk,S.dsp,S.ncr,S.sign];}
function nDone(){return done().filter(Boolean).length;}
function render(){
$('ins').innerHTML='<div class="ct">Inspections<span class="mut" style="font-weight:500">Today</span></div>'+INS.map(function(x,i){var st=i===0&&S.ncr?'NCR open':x[2];return '<button type="button" class="row'+(S.sel&&i===0?' sel':'')+'" id="i-'+x[0]+'"><span class="t"><b class="mono">'+x[0]+'</b><span>'+x[1]+'</span></span><span class="ch '+(st==='Passed'?'c-ok':st==='NCR open'?'c-bad':'c-warn')+'">'+st+'</span></button>';}).join('');
var a='<div class="ct">Audit record<span class="ch '+(S.sign?'c-ok':S.sel?'c-warn':'c-idle')+'" id="acnt">'+(S.sel?nDone()+' of 5'+(S.sign?' complete':''):'Not started')+'</span></div>';
if(!S.sel)a+='<div class="empt"><b>No record open</b><span>Pick an inspection to start its audit record.</span></div>';
else{a+='<div class="pg"><i style="width:'+(nDone()*20)+'%"></i></div>'+CHK.map(function(c,i){var ok=done()[i];return '<div class="ci'+(ok?' ok':'')+'"><span class="bx">'+(ok?'<svg width="10" height="10" viewBox="0 0 10 10" fill="none" aria-hidden="true"><path d="M2 5.2l2 2 4-4.4" stroke="#fff" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>':'')+'</span><span><b>'+c[0]+'</b><span>'+(i===2&&S.dsp?'Rework '+n0(S.rw)+', scrap '+n0(S.sc):i===4&&S.sign?'K. Moreno, Nov 11':ok?c[1]:'Pending')+'</span></span></div>';}).join('');
a+='<div class="ft">'+(S.sign?'<span class="ch c-ok" style="align-self:flex-start">Audit record complete</span><span>Inspection records, NCR and 8D kept with lot FGL-0913.</span>':'<button type="button" class="bt'+(S.dsp?' pri':'')+'" id="sgn" style="align-self:flex-start"'+(S.dsp?'':' disabled')+'>Sign off record</button><span>'+(S.dsp?'Every item is in. Sign off to close the record.':'Sign off opens once the disposition is in.')+'</span>')+'</div>';}
$('aud').innerHTML=a;
var c='<div class="ct"><span>'+(S.sel?'Bore diameter, WO-7108':'Measurements')+'</span>'+(S.sel?'<span class="mut" style="font-weight:500;margin-left:6px;margin-right:auto">'+mm(NOM)+' mm, plus or minus '+mm(TOL).replace(/^0/,'0')+'</span>':'')+(S.chk?'<span class="ch c-bad" id="cin">'+nIn()+' in, '+outs().length+' out</span>':S.sel?'<button type="button" class="bt" id="tol">Check against tolerance</button>':'')+'</div>';
if(!S.sel)c+='<div class="empt"><b>No inspection selected</b><span>Readings plot here against the tolerance band.</span></div>';
else{var W=394,H=136,L=34,lo=11920,hi=12100,yy=function(v){return H-(v-lo)/(hi-lo)*H;},xx=function(i){return L+8+i*((W-L-16)/(RD.length-1));};
var g='<svg width="'+W+'" height="'+(H+14)+'" viewBox="0 0 '+W+' '+(H+14)+'" aria-hidden="true"><rect class="bd" x="'+L+'" y="'+yy(NOM+TOL)+'" width="'+(W-L)+'" height="'+(yy(NOM-TOL)-yy(NOM+TOL))+'"/>'+
'<line class="lm" x1="'+L+'" x2="'+W+'" y1="'+yy(NOM+TOL)+'" y2="'+yy(NOM+TOL)+'"/><line class="lm" x1="'+L+'" x2="'+W+'" y1="'+yy(NOM-TOL)+'" y2="'+yy(NOM-TOL)+'"/><line class="nm" x1="'+L+'" x2="'+W+'" y1="'+yy(NOM)+'" y2="'+yy(NOM)+'"/>';
[11950,12000,12050].forEach(function(v){g+='<text class="yl" x="'+(L-4)+'" y="'+(yy(v)+3)+'" text-anchor="end">'+mm(v)+'</text>';});
g+='<polyline class="tr" points="'+RD.map(function(v,i){return xx(i)+','+yy(v);}).join(' ')+'"/>';
RD.forEach(function(v,i){g+='<circle class="pt '+(isIn(v)?'in':'out')+'" cx="'+xx(i)+'" cy="'+yy(v)+'" r="3.2"/>';if(S.chk&&!isIn(v))g+='<text class="ol" x="'+xx(i)+'" y="'+(yy(v)-7)+'" text-anchor="middle">'+mm(v)+'</text>';});
g+='<text class="yl" x="'+L+'" y="'+(H+12)+'">Sample 1</text><text class="yl" x="'+W+'" y="'+(H+12)+'" text-anchor="end">Sample '+RD.length+'</text></svg>';
c+='<div class="pl'+(S.an1?' in':'')+'">'+g+'</div>';}
$('chr').innerHTML=c;$('chr').classList.toggle('on',S.chk);
var n='<div class="ct">'+(S.ncr?'<span><span class="mono">NCR-0318</span> Non conformance</span><span class="ch c-bad">Open</span>':'<span>Non conformance</span>')+'</div>';
if(!S.ncr)n+='<div class="empt"><b>No NCR open</b><span>Readings outside the band open an NCR with the lot and work order filled in.</span>'+(S.sel?'<button type="button" class="bt'+(S.chk?' pri':'')+'" id="onc" style="margin-top:4px"'+(S.chk?'':' disabled')+'>Open NCR</button>':'')+'</div>';
else{n+='<div class="fg'+(S.an2?' in':'')+'"><div class="kv"><small>Work order</small><b class="mono">WO-7108</b></div><div class="kv"><small>Lot</small><b class="mono">FGL-0913</b></div><div class="kv"><small>Characteristic</small><b>Bore diameter</b></div><div class="kv"><small>Out of tolerance</small><b class="mono">'+outs().map(mm).join(', ')+'</b></div>'+
'<div class="kv"><small>Pieces affected</small><b class="mono" id="aff">'+n0(AFF)+'</b></div><div class="kv"><small>Found at</small><b>In process, Line 2</b></div><div class="kv"><small>Raised by</small><b>J. Okafor</b></div><div class="kv"><small>Sample</small><b class="mono">'+nIn()+' of '+RD.length+' in</b></div></div>';
n+='<div class="dsp frm"><label class="fld" id="frw"><small>Rework</small><input id="irw" value="'+S.v.rw+'" inputmode="numeric" autocomplete="off"><span class="em">Sum to 140</span></label><label class="fld" id="fsc"><small>Scrap</small><input id="isc" value="'+S.v.sc+'" inputmode="numeric" autocomplete="off"><span class="em">Sum to 140</span></label>'+
(S.dsp?'<span class="sb2"><span id="dsum">Rework '+n0(S.rw)+' and scrap '+n0(S.sc)+', '+n0(S.rw+S.sc)+' of '+n0(AFF)+'</span><span class="spb"><i class="rw" style="width:'+(S.rw/AFF*100)+'%">'+n0(S.rw)+'</i><i class="sc" style="width:'+(S.sc/AFF*100)+'%">'+n0(S.sc)+'</i></span></span>':'<button type="button" class="bt" id="rdp">Record disposition</button><span class="sb2">Each piece is reworked or scrapped, and the two must cover all '+n0(AFF)+'.</span>')+'</div>';
var dn=S.sign?5:4;n+='<div class="d8"><div class="tl">'+D8.map(function(d,i){var ok=i<dn,nw=i===dn;return '<span class="dp'+(ok?' ok':nw?' nw':'')+'"><i>D'+(i+1)+'</i>'+d+'</span>';}).join('')+'</div><div class="cs"><span>Cause <b>Tool wear on spindle 3</b></span><span>Owner <b>R. Diaz</b></span><span>Due <b>Nov 25</b></span></div></div>';}
$('ncr').innerHTML=n;
$('nte').textContent='Inspection records stay linked to the work order, the lot and any NCR.';
S.an1=S.an2=false;}
$('ncr').addEventListener('input',function(e){if(e.target.id==='irw')S.v.rw=e.target.value;if(e.target.id==='isc')S.v.sc=e.target.value;});
function ival(v){v=String(v).trim().replace(/,/g,'');return /^\d{1,4}$/.test(v)?parseInt(v,10):null;}
function resetState(){S={sel:false,chk:false,ncr:false,dsp:false,sign:false,rw:0,sc:0,v:{rw:'90',sc:'50'}};render();}
var CAPAT=function(hh){return cur>=4?{l:visW()-cap.offsetWidth-14,t:96}:cur<=1?{l:visW()-cap.offsetWidth-14,t:visH()-hh-14}:{l:14,t:visH()-hh-14};};
var ST=[
{id:'sel',target:function(){return $('i-WO-7108');},prompt:'Open the WO-7108 inspection',where:'right',run:function(){S.sel=true;S.an1=true;render();},
 after:function(){return['Every in process inspection keeps its plan and readings','WO-7108 bore diameter, '+mm(NOM)+' mm plus or minus '+mm(TOL)+', a sample of '+RD.length+'.'];}},
{id:'chk',target:function(){return $('tol');},prompt:'Check the readings against tolerance',where:'below',run:function(){S.chk=true;render();},
 after:function(){return['Readings outside the band are flagged as they come in',nIn()+' of '+RD.length+' inside, '+outs().length+' outside at '+outs().map(mm).join(', ')+' mm.'];}},
{id:'ncr',target:function(){return $('onc');},prompt:'Open the NCR',where:'above',run:function(){S.ncr=true;S.an2=true;render();},
 after:function(){return['The non conformance opens with the facts filled in','NCR-0318 on WO-7108, lot FGL-0913, '+n0(AFF)+' pieces. Cause: tool wear on spindle 3.'];}},
{id:'dsp',target:function(){return $('rdp');},prompt:'Record the disposition',where:'above',
 ok:function(){var r=ival(S.v.rw),s=ival(S.v.sc),b=r===null||s===null||r+s!==AFF;$('frw').classList.toggle('err',b);$('fsc').classList.toggle('err',b);return !b;},
 run:function(){S.rw=ival(S.v.rw);S.sc=ival(S.v.sc);S.dsp=true;render();},
 after:function(){return['The disposition is split and has to cover every piece','Rework '+n0(S.rw)+' and scrap '+n0(S.sc)+', '+n0(S.rw+S.sc)+' of '+n0(AFF)+' pieces.'];}},
{id:'sgn',target:function(){return $('sgn');},prompt:'Sign off the audit record',where:'above',run:function(){S.sign=true;render();},
 after:function(){return['The audit record assembles itself as the work is done',nDone()+' of 5 complete: plan, measurements, disposition, corrective action and sign off.'];}}];
'''
