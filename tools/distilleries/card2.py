"""Distilleries card 2: Barrel records and rickhouse locations. A rickhouse grid of barrels with a barrel record panel,
inside the app shell. Start: Rickhouse B with its six rows and five levels, every barrel in place, nothing selected.
Walkthrough: open row 4, open barrel 4-3-09 (fill date, age, source batch, gauge), compare gauge with fill, select
the ten barrels on level 3, dump them to blend tank BT-2 and watch the lot count drop. Volumes are held in tenths of
a liter so the sums are exact. Numbers are asserted in numbers_check.py."""
SUMMARY = 'Barrel records and rickhouse locations (a rickhouse with every barrel in place, row 4 opened barrel by barrel, one barrel record with fill, age, source batch and gauge, gauge compared with fill, ten barrels selected and dumped to blend tank BT-2, the lot count updated)'
ARIA = 'Interactive product screen: open row 4 of Rickhouse B, open barrel 4-3-09, compare its gauge with its fill, select the ten barrels on level 3 and dump 511.0 L to blend tank BT-2'
STEPS = 5
STUDIO = dict(lede='A typical rickhouse map and barrel record, built on your Sutton data with Studio. Want it different? Describe the change.',
              examples=['Add a barrel char field', 'Change rickhouse layout', 'Add a gauge alert', 'Track cooperage supplier'],
              built_on='Barrels, lots, locations and gauges', change='Fields, layout and alerts')
STORY = [('Rickhouse', 'whs', 'row card', 'center left'), ('Row 4', 'whs', 'grid cell', 'center'),
         ('Barrel record', 'whs', 'panel button', 'right'), ('Barrel record', 'whs', 'level header', 'left'),
         ('Dump selection', 'whs', 'primary button', 'bottom right')]

