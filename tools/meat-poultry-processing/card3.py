"""Meat and poultry card 3: Carcass & Primal Planning. Layout: a board (the week's plan grid, one row per cut).
Top: the read only week field with Open orders. Then the three customer orders as cards. Middle: the plan grid, one
row per cut (ribeye, brisket, trim for grinding) with the order kg by ship day, the yield per carcass, the carcasses
needed, the stock on hand and the net need. Bottom left: the working for each cut. Bottom right: the purchase order
for the gap, sized to the largest carcass count, with what those carcasses yield against the net need.
Carcasses are worked back first from the orders, then again net of stock, always rounded up."""
from frame_auto import header

SUMMARY = 'Carcass & Primal Planning (week 47, 3 customer orders need ribeye 252 kg, brisket 266 kg and trim 1,700 kg, yield per carcass 12, 14 and 85 kg, stock 36, 0 and 85 kg, net need 216, 266 and 1,615 kg, carcasses 18, 19 and 19, a purchase order for 19 carcasses with a ribeye surplus of 12 kg)'
ARIA = 'Interactive product screen: open the week of customer orders, see the quantity needed of each cut, work back through each cut yield to a number of carcasses, check stock on hand and raise a purchase order for the gap'
STEPS = 5
STUDIO = dict(lede='A typical cut plan on your Sutton data. Want it different? Describe the change.',
              examples=['Yields by grade and weight', 'Add chuck and short rib', 'Plan two weeks out', 'Split the PO by supplier'],
              built_on='Sales orders, BOMs, stock and purchase orders', change='Cuts, yields and views')

ICON = '<rect x="2" y="2.5" width="12" height="11" rx="1.5"/><path d="M2 6h12M2 9.5h12M6 6v7.5"/>'

CSS = (
 '.fld input[readonly]{background:#F4F4F5;color:#3F3F46;cursor:default;pointer-events:none}'
 '.g4{display:grid;grid-template-columns:300px 346px;grid-template-rows:58px 78px 178px 196px;gap:10px;padding:10px 44px 0 16px;width:716px}'
 '.top{grid-column:1/3;display:flex;flex-direction:column;justify-content:center;gap:5px;padding:0 12px}.top .frm{display:flex;align-items:flex-end;gap:8px}.top .fld{width:196px}.top .ctx{font-size:8.9px;color:#71717A}.top .rs{margin-left:auto;display:flex;gap:6px}'
 '.os{grid-column:1/3;display:grid;grid-template-columns:1fr 1fr 1fr;gap:8px;border:0;background:transparent;overflow:visible}.os>.empt{grid-column:1/4;padding:8px}'
 '.oc{border:1px solid #E4E4E7;border-radius:8px;background:#fff;padding:7px 9px;display:flex;flex-direction:column;gap:3px}.oc .t1{display:flex;justify-content:space-between;align-items:center}.oc .t1 b{font-family:"JetBrains Mono",ui-monospace,monospace;font-size:10px}.oc .nm{font-size:9.6px;font-weight:600}.oc .mt{font-size:8.4px;color:#71717A}.oc .ln{display:flex;gap:4px;flex-wrap:wrap;margin-top:1px}.oc .ln span{font-size:8.2px;border:1px solid #E4E4E7;border-radius:5px;padding:1px 5px;color:#3F3F46;font-family:"JetBrains Mono",ui-monospace,monospace}'
 '.bd{grid-column:1/3;display:flex;flex-direction:column}.bd>.empt{margin:9px;flex:1;padding:8px}.ct .bt{font-size:9px;padding:2px 9px}.ct .r3{display:flex;gap:6px;align-items:center}.ct .bt:disabled{opacity:.45;cursor:not-allowed}'
 '.pg .row{grid-template-columns:108px 40px 40px 40px 58px 50px 70px 52px 62px;font-size:9.3px;min-height:38px;gap:6px}.pg .row.h{min-height:26px;font-size:8.6px}.pg .row>span:nth-child(n+2){text-align:right;font-family:"JetBrains Mono",ui-monospace,monospace}.pg .row.h>span{font-family:inherit!important}'
 '.pg .row b{font-weight:600}.pg .row small{display:block;font-size:8px;color:#71717A;font-family:Inter,system-ui,sans-serif}.pg .row .e{color:#D4D4D8}.pg .row .cc{display:inline-flex;flex-direction:column;align-items:flex-end}.pg .row s{color:#A1A1AA;font-size:8.4px}'
 '.pg .row .mx{background:#18181B;color:#fff;border-radius:5px;padding:1px 6px}.pg .row.sm{background:#FAFAFA;font-weight:600;min-height:30px}.pg .cs{background:#FAFAFA}'
 '.wk,.po{display:flex;flex-direction:column}.wk>.empt,.po>.empt{margin:9px;flex:1;padding:8px}'
 '.wl{padding:7px 11px 0;display:flex;flex-direction:column;gap:5px}.wl div{display:grid;grid-template-columns:62px 1fr;gap:6px;font-size:9px;align-items:center}.wl div span:last-child{font-family:"JetBrains Mono",ui-monospace,monospace;background:#FAFAFA;border:1px solid #F0F0F1;border-radius:6px;padding:3px 7px}'
 '.ph{display:flex;align-items:flex-end;justify-content:space-between;padding:8px 11px 0}.ph .kv b{font-family:"JetBrains Mono",ui-monospace,monospace;font-size:14px}'
 '.pt .row{grid-template-columns:1fr 54px 54px 56px;font-size:9px;min-height:21px}.pt .row>span:nth-child(n+2){text-align:right;font-family:"JetBrains Mono",ui-monospace,monospace}.pt .row.h>span{font-family:inherit!important}.pt{margin:6px 11px 0;border:1px solid #E4E4E7;border-radius:8px;overflow:hidden}.pt .row.g{background:#F0FDF4}'
 '.tot{margin-top:auto;padding:6px 11px;border-top:1px solid #E4E4E7;font-size:8.8px;color:#52525B;line-height:1.4;background:#FAFAFA}.po .tot{padding-right:90px}'
)

