"""Beverage distributors card 3: Recall lookups from lot to account. A left to right trace (supplier lot, received,
shipped and on hand, accounts) inside the app shell. Start: the supplier lot field (prefilled BRW-4471, read only) and an
empty prompt. Walkthrough: trace the lot about 1.3 s after the card is in view, so the full trace is up by about 2 s
(960 cases received as 40 pallets of 24, 780 shipped to five accounts, 180 still on hand in cooler bin C-04), open the
shipped cases to list every account with its delivery date and cases (120 + 240 + 60 + 300 + 60 = 780), place a hold
on the 180 on hand, then download the account list. Case counts are asserted in numbers_check.py; every name is invented."""
SUMMARY = 'Recall lookups from lot to account (a supplier lot traced left to right from receipt to the accounts that got it, the account list with delivery dates and cases, a hold on the stock still on hand and the list downloaded)'
ARIA = 'Interactive product screen: trace supplier lot BRW-4471 from 960 cases received to 780 shipped to five accounts and 180 on hand, list the accounts, hold the 180 cases, then download the list'
STEPS = 4
STUDIO = dict(lede='A typical lot trace and recall lookup, built on your Sutton data with Studio. Want it different? Describe the change.',
              examples=['Add a supplier contact field', 'Change the account list layout', 'Add a recall notice step', 'Group accounts by route'],
              built_on='Lots, receipts, orders and deliveries', change='Fields, views and steps')
STORY = [('Lot search', 'trc', 'inline button', 'top right'), ('Trace', 'trc', 'flow node', 'center'),
         ('Accounts', 'trc', 'primary button', 'center right'), ('Accounts', 'trc', 'download button', 'top left')]
# the lot is traced about 1.3 s after the card is in view: start sooner and move the cursor faster
ENGINE_PATCH = [('startDelay:600,lead:900', 'startDelay:250,lead:650')]

