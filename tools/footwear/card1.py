"""Footwear card 1: Size & Color Matrix Inventory. A grid inside the app shell: an empty style search, the HR-210 size and
color matrix (colors by sizes 7 to 12, Regular and Wide), the shortage detail for Black size 9 Regular with the BOM behind
it, the purchase order for the short leather, then back to the grid with PO raised, and the Wide grid.
Counts are whole pairs; leather is in square feet to one decimal."""
SUMMARY = 'Size & Color Matrix Inventory (a style typed into an empty search, the size and color matrix with on hand, committed and available, a short cell opened to the materials behind it, the leather purchase order, the Wide grid)'
ARIA = 'Interactive product screen: search style HR-210, open the short Black size 9 Regular cell, raise a purchase order for 25.0 square feet of black leather from Ridgeline Tannery, then switch the grid to Wide'
STEPS = 5
STUDIO = dict(lede='A typical size and color matrix, built on your Sutton data with Studio. Want it different? Describe the change.',
              examples=['Add a width dimension to the grid', 'Color code cells by sell through', 'Add a reorder alert by size', 'Export the grid to a retailer order sheet'],
              built_on='Styles, variants, BOMs and orders', change='Dimensions, fields and views')
# storyboard: screen, module, target type, position (the variety test reads this and checks the built card against it)
STORY = [('Style search', 'inv', 'sample chip', 'top left'), ('Size matrix', 'inv', 'grid cell', 'center'),
         ('Shortage detail', 'inv', 'row button', 'right'), ('Purchase order', 'pur', 'primary button', 'bottom right'),
         ('Size matrix', 'inv', 'segmented toggle', 'top right')]

