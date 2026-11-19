"""Functional beverage card 3: Formula Versions & Reformulation. Layout: a board.
Top: the read only formula field with Open versions. Board: three columns the versions move between by click (History,
In production, Draft). The draft shows what changed from production, both show cost per can, approval moves v8 into
production and v7 into history with its dates. Bottom strip: the cost change. Costs are kept in cents so sums are exact."""
from frame_auto import header

SUMMARY = 'Formula Versions & Reformulation (open v7 in production beside draft v8, see stevia replace cane sugar and flavor drop to 0.6%, $0.84 against $0.79 a can, approve v8, view the history)'
ARIA = 'Interactive product screen: open the production version of a formula beside a draft, see the ingredient differences and cost per can for each, approve the draft for production and view earlier versions'
STEPS = 5
STUDIO = dict(lede='A typical formula version board on your Sutton data. Want it different? Describe the change.',
              examples=['A sensory panel score per draft', 'Two approvers for production', 'Cost at next quarter prices', 'A label change checklist'],
              built_on='BOMs, versions and costs', change='Columns, approvals and views')

ICON = '<path d="M3 3h4v4H3zM9 3h4v4H9zM3 9h4v4H3zM9 9h4v4H9z"/>'

CSS = (
 '.fld input[readonly]{background:#F4F4F5;color:#3F3F46;cursor:default;pointer-events:none}'
 '.g3{display:grid;grid-template-columns:186px 236px 214px;grid-template-rows:62px 398px 60px;gap:10px;padding:10px 44px 0 16px}'
 '.top{grid-column:1/4;display:flex;flex-direction:column;justify-content:center;gap:5px;padding:0 12px}.top .frm{display:flex;align-items:flex-end;gap:8px}.top .fld{width:200px}.top .ctx{font-size:8.9px;color:#71717A}.top .rs{margin-left:auto}'
 '.col{display:flex;flex-direction:column;min-width:0}.col>.empt{margin:9px;flex:1;padding:10px}.col .ct .bt{font-size:9px;padding:2px 8px}'
 '.vs{display:flex;flex-direction:column;gap:7px;padding:8px}'
 '.vc{border:1px solid #E4E4E7;border-radius:8px;background:#fff;overflow:hidden}.vc .vh{display:flex;align-items:center;gap:6px;padding:6px 8px;border-bottom:1px solid #F0F0F1}.vc .vh b{font-family:"JetBrains Mono",ui-monospace,monospace;font-size:11px;margin-right:auto}'
 '.vc .row{grid-template-columns:1fr 50px;font-size:9px;min-height:22px;padding:0 8px}.vc .row span:last-child{text-align:right;font-family:"JetBrains Mono",ui-monospace,monospace}'
 '.vc .row.add{background:#F0FDF4;color:#166534}.vc .row.rem{background:#FEF2F2;color:#991B1B;text-decoration:line-through}.vc .row.chg{background:#FEF9E7;color:#92400E}'
 '.vc .cs{display:flex;justify-content:space-between;padding:6px 8px;border-top:1px solid #E4E4E7;background:#FAFAFA;font-size:9.2px;font-weight:600}.vc .cs b{font-family:"JetBrains Mono",ui-monospace,monospace}'
 '.vc .ft{display:flex;gap:6px;padding:6px 8px;border-top:1px solid #F0F0F1}.vc .ft .bt{font-size:9px;padding:3px 8px}.vc.pro{border-color:#86EFAC}.vc.dr{border-style:dashed}'
 '.hk{border:1px solid #E4E4E7;border-radius:7px;padding:6px 8px;font-size:9px;background:#FAFAFA;color:#52525B;line-height:1.4}.hk b{font-family:"JetBrains Mono",ui-monospace,monospace;color:#18181B}'
 '.strip{grid-column:1/4;display:grid;grid-template-columns:repeat(4,1fr);gap:8px;align-items:center;padding:0 12px}.strip .kv b{font-size:12px;font-family:"JetBrains Mono",ui-monospace,monospace}.strip .wait{grid-column:1/5;font-size:9.2px;color:#A1A1AA}'
 '.tot{margin-top:auto;padding:8px 10px;border-top:1px solid #E4E4E7;font-size:8.8px;color:#52525B;line-height:1.4;background:#FAFAFA}'
)

