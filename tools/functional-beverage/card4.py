"""Functional beverage card 4: Batch Testing & Release. Layout: a stage chain.
Top: the batches list. Middle: Filled, Hold, Tests and Release with running can counts. Bottom: the results (read only,
preset, with a Result set 1 or 2 toggle) with Record results and Check limits, and the release panel with Sign off
and release and Trace; the trace then fills the bottom. A result is flagged only when outside its limit, and Release
is enabled only when every result is within limits."""
import json
from frame_auto import header

SUMMARY = 'Batch Testing & Release (open FB-0412 on hold, record 61 mg active, 80 and 20 CFU, check limits, sign off and release, trace to ASH-2291; result set 2 routes to review)'
ARIA = 'Interactive product screen: open a filled batch on hold, record potency and microbial results, see each result checked against its limit, release the batch with a sign off and trace the released lot to its ingredient lots'
STEPS = 5
STUDIO = dict(lede='A typical batch release screen on your Sutton data. Want it different? Describe the change.',
              examples=['Tests required per product', 'A retest when a result misses', 'Results imported from the lab', 'A release report per customer'],
              built_on='Batches, lots, tests and BOMs', change='Tests, limits and views')

ICON = '<path d="M6 2h4M7 2v4l-3.5 6.5A1 1 0 0 0 4.4 14h7.2a1 1 0 0 0 .9-1.5L9 6V2"/><path d="M5 10h6"/>'

CSS = (
 '.fld input[readonly]{background:#F4F4F5;color:#3F3F46;cursor:default;pointer-events:none}'
 '.g4{display:grid;grid-template-rows:140px 150px 230px;gap:10px;padding:10px 44px 0 16px;width:716px}'
 '.bl .row{grid-template-columns:62px 1fr 80px 84px;min-height:28px;font-size:9.6px}.bl .row span:nth-child(3){text-align:right;font-family:"JetBrains Mono",ui-monospace,monospace}.bl .row span:last-child{text-align:right}'
 '.chain{display:grid;grid-template-columns:1fr 16px 1fr 16px 1fr 16px 1fr}.arw{display:grid;place-items:center;color:#A1A1AA}.arw svg{width:10px;height:10px}'
 '.stg{border:1px solid #E4E4E7;border-radius:8px;background:#fff;display:flex;flex-direction:column;overflow:hidden;transition:background-color .35s,border-color .35s}'
 '.stg .sh{display:flex;align-items:center;justify-content:space-between;gap:4px;padding:6px 9px;border-bottom:1px solid #F0F0F1;font-weight:600;font-size:10.2px}'
 '.stg .vol{padding:6px 9px 0}.stg .vol small{display:block;font-size:8.5px;color:#71717A}.stg .vol b{font-family:"JetBrains Mono",ui-monospace,monospace;font-size:15px;font-weight:600}'
 '.stg .lim{padding:4px 9px 0;font-size:8.6px;color:#52525B;line-height:1.35}'
 '.stg .run{margin-top:auto;padding:5px 9px;border-top:1px dashed #E4E4E7;font-size:8.5px;color:#52525B;display:flex;justify-content:space-between}.stg .run em{font-style:normal;font-family:"JetBrains Mono",ui-monospace,monospace;font-weight:600;color:#18181B}'
 '.stg.e{background:#FAFAFA}.stg.e .sh{color:#A1A1AA}.stg.bad{border-color:#FCA5A5}.stg.ok{border-color:#BBF7D0}'
 '.bot{display:grid;grid-template-columns:1.25fr 1fr;gap:10px}.bc{display:flex;flex-direction:column}.bc>.empt{margin:9px;flex:1}.bc .ct .bt{font-size:9.2px;padding:3px 8px}'
 '.seg{display:inline-flex;padding:2px;gap:2px;border:1px solid #E4E4E7;border-radius:7px;background:#FAFAFA}.seg button{font:inherit;font-size:9px;font-weight:500;padding:2px 7px;border:0;border-radius:5px;background:transparent;color:#52525B;cursor:pointer}.seg button.on{background:#18181B;color:#fff}.seg button:focus-visible{outline:2px solid #18181B;outline-offset:1px}'
 '.rds{display:flex;flex-direction:column;gap:6px;padding:8px 10px 0}.rd{display:grid;grid-template-columns:1fr 92px 64px;gap:8px;align-items:end}.rd .lm{font-size:8.4px;color:#71717A;padding-bottom:6px}.rd .rs{text-align:right;padding-bottom:4px}'
 '.st{padding:9px 10px 0;display:flex;flex-direction:column;gap:6px}.st .big{font-size:17px}.note{margin:8px 10px 0;padding:7px 9px;border-radius:7px;font-size:9px;line-height:1.45;background:#FAFAFA;border:1px solid #F0F0F1;color:#52525B}.note.w{background:#FEF2F2;border-color:#FECACA;color:#991B1B}.note.g{background:#F0FDF4;border-color:#BBF7D0;color:#166534}'
 '.acts{display:flex;gap:6px;padding:8px 10px 0}.acts .bt{font-size:9.4px;padding:4px 10px}.acts .bt:disabled{opacity:.45;cursor:not-allowed}'
 '.ft{margin-top:auto;padding:7px 10px;border-top:1px solid #F0F0F1;font-size:8.6px;color:#71717A;background:#FAFAFA}'
 '.trc{grid-column:1/3;display:flex;flex-direction:column}.trc .row{grid-template-columns:86px 1fr 90px 76px;font-size:9.3px;min-height:24px}.trc .row span:nth-child(3){font-family:"JetBrains Mono",ui-monospace,monospace}.trc .row span:last-child{text-align:right}.trc .row.hit{background:#FEF9E7}'
 '.trc .sub{padding:6px 11px 2px;font-size:9px;color:#71717A;font-weight:500}'
)

