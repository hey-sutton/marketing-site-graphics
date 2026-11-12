"""Frozen food card 4: Production Stages & Output. Layout: a stage board of five columns (prep, cook, assemble, freeze,
pack) with an expected and an actual bar in each, a finished goods panel and a material check for the next run.
The bars share one scale from 370 to 400 lb, marked on the axis, so the loss at each stage is visible."""
from frame_auto import header

SUMMARY = 'Production Stages & Output (run MO-6105 moves through five stages with expected and actual output, posts 63 cases to Holding freezer A and flags the chicken shortage for MO-6106)'
ARIA = 'Interactive product screen: select run MO-6105, show expected output for prep, cook, assemble, freeze and pack, record actual output with the loss at each stage, post 63 cases to Holding freezer A and check material for MO-6106'
STEPS = 5
STUDIO = dict(lede='A typical production run screen, built on your Sutton data with Studio. Want it different? Describe the change.',
              examples=['A tablet screen for each stage', 'A loss reason list at the freezer', 'A shift report of output by line', 'A label print when cases post'],
              built_on='Runs, routings, output and stock', change='Stages, fields and checks')

ICON = '<path d="M2 13.5h12"/><rect x="2.5" y="7" width="2" height="6.5"/><rect x="5.5" y="5" width="2" height="8.5"/><rect x="8.5" y="6" width="2" height="7.5"/><rect x="11.5" y="8" width="2" height="5.5"/>'

CSS = (
 '.g4{display:grid;grid-template-columns:1fr 206px;gap:10px;padding:10px 40px 0 16px}'
 '.col{display:flex;flex-direction:column;gap:10px;min-width:0}'
 '.rl{flex:none;display:flex;gap:8px;padding:8px 10px;align-items:stretch}.rl .lb{display:flex;flex-direction:column;justify-content:center;font-size:9.6px;font-weight:600;padding-right:4px}.rl .lb span{font-weight:400;color:#71717A;font-size:8.8px}'
 '.rn{flex:1;text-align:left;border:1px solid #E4E4E7;border-radius:7px;background:#fff;padding:6px 8px;display:flex;flex-direction:column;gap:2px;font-size:9.2px;cursor:pointer;line-height:1.3;transition:background-color .2s}.rn:hover,.rn.fakehover{background:#FAFAFA}.rn.sel{border-color:#18181B;box-shadow:inset 3px 0 0 #18181B;cursor:default}.rn:focus-visible{outline:2px solid #18181B;outline-offset:2px}'
 '.rn .tp{display:flex;justify-content:space-between;align-items:center;gap:4px}.rn .mono{font-weight:600}'
 '.sbd{height:464px;flex:none;display:flex;flex-direction:column}.sbd .ct .bt{font-size:9.4px;padding:4px 9px}.lg4{display:flex;gap:12px;padding:7px 11px 0;font-size:8.8px;color:#52525B;white-space:nowrap}.lg4 span{display:inline-flex;align-items:center;gap:5px}.lg4 i{width:12px;height:8px;border-radius:2px;display:inline-block}'
 '.chs{position:relative;height:250px;margin:6px 11px 0}.gl{position:absolute;left:28px;right:0;height:0;border-top:1px solid #F0F0F1}.gl.in4{border-top:1.5px dashed #A1A1AA}.gy{position:absolute;left:0;width:24px;text-align:right;font-size:8.2px;color:#A1A1AA;transform:translateY(50%)}'
 '.sc{position:absolute;bottom:34px;display:flex;align-items:flex-end;justify-content:center;gap:5px}.bx{width:22px;border-radius:3px 3px 0 0;position:relative;transition:height .45s cubic-bezier(.22,.9,.28,1)}'
 '.bx.e{background:repeating-linear-gradient(135deg,#E0E7FF 0 3px,#fff 3px 6px);border:1px solid #A5B4FC;border-bottom:0}.bx.a{background:#18181B}.bx.a.lo{background:#B45309}.bx b{position:absolute;left:50%;transform:translateX(-50%);top:-13px;font-size:8.2px;font-weight:600;font-family:"JetBrains Mono",ui-monospace,monospace;color:#3F3F46;white-space:nowrap}'
 '.sx{position:absolute;bottom:0;height:30px;display:flex;flex-direction:column;align-items:center;font-size:9px;font-weight:600;line-height:1.3}.sx span{font-weight:400;font-size:8.4px;color:#B91C1C;font-family:"JetBrains Mono",ui-monospace,monospace}'
 '.stb{margin:8px 11px 0}.stb .row{grid-template-columns:80px repeat(5,1fr);min-height:22px;font-size:9px;padding:0 4px;gap:4px;white-space:nowrap}.stb .row span:nth-child(n+2){text-align:right;font-family:"JetBrains Mono",ui-monospace,monospace}.stb .row.h span{font-family:inherit}.stb .neg{color:#B91C1C}'
 '.fg{height:228px;flex:none;display:flex;flex-direction:column}.fg .pd{padding:9px 10px;display:flex;flex-direction:column;gap:8px;font-size:9.2px;color:#52525B}.fg .big{font-size:24px;color:#18181B}'
 '.cs{display:flex;flex-wrap:wrap;gap:2px}.cs i{width:9px;height:9px;border-radius:2px;background:#86EFAC;display:inline-block}.cs i.g{background:#fff;border:1px dashed #F87171}'
 '.mck{height:300px;flex:none;display:flex;flex-direction:column}.mck .row{grid-template-columns:1fr 32px 32px 30px;min-height:24px;font-size:9px;padding:0 10px;gap:4px;white-space:nowrap}.mck .row span:nth-child(n+2){text-align:right;font-family:"JetBrains Mono",ui-monospace,monospace}.mck .row.h span{font-family:inherit}'
 '.mck .row.sh{background:#FEF2F2}.mck .row.sh span:last-child{color:#B91C1C;font-weight:600}.mck .pd{padding:9px 10px;display:flex;flex-direction:column;gap:7px;font-size:9.2px;color:#52525B}'
 '.po{border:1px solid #BBF7D0;background:#F0FDF4;border-radius:7px;padding:7px 9px;display:flex;flex-direction:column;gap:2px;line-height:1.3;color:#14532D}'
 '.fg .empt,.mck .empt{margin:10px;flex:1}'
)

