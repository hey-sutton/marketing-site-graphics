"""Electronics card 1: BOM Changes & Cost Roll-Up. Layout: BOM tree with a change request on the left, detail panel with Lines, Cost and Revisions tabs on the right."""
SUMMARY = 'BOM Changes & Cost Roll-Up (multi level BOM, cost roll-up, a controlled revision with its open build impact and cost change)'
ARIA = 'Interactive product screen: open the controller board in the PCS-200 BOM, roll up unit cost, swap a capacitor as a new revision, check the open builds it touches, release it and see the cost change'
STEPS = 6
STUDIO = dict(lede='A typical BOM and revision screen, built on your Sutton data with Studio. Want it different? Describe the change.',
              examples=['Your BOM approval steps', 'Revision rules per product line', 'A cost review view', 'Change impact by customer'],
              built_on='BOMs, items, costs and manufacturing orders', change='Approval steps, fields and views')

CSS = (
 '.b1{display:grid;grid-template-columns:240px 1fr;gap:12px;padding:12px 40px 0 16px;height:596px}'
 '.lc{display:flex;flex-direction:column;gap:10px;min-height:0}.acl{flex:1 1 0;min-height:0}.acl .row{grid-template-columns:36px 1fr;min-height:23px}.acl.off{display:none}'
 '.tree .row{grid-template-columns:12px 1fr auto;min-height:24px}.tree .l2{grid-template-columns:1fr auto auto;padding-left:31px;min-height:21px;font-size:9.3px;color:#3F3F46}'
 '.tree .l2 .mono{font-size:9px}.tree .l2.chg{background:#FFFBEB}.tree b{font-weight:600}.tree .r0 b{font-size:10.6px}'
 '.cv{width:10px;height:10px;transition:transform .25s ease;color:#52525B}.op .cv{transform:rotate(90deg)}'
 '.crq .g{display:grid;grid-template-columns:1fr 1fr;gap:7px 8px;padding:8px 11px 10px;align-items:end}.crq .g .w{grid-column:1/2}.crq .g .bt{justify-self:end}'
 '.crq .kv b{font-family:"JetBrains Mono",ui-monospace,monospace;font-size:10px;padding:5px 0}'
 '.obd .row{grid-template-columns:56px 1fr 30px auto;min-height:24px;white-space:nowrap}'
 '.det{display:flex;flex-direction:column;min-height:0;border-bottom:0;border-radius:8px 8px 0 0}'
 '.pane{display:none;padding:10px 11px;flex-direction:column;gap:10px;min-height:0}.pane.on{display:flex}'
 '.ln .row{grid-template-columns:1.05fr 1.35fr .4fr .6fr .65fr}.ln .row.f{background:#FAFAFA;font-weight:600}.ln .row.f2{font-weight:600}'
 '.brec{display:grid;grid-template-columns:repeat(4,1fr);gap:8px;padding:10px 11px}'
 '.ru .row{grid-template-columns:1.6fr .5fr .7fr}.ru .row.sub{padding-left:24px;color:#52525B;min-height:22px}.ru .row.tot{min-height:52px;background:#FAFAFA}.ru .row.tot .big{font-size:24px}'
 '.dl{font-size:9px;margin-left:5px}'
 '.im .row{grid-template-columns:58px .9fr .45fr 1.25fr}.im .row.t{background:#FAFAFA;font-weight:600}'
 '.df .row{grid-template-columns:.95fr 1.1fr 1.1fr}.df .row span:nth-child(2){color:#71717A}'
 '.acts{display:flex;gap:8px;align-items:center}'
 '.hi .row{grid-template-columns:42px 1fr auto}'
)