WIN = (
 header(ICON, 'Cut plan', 'Orders worked back to carcasses for the week')
 + '<div class="g4"><div class="cd top"><div class="frm"><label class="fld"><small>Week</small>'
 '<input id="iwk" value="Week 47, 3 customer orders" readonly tabindex="-1" autocomplete="off" spellcheck="false"></label>'
 '<button type="button" class="bt pri" id="oob">Open orders</button><span class="rs" id="rs"></span></div><div class="ctx">Beef cutting room, ship days Monday, Wednesday and Friday</div></div>'
 '<div class="cd os" id="os"></div><div class="cd bd" id="bd"></div><div class="cd wk" id="wk"></div><div class="cd po" id="po"></div></div>'
)

JS = r'''
var FOC='.hd>*,.top .fld,.top .ctx,#oob,.os>*,.bd .ct,.bd>*:not(.ct),.wk .ct,.wk>*:not(.ct),.po .ct,.po>*:not(.ct)';
var MI=String.fromCharCode(8722),DV='÷';
var CUTS=[{k:'rb',nm:'Ribeye',sub:'Bone in, 103',y:12,oh:36,d:[84,96,72]},{k:'bk',nm:'Brisket',sub:'Packer, 120',y:14,oh:0,d:[0,140,126]},{k:'tr',nm:'Trim for grinding',sub:'80/20 lean',y:85,oh:85,d:[900,500,300]}];
var ORD=[{id:'SO-9101',cu:'Lakeside Market',dy:'Mon Nov 16',i:0},{id:'SO-9105',cu:'Ridge Foods',dy:'Wed Nov 18',i:1},{id:'SO-9110',cu:'Copper Kettle Grill',dy:'Fri Nov 20',i:2}];
var S;
function need(c){return c.d[0]+c.d[1]+c.d[2];}
function net(c){return Math.max(0,need(c)-c.oh);}
function gross(c){return Math.ceil(need(c)/c.y);}
function car(c){return Math.ceil(net(c)/c.y);}
function maxCar(){return Math.max.apply(null,CUTS.map(car));}
function buy(c){return maxCar()*c.y;}
function render(){
$('oob').className='bt '+(S.op?'done':'pri');$('oob').textContent=S.op?'Opened':'Open orders';
$('rs').innerHTML=S.op?'<span class="ch c-idle">Week 47</span>'+(S.po?'<span class="ch c-ok">PO raised</span>':'<span class="ch c-info">Planning</span>'):'';
var o='';
if(!S.op)o='<div class="empt"><b>No orders open</b><span>Open the week to see its customer orders.</span></div>';
else o=ORD.map(function(x){return '<div class="oc in" id="o-'+x.id+'"><div class="t1"><b>'+x.id+'</b><span class="ch c-idle">'+x.dy+'</span></div><div class="nm">'+x.cu+'</div><div class="ln">'+CUTS.filter(function(c){return c.d[x.i]>0;}).map(function(c){return '<span>'+c.nm.split(' ')[0]+' '+n0(c.d[x.i])+' kg</span>';}).join('')+'</div></div>';}).join('');
$('os').innerHTML=o;
var btn=!S.op?'':!S.ct?'<button type="button" class="bt pri" id="ctb">Show cuts</button>':!S.wb?'<button type="button" class="bt pri" id="wbb">Work back</button>':!S.sk?'<button type="button" class="bt pri" id="skb">Check stock</button>':'<span class="ch c-ok">Net of stock</span>';
var b='<div class="ct"><span>Plan grid, one row per cut</span><span class="r3">'+(S.ct?'<span class="ch c-idle">'+CUTS.length+' cuts</span>':'')+btn+'</span></div>';
if(!S.ct)b+='<div class="empt"><b>No cuts yet</b><span>'+(S.op?'Turn the orders into the kilograms needed of each cut.':'The week’s cuts show here once orders are open.')+'</span></div>';
else{b+='<div class="pg in" id="pg"><div class="row h"><span>Cut</span><span>Mon</span><span>Wed</span><span>Fri</span><span>Order kg</span><span>Yield kg</span><span>Carcasses</span><span>On hand</span><span>Net need</span></div>'+
CUTS.map(function(c){var cc='';if(S.wb)cc=S.sk?'<span class="cc"><s>'+gross(c)+'</s><b id="c-'+c.k+'"'+(S.po&&car(c)===maxCar()?' class="mx"':'')+'>'+car(c)+'</b></span>':'<b id="g-'+c.k+'">'+gross(c)+'</b>';else cc='<span class="e">·</span>';
return '<div class="row in" id="r-'+c.k+'"><span><b>'+c.nm+'</b><small>'+c.sub+'</small></span>'+c.d.map(function(v){return '<span>'+(v?n0(v):'<span class="e">0</span>')+'</span>';}).join('')+
'<span><b id="n-'+c.k+'">'+n0(need(c))+'</b></span><span class="cs">'+(S.wb?'<span id="y-'+c.k+'">'+c.y+'</span>':'<span class="e">·</span>')+'</span><span class="cs">'+cc+'</span>'+
'<span>'+(S.sk?'<span id="h-'+c.k+'">'+n0(c.oh)+'</span>':'<span class="e">·</span>')+'</span><span>'+(S.sk?'<b id="t-'+c.k+'">'+n0(net(c))+'</b>':'<span class="e">·</span>')+'</span></div>';}).join('')+'</div>';}
$('bd').innerHTML=b;
var w='<div class="ct"><span>Working</span>'+(S.sk?'<span class="ch c-idle">Net, rounded up</span>':S.wb?'<span class="ch c-idle">Gross, rounded up</span>':'')+'</div>';
if(!S.wb)w+='<div class="empt"><b>Nothing worked back</b><span>Each cut divides by its yield per carcass.</span></div>';
else w+='<div class="wl in" id="wl">'+CUTS.map(function(c){return '<div><span>'+c.nm.split(' ')[0]+'</span><span id="w-'+c.k+'">'+(S.sk?n0(need(c))+' '+MI+' '+n0(c.oh)+' = '+n0(net(c))+' '+DV+' '+c.y+' = '+car(c):n0(need(c))+' '+DV+' '+c.y+' = '+gross(c))+'</span></div>';}).join('')+'</div>';
w+='<div class="tot">'+(S.sk?'Buy for the largest count: '+maxCar()+' carcasses.':'Carcasses never round down.')+'</div>';
$('wk').innerHTML=w;
var p='<div class="ct"><span>Purchase order</span>'+(S.sk?'<button type="button" class="bt '+(S.po?'done':'pri')+'" id="pob">'+(S.po?'Created':'Create PO')+'</button>':'')+'</div>';
if(!S.po)p+='<div class="empt"><b>No purchase order</b><span>A PO for the carcasses short shows here once stock is checked.</span></div>';
else{p+='<div class="ph in"><div class="kv"><small>PO-5520, Bluestem Cattle Co, delivers Thu Nov 12</small><b id="poq">'+maxCar()+' carcasses</b></div><span class="ch c-info">Sent</span></div>'+
'<div class="pt in" id="pt"><div class="row h"><span>From '+maxCar()+' carcasses</span><span>Yields</span><span>Net need</span><span>Surplus</span></div>'+
CUTS.map(function(c){var sp=buy(c)-net(c);return '<div class="row'+(sp?' g':'')+'"><span>'+c.nm+'</span><span id="b-'+c.k+'">'+n0(buy(c))+'</span><span>'+n0(net(c))+'</span><span id="s-'+c.k+'">'+n0(sp)+'</span></div>';}).join('')+'</div>';}
p+='<div class="tot">Sized to the cut that needs the most carcasses.</div>';
$('po').innerHTML=p;
}
function resetState(){S={op:false,ct:false,wb:false,sk:false,po:false};render();}
var ST=[
{id:'op',target:function(){return $('oob');},prompt:'Open the week’s orders',where:'below',run:function(){S.op=true;render();},
 after:function(){return['The week’s orders','Week 47: 3 customer orders shipping Monday, Wednesday and Friday.'];}},
{id:'ct',target:function(){return $('ctb');},prompt:'Show the cuts needed',where:'below',run:function(){S.ct=true;render();},
 after:function(){return['The quantity needed of each cut',CUTS.map(function(c){return c.nm.toLowerCase()+' '+n0(need(c))+' kg';}).join(', ').replace(/^./,function(x){return x.toUpperCase();})+'.'];}},
{id:'wb',target:function(){return $('wbb');},prompt:'Work back to carcasses',where:'below',run:function(){S.wb=true;render();},
 after:function(){return['Worked back to carcasses','Each cut over its yield per carcass: '+CUTS.map(function(c){return c.y+' kg';}).join(', ')+'. Rounded up.'];}},
{id:'sk',target:function(){return $('skb');},prompt:'Check stock against the plan',where:'below',run:function(){S.sk=true;render();},
 after:function(){return['Stock on hand nets the need down','Net need '+CUTS.map(function(c){return n0(net(c));}).join(', ')+' kg: '+CUTS.map(car).join(', ')+' carcasses.'];}},
{id:'po',target:function(){return $('pob');},prompt:'Create the purchase order',where:'above',run:function(){S.po=true;render();},
 after:function(){return['A purchase order for the gap',maxCar()+' carcasses, the largest count. Ribeye comes to '+n0(buy(CUTS[0]))+' kg, '+n0(buy(CUTS[0])-net(CUTS[0]))+' kg over the net '+n0(net(CUTS[0]))+'.'];}}];
'''
