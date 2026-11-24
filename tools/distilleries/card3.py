"""Distilleries card 3: Lot tracing and recall lookups. A left to right trace flow of lots, batches, bottling runs and
accounts, inside the app shell. Start: an empty lot field (type and press Enter, or use the sample). Walkthrough:
BT-2209 is typed about 1.3 s after the card appears and the full forward trace is up by about 4 s, then bottling run B
is followed back to its source lots, the recall lookup lists every account holding the lot, and one account opens down
to its order. Case counts are asserted in numbers_check.py. Every account name is invented."""
SUMMARY = 'Lot tracing and recall lookups (a botanical lot typed into an empty lot field, the forward trace from lot to batch, bottling runs and accounts, one bottling run traced back to its source lots, the recall list of every account holding the lot, one account opened to its order)'
ARIA = 'Interactive product screen: trace botanical lot BT-2209 forward to gin batch GN-118, two bottling runs and five accounts, follow run B back to its source lots, then list every account for a recall lookup'
STEPS = 4
STUDIO = dict(lede='A typical lot trace and recall lookup, built on your Sutton data with Studio. Want it different? Describe the change.',
              examples=['Add a supplier lot field', 'Change the trace report layout', 'Add a recall notice step', 'Group accounts by region'],
              built_on='Lots, batches, bottling runs and orders', change='Fields, views and steps')
STORY = [('Lot search', 'trc', 'sample chip', 'top left'), ('Forward trace', 'trc', 'flow node', 'center'),
         ('Backward trace', 'trc', 'tab', 'top right'), ('Recall list', 'trc', 'table row', 'center left')]
# the walkthrough types the lot about 1.3 s after the card is in view: start sooner and move the cursor faster
ENGINE_PATCH = [('startDelay:600,lead:900', 'startDelay:250,lead:650')]