WIN = (
 '<div class="hd"><svg width="16" height="16" viewBox="0 0 16 16" fill="none" aria-hidden="true"><rect x="3.5" y="3.5" width="9" height="9" rx="1.5" stroke="#18181B" stroke-width="1.3"/><path d="M6 1.5v2M10 1.5v2M6 12.5v2M10 12.5v2M1.5 6h2M1.5 10h2M12.5 6h2M12.5 10h2" stroke="#18181B" stroke-width="1.2" stroke-linecap="round"/></svg>'
 '<span class="tt">PCS-200 motor controller</span><span class="ch c-ok" id="hrev">Rev C active</span><span class="sb grow">Multi level BOM, 3 sub assemblies</span></div>'
 '<div class="b1"><div class="lc">'
 '<div class="cd tree"><div class="ct">BOM<span class="mut" style="font-weight:500">Level, item, revision</span></div>'
 '<div class="row r0"><span></span><span><b class="mono">PCS-200</b> motor controller</span><span class="ch c-idle">Finished unit</span></div>'
 '<button type="button" class="row" id="tpcb"><svg class="cv" viewBox="0 0 10 10" fill="none" aria-hidden="true"><path d="M3.5 2L6.5 5 3.5 8" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"/></svg><span><b class="mono">PCBA-210</b> controller board</span><span class="ch c-idle" id="trev">Rev C</span></button>'
 '<div id="tln"></div>'
 '<div class="row"><span></span><span><b class="mono">HAR-220</b> cable harness</span><span class="ch c-idle">Rev A</span></div>'
 '<div class="row"><span></span><span><b class="mono">ENC-230</b> enclosure kit</span><span class="ch c-idle">Rev A</span></div></div>'
 '<div class="cd crq frm"><div class="ct">Change request<span class="ch c-idle" id="crs">Not started</span></div><div class="g">'
 '<div class="kv"><small>Part on rev C</small><b>CAP-1006</b></div>'
 '<label class="fld" id="frw"><small>Replace with</small><input id="rw" value="CAP-1007" spellcheck="false" autocomplete="off"><span class="em">Use an approved alternate: CAP-1007</span></label>'
 '<label class="fld w" id="frs"><small>Reason</small><input id="rs" value="Higher voltage rating" autocomplete="off"><span class="em">Add a reason for the change</span></label><button type="button" class="bt pri" id="nrv">New revision</button></div></div>'
 '<div class="cd obd"><div class="ct">Open builds<span class="mut" style="font-weight:500">PCS-200</span></div><div id="obr"></div></div>'
 '<div class="cd acl" id="acl"><div class="ct">Recent activity<span class="mut" style="font-weight:500">PCBA-210</span></div>'
 '<div class="row"><span class="mut">11/04</span><span>MO-3105 started on rev C</span></div><div class="row"><span class="mut">10/30</span><span>Cost review signed off by finance</span></div>'
 '<div class="row"><span class="mut">10/22</span><span>CAP-1007 approved as an alternate</span></div><div class="row"><span class="mut">10/09</span><span>Rev C costs updated from PO-1012</span></div></div>'
 '</div>'
 '<div class="cd det"><div class="ct" id="dh">No item selected</div>'
 '<div class="tabs" role="tablist"><button type="button" class="tab on" data-t="ln" role="tab">Lines</button><button type="button" class="tab" data-t="co" role="tab">Cost</button><button type="button" class="tab" data-t="rv" role="tab">Revisions</button></div>'
 '<div class="pane on" id="p-ln"></div><div class="pane" id="p-co"></div><div class="pane" id="p-rv"></div></div>'
 '</div>'
)

