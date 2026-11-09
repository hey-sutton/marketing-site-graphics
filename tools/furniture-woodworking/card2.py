"""Furniture and woodworking card 2: Offcuts & Remnants. A cut diagram plus compact tables: pick the plywood in stock, load
job J-2417's cut list, nest it on one 96 by 48 in sheet (the cuts draw in order), open the leftover (30 x 18 in, 3.75 sq ft,
yield 88.3%), book it back to stock as RM-0031 on shelf R2-04, then find it in inventory by width. Kerf is not modeled."""
SUMMARY = 'Offcuts & Remnants (a cut list nested on one 4 by 8 ft sheet with the cuts drawn in order, the leftover sized with the yield, booked back to stock as a serialized remnant with width, length and shelf, then found by width)'
ARIA = 'Interactive product screen: pick maple plywood, load the cut list for job J-2417, nest five parts on one sheet, open the 30 by 18 inch leftover at 88.3 percent yield, book it to stock as RM-0031 and filter remnants by width'
STEPS = 7
HEADLINE = 'Offcuts & Remnants'
STUDIO = dict(lede='A typical cut planner, built on your Sutton data with Studio. Want it different? Describe the change.',
              examples=['Set a minimum remnant size to keep', 'Require a reason code when scrapping', 'Group remnants by species and thickness', 'Print a label when a remnant is booked'],
              built_on='Serialized inventory and custom fields', change='Sizes, rules and labels')
STORY = [('Cut planner', 'pro', 'table row', 'bottom left'), ('Cut list J-2417', 'pro', 'sample chip', 'top center'),
         ('Sheet layout', 'pro', 'action button', 'bottom center'), ('Sheet layout', 'pro', 'diagram block', 'right'),
         ('Sheet layout', 'pro', 'primary button', 'bottom right'), ('Inventory', 'inv', 'nav item', 'top left'),
         ('Inventory', 'inv', 'filter chip', 'top center')]
# guillotine layout on one 96 x 48 in sheet, in inches: [label, x, y, w, h]. Rip at 30, cross cut at 66, then split each block.
PARTS = [('Side panel', 0, 0, 30, 24), ('Side panel', 0, 24, 30, 24), ('Shelf', 30, 0, 36, 24), ('Shelf', 30, 24, 36, 24), ('Back panel', 66, 0, 30, 30)]
REMNANT = (66, 30, 30, 18)

