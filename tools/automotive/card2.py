"""Automotive card 2: BOM Revisions & Engineering Changes (working title). Layout: side by side comparison table with an
approval stepper. ECO-0192 moves BA-5520 from Rev C to Rev D, effective Dec 1, 2026: open work orders due before then
stay on Rev C, the rest switch. Money is kept in cents so every roll-up is exact."""
from frame_auto import header

SUMMARY = 'BOM Revisions & Engineering Changes (ECO-0192 compares Rev C and Rev D of BA-5520 side by side, rolls up the cost change, splits open work orders by effectivity date and releases through an approval stepper)'
ARIA = 'Interactive product screen: open ECO-0192, compare BA-5520 Rev C and Rev D line by line, roll up the cost from $4.82 to $5.04, set effectivity to December 1 so one work order stays on Rev C and two switch, then approve and release'
STEPS = 5
STUDIO = dict(lede='A typical engineering change screen, built on your Sutton data with Studio. Want it different? Describe the change.',
              examples=['A PPAP document checklist on each ECO', 'An approval step for the customer', 'A where used list across every BOM', 'A stock run out date for the old part'],
              built_on='Items, BOMs, revisions and work orders', change='Approvers, fields and rules')

ICON = '<rect x="2" y="2.5" width="5" height="11" rx="1"/><rect x="9" y="2.5" width="5" height="11" rx="1"/><path d="M3.5 5.5h2M3.5 8h2M10.5 5.5h2M10.5 8h2M10.5 10.5h2"/>'

CSS = (
 '.g2{display:grid;grid-template-columns:186px 1fr;gap:10px;padding:10px 40px 0 16px}'
 '.col{display:flex;flex-direction:column;gap:10px;min-width:0}'
 '.eco .row{grid-template-columns:1fr auto;min-height:36px;padding:4px 11px;font-size:9.6px}.eco .row .t{display:flex;flex-direction:column;gap:1px;line-height:1.25;min-width:0}.eco .row .t span{color:#71717A;font-size:8.9px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}'
 '.apv{height:332px;flex:none;display:flex;flex-direction:column}.apv .bd{padding:12px 12px 0;display:flex;flex-direction:column;gap:0;flex:1}'
 '.sp{display:grid;grid-template-columns:22px 1fr;gap:8px;position:relative;min-height:64px}.sp:not(:last-child)::before{content:"";position:absolute;left:10.5px;top:24px;bottom:2px;width:1px;background:#E4E4E7}'
 '.sp.ok:not(:last-child)::before{background:#86EFAC}.sp .dot{width:22px;height:22px;border-radius:50%;border:1px solid #D4D4D8;background:#fff;display:grid;place-items:center;font-size:9px;font-weight:600;color:#71717A;transition:background-color .3s,border-color .3s}'
 '.sp.ok .dot{background:#16A34A;border-color:#16A34A;color:#fff}.sp.nx .dot{border-color:#18181B;color:#18181B}.sp .tx{display:flex;flex-direction:column;gap:2px;font-size:9.8px;line-height:1.3;padding-top:3px}.sp .tx span{font-size:8.9px;color:#71717A}'
 '.apv .ft{padding:10px 12px 12px;border-top:1px solid #F0F0F1;display:flex;flex-direction:column;gap:7px;font-size:9.2px;color:#52525B}'
 '.cmp{height:282px;flex:none;display:flex;flex-direction:column}.cmp .es{display:flex;align-items:center;gap:8px;padding:7px 11px;border-bottom:1px solid #F0F0F1;font-size:9.4px;color:#52525B;min-height:38px}.cmp .es .grow{line-height:1.35}'
 '.bt2{font-size:9.6px}.tb .row{grid-template-columns:52px 1fr 40px 26px 42px 26px 42px;min-height:24px;font-size:9.4px;white-space:nowrap;gap:6px}.tb .row span:nth-child(n+3){text-align:right}'
 '.tb .gh{display:grid;grid-template-columns:52px 1fr 40px 74px 74px;gap:6px;padding:4px 11px 0;font-size:8.6px;font-weight:600;color:#71717A}.tb .gh span:nth-child(n+3){text-align:center;border-bottom:1px solid #E4E4E7;padding-bottom:2px}'
 '.row.rm{background:#FEF2F2}.row.rm span:nth-child(-n+2){text-decoration:line-through;text-decoration-color:#F87171;color:#991B1B}.row.ad{background:#F0FDF4}.row.ad span:nth-child(-n+2){color:#166534}'
 '.row.tot{font-weight:600;background:#FAFAFA;min-height:28px}.dl{display:inline-flex;align-items:center;gap:6px;margin-left:auto}'
 '.eff{height:194px;flex:none}.eff .frm{display:flex;align-items:flex-end;gap:8px;padding:8px 11px;border-bottom:1px solid #F0F0F1}.eff .fld{width:112px}.eff .nt{font-size:9px;color:#71717A;margin-left:4px;padding-bottom:6px}'
 '.wo .row{grid-template-columns:62px 62px 70px 1fr;min-height:27px;font-size:9.4px;white-space:nowrap}'
 '.hst{display:flex;align-items:center;gap:8px;font-size:9.2px;color:#52525B;padding:2px 2px 0;white-space:nowrap}.hst b{font-weight:600;color:#18181B}'
 '.cmp .empt,.eff .empt{margin:10px;flex:1}.eff .empt{height:126px}.apv .empt{margin:10px;flex:1}'
)

