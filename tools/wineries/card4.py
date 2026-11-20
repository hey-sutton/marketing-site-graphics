"""Wineries card 4: Allocation Across Channels. Layout: a stage chain (order stages with running counts).
Top: the read only release field with Open release. Then the release counts: bottled, promised and free cases with a
stacked bar and the check that bottled equals promised plus free. Middle: the order stage chain, Open, Picking, Packed,
Shipped, with every order card in its stage. Bottom left: the two orders to place, each with its preset case chip.
Bottom right: the count log, one line per change, each with the bottled check.
Promised counts every order not yet cancelled, shipped or not, so moving an order along the chain never changes the
counts."""
from frame_auto import header

SUMMARY = 'Allocation Across Channels (Cellar Select Syrah, 300 cases bottled, 120 promised to restaurants, 180 free; a distributor order of 100 leaves 80 free, a club order of 60 leaves 20; bottled always equals promised plus free; the distributor order moves open, picking, packed, shipped)'
ARIA = 'Interactive product screen: open a limited release, read bottled, promised and free cases, place a distributor order and a club order and watch free cases drop, then move an order through picking and packing to shipped'
STEPS = 5
STUDIO = dict(lede='A typical allocation screen on your Sutton data. Want it different? Describe the change.',
              examples=['Allocations by state', 'A hold for library wine', 'Club members by tier', 'A text when free cases run low'],
              built_on='Items, lots, sales orders and shipments', change='Channels, stages and views')

ICON = '<path d="M2 4.5h12M2 8h8M2 11.5h5"/><circle cx="12.5" cy="11" r="2"/>'