CSS = (
 '.tb{display:flex;align-items:flex-end;gap:10px;flex:none}.tb .fld{width:190px}.tb .fld input{font-size:11px;padding:6px 8px}.smp{height:28px;padding:0 9px;border:1px dashed #A1A1AA;border-radius:6px;background:#fff;font-size:9.8px;cursor:pointer;display:inline-flex;align-items:center;gap:5px}.smp:hover,.smp.fakehover{background:#F4F4F5}.smp .mono{font-weight:600}'
 '.mat{margin-left:auto;display:flex;flex-direction:column;align-items:flex-end;gap:2px;font-size:9.6px}.mat small{font-size:8.6px;color:#71717A}'
 '.hero{position:relative;border:1px solid #E4E4E7;border-radius:10px;background:#FAFAF9;flex:none;height:232px;display:flex;align-items:center;justify-content:center;overflow:hidden}'
 '.hero .empt{position:absolute;inset:12px}.hero svg{display:block}'
 '.sh{fill:#FCFAF6;stroke:#A8A29E;stroke-width:3}.pt{fill:#F3E6D3;stroke:none}.pt.in{animation:none}.anim .pt{opacity:0;animation:ptin .35s ease forwards}@keyframes ptin{to{opacity:1}}'
 '.cut{stroke:#18181B;stroke-width:4;stroke-linecap:round}.anim .cut{stroke-dasharray:var(--l);stroke-dashoffset:var(--l);animation:cutin .38s cubic-bezier(.5,0,.3,1) forwards}@keyframes cutin{to{stroke-dashoffset:0}}'
 '.plb{font:600 25px Inter,sans-serif;fill:#44403C}.pls{font:500 21px "JetBrains Mono",ui-monospace,monospace;fill:#78716C}.anim .plb,.anim .pls{opacity:0;animation:ptin .3s ease forwards}'
 '.rem{fill:url(#hatch);stroke:#A8A29E;stroke-width:3;stroke-dasharray:10 8;cursor:pointer;transition:fill .3s}.rem.on{fill:#FEF9C3;stroke:#18181B;stroke-dasharray:none;stroke-width:5}.rem.fakehover{fill:#F5F5F4}'
 '.dim{font:500 19px "JetBrains Mono",ui-monospace,monospace;fill:#A1A1AA}'
 '.cols{display:grid;grid-template-columns:1fr 1fr 186px;gap:10px;flex:1 1 0;min-height:0}.cols .cd{min-height:0}'
 '.stk .row{grid-template-columns:1fr 40px 56px;font-size:9.6px;min-height:27px;white-space:nowrap}.stk .row>span:nth-child(n+2){text-align:right}.stk small{display:block;color:#71717A;font-size:8.4px}'
 '.cl .row{grid-template-columns:1fr 54px 26px;font-size:9.6px;min-height:28px;white-space:nowrap}.cl .row>span:nth-child(n+2){text-align:right}'
 '.yp{padding:9px 11px;display:flex;flex-direction:column;gap:6px;font-size:9.8px}.yp .wl{display:flex;justify-content:space-between;align-items:baseline}.yp .wl b{font-family:"JetBrains Mono",ui-monospace,monospace;font-size:10.4px}.yp .big{font-size:20px}.yp .bt{align-self:stretch;text-align:center}'
 '.chips{display:flex;gap:6px;flex:none}.fc{height:26px;padding:0 10px;border:1px solid #E4E4E7;border-radius:999px;background:#fff;font-size:9.8px;cursor:pointer;display:inline-flex;align-items:center;gap:5px}.fc.on{background:#18181B;border-color:#18181B;color:#fff}.fc.fakehover{background:#F4F4F5}.fc.on.fakehover{background:#3F3F46}'
 '.tl{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;flex:none}.tile{border:1px solid #E4E4E7;border-radius:8px;padding:8px 10px;display:flex;flex-direction:column;gap:2px}.tile small{font-size:8.8px;color:#71717A}.tile b{font-family:"JetBrains Mono",ui-monospace,monospace;font-size:15px;font-weight:600}'
 '.rt .row{grid-template-columns:62px 1fr 46px 50px 50px 48px 52px;font-size:9.6px;min-height:30px;white-space:nowrap}.rt .row>span:nth-child(n+3):nth-child(-n+5){text-align:right}.row.new{background:#F0FDF4}'
 '.lg .row{grid-template-columns:44px 1fr 84px;font-size:9.6px;min-height:27px}.lg .row>span:last-child{text-align:right}'
 # phone
 '.shot.ph .tb .fld{width:auto;flex:1}.shot.ph .hero{height:auto;border:0;background:none;padding:0}.prw{display:flex;align-items:center;gap:8px;justify-content:space-between;font-size:10px}.prw .bt{height:28px}'
 '.shot.ph .tile{padding:5px 9px}.shot.ph .tile b{font-size:13px}.shot.ph .rt .row{grid-template-columns:60px 1fr 60px 44px;min-height:27px;font-size:10px}.shot.ph .stk .row,.shot.ph .cl .row{min-height:27px;font-size:10px}'
)

WIN = ''

