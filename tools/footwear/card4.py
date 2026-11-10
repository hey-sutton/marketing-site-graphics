"""Footwear card 4: Cost per Pair & Margin. A stacked bar chart with a table inside the app shell: an empty style picker,
the cost stack per size (material, labor, overhead, landed) with size 9 selected, the landed cost screen that spreads a
receipt's freight and duties across its pairs, back to costing, quoted against actual with the variance per size, then
margin by channel. All money is computed in cents; percentages are rounded half up to one decimal."""
SUMMARY = 'Cost per Pair & Margin (a style picked into an empty picker, cost per pair stacked by size, the landed cost spread from a receipt, quoted against actual cost with the variance per size, margin by channel)'
ARIA = 'Interactive product screen: pick style HR-210, open the landed cost of size 9, go back to costing, compare quoted and actual cost, then switch the margin from wholesale to direct'
STEPS = 5
STUDIO = dict(lede='A typical cost and margin screen, built on your Sutton data with Studio. Want it different? Describe the change.',
              examples=['Add a duty rate table by material', 'Change the overhead allocation rule', 'Add a margin floor alert by channel', 'Build a quote approval screen'],
              built_on='BOMs, routings, receipts and price lists', change='Cost rules, fields and views')
STORY = [('Cost by size', 'cst', 'sample chip', 'top left'), ('Cost by size', 'cst', 'chart segment', 'center'),
         ('Landed cost', 'pur', 'nav item', 'left'), ('Cost by size', 'cst', 'tab', 'top right'),
         ('Quote variance', 'cst', 'channel chip', 'bottom')]