WIN = (
 header(ICON, 'Production runs', 'Line 1, chicken broccoli entree FE-2210')
 + '<div class="g4"><div class="col"><div class="cd rl" id="rl"></div><div class="cd sbd" id="sbd"></div></div>'
 '<div class="col"><div class="cd fg" id="fg"></div><div class="cd mck" id="mck"></div></div></div>'
)

JS = r'''
var FOC='.hd>*,.rl>*,.sbd .ct>*,.lg4,.chs,.stb,.fg .ct,.fg .pd>*,.mck .ct,.mck .row,.mck .pd>*';
var RUNS=[['MO-6105','400 lb in','Running'],['MO-6106','400 lb in','Tomorrow'],['MO-6098','400 lb in','Closed']];
var STG=['Prep','Cook','Assemble','Freeze','Pack'],IN=400,EXP=[392,388,386,385,384],ACT=[392,386,382,380,378],CASE=6;
var NEXT=[['Chicken',160,150],['Broccoli',120,140],['Cream sauce',120,130]];
var LO=370,HI=400,PX=170/(HI-LO),S;
function y(v){return Math.max(0,(v-LO)*PX);}
function lossAt(a,i){return (i?a[i-1]:IN)-a[i];}
function cases(lb){return Math.floor(lb/CASE);}
function short(n){return Math.max(0,n[1]-n[2]);}
function render(){
$('rl').innerHTML='<span class="lb">Runs<span>Line 1</span></span>'+RUNS.map(function(r,i){return '<button type="button" class="rn'+(S.sel&&i===0?' sel':'')+'" id="r-'+r[0]+'"><span class="tp"><span class="mono">'+r[0]+'</span><span class="ch '+(i===0?'c-info':i===1?'c-idle':'c-ok')+'">'+r[2]+'</span></span><span class="mut">FE-2210, '+r[1]+'</span></button>';}).join('');
var b='<div class="ct"><span>'+(S.sel?'Run MO-6105, '+IN+' lb in':'Stage board')+'</span>'+(!S.sel?'<span class="ch c-idle">No run selected</span>':!S.exp?'<button type="button" class="bt" id="lrt">Load routing</button>':S.act<5?'<button type="button" class="bt" id="rac">Record actuals</button>':'<span class="ch c-warn" id="vpk">Pack '+(EXP[4]-ACT[4])+' lb under</span>')+'</div>';
b+='<div class="lg4"><span><i style="background:repeating-linear-gradient(135deg,#E0E7FF 0 2px,#fff 2px 4px);border:1px solid #A5B4FC"></i>Expected out</span><span><i style="background:#18181B"></i>Actual out</span><span><i style="background:#B45309"></i>Below expected</span><span class="mut">Scale '+LO+' to '+HI+' lb</span></div>';
var c='<div class="chs">';[370,380,390,400].forEach(function(v){c+='<span class="gl'+(v===400?' in4':'')+'" style="bottom:'+(34+y(v))+'px"></span><span class="gy" style="bottom:'+(34+y(v))+'px">'+v+'</span>';});
var cw=(410-28)/5;STG.forEach(function(s,i){var l=28+i*cw,ea=S.exp,aa=S.act>i,lo=aa&&ACT[i]<EXP[i];
c+='<div class="sc" style="left:'+l+'px;width:'+cw+'px"><span class="bx e" style="height:'+(ea?y(EXP[i]):0)+'px;'+(ea?'':'border:0')+'">'+(ea?'<b id="e'+i+'">'+EXP[i]+'</b>':'')+'</span><span class="bx a'+(lo?' lo':'')+'" style="height:'+(aa?y(ACT[i]):0)+'px">'+(aa?'<b id="a'+i+'">'+ACT[i]+'</b>':'')+'</span></div>';
c+='<div class="sx" style="left:'+l+'px;width:'+cw+'px">'+s+(aa?'<span id="l'+i+'">'+lossAt(ACT,i)+' lb lost</span>':'')+'</div>';});
c+='</div>';
var E=['','','','',''],row=function(lb,a,cls){return '<div class="row'+(cls?' '+cls:'')+'"><span>'+lb+'</span>'+a.map(function(v){return '<span>'+v+'</span>';}).join('')+'</div>';};
var g='<div class="stb"><div class="row h"><span>Lb out</span>'+STG.map(function(s){return '<span>'+s+'</span>';}).join('')+'</div>'+
row('Expected',S.exp?EXP:E)+row('Actual',ACT.map(function(v,i){return S.act>i?v:'';}))+
row('Expected loss',S.exp?EXP.map(function(v,i){return lossAt(EXP,i);}):E)+row('Actual loss',ACT.map(function(v,i){return S.act>i?lossAt(ACT,i):'';}))+'</div>';
var tl=S.act>=5?'<div class="mut" style="padding:7px 15px 0;font-size:9px" id="tls">Total loss '+(IN-ACT[4])+' lb against '+(IN-EXP[4])+' lb expected.</div>':'';
$('sbd').innerHTML=b+c+g+tl;
var f='<div class="ct">Finished goods'+(S.post?'<span class="ch c-ok">Posted</span>':'')+'</div>';
if(S.act<5)f+='<div class="empt"><b>Nothing to post yet</b><span>Cases post once pack output is recorded.</span></div>';
else if(!S.post)f+='<div class="pd"><span>Pack output '+ACT[4]+' lb in '+CASE+' lb cases.</span><button type="button" class="bt pri" id="pst" style="align-self:flex-start">Post finished goods</button></div>';
else{var ex=cases(EXP[4]),ac=cases(ACT[4]),t='';for(var k=0;k<ex;k++)t+='<i'+(k>=ac?' class="g"':'')+'></i>';
f+='<div class="pd in"><span><b class="big" id="fgc">'+ac+'</b> cases to Holding freezer A</span><span class="cs">'+t+'</span><span id="fgg">Expected '+ex+', '+(ex-ac)+' case short. '+ACT[4]+' lb at '+CASE+' lb a case.</span></div>';}
$('fg').innerHTML=f;
var m='<div class="ct">Next run, MO-6106'+(S.chk?'<span class="ch c-bad" id="msh">1 short</span>':'')+'</div>';
if(!S.post)m+='<div class="empt"><b>No check yet</b><span>Material for the next run is checked after this one posts.</span></div>';
else if(!S.chk)m+='<div class="pd"><span>MO-6106 runs tomorrow on Line 1.</span><button type="button" class="bt" id="chk" style="align-self:flex-start">Check material</button></div>';
else{m+='<div class="row h"><span>Ingredient, lb</span><span>Need</span><span>Have</span><span>Short</span></div>'+NEXT.map(function(n,i){return '<div class="row'+(short(n)?' sh':'')+(S.an?' flash':'')+'"><span>'+n[0]+'</span><span>'+n[1]+'</span><span>'+n[2]+'</span><span id="ms'+i+'">'+short(n)+'</span></div>';}).join('');
m+='<div class="pd">'+(S.po?'<div class="po in" id="pod"><b>PO draft, chicken</b><span>'+short(NEXT[0])+' lb from Harvest Ridge Farms, due before MO-6106</span></div>':'<button type="button" class="bt pri" id="cpo" style="align-self:flex-start">Create purchase order</button>')+'</div>';}
$('mck').innerHTML=m;S.an=false;}
$('mck').addEventListener('click',function(e){if(e.target.closest&&e.target.closest('#cpo')&&S.chk&&!S.po){S.po=true;render();}});
function resetState(){S={sel:false,exp:false,act:0,post:false,chk:false,po:false};render();}
var CAPAT=function(hh){return cur>=3?{l:14,t:96}:{l:visW()-cap.offsetWidth-14,t:visH()-hh-14};};
var ST=[
{id:'sel',target:function(){return $('r-MO-6105');},prompt:'Select run MO-6105',where:'below',run:function(){S.sel=true;render();},
 after:['One run, five stages, 400 lb in','MO-6105 makes FE-2210 on Line 1 through prep, cook, assemble, freeze and pack.']},
{id:'exp',target:function(){return $('lrt');},prompt:'Load the routing',where:'below',run:function(){S.exp=true;render();},
 after:function(){return['The routing sets expected output at every stage',EXP.join(', ')+' lb. '+EXP[4]+' lb out is '+Math.round(EXP[4]/IN*100)+' percent.'];}},
{id:'act',target:function(){return $('rac');},prompt:'Record the actual output',where:'below',run:function(quick){if(quick||mode!=='watch'){S.act=5;render();return;}for(var i=1;i<=5;i++)(function(i){later(function(){S.act=i;render();},(i-1)*120);})(i);},
 after:function(){return['Actual output fills in stage by stage, with the loss at each',ACT.join(', ')+' lb. '+(IN-ACT[4])+' lb lost against '+(IN-EXP[4])+' expected.'];}},
{id:'post',target:function(){return $('pst');},prompt:'Post the finished goods',where:'above',run:function(){S.post=true;render();},
 after:function(){return['Finished cases post straight to a freezer',cases(ACT[4])+' cases of '+CASE+' lb to Holding freezer A, '+(cases(EXP[4])-cases(ACT[4]))+' short of the '+cases(EXP[4])+' expected.'];}},
{id:'chk',target:function(){return $('chk');},prompt:'Check material for MO-6106',where:'above',run:function(){S.chk=true;S.an=true;render();},
 after:function(){return['The next run is checked against stock before it starts','Chicken: '+NEXT[0][1]+' lb needed, '+NEXT[0][2]+' on hand, '+short(NEXT[0])+' lb short.'];}}];
'''
