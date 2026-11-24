"""Beverage distributors card 1: Available stock and peak season planning. Four number tiles above a planning table with
coverage bars, inside the app shell. Start: the planning table of four SKUs (baseline data) and four empty tiles.
Walkthrough: pick Citrus Seltzer 12 pack in the table, the tiles fill (300 in stock, 150 expected, 700 committed, 6.0
days of coverage), open In stock to split it by location (180 + 90 + 30), check the 14 day window (the row's coverage
bar turns amber and the net shortage of 250 cases appears), then draft a supplier order for the gap (250 at $11.40 =
$2,850.00). Money is held in cents and coverage in tenths of a day. Numbers are asserted in numbers_check.py."""
SUMMARY = 'Available stock and peak season planning (a SKU picked from a planning table of four, its stock, expected and committed cases in four tiles, stock split by location, the 14 day window checked and the shortage turned into a drafted supplier order)'
ARIA = 'Interactive product screen: pick Citrus Seltzer 12 pack, split its 300 cases by location, check the 14 day window to find a shortage of 250 cases, then draft a supplier order for the gap'
STEPS = 4
STUDIO = dict(lede='A typical stock and coverage planner, built on your Sutton data with Studio. Want it different? Describe the change.',
              examples=['Change the coverage window', 'Add a supplier lead time', 'Add a depot', 'Set a low stock alert'],
              built_on='Items, stock, orders and supplier orders', change='Windows, locations and alerts')
# storyboard: screen where the target sits, module, target type, position (the variety test reads this)
STORY = [('Planning', 'inv', 'table row', 'center left'), ('Planning', 'inv', 'tile', 'top left'),
         ('Stock by location', 'inv', 'inline button', 'center right'), ('Shortage', 'inv', 'primary button', 'bottom right')]