CSS = (
 '.sbar{display:flex;align-items:center;gap:8px}.srch{flex:1;position:relative;display:flex;flex-direction:column;gap:3px}.srch input{font:inherit;font-family:"JetBrains Mono",ui-monospace,monospace;font-size:11px;height:32px;padding:0 10px 0 30px;border:1px solid #D4D4D8;border-radius:7px;background:#fff;color:#18181B;width:100%}'
 '.srch input::placeholder{font-family:Inter,sans-serif;color:#A1A1AA}.srch input:focus-visible{outline:2px solid #18181B;outline-offset:1px}.srch svg{position:absolute;left:10px;top:10px}.srch.err input{border-color:#F87171;background:#FEF2F2}.srch .em{display:none;color:#B91C1C;font-size:8.8px;position:absolute;top:35px;left:2px}.srch.err .em{display:block}'
 '.smp{font-size:9.6px;color:#71717A}.sc{height:26px;padding:0 10px;border:1px solid #E4E4E7;border-radius:999px;background:#fff;font-family:"JetBrains Mono",ui-monospace,monospace;font-size:10px;cursor:pointer;transition:border-color .2s,background-color .2s}.sc:hover,.sc.fakehover{border-color:#18181B;background:#F4F4F5}'
 '.gax{flex:none;height:262px;border:1px dashed #E4E4E7;border-radius:8px;background:#FAFAFA;position:relative;display:flex;align-items:center;justify-content:center}.gax i{position:absolute;left:14px;right:14px;height:1px;background:#EDEDEF}.gax .msg{position:relative;background:#fff;border:1px solid #E4E4E7;border-radius:8px;padding:10px 14px;text-align:center;display:flex;flex-direction:column;gap:3px;width:270px}.gax .msg b{font-size:10.8px}.gax .msg span{font-size:9.4px;color:#71717A}'
 '.hdr{display:flex;align-items:center;gap:10px}.hdr .nm{display:flex;flex-direction:column;line-height:1.25}.hdr .nm b{font-size:12px}.hdr .nm small{font-size:9px;color:#71717A}'
 '.tabs.t2{height:28px;padding:0;gap:14px;border-bottom:0}.tabs.t2 .tab{padding-bottom:7px}'
 '.cw{display:grid;grid-template-columns:1fr 160px;gap:10px}.ch2{border:1px solid #E4E4E7;border-radius:8px;padding:10px 12px 8px 34px;position:relative;height:236px}'
 '.yl{position:absolute;left:0;right:12px;height:1px;background:#F0F0F1}.yl span{position:absolute;left:6px;top:-6px;font-family:"JetBrains Mono",ui-monospace,monospace;font-size:8px;color:#A1A1AA}'
 '.bars{position:absolute;left:34px;right:12px;top:10px;bottom:24px;display:flex;align-items:flex-end;justify-content:space-around}.bc2{width:40px;display:flex;flex-direction:column-reverse;align-items:stretch;position:relative;transition:opacity .3s}.bc2.dim{opacity:.4}'
 '.sg2{display:block;border:0;padding:0;width:100%;transform-origin:bottom;animation:grow .7s cubic-bezier(.22,.9,.28,1) both}@keyframes grow{from{transform:scaleY(0)}}.s-m{background:#3F3F46}.s-l{background:#71717A}.s-o{background:#A1A1AA}.s-d{background:#D4D4D8;border-radius:4px 4px 0 0}'
 'button.sg2{cursor:pointer}button.sg2:hover,button.sg2.fakehover{box-shadow:0 0 0 2px #18181B;position:relative;z-index:1}button.sg2:focus-visible{outline:2px solid #18181B;outline-offset:1px}'
 '.bc2 .tv{position:absolute;left:-10px;right:-10px;text-align:center;font-family:"JetBrains Mono",ui-monospace,monospace;font-size:9px;font-weight:600}.bc2 .xl{position:absolute;left:0;right:0;bottom:-17px;text-align:center;font-size:9px;color:#71717A}.bc2.sel .xl{color:#18181B;font-weight:600}'
 '.qline{position:absolute;left:34px;right:12px;border-top:1.5px dashed #18181B;z-index:2}.qline span{position:absolute;right:0;top:-15px;font-size:8.6px;background:#fff;padding:0 4px;font-family:"JetBrains Mono",ui-monospace,monospace}'
 '.bk2{border:1px solid #E4E4E7;border-radius:8px;display:flex;flex-direction:column}.bk2 .row{grid-template-columns:12px 1fr 44px;font-size:9.8px;min-height:28px}.bk2 .row span:last-child{text-align:right}.bk2 .row.t{font-weight:600;background:#FAFAFA}.dot{width:9px;height:9px;border-radius:3px}'
 '.ct2 .row{grid-template-columns:40px repeat(5,1fr);font-size:9.8px;min-height:24px;white-space:nowrap}.ct2 .row span:nth-child(n+2){text-align:right}.ct2 .row.sel{background:#F4F4F5;box-shadow:inset 3px 0 0 #18181B}'
 '.qv .row{grid-template-columns:40px repeat(5,1fr);font-size:9.8px;min-height:26px;white-space:nowrap}.qv .row span:nth-child(n+2){text-align:right}.qv .row.sel{background:#F4F4F5;box-shadow:inset 3px 0 0 #18181B}.up{color:#B91C1C}.dn2{color:#166534}'
 '.chs{display:flex;gap:6px;align-items:center}.fc{height:24px;border:1px solid #E4E4E7;border-radius:999px;background:#fff;padding:0 11px;font-size:9.6px;cursor:pointer;transition:background-color .2s,border-color .2s,color .2s}.fc.on{background:#18181B;border-color:#18181B;color:#fff}.fc:hover,.fc.fakehover{border-color:#18181B}.fc:focus-visible{outline:2px solid #18181B;outline-offset:1px}'
 '.tl{display:grid;grid-template-columns:repeat(4,1fr);gap:8px}.tile{border:1px solid #E4E4E7;border-radius:8px;padding:7px 10px;display:flex;flex-direction:column;gap:1px}.tile small{font-size:8.8px;color:#71717A}.tile b{font-family:"JetBrains Mono",ui-monospace,monospace;font-size:14px;font-weight:600}'
 '.sp2 .row{grid-template-columns:40px repeat(4,1fr);font-size:9.8px;min-height:26px;white-space:nowrap}.sp2 .row span:nth-child(n+2){text-align:right}.row.t{font-weight:600;background:#FAFAFA}.sp2 .row.sel{background:#F4F4F5}'
 '.note{border:1px solid #E4E4E7;background:#FAFAFA;border-radius:8px;padding:8px 10px;font-size:9.8px;line-height:1.45}'
 '.shot.ph.nar .ch2{height:124px}.shot.ph .ch2{height:132px;padding:6px 8px 6px 8px}.shot.ph .bars{left:8px;right:8px;top:14px;bottom:18px}.shot.ph .bc2{width:28px}.shot.ph .yl{display:none}.shot.ph .qline{left:8px;right:8px}.shot.ph .tile{padding:5px 9px}.shot.ph .tile b{font-size:12.5px}'
 '.shot.ph .sc{height:30px;padding:0 12px}.shot.ph .srch input{height:34px}.shot.ph .fc{height:30px;padding:0 13px}.shot.ph .tabs.t2 .tab{padding:6px 2px 7px}'
 '.shot.ph button.s-d{position:relative}.shot.ph button.s-d::after{content:"";position:absolute;left:-5px;right:-5px;top:-8px;bottom:-6px}.ph-g .row{grid-template-columns:52px repeat(6,1fr);min-height:24px;font-size:9.6px;white-space:nowrap;padding:0 8px;gap:4px}.ph-g .row span:nth-child(n+2){text-align:right}.ph2{display:grid;grid-template-columns:1fr 1fr;gap:8px}'
)