WIN = (
 header(ICON, 'Formula versions', 'Drafts beside production, with cost and changes')
 + '<div class="g3"><div class="cd top"><div class="frm"><label class="fld"><small>Formula</small>'
 '<input id="ifm" value="Focus Citrus Sparkling" readonly tabindex="-1" autocomplete="off" spellcheck="false"></label>'
 '<button type="button" class="bt pri" id="ovb">Open versions</button><span class="rs" id="rs"></span></div><div class="ctx">FCS-12, 12 oz can</div></div>'
 '<div class="cd col" id="c1"></div><div class="cd col" id="c2"></div><div class="cd col" id="c3"></div><div class="cd strip" id="stp"></div></div>'
)

JS = r'''
var FOC='.hd>*,.top .fld,.top .ctx,#ovb,.col>.ct,.vc,.hk,.col>.empt,.strip';
var V7={v:'v7',lines:[['Sparkling water','Balance'],['Cane sugar','2.4%'],['Natural citrus flavor','0.8%'],['Citric acid','0.3%'],['L-theanine','0.06%']],cost:[['Sweetener',9],['Flavor',12],['Actives',38],['Can and lid',25]],since:'Mar 3, 2026'};
var V8={v:'v8',lines:[['Sparkling water','Balance'],['Stevia leaf extract','0.03%'],['Natural citrus flavor','0.6%'],['Citric acid','0.3%'],['L-theanine','0.06%']],cost:[['Sweetener',7],['Flavor',9],['Actives',38],['Can and lid',25]]};
var OLD=[['v6','Oct 2, 2025 to Mar 3, 2026'],['v5','May 14 to Oct 2, 2025']],TODAY='Nov 19, 2026';
var S;
function cents(V){return V.cost.reduce(function(a,c){return a+c[1];},0);}
function $c(c){return (c<0?'−':'')+'$'+(Math.abs(c)/100).toFixed(2);}
function dc(){return cents(V8)-cents(V7);}
function pct(){var m=dc()<0?String.fromCharCode(8722):'';return m+Math.abs(dc()/cents(V7)*100).toFixed(1)+'%';}
function cls(V,l){if(!S.diff||V!==V8&&V!==V7)return '';var a=V7.lines.map(function(x){return x[0];}),b=V8.lines.map(function(x){return x[0];});
if(V===V8&&a.indexOf(l[0])<0)return ' add';if(V===V7&&b.indexOf(l[0])<0)return ' rem';var o=(V===V8?V7:V8).lines.filter(function(x){return x[0]===l[0];})[0];return o&&o[1]!==l[1]?' chg':'';}
function card(V,role){var id='vc-'+V.v;return '<div class="vc in'+(role==='pro'?' pro':role==='dr'?' dr':'')+'" id="'+id+'"><div class="vh"><b>'+V.v+'</b>'+(role==='pro'?'<span class="ch c-ok">In production</span>':role==='dr'?'<span class="ch c-info">Draft</span>':'<span class="ch c-idle">History</span>')+'</div>'+
V.lines.map(function(l){return '<div class="row'+cls(V,l)+'"><span>'+l[0]+'</span><span>'+l[1]+'</span></div>';}).join('')+
(S.cost?'<div class="cs"><span>Cost per can</span><b id="cpc-'+V.v+'">'+$c(cents(V))+'</b></div>':'')+
(role==='dr'?'<div class="ft">'+(!S.diff?'<button type="button" class="bt" id="dfb">Show changes</button>':'')+(S.diff&&!S.cost?'<button type="button" class="bt" id="csb">Cost per can</button>':'')+(S.cost?'<button type="button" class="bt pri" id="apb">Approve for production</button>':'')+'</div>':'')+'</div>';}
function render(){
var ovb=$('ovb');ovb.className='bt '+(S.op?'done':'pri');ovb.textContent=S.op?'Opened':'Open versions';
$('rs').innerHTML=S.ap?'<span class="ch c-ok" id="rst">v8 in production</span>':S.op?'<span class="ch c-idle">1 draft</span>':'';
var h='<div class="ct"><span>History</span>'+(S.ap&&!S.hist?'<button type="button" class="bt" id="hib">History</button>':S.hist?'<span class="ch c-idle" id="hct">'+(OLD.length+1)+' versions</span>':'')+'</div>';
if(!S.ap)h+='<div class="empt"><span>Earlier versions land here when a draft is approved.</span></div>';
else{h+='<div class="vs">'+card(V7,'his').replace('<div class="vh"><b>v7</b>','<div class="vh"><b>v7</b>')+'<div class="hk in" id="h7"><b>v7</b> in production '+V7.since+' to '+TODAY+'</div>'+(S.hist?OLD.map(function(o){return '<div class="hk in" id="h-'+o[0]+'"><b>'+o[0]+'</b> in production '+o[1]+'</div>';}).join(''):'')+'</div>';}
h+='<div class="tot">Every version is kept with its dates.</div>';
$('c1').innerHTML=h;
var p='<div class="ct"><span>In production</span>'+(S.op?'<span class="ch c-ok">1</span>':'')+'</div>';
p+=S.op?'<div class="vs" id="pro">'+card(S.ap?V8:V7,'pro')+(S.ap?'<div class="hk in">Approved '+TODAY+' by the R&amp;D lead. Next batch uses v8.</div>':'')+'</div>':'<div class="empt"><span>Open the formula to see the version in production.</span></div>';
p+='<div class="tot">Exactly one version runs in production.</div>';
$('c2').innerHTML=p;
var d='<div class="ct"><span>Draft</span></div>';
d+=S.op&&!S.ap?'<div class="vs" id="drf">'+card(V8,'dr')+'</div>':'<div class="empt"><span>'+(S.ap?'No draft open. Start a new draft from v8.':'Drafts from R&amp;D sit here beside production.')+'</span></div>';
d+='<div class="tot">Drafts never reach a batch until approved.</div>';
$('c3').innerHTML=d;
$('stp').innerHTML=S.cost?'<div class="kv in"><small>v7 per can</small><b id="s7">'+$c(cents(V7))+'</b></div><div class="kv in"><small>v8 per can</small><b id="s8">'+$c(cents(V8))+'</b></div><div class="kv in"><small>Change</small><b id="sdc">'+$c(dc())+'</b></div><div class="kv in"><small>Change, percent</small><b id="spc">'+pct()+'</b></div>':'<div class="wait">Cost per can and the change between versions show here.</div>';
}
function resetState(){S={op:false,diff:false,cost:false,ap:false,hist:false};render();}
function capN(){var i=cap.querySelector('.m i');return i?+i.textContent:1;}
var CAPAT=function(hh){var w=cap.offsetWidth;return {l:visW()-w-14,t:58};};
var ST=[
{id:'op',target:function(){return $('ovb');},prompt:'Open the versions',where:'below',run:function(){S.op=true;render();},
 after:function(){return['Production beside the draft','v7 is in production. Draft v8 from R&D sits beside it.'];}},
{id:'diff',target:function(){return $('dfb');},prompt:'Show the changes',where:'above',run:function(){S.diff=true;render();},
 after:function(){return['What changed from production','Stevia leaf extract replaces cane sugar. Natural citrus flavor drops from 0.8% to 0.6%.'];}},
{id:'cost',target:function(){return $('csb');},prompt:'Read cost per can',where:'above',run:function(){S.cost=true;render();},
 after:function(){return['Cost per can for each version','v7 '+$c(cents(V7))+', v8 '+$c(cents(V8))+': '+$c(dc())+' a can ('+pct()+').'];}},
{id:'ap',target:function(){return $('apb');},prompt:'Approve v8',where:'above',run:function(){S.ap=true;render();},
 after:function(){return['Approval promotes the draft','v8 is in production. v7 moves to history with its dates.'];}},
{id:'hist',target:function(){return $('hib');},prompt:'View the history',where:'below',run:function(){S.hist=true;render();},
 after:function(){return['Every earlier version, kept','v7, v6 and v5 with the dates each was in production.'];}}];
'''