CSS = (
 '.tl{display:grid;grid-template-columns:repeat(4,1fr);gap:8px}.tile{border:1px solid #E4E4E7;border-radius:8px;padding:8px 10px;display:flex;flex-direction:column;gap:2px;background:#fff;text-align:left;font:inherit;color:#18181B;min-width:0}'
 '.tile small{font-size:8.8px;color:#71717A}.tile b{font-family:var(--mn);font-size:17px;font-weight:600;line-height:1.25}.tile i{font-style:normal;font-size:8.4px;color:#A1A1AA;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}'
 '.tile .sk{display:block;height:12px;width:54%;margin:5px 0 4px;border-radius:4px;background:#EDEDEF}.tile.bad b{color:#B45309}'
 'button.tile{cursor:pointer;transition:border-color .2s,box-shadow .2s}button.tile:hover,button.tile.fakehover,.tile.on{border-color:#18181B;box-shadow:0 0 0 1px #18181B}button.tile:focus-visible{outline:2px solid #18181B;outline-offset:1px}.tile.new b{animation:exin .45s cubic-bezier(.22,.9,.28,1) both}'
 '.pt1 .row{grid-template-columns:1fr 56px 56px 66px 52px 150px;font-size:9.8px;min-height:30px;white-space:nowrap}.pt1 .row>span:nth-child(n+2):nth-child(-n+5){text-align:right;font-family:var(--mn)}.pt1 .row.h>span{font-family:Inter,sans-serif}'
 '.cvb{display:flex;align-items:center;gap:7px}.cvb .bar{position:relative;flex:1;height:8px;border-radius:4px;background:#F4F4F5}.cvb .bar i{position:absolute;left:0;top:0;bottom:0;border-radius:4px;background:#A1A1AA;transition:width .5s ease,background-color .4s}'
 '.cvb .bar u{position:absolute;top:-3px;bottom:-3px;width:0;border-left:1.5px dashed #18181B;opacity:0;transition:opacity .3s}.chk .cvb .bar u{opacity:.55}.cvb b{font-family:var(--mn);font-size:9.6px;font-weight:600;width:30px;text-align:right}'
 '.row.am .cvb .bar i{background:#F59E0B}.row.am .cvb b{color:#B45309}.row.sel{background:#F4F4F5;box-shadow:inset 3px 0 0 #18181B}'
 '.lg{display:flex;align-items:center;gap:6px;font-weight:500;font-size:9px;color:#71717A}.lg u{display:inline-block;width:0;height:10px;border-left:1.5px dashed #18181B;opacity:.55}'
 '.dp{display:grid;grid-template-columns:1fr 210px;gap:10px}.lc .row{grid-template-columns:1fr 1fr 56px;font-size:9.8px;min-height:28px}.lc .row .q,.lc .row.tot span:last-child{text-align:right;font-family:var(--mn)}.lc .ld{font-size:9px;color:#71717A;margin-left:4px}.lc .row.tot{font-weight:600;background:#FAFAFA}'
 '.lb{height:7px;border-radius:4px;background:#F4F4F5;overflow:hidden}.lb i{display:block;height:100%;background:#52525B;border-radius:4px;transition:width .5s ease}'
 '.side{display:flex;flex-direction:column;gap:8px;padding:10px 11px;font-size:9.8px;color:#52525B;line-height:1.45}.side .bt{align-self:flex-start}.side .bt.w{align-self:stretch;text-align:center;height:30px}'
 '.fm{display:flex;align-items:center;gap:7px;padding:10px 11px;font-size:10px;flex-wrap:wrap}.fm b{font-family:var(--mn);font-size:12px}.fm .op{color:#71717A}.fm .res{color:#B45309}'
 '.kg{display:grid;grid-template-columns:repeat(4,1fr);gap:8px 12px;padding:10px 11px}.po .row{grid-template-columns:1fr 70px 64px 84px;font-size:9.8px;min-height:28px;white-space:nowrap}.po .row span:nth-child(n+2){text-align:right;font-family:var(--mn)}.po .row.tot{font-weight:600;background:#FAFAFA}'
 '.op1 .row{grid-template-columns:70px 1fr 1fr 70px 50px;font-size:9.6px;white-space:nowrap}.op1 .row span:nth-child(n+4){text-align:right;font-family:var(--mn)}'
 '.note{border:1px solid #E4E4E7;background:#FAFAFA;border-radius:8px;padding:8px 10px;font-size:9.6px;line-height:1.45;color:#52525B}.cd.new{animation:exin .45s cubic-bezier(.22,.9,.28,1) both}'
 '.shot.ph .tl{grid-template-columns:1fr 1fr;gap:6px}.shot.ph .tile{padding:4px 9px;min-height:38px;gap:0}.shot.ph .tile b{font-size:13px}.shot.ph .tile i{display:none}.shot.ph .tile .sk{height:10px;margin:3px 0}'
 '.shot.ph .pt1 .row{grid-template-columns:1fr 44px 62px;min-height:26px;font-size:10px}.shot.ph .pt1 button.row{min-height:40px}.shot.ph .pt1 .row.h{min-height:20px}'
 '.shot.ph .bt.w{width:100%;min-height:40px;font-size:10.6px}.shot.ph .lc .row{grid-template-columns:1fr 50px;min-height:26px}.shot.ph .lc .row>span:nth-child(2){display:none}'
 '.p2{display:grid;grid-template-columns:1fr 1fr;gap:6px}.p2 .tile b{font-size:12.5px}.tile.xs b{font-family:Inter,sans-serif;font-size:11.5px;line-height:1.6}.shot.ph.nar .xn{display:none}.shot.ph.nar .pt1 .row{min-height:22px}.shot.ph.nar .pt1 button.row{min-height:40px}'
)

WIN = ''