CSS = (
 '.empt.big{min-height:196px}.shot.ph .empt.big{min-height:0}.nw{white-space:nowrap;font-family:var(--mn)}'
 '.fl{position:relative;display:grid;grid-template-columns:1fr 1fr 1fr 1.25fr;gap:28px;padding:12px 12px 14px}.fl svg.ln{position:absolute;left:0;top:0;width:100%;height:100%;pointer-events:none;overflow:visible}'
 '.col{display:flex;flex-direction:column;justify-content:center;gap:8px;position:relative;z-index:1}.col>small{font-size:8.6px;color:#A1A1AA;font-weight:500;text-align:center;margin-bottom:2px}'
 '.nd{border:1px solid #E4E4E7;border-radius:7px;background:#fff;padding:6px 8px;display:flex;flex-direction:column;gap:1px;text-align:left;font:inherit;color:#18181B;line-height:1.3;min-width:0;transition:box-shadow .2s,border-color .2s,background-color .3s}'
 '.nd small{font-size:8px;color:#71717A}.nd b{font-family:var(--mn);font-size:10px;font-weight:600}.nd span{font-size:8.8px;color:#52525B;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}.nd em{font-style:normal;font-family:var(--mn);font-size:11px;font-weight:600}'
 '.nd.ac{padding:4px 8px;flex-direction:row;align-items:center;justify-content:space-between;gap:6px}.nd.ac span{color:#18181B}.nd.ac em{font-size:9.6px}.nd.root{border-color:#18181B;box-shadow:0 0 0 1px #18181B}.nd.hold{border-color:#FDE68A;background:#FFFBEB}'
 'button.nd{cursor:pointer}button.nd:hover,button.nd.fakehover{border-color:#18181B;box-shadow:0 0 0 1px #18181B}button.nd:focus-visible{outline:2px solid #18181B;outline-offset:1px}'
 '.ln path{fill:none;stroke:#A1A1AA;stroke-width:1.2}.ln path.hot{stroke:#18181B;stroke-width:1.6}.fl.in .nd{animation:exin .45s cubic-bezier(.22,.9,.28,1) both}.fl.in .col:nth-child(3) .nd{animation-delay:.08s}.fl.in .col:nth-child(4) .nd{animation-delay:.16s}.fl.in .col:nth-child(5) .nd{animation-delay:.24s}'
 '.tl{display:grid;grid-template-columns:repeat(4,1fr);gap:8px}.tile{border:1px solid #E4E4E7;border-radius:8px;padding:7px 10px;display:flex;flex-direction:column;gap:1px;background:#fff}.tile small{font-size:8.8px;color:#71717A}.tile b{font-family:var(--mn);font-size:15px;font-weight:600}.tile.warn b{color:#B45309}'
 '.dt .row{grid-template-columns:110px 1fr 100px 70px;font-size:9.6px;white-space:nowrap}.dt .row span:nth-child(n+3){text-align:right}'
 '.rt .row{grid-template-columns:1fr 64px 70px 56px;font-size:9.8px;min-height:28px;white-space:nowrap}.rt .row span:nth-child(n+2){text-align:right;font-family:var(--mn)}.rt .row.tot{font-weight:600;background:#FAFAFA}.rt .row.h span{font-family:Inter,sans-serif}'
 '.dp{display:grid;grid-template-columns:1fr 210px;gap:10px}.side{display:flex;flex-direction:column;gap:7px;padding:10px 11px;font-size:9.8px;color:#52525B;line-height:1.45}.side b{color:#18181B}.side .bt.w{text-align:center;height:30px}'
 '.dl{display:inline-flex;align-items:center;gap:5px}.dl svg{flex:none}.done-l{display:inline-flex;align-items:center;gap:5px;font-weight:500;font-size:9.4px;color:#166534}'
 '.kg{display:grid;grid-template-columns:repeat(4,1fr);gap:8px 12px;padding:9px 11px}.note{border:1px solid #E4E4E7;background:#FAFAFA;border-radius:8px;padding:8px 10px;font-size:9.6px;line-height:1.45;color:#52525B}'
 '.vl{display:flex;flex-direction:column}.vl .vr{display:flex;align-items:center;justify-content:space-between;gap:8px;min-height:22px;padding:0 9px 0 22px;position:relative;border-top:1px solid #F0F0F1;background:#fff;width:100%;font:inherit;font-size:10px;color:#18181B;border-left:0;border-right:0;border-bottom:0;text-align:left}'
 '.vl .vr::before{content:"";position:absolute;left:10px;top:0;bottom:0;width:1px;background:#D4D4D8}.vl .vr::after{content:"";position:absolute;left:7px;top:50%;width:7px;height:7px;margin-top:-3.5px;border-radius:50%;background:#fff;border:1.5px solid #71717A}.vl .vr:first-child{border-top:0}'
 '.vl .vr.k1{padding-left:34px}.vl .vr.k1::after{left:19px}.vl .vr.k2{padding-left:46px}.vl .vr.k2::after{left:31px}.vl .vr b{font-family:var(--mn);font-size:10px}.vl .vr small{color:#71717A;font-size:9px;font-family:var(--mn)}'
 '.vl button.vr{min-height:40px;cursor:pointer}.vl button.vr:hover,.vl button.vr.fakehover{background:#F4F4F5}.vl button.vr:focus-visible{outline:2px solid #18181B;outline-offset:-2px}'
 '.shot.ph .bt.w{min-height:40px;width:100%;font-size:10.6px}.shot.ph .empt.big{padding:12px}.shot.ph .dl{min-height:40px}'
 '.shot.ph .rt .row{grid-template-columns:1fr 52px 40px;min-height:21px;font-size:10px}.shot.ph .rt .row span:nth-child(2){display:none}.shot.ph .rt .row.h{display:none}'
 '.ph2{display:grid;grid-template-columns:1fr 1fr;gap:6px}.ph2 .tile{padding:4px 9px}.ph2 .tile b{font-size:12px}.shot.ph.nar .xn{display:none}.shot.ph.nar .vl .vr{min-height:20px}.shot.ph.nar .vl button.vr{min-height:40px}'
)

WIN = ''

