"""Wineries card 2: Dry Goods & Bottling Dates. Layout: a board (a plan grid with one row per dry good).
Top: the read only bottling plan field with Open plan. Middle: the plan board, one row per dry good (glass, corks,
capsules, labels) with the need, the stock on hand, open orders placed in a lane before or after the bottling date,
what counts by the bottling date and the position. Bottom left: the supplier order raised from the short line.
Bottom right: the plan check, item by item.
Only an order arriving on or before the bottling date counts. The purchase order is the next whole pallet of 700."""
from frame_auto import header

SUMMARY = 'Dry Goods & Bottling Dates (Reserve Red bottling Mar 14, 1,200 cases need 14,400 of glass, corks, capsules and labels; glass 9,000 on hand with 6,000 arriving Mar 28, after the bottling date, so 5,400 short; PO of 8 pallets of 700, 5,600 bottles, clears it to 14,600, 200 over)'
ARIA = 'Interactive product screen: open a bottling plan, check stock, open orders and arrival dates for each dry good, find the item that is short, raise a supplier order from that line and see the plan clear'
STEPS = 5
STUDIO = dict(lede='A typical bottling plan on your Sutton data. Want it different? Describe the change.',
              examples=['Lead times by supplier', 'A buffer per dry good', 'Shared glass across blends', 'A weekly shortage email'],
              built_on='Items, BOMs, purchase orders and stock', change='Fields, rules and views')

ICON = '<rect x="2" y="2.5" width="12" height="11" rx="1.5"/><path d="M2 6h12M2 9.5h12M6 6v7.5"/>'

