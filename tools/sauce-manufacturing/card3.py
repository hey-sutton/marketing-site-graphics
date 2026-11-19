"""Sauce manufacturing card 3: Bulk Sauce to Filled Units. Layout: list and detail.
Left: the holding tanks, and the remaining bulk in the open tank with its history. Right: the bulk lot record with the
preset split (Original 200 gal in 12 oz, Original 80 gal in 32 oz, Spicy 100 gal in 12 oz), a Fill button per
allocation that creates a filled lot carrying the bulk lot, the yield and loss record, and the cost per jar and case.
Volumes are whole gallons; jar counts are whole jars filled from each allocation (128 fl oz per gal)."""
from frame_auto import header

SUMMARY = 'Bulk Sauce to Filled Units (open bulk lot BL-7710 in Tank T-3, split 400 gal across Original and Spicy, fill each allocation, record 95% yield, read cost per jar and case)'
ARIA = 'Interactive product screen: open a 400 gallon bulk lot in a holding tank, split it across two flavors and jar sizes, fill each allocation and watch the remaining volume fall, record yield and loss, and read the cost per jar and per case'
STEPS = 5
STUDIO = dict(lede='A typical bulk to fill screen on your Sutton data. Want it different? Describe the change.',
              examples=['Splits by customer order', 'Fill weight checks per jar', 'Loss by reason code', 'Cost with overhead per hour'],
              built_on='Lots, BOMs, jobs and costs', change='Allocations, cost lines and views')

ICON = '<path d="M4 2.5h8v3l-1.5 1.5v6.5h-5V7L4 5.5z"/><path d="M5.5 9.5h5"/>'

CSS = (
 '.g3{display:grid;grid-template-columns:206px 440px;gap:10px;padding:10px 44px 0 16px;height:550px}'
 '.lc{display:flex;flex-direction:column;gap:10px;min-width:0}.tk{flex:none}.tk .row{grid-template-columns:1fr auto;min-height:42px;font-size:9.6px}.tk .t2{display:flex;flex-direction:column;gap:2px}.tk .t2 small{font-size:8.4px;color:#71717A}'
 '.rm{flex:1;display:flex;flex-direction:column}.rm>.empt{margin:10px;flex:1}.rm .bx{padding:9px 11px 0}.rm .big{font-size:22px}'
 '.gauge{margin:8px 11px 0;height:10px;border-radius:5px;background:#F4F4F5;overflow:hidden}.gauge i{display:block;height:100%;background:#52525B;transition:width .5s ease}'
 '.hist .row{grid-template-columns:1fr 54px;font-size:9.1px;min-height:23px}.hist .row span:last-child{text-align:right;font-family:"JetBrains Mono",ui-monospace,monospace}'
 '.tot{margin-top:auto;padding:9px 11px;border-top:1px solid #E4E4E7;font-size:9px;color:#52525B;line-height:1.4;background:#FAFAFA}'
 '.dt{display:flex;flex-direction:column}.dt>.empt{margin:10px;flex:1}'
 '.facts{display:grid;grid-template-columns:repeat(4,1fr);gap:8px;padding:8px 11px;border-bottom:1px solid #E4E4E7;background:#FCFCFC}.facts .kv b{font-size:10px}'
 '.sec{margin:10px 10px 0;border:1px solid #E4E4E7;border-radius:8px;overflow:hidden;background:#fff}.sec .ct{height:28px;font-size:10px}.sec .ct .bt{font-size:9.2px;padding:3px 8px}'
 '.al .row{grid-template-columns:1fr 50px 50px 62px 66px;font-size:9.3px;min-height:30px;padding:0 9px}.al .row>span:nth-child(2),.al .row>span:nth-child(3),.al .row>span:nth-child(4){text-align:right;font-family:"JetBrains Mono",ui-monospace,monospace}.al .row.h>span{font-family:inherit!important}.al .row>span:last-child{text-align:right}'
 '.al .nm small{display:block;font-size:8.2px;color:#71717A}.al .bt{font-size:9px;padding:3px 9px}.al .row.t{min-height:26px;font-weight:600;background:#FAFAFA}'
 '.wait{padding:9px;font-size:9px;color:#A1A1AA;line-height:1.4}'
 '.two{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin:10px 10px 0}.two .sec{margin:0}'
 '.yl,.cs{display:flex;flex-direction:column}.kg{display:grid;grid-template-columns:1fr 1fr;gap:6px 8px;padding:8px 9px}.kg .kv b{font-size:12px;font-family:"JetBrains Mono",ui-monospace,monospace}'
 '.fls{flex:1;display:flex;flex-direction:column;margin-bottom:10px}.fls .row{grid-template-columns:64px 1fr 62px 52px;font-size:9.2px;min-height:24px;padding:0 9px}.fls .row>span:nth-child(n+3){text-align:right;font-family:"JetBrains Mono",ui-monospace,monospace}.fls .row.h>span{font-family:inherit!important}'
 '.cs .row{grid-template-columns:1fr 54px;font-size:9.2px;min-height:23px;padding:0 9px}.cs .row span:last-child{text-align:right;font-family:"JetBrains Mono",ui-monospace,monospace}.cs .row.t{font-weight:600;background:#FAFAFA}.cs .row.c{font-weight:600;background:#F0FDF4;color:#166534}'
)

