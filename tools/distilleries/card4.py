"""Distilleries card 4: Release allocation and dry goods planning. Four number tiles above a channel split table, inside
the app shell. Start: the release for Single Barrel Bourbon 750 ml with its baseline stock in the tiles and an empty
split table. Walkthrough: open Available to read how 560 is figured (900 + 300 less 640), split the 560 cases across
distributors, tasting room and online (typed, prefilled 400, 100, 60), commit it and watch committed and available
update, open the bottle shortage for the next run (1,800 needed, 1,500 on hand) and raise a PO for 300 bottles at $0.92.
Numbers are asserted in numbers_check.py."""
SUMMARY = 'Release allocation and dry goods planning (four live stock tiles for a release SKU, available cases split across distributors, tasting room and online, committed and available updated, the bottle shortage for the next run and its purchase order)'
ARIA = 'Interactive product screen: read how 560 cases of Single Barrel Bourbon are available, split them 400 to distributors, 100 to the tasting room and 60 online, commit the split, then raise a purchase order for the 300 bottles short for the next run'
STEPS = 5
STUDIO = dict(lede='A typical release planner, built on your Sutton data with Studio. Want it different? Describe the change.',
              examples=['Add a channel', 'Change the allocation rule', 'Add a reserve for club members', 'Set a low stock alert'],
              built_on='Items, stock, orders and runs', change='Channels, rules and alerts')
STORY = [('Release', 'sal', 'tile', 'top right'), ('Stock detail', 'sal', 'inline button', 'center'),
         ('Split draft', 'sal', 'primary button', 'bottom right'), ('Release', 'sal', 'alert chip', 'top right'),
         ('Dry goods', 'inv', 'primary button', 'right')]