WIN = (
 header(ICON, 'Engineering changes', 'BOM revisions, bracket assembly BA-5520')
 + '<div class="g2"><div class="col"><div class="cd eco" id="eco"></div><div class="cd apv" id="apv"></div></div>'
 '<div class="col"><div class="cd cmp" id="cmp"></div><div class="cd eff" id="eff"></div><div class="hst" id="hst"></div></div></div>'
)

JS = r'''
var FOC='.hd>*,.eco .ct,.eco .row,.apv .ct,.sp,.apv .ft>*,.cmp .ct,.cmp .es>*,.tb .gh,.tb .row,.eff .ct,.eff .frm>*,.wo .row,.hst';
var ECO=[['ECO-0192','BA-5520 fastener change','Draft'],['ECO-0188','BA-5410 label update','Released'],['ECO-0185','BKT-210 bushing','Released'],['ECO-0181','BA-5520 label','Released'],['ECO-0176','BA-5300 gauge','Cancelled']];
var UNIT={'STP-300':210,'FST-118':46,'FST-121':52,'WSH-044':5,'BSH-07':120,'LBL-12':60};
var DESC={'STP-300':'Stamped bracket','FST-118':'Fastener, zinc plated','FST-121':'Fastener, zinc nickel','WSH-044':'Flat washer','BSH-07':'Rubber bushing','LBL-12':'Part label'};
var REVC=[['STP-300',1],['FST-118',2],['BSH-07',1],['LBL-12',1]];
var REVD=[['STP-300',1],['FST-121',2],['WSH-044',2],['BSH-07',1],['LBL-12',1]];
var ORDER=['STP-300','FST-118','FST-121','WSH-044','BSH-07','LBL-12'];
var WOS=[['WO-7132',[11,20],'Released'],['WO-7140',[12,2],'Planned'],['WO-7146',[12,9],'Planned']];
var EFF=[12,1],MON=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];
var APV=[['Engineering review','A. Patel'],['Quality sign off','L. Ortiz'],['Release','Document control']];
var S;
function qty(rev,p){for(var i=0;i<rev.length;i++)if(rev[i][0]===p)return rev[i][1];return 0;}
function roll(rev){return rev.reduce(function(a,l){return a+l[1]*UNIT[l[0]];},0);}
function usd(c){return '$'+(c/100).toFixed(2);}
function dlt(c){return (c<0?'minus ':'+')+usd(Math.abs(c));}
function before(d,e){return d[0]<e[0]||(d[0]===e[0]&&d[1]<e[1]);}
function dstr(d){return MON[d[0]-1]+' '+d[1];}
function stays(){return WOS.filter(function(w){return before(w[1],S.eff);});}
function moves(){return WOS.filter(function(w){return !before(w[1],S.eff);});}
function render(){
var e='<div class="ct">Change orders<span class="mut" style="font-weight:500">5</span></div>'+ECO.map(function(x,i){var st=i===0&&S.rel?'Released':x[2];return '<button type="button" class="row'+(S.sel&&i===0?' sel':'')+'" id="e-'+x[0]+'"><span class="t"><b class="mono">'+x[0]+'</b><span>'+x[1]+'</span></span><span class="ch '+(st==='Released'?'c-ok':st==='Draft'?'c-warn':'c-idle')+'">'+st+'</span></button>';}).join('');
$('eco').innerHTML=e;
var a='<div class="ct">Approval<span class="ch '+(S.rel?'c-ok':S.sel?'c-warn':'c-idle')+'" id="ast">'+(S.rel?'Released':S.sel?'Draft':'None open')+'</span></div>';
if(!S.sel)a+='<div class="empt"><b>No change selected</b><span>Pick a change order to see who signs it off.</span></div>';
else{a+='<div class="bd">'+APV.map(function(x,i){var ok=S.ap>i,nx=!ok&&S.ap===i;return '<div class="sp'+(ok?' ok':nx?' nx':'')+'"><span class="dot">'+(ok?'<svg width="10" height="10" viewBox="0 0 10 10" fill="none" aria-hidden="true"><path d="M2 5.2l2 2 4-4.4" stroke="#fff" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>':(i+1))+'</span><span class="tx"><b>'+x[0]+'</b><span>'+x[1]+(ok?', approved Nov 11':nx?', waiting':'')+'</span></span></div>';}).join('')+'</div>';
a+='<div class="ft">'+(S.rel?'<span class="ch c-ok" style="align-self:flex-start">Rev D released</span><span>Effective '+dstr(S.eff)+', 2026. Earlier work orders finish on Rev C.</span>':'<button type="button" class="bt pri" id="apr" style="align-self:flex-start"'+(S.effset?'':' disabled')+'>Approve and release</button><span>'+(S.effset?'Both approvers are notified, then Rev D goes live on its date.':'Set the effective date first.')+'</span>')+'</div>';}
$('apv').innerHTML=a;
var c='<div class="ct"><span>BOM comparison</span>'+(S.cmp?'<span class="dl"><span class="ch c-info">Rev C, active</span><span class="ch c-warn">Rev D, '+(S.rel?'released':'draft')+'</span></span>':'')+'</div>';
if(!S.sel)c+='<div class="empt"><b>Nothing to compare</b><span>Select a change order to compare its BOM revisions line by line.</span></div>';
else{c+='<div class="es'+(S.an1?' in':'')+'"><span class="grow"><b class="mono">ECO-0192</b> Replace FST-118 with FST-121 and add washer WSH-044. Reason: clamp load loss found in a torque audit.</span>'+(S.cmp?'':'<button type="button" class="bt bt2" id="cmpb">Compare Rev C and Rev D</button>')+'</div>';
if(S.cmp){var tc=roll(REVC),td=roll(REVD);
c+='<div class="tb'+(S.an2?' in':'')+'"><div class="gh"><span></span><span></span><span></span><span>Rev C</span><span>Rev D</span></div><div class="row h"><span>Part</span><span>Description</span><span>Unit</span><span>Qty</span><span>Cost</span><span>Qty</span><span>Cost</span></div>'+
ORDER.map(function(p){var qc=qty(REVC,p),qd=qty(REVD,p),cl=qc&&!qd?' rm':!qc&&qd?' ad':'';return '<div class="row'+cl+'"><span class="mono">'+p+'</span><span>'+DESC[p]+'</span><span class="mono">'+usd(UNIT[p])+'</span><span class="mono">'+(qc||'')+'</span><span class="mono" id="cc-'+p+'">'+(S.cost&&qc?usd(qc*UNIT[p]):'')+'</span><span class="mono">'+(qd||'')+'</span><span class="mono" id="cd-'+p+'">'+(S.cost&&qd?usd(qd*UNIT[p]):'')+'</span></div>';}).join('')+
'<div class="row tot"><span>Roll up</span><span>'+(S.cost?'<span class="ch c-warn" id="dlt">'+dlt(td-tc)+' per assembly</span>':'<button type="button" class="bt bt2" id="rup">Roll up cost</button>')+'</span><span></span><span></span><span class="mono" id="rc">'+(S.cost?usd(tc):'')+'</span><span></span><span class="mono" id="rd">'+(S.cost?usd(td):'')+'</span></div></div>';}}
$('cmp').innerHTML=c;
var f='<div class="ct">Effectivity and open work orders'+(S.effset?'<span class="ch c-info" id="spl">'+stays().length+' stays, '+moves().length+' switch</span>':'')+'</div>';
if(!S.sel)f+='<div class="empt"><b>No work orders yet</b><span>Open work orders for the part show here with the revision each will use.</span></div>';
else{f+='<div class="frm"><label class="fld" id="fef"><small>Rev D effective from</small><input id="ief" value="'+S.v+'" autocomplete="off" spellcheck="false"><span class="em">Use a date like 12/01/2026</span></label>'+(S.effset?'<button type="button" class="bt done" disabled>Effectivity set</button>':'<button type="button" class="bt" id="efb"'+(S.cost?'':' disabled')+'>Set effectivity</button>')+'<span class="nt">Work orders due before this date finish on Rev C.</span></div>';
f+='<div class="wo"><div class="row h"><span>Work order</span><span>Due</span><span>Status</span><span>Revision</span></div>'+WOS.map(function(w){var st=before(w[1],S.eff);return '<div class="row'+(S.an3?' flash':'')+'"><span class="mono">'+w[0]+'</span><span>'+dstr(w[1])+'</span><span class="mut">'+w[2]+'</span><span id="r-'+w[0]+'">'+(S.effset?(st?'<span class="ch c-idle">Stays on Rev C</span>':'<span class="ch c-ok">Switches to Rev D</span>'):'<span class="ch c-idle">Rev C</span>')+'</span></div>';}).join('')+'</div>';}
$('eff').innerHTML=f;
$('hst').innerHTML='<b>Revisions</b><span>A Feb 2025, B Aug 2025, C Mar 2026'+(S.rel?', D Dec 2026':'')+'</span>';
S.an1=S.an2=S.an3=false;}
$('eff').addEventListener('input',function(e){if(e.target.id==='ief')S.v=e.target.value;});
function pdate(v){var m=String(v).trim().match(/^(\d{1,2})\/(\d{1,2})\/(2026)$/);if(!m)return null;var mo=+m[1],d=+m[2];if(mo<1||mo>12||d<1||d>31)return null;return [mo,d];}
function resetState(){S={sel:false,cmp:false,cost:false,effset:false,rel:false,ap:0,eff:EFF,v:'12/01/2026'};render();}
var CAPAT=function(hh){return cur>=4?{l:visW()-cap.offsetWidth-14,t:96}:{l:14,t:visH()-hh-14};};
var ST=[
{id:'sel',target:function(){return $('e-ECO-0192');},prompt:'Open change order ECO-0192',where:'right',run:function(){S.sel=true;S.an1=true;render();},
 after:['An engineering change opens with the BOM and the work orders it touches','ECO-0192 moves BA-5520 from Rev C to Rev D. Engineering review, then quality sign off.']},
{id:'cmp',target:function(){return $('cmpb');},prompt:'Compare the two revisions',where:'below',run:function(){S.cmp=true;S.an2=true;render();},
 after:['Both revisions side by side, changes highlighted','FST-118 comes out, FST-121 and two WSH-044 washers go in. STP-300, BSH-07 and LBL-12 stay.']},
{id:'cost',target:function(){return $('rup');},prompt:'Roll up the cost',where:'below',run:function(){S.cost=true;render();},
 after:function(){var tc=roll(REVC),td=roll(REVD);return['The cost change rolls up from every line',usd(tc)+' on Rev C, '+usd(td)+' on Rev D, '+dlt(td-tc)+' per assembly.'];}},
{id:'eff',target:function(){return $('efb');},prompt:'Set the effective date',where:'below',ok:function(){var d=pdate(S.v),b=!d;$('fef').classList.toggle('err',b);return !b;},
 run:function(){S.eff=pdate(S.v)||EFF;S.effset=true;S.an3=true;render();},
 after:function(){var s=stays(),m=moves();return['Open work orders switch only after the date',s.map(function(w){return w[0];}).join(', ')+' due '+s.map(function(w){return dstr(w[1]);}).join(', ')+' stays on Rev C. '+m.map(function(w){return w[0];}).join(' and ')+' switch to Rev D.'];}},
{id:'apr',target:function(){return $('apr');},prompt:'Approve and release',where:'above',run:function(quick){if(quick){S.ap=3;S.rel=true;render();return;}S.ap=1;render();later(function(){S.ap=2;render();},200);later(function(){S.ap=3;S.rel=true;render();},400);},
 after:function(){return['Approvals step through in order, then the change is released','A. Patel and L. Ortiz approved. Rev D is released, effective '+dstr(S.eff)+'.'];}}];
'''