CSS = (
 '.fld input[readonly]{background:#F4F4F5;color:#3F3F46;cursor:default;pointer-events:none}'
 '.g4{display:grid;grid-template-columns:322px 324px;grid-template-rows:60px 92px 184px 174px;gap:10px;padding:10px 44px 0 16px;width:716px}'
 '.top{grid-column:1/3;display:flex;flex-direction:column;justify-content:center;gap:5px;padding:0 12px}.top .frm{display:flex;align-items:flex-end;gap:8px}.top .fld{width:210px}.top .ctx{font-size:8.9px;color:#71717A}.top .rs{margin-left:auto;display:flex;gap:6px}'
 '.cn,.chw{grid-column:1/3;display:flex;flex-direction:column}.cn>.empt,.chw>.empt,.of>.empt,.lg2>.empt{margin:8px;flex:1;padding:6px}.ct .bt{font-size:9px;padding:2px 9px}'
 '.cw{display:grid;grid-template-columns:96px 14px 96px 14px 96px 1fr;align-items:center;gap:6px;padding:7px 11px}.cw .op{text-align:center;color:#A1A1AA;font-family:"JetBrains Mono",ui-monospace,monospace;font-size:12px}'
 '.tl{border:1px solid #E4E4E7;border-radius:8px;padding:5px 9px}.tl small{display:block;font-size:8.3px;color:#71717A}.tl b{font-family:"JetBrains Mono",ui-monospace,monospace;font-size:19px;letter-spacing:-.02em;transition:color .35s}.tl.p{border-color:#FDE68A;background:#FFFBEB}.tl.f{border-color:#BBF7D0;background:#F0FDF4}'
 '.sbx{display:flex;flex-direction:column;gap:4px;padding-left:6px}.sbx .br{display:flex;height:14px;border-radius:4px;overflow:hidden;background:#F4F4F5}.sbx .br i{height:100%;transition:width .5s cubic-bezier(.22,.9,.28,1)}.sbx .br .r{background:#D97706}.sbx .br .d{background:#1E3A8A}.sbx .br .c{background:#7F1D1D}.sbx .br .fr{background:#86EFAC}'
 '.sbx .lb{display:flex;gap:9px;font-size:8.2px;color:#52525B;white-space:nowrap}.sbx .lb span{display:inline-flex;align-items:center;gap:4px}.sbx .lb i{width:8px;height:8px;border-radius:2px}.sbx .eq{font-family:"JetBrains Mono",ui-monospace,monospace;font-size:9px;color:#166534}'
 '.chn{display:grid;grid-template-columns:1fr 12px 1fr 12px 1fr 12px 1fr;padding:7px 9px;flex:1;min-height:0}.arw{display:grid;place-items:center;color:#A1A1AA}.arw svg{width:9px;height:9px}'
 '.sc{border:1px solid #E4E4E7;border-radius:8px;background:#FAFAFA;display:flex;flex-direction:column;gap:4px;padding:5px;min-width:0}.sc .sh{display:flex;justify-content:space-between;align-items:center;font-size:9.2px;font-weight:600;padding:0 2px}.sc .sh .mono{font-weight:500;color:#71717A;font-size:8.6px}'
 '.sc.s4{background:#F0FDF4;border-color:#BBF7D0}'
 '.oc{border:1px solid #E4E4E7;border-radius:6px;background:#fff;padding:3px 6px;display:flex;flex-direction:column;gap:1px;font-size:8.4px;transition:border-color .35s,box-shadow .35s}.oc .t1{display:flex;justify-content:space-between;align-items:center}.oc b{font-family:"JetBrains Mono",ui-monospace,monospace;font-size:8.8px}.oc small{color:#71717A;font-size:8px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;text-align:left}.oc .trl{white-space:normal;color:#166534;line-height:1.35}'
 '.oc.r{box-shadow:inset 3px 0 0 #D97706}.oc.d{box-shadow:inset 3px 0 0 #1E3A8A}.oc.c{box-shadow:inset 3px 0 0 #7F1D1D}.oc.nw{border-color:#93C5FD}.oc .bt{font-size:8.4px;padding:2px 6px;margin-top:2px}'
 '.of,.lg2{display:flex;flex-direction:column}'
 '.orw{display:grid;grid-template-columns:1fr auto auto;align-items:center;gap:6px;padding:5px 11px;border-top:1px solid #F0F0F1;font-size:9px}.orw:first-of-type{border-top:0}.orw small{display:block;font-size:8px;color:#71717A}.orw .pc{border:1px solid #18181B;background:#18181B;color:#fff;border-radius:6px;padding:2px 7px;font-family:"JetBrains Mono",ui-monospace,monospace;font-size:8.6px}.orw .bt{font-size:9px;padding:3px 8px}'
 '.lg2 .row{grid-template-columns:1fr 34px 46px 30px 44px;font-size:8.8px;min-height:20px;padding:0 9px}.lg2 .row>span:nth-child(n+2){text-align:right;font-family:"JetBrains Mono",ui-monospace,monospace}.lg2 .row.h>span{font-family:inherit!important}'
 '.tot{margin-top:auto;padding:6px 11px;border-top:1px solid #E4E4E7;font-size:8.9px;color:#52525B;line-height:1.35;background:#FAFAFA}.lg2 .tot{padding-right:90px}'
)

WIN = (
 header(ICON, 'Release allocation', 'Bottled, promised and free cases by channel')
 + '<div class="g4"><div class="cd top"><div class="frm"><label class="fld"><small>Limited release</small>'
 '<input id="irl" value="Cellar Select Syrah, 300 cases" readonly tabindex="-1" autocomplete="off" spellcheck="false"></label>'
 '<button type="button" class="bt pri" id="orb">Open release</button><span class="rs" id="rs"></span></div><div class="ctx">Single vineyard Syrah, vintage 2023, cases of 12</div></div>'
 '<div class="cd cn" id="cn"></div><div class="cd chw" id="chw"></div><div class="cd of" id="of"></div><div class="cd lg2" id="lg2"></div></div>'
)