CSS = (
 '.tbr{display:flex;align-items:center;gap:10px}.pick{display:flex;align-items:center;gap:8px;height:32px;padding:0 10px;border:1px solid #D4D4D8;border-radius:7px;background:#fff;font-size:10.6px;font-weight:500;white-space:nowrap}.pick small{color:#71717A;font-family:"JetBrains Mono",ui-monospace,monospace;font-size:9.4px;font-weight:400}'
 '.tbr .nm{display:flex;flex-direction:column;gap:1px;line-height:1.25}.tbr .nm b{font-size:11.4px}.tbr .nm small{font-size:9px;color:#71717A}'
 '.tl{display:grid;grid-template-columns:repeat(4,1fr);gap:8px}.tile{border:1px solid #E4E4E7;border-radius:8px;padding:8px 10px;display:flex;flex-direction:column;gap:2px;background:#fff;text-align:left;font:inherit;color:#18181B}.tile small{font-size:8.8px;color:#71717A}.tile b{font-family:"JetBrains Mono",ui-monospace,monospace;font-size:17px;font-weight:600;transition:color .3s}.tile i{font-style:normal;font-size:8.4px;color:#A1A1AA}'
 'button.tile{cursor:pointer;transition:border-color .2s,box-shadow .2s}button.tile:hover,button.tile.fakehover{border-color:#18181B;box-shadow:0 0 0 1px #18181B}button.tile:focus-visible{outline:2px solid #18181B;outline-offset:1px}.tile.on{border-color:#18181B;box-shadow:0 0 0 1px #18181B}.tile.chg b{animation:exflash 1.2s ease}'
 '.fm{display:flex;align-items:center;gap:8px;padding:10px 11px;font-size:10px;flex-wrap:wrap}.fm b{font-family:"JetBrains Mono",ui-monospace,monospace;font-size:12px}.fm .op{color:#71717A}'
 '.sp .row{grid-template-columns:1fr 92px 64px 1fr 76px;font-size:9.8px;min-height:32px;white-space:nowrap}.sp .row span:nth-child(3){text-align:right}.sp .row .st{text-align:right}'
 '.sp .fld input{text-align:right;font-size:10.6px;padding:4px 7px}.sp .fld{position:relative}.sp .em{position:absolute;top:27px;right:0;white-space:nowrap}.sp .tot{font-weight:600;background:#FAFAFA}'
 '.mb{height:8px;border-radius:4px;background:#F4F4F5;overflow:hidden;display:flex}.mb i{display:block;height:100%;background:#3F3F46;border-right:1px solid #fff;transition:width .5s ease}.mb i:nth-child(2){background:#71717A}.mb i:nth-child(3){background:#A1A1AA}'
 '.spe{display:flex;align-items:center;justify-content:space-between;gap:10px;padding:12px 11px;font-size:9.8px;color:#71717A}.sf{display:flex;justify-content:flex-end;gap:10px;align-items:center;padding:8px 11px;border-top:1px solid #F0F0F1;font-size:9.8px;color:#71717A}.sf b{font-family:"JetBrains Mono",ui-monospace,monospace;color:#18181B}'
 '.al{display:inline-flex;align-items:center;gap:6px;height:26px;padding:0 10px;border:1px solid #FECACA;border-radius:999px;background:#FEF2F2;color:#B91C1C;font-size:9.8px;font-weight:600;cursor:pointer;white-space:nowrap;transition:box-shadow .2s}.al:hover,.al.fakehover{box-shadow:0 0 0 2px #FCA5A5}.al:focus-visible{outline:2px solid #18181B;outline-offset:1px}.al i{width:6px;height:6px;border-radius:50%;background:#DC2626}'
 '.od .row{grid-template-columns:62px 1fr 74px 50px;font-size:9.6px;white-space:nowrap}.od .row span:nth-child(n+3){text-align:right}'
 '.dg .row{grid-template-columns:1fr 62px 62px 62px 118px;font-size:9.8px;min-height:32px;white-space:nowrap}.dg .row span:nth-child(n+2){text-align:right}.dg .row.bad{background:#FFFBFB}'
 '.pov{display:grid;grid-template-columns:repeat(4,1fr);gap:8px 12px;padding:10px 11px}.pl .row{grid-template-columns:1fr 70px 60px 80px;font-size:9.8px;min-height:30px;white-space:nowrap}.pl .row span:nth-child(n+2){text-align:right}'
 '.note{border:1px solid #E4E4E7;background:#FAFAFA;border-radius:8px;padding:8px 10px;font-size:9.6px;line-height:1.45;color:#52525B}'
 '.shot.ph .tl{grid-template-columns:1fr 1fr;gap:6px}.shot.ph .tile{padding:4px 9px;min-height:38px;gap:0}.shot.ph .tile b{font-size:13px}.shot.ph .tile i{display:none}'
 '.shot.ph .sp .row{grid-template-columns:1fr 70px 70px;min-height:26px;font-size:10px}.shot.ph .sp .row>:nth-child(3),.shot.ph .sp .row>:nth-child(4){display:none}.shot.ph .bt.w{width:100%;min-height:38px;font-size:10.6px}.shot.ph .al{height:38px;width:100%;justify-content:center}'
 '.shot.ph .sf{padding:6px 0 0;border-top:0}.shot.ph .sp .row.tot{min-height:22px}.pr{display:flex;justify-content:space-between;font-size:10px;padding:0 2px}.pr b{font-family:"JetBrains Mono",ui-monospace,monospace}.shot.ph.nar .xn{display:none}'
)

WIN = ''