CSS = (
 '.sbar{display:flex;align-items:center;gap:8px}.srch{flex:1;position:relative;display:flex;flex-direction:column}.srch input{font:inherit;font-family:"JetBrains Mono",ui-monospace,monospace;font-size:11px;height:32px;padding:0 10px 0 30px;border:1px solid #D4D4D8;border-radius:7px;background:#fff;color:#18181B;width:100%}'
 '.srch input::placeholder{font-family:Inter,sans-serif;color:#A1A1AA}.srch input:focus-visible{outline:2px solid #18181B;outline-offset:1px}.srch svg{position:absolute;left:10px;top:10px}.srch.err input{border-color:#F87171;background:#FEF2F2}.srch .em{display:none;color:#B91C1C;font-size:8.8px;position:absolute;top:35px;left:2px}.srch.err .em{display:block}'
 '.smp{font-size:9.6px;color:#71717A;white-space:nowrap}.sc{height:28px;padding:0 11px;border:1px solid #E4E4E7;border-radius:999px;background:#fff;font-family:"JetBrains Mono",ui-monospace,monospace;font-size:10.2px;cursor:pointer;transition:border-color .2s,background-color .2s}.sc:hover,.sc.fakehover{border-color:#18181B;background:#F4F4F5}.sc:focus-visible{outline:2px solid #18181B;outline-offset:1px}'
 '.empt.big{flex:1 1 0;padding-bottom:20px}'
 '.tabs{padding:0 2px}.fl{position:relative;display:grid;grid-template-columns:repeat(4,1fr);gap:26px;padding:12px 12px 14px}.fl svg.ln{position:absolute;left:0;top:0;width:100%;height:100%;pointer-events:none;overflow:visible}'
 '.col{display:flex;flex-direction:column;justify-content:center;gap:7px;position:relative;z-index:1}.col>small{font-size:8.6px;color:#A1A1AA;font-weight:500;text-align:center;margin-bottom:2px}'
 '.nd{border:1px solid #E4E4E7;border-radius:7px;background:#fff;padding:5px 8px;display:flex;flex-direction:column;gap:1px;text-align:left;font:inherit;color:#18181B;line-height:1.3;min-width:0;transition:box-shadow .2s,border-color .2s,opacity .3s}'
 '.nd small{font-size:8px;color:#71717A}.nd b{font-family:"JetBrains Mono",ui-monospace,monospace;font-size:10px;font-weight:600}.nd span{font-size:8.8px;color:#52525B;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}.nd em{font-style:normal;font-family:"JetBrains Mono",ui-monospace,monospace;font-size:9.2px;font-weight:600}'
 '.nd.ac{padding:4px 8px;flex-direction:row;align-items:center;justify-content:space-between;gap:6px}.nd.ac span{color:#18181B}.nd.root{border-color:#18181B;box-shadow:0 0 0 1px #18181B}'
 'button.nd{cursor:pointer}button.nd:hover,button.nd.fakehover{border-color:#18181B;box-shadow:0 0 0 1px #18181B}button.nd:focus-visible{outline:2px solid #18181B;outline-offset:1px}'
 '.ln path{fill:none;stroke:#A1A1AA;stroke-width:1.2}.ln path.hot{stroke:#18181B;stroke-width:1.6}'
 '.tl{display:grid;grid-template-columns:repeat(4,1fr);gap:8px}.tile{border:1px solid #E4E4E7;border-radius:8px;padding:7px 10px;display:flex;flex-direction:column;gap:1px;background:#fff}.tile small{font-size:8.8px;color:#71717A}.tile b{font-family:"JetBrains Mono",ui-monospace,monospace;font-size:15px;font-weight:600}'
 '.dt .row{grid-template-columns:90px 1fr 90px 70px;font-size:9.6px;white-space:nowrap}.dt .row span:nth-child(n+3){text-align:right}'
 '.rt .row{grid-template-columns:1fr 70px 62px 60px 66px;font-size:9.8px;min-height:30px;white-space:nowrap}.rt .row span:nth-child(n+2){text-align:right}.rt .row.tot{font-weight:600;background:#FAFAFA}.rt .row .mono{font-weight:500}'
 '.kg{display:grid;grid-template-columns:repeat(4,1fr);gap:8px 12px;padding:10px 11px}.note{border:1px solid #E4E4E7;background:#FAFAFA;border-radius:8px;padding:8px 10px;font-size:9.6px;line-height:1.45;color:#52525B}'
 '.vl{display:flex;flex-direction:column}.vl .vr{display:flex;align-items:center;justify-content:space-between;gap:8px;min-height:21px;padding:0 9px 0 22px;position:relative;font-size:10px;border-top:1px solid #F0F0F1;background:#fff;width:100%;font:inherit;font-size:10px;color:#18181B;border-left:0;border-right:0;border-bottom:0;text-align:left}'
 '.vl .vr::before{content:"";position:absolute;left:10px;top:0;bottom:0;width:1px;background:#D4D4D8}.vl .vr::after{content:"";position:absolute;left:7px;top:50%;width:7px;height:7px;margin-top:-3.5px;border-radius:50%;background:#fff;border:1.5px solid #71717A}.vl .vr:first-child{border-top:0}'
 '.vl .vr.k1{padding-left:34px}.vl .vr.k1::after{left:19px}.vl .vr.k2{padding-left:46px}.vl .vr.k2::after{left:31px}.vl .vr b{font-family:"JetBrains Mono",ui-monospace,monospace;font-size:10px}.vl .vr small{color:#71717A;font-size:9px;font-family:"JetBrains Mono",ui-monospace,monospace}'
 '.vl button.vr{min-height:40px;cursor:pointer}.vl button.vr:hover,.vl button.vr.fakehover{background:#F4F4F5}.vl button.vr:focus-visible{outline:2px solid #18181B;outline-offset:-2px}'
 '.shot.ph .sc{height:40px;padding:0 14px}.shot.ph .srch input{height:40px}.shot.ph .srch svg{top:14px}.shot.ph .bt.w{min-height:38px;width:100%;font-size:10.6px}.shot.ph .empt.big{padding:12px}'
 '.shot.ph .rt .row{grid-template-columns:1fr 54px;min-height:20px;font-size:10px}.shot.ph .rt button.row{min-height:38px}.shot.ph .rt .row span:nth-child(n+2):not(:last-child){display:none}'
 '.ph2{display:grid;grid-template-columns:1fr 1fr;gap:6px}.ph2 .tile{padding:5px 9px}.ph2 .tile b{font-size:12px}.shot.ph.nar .xn{display:none}'
)

