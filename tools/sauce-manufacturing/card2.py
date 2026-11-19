"""Sauce manufacturing card 2: Kettle & Tank Batch Records. Layout: a stage chain.
Top: the batch list for Kettle K-2. Middle: the Cook, Hold and Fill stages with running volumes and the limit each
stage checks. Bottom: the readings (read only, preset) with Record readings and Check limits, and the batch status
with Hold, Sign off and release and Batch record; the batch record then fills the bottom on one page. A reading is
flagged only when it is outside its numeric limit, and Fill stays disabled while the batch is flagged or on hold."""
import json
from frame_auto import header

SUMMARY = 'Kettle & Tank Batch Records (open SP-2291, record 192 F, pH 4.4 and Brix 25, flag pH over 4.2, hold then sign off and release, view the batch record)'
ARIA = 'Interactive product screen: open batch SP-2291 moving through cook, hold and fill, record temperature, pH and Brix, see the pH reading flag the batch, place it on hold and release it after a sign off, and view the full batch record'
STEPS = 5
STUDIO = dict(lede='A typical batch record screen on your Sutton data. Want it different? Describe the change.',
              examples=['Viscosity at the hold stage', 'Limits per sauce and kettle', 'A photo of the chart recorder', 'A second sign off for releases'],
              built_on='Batches, lots, BOMs and quality checks', change='Readings, limits and views')

ICON = '<path d="M3 3h10v10H3z"/><path d="M5.5 6.5h5M5.5 9h5M5.5 11.5h3"/>'

CSS = (
 '.fld input[readonly]{background:#F4F4F5;color:#3F3F46;cursor:default;pointer-events:none}'
 '.g2{display:grid;grid-template-rows:140px 160px 220px;gap:10px;padding:10px 44px 0 16px;width:716px}'
 '.bl .row{grid-template-columns:62px 1fr 70px 84px;min-height:28px;font-size:9.6px}.bl .row span:nth-child(3){text-align:right;font-family:"JetBrains Mono",ui-monospace,monospace}.bl .row span:last-child{text-align:right}'
 '.chain{display:grid;grid-template-columns:1fr 18px 1fr 18px 1fr}.arw{display:grid;place-items:center;color:#A1A1AA}.arw svg{width:10px;height:10px}'
 '.stg{border:1px solid #E4E4E7;border-radius:8px;background:#fff;display:flex;flex-direction:column;overflow:hidden;transition:background-color .35s,border-color .35s}'
 '.stg .sh{display:flex;align-items:center;justify-content:space-between;padding:7px 10px;border-bottom:1px solid #F0F0F1;font-weight:600;font-size:10.6px}'
 '.stg .vol{padding:7px 10px 0}.stg .vol small{display:block;font-size:8.6px;color:#71717A}.stg .vol b{font-family:"JetBrains Mono",ui-monospace,monospace;font-size:17px;font-weight:600}'
 '.stg .lim{padding:6px 10px 0;display:flex;flex-direction:column;gap:4px;font-size:9px;color:#52525B}.stg .lim>div{display:flex;justify-content:space-between;align-items:center;gap:6px}'
 '.stg .run{margin-top:auto;padding:6px 10px;border-top:1px dashed #E4E4E7;font-size:8.6px;color:#52525B;display:flex;justify-content:space-between}.stg .run em{font-style:normal;font-family:"JetBrains Mono",ui-monospace,monospace;font-weight:600;color:#18181B}'
 '.stg.e{background:#FAFAFA}.stg.e .sh{color:#A1A1AA}.stg.bad{border-color:#FCA5A5}.stg.ok{border-color:#BBF7D0}'
 '.stg .bt{font-size:9px;padding:2px 8px}.stg .bt:disabled{opacity:.5;cursor:not-allowed}'
 '.bot{display:grid;grid-template-columns:1fr 1fr;gap:10px}.bc{display:flex;flex-direction:column}.bc>.empt{margin:9px;flex:1}.bc .ct .bt{font-size:9.2px;padding:3px 8px}'
 '.rds{display:grid;grid-template-columns:1fr 1fr 1fr;gap:8px;padding:9px 10px 0}.rds .fld small{display:flex;justify-content:space-between}.rds .lm{padding:3px 0 0;font-size:8.4px;color:#71717A}'
 '.chk{padding:8px 10px 0;display:flex;flex-direction:column;gap:5px}.chk>div{display:flex;justify-content:space-between;align-items:center;font-size:9.2px}'
 '.st{padding:9px 10px 0;display:flex;flex-direction:column;gap:6px}.st .big{font-size:17px}.note{margin:8px 10px 0;padding:7px 9px;border-radius:7px;font-size:9px;line-height:1.45;background:#FAFAFA;border:1px solid #F0F0F1;color:#52525B}.note.w{background:#FEF2F2;border-color:#FECACA;color:#991B1B}.note.g{background:#F0FDF4;border-color:#BBF7D0;color:#166534}'
 '.acts{display:flex;gap:6px;padding:8px 10px 0}.acts .bt{font-size:9.4px;padding:4px 10px}'
 '.ft{margin-top:auto;padding:7px 10px;border-top:1px solid #F0F0F1;font-size:8.6px;color:#71717A;background:#FAFAFA}'
 '.rec{grid-column:1/3;display:flex;flex-direction:column}.rec .row{grid-template-columns:72px 1fr 70px 76px 80px;font-size:9.3px;min-height:22px}.rec .row span:nth-child(3),.rec .row span:nth-child(4){text-align:right;font-family:"JetBrains Mono",ui-monospace,monospace}.rec .row.h span{font-family:inherit!important}.rec .row span:last-child{text-align:right}'
 '.rec .sub{padding:6px 11px 2px;font-size:9px;color:#71717A;font-weight:500}'
)