JS = r'''
var FOC='.rail .ni,.bc,.phd>*,.bn .bi,.pg .tile,.pg .ct,.pg .nd,.pg .col>small,.pg .row,.pg .empt,.pg .rof,.pg .side,.pg .note,.pg .vr,.pg .bt';
var LOT='BRW-4471',SUP='Harbor Brewing',PAL=40,PER=24,OH=180,BIN='C-04';
var ACC=[['Dockside Taproom','SO-5031','Nov 6',120],['Greenline Market','SO-5034','Nov 7',240],['Pier 9 Bar','SO-5040','Nov 9',60],['Northgate Grocers','SO-5042','Nov 10',300],['Elm Street Liquor','SO-5047','Nov 12',60]];
var S;
function rec(){return PAL*PER;}
function shp(){var t=0;ACC.forEach(function(a){t+=a[3];});return t;}
function nd(o){var t=o.btn?'button':'div';return '<'+t+(o.btn?' type="button"':'')+' class="nd'+(o.cls?' '+o.cls:'')+'" id="'+o.id+'">'+(o.k?'<small>'+o.k+'</small>':'')+'<b>'+o.b+'</b>'+(o.s?'<span>'+o.s+'</span>':'')+(o.q?'<em>'+o.q+'</em>':'')+'</'+t+'>';}
var EDGES=[['n-lot','n-rc'],['n-rc','n-sh'],['n-rc','n-oh'],['n-sh','n-a0'],['n-sh','n-a1'],['n-sh','n-a2'],['n-sh','n-a3'],['n-sh','n-a4']];
function links(){var fl=root.getElementById('fl');if(!fl)return;var sv=fl.querySelector('svg'),p='',F=fl.getBoundingClientRect(),k=F.width/fl.offsetWidth||1;function bx(e){var r=e.getBoundingClientRect();return{l:(r.left-F.left)/k,t:(r.top-F.top)/k,w:r.width/k,h:r.height/k};}
 EDGES.forEach(function(e){var a=$(e[0]),b=$(e[1]);if(!a||!b)return;a=bx(a);b=bx(b);var x1=a.l+a.w,y1=a.t+a.h/2,x2=b.l,y2=b.t+b.h/2,m=(x1+x2)/2;
  p+='<path class="'+(e[0]==='n-sh'||e[1]==='n-oh'?'':'hot')+'" d="M'+x1+' '+y1+'C'+m+' '+y1+' '+m+' '+y2+' '+x2+' '+y2+'"/>';});sv.innerHTML=p;}
function field(P){return rof({l:'Supplier lot',id:'il',v:LOT,b:S.scr==='search'?'Trace':'Traced',bid:'tr',cx:P?'':SUP+' supplier lot'});}
function ohNode(){return nd({id:'n-oh',k:'Still on hand',b:'Bin '+BIN,s:S.hold?'On hold':'Cooler',q:n0(OH),cls:S.hold?'hold':''});}
function dlb(){return S.dl?'<span class="done-l" id="dld"><svg width="11" height="11" viewBox="0 0 12 12" fill="none" aria-hidden="true"><path d="M2.5 6.2l2.3 2.3 4.7-5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>recall-'+LOT+'.csv</span>':'<button type="button" class="bt dl" id="dl"><svg width="11" height="11" viewBox="0 0 12 12" fill="none" aria-hidden="true"><path d="M6 1.8v6M3.4 5.4L6 8l2.6-2.6M2 10.2h8" stroke="currentColor" stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round"/></svg>Download list</button>';}
function acct(P){var h='<div class="cd rt"><div class="ct">'+(P?dlb():'Accounts that got '+LOT+dlb())+'</div><div class="row h"><span>Account</span><span>Order</span><span>Delivered</span><span>Cases</span></div>';
 ACC.forEach(function(a,i){h+='<div class="row"><span>'+a[0]+'</span><span>'+a[1]+'</span><span>'+a[2]+'</span><span id="ac-'+i+'">'+a[3]+'</span></div>';});
 return h+'<div class="row tot"><span>Total shipped</span><span></span><span></span><span id="ac-t">'+n0(shp())+'</span></div></div>';}
function holdCard(){return '<div class="cd"><div class="side"><span>Still on hand: <b id="h-q">'+OH+'</b> cases in cooler bin <b class="nw">'+BIN+'</b>.</span>'+(S.hold?'<span class="ch c-warn" id="h-st">On hold, H-0311</span><span>The 180 cases can’t be picked or shipped until the hold is released.</span>':'<button type="button" class="bt pri w" id="hd">Place hold on '+OH+' cases</button>')+'</div></div>';}
function lotCard(){return '<div class="cd"><div class="ct">Lot '+LOT+'<span class="mut" style="font-weight:500">From the receipt</span></div><div class="kg">'+[['Supplier',SUP],['Item','Harbor Lager 24 pack'],['Packaged','Oct 28'],['Best by','Feb 25']].map(function(k){return '<div class="kv"><small>'+k[0]+'</small><b>'+k[1]+'</b></div>';}).join('')+'</div></div>';}
function render(){var P=ph(),h='',bc0=['Traceability',['Recall lookup','cb-rl']];
if(S.scr==='search'){setNav({m:'trc',bc:['Traceability','Recall lookup'],t:'Recall lookup',scr:'Lot search'});
 h=field(P)+'<div class="empt big"><b>Trace a supplier lot</b><span>'+(P?'See where every case went.':'From receipt to every account that got it, with what is still on hand. Hold the stock and download the account list in two clicks.')+'</span></div>'+(P?'':'<div class="cd dt"><div class="ct">Recent lookups<span class="mut" style="font-weight:500">Quality team</span></div>'+[['KSB-2290','Kestrel Springs, seltzer cans','Mock recall','Oct 30'],['HCO-1187','Hollow Creek, juice bottles','Supplier notice','Oct 14'],['MTC-0932','Morning Tide, cold brew cans','Mock recall','Sep 22'],['BRW-4310','Harbor Brewing, lager cans','Supplier notice','Sep 8']].map(function(x){return '<div class="row"><span class="mono">'+x[0]+'</span><span>'+x[1]+'</span><span class="mut">'+x[2]+'</span><span class="mono mut">'+x[3]+'</span></div>';}).join('')+'</div><div class="cd dt"><div class="ct">Holds this quarter<span class="mut" style="font-weight:500">Released after review</span></div>'+[['H-0307','Morning Tide, cold brew cans','48 cases','Released'],['H-0298','Hollow Creek, juice bottles','96 cases','Released'],['H-0284','Kestrel Springs, seltzer cans','30 cases','Released']].map(function(x){return '<div class="row"><span class="mono">'+x[0]+'</span><span>'+x[1]+'</span><span class="mono">'+x[2]+'</span><span class="mut">'+x[3]+'</span></div>';}).join('')+'</div>');}
else if(S.scr==='trace'){setNav({m:'trc',bc:bc0.concat([LOT]),t:LOT,chip:['c-info','Traced'],scr:'Trace',back:1,pa:'<span class="mut" style="font-size:9.6px">'+SUP+'</span>'});
 if(P){h='<div class="cd vl"><div class="vr"><span>Lot <b>'+LOT+'</b></span><small>'+SUP+'</small></div><div class="vr k1"><span>Received</span><small id="f-rc">'+n0(rec())+'</small></div><button type="button" class="vr k1" id="n-sh"><span>Shipped, 5 accounts</span><small id="f-sh">'+n0(shp())+'</small></button>'+
  ACC.map(function(a,i){return '<div class="vr k2'+(i>2?' xn':'')+'"><span>'+a[0]+'</span><small>'+a[3]+'</small></div>';}).join('')+'<div class="vr k1"><span>On hand, bin '+BIN+'</span><small id="f-oh">'+OH+'</small></div></div>';}
 else{h=field(P)+'<div class="cd"><div class="fl in" id="fl"><svg class="ln" aria-hidden="true"></svg><div class="col"><small>Supplier lot</small>'+nd({id:'n-lot',k:SUP,b:LOT,s:'Harbor Lager 24 pack',cls:'root'})+'</div>'+
  '<div class="col"><small>Received</small>'+nd({id:'n-rc',k:'Nov 3, PO-2160',b:PAL+' pallets of '+PER,s:'Cases',q:'<span id="f-rc">'+n0(rec())+'</span>'})+'</div>'+
  '<div class="col"><small>Shipped and on hand</small>'+nd({id:'n-sh',k:'Shipped Nov 6 to 12',b:'5 accounts',s:'Cases',q:'<span id="f-sh">'+n0(shp())+'</span>',btn:1})+ohNode().replace('<em>','<em id="f-oh">')+'</div>'+
  '<div class="col"><small>Accounts</small>'+ACC.map(function(a,i){return '<div class="nd ac" id="n-a'+i+'"><span>'+a[0]+'</span><em>'+a[3]+'</em></div>';}).join('')+'</div></div></div>';
  h+='<div class="tl"><div class="tile"><small>Received</small><b>'+n0(rec())+'</b></div><div class="tile"><small>Shipped</small><b>'+n0(shp())+'</b></div><div class="tile"><small>Still on hand</small><b>'+OH+'</b></div><div class="tile"><small>Accounts</small><b>'+ACC.length+'</b></div></div>';
  h+='<div class="note">'+n0(shp())+' shipped plus '+OH+' on hand accounts for all '+n0(rec())+' cases received. Open the shipped cases to list every account.</div>'+lotCard();}}
else{setNav({m:'trc',bc:bc0.concat([['BRW-4471','cb-lot'],'Accounts']),t:'Accounts, '+LOT,chip:S.hold?['c-warn','Hold placed']:['c-info','5 accounts'],scr:'Accounts',back:1});
 if(P){h=acct(P)+(S.hold?'<div class="ph2"><div class="tile warn"><small>On hold</small><b id="h-q">'+OH+'</b></div><div class="tile"><small>Bin</small><b>'+BIN+'</b></div></div>':'<button type="button" class="bt pri w" id="hd">Place hold on '+OH+' cases</button>');}
 else{h='<div class="tl"><div class="tile"><small>Received</small><b>'+n0(rec())+'</b></div><div class="tile"><small>Shipped</small><b>'+n0(shp())+'</b></div><div class="tile'+(S.hold?' warn':'')+'"><small>'+(S.hold?'On hold':'Still on hand')+'</small><b>'+OH+'</b></div><div class="tile"><small>Accounts</small><b>'+ACC.length+'</b></div></div><div class="dp">'+acct(P)+holdCard()+'</div>';
  h+=S.dl?'<div class="note" id="dln">recall-'+LOT+'.csv saved: 5 accounts, '+n0(shp())+' cases, with order numbers, delivery dates and buyer contacts, ready for the recall notice.</div>':'<div class="note">Every case of '+LOT+' is accounted for: '+n0(shp())+' at five accounts and '+OH+' in the cooler.</div>';h+=lotCard();}}
if(P&&S.scr!=='search')h+=xw(S.scr==='trace'?[['Supplier',SUP],['Received','Nov 3, '+PAL+' pallets']]:S.hold?[['Hold','H-0311'],['Released by','Quality team']]:[['On hand','180 in bin C-04'],['Delivered','Nov 6 to 12']],S.scr==='acct');
$('pg').innerHTML=h;links();}
if('ResizeObserver'in window)new ResizeObserver(function(){if(S)links();}).observe($('pg'));
function resetState(){S={scr:'search',hold:false,dl:false};render();}
var CAPAT=function(hh){return ph()?{l:8,t:5}:{l:14,t:visH()-hh-40};};
var ST=[
{id:'trace',target:function(){return $('tr');},prompt:'Trace BRW-4471',where:'below',run:function(){S.scr='trace';render();},
 after:['The whole lot on one screen','960 cases received from Harbor Brewing, 40 pallets of 24. 780 shipped to five accounts, 180 still on hand in cooler bin C-04.'],pc:'960 in: 780 shipped, 180 on hand'},
{id:'acct',target:function(){return $('n-sh');},prompt:'Open the 780 shipped cases',where:function(){return ph()?'above':'below';},run:function(){S.scr='acct';render();},
 after:['Every account, with dates and cases','Dockside Taproom 120, Greenline Market 240, Pier 9 Bar 60, Northgate Grocers 300, Elm Street Liquor 60: 780 cases, delivered Nov 6 to 12.'],pc:'Five accounts, 780 cases'},
{id:'hold',target:function(){return $('hd');},prompt:'Hold the 180 cases on hand',where:function(){return ph()?'above':'below';},run:function(){S.hold=true;render();},
 after:['The stock still on hand is held','Hold H-0311 on 180 cases in cooler bin C-04. They can’t be picked until it is released.'],pc:'180 cases on hold in bin C-04'},
{id:'dl',target:function(){return $('dl');},prompt:'Download the account list',where:'below',run:function(){S.dl=true;render();},
 after:['The account list, ready to send','recall-BRW-4471.csv: five accounts and 780 cases, with order numbers, delivery dates and buyer contacts.'],pc:'Account list downloaded'}];
ST.forEach(function(s){['prompt','where'].forEach(function(k){if(typeof s[k]==='function'){var f=s[k];Object.defineProperty(s,k,{get:f});}});});
'''
