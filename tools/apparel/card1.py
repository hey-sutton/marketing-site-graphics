"""Apparel card 1: Size & Color Matrix. Layout: style panel on the left, size by color grid in the middle, materials panel on the right."""
SUMMARY = 'Size & Color Matrix (one style held once with 15 variants, low stock by variant, a production run entered as one size grid, fabric by size, release to cutting)'
ARIA = 'Interactive product screen: generate the size and color grid for crew tee ST-210, find the low stock variants, enter production run RUN-0412 as one grid, calculate fabric by size and release it to cutting'
STEPS = 5
STUDIO = dict(lede='A typical style and size run screen, built on your Sutton data with Studio. Want it different? Describe the change.',
              examples=['A size curve planner', 'A reorder view by size', 'A seasonal run builder', 'A low stock alert by color'],
              built_on='Styles, variants, stock and production runs', change='Sizes, fields and views')

CSS = (
 '.b1{display:grid;grid-template-columns:166px 1fr 168px;gap:12px;padding:12px 40px 0 16px;height:596px}'
 '.col{display:flex;flex-direction:column;gap:10px;min-height:0}'
 '.sty .g{display:flex;flex-direction:column;gap:7px;padding:9px 11px}.sty .ft{padding:0 11px 10px}.sty .ft .bt{width:100%}'
 '.rec{flex:none}.rec+.rec{flex:1 1 0;min-height:0}.rec .row{grid-template-columns:62px 1fr;min-height:23px;font-size:9.6px}.foh .row{grid-template-columns:1fr auto;min-height:23px;font-size:9.6px}'
 '.flt{display:flex;align-items:center;gap:6px;min-height:24px}.fc{border:1px solid #E4E4E7;border-radius:999px;background:#fff;padding:4px 10px;font-size:9.8px;cursor:pointer;transition:background-color .2s,border-color .2s,color .2s}.fc b{font-weight:600;margin-left:4px}.fc.on{background:#18181B;border-color:#18181B;color:#fff}.fc:focus-visible{outline:2px solid #18181B;outline-offset:2px}'
 '.mx .row{grid-template-columns:56px repeat(5,1fr) 52px;min-height:30px;padding:0 9px;gap:6px}.mx .row.t{background:#FAFAFA;font-weight:600}'
 '.cell{font-family:"JetBrains Mono",ui-monospace,monospace;font-size:10.4px;text-align:center;border-radius:5px;padding:4px 0;transition:background-color .35s,color .35s}.cell.low{background:#FEE2E2;color:#B91C1C;font-weight:600}.mx.lowon .cell:not(.low){color:#A1A1AA}'
 '.mx .r2{text-align:center}.sw{display:inline-block;width:9px;height:9px;border-radius:2px;margin-right:5px;vertical-align:-1px;border:1px solid rgba(0,0,0,.12)}'
 '.ent .row{grid-template-columns:56px repeat(5,1fr) 52px;min-height:30px;padding:0 9px;gap:6px}.ent .row.t{background:#FAFAFA;font-weight:600}'
 '.ent input{font:inherit;font-family:"JetBrains Mono",ui-monospace,monospace;font-size:10px;width:100%;padding:4px 3px;text-align:center;border:1px solid #D4D4D8;border-radius:5px;background:#fff}.ent input.bad{border-color:#F87171;background:#FEF2F2}'
 '.ent .ft{display:flex;align-items:center;justify-content:space-between;gap:8px;padding:8px 11px;border-top:1px solid #F0F0F1}.ent .em2{color:#B91C1C;font-size:8.8px;display:none}.ent.err .em2{display:inline}'
 '.mat{flex:1 1 0;min-height:0;display:flex;flex-direction:column}.mat .row{grid-template-columns:24px 1fr 62px;min-height:23px;font-size:9.6px;white-space:nowrap;padding:0 9px;gap:5px}.mat .row.t{background:#FAFAFA;font-weight:600}.mat .pad{padding:9px 11px;display:flex;flex-direction:column;gap:8px}'
 '.mat .ft{padding:0 11px 10px}.mat .ft .bt{width:100%}'
)

