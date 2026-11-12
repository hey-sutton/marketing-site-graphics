"""Textile card 1: Roll & Dye Lot Control. Layout: list with a record panel.
Left, the serialized roll table (roll ID, dye lot chip, shade, length, bin, status). Right, the selected roll's label with
a barcode and dye lot chip, its record, and order SO-3318's reservation. A summary strip runs across the bottom.
Scan a roll, reserve 360 yd from one dye lot, see a mixed lot pick blocked, split a roll and keep its lot.
Every figure comes from tools/textile/data.py, where the brief's sums are asserted."""
import json
import data as D
from frame_textile import header

SUMMARY = 'Roll & Dye Lot Control (scan a roll label, reserve SO-3318 from one dye lot, block a pick from another lot, split a roll and keep its lot)'
ARIA = 'Interactive demo: scan a fabric roll, reserve rolls from one dye lot and split a roll.'
STEPS = 4
STUDIO = dict(lede='A typical roll and dye lot screen, built on your Sutton data with Studio. Want it different? Describe the change.',
              examples=['A shade approval status on each roll', 'GSM and thread count on the label', 'A lab dip reference on the lot', 'Limits on who can override a lot mismatch'],
              built_on='Roll labels, serialized inventory and reservations', change='Fields, label layout and lot rules')

ICON = '<ellipse cx="4" cy="8" rx="2" ry="5"/><path d="M4 3h7.5c1.1 0 2 2.2 2 5s-.9 5-2 5H4"/><path d="M4 6.5v3"/>'

ROLLS = ([dict(id=i, lot=D.LOT, sh=D.SHADE, yd=q, bin=b, st='av') for i, q, b in D.AVAIL]
         + [dict(id=i, lot=D.LOT, sh=D.SHADE, yd=q, bin=b, st='hd') for i, q, b in D.HELD]
         + [dict(id=D.OTHER[0], lot=D.OTHER[1], sh=D.OTHER[2], yd=D.OTHER[3], bin='C-11', st='av')])