WIN = ''

JS = r'''
var FOC='.rail .ni,.bc,.phd>*,.bn .bi,.pg .tile,.pg .ct,.pg .nd,.pg .col>small,.pg .row,.pg .tab,.pg .empt,.pg .smp,.pg .srch,.pg .sc,.pg .note,.pg .kv,.pg .vr,.pg .bt';
var ACC=[['Harbor Wine and Spirits','A',60,'Oct 9','SO-4471','Portland'],['Oakmont Bottle Shop','A',12,'Oct 10','SO-4475','Salem'],['Lantern Room Bar','A',8,'Oct 10','SO-4478','Eugene'],['Brightwater Liquors','B',30,'Oct 16','SO-4490','Bend'],['Ridgeway Beverage Supply','B',40,'Oct 17','SO-4493','Medford']];
var RUN={A:['BR-0921','Oct 7'],B:['BR-0928','Oct 14']};
var SRC=[['Botanical lot','BT-2209','Juniper berries'],['Botanical lot','CR-1180','Coriander seed'],['Spirit lot','NS-0731','Neutral grain spirit'],['Glass lot','GL-5521','750 ml bottles'],['Closure lot','CL-0907','Bar top corks']];
var S;
function cases(r){var t=0;ACC.forEach(function(a){if(!r||a[1]===r)t+=a[2];});return t;}
function nd(o){var t=o.btn?'button':'div';return '<'+t+(o.btn?' type="button"':'')+' class="nd'+(o.cls?' '+o.cls:'')+'" id="'+o.id+'">'+(o.k?'<small>'+o.k+'</small>':'')+'<b>'+o.b+'</b>'+(o.s?'<span>'+o.s+'</span>':'')+(o.q?'<em>'+o.q+'</em>':'')+'</'+t+'>';}
function acc(a,i){return '<div class="nd ac" id="n-a'+i+'"><span>'+a[0]+'</span><em>'+a[2]+'</em></div>';}
var EDGES={fwd:[['n-lot','n-gn'],['n-gn','n-ra'],['n-gn','n-rb'],['n-ra','n-a0'],['n-ra','n-a1'],['n-ra','n-a2'],['n-rb','n-a3'],['n-rb','n-a4']],
 back:[['n-s0','n-gn'],['n-s1','n-gn'],['n-s2','n-gn'],['n-s3','n-rb'],['n-s4','n-rb'],['n-gn','n-rb'],['n-rb','n-a3'],['n-rb','n-a4']]};
function links(){var fl=root.getElementById('fl');if(!fl)return;var sv=fl.querySelector('svg'),p='',F=fl.getBoundingClientRect(),k=F.width/fl.offsetWidth||1;function bx(e){var r=e.getBoundingClientRect();return{l:(r.left-F.left)/k,t:(r.top-F.top)/k,w:r.width/k,h:r.height/k};}
 (S.scr==='back'?EDGES.back:EDGES.fwd).forEach(function(e){var a=$(e[0]),b=$(e[1]);if(!a||!b)return;a=bx(a);b=bx(b);
  var x1=a.l+a.w,y1=a.t+a.h/2,x2=b.l,y2=b.t+b.h/2,m=(x1+x2)/2;
  var hot=S.scr==='back'||e[0]==='n-lot'||e[0]==='n-gn';p+='<path class="'+(hot?'hot':'')+'" d="M'+x1+' '+y1+'C'+m+' '+y1+' '+m+' '+y2+' '+x2+' '+y2+'"/>';});
 sv.innerHTML=p;}
function tabs(){return '<div class="tabs" role="tablist">'+[['fwd','Forward trace'],['back','Backward trace'],['recall','Recall lookup']].map(function(t){return '<button type="button" role="tab" class="tab'+(S.scr===t[0]?' on':'')+'" id="tb-'+t[0]+'" aria-selected="'+(S.scr===t[0])+'">'+t[1]+'</button>';}).join('')+'</div>';}
function top(){return '<div class="sbar"><label class="srch" style="max-width:170px"><svg width="13" height="13" viewBox="0 0 14 14" fill="none" aria-hidden="true"><circle cx="6" cy="6" r="4.2" stroke="#A1A1AA" stroke-width="1.4"/><path d="M9.2 9.2l3 3" stroke="#A1A1AA" stroke-width="1.4" stroke-linecap="round"/></svg><input value="BT-2209" aria-label="Lot" readonly></label><span class="grow"></span>'+tabs()+'</div>';}
function card(t,r,rows){return '<div class="cd dt"><div class="ct">'+t+'<span class="mut" style="font-weight:500">'+r+'</span></div>'+rows.map(function(x){return '<div class="row"><span>'+x[0]+'</span><span>'+x[1]+'</span><span class="mono">'+x[2]+'</span><span class="mono mut">'+x[3]+'</span></div>';}).join('')+'</div>';}
function render(){var P=ph(),h='',bc0=['Traceability',['Lot trace','cb-lt']];
if(S.scr==='search'){setNav({m:'trc',bc:['Traceability','Lot trace'],t:'Lot trace',scr:'Lot search'});
 h='<div class="frm sbar"><label class="srch" id="fs"><svg width="13" height="13" viewBox="0 0 14 14" fill="none" aria-hidden="true"><circle cx="6" cy="6" r="4.2" stroke="#A1A1AA" stroke-width="1.4"/><path d="M9.2 9.2l3 3" stroke="#A1A1AA" stroke-width="1.4" stroke-linecap="round"/></svg><input id="iq" placeholder="Type a lot, batch or run" value="'+S.v.q+'" autocomplete="off" aria-label="Lot, batch or run"><span class="em">No lot matches. Try BT-2209.</span></label>'+(P?'':'<span class="smp">Sample</span>')+'<button type="button" class="sc" id="smp">BT-2209</button></div>';
 h+='<div class="empt big"><b>Type a lot to trace it</b><span>'+(P?'Forward to every account, or back to every source lot.':'Forward from a lot to the batches, bottling runs and accounts it reached, or back from a bottling run to every lot that went into it.')+'</span></div>'+(P?'':card('Recent traces','Quality team',[['GN-112','Dry gin batch, mock recall drill','Forward','Nov 3'],['BR-0897','Barrel Rye bottling run','Backward','Oct 21'],['CR-1102','Coriander seed lot','Forward','Oct 9']]));}
else if(S.scr==='fwd'){setNav({m:'trc',bc:bc0.concat(['BT-2209']),t:'BT-2209',chip:['c-info','Forward'],scr:'Forward trace',back:1});
 if(P){h='<div class="cd vl"><div class="vr"><span>Lot <b>BT-2209</b></span><small>Juniper</small></div><div class="vr k1"><span>Batch <b>GN-118</b></span><small>'+cases()+' cases</small></div>'+
  '<div class="vr k2"><span>Run A <b>'+RUN.A[0]+'</b></span><small>'+cases('A')+' cases</small></div><div class="vr k2 xn"><span class="mut" style="font-size:9.2px">Accounts 60, 12, 8</span></div><button type="button" class="vr k2" id="n-rb"><span>Run B <b>'+RUN.B[0]+'</b></span><small>'+cases('B')+' cases</small></button></div><div class="ph2"><div class="tile"><small>Cases out</small><b id="f-cs">'+cases()+'</b></div><div class="tile"><small>Accounts</small><b>5</b></div></div>';}
 else{h=top()+'<div class="cd"><div class="fl" id="fl"><svg class="ln" aria-hidden="true"></svg><div class="col"><small>Lot</small>'+nd({id:'n-lot',k:'Botanical lot',b:'BT-2209',s:'Juniper berries',q:'40 kg',cls:'root'})+'</div><div class="col"><small>Batch</small>'+nd({id:'n-gn',k:'Gin batch',b:'GN-118',s:'Dry gin, distilled Sep 9',q:cases()+' cases'})+'</div>'+
  '<div class="col"><small>Bottling runs</small>'+nd({id:'n-ra',k:'Run A',b:RUN.A[0],s:'Bottled '+RUN.A[1],q:cases('A')+' cases'})+nd({id:'n-rb',k:'Run B',b:RUN.B[0],s:'Bottled '+RUN.B[1],q:cases('B')+' cases',btn:1})+'</div><div class="col"><small>Accounts</small>'+ACC.map(function(a,i){return acc(a,i);}).join('')+'</div></div></div>';
  h+='<div class="tl"><div class="tile"><small>Batches</small><b>1</b></div><div class="tile"><small>Bottling runs</small><b>2</b></div><div class="tile"><small>Cases shipped</small><b id="f-cs">'+cases()+'</b></div><div class="tile"><small>Accounts</small><b>5</b></div></div>';
  h+='<div class="cd dt"><div class="ct">Lot BT-2209<span class="mut" style="font-weight:500">Received Aug 4, 2026</span></div><div class="row"><span>Supplier</span><span>Northfield Botanicals</span><span class="mono">PO-3381</span><span class="mono mut">40 kg</span></div><div class="row"><span>Used in</span><span>Gin batch GN-118, dry gin</span><span class="mono">GN-118</span><span class="mono mut">40 kg</span></div></div>';}}
else if(S.scr==='back'){setNav({m:'trc',bc:bc0.concat([['BT-2209','cb-bt'],RUN.B[0]]),t:RUN.B[0],chip:['c-info','Backward'],scr:'Backward trace',back:1});
 if(P){h='<div class="cd vl"><div class="vr"><span>Run B <b>'+RUN.B[0]+'</b></span><small>'+cases('B')+' cases</small></div><div class="vr k1"><span>Batch <b>GN-118</b></span><small>Dry gin</small></div>'+SRC.slice(0,3).map(function(s,i){return '<div class="vr k2'+(i===1?' xn':'')+'"><span>'+s[2]+'</span><small>'+s[1]+'</small></div>';}).join('')+'<div class="vr k1 xn"><span>Glass and closures</span><small>2 lots</small></div></div><button type="button" class="bt w" id="tb-recall">Recall lookup for BT-2209</button>';}
 else{h=top()+'<div class="cd"><div class="fl" id="fl"><svg class="ln" aria-hidden="true"></svg><div class="col"><small>Source lots</small>'+SRC.map(function(s,i){return nd({id:'n-s'+i,k:s[0],b:s[1],s:s[2],cls:i===0?'root':''});}).join('')+'</div><div class="col"><small>Batch</small>'+nd({id:'n-gn',k:'Gin batch',b:'GN-118',s:'Dry gin, distilled Sep 9'})+'</div>'+
  '<div class="col"><small>Bottling run</small>'+nd({id:'n-rb',k:'Run B',b:RUN.B[0],s:'Bottled '+RUN.B[1],q:cases('B')+' cases',cls:'root'})+'</div><div class="col"><small>Accounts</small>'+ACC.map(function(a,i){return a[1]==='B'?acc(a,i):'';}).join('')+'</div></div></div>';
  h+='<div class="tl"><div class="tile"><small>Source lots</small><b>5</b></div><div class="tile"><small>Suppliers</small><b>4</b></div><div class="tile"><small>Run B cases</small><b id="b-cs">'+cases('B')+'</b></div><div class="tile"><small>Accounts</small><b>2</b></div></div>'+card('Run '+RUN.B[0],'Line 2',[['Bottled','Oct 14, 2026','','70 cases'],['Filled from','Gin batch GN-118','GN-118','420 bottles']]);}}
else if(S.scr==='recall'){setNav({m:'trc',bc:bc0.concat([['BT-2209','cb-bt'],'Recall lookup']),t:'Recall lookup, BT-2209',chip:['c-warn','5 accounts'],scr:'Recall list',back:1});
 var rows=ACC.map(function(a,i){var inner='<span>'+a[0]+'</span><span class="mut">'+a[5]+'</span><span class="mono">Run '+a[1]+'</span><span class="mono mut">'+a[3]+'</span><span class="mono">'+a[2]+'</span>';
  return i===0?'<button type="button" class="row" id="ac-0">'+inner+'</button>':'<div class="row">'+inner+'</div>';}).join('');
 h=(P?'':top())+'<div class="cd rt">'+(P?'':'<div class="ct">Accounts holding BT-2209<span class="mut" style="font-weight:500">Through GN-118, runs A and B</span></div>')+(P?'':'<div class="row h"><span>Account</span><span>City</span><span>Run</span><span>Shipped</span><span>Cases</span></div>')+rows+'<div class="row tot"><span>Total</span><span></span><span></span><span></span><span class="mono" id="r-tot">'+cases()+'</span></div></div>';
 if(!P)h+='<div class="tl"><div class="tile"><small>Run A</small><b id="r-a">'+cases('A')+'</b></div><div class="tile"><small>Run B</small><b id="r-b">'+cases('B')+'</b></div><div class="tile"><small>Cases out</small><b>'+cases()+'</b></div><div class="tile"><small>Still at the distillery</small><b>0</b></div></div>'+card('Other batches checked','Juniper lots by batch',[['GN-115','Dry gin, Aug 18','BT-2160','Not in scope'],['GN-121','Dry gin, Oct 2','BT-2241','Not in scope']]);}
else{var a=ACC[0];setNav({m:'trc',bc:bc0.concat([['Recall lookup','cb-rl'],a[0]]),t:a[0],chip:['c-warn','Holds BT-2209'],scr:'Account',back:1});
 if(P){h='<div class="ph2"><div class="tile"><small>Cases</small><b id="h-cs">'+a[2]+'</b></div><div class="tile"><small>Run</small><b>A</b></div><div class="tile"><small>Order</small><b style="font-size:11px">'+a[4]+'</b></div><div class="tile"><small>Shipped</small><b style="font-size:11px">'+a[3]+'</b></div></div>';}
 else{h='<div class="cd"><div class="kg">'+[['City',a[5]],['Buyer','Dana Whitfield'],['Phone','(503) 555 0142'],['Terms','Net 30']].map(function(x){return '<div class="kv"><small>'+x[0]+'</small><b>'+x[1]+'</b></div>';}).join('')+'</div></div>';
  h+='<div class="cd rt"><div class="ct">Orders since Sep 1<span class="mut" style="font-weight:500">1 holds the lot</span></div><div class="row h"><span>Item</span><span>Order</span><span>Run</span><span>Shipped</span><span>Cases</span></div>'+
  [['Dry gin 750 ml',a[4],'A',a[3],a[2],1],['Barrel Rye 750 ml','SO-4402','BR-0897','Sep 22',20,0],['Dry gin 750 ml','SO-4368','BR-0874','Sep 8',24,0]].map(function(x){return '<div class="row"><span>'+x[0]+(x[5]?' <span class="ch c-warn">BT-2209</span>':'')+'</span><span class="mono">'+x[1]+'</span><span class="mono">'+(x[5]?'Run A':x[2])+'</span><span class="mono mut">'+x[3]+'</span><span class="mono"'+(x[5]?' id="h-cs"':'')+'>'+x[4]+'</span></div>';}).join('')+'</div>';
  h+=card('Shipment '+a[4],'Warehouse A',[['Shipped','Oct 9, 2 pallets','','60 cases'],['Delivered','Oct 10, signed by D. Whitfield','','Portland']]);
  h+='<div class="note">Runs BR-0897 and BR-0874 used juniper lots BT-2160 and BT-2131, so only '+a[4]+' is in scope for BT-2209.</div>';}}
if(P&&S.scr!=='search')h+=xw(S.scr==='fwd'?[['Supplier','Northfield Botanicals'],['Received','Aug 4, 2026']]:S.scr==='back'?[['Glass and closure lots','GL-5521, CL-0907'],['Bottled','Oct 14, 2026']]:S.scr==='recall'?[['Run A','80 cases'],['Run B','70 cases']]:[['City','Portland'],['Buyer','Dana Whitfield'],['Delivered','Oct 10']]);
$('pg').innerHTML=h;links();}
$('pg').addEventListener('input',function(e){if(e.target.id==='iq'){S.v.q=e.target.value;$('fs').classList.remove('err');}});
if('ResizeObserver'in window)new ResizeObserver(function(){if(S)links();}).observe($('pg'));
function resetState(){S={scr:'search',v:{q:''}};render();}
function okQ(){var v=$('iq').value.trim(),b=v!==''&&!/^bt-?2209$/i.test(v);$('fs').classList.toggle('err',b);return !b;}
function typeIn(done){var inp=$('iq'),s='BT-2209',i=0;if(!inp||/^bt-?2209$/i.test(inp.value.trim())){done();return;}(function t(){inp.value=s.slice(0,++i);if(i<s.length)later(t,60);else later(done,160);})();}
var CAPAT=function(hh){return ph()?{l:8,t:5}:{l:14,t:visH()-hh-40};};
var ST=[
{id:'lot',target:function(){return $('smp');},prompt:'Click the sample, or type BT-2209 and press Enter',where:'below',ok:okQ,run:function(q){var go=function(){S.v.q='BT-2209';S.scr='fwd';render();};if(q)go();else typeIn(go);},
 after:['The full trace on one screen','BT-2209 went into gin batch GN-118, bottled in two runs: A 80 cases, B 70 cases. 150 cases at five accounts.'],pc:'BT-2209: 150 cases, 5 accounts'},
{id:'runb',target:function(){return $('n-rb');},prompt:'Follow run B back to its source lots',where:function(){return ph()?'above':'below';},run:function(){S.scr='back';render();},
 after:['Run B traced back to its source lots','BR-0928, 70 cases, came from gin batch GN-118: juniper BT-2209, coriander CR-1180 and spirit NS-0731, plus its glass and closure lots.'],pc:'Run B back to five source lots'},
{id:'recall',target:function(){return $('tb-recall');},prompt:'Open the recall lookup',where:'below',run:function(){S.scr='recall';render();},
 after:['Every account that holds the lot','Five accounts: 60, 12 and 8 cases from run A, 30 and 40 from run B. 150 cases in all.'],pc:'Five accounts, 150 cases'},
{id:'acct',target:function(){return $('ac-0');},prompt:'Open Harbor Wine and Spirits',where:'below',run:function(){S.scr='acct';render();},
 after:['One account, down to the order','Harbor Wine and Spirits took 60 cases of run A on SO-4471, shipped Oct 9.'],pc:'Harbor: 60 cases on SO-4471'}];
ST.forEach(function(s){['prompt','where'].forEach(function(k){if(typeof s[k]==='function'){var f=s[k];Object.defineProperty(s,k,{get:f});}});});
'''