CSS = (
 '.fld input[readonly]{background:#F4F4F5;color:#3F3F46;cursor:default;pointer-events:none}'
 '.g2{display:grid;grid-template-columns:330px 316px;grid-template-rows:60px 250px 210px;gap:10px;padding:10px 44px 0 16px;width:716px}'
 '.top{grid-column:1/3;display:flex;flex-direction:column;justify-content:center;gap:5px;padding:0 12px}.top .frm{display:flex;align-items:flex-end;gap:8px}.top .fld{width:300px}.top .ctx{font-size:8.9px;color:#71717A}.top .rs{margin-left:auto;display:flex;gap:6px}'
 '.bd{grid-column:1/3;display:flex;flex-direction:column}.bd>.empt{margin:9px;flex:1;padding:8px}.ct .bt{font-size:9px;padding:2px 9px}.ct .r3{display:flex;gap:6px;align-items:center}'
 '.pg{display:grid;grid-template-columns:98px 46px 50px 104px 8px 104px 56px 1fr;column-gap:6px;align-items:stretch}'
 '.pg.h{padding:4px 9px;background:#FAFAFA;border-bottom:1px solid #E4E4E7;font-size:8.4px;color:#71717A;font-weight:500}.pg.h>span:nth-child(2),.pg.h>span:nth-child(3),.pg.h>span:nth-child(7),.pg.h>span:nth-child(8){text-align:right}'
 '.pg.h .bm{color:#7F1D1D;font-weight:600;text-align:center}'
 '.pr{padding:0 9px;border-top:1px solid #F0F0F1;min-height:41px;transition:background-color .35s,box-shadow .35s}.pr:first-of-type{border-top:0}'
 '.pr>span{display:flex;flex-direction:column;justify-content:center;font-size:9.2px}.pr small{font-size:8px;color:#71717A}.pr .n{font-family:"JetBrains Mono",ui-monospace,monospace;text-align:right;align-items:flex-end}'
 '.pr .ln{background:#FAFAFA;border-radius:6px;padding:3px;gap:3px;justify-content:center}.pr .ln.af{background:#F4F4F5}'
 '.pr .dv{background:repeating-linear-gradient(#7F1D1D 0 4px,transparent 4px 7px);width:2px;justify-self:center}'
 '.ar{display:flex;align-items:center;justify-content:space-between;gap:4px;border:1px solid #E4E4E7;background:#fff;border-radius:5px;padding:2px 5px;font-size:8.3px}.ar b{font-family:"JetBrains Mono",ui-monospace,monospace;font-size:8.6px}.ar.lt{border-color:#FCA5A5;background:#FEF2F2;color:#991B1B}.ar.nw{border-color:#86EFAC;background:#F0FDF4;color:#166534}'
 '.pr .ps{align-items:flex-end;gap:2px}.pr .ps .ch{font-size:8.6px}.pr .ps b{font-family:"JetBrains Mono",ui-monospace,monospace;font-size:9.6px}'
 '.pr.sh{background:#FEF2F2;box-shadow:inset 3px 0 0 #DC2626}.pr.ok{background:#F0FDF4;box-shadow:inset 3px 0 0 #16A34A}.pr .po{margin-top:3px}.pr .po .bt{font-size:8.6px;padding:2px 7px}'
 '.po2,.ck2{display:flex;flex-direction:column}.po2>.empt,.ck2>.empt{margin:9px;flex:1;padding:8px}'
 '.ph{padding:8px 11px 0;display:flex;justify-content:space-between;align-items:flex-start}.ph .kv b{font-family:"JetBrains Mono",ui-monospace,monospace;font-size:13px}'
 '.pl{margin:7px 11px 0;border:1px solid #E4E4E7;border-radius:8px;overflow:hidden}.pl .row{grid-template-columns:1fr 50px 64px;font-size:9px;min-height:24px;padding:0 7px}.pl .row>span:nth-child(n+2){text-align:right;font-family:"JetBrains Mono",ui-monospace,monospace}.pl .row.h>span{font-family:inherit!important}'
 '.pals{margin:7px 11px 0;display:grid;grid-template-columns:repeat(8,1fr);gap:3px}.pals i{height:12px;border-radius:3px;background:#18181B;opacity:.85}'
 '.calc{margin:6px 11px 0;padding:4px 7px;border-radius:6px;background:#FAFAFA;border:1px solid #F0F0F1;font-family:"JetBrains Mono",ui-monospace,monospace;font-size:8.8px;text-align:center;white-space:nowrap}'
 '.pa2{margin:7px 11px 0;display:flex;align-items:center;gap:8px;font-size:8.8px;color:#52525B}.pa2 .bt{margin-left:auto;font-size:9px;padding:3px 9px}'
 '.cl2{padding:5px 11px 0;display:flex;flex-direction:column;gap:2px}.cl2 div{display:grid;grid-template-columns:1fr 70px 64px;align-items:center;font-size:9px;color:#3F3F46;padding:2px 0;border-bottom:1px dashed #F0F0F1}.cl2 div span:nth-child(2){text-align:right;font-family:"JetBrains Mono",ui-monospace,monospace}.cl2 div span:last-child{text-align:right}'
 '.big2{margin:7px 11px 0;padding:7px 9px;border-radius:8px;display:flex;justify-content:space-between;align-items:center;font-size:9.4px;font-weight:600}.big2.w{background:#FEF2F2;color:#991B1B;border:1px solid #FECACA}.big2.g{background:#F0FDF4;color:#166534;border:1px solid #BBF7D0}.big2.i{background:#FAFAFA;color:#52525B;border:1px solid #F0F0F1}'
 '.tot{margin-top:auto;padding:7px 11px;border-top:1px solid #E4E4E7;font-size:9px;color:#52525B;line-height:1.4;background:#FAFAFA}.ck2 .tot{padding-right:90px}'
)

WIN = (
 header(ICON, 'Bottling plan', 'Dry goods against the bottling date')
 + '<div class="g2"><div class="cd top"><div class="frm"><label class="fld"><small>Bottling plan</small>'
 '<input id="ipl" value="Reserve Red, bottling Mar 14, 1,200 cases" readonly tabindex="-1" autocomplete="off" spellcheck="false"></label>'
 '<button type="button" class="bt pri" id="opb">Open plan</button><span class="rs" id="rs"></span></div><div class="ctx">Bottling line 1, 750 ml, cases of 12</div></div>'
 '<div class="cd bd" id="bd"></div><div class="cd po2" id="po2"></div><div class="cd ck2" id="ck2"></div></div>'
)