JS = r'''
var FOC='.hd>*,.tree .row,.tree .ct,.crq .ct,.crq .kv,.crq .fld,.crq .bt,.obd .ct,.obd .row,.det>.ct,.tab,.pane>*';
var LC=[['PCB-210','Bare board',1,320],['MCU-STM32','Microcontroller',1,460],['CAP-1006','10 uF capacitor',18,12],['RES-0402','10k resistor',64,1],['IC-PWR','Power regulator',2,135],['CON-J12','12 pin connector',3,90]];
var LD=LC.map(function(l){return l[0]==='CAP-1006'?['CAP-1007','10 uF 50 V capacitor',18,15]:l;});
var LABOR=450,HAR=625,ENC=1140;
var BUILDS=[['MO-3102','Scheduled',250],['MO-3105','In progress',120],['MO-3110','Scheduled',400]];
function mat(L){return L.reduce(function(a,l){return a+l[2]*l[3];},0);}
function unitC(L){return mat(L)+LABOR+HAR+ENC;}
function c2(c){return m2(c/100);}
var DELTA=unitC(LD)-unitC(LC);
var tabs=[].slice.call(root.querySelectorAll('.tab')),tpcb=$('tpcb'),nrv=$('nrv'),rw=$('rw'),rs=$('rs');
var S;
function act(){return S.rel?LD:LC;}
function rev(){return S.rel?'D':'C';}
function setTab(t){S.tab=t;render();}
tabs.forEach(function(b){b.addEventListener('click',function(){setTab(b.getAttribute('data-t'));});});
function chip(cls,t){return '<span class="ch '+cls+'">'+t+'</span>';}
function render(){
tabs.forEach(function(b){var on=b.getAttribute('data-t')===S.tab;b.classList.toggle('on',on);b.setAttribute('aria-selected',on?'true':'false');});
['ln','co','rv'].forEach(function(k){$('p-'+k).classList.toggle('on',k===S.tab);});
$('hrev').textContent='Rev '+rev()+' active';$('trev').textContent='Rev '+rev();tpcb.classList.toggle('op',S.open);tpcb.classList.toggle('sel',S.sel);
var tl='';if(S.open)act().forEach(function(l,i){tl+='<div class="row l2'+(S.rel&&l[0]==='CAP-1007'?' chg':'')+(S.anim?' in':'')+'" style="animation-delay:'+(i*45)+'ms"><span class="mono">'+l[0]+'</span><span class="mut">x'+l[2]+'</span><span class="mono">'+c2(l[2]*l[3])+'</span></div>';});$('tln').innerHTML=tl;$('acl').classList.toggle('off',S.open);
var cs=$('crs');cs.className='ch '+(S.rel?'c-ok':S.draft?'c-warn':'c-idle');cs.textContent=S.rel?'Released as rev D':S.draft?'Draft rev D':'Not started';
nrv.disabled=S.draft;nrv.className='bt '+(S.draft?'done':'pri');nrv.textContent=S.draft?'Rev D drafted':'New revision';
var ob='';BUILDS.forEach(function(b){var stay=b[0]==='MO-3105',r=S.rel&&!stay?'Rev D':'Rev C';ob+='<div class="row"><span class="mono">'+b[0]+'</span><span class="mut">'+b[1]+'</span><span class="mono r">'+n0(b[2])+'</span>'+(S.rel&&stay?chip('c-warn','Finish on rev C'):chip(S.rel?'c-ok':'c-idle',r))+'</div>';});$('obr').innerHTML=ob;
$('dh').innerHTML=S.sel?'<span><span class="mono">PCBA-210</span> controller board</span>'+chip(S.rel?'c-ok':'c-idle','Rev '+rev()):'No item selected';
if(!S.sel){var e='<div class="empt"><b>Pick an item in the BOM</b><span>See its lines, the cost roll up to the finished unit and its revision history.</span></div>';$('p-ln').innerHTML=e;$('p-co').innerHTML=e;$('p-rv').innerHTML=e;return;}
var L=act(),m=mat(L),r='';L.forEach(function(l,i){r+='<div class="row'+(S.anim?' in':'')+'" style="animation-delay:'+(i*50)+'ms"><span class="mono">'+l[0]+'</span><span>'+l[1]+'</span><span class="mono r">'+l[2]+'</span><span class="mono r">'+c2(l[3])+'</span><span class="mono r">'+c2(l[2]*l[3])+'</span></div>';});
$('p-ln').innerHTML='<div class="cd ln"><div class="ct">Lines, rev '+rev()+'<span class="mut" style="font-weight:500">Per board</span></div><div class="row h"><span>Part</span><span>Description</span><span class="r">Qty</span><span class="r">Unit</span><span class="r">Extended</span></div>'+r+
'<div class="row f"><span>Board material</span><span></span><span></span><span></span><span class="mono r" id="lmat">'+c2(m)+'</span></div><div class="row"><span>Board labor</span><span class="mut">SMT and test</span><span></span><span></span><span class="mono r">'+c2(LABOR)+'</span></div><div class="row f2"><span>Board cost</span><span></span><span></span><span></span><span class="mono r">'+c2(m+LABOR)+'</span></div></div>'+
'<div class="cd brec"><div class="kv"><small>Revision</small><b>Rev '+rev()+'</b></div><div class="kv"><small>Released</small><b>'+(S.rel?'11/06/2026':'08/14/2026')+'</b></div><div class="kv"><small>Placements</small><b>142</b></div><div class="kv"><small>Owner</small><b>D. Ortiz</b></div></div>';
var u=unitC(L),dl=S.rel?'<span class="ch c-warn dl">+'+c2(DELTA)+'</span>':'';
var co='<div class="cd ru"><div class="ct">Cost roll up<span class="mut" style="font-weight:500">Per finished unit</span></div><div class="row h"><span>Level and item</span><span>Rev</span><span class="r">Cost</span></div>'+
'<div class="row"><span><span class="mono">PCBA-210</span> controller board</span><span>'+rev()+'</span><span class="mono r">'+c2(m+LABOR)+dl+'</span></div><div class="row sub"><span>Material, 6 lines</span><span></span><span class="mono r">'+c2(m)+'</span></div><div class="row sub"><span>Labor</span><span></span><span class="mono r">'+c2(LABOR)+'</span></div>'+
'<div class="row"><span><span class="mono">HAR-220</span> cable harness</span><span>A</span><span class="mono r">'+c2(HAR)+'</span></div><div class="row"><span><span class="mono">ENC-230</span> enclosure kit</span><span>A</span><span class="mono r">'+c2(ENC)+'</span></div>'+
'<div class="row tot"><span><b>Unit cost</b>'+(S.rel?'<br><span class="mut">Was '+c2(unitC(LC))+' on rev C</span>':'')+'</span><span></span><span class="r"><span class="big mono" id="ucost">'+c2(u)+'</span></span></div></div>';
if(S.rel){var tr='',tot=0;BUILDS.forEach(function(b){var stay=b[0]==='MO-3105',x=stay?0:b[2]*DELTA;tot+=x;tr+='<div class="row"><span class="mono">'+b[0]+'</span><span class="mut">'+(stay?'Stays on rev C':'Rev D')+'</span><span class="mono r">'+n0(b[2])+'</span><span class="mono r">'+(stay?'No change':'+'+c2(x))+'</span></div>';});
co+='<div class="cd im'+(S.anim?' in':'')+'"><div class="ct">Cost change on open builds<span class="ch c-warn">+'+c2(DELTA)+' a unit</span></div><div class="row h"><span>Build</span><span>Revision</span><span class="r">Units</span><span class="r">Extra cost</span></div>'+tr+'<div class="row t"><span>Total</span><span></span><span></span><span class="mono r" id="xtot">+'+c2(tot)+'</span></div></div>';}
$('p-co').innerHTML=co;
var rv='';
if(!S.draft){rv='<div class="cd hi"><div class="ct">Revision history<span class="mut" style="font-weight:500">PCBA-210</span></div>'+[['Rev C','08/14/2026','Regulator moved to IC-PWR','Active'],['Rev B','05/02/2026','12 pin connector added','Replaced'],['Rev A','01/20/2026','First production build','Replaced']].map(function(h){return '<div class="row"><b>'+h[0]+'</b><span><span class="mut">'+h[1]+'</span> '+h[2]+'</span>'+chip(h[3]==='Active'?'c-ok':'c-idle',h[3])+'</div>';}).join('')+'</div><div class="empt"><b>No draft revision</b><span>Start a change request to draft rev D. Rev C stays on record.</span></div>';}
else{var reason=(rs.value||'').trim()||'Higher voltage rating';
rv='<div class="cd df'+(S.anim&&!S.checked?' in':'')+'"><div class="ct">Rev D'+chip(S.rel?'c-ok':'c-warn',S.rel?'Released 11/06':'Draft')+'</div><div class="row h"><span>Change</span><span>Rev C</span><span>Rev D</span></div>'+
'<div class="row"><span>Capacitor, 18 a board</span><span class="mono">CAP-1006, '+c2(12)+'</span><span class="mono">CAP-1007, '+c2(15)+'</span></div>'+
'<div class="row"><span>Line cost</span><span class="mono">'+c2(18*12)+'</span><span class="mono">'+c2(18*15)+'</span></div>'+
'<div class="row"><span>Board material</span><span class="mono">'+c2(mat(LC))+'</span><span class="mono">'+c2(mat(LD))+'</span></div>'+
'<div class="row"><span>Unit cost</span><span class="mono">'+c2(unitC(LC))+'</span><span class="mono">'+c2(unitC(LD))+' <span class="ch c-warn" id="dlt">+'+c2(DELTA)+'</span></span></div>'+
'<div class="row"><span>Reason</span><span class="mut">Rev C stays on record</span><span>'+reason.replace(/</g,'&lt;')+'</span></div></div>';
if(S.checked){var ir='';BUILDS.forEach(function(b){var stay=b[0]==='MO-3105';ir+='<div class="row'+(S.anim?' in':'')+'"><span class="mono">'+b[0]+'</span><span class="mut">'+b[1]+'</span><span class="mono r">'+n0(b[2])+'</span>'+(stay?chip('c-warn',S.rel?'Finish on rev C':'Stays on rev C'):chip(S.rel?'c-ok':'c-info',S.rel?'Updated to rev D':'Will switch to rev D'))+'</div>';});
rv+='<div class="cd im"><div class="ct">Open builds this change touches<span class="mut" style="font-weight:500">2 of 3 switch</span></div><div class="row h"><span>Build</span><span>Status</span><span class="r">Units</span><span>Result</span></div>'+ir+'</div>';}
rv+='<div class="acts">'+(!S.checked?'<button type="button" class="bt pri" id="ckb">Check open builds</button>':'')+(S.checked&&!S.rel?'<button type="button" class="bt pri" id="rlb">Release rev D</button>':'')+'</div>';}
$('p-rv').innerHTML=rv;S.anim=false;}
function resetState(){S={sel:false,open:false,tab:'ln',draft:false,checked:false,rel:false,anim:false};rw.value='CAP-1007';rs.value='Higher voltage rating';$('frw').classList.remove('err');$('frs').classList.remove('err');render();}
function badInputs(){var a=(rw.value||'').trim().toUpperCase()!=='CAP-1007',b=!(rs.value||'').trim();$('frw').classList.toggle('err',a);$('frs').classList.toggle('err',b);return a||b;}
function onRv(){return S.tab==='rv'?null:[tabs[2],'Back to Revisions','below'];}
var CAPAT=function(hh){var r=rel($('p-ln').parentNode);return{l:r.l+10,t:visH()-hh-50};};
var ST=[
{id:'open',target:function(){return tpcb;},prompt:'Click PCBA-210 in the BOM',where:'below',run:function(){S.sel=true;S.open=true;S.tab='ln';S.anim=true;render();},after:['Each level is costed on its own','Boards, harnesses and enclosures build up to the finished unit. PCBA-210 is on rev C.']},
{id:'cost',target:function(){return tabs[1];},prompt:'Click Cost',where:'below',run:function(){S.tab='co';render();},after:['Unit cost rolls up from every level','Board $20.50, harness $6.25, enclosure $11.40. A build really costs $38.15.']},
{id:'newrev',target:function(){return nrv;},prompt:'Click New revision',where:'below',ok:function(){return !badInputs();},run:function(){badInputs();S.draft=true;S.tab='rv';S.anim=true;render();},after:['Every change is a new revision','Draft rev D swaps in CAP-1007 for $0.54 more a unit. Rev C stays on record.']},
{id:'check',target:function(){return $('ckb');},back:onRv,prompt:'Click Check open builds',where:'below',run:function(){S.checked=true;S.tab='rv';S.anim=true;render();},after:['See the builds a change touches first','MO-3102 and MO-3110 will switch. MO-3105 is in progress and stays on rev C.']},
{id:'release',target:function(){return $('rlb');},back:onRv,prompt:'Click Release rev D',where:'below',run:function(){S.rel=true;S.tab='rv';render();},after:['Released, without stopping the line','Builds not started pick up rev D. The one in progress finishes on rev C.']},
{id:'cost2',target:function(){return tabs[1];},prompt:'Click Cost again',where:'below',run:function(){S.tab='co';S.anim=true;render();},after:['You saw what one part change costs','Unit cost $38.69. $135.00 more on MO-3102 and $216.00 on MO-3110, $351.00 together.']}];
'''