JS = r'''
var FOC='.rail .ni,.bc,.phd>*,.bn .bi,.pg .tile,.pg .ct,.pg .row,.pg .fm,.pg .spe,.pg .sf,.pg .tbr>*,.pg .note,.pg .pov,.pg .pr,.pg .al,.pg .bt';
var STOCK=900,EXP=300,COM=640,CH=['Distributors','Tasting room','Online'],DEF=[400,100,60];
var ORD=[['SO-5102','Northgate Beverage',300,'Nov 4'],['SO-5110','Club pickup, fall',180,'Nov 8'],['SO-5117','Elm Street Spirits',100,'Nov 12'],['SO-5121','Online preorders',60,'Nov 15']];
var NEED=1800,OH=1500,PRICE=92;
var S;
function spl(){var t=0;S.sp.forEach(function(v){t+=v;});return t;}
function avail0(){return STOCK+EXP-COM;}
function com(){return COM+(S.done?spl():0);}
function avail(){return STOCK+EXP-com();}
function num(v){v=String(v).replace(/,/g,'').trim();return /^\d{1,4}$/.test(v)?parseInt(v,10):-1;}
function tile(id,l,v,sub,btn,cls){var t=btn?'button':'div';return '<'+t+(btn?' type="button"':'')+' class="tile'+(cls?' '+cls:'')+'" id="'+id+'"><small>'+l+'</small><b id="'+id+'-v">'+n0(v)+'</b>'+(sub?'<i>'+sub+'</i>':'')+'</'+t+'>';}
function tiles(){var ch=S.anim==='done'?' chg':'';return '<div class="tl">'+tile('t-st','In stock',STOCK,'Cases in the warehouse')+tile('t-ex','Expected',EXP,'Run BR-0940, Dec 2')+tile('t-cm','Committed',com(),'On open orders','',ch)+tile('t-av','Available',avail(),'In stock plus expected, less committed',!S.det&&!S.split,(S.det&&!S.done?'on':'')+ch)+'</div>';}
function splitTable(P){var h='<div class="cd sp frm">'+(P?'':'<div class="ct">Channel split<span class="mut" style="font-weight:500">'+(S.split?(S.done?'Committed':'Draft, '+n0(avail0())+' cases'):'No split yet')+'</span></div>');
 if(!S.split)return h+'<div class="spe"><span>'+(P?'Split the available cases.':'Choose how the available cases go out by channel.')+'</span>'+(S.det?'<button type="button" class="bt" id="mk-sp">Split '+n0(avail0())+' cases</button>':'')+'</div></div>';
 if(!P)h+='<div class="row h"><span>Channel</span><span>Cases</span><span>Share</span><span></span><span class="st">Status</span></div>';
 S.sp.forEach(function(v,i){var sh=avail0()?Math.round(v*100/avail0()):0;h+='<div class="row"><span>'+CH[i]+'</span>'+(S.done?'<span class="mono" id="sp-'+i+'-v">'+n0(v)+'</span>':'<label class="fld" id="f-'+i+'"><input id="sp-'+i+'" value="'+S.v[i]+'" inputmode="numeric" autocomplete="off" aria-label="'+CH[i]+' cases"><span class="em">Over by '+(spl()-avail0())+'</span></label>')+'<span class="mono mut">'+sh+'%</span><span><span class="mb"><i style="width:'+sh+'%"></i></span></span><span class="st"><span class="ch '+(S.done?'c-ok">Committed':'c-idle">Draft')+'</span></span></div>';});
 h+='<div class="row tot"><span>Total</span><span class="mono" id="sp-t">'+n0(spl())+'</span><span class="mono mut">'+(P?'':'of '+n0(avail0()))+'</span><span></span><span class="st mono" id="sp-left">'+n0(avail0()-spl())+' left</span></div>';
 if(!S.done)h+='<div class="sf">'+(P?'':'<span>Available after the split <b id="sp-av">'+n0(avail0()-spl())+'</b></span>')+'<button type="button" class="bt pri'+(P?' w':'')+'" id="commit">Commit split</button></div>';
 return h+'</div>';}
function render(){var P=ph(),h='',bc0=['Sales',['Releases','cb-rl']];
if(S.scr==='rel'){var scr=S.done?'Release':S.split?'Split draft':S.det?'Stock detail':'Release';
 setNav({m:'sal',bc:bc0.concat([S.det&&!S.done?(S.split?'Split':'Available'):'Fall release']),t:'Fall release',chip:S.done?['c-ok','Allocated']:['c-idle','Planning'],scr:scr,back:S.det?1:0,pa:S.done?'<button type="button" class="al" id="al"><i></i>Bottles short 300</button>':''});
 if(P){if(S.split&&!S.done)h=splitTable(P);
  else if(S.det&&!S.done)h='<div class="cd"><div class="row" style="grid-template-columns:1fr auto"><span>In stock</span><span class="mono">'+n0(STOCK)+'</span></div><div class="row" style="grid-template-columns:1fr auto"><span>Plus expected</span><span class="mono">'+n0(EXP)+'</span></div><div class="row" style="grid-template-columns:1fr auto"><span>Less committed</span><span class="mono">'+n0(COM)+'</span></div><div class="row" style="grid-template-columns:1fr auto;font-weight:600"><span>Available</span><span class="mono" id="f-av">'+n0(avail0())+'</span></div></div><button type="button" class="bt w" id="mk-sp">Split '+n0(avail0())+' cases</button>';
  else{h=tiles()+(S.done?'<button type="button" class="al" id="al-p"><i></i>Bottles short 300 for the next run</button>':'<div class="cd sp">'+CH.map(function(c){return '<div class="row" style="min-height:20px"><span>'+c+'</span><span class="mono mut">0</span><span class="mut">Not set</span></div>';}).join('')+'</div>');}}
 else{h='<div class="tbr"><span class="pick">Single Barrel Bourbon 750 ml<small>SB-750</small><svg width="10" height="10" viewBox="0 0 10 10" fill="none" aria-hidden="true"><path d="M2.5 4l2.5 2.5L7.5 4" stroke="#71717A" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"/></svg></span><span class="nm grow"><b>Fall release</b><small>Cases of 6, release date Dec 9</small></span></div>'+tiles();
  if(S.det&&!S.done)h+='<div class="cd"><div class="ct">How available is figured<span class="mut" style="font-weight:500">Live from stock and orders</span></div><div class="fm"><span>In stock</span><b>'+n0(STOCK)+'</b><span class="op">plus expected</span><b>'+n0(EXP)+'</b><span class="op">less committed</span><b>'+n0(COM)+'</b><span class="op">is available</span><b id="f-av">'+n0(avail0())+'</b></div></div>';
  h+=splitTable(false);
  h+='<div class="cd od"><div class="ct">Committed orders<span class="mut" style="font-weight:500">'+n0(com())+' cases</span></div>'+ORD.map(function(o){return '<div class="row"><span class="mono">'+o[0]+'</span><span>'+o[1]+'</span><span class="mono">'+o[2]+' cases</span><span class="mono mut">'+o[3]+'</span></div>';}).join('')+(S.done?'<div class="row"><span class="mono">SPL-0311</span><span>Fall release split, 3 channels</span><span class="mono">'+n0(spl())+' cases</span><span class="mono mut">Nov 24</span></div>':'')+'</div>';
  if(!S.det)h+='<div class="cd od"><div class="ct">Past releases<span class="mut" style="font-weight:500">Distributors, tasting room, online</span></div><div class="row"><span class="mono">SPL-0274</span><span>Spring release, Single Barrel Bourbon</span><span class="mono">380, 90, 50</span><span class="mono mut">Apr 9</span></div><div class="row"><span class="mono">SPL-0231</span><span>Holiday release, Barrel Rye</span><span class="mono">300, 120, 80</span><span class="mono mut">Dec 3</span></div><div class="row"><span class="mono">SPL-0198</span><span>Fall release, Single Barrel Bourbon</span><span class="mono">360, 110, 40</span><span class="mono mut">Dec 11</span></div><div class="row"><span class="mono">SPL-0174</span><span>Summer release, Dry gin</span><span class="mono">240, 140, 70</span><span class="mono mut">Jul 15</span></div><div class="row"><span class="mono">SPL-0150</span><span>Spring release, Barrel Rye</span><span class="mono">280, 100, 60</span><span class="mono mut">Apr 2</span></div></div>';}}
else if(S.scr==='dry'){setNav({m:'inv',bc:['Inventory',['Dry goods','cb-dg'],'Run BR-0940'],t:'Dry goods, run BR-0940',chip:['c-bad','1 short'],scr:'Dry goods',back:1});
 if(P)h='<div class="tl">'+tile('d-nd','Bottles needed',NEED)+tile('d-oh','On hand',OH)+tile('d-sh','Short',NEED-OH,'','','')+tile('d-cs','Run, cases',EXP)+'</div><button type="button" class="bt pri w" id="po">Raise PO for '+n0(NEED-OH)+' bottles</button>';
 else{h='<div class="tl">'+tile('d-rn','Run BR-0940',EXP,'Cases, bottling Dec 2')+tile('d-nd','Bottles needed',NEED,'300 cases of 6')+tile('d-oh','Bottles on hand',OH,'Glass, 750 ml')+tile('d-sh','Short',NEED-OH,'Glass only')+'</div>';
  h+='<div class="cd dg"><div class="ct">Dry goods for run BR-0940<span class="mut" style="font-weight:500">From the BOM, 300 cases</span></div><div class="row h"><span>Item</span><span>Needed</span><span>On hand</span><span>Short</span><span>Status</span></div>'+
  [['Glass bottle, 750 ml',NEED,OH],['Closure, bar top cork',1800,2400],['Front label',1800,3000],['Back label',1800,2600],['Carton, 6 bottle',300,420]].map(function(x,i){var sh=x[1]-x[2];return '<div class="row'+(sh>0?' bad':'')+'"><span>'+x[0]+'</span><span class="mono">'+n0(x[1])+'</span><span class="mono">'+n0(x[2])+'</span><span class="mono">'+(sh>0?n0(sh):'0')+'</span><span>'+(sh>0?'<button type="button" class="bt pri" id="po">Raise PO</button>':'<span class="ch c-ok">Covered</span>')+'</span></div>';}).join('')+'</div>';
  h+='<div class="note">The 300 expected cases are now committed to the fall release, so run BR-0940 needs all 1,800 bottles by Dec 2. Glass is the only line short.</div>';}}
else{var amt=(NEED-OH)*PRICE;setNav({m:'pur',bc:['Purchasing',['Purchase orders','cb-po'],'PO-3412'],t:'PO-3412',chip:['c-info','Sent'],scr:'Purchase order',back:1});
 if(P)h='<div class="cd"><div class="row" style="grid-template-columns:1fr auto"><span>Coastline Glass Works</span><span class="ch c-info">Sent</span></div><div class="row" style="grid-template-columns:1fr auto"><span>Bottles at $0.92</span><span class="mono">'+n0(NEED-OH)+'</span></div><div class="row" style="grid-template-columns:1fr auto;font-weight:600"><span>Total</span><span class="mono" id="po-t">'+m2(amt/100)+'</span></div><div class="row xn" style="grid-template-columns:1fr auto"><span>Arrives</span><span class="mono">Nov 28</span></div></div>';
 else{h='<div class="cd"><div class="pov">'+[['Vendor','Coastline Glass Works'],['Lead time','4 days'],['Arrives','Nov 28'],['For run','BR-0940, Dec 2']].map(function(x){return '<div class="kv"><small>'+x[0]+'</small><b>'+x[1]+'</b></div>';}).join('')+'</div></div>';
  h+='<div class="cd pl"><div class="ct">Lines<span class="mut" style="font-weight:500">From the shortage on run BR-0940</span></div><div class="row h"><span>Item</span><span>Quantity</span><span>Price</span><span>Amount</span></div><div class="row"><span>Glass bottle, 750 ml</span><span class="mono" id="po-q">'+n0(NEED-OH)+'</span><span class="mono">$0.92</span><span class="mono">'+m2(amt/100)+'</span></div><div class="row" style="font-weight:600;background:#FAFAFA"><span>Total</span><span></span><span></span><span class="mono" id="po-t">'+m2(amt/100)+'</span></div></div>';
  h+='<div class="tl">'+tile('p-nd','Bottles needed',NEED)+tile('p-oh','On hand',OH)+tile('p-in','On order',NEED-OH)+tile('p-sh','Short',0)+'</div>';
  h+='<div class="note">With PO-3412 the run is covered: '+n0(OH)+' on hand plus '+n0(NEED-OH)+' arriving Nov 28 makes '+n0(NEED)+' bottles, two working days before bottling.</div>';}}
if(P)h+=xw(S.scr==='dry'?[['Closures, labels, cartons','Covered'],['Bottling','Dec 2'],['Vendor','Coastline Glass Works']]:S.scr==='po'?[['Lead time','4 days'],['For run','BR-0940, Dec 2'],['Bottles after the PO',n0(NEED)]]:S.done?[['Distributors',n0(S.sp[0])+' committed'],['Tasting room',n0(S.sp[1])+' committed'],['Online',n0(S.sp[2])+' committed']]:S.split?[['Share','71%, 18%, 11%'],['Release date','Dec 9']]:S.det?[['Open orders','4, 640 cases'],['Next run','BR-0940, Dec 2']]:[['Committed orders','4'],['Next run','BR-0940, Dec 2'],['Release date','Dec 9']]);
$('pg').innerHTML=h;}
$('pg').addEventListener('input',function(e){var m=/^sp-(\d)$/.exec(e.target.id);if(!m)return;var i=+m[1];S.v[i]=e.target.value;var n=num(e.target.value);S.sp[i]=n<0?0:n;
 [0,1,2].forEach(function(k){var f=$('f-'+k);if(f)f.classList.remove('err');});
 if($('sp-t'))$('sp-t').textContent=n0(spl());if($('sp-left'))$('sp-left').textContent=n0(avail0()-spl())+' left';if($('sp-av'))$('sp-av').textContent=n0(avail0()-spl());});
function resetState(){S={scr:'rel',det:false,split:false,done:false,anim:'',sp:[0,0,0],v:['','','']};render();}
function okS(){var bad=false;[0,1,2].forEach(function(i){var n=num($('sp-'+i).value);if(n<0){bad=true;$('f-'+i).classList.add('err');}});
 if(!bad&&spl()>avail0()){bad=true;$('f-0').classList.add('err');[0,1,2].forEach(function(i){$('f-'+i).querySelector('.em').textContent='Over by '+(spl()-avail0());});}return !bad;}
var CAPAT=function(hh){return ph()?{l:8,t:5}:{l:14,t:visH()-hh-40};};
var ST=[
{id:'avail',target:function(){return $('t-av');},prompt:'Open Available',where:'below',run:function(){S.det=true;render();},
 after:['Four live numbers, and how available is figured','900 in stock plus 300 expected, less 640 committed: 560 cases free for the fall release.'],pc:'900 plus 300, less 640: 560 free'},
{id:'split',target:function(){return $('mk-sp');},prompt:'Split the 560 cases',where:'below',run:function(){S.split=true;S.sp=DEF.slice();S.v=DEF.map(String);render();},
 after:['A split across three channels','Distributors 400, tasting room 100, online 60. Type over any number and the total and what is left follow.'],pc:'400, 100 and 60 across three channels'},
{id:'commit',target:function(){return $('commit');},prompt:'Commit the split',where:'above',ok:okS,run:function(){S.done=true;S.anim='done';render();},
 after:function(){return['Committed and available update',S.sp.map(n0).join(' + ')+' = '+n0(spl())+' cases committed. Committed goes from 640 to '+n0(com())+', available to '+n0(avail())+'.'];},pc:'Committed 1,200, available 0'},
{id:'short',target:function(){return ph()?$('al-p'):$('al');},prompt:'Open the bottle shortage',where:'below',run:function(){S.scr='dry';render();},
 after:['The next run is short on glass','Run BR-0940 bottles 300 cases: 1,800 bottles needed, 1,500 on hand, 300 short.'],pc:'1,800 needed, 1,500 on hand: 300 short'},
{id:'po',target:function(){return $('po');},prompt:'Raise a PO for the 300 bottles',where:function(){return ph()?'above':'below';},run:function(){S.scr='po';render();},
 after:['The PO covers the shortage','PO-3412 to Coastline Glass Works: 300 bottles at $0.92, $276.00, arriving Nov 28.'],pc:'300 bottles at $0.92: $276.00'}];
ST.forEach(function(s){['prompt','where'].forEach(function(k){if(typeof s[k]==='function'){var f=s[k];Object.defineProperty(s,k,{get:f});}});});
'''