JS = r'''
var FOC='.hd>*,.top .fld,.top .ctx,#orb,.cn .ct,.cn>*:not(.ct),.chw .ct,.chw .sc,.chw>.empt,.of .ct,.of>*:not(.ct),.lg2 .ct,.lg2>*:not(.ct)';
var BOT=300,STG=['Open','Picking','Packed','Shipped'];
var REST=[{id:'SO-7391',nm:'Alder Street Bistro',q:50,st:2,k:'r'},{id:'SO-7398',nm:'Copper Pot Kitchen',q:40,st:1,k:'r'},{id:'SO-7402',nm:'Marlow Room',q:30,st:0,k:'r'}];
var DIS={id:'SO-7410',nm:'Westvale Distributing',q:100,k:'d'},CLB={id:'CL-1124',nm:'Cellar club, fall release',q:60,k:'c'};
var S;
function orders(){var a=REST.slice();if(S.po)a.push({id:DIS.id,nm:DIS.nm,q:DIS.q,st:S.av?3:0,k:'d',nw:true});if(S.cl)a.push({id:CLB.id,nm:CLB.nm,q:CLB.q,st:0,k:'c',nw:true});return a;}
function promised(){return orders().reduce(function(a,o){return a+o.q;},0);}
function free(){return BOT-promised();}
function by(k){return orders().filter(function(o){return o.k===k;}).reduce(function(a,o){return a+o.q;},0);}
var ARW='<div class="arw" aria-hidden="true"><svg viewBox="0 0 10 10" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"><path d="M2 5h6M5.5 2.5L8 5 5.5 7.5"/></svg></div>';
function card(o){var adv=o.id===DIS.id&&!S.av&&S.cl;
return '<div class="oc in '+o.k+(o.nw?' nw':'')+'" id="o-'+o.id+'"><div class="t1"><b>'+o.id+'</b><b>'+o.q+'</b></div><small>'+o.nm+'</small>'+(adv?'<button type="button" class="bt pri" id="avb">Advance</button>':'')+(o.id===DIS.id&&S.av?'<small class="trl" id="dtr">'+STG.map(function(x){return '\u2713 '+x;}).join(' ')+'</small>':'')+'</div>';}
function render(){
$('orb').className='bt '+(S.op?'done':'pri');$('orb').textContent=S.op?'Opened':'Open release';
$('rs').innerHTML=S.op?'<span class="ch c-idle">Limited release</span>':'';
var c='<div class="ct"><span>Release counts</span>'+(S.op?'<button type="button" class="bt '+(S.ct?'done':'pri')+'" id="ccb">'+(S.ct?'Counted':'Count cases')+'</button>':'')+'</div>';
if(!S.ct)c+='<div class="empt"><b>'+(S.op?'Not counted yet':'No release open')+'</b><span>'+(S.op?'Count bottled, promised and free cases for this release.':'Open a limited release to see what is bottled, promised and free.')+'</span></div>';
else{var P=promised(),F=free();
c+='<div class="cw in"><div class="tl"><small>Bottled</small><b id="cbt">'+BOT+'</b></div><span class="op">=</span><div class="tl p"><small>Promised</small><b id="cpr">'+P+'</b></div><span class="op">+</span><div class="tl f"><small>Free</small><b id="cfr">'+F+'</b></div>'+
'<div class="sbx"><div class="br"><i class="r" style="width:'+(by('r')/BOT*100).toFixed(1)+'%"></i><i class="d" style="width:'+(by('d')/BOT*100).toFixed(1)+'%"></i><i class="c" style="width:'+(by('c')/BOT*100).toFixed(1)+'%"></i><i class="fr" style="width:'+(F/BOT*100).toFixed(1)+'%"></i></div>'+
'<div class="lb"><span><i style="background:#D97706"></i>Restaurants '+by('r')+'</span><span><i style="background:#1E3A8A"></i>Distributor '+by('d')+'</span><span><i style="background:#7F1D1D"></i>Club '+by('c')+'</span></div><span class="eq" id="ceq">'+BOT+' = '+P+' + '+F+'</span></div></div>';}
$('cn').innerHTML=c;
var h='<div class="ct"><span>Order stages</span>'+(S.op?'<span class="ch c-idle">'+orders().length+' orders</span>':'')+'</div>';
if(!S.op)h+='<div class="empt"><b>No orders yet</b><span>Orders on this release move from open to picking, packed and shipped.</span></div>';
else{var O=orders();h+='<div class="chn">'+STG.map(function(s,i){var L=O.filter(function(o){return o.st===i;});return (i?ARW:'')+'<div class="sc'+(i===3?' s4':'')+'" id="st-'+i+'"><div class="sh"><span>'+s+'</span><span class="mono">'+L.reduce(function(a,o){return a+o.q;},0)+'</span></div>'+L.map(card).join('')+'</div>';}).join('')+'</div>';}
$('chw').innerHTML=h;
var f='<div class="ct"><span>New orders</span></div>';
if(!S.op)f+='<div class="empt"><b>Nothing to place</b><span>Distributor and club orders draw on the same free cases.</span></div>';
else{f+='<div class="orw in"><span>Distributor<small>'+DIS.nm+'</small></span><span class="pc">'+DIS.q+' cases</span>'+(S.po?'<span class="ch c-ok">'+DIS.id+'</span>':'<button type="button" class="bt'+(S.ct?' pri':'')+'" id="pob">Place order</button>')+'</div>'+
'<div class="orw in"><span>Club<small>'+CLB.nm+'</small></span><span class="pc">'+CLB.q+' cases</span>'+(S.cl?'<span class="ch c-ok">'+CLB.id+'</span>':'<button type="button" class="bt'+(S.po?' pri':'')+'" id="acb">Add club order</button>')+'</div>';}
f+='<div class="tot">Case quantities come from the order, not typed.</div>';
$('of').innerHTML=f;
var g='<div class="ct"><span>Count log</span></div>';
if(!S.ct)g+='<div class="empt"><b>No counts yet</b><span>Every change to the release is logged with its counts.</span></div>';
else{var rows=[['Release opened',0,120]];if(S.po)rows.push(['Distributor '+DIS.q,DIS.q,220]);if(S.cl)rows.push(['Club '+CLB.q,CLB.q,280]);if(S.av)rows.push([DIS.id+' shipped',0,280]);
g+='<div class="in"><div class="row h"><span>Change</span><span>Cases</span><span>Promised</span><span>Free</span><span>Bottled</span></div>'+rows.map(function(x,i){return '<div class="row" id="lg-'+i+'"><span>'+x[0]+'</span><span>'+(x[1]?'+'+x[1]:'')+'</span><span>'+x[2]+'</span><span>'+(BOT-x[2])+'</span><span>'+BOT+' ✓</span></div>';}).join('')+'</div>';}

$('lg2').innerHTML=g;
}
function resetState(){S={op:false,ct:false,po:false,cl:false,av:false};render();}
var ST=[
{id:'op',target:function(){return $('orb');},prompt:'Open the Syrah release',where:'below',run:function(){S.op=true;render();},
 after:function(){return['A limited release and its orders','Cellar Select Syrah: three restaurant orders already on the stage chain.'];}},
{id:'ct',target:function(){return $('ccb');},prompt:'Count bottled, promised and free',where:'below',run:function(){S.ct=true;render();},
 after:function(){return['Bottled, promised and free cases',BOT+' bottled = '+promised()+' promised to restaurants + '+free()+' free.'];}},
{id:'po',target:function(){return $('pob');},prompt:'Place the distributor order',where:'above',run:function(){S.po=true;render();},
 after:function(){return['A distributor order draws on free cases',DIS.q+' cases to '+DIS.nm+': '+promised()+' promised, '+free()+' free.'];}},
{id:'cl',target:function(){return $('acb');},prompt:'Add the club order',where:'above',run:function(){S.cl=true;render();},
 after:function(){return['A club order and what is left',CLB.q+' cases for the fall release: '+promised()+' promised, '+free()+' free of '+BOT+'.'];}},
{id:'av',target:function(){return $('avb');},prompt:'Advance the distributor order',where:'below',run:function(){S.av=true;render();},
 after:function(){return['An order moved from open to shipped',DIS.id+' went through picking and packing to shipped. Still '+BOT+' = '+promised()+' + '+free()+'.'];}}];
'''
