"""Automotive card 3: Release Driven Scheduling (working title). Layout: week board with a capacity line.
Customer release REL-4410 for BA-5520 lands on Line 2's week of Dec 7. Planning levels it to the 700 a day capacity by
building ahead (a backward pass), then the material check finds the FST-121 shortage and drafts a purchase order."""
from frame_auto import header

SUMMARY = 'Release Driven Scheduling (import release REL-4410, place its daily demand on the Line 2 week board, level it to the 700 a day capacity line, check material and draft a purchase order for the shortage)'
ARIA = 'Interactive product screen: import customer release REL-4410 for BA-5520, place 3,400 pieces of daily demand on the week of December 7, level the plan to 700 a day by building 100 ahead on Monday and Tuesday, find a 1,600 piece FST-121 shortage and draft a purchase order'
STEPS = 5
STUDIO = dict(lede='A typical release planning screen, built on your Sutton data with Studio. Want it different? Describe the change.',
              examples=['An 830 and 862 release import', 'A second shift as extra capacity', 'A cumulative shipped check per customer', 'A supplier schedule sent from the PO'],
              built_on='Releases, routings, capacity and stock', change='Lines, rules and views')

ICON = '<rect x="2" y="3" width="12" height="11" rx="1.2"/><path d="M2 6.5h12M5.5 1.8v2.4M10.5 1.8v2.4M4.5 9h2M4.5 11.5h2M9.5 9h2"/>'

CSS = (
 '.g3{display:grid;grid-template-columns:1fr 216px;gap:10px;padding:10px 40px 0 16px}'
 '.col{display:flex;flex-direction:column;gap:10px;min-width:0}'
 '.brd{height:520px;flex:none;display:flex;flex-direction:column}.brd .ct .bt{font-size:9.6px;padding:4px 9px}'
 '.lg{display:flex;align-items:center;gap:12px;padding:7px 11px 0;font-size:8.8px;color:#52525B;white-space:nowrap}.lg span{display:inline-flex;align-items:center;gap:5px}.lg .k{width:12px;height:8px;border-radius:2px;flex:none}'
 '.k.dm{background:repeating-linear-gradient(135deg,#E0E7FF 0 2px,#fff 2px 4px);border:1px solid #A5B4FC}.k.pl{background:#18181B}.k.cp{height:0;border-top:1.5px dashed #F59E0B;border-radius:0}.lg .ch{margin-left:auto}'
 '.cht{position:relative;height:236px;margin:6px 11px 0 11px}.yg{position:absolute;left:30px;right:0;height:0;border-top:1px solid #F0F0F1}.yl{position:absolute;left:0;width:26px;text-align:right;font-size:8.4px;color:#A1A1AA;transform:translateY(-50%)}'
 '.cap7{position:absolute;left:30px;right:0;height:0;border-top:1.5px dashed #F59E0B;z-index:2}.cap7 span{position:absolute;right:0;top:-14px;font-size:8.4px;font-weight:600;color:#B45309;background:#fff;padding:0 3px}'
 '.dc{position:absolute;bottom:20px;display:flex;align-items:flex-end;justify-content:center;gap:4px}.br{width:24px;border-radius:3px 3px 0 0;position:relative;transition:height .55s cubic-bezier(.22,.9,.28,1)}'
 '.br.dm{background:repeating-linear-gradient(135deg,#E0E7FF 0 3px,#fff 3px 6px);border:1px solid #A5B4FC;border-bottom:0}.br.dm.ov{border-color:#F87171;background:repeating-linear-gradient(135deg,#FEE2E2 0 3px,#fff 3px 6px)}.br.pl{background:#18181B}'
 '.br b{position:absolute;left:50%;transform:translateX(-50%);top:-13px;font-size:8.2px;font-weight:600;font-family:"JetBrains Mono",ui-monospace,monospace;color:#3F3F46;white-space:nowrap}.br.pl b{color:#18181B}'
 '.dx{position:absolute;bottom:0;height:16px;font-size:8.8px;color:#52525B;text-align:center;white-space:nowrap}.dx b{font-weight:600;color:#18181B}'
 '.gt{margin:8px 11px 0}.gt .row{grid-template-columns:86px repeat(5,1fr) 52px;min-height:24px;padding:0 4px;font-size:9.2px;white-space:nowrap;gap:4px}.gt .row span:nth-child(n+2){text-align:right;font-family:"JetBrains Mono",ui-monospace,monospace}.gt .row.h span{font-family:inherit}'
 '.gt .row.k2{background:#FAFAFA;font-weight:600}.gt .pos{color:#166534}.gt .up{color:#1E3A8A;font-weight:600}'
 '.rel{height:196px;flex:none;display:flex;flex-direction:column}.rel .pd{padding:9px 10px;display:flex;flex-direction:column;gap:7px;font-size:9.2px;color:#52525B}'
 '.rr{display:flex;flex-direction:column;gap:3px;text-align:left;border:1px solid #E4E4E7;border-radius:7px;background:#fff;padding:7px 9px;cursor:pointer;font-size:9.2px;line-height:1.3;transition:background-color .2s}.rr:hover,.rr.fakehover{background:#FAFAFA}.rr.sel{border-color:#18181B;box-shadow:inset 3px 0 0 #18181B;cursor:default}.rr .tp{display:flex;justify-content:space-between;align-items:center}'
 '.dd{display:grid;grid-template-columns:repeat(5,1fr);gap:3px;text-align:center}.dd span{display:flex;flex-direction:column;border:1px solid #F0F0F1;border-radius:5px;padding:3px 0;font-size:8.4px;color:#71717A}.dd b{font-family:"JetBrains Mono",ui-monospace,monospace;font-size:9.2px;color:#18181B}'
 '.mat{height:288px;flex:none;display:flex;flex-direction:column}.mat .row{grid-template-columns:minmax(0,1fr) 34px 34px 32px;min-height:23px;font-size:9px;padding:0 10px;gap:5px;white-space:nowrap}.mat .row span:nth-child(n+2){text-align:right;font-family:"JetBrains Mono",ui-monospace,monospace}.mat .row.h span{font-family:inherit}'
 '.mat .row.sh{background:#FEF2F2}.mat .row.sh span:last-child{color:#B91C1C;font-weight:600}.mat .ac{padding:9px 10px;display:flex;flex-direction:column;gap:6px;font-size:9.2px;color:#52525B}'
 '.bn2{margin-top:auto;padding:0 11px 10px;font-size:9px;color:#71717A}'
 '.po{border:1px solid #BBF7D0;background:#F0FDF4;border-radius:7px;padding:7px 9px;display:flex;flex-direction:column;gap:2px;font-size:9.2px;line-height:1.3;color:#14532D}'
 '.rel .empt,.mat .empt{margin:10px;flex:1}'
)