ARW = '<div class="arw" aria-hidden="true"><svg viewBox="0 0 10 10" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"><path d="M2 5h6M5.5 2.5L8 5 5.5 7.5"/></svg></div>'

WIN = (
 header(ICON, 'Batch records', 'Cook, hold and fill with readings against limits')
 + '<div class="g2"><div class="cd bl" id="bl"></div><div class="chain" id="chn"></div><div class="bot" id="bot"></div></div>'
)

JS = r'''
var FOC='.hd>*,.bl .ct,.bl .row,.stg,.bc>.ct,.bc>*:not(.ct),.rec';
var BAT=[['SP-2289','Smoky barbecue base',500,'Filled','c-idle'],['SP-2290','Garlic stir fry base',400,'Released','c-ok'],['SP-2291','Teriyaki base',500,'Cooking','c-info']];
var B=BAT[2],VOL=B[2];
var RD=[{k:'temp',nm:'Cook temperature',st:'Cook',v:192,u:' F',lim:'190 F minimum',ok:function(v){return v>=190;}},{k:'ph',nm:'pH',st:'Hold',v:4.4,u:'',lim:'4.2 maximum',ok:function(v){return v<=4.2;}},{k:'brix',nm:'Brix',st:'Hold',v:25,u:'',lim:'24 to 26',ok:function(v){return v>=24&&v<=26;}}];
var S;
function fl(){return RD.filter(function(r){return !r.ok(r.v);});}
function fv(r){return (r.k==='ph'?r.v.toFixed(1):String(r.v))+r.u;}
function status(){return S.rel?['Released','c-ok']:S.hold?['On hold','c-bad']:S.ck&&fl().length?['Flagged','c-bad']:S.op?['In process','c-info']:['',''];}
function blocked(){return !S.rel&&(S.hold||(S.ck&&fl().length>0))||!S.ck;}
function chip(r){if(!S.rd)return '<span class="ch c-idle">Not read</span>';if(!S.ck)return '<span class="ch c-info" id="c-'+r.k+'">'+fv(r)+'</span>';return '<span class="ch '+(r.ok(r.v)?'c-ok':'c-bad')+'" id="c-'+r.k+'">'+fv(r)+'</span>';}
function stg(nm,cls,stc,vol,vl,lims,run){return '<div class="stg'+(cls?' '+cls:'')+'"><div class="sh"><span>'+nm+'</span>'+stc+'</div><div class="vol"><small>'+vl+'</small><b>'+vol+'</b></div><div class="lim">'+lims+'</div><div class="run"><span>Running</span><em>'+run+'</em></div></div>';}
function render(){
var st=status();
$('bl').innerHTML='<div class="ct"><span>Batches on Kettle K-2</span>'+(S.op?'<span class="ch '+st[1]+'" id="bst">'+st[0]+'</span>':'')+'</div><div class="row h"><span>Batch</span><span>Sauce</span><span>Volume</span><span>Status</span></div>'+
BAT.map(function(x,i){var me=i===2;return '<button type="button" class="row'+(me&&S.op?' sel':'')+'" id="b-'+x[0]+'"><span class="mono"><b>'+x[0]+'</b></span><span>'+x[1]+'</span><span>'+n0(x[2])+' gal</span><span><span class="ch '+(me&&S.op?st[1]:x[4])+'">'+(me&&S.op?st[0]:x[3])+'</span></span></button>';}).join('');
var c;
if(!S.op)c=['Cook','Hold','Fill'].map(function(n){return '<div class="stg e"><div class="sh"><span>'+n+'</span></div><div class="lim" style="padding-top:10px">Open a batch to follow it through this stage.</div></div>';});
else{var t=RD[0],ph=RD[1],bx=RD[2];
c=[stg('Cook','ok','<span class="ch c-ok">Done</span>',n0(VOL)+' gal','Cooked','<div><span>Temperature, '+t.lim+'</span>'+chip(t)+'</div>',n0(VOL)+' gal'),
stg('Hold',S.ck&&fl().length&&!S.rel?'bad':S.rel?'ok':'',S.hold&&!S.rel?'<span class="ch c-bad">On hold</span>':S.rel?'<span class="ch c-ok">Released</span>':'<span class="ch c-info">Tank T-4</span>',n0(VOL)+' gal','Held','<div><span>pH, '+ph.lim+'</span>'+chip(ph)+'</div><div><span>Brix, '+bx.lim+'</span>'+chip(bx)+'</div>',n0(VOL)+' gal'),
stg('Fill',blocked()?'e':'ok',blocked()?'<span class="ch c-bad" id="fst">Blocked</span>':'<span class="ch c-ok" id="fst">Ready</span>','0 gal','Filled','<div><span>Needs a released batch</span><button type="button" class="bt" id="fib"'+(blocked()?' disabled':'')+'>Fill</button></div>',(S.rel?n0(VOL)+' gal to fill':'0 gal'))];}
$('chn').innerHTML=c.join(ARW);
var b='';
if(S.rec){b='<div class="cd rec in" id="rec"><div class="ct"><span>Batch record <span class="mono">'+B[0]+'</span>, '+B[1]+', '+n0(VOL)+' gal</span><span class="ch c-ok">Released</span></div><div class="row h"><span>Stage</span><span>Reading</span><span>Value</span><span>Limit</span><span>Result</span></div>'+
RD.map(function(r){return '<div class="row"><span>'+r.st+'</span><span>'+r.nm+'</span><span id="rv-'+r.k+'">'+fv(r)+'</span><span>'+r.lim.replace(' minimum',' min').replace(' maximum',' max')+'</span><span><span class="ch '+(r.ok(r.v)?'c-ok':'c-bad')+'">'+(r.ok(r.v)?'Within':'Outside')+'</span></span></div>';}).join('')+
'<div class="sub">Events</div>'+[['Nov 19, 9:42','Readings recorded','3 readings'],['Nov 19, 9:44','Placed on hold','pH '+fv(RD[1])],['Nov 19, 10:15','Signed off by the quality lead and released','Released']].map(function(e){return '<div class="row"><span>'+e[0].split(', ')[1]+'</span><span>'+e[1]+'</span><span></span><span></span><span>'+e[2]+'</span></div>';}).join('')+'</div>';}
else{b='<div class="cd bc"><div class="ct"><span>Readings</span>'+(!S.op?'':!S.rd?'<button type="button" class="bt pri" id="rrb">Record readings</button>':!S.ck?'<button type="button" class="bt" id="ckb">Check limits</button>':'<span class="ch '+(fl().length?'c-bad':'c-ok')+'" id="flc">'+fl().length+' outside limit</span>')+'</div>';
if(!S.rd)b+='<div class="empt"><b>No readings yet</b><span>'+(S.op?'Record the cook and hold readings for this batch.':'Open a batch to record its readings.')+'</span></div>';
else{b+='<div class="rds in">'+RD.map(function(r){return '<label class="fld"><small><span>'+r.nm+'</span></small><input id="i-'+r.k+'" value="'+fv(r)+'" readonly tabindex="-1" autocomplete="off" spellcheck="false"><span class="lm">'+r.lim+'</span></label>';}).join('')+'</div>';
b+=S.ck?'<div class="note '+(fl().length?'w':'g')+' in">'+(fl().length?fl().map(function(r){return r.nm+' '+fv(r)+' is outside '+r.lim;}).join('. ')+'. Fill is blocked.':'All readings within limits.')+'</div>':'<div class="note">Preset readings from the kettle probe and the hold tank sample.</div>';}
b+='<div class="ft">Readings stay on the lot after filling.</div></div>';
b+='<div class="cd bc"><div class="ct"><span>Batch status</span>'+(S.op?'<span class="ch '+st[1]+'">'+st[0]+'</span>':'')+'</div>';
if(!S.ck)b+='<div class="empt"><b>Nothing to decide yet</b><span>Hold and release open once the readings are checked.</span></div>';
else{b+='<div class="st in"><div class="kv"><small>'+B[0]+', '+B[1]+'</small><b class="big">'+(S.rel?'Released':S.hold?'On hold':'Flagged')+'</b></div></div>'+
'<div class="acts">'+(S.hold?'':'<button type="button" class="bt" id="hdb" data-pick="1">Hold</button>')+(S.hold&&!S.rel?'<button type="button" class="bt pri" id="srb">Sign off and release</button>':'')+(S.rel?'<button type="button" class="bt pri" id="brb">Batch record</button>':'')+'</div>'+
(S.rel?'<div class="note g in">Signed off by the quality lead. Fill is open and the readings stay on the record.</div>':S.hold?'<div class="note w in">On hold in Tank T-4. Fill is disabled until a sign off.</div>':'<div class="note">Hold the batch while the quality lead reviews the pH reading.</div>');}
b+='<div class="ft">Holds, sign offs and releases are logged with time and user.</div></div>';}
$('bot').innerHTML=b;
}
function resetState(){S={op:false,rd:false,ck:false,hold:false,rel:false,rec:false};render();}
winEl.addEventListener('click',function(e){var h=e.target.closest&&e.target.closest('#hdb');if(h&&S.ck&&!S.hold){S.hold=true;render();}});
function capN(){var i=cap.querySelector('.m i');return i?+i.textContent:1;}
var CAPAT=function(hh){var w=cap.offsetWidth;return capN()>=3?{l:visW()-w-14,t:60}:{l:visW()-w-14,t:visH()-hh-14};};
var ST=[
{id:'op',target:function(){return $('b-SP-2291');},prompt:'Open batch SP-2291',where:'below',run:function(){S.op=true;render();},
 after:function(){return['One batch through cook, hold and fill',B[0]+', '+B[1]+': '+n0(VOL)+' gal cooked on Kettle K-2 and moving to hold.'];}},
{id:'rd',target:function(){return $('rrb');},prompt:'Record the readings',where:'below',run:function(){S.rd=true;render();},
 after:function(){return['Temperature, pH and Brix on the batch',RD.map(function(r){return r.nm+' '+fv(r);}).join(', ')+'.'];}},
{id:'ck',target:function(){return $('ckb');},prompt:'Check the limits',where:'below',run:function(){S.ck=true;render();},
 after:function(){var f=fl();return['A reading outside its limit flags the batch',f.map(function(r){return r.nm+' '+fv(r)+' is over '+r.lim.replace(' maximum','');}).join(', ')+'. Temperature and Brix are within. Fill is blocked.'];}},
{id:'rel',target:function(){return $('srb');},back:function(){return S.hold?null:[$('hdb'),'Hold the batch','below'];},prompt:'Sign off and release',where:'below',
 run:function(){S.hold=true;S.rel=true;render();},
 after:function(){return['Hold, then release after a sign off','The quality lead signed off. '+B[0]+' is Released and Fill is open.'];}},
{id:'rec',target:function(){return $('brb');},prompt:'Open the batch record',where:'below',run:function(){S.rec=true;render();},
 after:function(){return['The full batch record on one page','Readings, limits, the hold and the release, kept on lot '+B[0]+'.'];}}];
'''
JS = 'var ARW=' + json.dumps(ARW) + ';' + JS