WIN = (
 header(ICON, 'Bulk to filled units', 'Holding tanks split into flavors and jar sizes')
 + '<div class="g3"><div class="lc"><div class="cd tk" id="tk"></div><div class="cd rm" id="rm"></div></div><div class="cd dt" id="dt"></div></div>'
)

JS = r'''
var FOC='.hd>*,.tk .ct,.tk .row,.rm>*,.dt>.ct,.facts,.sec';
var TK=[['T-1','BL-7708','Smoky barbecue',300,'Filling','c-info'],['T-2','BL-7706','Garlic stir fry',250,'Holding','c-idle'],['T-3','BL-7710','Teriyaki base',400,'Holding','c-idle']];
var BULK=400,LOT='BL-7710';
var AL=[{fl:'Original',oz:12,g:200,id:'FL-9101'},{fl:'Original',oz:32,g:80,id:'FL-9102'},{fl:'Spicy',oz:12,g:100,id:'FL-9103'}];
var COST=[['Ingredients',0.62],['Labor',0.18],['Packaging, jar, cap and label',0.35]],CASE=12;
var S;
function jars(a){return Math.floor(a.g*128/a.oz);}
function filled(){return AL.reduce(function(a,x,i){return a+(S.f[i]?x.g:0);},0);}
function loss(){return S.y?BULK-AL.reduce(function(a,x){return a+x.g;},0):0;}
function rem(){return BULK-filled()-loss();}
function jc(){return COST.reduce(function(a,c){return a+Math.round(c[1]*100);},0)/100;}
function hist(){var h=[['Bulk lot cooked',BULK]],r=BULK;AL.forEach(function(x,i){if(S.f[i]){r-=x.g;h.push(['Filled '+x.id,r]);}});if(S.y){r-=loss();h.push(['Loss recorded',r]);}return h;}
function render(){
$('tk').innerHTML='<div class="ct"><span>Holding tanks</span></div>'+TK.map(function(t,i){var me=i===2&&S.op;return '<button type="button" class="row'+(me?' sel':'')+'" id="t-'+t[0]+'"><span class="t2"><b><span class="mono">'+t[0]+'</span> '+t[2]+'</b><small>Lot '+t[1]+', '+n0(t[3])+' gal</small></span><span class="ch '+(me?(S.y?'c-ok':S.f.some(Boolean)?'c-info':'c-idle'):t[5])+'">'+(me?(S.y?'Empty':S.f.some(Boolean)?'Filling':'Holding'):t[4])+'</span></button>';}).join('');
var m='<div class="ct"><span>Remaining in T-3</span></div>';
if(!S.op)m+='<div class="empt"><b>No tank open</b><span>Open a tank to follow its bulk volume down to zero.</span></div>';
else{m+='<div class="bx in"><div class="kv"><small>Bulk lot '+LOT+'</small><b class="big mono" id="rmg">'+n0(rem())+' gal</b></div></div><div class="gauge"><i style="width:'+(rem()/BULK*100).toFixed(1)+'%"></i></div>'+
'<div class="hist" style="margin-top:8px"><div class="row h"><span>Step</span><span>Left</span></div>'+hist().map(function(h,i){return '<div class="row in"><span>'+h[0]+'</span><span id="h-'+i+'">'+n0(h[1])+'</span></div>';}).join('')+'</div>';}
m+='<div class="tot">Bulk volume drops with every fill.</div>';
$('rm').innerHTML=m;
var d='<div class="ct"><span>'+(S.op?'Bulk lot <span class="mono">'+LOT+'</span>':'Bulk lot')+'</span>'+(S.op?'<span class="ch c-idle">Tank T-3</span>':'')+'</div>';
if(!S.op)d+='<div class="empt"><b>No bulk lot open</b><span>Open a holding tank to split its bulk sauce into filled units.</span></div>';
else{d+='<div class="facts in"><div class="kv"><small>Sauce</small><b>Teriyaki base</b></div><div class="kv"><small>Cooked</small><b>Nov 18, 2026</b></div><div class="kv"><small>Batch</small><b class="mono">SP-2291</b></div><div class="kv"><small>Volume</small><b class="mono">'+n0(BULK)+' gal</b></div></div>';
d+='<div class="sec al"><div class="ct"><span>Split</span>'+(S.sp?'<span class="ch c-info">'+AL.length+' allocations</span>':'<button type="button" class="bt pri" id="spb">Split</button>')+'</div>';
if(!S.sp)d+='<div class="wait">Split the bulk lot across flavors and jar sizes. Each fill becomes a lot that carries '+LOT+'.</div>';
else{d+='<div class="row h"><span>Flavor and jar</span><span>gal</span><span>Jars</span><span>Lot</span><span></span></div>'+AL.map(function(a,i){var last=i===AL.length-1;return '<div class="row in"><span class="nm">'+a.fl+', '+a.oz+' oz<small>From '+LOT+'</small></span><span>'+n0(a.g)+'</span><span id="j-'+i+'">'+n0(jars(a))+'</span><span class="mono">'+(S.f[i]?a.id:'')+'</span><span>'+(S.f[i]?'<span class="ch c-ok">Filled</span>':'<button type="button" class="bt'+(last?' pri':'')+'" id="fb-'+i+'"'+(last?'':' data-pick="1"')+'>Fill</button>')+'</span></div>';}).join('')+
'<div class="row t"><span>Planned</span><span id="alt">'+n0(AL.reduce(function(a,x){return a+x.g;},0))+'</span><span></span><span></span><span></span></div>';}
d+='</div><div class="two"><div class="sec yl"><div class="ct"><span>Yield</span>'+(S.y?'<span class="ch c-ok">Recorded</span>':S.f.every(Boolean)?'<button type="button" class="bt" id="ryb">Record yield</button>':'')+'</div>'+
(S.y?'<div class="kg in"><div class="kv"><small>Filled</small><b id="yf">'+n0(filled())+' gal</b></div><div class="kv"><small>Loss</small><b id="yl">'+n0(loss())+' gal</b></div><div class="kv"><small>Yield</small><b id="yp">'+(filled()/BULK*100).toFixed(1)+'%</b></div><div class="kv"><small>Left in tank</small><b id="yr">'+n0(rem())+' gal</b></div></div>':'<div class="wait">Yield and loss record once every allocation is filled.</div>')+'</div>';
d+='<div class="sec cs"><div class="ct"><span>Cost, 12 oz jar</span>'+(S.cs?'<span class="ch c-ok">Costed</span>':S.y?'<button type="button" class="bt" id="csb">Costing</button>':'')+'</div>'+
(S.cs?COST.map(function(c,i){return '<div class="row in"><span>'+c[0]+'</span><span id="cc-'+i+'">'+m2(c[1])+'</span></div>';}).join('')+'<div class="row t"><span>Per jar</span><span id="cpj">'+m2(jc())+'</span></div><div class="row c"><span>Per case of '+CASE+'</span><span id="cpc">'+m2(Math.round(jc()*100)*CASE/100)+'</span></div>':'<div class="wait">Ingredients, labor and packaging per jar, then per case.</div>')+'</div></div>';
var FL=AL.filter(function(a,i){return S.f[i];});d+='<div class="sec fls"><div class="ct"><span>Filled lots</span><span class="ch c-idle">'+FL.length+' of '+AL.length+'</span></div>'+(FL.length?'<div class="row h"><span>Lot</span><span>Made from</span><span>Jars</span><span>Cases</span></div>'+FL.map(function(a){return '<div class="row in"><span class="mono">'+a.id+'</span><span>'+LOT+', '+a.fl+' '+a.oz+' oz</span><span>'+n0(jars(a))+'</span><span>'+n0(Math.floor(jars(a)/CASE))+'</span></div>';}).join(''):'<div class="wait">Each fill creates a lot that links back to '+LOT+' and batch SP-2291.</div>')+'</div>';}
$('dt').innerHTML=d;
}
function resetState(){S={op:false,sp:false,f:[false,false,false],y:false,cs:false};render();}
winEl.addEventListener('click',function(e){var b=e.target.closest&&e.target.closest('[id^="fb-"]');if(b&&b.hasAttribute('data-pick')){var i=+b.id.slice(3);if(S.sp&&!S.f[i]&&S.f.slice(0,i).every(Boolean)){S.f[i]=true;render();}}});
function capN(){var i=cap.querySelector('.m i');return i?+i.textContent:1;}
var CAPAT=function(hh){var w=cap.offsetWidth;return capN()>=4?{l:14,t:visH()-hh-14}:{l:visW()-w-14,t:visH()-hh-14};};
function nextFill(){for(var i=0;i<AL.length-1;i++)if(!S.f[i])return i;return -1;}
var ST=[
{id:'op',target:function(){return $('t-T-3');},prompt:'Open Tank T-3',where:'right',run:function(){S.op=true;render();},
 after:function(){return['A cooked bulk lot in a holding tank',LOT+', '+n0(BULK)+' gal of teriyaki base from batch SP-2291.'];}},
{id:'sp',target:function(){return $('spb');},prompt:'Split the bulk lot',where:'below',run:function(){S.sp=true;render();},
 after:function(){return['Two flavors, two jar sizes, three fills',AL.map(function(a){return a.fl+' '+a.g+' gal in '+a.oz+' oz';}).join(', ')+'.'];}},
{id:'fill',target:function(){return $('fb-2');},back:function(){var i=nextFill();return i<0?null:[$('fb-'+i),'Fill '+AL[i].fl+', '+AL[i].oz+' oz','below'];},prompt:'Fill Spicy, 12 oz',where:'below',
 run:function(){S.f=[true,true,true];render();},
 after:function(){var r=BULK,o=[];AL.forEach(function(a){r-=a.g;o.push(n0(r));});return['Remaining bulk drops with each fill',n0(BULK)+' gal to '+o.join(', then ')+' gal. Each filled lot carries '+LOT+'.'];}},
{id:'y',target:function(){return $('ryb');},prompt:'Record yield',where:'below',run:function(){S.y=true;render();},
 after:function(){return['Yield and loss on the batch',n0(filled())+' of '+n0(BULK)+' gal filled, '+n0(loss())+' gal loss. Yield '+(filled()/BULK*100).toFixed(1)+'%, tank at 0.'];}},
{id:'cs',target:function(){return $('csb');},prompt:'Open costing',where:'above',run:function(){S.cs=true;render();},
 after:function(){return['Cost per jar and per case',COST.map(function(c){return m2(c[1]);}).join(' + ')+' = '+m2(jc())+' a jar. A case of '+CASE+' is '+m2(Math.round(jc()*100)*CASE/100)+'.'];}}];
'''