WIN = (
 '<div class="hd"><svg width="16" height="16" viewBox="0 0 16 16" fill="none" aria-hidden="true"><path d="M5.5 2.5L2 4.5l1.2 3 1.6-.6V13.5h6.4V6.9l1.6.6 1.2-3-3.5-2a2.5 2.5 0 0 1-5 0z" stroke="#18181B" stroke-width="1.2" stroke-linejoin="round"/></svg>'
 '<span class="tt">Crew tee <span class="mono">ST-210</span></span><span class="ch c-idle" id="hst">No grid yet</span><span class="sb grow">Style, sizes and colors</span></div>'
 '<div class="b1"><div class="col">'
 '<div class="cd sty frm"><div class="ct">Style<span class="mono mut" style="font-weight:500">ST-210</span></div><div class="g">'
 '<label class="fld" id="fsz"><small>Sizes</small><input id="isz" value="XS, S, M, L, XL" autocomplete="off" spellcheck="false"><span class="em">Use XS, S, M, L, XL</span></label>'
 '<label class="fld" id="fco"><small>Colors</small><input id="ico" value="Black, Navy, Sand" autocomplete="off" spellcheck="false"><span class="em">Use Black, Navy, Sand</span></label>'
 '<div class="kv"><small>Reorder point</small><b class="mono">15 a variant</b></div></div>'
 '<div class="ft"><button type="button" class="bt pri" id="gen">Generate grid</button></div></div>'
 '<div class="cd rec"><div class="ct">Style record</div>'
 '<div class="row"><span class="mut">Season</span><span>Fall 2026 core</span></div><div class="row"><span class="mut">Fabric</span><span>Cotton jersey, 180 gsm</span></div>'
 '<div class="row"><span class="mut">Wholesale</span><span class="mono">$11.50</span></div><div class="row"><span class="mut">Retail</span><span class="mono">$24.00</span></div>'
 '<div class="row"><span class="mut">Owner</span><span>T. Moreno</span></div></div>'
 '<div class="cd rec"><div class="ct">Recent runs</div><div class="row"><span class="mono mut">RUN-0398</span><span>240 pieces, packed 10/02</span></div><div class="row"><span class="mono mut">RUN-0371</span><span>300 pieces, packed 08/19</span></div><div class="row"><span class="mono mut">RUN-0344</span><span>180 pieces, packed 07/08</span></div></div>'
 '</div>'
 '<div class="col" id="mid"></div>'
 '<div class="col"><div class="cd mat" id="mat"></div>'
 '<div class="cd foh"><div class="ct">Fabric on hand<span class="mut" style="font-weight:500">Cotton jersey</span></div><div class="row"><span class="mono">FAB-BLK</span><span class="mono r">310.0 yd</span></div><div class="row"><span class="mono">FAB-NVY</span><span class="mono r">260.0 yd</span></div><div class="row"><span class="mono">FAB-SND</span><span class="mono r">180.0 yd</span></div></div></div>'
 '</div>'
)