CSS = (
 '.g1{padding:10px 0 0 16px;display:flex;flex-direction:column;gap:10px}.g1>*{width:656px;flex:none}'
 '.srch{height:44px;display:flex;align-items:center;gap:8px;padding:0 10px}.srch .fld{flex-direction:row;align-items:center;gap:8px;position:relative}'
 '.srch .fld small{font-size:10px;color:#18181B;font-weight:600;white-space:nowrap}.srch .fld input{width:168px;font-size:10.6px;padding:6px 8px}.srch .fld .em{position:absolute;left:30px;top:34px;white-space:nowrap}'
 '.smp{display:inline-flex;align-items:center;gap:5px;font-size:9.4px;color:#71717A;margin-left:4px}.smp .bt{font-family:"JetBrains Mono",ui-monospace,monospace;font-size:9.6px;padding:4px 8px}'
 '.mid{display:grid;grid-template-columns:384px 262px;gap:10px;height:380px}'
 '.tb{display:flex;flex-direction:column}.tb .row{grid-template-columns:66px 70px 46px 40px 32px 1fr;gap:6px;font-size:9.6px;min-height:28px}.tb .row.h{min-height:24px}.tb .row.sp{min-height:32px}'
 '.rid{display:flex;flex-direction:column;line-height:1.2}.rid small{font-size:7.8px;color:#71717A;font-family:Inter,sans-serif;letter-spacing:0}'
 '.stc{display:flex;align-items:center;gap:4px}.bt.spl{font-size:8.8px;padding:2px 7px}'
 '.tf{margin-top:auto;border-top:1px solid #E4E4E7;padding:8px 11px;font-size:9.2px;color:#52525B;background:#FAFAFA;white-space:nowrap}.tf b{color:#18181B;font-weight:600}'
 '.tb .empt{margin:10px;flex:1}.lb .empt,.sm .empt{margin:8px 10px;flex:1;padding:8px}'
 '.rc{display:flex;flex-direction:column;gap:10px;min-width:0}'
 '.lb{height:172px;flex:none;display:flex;flex-direction:column}.lab{margin:9px 10px 6px;border:1px dashed #D4D4D8;border-radius:6px;padding:7px 9px;display:grid;grid-template-columns:1fr auto;align-items:center;gap:5px 8px}'
 '.lab .bcd{grid-column:1/3;width:100%;height:24px;fill:#18181B}.lab .lid{font-size:14px;font-weight:600}.lab .par{grid-column:1/3;font-size:8.6px;color:#71717A;margin-top:-3px}'
 '.ch.lot{font-family:"JetBrains Mono",ui-monospace,monospace;font-size:9px}.lab .ch.lot{font-size:10px;padding:3px 7px}'
 '.kvg{display:grid;grid-template-columns:repeat(3,1fr);gap:6px 8px;padding:2px 11px 0}.kvg .kv b{font-size:10px}'
 '.rs{flex:1;display:flex;flex-direction:column;min-height:0}.pr{padding:7px 11px 6px;display:flex;flex-direction:column;gap:5px;font-size:9.2px}'
 '.pr .bar{height:7px;border-radius:4px;background:#F0F0F1;overflow:hidden}.pr .bar i{display:block;height:100%;background:#18181B;transition:width .6s ease,background-color .4s}.pr .bar i.full{background:#16A34A}'
 '.pr .t{display:flex;justify-content:space-between;color:#52525B}.pr .t b{color:#18181B;font-weight:600}'
 '.pk{display:grid;grid-template-columns:1fr auto;padding:0 11px;font-size:9.2px;line-height:19px;border-top:1px solid #F4F4F5}'
 '.ac{margin-top:auto;padding:7px 11px 9px;display:flex;align-items:center;gap:6px;border-top:1px solid #F0F0F1}.ac .fld{flex-direction:row;align-items:center;gap:6px;position:relative}'
 '.ac .fld small{white-space:nowrap}.ac .fld input{width:92px}.ac .fld .em{position:absolute;bottom:27px;left:0;white-space:nowrap}.ac .mut{font-size:8.8px}'
 '.blk{margin:auto 10px 9px;padding:7px 9px;border-radius:7px;background:#FEF2F2;border:1px solid #FECACA;color:#991B1B;font-size:9px;line-height:1.35;display:flex;flex-direction:column;gap:6px}'
 '.blk b{font-weight:600}.blk .bt{align-self:flex-start;font-size:9px;padding:3px 8px;border-color:#FCA5A5;color:#991B1B;background:#fff}.blk .nt{color:#7F1D1D;font-size:8.6px}'
 '.sm{height:84px;display:flex;flex-direction:column}.tls{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;padding:8px 10px 0;width:560px}'
 '.tl{border:1px solid #F0F0F1;border-radius:7px;padding:6px 9px;height:52px;display:flex;flex-direction:column;justify-content:space-between;background:#FAFAFA;min-width:0}'
 '.tl small{font-size:8.8px;color:#71717A;white-space:nowrap}.tl b{font-size:14.5px;font-weight:600;letter-spacing:-.01em;white-space:nowrap}.tl em{font-style:normal;font-size:8.4px;color:#71717A;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}'
 '.tl.ok{background:#F0FDF4;border-color:#BBF7D0}.tl.bad{background:#FEF2F2;border-color:#FECACA}.ln{padding:6px 11px 0;font-size:9.2px;color:#52525B;white-space:nowrap}'
 '.od{padding:4px 11px 0;display:grid;grid-template-columns:1fr 1fr;gap:6px 8px}.od .kv b{font-size:9.8px}'
)

WIN = (
 header(ICON, 'Rolls', 'Inventory, serialized roll goods')
 + '<div class="g1"><div class="cd srch frm" id="srch"><label class="fld" id="frin"><small>Roll</small><input id="rin" value="" placeholder="Scan or type a roll ID" autocomplete="off" spellcheck="false" aria-label="Roll ID">'
 '<span class="em" id="rem">No roll found. Try R-48214</span></label><button type="button" class="bt pri" id="scn">Scan</button>'
 '<span class="smp">Sample<button type="button" class="bt" data-sample data-v="R-48211">R-48211</button><button type="button" class="bt" data-sample data-v="R-48330">R-48330</button></span>'
 '<span class="grow"></span><span class="ch c-idle" id="sst">No roll scanned</span></div>'
 '<div class="mid"><div class="cd tb" id="tb"></div><div class="rc"><div class="cd lb" id="lb"></div><div class="cd rs" id="rs"></div></div></div>'
 '<div class="cd sm" id="sm"></div></div>'
)