JS = r'''
var FOC='.rail .ni,.bc,.phd>*,.bn .bi,.tb>*,.pg .hero,.pg .cd>*,.pg .cd .row,.chips>*,.pg .tile,.prw>*';
var PARTS=__PARTS__,REM=__REM__,SW=96,SL=48;
var STOCK=[['PLY-MPL-34','Maple plywood, 3/4 in',12,2],['PLY-BIR-12','Baltic birch, 1/2 in',18,4],['PLY-WAL-34','Walnut plywood, 3/4 in',6,1],['MDF-34','MDF, 3/4 in',9,0],['HDF-14','Hardboard, 1/4 in',22,0]];
var RMS=[['RM-0026','PLY-MPL-34',36,22,'R2-01','J-2402'],['RM-0029','PLY-MPL-34',16,40,'R2-03','J-2409']];
var NEW=['RM-0031','PLY-MPL-34',REM[2],REM[3],'R2-04','J-2417'];
var S;
function area(p){return p[3]*p[4];}
function partsArea(){return PARTS.reduce(function(a,p){return a+area(p);},0);}
function yld(){return Math.round(partsArea()/(SW*SL)*1000)/10;}
function remSqft(){return REM[2]*REM[3]/144;}
function sheets(){return STOCK[0][2]-(S.booked?1:0);}
function rems(){return STOCK[0][3]+(S.booked?1:0);}
function cutlist(){var m={};PARTS.forEach(function(p){var k=p[0]+'|'+p[3]+' x '+p[4];m[k]=(m[k]||0)+1;});return Object.keys(m).map(function(k){return [k.split('|')[0],k.split('|')[1],m[k]];});}
function svg(P){var W=P?290:440,H=W/2,K=10,ln=function(x1,y1,x2,y2,i){var l=Math.abs(x2-x1+y2-y1)*K;return '<line class="cut" x1="'+x1*K+'" y1="'+y1*K+'" x2="'+x2*K+'" y2="'+y2*K+'" style="--l:'+l+';animation-delay:'+(i*.32)+'s"/>';};
 var h='<svg width="'+W+'" height="'+H+'" viewBox="-6 -6 972 492" aria-label="Sheet layout, 96 by 48 inches" role="img"><defs><pattern id="hatch" width="16" height="16" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><rect width="16" height="16" fill="#fff"/><line x1="0" y1="0" x2="0" y2="16" stroke="#E7E5E4" stroke-width="6"/></pattern></defs><g class="'+(S.anim?'anim':'')+'"><rect class="sh" x="0" y="0" width="960" height="480" rx="4"/>';
 if(!S.nest)return h+'</g></svg>';
 PARTS.forEach(function(p,i){var d=(i<2?2:i<4?3:4)*.32+.2;h+='<rect class="pt" x="'+(p[1]*K+3)+'" y="'+(p[2]*K+3)+'" width="'+(p[3]*K-6)+'" height="'+(p[4]*K-6)+'" rx="3" style="animation-delay:'+d+'s"/>';});
 h+='<rect class="rem'+(S.open?' on':'')+'" id="rem" x="'+(REM[0]*K+3)+'" y="'+(REM[1]*K+3)+'" width="'+(REM[2]*K-6)+'" height="'+(REM[3]*K-6)+'" rx="3"/>';
 h+=ln(30,0,30,48,0)+ln(66,0,66,48,1)+ln(0,24,30,24,2)+ln(30,24,66,24,3)+ln(66,30,96,30,4);
 PARTS.forEach(function(p,i){var d=(i<2?2:i<4?3:4)*.32+.35,cx=(p[1]+p[3]/2)*K,cy=(p[2]+p[4]/2)*K;h+='<text class="plb" text-anchor="middle" x="'+cx+'" y="'+(cy-4)+'" style="animation-delay:'+d+'s">'+p[0]+'</text><text class="pls" text-anchor="middle" x="'+cx+'" y="'+(cy+24)+'" style="animation-delay:'+d+'s">'+p[3]+' x '+p[4]+'</text>';});
 var rx=(REM[0]+REM[2]/2)*K,ry=(REM[1]+REM[3]/2)*K;h+='<text class="plb" text-anchor="middle" x="'+rx+'" y="'+(ry-2)+'" style="animation-delay:1.7s;pointer-events:none">'+(S.booked?NEW[0]:'Leftover')+'</text><text class="pls" text-anchor="middle" x="'+rx+'" y="'+(ry+24)+'" style="animation-delay:1.7s;pointer-events:none">'+REM[2]+' x '+REM[3]+'</text>';
 return h+'</g></svg>';}
function stockCard(P){return '<div class="cd stk"><div class="ct">Stock on hand'+(P?'<span class="mut" style="font-weight:500">Sheets, remnants</span>':'')+'</div>'+(P?'':'<div class="row h"><span>Item</span><span>Sheets</span><span>Remnants</span></div>')+STOCK.slice(0,P?3:5).map(function(x,i){var s=i===0?sheets():x[2],r=i===0?rems():x[3];
 return '<button type="button" class="row'+(i===0&&S.mat?' sel':'')+'" id="st-'+x[0]+'"><span><span class="mono">'+x[0]+'</span><small>'+x[1]+'</small></span><span class="mono'+(i===0&&S.booked?' flash':'')+'" id="'+(i===0?'sh0':'')+'">'+s+'</span><span class="mono" id="'+(i===0?'rm0':'')+'">'+r+'</span></button>';}).join('')+'</div>';}
function cutCard(P){if(!S.job)return '<div class="cd cl"><div class="ct">Cut list</div><div class="empt" style="border:0;background:none;padding:22px 10px"><b>No cut list yet</b><span>Choose a job to load its cut list.</span></div></div>';
 return '<div class="cd cl"><div class="ct">Cut list'+(S.nest?'<span class="ch c-ok">Nested</span>':'<button type="button" class="bt" id="nest">Nest on sheet</button>')+'</div><div class="row h"><span>Part</span><span>Size, in</span><span>Qty</span></div>'+
 cutlist().map(function(c){return '<div class="row in"><span>'+c[0]+'</span><span class="mono">'+c[1]+'</span><span class="mono">'+c[2]+'</span></div>';}).join('')+(P?'':'<div class="row"><span class="mut">PLY-MPL-34, 3/4 in</span><span class="mono mut">'+PARTS.length+' parts</span><span></span></div>')+'</div>';}
function yieldCard(){if(!S.nest)return '<div class="cd"><div class="ct">Sheet</div><div class="empt" style="border:0;background:none;padding:22px 10px"><b>Nothing nested</b><span>Yield and leftovers show once parts are on a sheet.</span></div></div>';
 if(!S.open)return '<div class="cd"><div class="ct">Sheet 1 of 1<span class="ch c-info">5 cuts</span></div><div class="yp"><div class="wl"><span>Parts placed</span><b>'+PARTS.length+' of '+PARTS.length+'</b></div><div class="wl"><span>Sheet</span><b>96 x 48 in</b></div><div class="wl"><span class="mut">Open the leftover to size it</span></div></div></div>';
 return '<div class="cd in"><div class="ct">Leftover<span class="ch '+(S.booked?'c-ok':'c-info')+'">'+(S.booked?'Booked':'Keep')+'</span></div><div class="yp"><div class="wl"><span>Size</span><b id="rsz">'+REM[2]+' x '+REM[3]+' in</b></div><div class="wl"><span>Area</span><b id="rsf">'+remSqft().toFixed(2)+' sq ft</b></div><div class="wl"><span>Parts</span><b>'+n0(partsArea())+' of '+n0(SW*SL)+' sq in</b></div><div class="wl"><span>Yield</span><b class="big" id="yl">'+yld().toFixed(1)+'%</b></div>'+
 (S.booked?'<span class="ch c-ok" id="bk-ok">'+NEW[0]+' on shelf '+NEW[4]+'</span>':'<button type="button" class="bt pri" id="book">Book remnant to stock</button>')+'</div></div>';}
function render(){var P=ph(),h='',scr=S.scr;
if(scr!=='inv'){var nm=scr==='plan'?'Cut planner':scr==='list'?'Cut list J-2417':'Sheet layout';
 setNav({m:'pro',bc:scr==='plan'?['Production','Cut planner']:scr==='list'?['Production','Cut planner','J-2417']:['Production','Cut planner','J-2417','Sheet 1'],t:P&&scr==='sheet'?'Sheet 1, J-2417':'Cut planner',chip:S.nest?['c-ok',yld().toFixed(1)+'% yield']:null,scr:nm,back:P&&scr!=='plan'?1:0});
 var tb='<div class="tb frm"><label class="fld" id="fj"><small>Job</small><input id="ij" value="'+S.vj+'" placeholder="Type a job, like J-2417" autocomplete="off" spellcheck="false"><span class="em">Try J-2417</span></label><button type="button" class="smp" id="smp">Try <span class="mono">J-2417</span></button>'+(P?'':'<div class="mat"><b>'+(S.mat?'Maple plywood, 3/4 in':'No material picked')+'</b><small>'+(S.mat?'PLY-MPL-34, sheet 96 x 48 in':'Pick a stock line below')+'</small></div>')+'</div>';
 if(!P){h=tb+'<div class="hero">'+(S.nest?svg(P):'<div class="empt"><b>Sheet layout</b><span>Choose a job to load its cut list, then nest it on a sheet.</span></div>')+'</div><div class="cols">'+stockCard(P)+cutCard(P)+yieldCard()+'</div>';}
 else if(scr==='plan')h=tb+stockCard(P);
 else if(scr==='list')h=cutCard(P);
 else{h='<div class="hero">'+svg(P)+'</div>';h+=S.open?'<div class="prw in"><span><b class="mono" id="rsz">'+REM[2]+' x '+REM[3]+' in</b>, <span id="rsf">'+remSqft().toFixed(2)+' sq ft</span>, yield <b id="yl">'+yld().toFixed(1)+'%</b></span>'+(S.booked?'<span class="ch c-ok" id="bk-ok">'+NEW[0]+'</span>':'<button type="button" class="bt pri" id="book">Book to stock</button>')+'</div>':'<div class="prw"><span class="mut">5 parts on one sheet, 5 cuts</span></div>';}}
else{setNav({m:'inv',bc:['Inventory','PLY-MPL-34','Remnants'],t:P?'PLY-MPL-34':'PLY-MPL-34 Maple plywood, 3/4 in',chip:['c-info','Serialized remnants'],scr:'Inventory'});
 var list=RMS.concat([NEW]).filter(function(r){return !S.flt||r[2]>=24;});
 h='<div class="tl"'+(P?' style="grid-template-columns:1fr 1fr"':'')+'><div class="tile"><small>Full sheets</small><b id="ish">'+sheets()+'</b></div><div class="tile"><small>Remnants</small><b id="irm">'+rems()+'</b></div>'+(P?'':'<div class="tile"><small>Booked today</small><b>'+NEW[0]+'</b></div>')+'</div>';
 h+='<div class="chips"><button type="button" class="fc'+(S.flt?'':' on')+'" id="f-all">All remnants</button><button type="button" class="fc'+(S.flt?' on':'')+'" id="f-w">Width 24 in or more</button>'+(P?'':'<button type="button" class="fc">Shelf R2</button>')+'</div>';
 h+='<div class="cd rt">'+(P?'':'<div class="row h">')+(P?'':'<span>Serial</span><span>Item</span><span>Width</span><span>Length</span><span>Sq ft</span><span>Shelf</span><span>From</span></div>')+list.map(function(r){var nw=r[0]===NEW[0];
  return '<div class="row'+(nw?' new in':'')+'" id="rw-'+r[0]+'">'+(P?'<span class="mono">'+r[0]+'</span><span class="mono">'+r[2]+' x '+r[3]+'</span><span class="mono">'+r[4]+'</span><span class="mono mut">'+r[5]+'</span>':'<span class="mono">'+r[0]+'</span><span class="mono mut">'+r[1]+'</span><span class="mono">'+r[2]+'</span><span class="mono">'+r[3]+'</span><span class="mono">'+(Math.round(r[2]*r[3]/144*100)/100).toFixed(2)+'</span><span class="mono">'+r[4]+'</span><span class="mono mut">'+r[5]+'</span>')+'</div>';}).join('')+'</div>';
 if(!P)h+='<div class="cd lg" style="flex:1 1 0"><div class="ct">Stock ledger<span class="mut" style="font-weight:500">Today</span></div><div class="row in"><span class="mono mut">10:14</span><span>'+NEW[0]+' booked from J-2417, '+NEW[2]+' x '+NEW[3]+' in</span><span class="mono">1 remnant in</span></div><div class="row in"><span class="mono mut">10:14</span><span>Sheet issued to J-2417, cut on sheet 1</span><span class="mono">1 sheet out</span></div><div class="row"><span class="mono mut">8:05</span><span>RM-0026 reserved for J-2423 drawer boxes</span><span class="mono">Reserved</span></div><div class="row"><span class="mono mut">7:50</span><span>Received PO-5512, 10 sheets PLY-BIR-12</span><span class="mono">10 sheets in</span></div></div>';}
$('pg').innerHTML=h;S.anim=false;}
$('pg').addEventListener('input',function(e){if(e.target.id==='ij')S.vj=e.target.value;});
function resetState(){S={scr:'plan',mat:false,job:false,nest:false,open:false,booked:false,flt:false,anim:false,vj:''};render();}
function okJ(){var v=String($('ij').value).trim(),b=!(v===''||/^J-?2417$/i.test(v));$('fj').classList.toggle('err',b);return !b;}
var CAPAT=function(hh){return ph()?{l:8,t:5}:{l:14,t:visH()-hh-40};};
var ST=[
{id:'mat',target:function(){return $('st-PLY-MPL-34');},prompt:'Click Maple plywood, 3/4 in',where:'above',run:function(){S.mat=true;render();},after:['Start from the stock you actually have','Maple plywood, 3/4 in: 12 sheets and 2 remnants on hand.'],pc:'Start from the stock you have'},
{id:'job',target:function(){return $('smp');},prompt:'Type J-2417 and press Enter, or click Try J-2417',where:'below',ok:okJ,run:function(){S.vj='J-2417';S.job=true;S.mat=true;S.scr='list';render();},after:['Load a job\'s cut list','J-2417: two side panels, two shelves and a back panel.']},
{id:'nest',target:function(){return $('nest');},prompt:'Click Nest on sheet',where:'above',run:function(q){S.nest=true;S.scr='sheet';S.anim=!q;render();},after:['Parts nest on one sheet','Five parts on one 96 x 48 in sheet, cut in five passes.']},
{id:'rem',target:function(){return $('rem');},prompt:'Click the leftover',where:'below',run:function(){S.open=true;render();},
 after:function(){return['The leftover is a usable piece, not waste',REM[2]+' x '+REM[3]+' in, '+remSqft().toFixed(2)+' sq ft. Yield '+yld().toFixed(1)+'%.'];},pc:'The leftover is usable, not waste'},
{id:'book',target:function(){return $('book');},prompt:'Click Book remnant to stock',where:'above',run:function(){S.booked=true;render();},after:['One click books it back',NEW[0]+', '+NEW[2]+' x '+NEW[3]+' in, goes to shelf '+NEW[4]+'.']},
{id:'inv',target:function(){return $(ph()?'bn-inv':'nv-inv');},prompt:'Click Inventory',where:'right',run:function(){S.scr='inv';render();},
 after:function(){return['It lands in inventory with its size and shelf',sheets()+' sheets and '+rems()+' remnants. '+NEW[0]+' is on shelf '+NEW[4]+'.'];},pc:'It lands in inventory, sized and shelved'},
{id:'flt',target:function(){return $('f-w');},prompt:'Click Width 24 in or more',where:'below',run:function(){S.flt=true;render();},after:['Find leftovers by width before ordering new sheets','Two remnants qualify, including '+NEW[0]+'.'],pc:'Find leftovers by width first'}];
'''
JS = JS.replace('__PARTS__', repr([list(p) for p in PARTS]).replace("'", '"')).replace('__REM__', repr(list(REMNANT)))