WIN = (
 header(ICON, 'Production planning', 'Customer releases, Line 2')
 + '<div class="g3"><div class="cd brd" id="brd"></div><div class="col"><div class="cd rel" id="rel"></div><div class="cd mat" id="mat"></div></div></div>'
)

JS = r'''
var FOC='.hd>*,.brd .ct>*,.lg,.cht,.gt,.rel .ct,.rel .pd>*,.mat .ct,.mat .row,.mat .ac>*';
var DAYS=[['Mon','Dec 7'],['Tue','Dec 8'],['Wed','Dec 9'],['Thu','Dec 10'],['Fri','Dec 11']];
var DEM=[600,600,800,800,600],CAP=700,PER=2;
var MATS=[['FST-121',PER,5200],['STP-300',1,4000],['WSH-044',2,7500],['BSH-07',1,3600],['LBL-12',1,5000]];
var H=236,TOP=900,BASE=20,PX=(H-BASE-14)/TOP;
var S;
function sum(a){return a.reduce(function(x,y){return x+y;},0);}
function cum(a){var t=0;return a.map(function(x){t+=x;return t;});}
function level(d,cap){var p=d.slice(),carry=0;for(var i=d.length-1;i>=0;i--){var want=d[i]+carry;p[i]=Math.min(cap,want);carry=want-p[i];}return p;}
function plan(){return level(DEM,CAP);}
function need(m){return sum(plan())*m[1];}
function short(m){return Math.max(0,need(m)-m[2]);}
function y(v){return BASE+v*PX;}
function render(){
var P=plan(),CR=cum(DEM),CB=cum(P),over=DEM.map(function(d){return d>CAP;});
var b='<div class="ct"><span>Line 2, week of Dec 7</span><span class="mut" style="font-weight:500;margin-right:auto;margin-left:8px">BA-5520, '+n0(CAP)+' a day</span>'+
(!S.imp?'<button type="button" class="bt pri" id="imp">Import release</button>':S.lev?'<span class="ch c-ok" id="pst">Plan '+n0(sum(P))+' of '+n0(sum(DEM))+'</span>':'<button type="button" class="bt'+(S.dem?' pri':'')+'" id="lvl"'+(S.dem?'':' disabled')+'>Level to capacity</button>')+'</div>';
b+='<div class="lg"><span><i class="k dm"></i>Release demand</span><span><i class="k pl"></i>Build plan</span><span><i class="k cp"></i>Capacity</span>'+
(S.lev?'<span class="ch c-info" id="flg">100 built ahead Mon and Tue</span>':S.dem?'<span class="ch c-bad" id="flg">Wed and Thu over by '+n0(DEM[2]-CAP)+'</span>':'')+'</div>';
var c='<div class="cht">';[0,300,600,900].forEach(function(v){c+='<span class="yg" style="bottom:'+y(v)+'px"></span><span class="yl" style="bottom:'+y(v)+'px;transform:translateY(50%)">'+n0(v)+'</span>';});
c+='<span class="cap7" style="bottom:'+y(CAP)+'px"><span>Capacity '+n0(CAP)+'</span></span>';
var cw=(414-30)/5;DAYS.forEach(function(d,i){var l=30+i*cw;c+='<div class="dc" style="left:'+l+'px;width:'+cw+'px">'+
'<span class="br dm'+(S.dem&&over[i]&&!S.lev?' ov':'')+'" style="height:'+(S.dem?DEM[i]*PX:0)+'px;'+(S.dem?'':'border:0')+'">'+(S.dem?'<b id="dm'+i+'">'+n0(DEM[i])+'</b>':'')+'</span>'+
'<span class="br pl" style="height:'+(S.lev?P[i]*PX:0)+'px">'+(S.lev?'<b id="pl'+i+'">'+n0(P[i])+'</b>':'')+'</span></div>'+
'<span class="dx" style="left:'+l+'px;width:'+cw+'px"><b>'+d[0]+'</b> '+d[1]+'</span>';});
c+='</div>';
var row=function(lb,arr,tot,cls,fmt){return '<div class="row'+(cls?' '+cls:'')+'"><span>'+lb+'</span>'+arr.map(function(v,i){return '<span'+(fmt?fmt(v,i):'')+'>'+(v===''?'':n0(v))+'</span>';}).join('')+'<span>'+(tot===''?'':n0(tot))+'</span></div>';};
var E=['','','','',''];
var g='<div class="gt"><div class="row h"><span></span>'+DAYS.map(function(d){return '<span>'+d[0]+'</span>';}).join('')+'<span>Total</span></div>'+
row('Capacity',[CAP,CAP,CAP,CAP,CAP],CAP*5)+row('Release demand',S.dem?DEM:E,S.dem?sum(DEM):'')+
row('Build plan',S.lev?P:E,S.lev?sum(P):'','',function(v,i){return S.lev&&P[i]>DEM[i]?' class="up"':'';})+
row('Cum. required',S.dem?CR:E,'')+row('Cum. built',S.lev?CB:E,'')+
row('Ahead of release',S.lev?CB.map(function(v,i){return v-CR[i];}):E,'','k2',function(v){return v!==''&&v>0?' class="pos"':'';})+'</div>';
$('brd').innerHTML=b+c+g+'<div class="bn2">Line 2 runs one shift, Monday to Friday. Every change to the plan is logged against the release.</div>';
var r='<div class="ct">Customer releases'+(S.imp?'<span class="ch '+(S.dem?'c-ok':'c-warn')+'">'+(S.dem?'On the board':'1 new')+'</span>':'')+'</div>';
if(!S.imp)r+='<div class="empt"><b>No release imported</b><span>Import a customer release to plan it against Line 2.</span></div>';
else{r+='<div class="pd'+(S.an1?' in':'')+'"><button type="button" class="rr'+(S.dem?' sel':'')+'" id="r4410"><span class="tp"><b class="mono">REL-4410</b><span class="ch c-info">Firm</span></span><span>Plant North, BA-5520</span><span class="mut">'+n0(sum(DEM))+' pcs, Dec 7 to Dec 11</span></button>';
r+=S.dem?'<div class="dd">'+DAYS.map(function(d,i){return '<span>'+d[0]+'<b>'+n0(DEM[i])+'</b></span>';}).join('')+'</div>':'<span>Received today, 06:12. Open it to place the daily quantities on the board.</span>';
r+='</div>';}
$('rel').innerHTML=r;
var m='<div class="ct">Material check'+(S.mat?'<span class="ch c-bad" id="msh">1 short</span>':'')+'</div>';
if(!S.lev)m+='<div class="empt"><b>Nothing planned yet</b><span>Once the week is planned, every BOM line is checked against stock.</span></div>';
else{m+='<div class="row h"><span>Part, per unit</span><span>Need</span><span>Stock</span><span>Short</span></div>';
m+=MATS.map(function(x){var sh=S.mat&&short(x)>0;return '<div class="row'+(sh?' sh':'')+(S.an2?' flash':'')+'"><span><span class="mono">'+x[0]+'</span> <span class="mut">x '+x[1]+'</span></span><span id="nd-'+x[0]+'">'+(S.mat?n0(need(x)):'')+'</span><span>'+n0(x[2])+'</span><span id="sh-'+x[0]+'">'+(S.mat?(short(x)?n0(short(x)):'0'):'')+'</span></div>';}).join('');
m+='<div class="ac">';var f=MATS[0];
if(!S.mat)m+='<button type="button" class="bt" id="chk" style="align-self:flex-start">Check material</button><span>Needs come from the plan and the Rev D BOM.</span>';
else if(!S.po)m+='<span>'+f[0]+' is short '+n0(short(f))+' for the week.</span><button type="button" class="bt pri" id="cpo" style="align-self:flex-start">Create purchase order</button>';
else m+='<div class="po in"><b>PO draft, '+f[0]+'</b><span id="poq">'+n0(short(f))+' pcs from Ridgefield Fasteners</span><span>Due Mon Dec 7, before the first build</span></div>';
m+='</div>';}
$('mat').innerHTML=m;
S.an1=S.an2=false;}
function resetState(){S={imp:false,dem:false,lev:false,mat:false,po:false};render();}
var CAPAT=function(hh){return cur===2||cur===1?{l:visW()-cap.offsetWidth-14,t:visH()-hh-14}:{l:14,t:visH()-hh-14};};
var ST=[
{id:'imp',target:function(){return $('imp');},prompt:'Import the customer release',where:'below',run:function(){S.imp=true;S.an1=true;render();},
 after:function(){return['A customer release arrives with its daily quantities','REL-4410 from Plant North: '+n0(sum(DEM))+' BA-5520 for Dec 7 to Dec 11.'];}},
{id:'dem',target:function(){return $('r4410');},prompt:'Open REL-4410',where:'below',run:function(){S.dem=true;render();},
 after:function(){return['Demand lands on the week board against the capacity line',DEM.map(function(d,i){return DAYS[i][0]+' '+n0(d);}).join(', ')+'. Wed and Thu are over '+n0(CAP)+'.'];}},
{id:'lvl',target:function(){return $('lvl');},prompt:'Level the plan to capacity',where:'below',run:function(){S.lev=true;render();},
 after:function(){var P=plan();return['The plan builds ahead so no day goes over capacity',P.map(function(p,i){return DAYS[i][0]+' '+n0(p);}).join(', ')+'. Built stays ahead of required every day.'];}},
{id:'chk',target:function(){return $('chk');},prompt:'Check material',where:'above',run:function(){S.mat=true;S.an2=true;render();},
 after:function(){var f=MATS[0];return['Every BOM line is checked against stock for the week',f[0]+': '+n0(sum(plan()))+' x '+f[1]+' = '+n0(need(f))+' needed, '+n0(f[2])+' in stock, short '+n0(short(f))+'.'];}},
{id:'cpo',target:function(){return $('cpo');},prompt:'Create the purchase order',where:'above',run:function(){S.po=true;render();},
 after:function(){return['The shortage becomes a purchase order in one click','PO draft for '+n0(short(MATS[0]))+' FST-121 from Ridgefield Fasteners, due Mon Dec 7.'];}}];
'''