CSS = (
 '.sbar{display:flex;align-items:center;gap:8px}.srch{flex:1;position:relative;display:flex;flex-direction:column;gap:3px}.srch input{font:inherit;font-family:"JetBrains Mono",ui-monospace,monospace;font-size:11px;height:32px;padding:0 10px 0 30px;border:1px solid #D4D4D8;border-radius:7px;background:#fff;color:#18181B;width:100%}'
 '.srch input::placeholder{font-family:Inter,sans-serif;color:#A1A1AA}.srch input:focus-visible{outline:2px solid #18181B;outline-offset:1px}.srch svg{position:absolute;left:10px;top:10px}.srch.err input{border-color:#F87171;background:#FEF2F2}.srch .em{display:none;color:#B91C1C;font-size:8.8px;position:absolute;top:35px;left:2px}.srch.err .em{display:block}'
 '.smp{display:flex;align-items:center;gap:6px;font-size:9.6px;color:#71717A;white-space:nowrap}.sc{height:26px;padding:0 10px;border:1px solid #E4E4E7;border-radius:999px;background:#fff;font-family:"JetBrains Mono",ui-monospace,monospace;font-size:10px;cursor:pointer;transition:border-color .2s,background-color .2s}.sc:hover,.sc.fakehover{border-color:#18181B;background:#F4F4F5}'
 '.empt.big{flex:1 1 0;padding-bottom:70px;position:relative}.empt .ft{position:absolute;left:0;right:0;bottom:84px;font-size:9px;color:#A1A1AA}'
 '.tbr{display:flex;align-items:center;gap:10px}.tbr .nm{display:flex;flex-direction:column;gap:1px;line-height:1.25}.tbr .nm b{font-size:12px}.tbr .nm small{font-size:9px;color:#71717A}'
 '.seg{display:inline-flex;padding:2px;gap:2px;border:1px solid #E4E4E7;border-radius:7px;background:#FAFAFA}.sg{height:24px;padding:0 11px;border:0;border-radius:5px;background:transparent;font-size:10px;color:#52525B;cursor:pointer;transition:background-color .2s,color .2s}.sg.on{background:#fff;color:#18181B;font-weight:600;box-shadow:0 0 0 1px #E4E4E7}.sg.fakehover,.sg:hover{color:#18181B}.sg:focus-visible,.gc:focus-visible{outline:2px solid #18181B;outline-offset:1px}'
 '.tl{display:grid;grid-template-columns:repeat(4,1fr);gap:8px}.tile{border:1px solid #E4E4E7;border-radius:8px;padding:7px 10px;display:flex;flex-direction:column;gap:1px}.tile small{font-size:8.8px;color:#71717A}.tile b{font-family:"JetBrains Mono",ui-monospace,monospace;font-size:15px;font-weight:600}.tile.bad b{color:#B91C1C}'
 '.mx{border:1px solid #E4E4E7;border-radius:8px;overflow:hidden}.gr{display:grid;grid-template-columns:84px repeat(6,1fr) 54px;gap:4px;padding:4px 8px;align-items:center}.gr.h{background:#FAFAFA;color:#71717A;font-size:9.2px;font-weight:500;padding:5px 8px}.gr.h span{text-align:center}.gr.h span:first-child{text-align:left}'
 '.gr+.gr{border-top:1px solid #F0F0F1}.cl{display:flex;align-items:center;gap:6px;font-size:10px;font-weight:500}.sw{width:10px;height:10px;border-radius:3px;flex:none;border:1px solid rgba(0,0,0,.12)}'
 '.gc{height:42px;border:1px solid #F0F0F1;border-radius:6px;background:#fff;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:1px;padding:0;font:inherit;color:#18181B;position:relative;transition:box-shadow .2s,background-color .3s}'
 '.gc b{font-family:"JetBrains Mono",ui-monospace,monospace;font-size:13px;font-weight:600;line-height:1.1}.gc small{font-family:"JetBrains Mono",ui-monospace,monospace;font-size:8px;color:#A1A1AA}button.gc{cursor:pointer}button.gc:hover,button.gc.fakehover{box-shadow:0 0 0 2px #18181B}'
 '.gc.short{background:#FEF2F2;border-color:#FECACA}.gc.short b{color:#B91C1C}.gc.low::after{content:"";position:absolute;right:4px;top:4px;width:5px;height:5px;border-radius:50%;background:#F59E0B}.gc .po{position:absolute;left:2px;right:2px;bottom:2px;font-size:7.6px;font-weight:600;color:#1E3A8A;background:#E8EEFC;border-radius:3px;line-height:1.5}.gc.has-po small{visibility:hidden}'
 '.tot{text-align:right;font-family:"JetBrains Mono",ui-monospace,monospace;font-size:10.5px;font-weight:600}.gr.sub{font-size:9px;color:#71717A;min-height:24px}.gr.sub span{text-align:center;font-family:"JetBrains Mono",ui-monospace,monospace}.gr.sub span:first-child{text-align:left;font-family:Inter,sans-serif}'
 '.lgd{display:flex;align-items:center;gap:12px;font-size:8.8px;color:#71717A;white-space:nowrap}.lgd i{display:inline-block;width:9px;height:9px;border-radius:3px;margin-right:4px;vertical-align:-1px}'
 '.ord .row{grid-template-columns:62px 1fr 74px 58px;font-size:9.8px;white-space:nowrap}.ord .row span:nth-child(n+3){text-align:right}'
 '.mt .row{grid-template-columns:1fr 46px 50px 54px 214px;font-size:9.8px;min-height:32px;white-space:nowrap}.mt .row span:nth-child(n+2){text-align:right}.mt .row.bad{background:#FFFBFB}'
 '.mkp{height:24px;padding:0 9px;border:1px solid #18181B;border-radius:6px;background:#fff;font-size:9.6px;font-weight:500;cursor:pointer;margin-left:6px}.mkp:hover,.mkp.fakehover{background:#F4F4F5}'
 '.two{display:grid;grid-template-columns:1fr 1fr;gap:10px;flex:1 1 0;min-height:0}.two .cd .row{grid-template-columns:62px 1fr 60px;font-size:9.8px;white-space:nowrap}.two .cd .row span:last-child{text-align:right}'
 '.note{border:1px solid #E4E4E7;background:#FAFAFA;border-radius:8px;padding:8px 10px;font-size:9.8px;line-height:1.45}'
 '.pov{display:grid;grid-template-columns:repeat(4,1fr);gap:8px 12px;padding:10px 11px}.pl .row{grid-template-columns:1fr 104px 60px 80px;font-size:9.8px;min-height:40px;white-space:nowrap}.pl .row span:nth-child(n+3){text-align:right}'
 '.pl .fld input{font-size:11px;padding:5px 7px;text-align:right}.pl .fld .em{position:absolute;white-space:normal;width:180px;margin-top:30px}.pl .fld{position:relative}.pf{display:flex;justify-content:flex-end;align-items:center;gap:10px;padding:10px 11px;border-top:1px solid #F0F0F1}.pf .tt2{font-size:10px;color:#71717A}.pf .tt2 b{font-family:"JetBrains Mono",ui-monospace,monospace;font-size:13px;color:#18181B;margin-left:6px}'
 '.bt.pri.big{font-size:10.6px;padding:7px 14px}'
 '.shot.ph .gr{grid-template-columns:48px repeat(6,1fr);gap:3px;padding:3px 6px}.shot.ph .gc{height:26px}.shot.ph .gc b{font-size:11px}.shot.ph .gc small{display:none}.shot.ph .gc .po{font-size:7px;left:auto;right:1px;top:1px;bottom:auto;padding:0 3px;line-height:1.4}.shot.ph .tile{padding:5px 9px}.shot.ph .tile b{font-size:12.5px}'
 '.shot.ph .sg{height:28px;padding:0 13px}.shot.ph .sc{height:30px;padding:0 12px}.shot.ph .srch input{height:34px}.shot.ph .mkp{height:30px}.shot.ph .bt.pri.big{padding:9px 14px}'
 '.shot.ph.nar .lgd{display:none}.ph-m .row{grid-template-columns:1fr auto;min-height:30px;font-size:10.4px}.ph2{display:grid;grid-template-columns:1fr 1fr;gap:8px}'
)

