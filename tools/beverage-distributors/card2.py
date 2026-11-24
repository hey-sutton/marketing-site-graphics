"""Beverage distributors card 2: Lot dates and oldest first picking. Horizontal bars of days left per lot with a 30 day
threshold line, inside the app shell. Start: the SKU list only, no lots or bars. Walkthrough: open Harbor Lager 24 pack
(three lots draw as bars of days left as of Nov 16: A 28, B 70, C 112 days, 180 + 420 + 600 = 1,200 cases), start the
pick for order SO-5126 (prefilled, read only: Northgate Grocers, 500 cases), which takes the oldest lots first (180
from A, then 320 from B), check lot A against the threshold (28 days, under 30, 180 cases at risk for a retailer that
needs 30 days on arrival), then offer lot A to Dockside Taproom, which takes 14 days: lot A drops to 0 and the
Northgate pick moves to lots B and C (420 + 80 = 500). Numbers are asserted in numbers_check.py."""
SUMMARY = 'Lot dates and oldest first picking (a SKU opened to bars of days left per lot against a 30 day threshold, a 500 case pick taken oldest first, the near date lot flagged and offered to an account that takes short dates)'
ARIA = 'Interactive product screen: open Harbor Lager 24 pack to see three lots by days left, pick 500 cases oldest first, flag the lot under the 30 day threshold, then offer its 180 cases to Dockside Taproom'
STEPS = 4
STUDIO = dict(lede='A typical lot and best by date view, built on your Sutton data with Studio. Want it different? Describe the change.',
              examples=['Change the near date threshold', 'Add a retailer shelf life rule', 'Add a lot attribute', 'Group lots by supplier'],
              built_on='Items, lots, best by dates and orders', change='Thresholds, rules and fields')
STORY = [('SKU list', 'inv', 'table row', 'center left'), ('Lots', 'inv', 'inline button', 'top right'),
         ('Pick', 'inv', 'lot bar', 'center'), ('At risk', 'inv', 'primary button', 'bottom right')]