JS = r'''
var FOC='.hd>*,.srch>*,.tb .ct,.tb .row,.tf,.lb,.rs .ct,.pr,.pk,.ac>*,.blk,.sm .tl,.ln';
var LOT='@LOT@',SO='@SO@',NEED=@NEED@,RES=@RES@,SPL=@SPL@,WID=@WID@;
var ROLLS=@ROLLS@;
var S;
function sum(a){return a.reduce(function(x,y){return x+y;},0);}
function find(id){return rows().filter(function(r){return r.id===id;})[0]||ROLLS.filter(function(r){return r.id===id;})[0];}
function rows(){var out=[];ROLLS.forEach(function(r){if(S.spl&&r.id===SPL[0]){out.push({id:SPL[0]+'-A',lot:r.lot,sh:r.sh,yd:SPL[1],bin:r.bin,st:'av',par:SPL[0]});out.push({id:SPL[0]+'-B',lot:r.lot,sh:r.sh,yd:SPL[2],bin:r.bin,st:'av',par:SPL[0]});}else out.push(r);});return out;}
function st(r){if(S.blk&&r.lot!==LOT)return 'bl';if(S.rsv&&RES.indexOf(r.id)>-1)return 'rs';return r.st;}
var STX={av:['c-ok','Available'],hd:['c-warn','Held, shade check'],rs:['c-info','Reserved, '+SO],bl:['c-bad','Blocked on '+SO]};
function lotChip(l,bad){return '<span class="ch lot '+(bad?'c-bad':l===LOT?'c-info':'c-idle')+'">'+l+'</span>';}
function inLot(f){return sum(ROLLS.filter(function(r){return r.lot===LOT&&f(r);}).map(function(r){return r.yd;}));}
function resYd(){return S.rsv?sum(RES.map(function(id){return find(id).yd;})):0;}
function availYd(){return sum(ROLLS.filter(function(r){return r.lot===LOT&&r.st==='av'&&!(S.rsv&&RES.indexOf(r.id)>-1);}).map(function(r){return r.yd;}));}
function bars(id){var x=0,s='';for(var i=0;i<id.length;i++){var c=id.charCodeAt(i)*7+i*3;for(var k=0;k<4;k++){var w=1+((c>>k)&1)+((c>>(k+4))&1);s+='<rect x="'+x+'" y="0" width="'+w+'" height="24"/>';x+=w+1+((c>>(k+2))&1);}}
return '<svg class="bcd" viewBox="0 0 '+x+' 24" preserveAspectRatio="none" aria-hidden="true">'+s+'</svg>';}
function render(){
var t='<div class="ct"><span>'+(S.scan?'Navy twill TW-5810, 58 in':'Rolls')+'</span>'+(S.scan?'<span class="ch c-idle">'+rows().length+' rolls in stock</span>':'')+'</div>';
if(!S.scan)t+='<div class="empt"><svg width="26" height="26" viewBox="0 0 16 16" fill="none" stroke="#A1A1AA" stroke-width="1.1" stroke-linecap="round" stroke-linejoin="round">@ICON@</svg><b>Scan or type a roll ID</b><span>The roll list, its dye lot and its bin fill in after the first scan.</span></div>';
else{t+='<div class="row h"><span>Roll</span><span>Dye lot</span><span>Shade</span><span class="r">Length</span><span>Bin</span><span>Status</span></div>';
rows().forEach(function(r){var s=st(r),x=STX[s],nw=(S.fs&&r.par)||(S.fb&&r.lot!==LOT);
t+='<div class="row'+(r.par?' sp':'')+(nw?' flash':'')+'" id="rw-'+r.id+'"><span class="rid mono">'+r.id+(r.par?'<small>parent '+r.par+'</small>':'')+'</span><span>'+lotChip(r.lot,s==='bl')+'</span><span class="mono">'+r.sh+'</span><span class="mono r">'+r.yd+' yd</span><span class="mono">'+r.bin+'</span>'
+'<span class="stc"><span class="ch '+x[0]+'">'+(s==='rs'?'Reserved':s==='bl'?'Blocked':s==='hd'?'Held':'Available')+'</span>'+(r.id===SPL[0]&&S.blk&&!S.spl?'<button type="button" class="bt spl" id="spl">Split</button>':'')+'</span></div>';});
t+='<div class="tf" id="tf">'+LOT+' in stock: <b>'+n0(inLot(function(){return true;}))+' yd</b> in '+ROLLS.filter(function(r){return r.lot===LOT;}).length+' rolls, '+n0(inLot(function(r){return r.st==='av';}))+' available, '+n0(inLot(function(r){return r.st==='hd';}))+' held</div>';}
$('tb').innerHTML=t;
var l='<div class="ct"><span>Roll label</span>';
if(!S.scan)l+='</div><div class="empt"><b>No roll scanned</b><span>The label and the roll record show here.</span></div>';
else{var r=find(S.sel),s=st(r),x=STX[s];l+='<span class="ch '+x[0]+'" id="lst">'+x[1]+'</span></div>'
+'<div class="lab'+(S.fl?' in':'')+'">'+bars(r.id)+'<span class="lid mono" id="lid">'+r.id+'</span>'+lotChip(r.lot,s==='bl')+(r.par?'<span class="par" id="lpar">Split from '+r.par+', lot kept</span>':'')+'</div>'
+'<div class="kvg" id="rec"><span class="kv"><small>Dye lot</small><b class="mono">'+r.lot+'</b></span><span class="kv"><small>Shade</small><b class="mono">'+r.sh+'</b></span><span class="kv"><small>Width</small><b class="mono">'+WID+' in</b></span>'
+'<span class="kv"><small>Length</small><b class="mono">'+r.yd+' yd</b></span><span class="kv"><small>Bin</small><b class="mono">'+r.bin+'</b></span><span class="kv"><small>Status</small><b>'+(s==='av'?'Available':s==='rs'?'Reserved':s==='bl'?'Blocked':'Held')+'</b></span></div>';}
$('lb').innerHTML=l;
var ry=resYd(),q='<div class="ct"><span>'+SO+', navy twill</span><span class="ch '+(ry>=NEED?'c-ok':'c-idle')+'" id="rst">'+(ry>=NEED?'Reserved':'Open')+'</span></div>'
+'<div class="pr"><div class="t"><span>Reserved from one dye lot</span><b class="mono" id="rqty">'+n0(ry)+' of '+n0(NEED)+' yd</b></div><div class="bar"><i class="'+(ry>=NEED?'full':'')+'" style="width:'+(100*ry/NEED)+'%"></i></div></div>';
if(S.rsv)RES.forEach(function(id){var r=find(id);q+='<div class="pk'+(S.fr?' in':'')+'"><span class="mono">'+id+' &nbsp;'+r.lot+'</span><span class="mono">'+r.yd+' yd</span></div>';});
if(S.blk)q+='<div class="blk in" id="blk"><span><b>Pick blocked.</b> Dye lot '+find('R-48330').lot+' does not match '+LOT+' on this order</span><button type="button" class="bt" id="ovr">Override with reason</button>'+(S.note?'<span class="nt">A reason and a supervisor sign off are required.</span>':'')+'</div>';
else if(S.rsv)q+='<div class="ac frm" id="acr"><label class="fld" id="fain"><small>Add roll</small><input id="ain" value="" autocomplete="off" spellcheck="false" aria-label="Add roll to order"><span class="em" id="aem">Try R-48330</span></label><button type="button" class="bt" id="add">Add</button></div>';
else q+='<div class="od"><span class="kv"><small>Item</small><b class="mono">TW-5810</b></span><span class="kv"><small>Shade</small><b class="mono">NVY-204</b></span><span class="kv"><small>Customer</small><b>Harbor Home Textiles</b></span><span class="kv"><small>Lot rule</small><b>One dye lot per order</b></span></div><div class="ac"><button type="button" class="bt pri" id="rsv"'+(S.scan?'':' disabled')+'>Reserve '+NEED+' yd from one lot</button><span class="mut">'+(S.scan?'Picks whole rolls from '+LOT:'Scan a roll first')+'</span></div>';
$('rs').innerHTML=q;if($('ain'))$('ain').value=S.av||'';
var m='';
if(!S.scan)m='<div class="empt"><b>Nothing scanned yet</b><span>Totals for the dye lot appear after the first scan.</span></div>';
else{var T=[['In stock, '+LOT,n0(inLot(function(){return true;}))+' yd',ROLLS.filter(function(r){return r.lot===LOT;}).length+' rolls, '+n0(inLot(function(r){return r.st==='hd';}))+' held','t-stk',''],
['Reserved, '+SO,n0(ry)+' of '+n0(NEED)+' yd',S.rsv?'from '+LOT:'Not reserved yet','t-res',ry>=NEED?'ok':''],
['Available in this dye lot',n0(availYd())+' yd',S.rsv?'R-48214 '+find('R-48214').yd+' + '+SPL[0]+' '+(SPL[1]+SPL[2]):'5 rolls','t-av',''],
];
m='<div class="tls">'+T.map(function(x){return '<div class="tl '+x[4]+'"><small>'+x[0]+'</small><b id="'+x[3]+'">'+x[1]+'</b><em>'+x[2]+'</em></div>';}).join('')+'</div>';
m+='<div class="ln" id="sln">'+(S.spl?SPL[0]+' split into '+SPL[0]+'-A '+SPL[1]+' yd and '+SPL[0]+'-B '+SPL[2]+' yd, both '+LOT+'. R-48330 blocked.':S.blk?'R-48330 blocked on '+SO+'. Mixed dye lots never reach the cutter.':S.rsv?'Three rolls, one dye lot, one shade on '+SO+'.':'Roll '+S.sel+' scanned. Lot and bin come from the label.')+'</div>';}
$('sm').innerHTML=m;
var ss=$('sst');ss.textContent=S.scan?S.sel+' scanned':'No roll scanned';ss.className='ch '+(S.scan?'c-info':'c-idle');
S.fl=S.fr=S.fb=S.fs=false;}
function norm(v){v=String(v).trim().toUpperCase().replace(/\s/g,'');if(/^R?\d{5}$/.test(v))v='R-'+v.replace(/^R/,'');return v;}
function known(v){return ROLLS.some(function(r){return r.id===v;});}
[].forEach.call(root.querySelectorAll('[data-sample]'),function(b){b.addEventListener('click',function(){$('rin').value=b.getAttribute('data-v');$('frin').classList.remove('err');});});
$('rs').addEventListener('click',function(e){if(e.target&&e.target.id==='ovr'){S.note=true;render();}});
$('rs').addEventListener('input',function(e){if(e.target&&e.target.id==='ain')S.av=e.target.value;});
function typeIn(inp,t,done){var i=0;(function k(){inp.value=t.slice(0,i);if(i<t.length){i++;later(k,60);}else done();})();}
function resetState(){S={scan:false,sel:null,rsv:false,blk:false,spl:false,note:false,av:''};$('rin').value='';$('frin').classList.remove('err');render();}
var CAPAT=function(hh){return {l:14,t:52};};
var ST=[
{id:'scan',target:function(){return mode==='try'?$('scn'):$('rin');},prompt:'Type R-48214 or pick a sample, then Scan',where:'below',
 ok:function(){var v=norm($('rin').value),b=!known(v);$('rem').textContent=v?'No roll found. Try R-48214':'Enter a roll ID, for example R-48214';$('frin').classList.toggle('err',b);return !b;},
 run:function(quick){var v=mode==='try'&&known(norm($('rin').value))?norm($('rin').value):'R-48214';S.scan=true;S.sel=v;var go=function(){$('rin').value=v;$('frin').classList.remove('err');S.fl=true;render();};if(mode==='watch'&&!quick)typeIn($('rin'),v,go);else go();},
 after:function(){var r=find(S.sel);return['Scan a roll label',r.id+' is '+r.yd+' yd of shade '+r.sh+', dye lot '+r.lot+', '+WID+' in wide, bin '+r.bin+'.'];}},
{id:'rsv',target:function(){return $('rsv');},prompt:'Reserve '+NEED+' yd for '+SO,where:'above',run:function(){S.rsv=true;S.fr=true;S.av='R-48330';render();},
 after:function(){return['Reserve rolls from one dye lot',RES.join(', ').replace(/, ([^,]*)$/,' and $1')+' from '+LOT+': '+RES.map(function(id){return find(id).yd;}).join(' + ')+' = '+n0(resYd())+' yd.'];}},
{id:'mix',target:function(){return mode==='try'?$('add'):$('ain');},prompt:'Add roll R-48330 to the order',where:'above',
 ok:function(){var v=norm($('ain').value),b=v!=='R-48330';$('aem').textContent=v?'For this step, add R-48330':'Enter R-48330';$('fain').classList.toggle('err',b);return !b;},
 run:function(quick){S.blk=true;S.sel='R-48330';var go=function(){S.fb=true;render();};if(mode==='watch'&&!quick&&$('ain'))typeIn($('ain'),'R-48330',go);else go();},
 after:function(){return['A pick that mixes lots is blocked','Dye lot '+find('R-48330').lot+' does not match '+LOT+' on this order. Override needs a reason.'];}},
{id:'spl',target:function(){return $('spl');},prompt:'Split '+SPL[0]+' into '+SPL[1]+' and '+SPL[2]+' yd',where:'below',run:function(){S.spl=true;S.fs=true;S.fl=true;S.sel=SPL[0]+'-A';render();},
 after:function(){return['Split a roll and keep its lot',SPL[0]+' '+(SPL[1]+SPL[2])+' yd becomes '+SPL[0]+'-A '+SPL[1]+' yd and '+SPL[0]+'-B '+SPL[2]+' yd, both '+LOT+'.'];}}];
'''

JS = (JS.replace('@LOT@', D.LOT).replace('@SO@', D.SO[0]).replace('@NEED@', str(D.SO[1])).replace('@RES@', json.dumps(D.RESERVE))
      .replace('@SPL@', json.dumps(list(D.SPLIT))).replace('@WID@', str(D.WIDTH_IN)).replace('@ROLLS@', json.dumps(ROLLS, separators=(',', ':')))
      .replace('@ICON@', ICON))
assert '@' not in JS.replace('@media', '')