WIN = ''

JS = r'''
var FOC='.rail .ni,.bc,.phd>*,.bn .bi,.pg .tile,.pg .ct,.pg .row,.pg .gr>span,.pg .gc,.pg .lgd,.pg .empt,.pg .smp,.pg .srch,.pg .tbr .nm,.pg .seg,.pg .note,.pg .pov,.pg .pf>*';
var SZ=[7,8,9,10,11,12];
var COL=[['B','Black','#18181B'],['S','Sand','#D6C7A1'],['N','Navy','#1E2A4A']];
var OH={B:[24,36,18,40,32,20],S:[16,28,34,30,22,14],N:[12,22,26,28,20,10]};
var CM={B:[10,22,46,28,30,12],S:[8,12,20,24,18,6],N:[6,14,30,12,14,4]};
var RP={R:[8,10,12,12,10,6],W:[4,4,5,5,4,3]};
var LEA=[2.6,2.8,3.0,3.2,3.4,3.6];
var ORD=[['SO-6120','Tidewater Shoe Shop',96,'11/18'],['SO-6127','Kestrel Run Co.',84,'11/21'],['SO-6133','Marlow web store',62,'11/24'],['SO-6138','Fernhill Outdoor',44,'11/26'],['SO-6141','Brightwater Sports',30,'12/02']];
var B9=[['SO-6120','Tidewater Shoe Shop',18],['SO-6127','Kestrel Run Co.',16],['SO-6133','Marlow web store',12]];
var PER=3.0,PAIRS=28,LOH=61.5,STEP=5.0,PRICE=4.60;
var MAT=[['Full grain leather, Black','3.0 sq ft',PER*PAIRS,LOH,'sq ft'],['Outsole, size 9','1',28,30,''],['Insole, size 9','1',28,40,''],['Laces','1',28,120,''],['Shoe box','1',28,60,'']];
var S;
function oh(c,i,w){var v=OH[c][i];return w==='W'?Math.round(v*0.4):v;}
function cm(c,i,w){var v=CM[c][i];return w==='W'?Math.round(v*0.3):v;}
function av(c,i,w){return oh(c,i,w)-cm(c,i,w);}
function sum(f,w){var t=0;COL.forEach(function(c){SZ.forEach(function(_,i){t+=f(c[0],i,w);});});return t;}
function shorts(w){var n=0;COL.forEach(function(c){SZ.forEach(function(_,i){if(av(c[0],i,w)<0)n++;});});return n;}
function need(){return PER*PAIRS;}
function gap(){return Math.round((need()-LOH)*10)/10;}
function poq(){return Math.ceil(gap()/STEP)*STEP;}
function f1(n){return n.toFixed(1);}
function num(v){v=String(v).replace(/,/g,'').replace(/\s*sq\s*ft$/i,'').trim();return /^\d{1,4}(\.\d)?$/.test(v)?parseFloat(v):-1;}
function ico(){return '<svg width="13" height="13" viewBox="0 0 14 14" fill="none" aria-hidden="true"><circle cx="6" cy="6" r="4.2" stroke="#A1A1AA" stroke-width="1.4"/><path d="M9.2 9.2l3 3" stroke="#A1A1AA" stroke-width="1.4" stroke-linecap="round"/></svg>';}
function seg(){return '<div class="seg" role="group" aria-label="Width">'+[['R','Regular'],['W','Wide']].map(function(x){return '<button type="button" class="sg'+(S.w===x[0]?' on':'')+'" id="w-'+x[0]+'" aria-pressed="'+(S.w===x[0])+'">'+x[1]+'</button>';}).join('')+'</div>';}
function cell(c,i,P){var w=S.w,a=av(c,i,w),id='c-'+c+'-'+SZ[i]+'-'+w,cls='gc'+(a<0?' short':(a<RP[w][i]?' low':'')),po=S.po&&w==='R'&&c==='B'&&i===2;
 return '<button type="button" class="'+cls+(po?' has-po':'')+'" id="'+id+'" aria-label="'+c+' size '+SZ[i]+', '+a+' available"><b>'+a+'</b>'+(P?'':'<small>'+oh(c,i,w)+' / '+cm(c,i,w)+'</small>')+(po?'<span class="po" id="po-flag">'+(P?'PO':'PO raised')+'</span>':'')+'</button>';}
function grid(P){var w=S.w,h='<div class="mx"><div class="gr h"><span>'+(P?'':'Color')+'</span>'+SZ.map(function(s){return '<span>'+s+'</span>';}).join('')+(P?'':'<span style="text-align:right">Total</span>')+'</div>';
 COL.forEach(function(c){var t=0;SZ.forEach(function(_,i){t+=av(c[0],i,w);});h+='<div class="gr"><span class="cl"><span class="sw" style="background:'+c[2]+'"></span>'+c[1]+'</span>'+SZ.map(function(_,i){return cell(c[0],i,P);}).join('')+(P?'':'<span class="tot">'+t+'</span>')+'</div>';});
 if(!P)h+='<div class="gr sub"><span>Reorder point</span>'+RP[w].map(function(x){return '<span>'+x+'</span>';}).join('')+'<span></span></div><div class="gr sub"><span>Leather, sq ft</span>'+LEA.map(function(x){return '<span>'+f1(x)+'</span>';}).join('')+'<span></span></div>';
 return h+'</div>';}
function render(){var P=ph(),h='',scr=S.scr;
if(scr==='search'){setNav({m:'inv',bc:['Inventory','Styles'],t:'Size and color matrix',scr:'Style search'});
 h='<div class="frm sbar"><label class="srch" id="fs">'+ico()+'<input id="iq" placeholder="Search a style" value="'+S.v.q+'" autocomplete="off" aria-label="Search a style"><span class="em">No style matches. Try HR-210.</span></label>'+(P?'':'<span class="smp">Try</span>')+'<button type="button" class="sc" id="smp">HR-210</button></div>';
 h+='<div class="empt big"><svg width="34" height="34" viewBox="0 0 34 34" fill="none" aria-hidden="true"><rect x="3" y="3" width="28" height="28" rx="5" stroke="#D4D4D8" stroke-width="1.5"/><path d="M3 12h28M3 21h28M12 3v28M21 3v28" stroke="#D4D4D8" stroke-width="1.5"/></svg><b>Search a style to see its size and color grid</b><span>Every size, width and color under one parent style, with on hand, committed and available side by side.</span>'+(P?'':'<span class="ft">Type a style number and press Enter, or pick the sample</span>')+'</div>';}
else if(scr==='matrix'){var w=S.w;setNav({m:'inv',bc:['Inventory','Styles','HR-210'],t:'Harbor Runner',chip:['c-bad',shorts(w)+' short'],scr:'Size matrix'});
 if(P){h='<div class="tbr"><span class="nm grow"><b>HR-210</b><small>'+(w==='R'?'Regular':'Wide')+'</small></span>'+seg()+'</div>'+grid(P)+'<div class="lgd"><span><i style="background:#FEE2E2"></i>Short</span><span><i style="background:#F59E0B"></i>Below reorder point</span></div>';}
 else{h='<div class="tbr"><label class="srch" style="max-width:200px">'+ico()+'<input value="HR-210" aria-label="Search a style" readonly></label><span class="nm grow"><b>HR-210, Harbor Runner</b><small>3 colors, sizes 7 to 12, '+(w==='R'?'Regular':'Wide')+' width</small></span>'+seg()+'</div>';
  h+='<div class="tl"><div class="tile"><small>On hand</small><b id="t-oh">'+sum(oh,w)+'</b></div><div class="tile"><small>Committed</small><b id="t-cm">'+sum(cm,w)+'</b></div><div class="tile"><small>Available</small><b id="t-av">'+sum(av,w)+'</b></div><div class="tile bad"><small>Short cells</small><b id="t-sh">'+shorts(w)+'</b></div></div>';
  h+=grid(P)+'<div class="lgd"><span>Cell: available, then on hand / committed</span><span><i style="background:#FEE2E2"></i>Short</span><span><i style="background:#F59E0B;border-radius:50%"></i>Below reorder point</span>'+(S.po?'<span><i style="background:#E8EEFC"></i>PO raised</span>':'')+'</div>';
  var tot=0;ORD.forEach(function(o){tot+=o[2];});
  h+='<div class="cd ord" style="flex:1 1 0"><div class="ct">Open orders, HR-210<span class="mut" style="font-weight:500">'+(w==='R'?tot+' pairs committed, Regular':sum(cm,w)+' pairs committed, Wide')+'</span></div>'+ORD.map(function(o){return '<div class="row"><span class="mono">'+o[0]+'</span><span>'+o[1]+'</span><span class="mono">'+(w==='R'?o[2]:Math.round(o[2]*0.3))+' pairs</span><span class="mono mut">'+o[3]+'</span></div>';}).join('')+'</div>';}}
else if(scr==='detail'){setNav({m:'inv',bc:['Inventory',['HR-210','cb-st'],'Black 9 Regular'],t:'HR-210-BLK-9',chip:['c-bad',PAIRS+' short'],scr:'Shortage detail',back:1});
 var o=oh('B',2,'R'),c=cm('B',2,'R');
 if(P){h='<div class="ph2"><div class="tile bad"><small>Short</small><b>'+PAIRS+' pairs</b></div><div class="tile bad"><small>Leather short</small><b>'+f1(gap())+' sq ft</b></div></div>';
  h+='<div class="cd ph-m"><div class="row"><span>Full grain leather, Black<br><span class="mut mono">'+f1(need())+' needed, '+f1(LOH)+' on hand</span></span><button type="button" class="mkp" id="mk-po">Create PO</button></div><div class="row"><span class="mut">Outsole, insole, laces, box</span><span class="ch c-ok">OK</span></div><div class="row"><span class="mut">On hand '+o+', committed '+c+'</span><span class="mono">'+PAIRS+' short</span></div></div>';}
 else{h='<div class="tl"><div class="tile"><small>On hand</small><b>'+o+'</b></div><div class="tile"><small>Committed</small><b>'+c+'</b></div><div class="tile bad"><small>Short</small><b id="d-sh">'+(c-o)+'</b></div><div class="tile"><small>Reorder point</small><b>'+RP.R[2]+'</b></div></div>';
  h+='<div class="cd mt"><div class="ct">Materials for '+PAIRS+' pairs, from the BOM<span class="mut" style="font-weight:500">Size 9 quantities</span></div><div class="row h"><span>Material</span><span>Per pair</span><span>Needed</span><span>On hand</span><span>Status</span></div>'+
  MAT.map(function(m,i){var bad=m[3]<m[2];return '<div class="row'+(bad?' bad':'')+'"><span>'+m[0]+'</span><span class="mono">'+m[1]+'</span><span class="mono" id="'+(i?'':'m-need')+'">'+(m[4]?f1(m[2]):m[2])+'</span><span class="mono">'+(m[4]?f1(m[3]):m[3])+'</span><span>'+(bad?'<span class="ch c-bad" id="m-gap">Short '+f1(gap())+' sq ft</span>'+(S.po?'<span class="ch c-info" style="margin-left:6px">PO raised</span>':'<button type="button" class="mkp" id="mk-po">Create purchase order</button>'):'<span class="ch c-ok">OK</span>')+'</span></div>';}).join('')+'</div>';
  h+='<div class="two"><div class="cd"><div class="ct">Committed to<span class="mut" style="font-weight:500">'+c+' pairs</span></div>'+B9.map(function(x){return '<div class="row"><span class="mono">'+x[0]+'</span><span>'+x[1]+'</span><span class="mono">'+x[2]+' pairs</span></div>';}).join('')+'</div>'+
  '<div class="note">Leather is the only short material for this cell. Outsoles, insoles, laces and boxes cover all '+PAIRS+' pairs, so one leather order closes the gap.</div></div>';}}
else{setNav({m:'pur',bc:['Purchasing','Purchase orders','PO-3318'],t:'PO-3318',chip:['c-idle','Draft'],scr:'Purchase order',back:1});
 var q=num(S.v.q2),amt=q>0?q*PRICE:0;
 if(P){h='<div class="cd pl frm"><div class="ct">Ridgeline Tannery<span class="mut" style="font-weight:500">9 day lead</span></div><div class="row" style="grid-template-columns:1fr 92px"><span>Full grain leather, Black<br><span class="mut mono">Short '+f1(gap())+' sq ft</span></span><label class="fld" id="fq"><small>Sq ft</small><input id="iq2" value="'+S.v.q2+'" inputmode="decimal" autocomplete="off"><span class="em">At least '+f1(gap())+'</span></label></div><div class="pf"><span class="tt2">Total<b id="amt">'+m2(amt)+'</b></span><button type="button" class="bt pri big" id="send">Send to vendor</button></div></div><div class="note">'+f1(gap())+' short, rounded up to the '+f1(STEP)+' sq ft order step.</div>';}
 else{h='<div class="cd"><div class="pov">'+[['Vendor','Ridgeline Tannery'],['Lead time','9 days'],['Expected','11/19'],['Terms','Net 30']].map(function(x){return '<div class="kv"><small>'+x[0]+'</small><b>'+x[1]+'</b></div>';}).join('')+'</div></div>';
  h+='<div class="cd pl frm"><div class="ct">Lines<span class="mut" style="font-weight:500">From shortage HR-210-BLK-9, '+PAIRS+' pairs</span></div><div class="row h"><span>Item</span><span>Quantity, sq ft</span><span>Price</span><span>Amount</span></div>'+
  '<div class="row"><span>Full grain leather, Black<br><span class="mut" style="font-size:9px">LTH-FG-BLK</span></span><label class="fld" id="fq"><input id="iq2" value="'+S.v.q2+'" inputmode="decimal" autocomplete="off" aria-label="Quantity in square feet"><span class="em">At least '+f1(gap())+' sq ft to cover the short</span></label><span class="mono">'+PRICE.toFixed(2)+'</span><span class="mono" id="amt">'+m2(amt)+'</span></div>'+
  '<div class="pf"><span class="tt2">Total<b id="amt2">'+m2(amt)+'</b></span><button type="button" class="bt pri big" id="send">Send to vendor</button></div></div>';
  h+='<div class="note">Short '+f1(gap())+' sq ft, rounded up to Ridgeline\'s '+f1(STEP)+' sq ft order step: '+f1(poq())+' sq ft. The extra '+f1(poq()-gap())+' sq ft goes to stock for the next run.</div>';
  h+='<div class="cd" style="flex:1 1 0"><div class="ct">Recent orders, Ridgeline Tannery<span class="mut" style="font-weight:500">On time 11 of 12</span></div>'+[['PO-3297','Full grain leather, Black','60.0 sq ft','10/28'],['PO-3281','Full grain leather, Sand','45.0 sq ft','10/14'],['PO-3266','Full grain leather, Navy','50.0 sq ft','10/02'],['PO-3240','Full grain leather, Black','80.0 sq ft','09/18']].map(function(x){return '<div class="row" style="grid-template-columns:62px 1fr 80px 50px;font-size:9.8px"><span class="mono">'+x[0]+'</span><span>'+x[1]+'</span><span class="mono r">'+x[2]+'</span><span class="mono mut r">'+x[3]+'</span></div>';}).join('')+'</div>';}}
$('pg').innerHTML=h;}
$('pg').addEventListener('input',function(e){if(e.target.id==='iq'){S.v.q=e.target.value;$('fs').classList.remove('err');}if(e.target.id==='iq2'){S.v.q2=e.target.value;var q=num(e.target.value),a=m2(q>0?q*PRICE:0);if($('amt'))$('amt').textContent=a;if($('amt2'))$('amt2').textContent=a;}});
function resetState(){S={scr:'search',w:'R',po:false,v:{q:'',q2:f1(poq())}};render();}
function okQ(){var v=$('iq').value.trim(),b=v!==''&&!/^hr-?210$/i.test(v);$('fs').classList.toggle('err',b);return !b;}
function okP(){var q=num($('iq2').value),b=!(q>=gap()&&q<1000);$('fq').classList.toggle('err',b);return !b;}
function typeIn(done){var inp=$('iq'),s='HR-210',k=0;if(!inp||/^hr-?210$/i.test(inp.value.trim())){done();return;}(function t(){inp.value=s.slice(0,++k);if(k<s.length)later(t,55);else later(done,120);})();}
var CAPAT=function(hh){return ph()?{l:8,t:5}:{l:14,t:visH()-hh-40};};
var ST=[
{id:'find',target:function(){return $('smp');},prompt:'Click the sample HR-210, or type it and press Enter',where:'below',ok:okQ,run:function(q){var go=function(){S.v.q='HR-210';S.scr='matrix';render();};if(q)go();else typeIn(go);},
 after:['Every size and color of a style in one grid','HR-210 Harbor Runner, Regular width: 3 colors by sizes 7 to 12, two cells short.'],pc:'Every size and color in one grid'},
{id:'cell',target:function(){return $('c-B-9-R');},prompt:'Click the short Black size 9 cell',where:'below',run:function(){S.scr='detail';render();},
 after:function(){return['A short cell opens to the materials behind it',cm('B',2,'R')+' committed against '+oh('B',2,'R')+' on hand: '+PAIRS+' pairs short. Leather is the only short material.'];},pc:'28 short, and leather is why'},
{id:'mkpo',target:function(){return $('mk-po');},prompt:'Click Create purchase order',where:'below',run:function(){S.scr='po';render();},
 after:function(){return['The purchase order is drafted from the gap',f1(need())+' sq ft needed, '+f1(LOH)+' on hand, '+f1(gap())+' short. Ridgeline Tannery orders in '+f1(STEP)+' sq ft steps.'];},pc:'A PO drafted from the gap'},
{id:'send',target:function(){return $('send');},prompt:'Click Send to vendor',where:'above',ok:okP,run:function(){okP();S.po=true;S.scr='matrix';render();},
 after:function(){return['Back on the grid, the cell shows PO raised','PO-3318 sent to Ridgeline Tannery: '+f1(num(S.v.q2))+' sq ft of black full grain leather, '+m2(num(S.v.q2)*PRICE)+'.'];},pc:'PO sent, the cell shows PO raised'},
{id:'wide',target:function(){return $('w-W');},prompt:'Switch the grid to Wide',where:'below',run:function(){S.w='W';render();},
 after:function(){return['Wide has its own counts and its own reorder points','Black size 9 Wide: '+oh('B',2,'W')+' on hand, '+cm('B',2,'W')+' committed, '+(-av('B',2,'W'))+' short.'];},pc:'Wide has its own counts'}];
'''