CSS = (
 '.sl .row{grid-template-columns:1fr 70px 50px 110px 90px;font-size:9.8px;min-height:32px;white-space:nowrap}.sl .row>span:nth-child(n+2){text-align:right}.sl .row .mono{font-weight:500}'
 '.rl .row{grid-template-columns:1fr 1fr 80px;font-size:9.6px;white-space:nowrap}.rl .row span:last-child{text-align:right;font-family:var(--mn)}'
 '.lots{padding:8px 11px 10px;display:flex;flex-direction:column;gap:0;position:relative}'
 '.lr{display:grid;grid-template-columns:150px 1fr 76px;align-items:center;gap:10px;min-height:38px;border:0;background:#fff;width:100%;text-align:left;font:inherit;color:#18181B;padding:0 4px;border-radius:6px;transition:background-color .2s,box-shadow .2s}'
 'button.lr{cursor:pointer}button.lr:hover,button.lr.fakehover{background:#FAFAFA;box-shadow:0 0 0 1px #E4E4E7}button.lr:focus-visible{outline:2px solid #18181B;outline-offset:1px}'
 '.lr .id{display:flex;flex-direction:column;line-height:1.3}.lr .id b{font-family:var(--mn);font-size:10.2px;font-weight:600}.lr .id small{font-size:8.8px;color:#71717A}'
 '.lr .tr{position:relative;height:16px;border-radius:5px;background:#F4F4F5}.lr .tr i{position:absolute;left:0;top:0;bottom:0;border-radius:5px;background:#A1A1AA;transition:width .7s cubic-bezier(.22,.9,.28,1),background-color .4s}'
 '.lr .tr em{position:absolute;top:0;line-height:16px;font-style:normal;font-family:var(--mn);font-size:9px;color:#52525B;white-space:nowrap}.lr.risk .tr em{color:#B45309;font-weight:600}'
 '.lr .tr .pk{position:absolute;top:0;bottom:0;left:0;border-radius:5px;background:repeating-linear-gradient(135deg,rgba(24,24,27,.35) 0 3px,transparent 3px 6px);transition:width .5s}'
 '.lr .cs{text-align:right;font-family:var(--mn);font-size:10px;line-height:1.3}.lr .cs small{display:block;font-size:8.6px;color:#71717A;font-family:Inter,sans-serif}'
 '.lr.risk .tr i{background:#F59E0B}.lr.risk .id b{color:#B45309}.lr.gone .tr i{background:#D4D4D8}.lr.sel{background:#FFFBEB;box-shadow:0 0 0 1px #FDE68A}'
 '.thr{position:absolute;top:4px;bottom:6px;border-left:1.5px dashed #B45309;pointer-events:none}.thr span{position:absolute;top:-1px;left:4px;font-size:8.4px;color:#B45309;white-space:nowrap;background:#fff;padding:0 2px}'
 '.ax{display:grid;grid-template-columns:150px 1fr 76px;gap:10px;padding:0 4px;font-size:8.4px;color:#A1A1AA;font-family:var(--mn)}.ax div{display:flex;justify-content:space-between}'
 '.pl .row{grid-template-columns:110px 1fr 70px 70px;font-size:9.8px;min-height:28px;white-space:nowrap}.pl .row span:nth-child(n+3){text-align:right;font-family:var(--mn)}.pl .row.tot{font-weight:600;background:#FAFAFA}'
 '.dp{display:grid;grid-template-columns:1fr 220px;gap:10px}.side{display:flex;flex-direction:column;gap:8px;padding:10px 11px;font-size:9.8px;color:#52525B;line-height:1.45}.side .bt.w{text-align:center;height:30px}'
 '.flag{display:flex;flex-direction:column;gap:6px;padding:10px 11px;font-size:9.8px;line-height:1.45;color:#52525B}.flag b{color:#18181B}'
 '.kg{display:grid;grid-template-columns:repeat(4,1fr);gap:8px 12px;padding:10px 11px}.cd.new{animation:exin .45s cubic-bezier(.22,.9,.28,1) both}'
 '.note{border:1px solid #E4E4E7;background:#FAFAFA;border-radius:8px;padding:8px 10px;font-size:9.6px;line-height:1.45;color:#52525B}'
 '.tl{display:grid;grid-template-columns:1fr 1fr;gap:6px}.tile{border:1px solid #E4E4E7;border-radius:8px;padding:4px 9px;display:flex;flex-direction:column;background:#fff;min-height:38px}.tile small{font-size:8.8px;color:#71717A}.tile b{font-family:var(--mn);font-size:13px;font-weight:600}.tile.bad b{color:#B45309}'
 '.shot.ph .sl .row{grid-template-columns:1fr 54px 40px;min-height:26px;font-size:10px}.shot.ph .sl .row>span:nth-child(n+4){display:none}.shot.ph .sl button.row{min-height:40px}'
 '.shot.ph .lots{padding:4px 8px 6px}.shot.ph .lr{grid-template-columns:76px 1fr 44px;gap:6px;min-height:34px;padding:0 2px}.shot.ph button.lr{min-height:40px}.shot.ph .lr .id small{display:none}.shot.ph .lr .cs small{display:none}.shot.ph .lr .tr em{display:none}.shot.ph .lr.risk .cs{color:#B45309;font-weight:600}'
 '.shot.ph .thr span{display:none}.shot.ph .pl .row{grid-template-columns:1fr 60px;min-height:26px;font-size:10px}.shot.ph .pl .row>span:nth-child(2),.shot.ph .pl .row>span:nth-child(3){display:none}'
 '.shot.ph .bt.w{width:100%;min-height:40px;font-size:10.6px}.shot.ph.nar .xn{display:none}'
)

WIN = ''