WIN = ''

JS = r'''
var FOC='.rail .ni,.bc,.phd>*,.bn .bi,.pg .tile,.pg .ct,.pg .row,.pg .sbar>*,.pg .gax,.pg .hdr>*,.pg .ch2,.pg .bk2,.pg .note,.pg .chs>*,.pg .empt,.pg .tabs .tab';
var SZ=[7,8,9,10,11,12],MAT=[1640,1740,1840,1940,2040,2140],LAB=680,OVH=310,FRT=140,DUT=100,QUO=2950,PRICE={wh:5200,dr:7800};
var RCP=[60,90,120,110,85,60],RFRT=73500,RDUT=52500;
var S;
function c2(c){return (c/100).toFixed(2);}
function sg(c){return (c>0?'+':c<0?'-':'')+c2(Math.abs(c));}
function lnd(){return FRT+DUT;}
function tot(i){return MAT[i]+LAB+OVH+lnd();}
function pct(n,d){return (Math.round(n*1000/d)/10).toFixed(1);}
function mg(i){var p=PRICE[S.ch];return pct(p-tot(i),p);}
function vr(i){return tot(i)-QUO;}
function rpairs(){var t=0;RCP.forEach(function(x){t+=x;});return t;}
function ico(){return '<svg width="13" height="13" viewBox="0 0 14 14" fill="none" aria-hidden="true"><circle cx="6" cy="6" r="4.2" stroke="#A1A1AA" stroke-width="1.4"/><path d="M9.2 9.2l3 3" stroke="#A1A1AA" stroke-width="1.4" stroke-linecap="round"/></svg>';}
function chart(P,q){var H=P?100:200,mx=3600,h='<div class="ch2">';if(!P)[0,1000,2000,3000].forEach(function(v){h+='<div class="yl" style="bottom:'+(24+v/mx*H)+'px"><span>'+(v/100)+'</span></div>';});
 h+='<div class="bars">'+SZ.map(function(s,i){var parts=[['m',MAT[i]],['l',LAB],['o',OVH],['d',lnd()]];return '<div class="bc2'+(i===2?' sel':(q?'':' dim'))+'" style="height:'+(tot(i)/mx*H)+'px">'+parts.map(function(p,k){var st='height:'+(p[1]/tot(i)*100)+'%;animation-delay:'+(i*60+k*40)+'ms';return p[0]==='d'?'<button type="button" class="sg2 s-d" id="seg-d-'+s+'" style="'+st+'" aria-label="Landed cost, size '+s+'"></button>':'<span class="sg2 s-'+p[0]+'" style="'+st+'"></span>';}).join('')+
 '<span class="tv'+(q?(vr(i)>0?' up':' dn2'):'')+'" style="top:-14px">'+(q?sg(vr(i)):c2(tot(i)))+'</span><span class="xl">'+s+'</span></div>';}).join('')+'</div>';
 if(q)h+='<div class="qline" style="bottom:'+((P?18:24)+QUO/mx*H)+'px"><span>Quoted '+c2(QUO)+'</span></div>';
 return h+'</div>';}
function tabs(){return '<div class="tabs t2">'+[['cs','Cost stack'],['qa','Quoted vs actual']].map(function(x){return '<button type="button" class="tab'+((S.scr==='qv')===(x[0]==='qa')?' on':'')+'" id="tb-'+x[0]+'">'+x[1]+'</button>';}).join('')+'</div>';}
function render(){var P=ph(),h='',scr=S.scr;
if(scr==='pick'){setNav({m:'cst',bc:['Costing','Cost per pair'],t:'Cost per pair',scr:'Cost by size'});
 h='<div class="frm sbar"><label class="srch" id="fs">'+ico()+'<input id="iq" placeholder="Pick a style" value="'+S.v.q+'" autocomplete="off" aria-label="Pick a style"><span class="em">No style matches. Try HR-210.</span></label>'+(P?'':'<span class="smp">Try</span>')+'<button type="button" class="sc" id="smp">HR-210</button></div>';
 if(P)h+='<div class="empt" style="padding:14px"><b>Pick a style to see its cost per pair</b><span>Material, labor, overhead and landed cost for every size.</span></div>';
 else{h+='<div class="gax"><i style="top:25%"></i><i style="top:50%"></i><i style="top:75%"></i><div class="msg"><b>Pick a style to see its cost per pair</b><span>Material, labor, overhead and landed cost stacked for every size, next to the quoted cost.</span></div></div>';
  h+='<div class="cd" style="flex:1 1 0"><div class="ct">Cost rules<span class="mut" style="font-weight:500">Apply to every style</span></div>'+[['Material','From the BOM, at the last receipt price'],['Labor','Routing minutes at the stage rate'],['Overhead','Spread by labor minutes'],['Landed','Freight and duties spread by pairs on the receipt'],['Price lists','Wholesale and Direct'],['Quotes','Quoted cost per pair, kept with each style'],['Seconds','Priced on the outlet list']].map(function(x){return '<div class="row" style="grid-template-columns:90px 1fr;font-size:9.8px"><span>'+x[0]+'</span><span class="mut">'+x[1]+'</span></div>';}).join('')+'</div>';}}
else if(scr==='cost'){setNav({m:'cst',bc:['Costing','Cost per pair','HR-210'],t:'Harbor Runner HR-210',chip:['c-info','Size 9: '+c2(tot(2))],scr:'Cost by size'});
 if(P){h='<div class="hdr"><span class="nm grow"><b>Size 9: '+c2(tot(2))+'</b><small>Landed '+c2(lnd())+'</small></span>'+tabs()+'</div>'+chart(P,false);}
 else{h='<div class="hdr"><span class="nm grow"><b>HR-210, Harbor Runner</b><small>Black, sizes 7 to 12, cost per pair</small></span>'+tabs()+'</div>';
  h+='<div class="cw">'+chart(P,false)+'<div class="bk2"><div class="ct">Size 9, per pair</div>'+[['Material','#3F3F46',MAT[2]],['Labor','#71717A',LAB],['Overhead','#A1A1AA',OVH],['Landed','#D4D4D8',lnd()]].map(function(x){return '<div class="row"><i class="dot" style="background:'+x[1]+'"></i><span>'+x[0]+'</span><span class="mono">'+c2(x[2])+'</span></div>';}).join('')+'<div class="row t"><span></span><span>Total</span><span class="mono" id="t9">'+c2(tot(2))+'</span></div><div class="row" style="grid-template-columns:1fr;color:#71717A;font-size:9px;flex:1;align-items:end;padding-bottom:6px">Click a landed segment for the receipt</div></div></div>';
  h+='<div class="cd ct2"><div class="row h"><span>Size</span><span>Material</span><span>Labor</span><span>Overhead</span><span>Landed</span><span>Total</span></div>'+SZ.map(function(s,i){return '<div class="row'+(i===2?' sel':'')+'"><span class="mono">'+s+'</span><span class="mono">'+c2(MAT[i])+'</span><span class="mono">'+c2(LAB)+'</span><span class="mono">'+c2(OVH)+'</span><span class="mono">'+c2(lnd())+'</span><span class="mono" id="tt-'+s+'">'+c2(tot(i))+'</span></div>';}).join('')+'</div>';}}
else if(scr==='land'){setNav({m:'pur',bc:['Purchasing','Receipts','RC-7720'],t:'Landed cost, RC-7720',chip:['c-ok','Spread'],scr:'Landed cost',back:1});
 var tc=RFRT+RDUT,np=rpairs();
 h='<div class="tl" style="'+(P?'grid-template-columns:1fr 1fr':'')+'"><div class="tile"><small>Pairs on the receipt</small><b id="lp">'+np+'</b></div><div class="tile"><small>Freight</small><b id="lf">'+m2(RFRT/100)+'</b></div><div class="tile"><small>Duties</small><b id="ld">'+m2(RDUT/100)+'</b></div><div class="tile"><small>Per pair</small><b id="lpp">'+c2(tc/np)+'</b></div></div>'+(P?'<div class="cd ph-g"><div class="row" style="grid-template-columns:1fr auto"><span>'+c2(RFRT/np)+' freight plus '+c2(RDUT/np)+' duties</span><span class="mono">'+c2(tc/np)+'</span></div></div>':'');
 if(!P){h+='<div class="note">Freight '+m2(RFRT/100)+' plus duties '+m2(RDUT/100)+' is '+m2(tc/100)+' for the receipt. Spread over '+np+' pairs that is '+c2(RFRT/np)+' freight and '+c2(RDUT/np)+' duties, '+c2(tc/np)+' a pair, on every size.</div>';
  h+='<div class="cd sp2"><div class="ct">Spread by size<span class="mut" style="font-weight:500">HR-210 Black, received 11/04</span></div><div class="row h"><span>Size</span><span>Pairs</span><span>Freight</span><span>Duties</span><span>Landed</span></div>'+SZ.map(function(s,i){var p=RCP[i];return '<div class="row'+(i===2?' sel':'')+'"><span class="mono">'+s+'</span><span class="mono">'+p+'</span><span class="mono">'+m2(p*FRT/100)+'</span><span class="mono">'+m2(p*DUT/100)+'</span><span class="mono">'+m2(p*lnd()/100)+'</span></div>';}).join('')+
  '<div class="row t"><span>All</span><span class="mono">'+np+'</span><span class="mono">'+m2(np*FRT/100)+'</span><span class="mono">'+m2(np*DUT/100)+'</span><span class="mono" id="lt">'+m2(np*lnd()/100)+'</span></div></div>';
  h+='<div class="cd" style="flex:1 1 0"><div class="ct">Receipt RC-7720</div><div class="row" style="grid-template-columns:1fr auto;font-size:9.8px"><span>Bill of lading BL-20981, ocean freight</span><span class="mono">'+m2(RFRT/100)+'</span></div><div class="row" style="grid-template-columns:1fr auto;font-size:9.8px"><span>Duty entry DE-4471</span><span class="mono">'+m2(RDUT/100)+'</span></div></div>';}}
else{var ch=S.ch;setNav({m:'cst',bc:['Costing','Cost per pair',['HR-210','cb-st'],'Quoted vs actual'],t:'Harbor Runner HR-210',chip:['c-warn','Size 9 over quote by '+pct(vr(2),QUO)+'%'],scr:'Quote variance'});
 var chips='<div class="chs">'+(P?'':'<span class="mut" style="font-size:9.4px">Margin for</span>')+[['wh','Wholesale',PRICE.wh],['dr','Direct',PRICE.dr]].map(function(x){return '<button type="button" class="fc'+(ch===x[0]?' on':'')+'" id="ch-'+x[0]+'" aria-pressed="'+(ch===x[0])+'">'+x[1]+(P?'':' at '+c2(x[2]))+'</button>';}).join('')+'</div>';
 if(P){h=chips+'<div class="cd ph-g"><div class="row h"><span>Size</span>'+SZ.map(function(s){return '<span>'+s+'</span>';}).join('')+'</div><div class="row"><span>Actual</span>'+SZ.map(function(s,i){return '<span class="mono">'+c2(tot(i)).replace(/\.\d0$/,function(m){return m;})+'</span>';}).join('')+'</div><div class="row"><span>Variance</span>'+SZ.map(function(s,i){return '<span class="mono '+(vr(i)>0?'up':'dn2')+'">'+sg(vr(i))+'</span>';}).join('')+'</div><div class="row"><span>Margin</span>'+SZ.map(function(s,i){return '<span class="mono" id="mg-'+s+'">'+mg(i)+'</span>';}).join('')+'</div></div>';}
 else{h='<div class="hdr"><span class="nm grow"><b>HR-210, Harbor Runner</b><small>Quoted '+c2(QUO)+' a pair for every size</small></span>'+tabs()+'</div>'+chart(P,true).replace('height:236px','height:206px');
  h+='<div class="cd qv"><div class="ct">Quoted vs actual, and margin'+chips+'</div><div class="row h"><span>Size</span><span>Actual</span><span>Quoted</span><span>Variance</span><span>Of quoted</span><span>Margin, '+(ch==='wh'?'wholesale':'direct')+'</span></div>'+SZ.map(function(s,i){return '<div class="row'+(i===2?' sel':'')+'"><span class="mono">'+s+'</span><span class="mono">'+c2(tot(i))+'</span><span class="mono">'+c2(QUO)+'</span><span class="mono '+(vr(i)>0?'up':'dn2')+'" id="vr-'+s+'">'+sg(vr(i))+'</span><span class="mono">'+pct(vr(i),QUO)+'%</span><span class="mono" id="mg-'+s+'">'+mg(i)+'%</span></div>';}).join('')+'</div>';}}
$('pg').innerHTML=h;}
$('pg').addEventListener('input',function(e){if(e.target.id==='iq'){S.v.q=e.target.value;$('fs').classList.remove('err');}});
function resetState(){S={scr:'pick',ch:'wh',v:{q:''}};render();}
function okQ(){var v=$('iq').value.trim(),b=v!==''&&!/^hr-?210$/i.test(v);$('fs').classList.toggle('err',b);return !b;}
function typeIn(done){var inp=$('iq'),s='HR-210',k=0;if(!inp||/^hr-?210$/i.test(inp.value.trim())){done();return;}(function t(){inp.value=s.slice(0,++k);if(k<s.length)later(t,55);else later(done,120);})();}
var CAPAT=function(hh){return ph()?{l:8,t:5}:{l:14,t:visH()-hh-40};};
var ST=[
{id:'pick',target:function(){return $('smp');},prompt:'Click the sample HR-210, or type it and press Enter',where:'below',ok:okQ,run:function(q){var go=function(){S.v.q='HR-210';S.scr='cost';render();};if(q)go();else typeIn(go);},
 after:function(){return['Cost per pair stacks up for every size','Material, labor, overhead and landed. Size 9 comes to '+c2(tot(2))+' a pair, '+c2(tot(0))+' to '+c2(tot(5))+' across the run.'];},pc:'Cost per pair for every size'},
{id:'seg',target:function(){return $('seg-d-9');},prompt:'Click the landed cost on size 9',where:'right',run:function(){S.scr='land';render();},
 after:function(){return['Landed cost comes from the receipt',m2(RFRT/100)+' freight and '+m2(RDUT/100)+' duties over '+rpairs()+' pairs: '+c2(lnd())+' a pair.'];},pc:'2.40 landed, spread from the receipt'},
{id:'nav',target:function(){return $(ph()?'bn-cst':'nv-cst');},prompt:'Click Costing',where:'right',run:function(){S.scr='cost';render();},
 after:['Back to the cost stack for HR-210','The landed segment on every size is the 2.40 spread from receipt RC-7720.'],pc:'Back to the cost stack'},
{id:'qa',target:function(){return $('tb-qa');},prompt:'Click Quoted vs actual',where:'below',run:function(){S.scr='qv';render();},
 after:function(){return['Quoted cost sits next to actual cost','Quoted '+c2(QUO)+' for every size. Size 9 is '+c2(tot(2))+', '+sg(vr(2))+' or '+pct(vr(2),QUO)+'% over quote.'];},pc:'Size 9 is 1.20 over the quote'},
{id:'ch',target:function(){return $('ch-dr');},prompt:'Switch the margin to Direct',where:'above',run:function(){S.ch='dr';render();},
 after:function(){var w=pct(PRICE.wh-tot(2),PRICE.wh);return['Margin changes by channel','Size 9 at '+c2(tot(2))+': wholesale '+c2(PRICE.wh)+' gives '+w+'%, direct '+c2(PRICE.dr)+' gives '+mg(2)+'%.'];},pc:'Direct margin on size 9: 60.6%'}];
'''