ARW = '<div class="arw" aria-hidden="true"><svg viewBox="0 0 10 10" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"><path d="M2 5h6M5.5 2.5L8 5 5.5 7.5"/></svg></div>'

WIN = (
 header(ICON, 'Batch release', 'Filled batches held until their tests are in and within limits')
 + '<div class="g4"><div class="cd bl" id="bl"></div><div class="chain" id="chn"></div><div class="bot" id="bot"></div></div>'
)

JS = r'''
var FOC='.hd>*,.bl .ct,.bl .row,.stg,.bc>.ct,.bc>*:not(.ct),.trc';
var BAT=[['FB-0410','Recovery Ginger Brew',24000,'Shipped','c-idle'],['FB-0411','Focus Citrus Sparkling',20000,'Released','c-ok'],['FB-0412','Calm Adaptogen Tonic',18000,'On hold','c-warn']];
var B=BAT[2],CANS=B[2];
var RS=[{k:'act',nm:'Active, withanolides',u:' mg',lim:'57 to 63 mg per can',lo:57,hi:63,v:[61,61]},{k:'tpc',nm:'Total plate count',u:' CFU/mL',lim:'100 maximum',lo:null,hi:100,v:[80,80]},{k:'ym',nm:'Yeast and mold',u:' CFU/mL',lim:'100 maximum',lo:null,hi:100,v:[20,150]}];
var TR=[['Ashwagandha root extract','Verdant Botanicals','ASH-2291','1,200 mg'],['L-theanine','Coastline Nutrients','LT-0877','200 mg'],['Lemon balm extract','Coastline Nutrients','LB-1140','150 mg'],['Cans and lids','Northbay Can Co.','CN-5520','1 each']];
var S;
function val(r){return r.v[S.set];}
function ok(r){var v=val(r);return (r.lo===null||v>=r.lo)&&v<=r.hi;}
function bad(){return RS.filter(function(r){return !ok(r);});}
function canRelease(){return S.ck&&bad().length===0;}
function status(){return S.rel?['Released','c-ok']:S.ck&&bad().length?['Review','c-bad']:['On hold','c-warn'];}
function chip(r){if(!S.rd)return '';if(!S.ck)return '<span class="ch c-info" id="c-'+r.k+'">Recorded</span>';return '<span class="ch '+(ok(r)?'c-ok':'c-bad')+'" id="c-'+r.k+'">'+(ok(r)?'Within':'Outside')+'</span>';}
function stg(nm,cls,stc,vol,vl,lims,run){return '<div class="stg'+(cls?' '+cls:'')+'"><div class="sh"><span>'+nm+'</span>'+stc+'</div><div class="vol"><small>'+vl+'</small><b>'+vol+'</b></div><div class="lim">'+lims+'</div><div class="run"><span>Running</span><em>'+run+'</em></div></div>';}
function render(){
var st=status();
$('bl').innerHTML='<div class="ct"><span>Filled batches</span>'+(S.op?'<span class="ch '+st[1]+'" id="bst">'+st[0]+'</span>':'')+'</div><div class="row h"><span>Batch</span><span>Product</span><span>Cans</span><span>Status</span></div>'+
BAT.map(function(x,i){var me=i===2;return '<button type="button" class="row'+(me&&S.op?' sel':'')+'" id="b-'+x[0]+'"><span class="mono"><b>'+x[0]+'</b></span><span>'+x[1]+'</span><span>'+n0(x[2])+'</span><span><span class="ch '+(me&&S.op?st[1]:x[4])+'">'+(me&&S.op?st[0]:x[3])+'</span></span></button>';}).join('');
var c;
if(!S.op)c=['Filled','Hold','Tests','Release'].map(function(n){return '<div class="stg e"><div class="sh"><span>'+n+'</span></div><div class="lim" style="padding-top:8px">Open a batch to follow it through this stage.</div></div>';});
else{var nb=bad().length,rec=S.rd?RS.length:0;
c=[stg('Filled','ok','<span class="ch c-ok">Done</span>',n0(CANS),'Cans filled','Line 2, Nov 18',n0(CANS)),
stg('Hold',S.rel?'ok':'','<span class="ch '+(S.rel?'c-ok':'c-warn')+'">'+(S.rel?'Cleared':'On hold')+'</span>',n0(CANS),'Cans held','Held at filling until tests pass',S.rel?'0':n0(CANS)),
stg('Tests',S.ck?(nb?'bad':'ok'):'',S.ck?'<span class="ch '+(nb?'c-bad':'c-ok')+'">'+(nb?nb+' outside':'All within')+'</span>':'<span class="ch c-idle">'+rec+' of 3</span>',rec+' of 3','Results recorded','Potency and microbial',S.ck?(RS.length-nb)+' within':rec+' in'),
stg('Release',S.rel?'ok':S.ck&&nb?'bad':'e',S.rel?'<span class="ch c-ok" id="rst">Released</span>':S.ck&&nb?'<span class="ch c-bad" id="rst">Review</span>':'<span class="ch c-idle" id="rst">Waiting</span>',S.rel?n0(CANS):'0','Cans released',S.ck&&nb&&!S.rel?'Routed to review, not to shipping':'Sign off releases to shipping',S.rel?n0(CANS):'0')];}
$('chn').innerHTML=c.join(ARW);
var b='';
if(S.tr){b='<div class="cd trc in" id="trc"><div class="ct"><span>Trace, lot <span class="mono">'+B[0]+'</span>, '+B[1]+'</span><span class="ch c-ok">Released</span></div><div class="row h"><span>Input</span><span>Supplier</span><span>Lot</span><span>Per can</span></div>'+
TR.map(function(t,i){return '<div class="row'+(i===0?' hit':'')+'" id="t-'+t[2]+'"><span>'+t[0].replace(' root extract','')+'</span><span>'+t[1]+'</span><span>'+t[2]+'</span><span>'+t[3]+'</span></div>';}).join('')+
'<div class="sub">Results on the lot: active '+val(RS[0])+' mg, plate count '+val(RS[1])+', yeast and mold '+val(RS[2])+'. Signed off Nov 19.</div></div>';}
else{b='<div class="cd bc"><div class="ct"><span>Results</span>'+(!S.op?'':!S.rd?'<button type="button" class="bt pri" id="rrb">Record results</button>':'<span class="seg" role="group" aria-label="Result set"><button type="button" id="s1" class="'+(S.set===0?'on':'')+'" aria-pressed="'+(S.set===0)+'">Result set 1</button><button type="button" id="s2" class="'+(S.set===1?'on':'')+'" aria-pressed="'+(S.set===1)+'">Result set 2</button></span>')+'</div>';
if(!S.rd)b+='<div class="empt"><b>No results yet</b><span>'+(S.op?'Record the potency and microbial results for this batch.':'Open a batch to record its results.')+'</span></div>';
else{b+='<div class="rds in">'+RS.map(function(r){return '<div class="rd"><label class="fld"><small>'+r.nm+'</small><input id="i-'+r.k+'" value="'+val(r)+r.u+'" readonly tabindex="-1" autocomplete="off" spellcheck="false"></label><span class="lm">'+r.lim+'</span><span class="rs">'+chip(r)+'</span></div>';}).join('')+'</div>';
if(!S.ck)b+='<div class="acts"><button type="button" class="bt" id="ckb">Check limits</button></div>';}
b+='<div class="ft">Results are attached to the batch.</div></div>';
b+='<div class="cd bc"><div class="ct"><span>Release</span>'+(S.op?'<span class="ch '+st[1]+'">'+st[0]+'</span>':'')+'</div>';
if(!S.ck)b+='<div class="empt"><b>Not ready</b><span>Release opens once every result is in and checked.</span></div>';
else{b+='<div class="st in"><div class="kv"><small>'+B[0]+', '+n0(CANS)+' cans</small><b class="big">'+(S.rel?'Released':bad().length?'Routed to review':'Ready to release')+'</b></div></div>';
if(!S.rel)b+='<div class="acts"><button type="button" class="bt pri" id="rlb"'+(canRelease()?'':' disabled')+'>Sign off and release</button></div>'+(bad().length?'<div class="note w in" id="rno">'+bad().map(function(r){return r.nm+' '+val(r)+' is over '+r.hi;}).join('. ')+'. Release is disabled.</div>':'<div class="note g in">All three results within limits.</div>');
else b+='<div class="acts"><button type="button" class="bt pri" id="trb">Trace to ingredient lots</button></div><div class="note g in">Signed off by the quality lead. '+n0(CANS)+' cans released to shipping.</div>';}
b+='<div class="ft">A miss routes the batch to review.</div></div>';}
$('bot').innerHTML=b;
}
function resetState(){S={op:false,rd:false,ck:false,set:0,rel:false,tr:false};render();}
winEl.addEventListener('click',function(e){var t=e.target.closest&&e.target.closest('#s1,#s2');if(t&&S.rd&&!S.rel&&mode==='try'){S.set=t.id==='s2'?1:0;render();}});
function capN(){var i=cap.querySelector('.m i');return i?+i.textContent:1;}
var CAPAT=function(hh){var w=cap.offsetWidth;return capN()>=3?{l:visW()-w-14,t:60}:{l:visW()-w-14,t:visH()-hh-14};};
var ST=[
{id:'op',target:function(){return $('b-FB-0412');},prompt:'Open batch FB-0412',where:'below',run:function(){S.op=true;render();},
 after:function(){return['A filled batch, on hold',B[0]+', '+B[1]+': '+n0(CANS)+' cans filled and held until the tests are in.'];}},
{id:'rd',target:function(){return $('rrb');},prompt:'Record the results',where:'below',run:function(){S.rd=true;render();},
 after:function(){return['Potency and microbial results on the batch','Active '+val(RS[0])+' mg per can, plate count '+val(RS[1])+', yeast and mold '+val(RS[2])+' CFU/mL.'];}},
{id:'ck',target:function(){return $('ckb');},prompt:'Check the limits',where:'below',run:function(){S.ck=true;render();},
 after:function(){return['Each result against its limit','61 mg is within 57 to 63. Plate count 80 and yeast and mold 20 are under 100.'];}},
{id:'rel',target:function(){return $('rlb');},prompt:'Sign off and release',where:'below',run:function(){S.set=0;S.rel=true;render();},
 after:function(){return['Released with a sign off',n0(CANS)+' cans of '+B[0]+' released to shipping.'];}},
{id:'tr',target:function(){return $('trb');},prompt:'Trace to ingredient lots',where:'below',run:function(){S.tr=true;render();},
 after:function(){return['From the released lot to its inputs',B[0]+' used ashwagandha lot ASH-2291, with L-theanine, lemon balm and can lots.'];}}];
'''
JS = 'var ARW=' + json.dumps(ARW) + ';' + JS