JS = r'''
var FOC='.rail .ni,.bc,.phd>*,.bn .bi,.pg .ct,.pg .row,.pg .lr,.pg .ax,.pg .rof,.pg .side,.pg .flag,.pg .note,.pg .kg,.pg .tile,.pg .bt';
var MAXD=120,THR=30,ORD=500,SO='SO-5126',ACC='Northgate Grocers',ALT='Dockside Taproom',OFR='SO-5127';
var LOTS=[['HL-2611-A','Dec 14',28,180],['HL-2611-B','Jan 25',70,420],['HL-2611-C','Mar 8',112,600]];
var SKUS=[['HL-24','Harbor Lager 24 pack',1200,3,'Dec 14'],['CS-12','Citrus Seltzer 12 pack',300,2,'Jan 9'],['OJ-24','Orchard Juice 24 pack',480,2,'Dec 30'],['CB-4','Cold Brew RTD 4 pack',900,3,'Feb 2']];
var RULES=[[ACC,'Retail, grocery',30],['Greenline Market','Retail, grocery',30],[ALT,'On premise, taproom',14],['Pier 9 Bar','On premise, bar',14]];
var S;
function pick(){var left=ORD,out=[];LOTS.forEach(function(l,i){if(S.off&&i===0)return;var t=Math.min(l[3],left);if(t>0)out.push([i,t]);left-=t;});return out;}
function picked(i){var t=0;pick().forEach(function(p){if(p[0]===i)t=p[1];});return S.pick?t:0;}
function left(i){if(S.off&&i===0)return 0;return LOTS[i][3]-(S.off?picked(i):0);}
function total(){var t=0;LOTS.forEach(function(l,i){t+=left(i);});return t;}
function lotRow(l,i,P){var risk=S.flag&&i===0&&!S.off,btn=S.pick&&!S.flag&&i===0,w=Math.round(l[2]*100/MAXD),cls='lr'+(risk?' risk sel':'')+(S.off&&i===0?' gone':'');
 var pk=picked(i)&&!S.off?'<span class="pk" style="width:'+Math.round(picked(i)/l[3]*w)+'%"></span>':'';
 var inner='<span class="id"><b>'+l[0]+'</b><small>Best by '+l[1]+'</small></span><span class="tr"><i style="width:'+(S.anim===1?0:w)+'%" data-w="'+w+'"></i>'+pk+'<em style="left:calc('+w+'% + 6px)">'+l[2]+' days</em></span><span class="cs">'+(P?'<span id="ld-'+i+'">'+l[2]+' days</span>':'<span id="lq-'+i+'">'+n0(left(i))+'</span>')+(P?'':'<small>'+(S.off&&i===0?'offered':(S.pick&&picked(i)?n0(picked(i))+' picked':'cases'))+'</small>')+'</span>';
 return btn?'<button type="button" class="'+cls+'" id="lot-'+i+'">'+inner+'</button>':'<div class="'+cls+'" id="lot-'+i+'">'+inner+'</div>';}
function lots(P){var h='<div class="cd">'+(P?'':'<div class="ct">Days left by lot<span class="mut" style="font-weight:500">As of Nov 16, oldest first</span></div>')+'<div class="lots"><div class="thr" style="left:calc('+(P?'92px':'175px')+' + (100% - '+(P?'152px':'276px')+') * '+(THR/MAXD)+')"><span>30 day threshold</span></div>';
 LOTS.forEach(function(l,i){h+=lotRow(l,i,P);});
 if(!P)h+='<div class="ax"><span></span><div><span>0</span><span>30</span><span>60</span><span>90</span><span>120 days</span></div><span></span></div>';
 return h+'</div></div>';}
function field(P){return rof({l:'Order to pick',id:'io',v:SO+', '+ORD+' cases',b:S.pick?'Pick started':'Start pick',bid:'sp',cx:P?'':ACC+', ships Nov 18'});}
function pl(P){var h='<div class="cd pl'+(S.anim===2?' new':'')+'">'+(P?'':'<div class="ct">Pick list '+SO+'<span class="mut" style="font-weight:500">'+(S.off?'Moved off lot A':'Oldest first')+'</span></div><div class="row h"><span>Lot</span><span>Bin</span><span>Best by</span><span>Cases</span></div>');
 pick().forEach(function(p){var l=LOTS[p[0]];h+='<div class="row"><span class="mono">'+l[0]+'</span><span class="mut">'+['A-02-1','A-04-3','B-11-2'][p[0]]+'</span><span>'+l[1]+'</span><span id="pk-'+p[0]+'">'+n0(p[1])+'</span></div>';});
 return h+'<div class="row tot"><span>Total</span><span></span><span></span><span id="pk-t">'+n0(ORD)+'</span></div></div>';}
function rules(){return '<div class="cd rl"><div class="ct">Shelf life rules by account<span class="mut" style="font-weight:500">Days left on arrival</span></div>'+RULES.map(function(r){return '<div class="row"><span>'+r[0]+'</span><span class="mut">'+r[1]+'</span><span>'+r[2]+' days</span></div>';}).join('')+'</div>';}
function recent(){return '<div class="cd rl"><div class="ct">Recent picks<span class="mut" style="font-weight:500">Oldest lot first</span></div>'+[['SO-5119, Greenline Market','HL-2610-C, best by Dec 2','240 cases'],['SO-5114, Pier 9 Bar','HL-2610-B, best by Nov 24','40 cases'],['SO-5109, Northgate Grocers','HL-2610-C, best by Dec 2','360 cases']].map(function(r){return '<div class="row"><span>'+r[0]+'</span><span class="mut mono">'+r[1]+'</span><span>'+r[2]+'</span></div>';}).join('')+'</div>';}
function tile(id,l,v,c){return '<div class="tile'+(c?' '+c:'')+'"><small>'+l+'</small><b id="'+id+'">'+v+'</b></div>';}
function render(){var P=ph(),h='',bc0=['Inventory',['Lots','cb-lt']];
if(S.scr==='list'){setNav({m:'inv',bc:['Inventory','Lots'],t:'Lots and best by dates',scr:'SKU list',pa:'<span class="mut mono" style="font-size:9.6px">As of Nov 16</span>'});
 h='<div class="cd sl">'+(P?'':'<div class="ct">Lot tracked SKUs<span class="mut" style="font-weight:500">Picked oldest first</span></div>')+'<div class="row h"><span>SKU</span><span>In stock</span><span>Lots</span><span>Nearest best by</span><span>Supplier</span></div>'+
 SKUS.map(function(x,i){var inner='<span>'+x[1]+'</span><span class="mono">'+n0(x[2])+'</span><span class="mono">'+x[3]+'</span><span class="mono">'+x[4]+'</span><span class="mut">'+['Harbor Brewing','Kestrel Springs','Hollow Creek','Morning Tide'][i]+'</span>';return i===0?'<button type="button" class="row" id="sku-0">'+inner+'</button>':'<div class="row">'+inner+'</div>';}).join('')+'</div>';
 if(!P)h+=rules()+recent()+'<div class="note">Open a SKU to see its lots as bars of days left, with the near date threshold drawn across them.</div>';}
else if(S.scr==='lots'||S.scr==='pick'){var pk=S.scr==='pick';setNav({m:'inv',bc:bc0.concat(pk?[['Harbor Lager 24 pack','cb-hl'],'Pick '+SO]:['Harbor Lager 24 pack']),t:'Harbor Lager 24 pack',chip:['c-idle','3 lots'],scr:pk?'Pick':'Lots',back:1,pa:'<span class="mut mono" style="font-size:9.6px">1,200 cases</span>'});
 if(P)h=(pk?pl(P):field(P))+lots(P);
 else{h=field(P)+lots(P)+(pk?'<div class="dp">'+pl(P)+'<div class="cd"><div class="side"><span>Lot A is picked first because it has the nearest best by date. Click it to check it against '+ACC+'’s 30 day rule.</span></div></div></div>'+recent():rules()+recent());}}
else if(S.scr==='risk'){setNav({m:'inv',bc:bc0.concat([['Harbor Lager 24 pack','cb-hl'],'HL-2611-A']),t:'HL-2611-A',chip:['c-warn','Near date'],scr:'At risk',back:1});
 if(P)h='<div class="tl">'+tile('r-d','Days left','28','bad')+tile('r-q','At risk','180','bad')+tile('r-t','Threshold','30 days')+tile('r-a',ACC.split(' ')[0]+' needs','30 days')+'</div><button type="button" class="bt pri w" id="of">Offer lot A to '+ALT+'</button>';
 else{h=lots(P)+'<div class="dp"><div class="cd new"><div class="ct">Near date flag<span class="ch c-warn">180 cases at risk</span></div><div class="flag"><span>Lot <b>HL-2611-A</b> has <b id="r-d">28</b> days left, under the 30 day threshold. '+ACC+' needs 30 days on arrival, so <b id="r-q">180</b> cases can’t ship on '+SO+'.</span><span>'+ALT+' takes 14 days and orders lager every week.</span></div></div>'+
  '<div class="cd"><div class="side"><span>Offer the lot to '+ALT+'. The pick for '+SO+' moves to lots B and C.</span><button type="button" class="bt pri w" id="of">Offer lot A to '+ALT+'</button></div></div></div>'+pl(P);}}
else{setNav({m:'sal',bc:['Sales',['Offers','cb-of'],OFR],t:'Lot A offered',chip:['c-ok','Accepted'],scr:'Lot offered',back:1});
 if(P)h='<div class="tl">'+tile('o-a','Lot A left','0')+tile('o-q',ALT.split(' ')[0],'180')+tile('o-p',SO,n0(ORD))+tile('o-t','Cases left',n0(total()))+'</div>'+pl(P);
 else{h='<div class="cd new"><div class="kg">'+[['Offer',OFR],['Account',ALT],['Lot','HL-2611-A, 180 cases'],['Delivers','Nov 17']].map(function(k){return '<div class="kv"><small>'+k[0]+'</small><b>'+k[1]+'</b></div>';}).join('')+'</div></div>'+lots(P)+'<div class="dp">'+pl(P)+'<div class="cd"><div class="side"><span>'+ALT+' gets lot A with 27 days left on delivery. '+ACC+' gets lots B and C, 70 and 112 days left.</span><span>Cases left after both orders: <b class="mono" id="o-t">'+n0(total())+'</b></span></div></div></div>';}}
if(P&&S.scr!=='list')h+=xw(S.scr==='lots'?[['Account',ACC],['Ships','Nov 18'],['Rule','30 days on arrival']]:S.scr==='pick'?[['Lot A','28 days left'],['Account',ACC],['Ships','Nov 18']]:S.scr==='risk'?[[ALT,'Takes 14 days'],['Lot A','180 cases'],['Pick moves to','Lots B and C']]:[['Offer',OFR],['Delivers','Nov 17'],['Lot B and C','420 and 80']],S.scr==='pick');
if(P&&S.scr==='list')h+=xw([['Rule',ACC+' 30 days'],['Rule',ALT+' 14 days'],['Picking','Oldest first']]);
$('pg').innerHTML=h;
if(S.anim===1){var bs=[].slice.call(root.querySelectorAll('.lr .tr i'));later(function(){bs.forEach(function(b){b.style.width=b.getAttribute('data-w')+'%';});},60);}
S.anim=0;}
function resetState(){S={scr:'list',pick:false,flag:false,off:false,anim:0};render();}
var CAPAT=function(hh){return ph()?{l:8,t:5}:{l:14,t:visH()-hh-40};};
var ST=[
{id:'sku',target:function(){return $('sku-0');},prompt:'Open Harbor Lager 24 pack',where:'below',run:function(){S.scr='lots';S.anim=1;render();},
 after:['Three lots, drawn as days left','As of Nov 16: lot A 28 days, B 70 days, C 112 days. 180 + 420 + 600 = 1,200 cases, with the 30 day threshold drawn across.'],pc:'Lots A, B, C: 28, 70 and 112 days'},
{id:'pick',target:function(){return $('sp');},prompt:'Start the pick for SO-5126',where:'below',run:function(){S.pick=true;S.scr='pick';S.anim=2;render();},
 after:['The pick takes the oldest lots first','500 cases for Northgate Grocers: 180 from lot A, then 320 from lot B.'],pc:'180 from A, then 320 from B'},
{id:'flag',target:function(){return $('lot-0');},prompt:'Check lot A against the threshold',where:'below',run:function(){S.flag=true;S.scr='risk';render();},
 after:['Lot A is flagged at risk','28 days left is under the 30 day threshold, so 180 cases can’t ship to Northgate Grocers.'],pc:'Lot A flagged: 180 cases at risk'},
{id:'offer',target:function(){return $('of');},prompt:'Offer lot A to Dockside Taproom',where:function(){return ph()?'above':'below';},run:function(){S.off=true;S.scr='off';render();},
 after:['The near date lot finds a buyer','Dockside Taproom takes the 180 cases and lot A drops to 0. The Northgate pick moves to lots B and C: 420 + 80 = 500.'],pc:'Lot A to Dockside, lot A now 0'}];
ST.forEach(function(s){['prompt','where'].forEach(function(k){if(typeof s[k]==='function'){var f=s[k];Object.defineProperty(s,k,{get:f});}});});
'''