CSS = (
 '.tl{display:grid;grid-template-columns:repeat(4,1fr);gap:8px}.tile{border:1px solid #E4E4E7;border-radius:8px;padding:7px 10px;display:flex;flex-direction:column;gap:1px;background:#fff}.tile small{font-size:8.8px;color:#71717A}.tile b{font-family:"JetBrains Mono",ui-monospace,monospace;font-size:15px;font-weight:600}'
 '.rg{display:grid;grid-template-columns:repeat(3,1fr);gap:8px}'
 '.rc{border:1px solid #E4E4E7;border-radius:8px;background:#fff;padding:8px 9px;display:flex;flex-direction:column;gap:6px;text-align:left;font:inherit;color:#18181B;cursor:pointer;transition:box-shadow .2s,border-color .2s}.rc:hover,.rc.fakehover{border-color:#18181B;box-shadow:0 0 0 1px #18181B}.rc:focus-visible{outline:2px solid #18181B;outline-offset:1px}'
 '.rc .t{display:flex;justify-content:space-between;align-items:center;font-size:10.2px;font-weight:600}.rc .t span{font-family:"JetBrains Mono",ui-monospace,monospace;font-weight:500;font-size:9.2px;color:#71717A}'
 '.dots{display:grid;grid-template-columns:repeat(10,1fr);gap:2px}.dots i{height:7px;border-radius:2px;background:#D4D4D8}.dots i.f{background:#3F3F46}.dots i.e{background:transparent;box-shadow:inset 0 0 0 1px #D4D4D8}'
 '.lgd{display:flex;align-items:center;gap:12px;font-size:8.8px;color:#71717A;white-space:nowrap}.lgd i{display:inline-block;width:9px;height:9px;border-radius:2px;margin-right:4px;vertical-align:-1px}'
 '.mv .row{grid-template-columns:70px 1fr 90px 60px;font-size:9.6px;white-space:nowrap}.mv .row span:nth-child(n+3){text-align:right}'
 '.bw{display:grid;grid-template-columns:1fr 196px;gap:10px;align-items:start}.bw>div{display:flex;flex-direction:column;gap:10px}'
 '.gd{padding:8px 9px 9px}.gl{display:grid;grid-template-columns:44px repeat(10,1fr);gap:3px;align-items:center}.gl+.gl{margin-top:3px}.gl.hp span{font-size:8.4px;color:#A1A1AA;text-align:center;font-family:"JetBrains Mono",ui-monospace,monospace}'
 '.lh{height:30px;display:flex;align-items:center;border:0;border-radius:5px;background:#FAFAFA;font:inherit;font-size:9px;color:#52525B;text-align:left;padding:0 6px;white-space:nowrap}button.lh{cursor:pointer;transition:background-color .2s}button.lh:hover,button.lh.fakehover{background:#F0F0F1;color:#18181B}.lh:focus-visible,.bc2:focus-visible{outline:2px solid #18181B;outline-offset:1px}'
 '.bc2{height:30px;border:0;border-radius:6px;background:#E4E4E7;padding:0;position:relative;cursor:pointer;display:grid;place-items:center;transition:background-color .25s,box-shadow .2s}.bc2::before{content:"";width:12px;height:16px;border-radius:5px;border:1.5px solid rgba(0,0,0,.18)}'
 '.bc2:hover,.bc2.fakehover{box-shadow:0 0 0 2px #18181B}.bc2.cur{box-shadow:0 0 0 2px #18181B;background:#FFF4D6}.bc2.sel{background:#18181B}.bc2.sel::before{border-color:rgba(255,255,255,.55)}.bc2.dmp{background:transparent;box-shadow:inset 0 0 0 1px #D4D4D8;border:1px dashed #D4D4D8}.bc2.dmp::before{display:none}'
 '.pn .bd{padding:9px 11px;display:flex;flex-direction:column;gap:7px}.kvl{display:flex;justify-content:space-between;gap:8px;font-size:9.6px;white-space:nowrap}.kvl span:first-child{color:#71717A}.kvl b{font-weight:500}.kvl .mono{font-weight:500}'
 '.cmp{display:flex;flex-direction:column;gap:4px;padding:8px 9px;border:1px solid #E4E4E7;border-radius:7px;background:#FAFAFA}.bar{height:8px;border-radius:4px;background:#E4E4E7;position:relative;overflow:hidden}.bar i{position:absolute;left:0;top:0;bottom:0;background:#3F3F46;border-radius:4px;transition:width .6s ease}'
 '.bt.w{width:100%;justify-content:center;display:flex;padding:7px 10px}.gz{display:grid;grid-template-columns:1fr 1fr;gap:1px 12px;font-size:9.2px}.gz span{display:flex;justify-content:space-between}.gz span b{font-family:"JetBrains Mono",ui-monospace,monospace;font-weight:500}'
 '.lt .row{grid-template-columns:1fr 70px;font-size:9.6px;min-height:23px}.lt .row span:last-child{text-align:right;font-family:"JetBrains Mono",ui-monospace,monospace}.lt .row.tot{font-weight:600}'
 '.note{border:1px solid #E4E4E7;background:#FAFAFA;border-radius:8px;padding:8px 10px;font-size:9.6px;line-height:1.45;color:#52525B}'
 '.shot.ph .rg{grid-template-columns:1fr 1fr;gap:6px}.shot.ph .rc{min-height:40px;padding:6px 8px;gap:4px}.shot.ph .dots i{height:4px}.shot.ph .rc .t{font-size:10.2px}'
 '.shot.ph .gl{grid-template-columns:36px repeat(6,1fr)}.shot.ph .bc2,.shot.ph .lh{height:22px}.shot.ph.nar .bc2,.shot.ph.nar .lh{height:17px}.shot.ph.nar .ph2 .tile{padding:3px 8px}.shot.ph.nar .gd{padding:6px 8px}.shot.ph .bc2::before{width:9px;height:11px}'
 '.ph2{display:grid;grid-template-columns:1fr 1fr;gap:6px}.ph2 .tile{padding:5px 9px}.ph2 .tile b{font-size:12px}.shot.ph .bt.w{min-height:40px;font-size:10.8px}.pline{font-size:9.8px;color:#52525B;display:flex;justify-content:space-between}.pline b{color:#18181B;font-family:"JetBrains Mono",ui-monospace,monospace}'
 '.shot.ph.nar .xn{display:none}.tk .bd{padding:9px 11px;display:flex;flex-direction:column;gap:6px}'
)