JS = r'''
var FOC='.hd>*,.top .fld,.top .ctx,#opb,.bd .ct,.bd .pg,.bd>.empt,.bd .tot,.po2 .ct,.po2>*:not(.ct),.ck2 .ct,.ck2>*:not(.ct)';
var CASES=1200,PER=12,BOT={d:'Mar 14',n:314},PAL=700;
var DG=[{k:'gl',nm:'Glass',sub:'750 ml Bordeaux',oh:9000,ord:[{po:'PO-2188',q:6000,d:'Mar 28',n:328}]},
{k:'ck',nm:'Corks',sub:'Natural, 44 mm',oh:12000,ord:[{po:'PO-2191',q:4000,d:'Feb 20',n:220}]},
{k:'cp',nm:'Capsules',sub:'Tin, burgundy',oh:14400,ord:[]},
{k:'lb',nm:'Labels',sub:'Front and back sets',oh:15000,ord:[]}];
var NEWPO={po:'PO-2207',q:0,d:'Mar 6',n:306,sup:'Ridgeline Glass Co'};
var S;
function need(){return CASES*PER;}
function ords(g){var a=g.ord.slice();if(g.k==='gl'&&S.pl)a.push({po:NEWPO.po,q:pallets()*PAL,d:NEWPO.d,n:NEWPO.n,nw:true});return a;}
function counts(o){return o.n<=BOT.n;}
function avail(g){return g.oh+ords(g).filter(counts).reduce(function(a,o){return a+o.q;},0);}
function pos(g){return avail(g)-need();}
function short(){return need()-avail(DG[0]);}
function pallets(){return Math.ceil((need()-DG[0].oh)/PAL);}
function row(g){var p=pos(g),sh=S.sh&&p<0,ok=S.pl&&g.k==='gl';
var bf=ords(g).filter(counts),af=ords(g).filter(function(o){return !counts(o);});
function chip(o){var lt=S.sh&&!counts(o);return '<span class="ar'+(lt?' lt':'')+(o.nw?' nw':'')+'" id="a-'+o.po+'"><span>'+o.d+(lt?', late':'')+'</span><b>+'+n0(o.q)+'</b></span>';}
var st='';
if(S.ck){if(sh)st='<span class="ch c-bad" id="f-'+g.k+'">Short</span><b id="p-'+g.k+'">'+n0(-p)+' short</b>';
else if(ok)st='<span class="ch c-ok" id="f-'+g.k+'">Clear</span><b id="p-'+g.k+'">'+n0(p)+' over</b>';
else st=(S.sh?'<span class="ch c-ok" id="f-'+g.k+'">No flag</span>':'')+'<b id="p-'+g.k+'">'+(p<0?n0(-p)+' short':p===0?'Exact':n0(p)+' over')+'</b>';}
var po=(g.k==='gl'&&S.sh&&!S.pl)?'<span class="po">'+(S.po?'<span class="ch c-warn">PO drafted</span>':'<button type="button" class="bt pri" id="pob">Create PO</button>')+'</span>':'';
return '<div class="pg pr in'+(sh?' sh':'')+(ok?' ok':'')+'" id="r-'+g.k+'"><span><b style="font-weight:600">'+g.nm+'</b><small>'+g.sub+'</small>'+po+'</span><span class="n" id="n-'+g.k+'">'+n0(need())+'</span>'+
'<span class="n" id="o-'+g.k+'">'+(S.ck?n0(g.oh):'')+'</span><span class="ln">'+(S.ck?bf.map(chip).join(''):'')+'</span><span class="dv"></span><span class="ln af">'+(S.ck?af.map(chip).join(''):'')+'</span>'+
'<span class="n" id="v-'+g.k+'">'+(S.ck?n0(avail(g)):'')+'</span><span class="n ps">'+st+'</span></div>';}
function render(){
$('opb').className='bt '+(S.op?'done':'pri');$('opb').textContent=S.op?'Opened':'Open plan';
$('rs').innerHTML=!S.op?'':'<span class="ch c-idle">4 dry goods</span>'+(S.sh?(S.pl?'<span class="ch c-ok" id="pst">Plan clear</span>':'<span class="ch c-bad" id="pst">1 short</span>'):'');
var b='<div class="ct"><span>Dry goods for Mar 14'+(S.op?', '+n0(CASES)+' cases × 12 = '+n0(need())+' each':'')+'</span>'+(S.op?'<span class="r3">'+(S.ck?'<button type="button" class="bt '+(S.sh?'done':'pri')+'" id="shb">'+(S.sh?'Checked':'Check for shortages')+'</button>':'<button type="button" class="bt pri" id="ckb">Check stock and arrivals</button>')+'</span>':'')+'</div>';
if(!S.op)b+='<div class="empt"><b>No plan open</b><span>Open a bottling plan to set every dry good against the bottling date.</span></div>';
else{b+='<div class="pg h"><span>Dry good</span><span>Need</span><span>On hand</span><span>Arrives by Mar 14</span><span></span><span>Arrives after Mar 14</span><span>Counts</span><span>Position</span></div>'+DG.map(row).join('')+
'<div class="tot">Only orders arriving by the bottling date count. Bottling line 1, Mar 14.</div>';}
$('bd').innerHTML=b;
var p='<div class="ct"><span>Supplier order</span>'+(S.po?'<span class="r3"><span class="ch '+(S.pl?'c-ok':'c-warn')+'" id="pos">'+(S.pl?'Placed':'Draft')+'</span>'+(S.pl?'':'<button type="button" class="bt pri" id="plb">Place order</button>')+'</span>':'')+'</div>';
if(!S.po)p+='<div class="empt"><b>No order yet</b><span>Raise a purchase order straight from a line on the plan.</span></div>';
else{p+='<div class="ph in"><div class="kv"><small>'+NEWPO.sup+'</small><b>'+NEWPO.po+'</b></div><div class="kv" style="text-align:right"><small>Arrives</small><b style="font-size:10.4px">'+NEWPO.d+'</b></div></div>'+
'<div class="pl in"><div class="row h"><span>Line</span><span>Pallets</span><span>Bottles</span></div><div class="row"><span>Glass, 750 ml Bordeaux</span><span id="ppl">'+pallets()+'</span><span id="pbt">'+n0(pallets()*PAL)+'</span></div></div>'+
'<div class="pals in" aria-hidden="true">'+Array(pallets()+1).join('<i></i>')+'</div>'+
'<div class="calc in" id="pcal">'+n0(short())+' short ÷ 700 a pallet, rounded up = '+pallets()+' pallets</div>';}
p+='<div class="tot">'+(S.po?'Glass comes in pallets of 700 bottles.':'Orders are raised in whole pallets.')+'</div>';
$('po2').innerHTML=p;
var c='<div class="ct"><span>Plan check</span></div>';
if(!S.ck)c+='<div class="empt"><b>Not checked</b><span>Each dry good is checked against the need by the bottling date.</span></div>';
else{if(S.pl)c+='<div class="big2 g in" id="cnt"><span>Glass '+n0(avail(DG[0]))+' against '+n0(need())+'</span><span>'+n0(pos(DG[0]))+' over</span></div>';
else if(S.sh)c+='<div class="big2 w in" id="cnt"><span>Glass counts '+n0(avail(DG[0]))+'</span><span>'+n0(short())+' short</span></div>';
else c+='<div class="big2 i in"><span>Shortages</span><span>Not checked</span></div>';c+='<div class="cl2 in">'+DG.map(function(g){var p=pos(g),bad=S.sh&&p<0;return '<div><span>'+g.nm+'</span><span>'+(p<0?'−'+n0(-p):'+'+n0(p))+'</span><span><span class="ch '+(!S.sh?'c-idle':bad?'c-bad':'c-ok')+'">'+(!S.sh?'Open':bad?'Short':S.pl&&g.k==='gl'?'Clear':'No flag')+'</span></span></div>';}).join('')+'</div>';
}

$('ck2').innerHTML=c;
}
function resetState(){S={op:false,ck:false,sh:false,po:false,pl:false};render();}
var ST=[
{id:'op',target:function(){return $('opb');},prompt:'Open the Mar 14 bottling plan',where:'below',run:function(){S.op=true;render();},
 after:function(){return['A bottling plan for a date',n0(CASES)+' cases × 12 = '+n0(need())+' each of glass, corks, capsules and labels.'];}},
{id:'ck',target:function(){return $('ckb');},prompt:'Check stock and arrival dates',where:'below',run:function(){S.ck=true;render();},
 after:function(){return['Stock, orders and arrival dates','Each dry good shows stock on hand and open orders before or after Mar 14.'];}},
{id:'sh',target:function(){return $('shb');},prompt:'Check for shortages',where:'below',run:function(){S.sh=true;render();},
 after:function(){return['The item marked short','Glass: '+n0(DG[0].oh)+' on hand, the 6,000 due Mar 28 arrive late, so '+n0(short())+' short.'];}},
{id:'po',target:function(){return $('pob');},prompt:'Create a PO for the glass',where:'right',run:function(){S.po=true;render();},
 after:function(){return['A supplier order from the short line',NEWPO.po+': '+pallets()+' pallets of 700 = '+n0(pallets()*PAL)+' bottles, arriving '+NEWPO.d+'.'];}},
{id:'pl',target:function(){return $('plb');},prompt:'Place the order',where:'above',run:function(){S.pl=true;render();},
 after:function(){return['The plan clears once ordered','Glass now counts '+n0(avail(DG[0]))+' against '+n0(need())+', '+n0(pos(DG[0]))+' over. Corks, capsules and labels have no flag.'];}}];
'''