JS = r'''
var FOC='.hd>*,.sty .ct,.sty .fld,.sty .kv,.sty .bt,.rec,.flt .fc,.mx .row,.mx .ct,.ent .ct,.ent .row,.ent .ft>*,.mat .ct,.mat .pad>*,.mat .row,.mat .ft';
var SIZES=['XS','S','M','L','XL'],COLORS=[['Black','#18181B'],['Navy','#1E3A8A'],['Sand','#D6C7A1']],RP=15;
var STOCK={Black:[24,60,85,12,40],Navy:[18,44,70,9,31],Sand:[12,30,52,6,22]};
var RUN0={Black:[10,20,30,60,20],Navy:[10,20,30,50,20],Sand:[10,10,20,40,10]};
var YD=[1.0,1.1,1.2,1.3,1.4];
var S;
function sum(a){return a.reduce(function(x,y){return x+y;},0);}
function colTot(M,j){return COLORS.reduce(function(a,c){return a+M[c[0]][j];},0);}
function low(c,j){return STOCK[c][j]<RP;}
function nLow(){var n=0;COLORS.forEach(function(c){STOCK[c[0]].forEach(function(v){if(v<RP)n++;});});return n;}
function y1(n){return n.toFixed(1);}
function readRun(){var bad=false,M={};COLORS.forEach(function(c){M[c[0]]=SIZES.map(function(s,j){var e=$('q-'+c[0]+'-'+j),v=e?String(e.value).trim():'';var ok=/^\d{1,4}$/.test(v);if(e)e.classList.toggle('bad',!ok);if(!ok)bad=true;return ok?parseInt(v,10):0;});});return{M:M,bad:bad};}
function render(){var mid='';
$('hst').textContent=S.rel?'RUN-0412 released':S.grid?'15 variants':'No grid yet';$('hst').className='ch '+(S.rel?'c-ok':S.grid?'c-info':'c-idle');
var g=$('gen');g.disabled=S.grid;g.className='bt '+(S.grid?'done':'pri');g.textContent=S.grid?'Grid ready':'Generate grid';
if(!S.grid){mid='<div class="cd" style="flex:1"><div class="ct">Stock by size and color</div><div style="padding:10px 11px"><div class="empt"><b>No grid yet</b><span>Generate the grid to hold ST-210 once, with every size and color counted on its own.</span></div></div></div>';}
else{mid='<div class="flt" id="flt"><button type="button" class="fc'+(S.low?'':' on')+'" data-f="all">All<b>15</b></button><button type="button" class="fc'+(S.low?' on':'')+'" data-f="low" id="flow">Low stock<b>'+nLow()+'</b></button><span class="mut" style="margin-left:auto;font-size:9px">Reorder point '+RP+'</span></div>';
var rows='<div class="row h"><span>Color</span>'+SIZES.map(function(s){return '<span class="r2">'+s+'</span>';}).join('')+'<span class="r">Total</span></div>';
COLORS.forEach(function(c,i){rows+='<div class="row'+(S.anim?' in':'')+'" style="animation-delay:'+(i*70)+'ms"><span><i class="sw" style="background:'+c[1]+'"></i>'+c[0]+'</span>'+STOCK[c[0]].map(function(v,j){return '<span class="cell'+(S.low&&low(c[0],j)?' low':'')+'">'+v+'</span>';}).join('')+'<span class="mono r">'+sum(STOCK[c[0]])+'</span></div>';});
var gt=0;rows+='<div class="row t"><span>Total</span>'+SIZES.map(function(s,j){var t=colTot(STOCK,j);gt+=t;return '<span class="mono r2">'+t+'</span>';}).join('')+'<span class="mono r">'+gt+'</span></div>';
mid+='<div class="cd mx'+(S.low?' lowon':'')+'"><div class="ct">Stock by size and color<span class="mut" style="font-weight:500">Pieces on hand</span></div>'+rows+'</div>';
if(!S.run){mid+='<div class="frm"><button type="button" class="bt pri" id="nrun">New production run</button></div>';}
else{var er='<div class="row h"><span>Color</span>'+SIZES.map(function(s){return '<span class="r2">'+s+'</span>';}).join('')+'<span class="r">Total</span></div>';
COLORS.forEach(function(c){er+='<div class="row"><span><i class="sw" style="background:'+c[1]+'"></i>'+c[0]+'</span>'+S.M[c[0]].map(function(v,j){return S.mat?'<span class="mono r2">'+v+'</span>':'<span><input id="q-'+c[0]+'-'+j+'" value="'+v+'" inputmode="numeric" aria-label="'+c[0]+' '+SIZES[j]+'"></span>';}).join('')+'<span class="mono r" id="rt-'+c[0]+'">'+sum(S.M[c[0]])+'</span></div>';});
er+='<div class="row t"><span>Total</span>'+SIZES.map(function(s,j){return '<span class="mono r2" id="ct-'+j+'">'+colTot(S.M,j)+'</span>';}).join('')+'<span class="mono r" id="gt">'+COLORS.reduce(function(a,c){return a+sum(S.M[c[0]]);},0)+'</span></div>';
mid+='<div class="cd ent frm'+(S.anim&&!S.mat?' in':'')+'" id="ent"><div class="ct">Production run <span class="mono">RUN-0412</span><span class="ch '+(S.rel?'c-ok':S.mat?'c-info':'c-warn')+'">'+(S.rel?'Released':S.mat?'Planned':'Draft')+'</span></div>'+er+
(S.mat?'':'<div class="ft"><span class="em2">Enter whole numbers in every cell</span><span class="grow"></span><button type="button" class="bt pri" id="calc">Calculate materials</button></div>')+'</div>';}}
$('mid').innerHTML=mid;
var m='<div class="ct">Materials<span class="mut" style="font-weight:500">Per run</span></div>';
if(!S.mat)m+='<div class="pad"><div class="empt"><b>No run yet</b><span>Fabric and labels by size show up when you calculate a run.</span></div></div>';
else{var tot=0,r='<div class="row h"><span>Size</span><span class="r">Pcs x yd</span><span class="r">Fabric</span></div>';SIZES.forEach(function(s,j){var q=colTot(S.M,j),y=Math.round(q*YD[j]*10)/10;tot+=y;r+='<div class="row in" style="animation-delay:'+(j*60)+'ms"><span>'+s+'</span><span class="mono r mut">'+q+' x '+y1(YD[j])+'</span><span class="mono r">'+y1(y)+' yd</span></div>';});
var pcs=COLORS.reduce(function(a,c){return a+sum(S.M[c[0]]);},0);
r+='<div class="row t"><span></span><span>Fabric</span><span class="mono r" id="ftot">'+y1(Math.round(tot*10)/10)+' yd</span></div><div class="row t"><span></span><span>Neck labels</span><span class="mono r" id="lab">'+pcs+'</span></div>';
m+=r+'<div class="pad"><span class="mut" style="font-size:9.2px;line-height:1.4">Large sizes use more cloth, so a run heavy on L needs more fabric.</span>'+(S.rel?'<span class="ch c-ok" style="align-self:flex-start">Cut order CUT-0412 created</span>':'')+'</div>'+
'<div class="ft">'+(S.rel?'<button type="button" class="bt done" disabled>Released to cutting</button>':'<button type="button" class="bt pri" id="rel">Release to cutting</button>')+'</div>';}
$('mat').innerHTML=m;S.anim=false;}
$('mid').addEventListener('click',function(e){var b=e.target.closest&&e.target.closest('.fc');if(!b)return;S.low=b.getAttribute('data-f')==='low';render();});
$('mid').addEventListener('input',function(e){if(!/^q-/.test(e.target.id))return;var r=readRun();S.M=r.M;COLORS.forEach(function(c){$('rt-'+c[0]).textContent=sum(r.M[c[0]]);});SIZES.forEach(function(s,j){$('ct-'+j).textContent=colTot(r.M,j);});$('gt').textContent=COLORS.reduce(function(a,c){return a+sum(r.M[c[0]]);},0);$('ent').classList.toggle('err',r.bad);});
function copyRun(){var M={};COLORS.forEach(function(c){M[c[0]]=RUN0[c[0]].slice();});return M;}
function resetState(){S={grid:false,low:false,run:false,mat:false,rel:false,M:copyRun(),anim:false};$('isz').value='XS, S, M, L, XL';$('ico').value='Black, Navy, Sand';$('fsz').classList.remove('err');$('fco').classList.remove('err');render();}
function norm(v){return String(v).toUpperCase().replace(/\s+/g,'');}
var CAPAT=function(hh){return{l:14,t:visH()-hh-14};};
var ST=[
{id:'gen',target:function(){return $('gen');},prompt:'Click Generate grid',where:'below',ok:function(){var a=norm($('isz').value)!=='XS,S,M,L,XL',b=norm($('ico').value)!=='BLACK,NAVY,SAND';$('fsz').classList.toggle('err',a);$('fco').classList.toggle('err',b);return !(a||b);},
 run:function(){S.grid=true;S.anim=true;render();},after:['Every size and color counted on its own','ST-210 is held once, with 15 variants and stock for each.']},
{id:'low',target:function(){return $('flow');},prompt:'Click Low stock',where:'below',run:function(){S.low=true;render();},after:['Four of fifteen variants are running short','Black L 12, Navy L 9, Sand L 6 and Sand XS 12. Three are size L.']},
{id:'run',target:function(){return $('nrun');},prompt:'Click New production run',where:'below',run:function(){S.run=true;S.anim=true;render();},after:['Enter the whole size run in one grid','RUN-0412 is 360 pieces, with row, column and grand totals.']},
{id:'calc',target:function(){return $('calc');},prompt:'Click Calculate materials',where:'below',ok:function(){var r=readRun();$('ent').classList.toggle('err',r.bad);if(!r.bad)S.M=r.M;return !r.bad;},
 run:function(){var r=readRun();if(!r.bad)S.M=r.M;S.mat=true;S.anim=true;render();},after:function(){var t=0;SIZES.forEach(function(s,j){t+=Math.round(colTot(S.M,j)*YD[j]*10)/10;});return['Each size draws its own fabric',y1(Math.round(t*10)/10)+' yd and '+COLORS.reduce(function(a,c){return a+sum(S.M[c[0]]);},0)+' neck labels. Size L alone needs '+y1(Math.round(colTot(S.M,3)*YD[3]*10)/10)+' yd.'];}},
{id:'rel',target:function(){return $('rel');},prompt:'Click Release to cutting',where:'below',run:function(){S.rel=true;render();},after:['Released to the cutting room','Cut order CUT-0412 carries the sizes and fabric already worked out.']}];
'''