WIN = ''

JS = r'''
var FOC='.rail .ni,.bc,.phd>*,.bn .bi,.pg .tile,.pg .ct,.pg .rc,.pg .row,.pg .gl>*,.pg .lgd,.pg .kvl,.pg .cmp,.pg .bt,.pg .gz,.pg .note,.pg .pline';
var G=[512,510,508,514,511,509,513,510,512,511];
var FILL=530,GAUGE=512;
var S;
function lotOf(r,l,p){if(r===1||r===3||r===4||r===5)return r===1?'DS-0298':r===3?'DS-0388':'DS-0412';if(r===2)return l===5&&p>6?'':'DS-0331';if(l<=2)return 'DS-0412';return p<=8?'DS-0418':'';}
function dumped(l){return S.dump&&l===3;}
function lotCount(){var n=0;for(var r=1;r<=6;r++)for(var l=1;l<=5;l++)for(var p=1;p<=10;p++)if(lotOf(r,l,p)==='DS-0412'&&!(r===4&&dumped(l)))n++;return n;}
function rowCount(r){var n=0;for(var l=1;l<=5;l++)for(var p=1;p<=10;p++)if(lotOf(r,l,p)&&!(r===4&&dumped(l)))n++;return n;}
function rowLots(r){var o=[];for(var l=1;l<=5;l++)for(var p=1;p<=10;p++){var x=lotOf(r,l,p);if(x&&o.indexOf(x)<0)o.push(x);}return o.join(', ');}
function v1(t){return (t/10).toFixed(1);}
function gsum(){var t=0;G.forEach(function(g){t+=g;});return t;}
function cellCls(l,p){var c='bc2';if(dumped(l))return c+' dmp';if(S.sel&&l===3)c+=' sel';if(S.cur&&l===3&&p===9&&!S.sel)c+=' cur';return c;}
function grid(P){var ps=P?[5,6,7,8,9,10]:[1,2,3,4,5,6,7,8,9,10],h='<div class="gl hp"><span></span>'+ps.map(function(p){return '<span>'+p+'</span>';}).join('')+'</div>';
 for(var l=5;l>=1;l--){var lh=(!P&&l===3&&!S.dump)?'<button type="button" class="lh" id="lv-3" aria-label="Select level 3">Level 3</button>':'<span class="lh">'+(P?'L':'Level ')+l+'</span>';
  h+='<div class="gl">'+lh+ps.map(function(p){return dumped(l)?'<span class="'+cellCls(l,p)+'"></span>':'<button type="button" class="'+cellCls(l,p)+'" id="b-'+l+'-'+p+'" aria-label="Barrel 4-'+l+'-'+(p<10?'0':'')+p+'"></button>';}).join('')+'</div>';}
 return h;}
function kvl(a,b,id){return '<div class="kvl"><span>'+a+'</span><b'+(id?' id="'+id+'"':'')+'>'+b+'</b></div>';}
function cmpBox(){return '<div class="cmp in"><div class="kvl"><span>Fill</span><b class="mono">'+v1(FILL)+' L</b></div><div class="bar"><i style="width:100%"></i></div><div class="kvl"><span>Gauge</span><b class="mono">'+v1(GAUGE)+' L</b></div><div class="bar"><i style="width:'+(GAUGE*100/FILL).toFixed(1)+'%"></i></div><div class="kvl"><span>Loss</span><b><span class="ch c-warn" id="loss">'+v1(FILL-GAUGE)+' L, '+(Math.round((FILL-GAUGE)*1000/FILL)/10).toFixed(1)+'%</span></b></div></div>';}
function panel(){var h;
 if(S.dump){h='<div class="cd pn"><div class="ct">Dump DMP-0207<span class="ch c-ok">Posted</span></div><div class="bd">'+kvl('Barrels','10')+kvl('Into','Blend tank BT-2')+kvl('Volume','<span class="mono" id="d-vol">'+v1(gsum())+' L</span>')+kvl('Lot DS-0412','<span class="mono">120 to <span id="d-lot">'+lotCount()+'</span></span>')+'<div class="note">Level 3 is empty and ready to refill. BT-2 now holds '+v1(gsum())+' L for blend BL-RYE-07.</div></div></div>';}
 else if(S.sel){h='<div class="cd pn"><div class="ct">Dump to blend tank<span class="mut" style="font-weight:500">10 selected</span></div><div class="bd"><div class="gz">'+G.map(function(g,i){return '<span><span class="mut">4-3-'+(i<9?'0':'')+(i+1)+'</span><b>'+v1(g)+'</b></span>';}).join('')+'</div>'+kvl('Gauge total','<span class="mono" id="s-tot">'+v1(gsum())+' L</span>')+kvl('Destination','Blend tank BT-2')+'<button type="button" class="bt pri w" id="dump">Dump to BT-2</button></div></div>';}
 else if(S.cur){h='<div class="cd pn"><div class="ct">Barrel 4-3-09<span class="ch c-idle">In storage</span></div><div class="bd">'+kvl('Lot','<span class="mono">DS-0412</span>')+kvl('Source batch','<span class="mono">DS-0412</span>, mash bill v3')+kvl('Filled','Mar 14, 2022')+kvl('Age','4 yr 8 mo')+kvl('Fill','<span class="mono">'+v1(FILL)+' L</span>')+kvl('Gauge, Nov 10','<span class="mono" id="r-g">'+v1(GAUGE)+' L</span>')+(S.cmp?cmpBox():'<button type="button" class="bt w" id="cmp">Compare gauge with fill</button>')+'</div></div>';}
 else h='<div class="cd pn"><div class="ct">Lot DS-0412<span class="mut" style="font-weight:500">Straight rye</span></div><div class="bd">'+kvl('Barrels','<span class="mono">120</span>')+kvl('Filled','Mar 14, 2022')+kvl('Source batch','<span class="mono">DS-0412</span>')+kvl('Locations','Rows 4, 5, 6')+'<div class="note">Click a barrel to open its record.</div></div></div>';
 return h;}
function lotCard(){return '<div class="cd lt"><div class="ct">Where lot DS-0412 sits<span class="mut" style="font-weight:500">Rickhouse B</span></div><div class="row"><span>Row 4, levels 1 to 5</span><span>'+rowCount(4)+'</span></div><div class="row"><span>Row 5, levels 1 to 5</span><span>50</span></div><div class="row"><span>Row 6, levels 1 and 2</span><span>20</span></div><div class="row tot"><span>Lot total</span><span id="lot">'+lotCount()+'</span></div></div>';}
function tank(){var v=S.dump?gsum():0;return '<div class="cd tk"><div class="ct">Blend tank BT-2<span class="ch '+(S.dump?'c-ok">Filling':'c-idle">Empty')+'</span></div><div class="bd"><div class="kvl"><span>Volume</span><b class="mono" id="tk">'+v1(v)+' L of 2,000.0 L</b></div><div class="bar"><i style="width:'+(v/200).toFixed(1)+'%"></i></div><div class="kvl"><span>For blend</span><b>BL-RYE-07, Barrel Rye</b></div></div></div>';}
function render(){var P=ph(),h='';
var bc0=['Warehouse',['Rickhouse B','cb-rh']];
if(S.scr==='house'){setNav({m:'whs',bc:['Warehouse','Rickhouse B'],t:'Rickhouse B',chip:['c-idle','6 rows, 5 levels'],scr:'Rickhouse'});
 var rows=[1,2,3,4,5,6].map(function(r){var d='';for(var l=5;l>=1;l--)for(var p=1;p<=10;p++){var x=lotOf(r,l,p);d+='<i class="'+(!x?'e':x==='DS-0412'?'f':'')+'"></i>';}
  return '<button type="button" class="rc" id="row-'+r+'"><span class="t">Row '+r+'<span>'+rowCount(r)+(P?'':' barrels')+'</span></span>'+(P?'':'<span class="dots">'+d+'</span><span class="mut" style="font-size:8.8px">'+rowLots(r)+'</span>')+'</button>';}).join('');
 if(P)h='<div class="pline xn"><span>Barrels in house</span><b>290</b></div><div class="rg">'+rows+'</div>';
 else{h='<div class="tl"><div class="tile"><small>Barrels in house</small><b>290</b></div><div class="tile"><small>Lots</small><b>5</b></div><div class="tile"><small>Empty slots</small><b>10</b></div><div class="tile"><small>Levels per row</small><b>5</b></div></div>';
  h+='<div class="rg">'+rows+'</div><div class="lgd"><span><i style="background:#3F3F46"></i>Lot DS-0412</span><span><i style="background:#D4D4D8"></i>Other lots</span><span><i style="box-shadow:inset 0 0 0 1px #D4D4D8"></i>Empty slot</span></div>';
  h+='<div class="cd mv"><div class="ct">Recent movements<span class="mut" style="font-weight:500">Rickhouse B</span></div>'+[['Gauge','Row 4, 50 barrels','DS-0412','Nov 10'],['Fill','Row 6, 24 barrels','DS-0418','Oct 21'],['Rotate','Row 2, 4 barrels','DS-0331','Oct 02'],['Gauge','Row 3, 50 barrels','DS-0388','Sep 18'],['Fill','Row 5, 50 barrels','DS-0412','Mar 15'],['Gauge','Row 1, 50 barrels','DS-0298','Mar 02'],['Fill','Row 4, 50 barrels','DS-0412','Mar 14']].map(function(x){return '<div class="row"><span>'+x[0]+'</span><span>'+x[1]+'</span><span class="mono">'+x[2]+'</span><span class="mono mut">'+x[3]+'</span></div>';}).join('')+'</div>';}}
else if(P&&S.scr==='rec'){setNav({m:'whs',bc:bc0.concat([['Row 4','cb-r4'],'Barrel 4-3-09']),t:'Barrel 4-3-09',chip:['c-idle','DS-0412'],scr:'Barrel record',back:1});
 h='<div class="ph2"><div class="tile"><small>Filled</small><b style="font-size:11px">Mar 14, 2022</b></div><div class="tile"><small>Age</small><b style="font-size:11px">4 yr 8 mo</b></div><div class="tile"><small>Fill</small><b>'+v1(FILL)+' L</b></div><div class="tile"><small>Gauge</small><b id="r-g">'+v1(GAUGE)+' L</b></div></div>';
 h+=S.cmp?'<div class="pline"><span>Loss since fill</span><span class="ch c-warn" id="loss">'+v1(FILL-GAUGE)+' L, 3.4%</span></div><button type="button" class="bt w" id="sel3">Select level 3 for a dump</button>':'<div class="pline xn"><span>Source batch</span><b>DS-0412</b></div><button type="button" class="bt w" id="cmp">Compare gauge with fill</button>';}
else if(P&&S.scr==='sel'){setNav({m:'whs',bc:bc0.concat([['Row 4','cb-r4'],'Dump to BT-2']),t:'Dump to BT-2',chip:['c-idle','10 barrels'],scr:'Dump selection',back:1});
 h='<div class="ph2"><div class="tile"><small>Barrels</small><b>10</b></div><div class="tile"><small>Gauge total</small><b id="s-tot">'+v1(gsum())+' L</b></div></div><div class="pline mono" style="font-size:9.2px;line-height:1.5;display:block">'+G.map(v1).join(', ')+'</div><button type="button" class="bt pri w" id="dump">Dump to BT-2</button>';}
else{var scr=S.dump?'Dump posted':S.sel?'Dump selection':S.cur?'Barrel record':'Row 4',last=S.dump?'DMP-0207':S.sel?'Dump to BT-2':S.cur?'Barrel 4-3-09':null;
 setNav({m:'whs',bc:last?bc0.concat([['Row 4','cb-r4'],last]):bc0.concat(['Row 4']),t:'Row 4',chip:S.dump?['c-ok','Dump posted']:['c-idle','DS-0412'],scr:scr,back:1});
 if(P){h='<div class="pline"><span>Lot DS-0412 <b id="lot">'+lotCount()+'</b></span><span>'+(S.dump?'BT-2 <b id="d-vol">'+v1(gsum())+' L</b>':'Positions 5 to 10')+'</span></div><div class="cd gd">'+grid(true)+'</div>';}
 else{h='<div class="bw"><div><div class="cd gd">'+grid(false)+'</div><div class="lgd"><span><i style="background:#E4E4E7"></i>Barrel</span><span><i style="background:#18181B"></i>Selected</span><span><i style="box-shadow:inset 0 0 0 1px #D4D4D8"></i>Empty</span><span>Level 5 is the top</span></div>'+lotCard()+tank()+'</div><div>'+panel()+'</div></div>';}}
if(P)h+=xw(S.scr==='house'?[['Levels per row','5'],['Lot DS-0412','120 barrels'],['Empty slots','10']]:S.scr==='rec'?[['Lot','DS-0412'],['Location','Row 4, level 3, position 9'],['Last gauged','Nov 10']]:S.scr==='sel'?[['Destination','Blend tank BT-2'],['Level 3','Positions 1 to 10'],['Lot after the dump','110 barrels']]:[['Rows 4, 5, 6',rowCount(4)+', 50, 20'],['Blend tank BT-2',S.dump?v1(gsum())+' L':'Empty']]);
$('pg').innerHTML=h;}
function resetState(){S={scr:'house',cur:false,cmp:false,sel:false,dump:false};render();}
var CAPAT=function(hh){return ph()?{l:8,t:5}:{l:14,t:visH()-hh-40};};
var ST=[
{id:'row',target:function(){return $('row-4');},prompt:'Open row 4',where:'below',run:function(){S.scr='row';render();},
 after:['Row 4 opens barrel by barrel','5 levels by 10 positions, all 50 from lot DS-0412. The lot holds 120 barrels across rows 4 to 6.'],pc:'Row 4: 50 barrels of DS-0412'},
{id:'barrel',target:function(){return $('b-3-9');},prompt:'Open barrel 4-3-09',where:'below',run:function(){S.cur=true;S.scr='rec';render();},
 after:['The barrel record opens','Barrel 4-3-09 was filled Mar 14, 2022 from batch DS-0412. Aged 4 years 8 months, last gauged at 51.2 L.'],pc:'Barrel 4-3-09, gauged at 51.2 L'},
{id:'cmp',target:function(){return $('cmp');},prompt:'Compare gauge with fill',where:'below',run:function(){S.cmp=true;render();},
 after:['Gauge against fill shows the loss','Filled at 53.0 L, gauged at 51.2 L: 1.8 L lost in the barrel, 3.4% of the fill.'],pc:'1.8 L lost, 3.4% of the fill'},
{id:'sel',target:function(){return ph()?$('sel3'):$('lv-3');},prompt:function(){return ph()?'Select level 3 for a dump':'Select all ten barrels on level 3';},where:function(){return ph()?'below':'right';},run:function(){S.sel=true;S.scr='sel';render();},
 after:['Ten barrels selected for the dump','All of level 3, gauged from 50.8 to 51.4 L: 511.0 L in total, bound for blend tank BT-2.'],pc:'Ten barrels, 511.0 L'},
{id:'dump',target:function(){return $('dump');},prompt:'Dump them to blend tank BT-2',where:'above',run:function(){S.dump=true;S.scr='row';render();},
 after:['The dump posts and the lot count updates','511.0 L into blend tank BT-2. Lot DS-0412 drops from 120 to 110 barrels.'],pc:'BT-2 holds 511.0 L, lot at 110'}];
ST.forEach(function(s){['prompt','where'].forEach(function(k){if(typeof s[k]==='function'){var f=s[k];Object.defineProperty(s,k,{get:f});}});});
'''