JS = r'''
var FOC='.rail .ni,.bc,.phd>*,.bn .bi,.pg .tile,.pg .ct,.pg .row,.pg .fm,.pg .side,.pg .note,.pg .kg,.pg .bt,.pg .lg';
var W=14,SK=[['CS-12','Citrus Seltzer 12 pack',300,150,700],['HL-24','Harbor Lager 24 pack',1200,400,840],['OJ-24','Orchard Juice 24 pack',480,0,560],['CB-4','Cold Brew RTD 4 pack',900,300,420]];
var LOC=[['Warehouse','Aisles 1 to 12',180],['Cooler','Bins C-01 to C-08',90],['3PL','Eastside overflow',30]];
var PRICE=1140,PO='PO-2214',SUP='Kestrel Springs Beverage';
var S;
function sk(){return SK[0];}
function perDay(x){return x[4]/W;}
function cov10(x){return Math.round(x[2]*10/perDay(x));}
function d1(t){return (t/10).toFixed(1);}
function avl(x){return x[2]+x[3]-x[4];}
function short(){return -avl(sk());}
function tile(id,l,v,sub,o){o=o||{};var t=o.btn?'button':'div';return '<'+t+(o.btn?' type="button"':'')+' class="tile'+(o.cls?' '+o.cls:'')+'" id="'+id+'"><small>'+l+'</small>'+(v===null?'<span class="sk"></span>':'<b id="'+id+'-v">'+v+'</b>')+(sub?'<i>'+sub+'</i>':'')+'</'+t+'>';}
function tiles(P){var x=sk(),on=S.pick,a=S.anim===1?' new':'';
 return '<div class="tl">'+tile('t-st','In stock',on?n0(x[2]):null,on?'Cases, all locations':'Pick a SKU below',{btn:on&&!S.loc,cls:(S.loc&&!S.chk&&!P?'on':'')+a})+tile('t-ex','Expected',on?n0(x[3]):null,on?'On '+(P?'PO':'PO-2190, Nov 20'):'',{cls:a})+
 tile('t-cm','Committed',on?n0(x[4]):null,on?'Next 14 days':'',{cls:a})+tile('t-dc','Days of coverage',on?d1(cov10(x)):null,on?n0(perDay(x))+' cases a day':'',{cls:a+(S.chk?' bad':'')})+'</div>';}
function cbar(x,i){var t=cov10(x),am=S.chk&&i===0;return '<span class="cvb"><span class="bar"><i style="width:'+Math.min(100,t/3)+'%"></i><u style="left:'+(W*10/3)+'%"></u></span><b id="cv-'+i+'">'+d1(t)+'</b></span>';}
function table(P){var h='<div class="cd pt1'+(S.chk?' chk':'')+'">'+(P?'':'<div class="ct">Planning table<span class="lg">'+(S.chk?'<u></u>14 day window':'Days of coverage at today’s pace')+'</span></div>');
 h+=P?'<div class="row h"><span>SKU</span><span style="text-align:right">Days</span><span style="text-align:right">Status</span></div>':'<div class="row h"><span>SKU</span><span>In stock</span><span>Expected</span><span>Committed</span><span>Per day</span><span>Days of coverage</span></div>';
 SK.forEach(function(x,i){var btn=i===0&&!S.pick,cls='row'+(S.pick&&i===0?' sel':'')+(S.chk&&i===0?' am':'');
  var inner=P?'<span>'+x[1]+'</span><span class="mono" style="text-align:right" id="cv-'+i+'">'+d1(cov10(x))+'</span><span style="text-align:right">'+(S.chk&&i===0?'<span class="ch c-warn">Short</span>':(S.pick&&i===0?'<span class="ch c-info">Open</span>':'<span class="ch c-idle">'+(i===0?'Pick':'Planned')+'</span>'))+'</span>'
   :'<span>'+x[1]+'</span><span>'+n0(x[2])+'</span><span>'+n0(x[3])+'</span><span>'+n0(x[4])+'</span><span>'+n0(perDay(x))+'</span>'+cbar(x,i);
  h+=btn?'<button type="button" class="'+cls+'" id="r-'+i+'">'+inner+'</button>':'<div class="'+cls+'"'+(i===0?' id="r-0"':'')+'>'+inner+'</div>';});
 return h+'</div>';}
function locs(P){var x=sk(),h='<div class="cd lc'+(S.anim===2?' new':'')+'">'+(P?'':'<div class="ct">Stock by location<span class="mut" style="font-weight:500">Citrus Seltzer 12 pack</span></div>');
 LOC.forEach(function(l,i){h+='<div class="row"><span>'+l[0]+(P?'':' <small class="ld">'+l[1]+'</small>')+'</span><span><span class="lb"><i style="width:'+Math.round(l[2]*100/x[2])+'%"></i></span></span><span class="q" id="lc-'+i+'">'+n0(l[2])+'</span></div>';});
 return h+'<div class="row tot"><span>Total in stock</span><span></span><span class="q" id="lc-t">'+n0(x[2])+'</span></div></div>';}
function render(){var P=ph(),h='',x=sk(),bc0=['Inventory',['Planning','cb-pl']];
if(S.scr==='plan'){setNav({m:'inv',bc:S.pick?bc0.concat([x[1]]):['Inventory','Planning'],t:'Peak season planning',chip:['c-info','Next 14 days'],scr:'Planning',back:0,pa:'<span class="mut mono" style="font-size:9.6px">As of Nov 16</span>'});
 h=tiles(P)+table(P);
 if(!P)h+='<div class="cd op1"><div class="ct">Open supplier orders<span class="mut" style="font-weight:500">Counted in expected</span></div><div class="row h"><span>PO</span><span>SKU</span><span>Supplier</span><span>Cases</span><span>Due</span></div>'+
  [['PO-2188','Harbor Lager 24 pack','Harbor Brewing',400,'Nov 19'],['PO-2190','Citrus Seltzer 12 pack',SUP,150,'Nov 20'],['PO-2193','Cold Brew RTD 4 pack','Morning Tide Coffee',300,'Nov 24']].map(function(o){return '<div class="row"><span class="mono">'+o[0]+'</span><span>'+o[1]+'</span><span class="mut">'+o[2]+'</span><span>'+n0(o[3])+'</span><span class="mut">'+o[4]+'</span></div>';}).join('')+'</div>'+(S.pick?'':'<div class="cd op1 wk"><div class="ct">Committed by week<span class="mut" style="font-weight:500">All four SKUs</span></div>'+[['Nov 16 to 22','Regular week',1110],['Nov 23 to 29','Thanksgiving week',1410]].map(function(w){return '<div class="row"><span class="mono">'+w[0]+'</span><span>'+w[1]+'</span><span></span><span>'+n0(w[2])+'</span><span class="mut">cases</span></div>';}).join('')+'</div>');}
else if(S.scr==='loc'){setNav({m:'inv',bc:bc0.concat([['Citrus Seltzer 12 pack','cb-cs'],'Locations']),t:'Peak season planning',chip:['c-info','Next 14 days'],scr:'Stock by location',back:1});
 if(P)h='<div class="p2">'+tile('p-st','In stock',n0(x[2]))+tile('p-dc','Days of coverage',d1(cov10(x)))+'</div>'+locs(P)+'<button type="button" class="bt w" id="chk">Check 14 day coverage</button>';
 else h=tiles(P)+'<div class="dp">'+locs(P)+'<div class="cd"><div class="side"><span>Coverage counts what is on hand today against 14 days of committed orders. Expected cases arrive Nov 20.</span><button type="button" class="bt" id="chk">Check 14 day coverage</button></div></div></div>'+table(P);}
else if(S.scr==='short'){setNav({m:'inv',bc:bc0.concat([['Citrus Seltzer 12 pack','cb-cs'],'Shortage']),t:'Peak season planning',chip:['c-warn','1 short'],scr:'Shortage',back:1});
 if(P)h='<div class="p2">'+tile('s-av','Net shortage',n0(short()),'',{cls:'bad'})+tile('s-dc','Days of coverage',d1(cov10(x)),'',{cls:'bad'})+tile('s-pd','Per day',n0(perDay(x)))+tile('s-w','Window','14 days')+'</div><button type="button" class="bt pri w" id="dr">Draft supplier order</button>';
 else h=tiles(P)+'<div class="dp"><div class="cd new"><div class="ct">Net shortage, next 14 days<span class="ch c-warn">'+n0(short())+' cases short</span></div><div class="fm"><span>In stock</span><b>'+n0(x[2])+'</b><span class="op">plus expected</span><b>'+n0(x[3])+'</b><span class="op">less committed</span><b>'+n0(x[4])+'</b><span class="op">is</span><b class="res" id="s-av">'+n0(short())+' short</b></div><div class="fm" style="border-top:1px solid #F0F0F1"><span>'+n0(perDay(x))+' cases a day covers</span><b class="res" id="s-dc">'+d1(cov10(x))+'</b><span class="op">of 14 days</span></div></div>'+
  '<div class="cd"><div class="side"><span>Order the gap from '+SUP+'. Lead time 5 days, $11.40 a case.</span><button type="button" class="bt pri w" id="dr">Draft supplier order</button></div></div></div>'+table(P);}
else{var amt=short()*PRICE;setNav({m:'pur',bc:['Purchasing',['Supplier orders','cb-po'],PO],t:PO,chip:['c-idle','Draft'],scr:'Supplier order',back:1});
 if(P)h='<div class="p2">'+tile('o-sp','Supplier','Kestrel Springs','',{cls:'xs'})+tile('o-q','Cases',n0(short()))+tile('o-p','Price','$11.40')+tile('o-t','Total',m2(amt/100))+'</div>';
 else{h='<div class="cd new"><div class="kg">'+[['Supplier',SUP],['For','Citrus Seltzer 12 pack'],['Arrives','Nov 21'],['Reason','Shortage, 14 day window']].map(function(k){return '<div class="kv"><small>'+k[0]+'</small><b>'+k[1]+'</b></div>';}).join('')+'</div></div>';
  h+='<div class="cd po"><div class="ct">Lines<span class="mut" style="font-weight:500">Drafted from the shortage</span></div><div class="row h"><span>Item</span><span>Cases</span><span>Price</span><span>Amount</span></div><div class="row"><span>Citrus Seltzer 12 pack</span><span id="o-q">'+n0(short())+'</span><span>$11.40</span><span>'+m2(amt/100)+'</span></div><div class="row tot"><span>Total</span><span></span><span></span><span id="o-t">'+m2(amt/100)+'</span></div></div>';
  h+='<div class="tl">'+tile('a-st','In stock',n0(x[2]))+tile('a-ex','Expected after this PO',n0(x[3]+short()),'150 plus 250')+tile('a-cm','Committed',n0(x[4]))+tile('a-av','Short after this PO','0','Covered for 14 days')+'</div>';
  h+='<div class="cd op1"><div class="ct">Recent orders to '+SUP+'<span class="mut" style="font-weight:500">Lead time 5 days</span></div>'+[['PO-2190','Citrus Seltzer 12 pack','Open, due Nov 20',150,'Nov 15'],['PO-2141','Citrus Seltzer 12 pack','Received on time',400,'Oct 28'],['PO-2117','Citrus Seltzer 12 pack','Received on time',350,'Oct 9']].map(function(o){return '<div class="row"><span class="mono">'+o[0]+'</span><span>'+o[1]+'</span><span class="mut">'+o[2]+'</span><span>'+n0(o[3])+'</span><span class="mut">'+o[4]+'</span></div>';}).join('')+'</div>';
  h+='<div class="note">With '+PO+' the next 14 days are covered: 300 in stock plus 400 expected meets the 700 committed. Send it to '+SUP+' to confirm the Nov 21 arrival.</div>';}}
if(P&&S.scr==='short')h+='<div class="cd lc xn"><div class="row"><span>Expected on PO-2190</span><span></span><span class="q">150</span></div><div class="row"><span>Supplier lead time</span><span></span><span class="q">5 days</span></div></div>';
if(P&&S.scr==='po')h+='<div class="cd lc"><div class="row"><span>Citrus Seltzer 12 pack</span><span></span><span class="q">250</span></div><div class="row"><span>Short after this PO</span><span></span><span class="q">0</span></div></div>';
if(P)h+=xw(S.scr==='plan'?(S.pick?[['Expected','PO-2190, Nov 20'],['Supplier',SUP],['Window','Nov 16 to Nov 30']]:[['Window','Nov 16 to Nov 30'],['SKUs','4 planned'],['Open supplier orders','3']]):S.scr==='loc'?[['Expected','150, Nov 20'],['Committed','700 in 14 days'],['Cooler bins','C-01 to C-08']]:S.scr==='short'?[['In stock plus expected','450'],['Committed','700'],['Supplier',SUP]]:[['Supplier',SUP],['Arrives','Nov 21'],['Status','Draft']],S.scr==='plan'||S.scr==='loc');
$('pg').innerHTML=h;S.anim=0;}
function resetState(){S={scr:'plan',pick:false,loc:false,chk:false,anim:0};render();}
var CAPAT=function(hh){return ph()?{l:8,t:5}:{l:14,t:visH()-hh-40};};
var ST=[
{id:'pick',target:function(){return $('r-0');},prompt:'Pick Citrus Seltzer 12 pack',where:'below',run:function(){S.pick=true;S.anim=1;render();},
 after:['Four numbers for the SKU you picked','Citrus Seltzer 12 pack: 300 in stock, 150 expected, 700 committed over 14 days. At 50 cases a day that is 6.0 days of coverage.'],pc:'300 in stock, 6.0 days of coverage'},
{id:'loc',target:function(){return $('t-st');},prompt:'Open In stock',where:'below',run:function(){S.loc=true;S.scr='loc';S.anim=2;render();},
 after:['Stock split by location','Warehouse 180, cooler 90 and 30 at the 3PL: 300 cases in all.'],pc:'Warehouse 180, cooler 90, 3PL 30'},
{id:'chk',target:function(){return $('chk');},prompt:'Check the 14 day window',where:function(){return ph()?'above':'below';},run:function(){S.chk=true;S.scr='short';render();},
 after:['The row turns amber and the shortage shows','300 in stock plus 150 expected, less 700 committed: 250 cases short. 6.0 days of coverage against a 14 day window.'],pc:'250 cases short in 14 days'},
{id:'po',target:function(){return $('dr');},prompt:'Draft a supplier order for the gap',where:function(){return ph()?'above':'below';},run:function(){S.scr='po';render();},
 after:['A supplier order for the gap','PO-2214 to Kestrel Springs Beverage: 250 cases at $11.40, $2,850.00, arriving Nov 21.'],pc:'250 cases at $11.40: $2,850.00'}];
ST.forEach(function(s){['prompt','where'].forEach(function(k){if(typeof s[k]==='function'){var f=s[k];Object.defineProperty(s,k,{get:f});}});});
'''
