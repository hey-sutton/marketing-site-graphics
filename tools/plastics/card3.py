"""Plastics card 3: Production Runs & Output. Layout: the run form and a work order routing strip across the top, press cards under it,
then the output log and an expected vs actual materials panel that stays empty until step 4. Operator logging only, no machine monitoring.
Rounding: caps whole, compound to 0.1 lb, regrind to 0.01 lb."""
SUMMARY = 'Production Runs & Output (a run released to a press with its mold and compound, output logged by shift at the press, expected against actual, the run completed into a finished lot and a regrind credit)'
ARIA = 'Interactive product screen: release RUN-7720 for 40,000 caps to Press 4 with mold M-0412, log shift 1 and shift 2 output, compare expected and actual output and compound, and complete the run into finished lot FL-7720'
STEPS = 5
STUDIO = dict(lede='A typical production run screen, built on your Sutton data with Studio. Want it different? Describe the change.',
              examples=['A mold and press assignment board', 'A scrap reason list', 'A shift output summary', 'A changeover log'],
              built_on='Runs, routings, BOMs and output logs', change='Steps, fields and views')

CSS = (
 '.b3{display:flex;flex-direction:column;gap:10px;padding:12px 40px 0 16px;height:596px}'
 '.top{display:grid;grid-template-columns:236px 1fr;gap:12px;flex:none}.bot{display:grid;grid-template-columns:1fr 236px;gap:12px;flex:1 1 0;min-height:0}'
 '.rf .g{display:grid;grid-template-columns:1fr 1fr;gap:6px 7px;padding:8px 10px}.rf .ft{padding:0 10px 9px}.rf .ft .bt{width:100%}'
 '.rtg{display:flex;flex-direction:column}.rs{display:flex;align-items:stretch;gap:5px;padding:9px 10px 6px}.st{flex:1;border:1px solid #E4E4E7;border-radius:7px;padding:5px 7px;display:flex;flex-direction:column;gap:2px;min-width:0;background:#FAFAFA;transition:border-color .35s,background-color .35s,opacity .35s}'
 '.st small{font-size:7.8px;color:#A1A1AA;font-family:"JetBrains Mono",ui-monospace,monospace}.st b{font-size:9.6px;white-space:nowrap}.st span{font-size:8.6px;color:#71717A;white-space:nowrap}.st .ch{align-self:flex-start;margin-top:2px}.st.on{background:#fff;border-color:#18181B}.rs .ar{align-self:center;color:#A1A1AA;font-size:10px}'
 '.pg{display:flex;align-items:center;gap:8px;padding:2px 10px 9px;font-size:9.4px}.pg .bar{flex:1;height:6px;border-radius:3px;background:#F4F4F5;overflow:hidden}.pg .bar i{display:block;height:100%;background:#18181B;border-radius:3px;transition:width .6s ease}'
 '.prs{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;flex:none}.pc{padding:7px 10px;display:flex;flex-direction:column;gap:3px}.pc .l1{display:flex;align-items:center;gap:6px;font-size:10px;font-weight:600}.pc .l1 .ch{margin-left:auto}.pc .l2{font-size:9.2px;color:#52525B;white-space:nowrap}.pc.cur{border-color:#18181B}'
 '.out{display:flex;flex-direction:column;min-height:0}.out .g{display:grid;grid-template-columns:46px 70px 56px 1fr auto;gap:6px;align-items:end;padding:8px 10px;border-bottom:1px solid #F0F0F1}.out .g .sh{font-size:9.6px;font-weight:600;padding-bottom:6px}'
 '.out .row{grid-template-columns:44px 64px 1fr 56px 46px 58px;min-height:24px;font-size:9.6px;white-space:nowrap}.out .row span:nth-child(4),.out .row span:nth-child(5){text-align:right}.out .pd{padding:9px 10px;border-bottom:1px solid #F0F0F1}'
 '.mat{display:flex;flex-direction:column}.mat .pd{padding:9px 10px}.mat .row{grid-template-columns:1fr 60px 52px;min-height:24px;font-size:9.4px;white-space:nowrap}.mat .row span:not(:first-child){text-align:right}.mat .row.t{font-weight:600;background:#FAFAFA}'
 '.mat .ft{padding:8px 10px;display:flex;flex-direction:column;gap:5px}.mat .ft .bt{width:100%}.mat .ft .ch{align-self:flex-start;white-space:normal}'
)

WIN = (
 '<div class="hd"><svg width="16" height="16" viewBox="0 0 16 16" fill="none" aria-hidden="true"><rect x="2" y="3" width="12" height="10" rx="1.5" stroke="#18181B" stroke-width="1.2"/><path d="M5 3v10M2 7h3M2 10h3M8 6.5h4M8 9.5h3" stroke="#18181B" stroke-width="1.2"/></svg>'
 '<span class="tt">Production</span><span class="ch c-idle" id="hst">RUN-7720 planned</span><span class="sb grow">Ridgeway Plastics, molding floor</span></div>'
 '<div class="b3"><div class="top"><div class="cd rf frm" id="rf"></div><div class="cd rtg" id="rtg"></div></div><div class="prs" id="prs"></div>'
 '<div class="bot"><div class="cd out" id="out"></div><div class="cd mat" id="mat"></div></div></div>'
)

JS = r'''
var FOC='.hd>*,.rf .ct,.rf .fld,.rf .ft,.rtg .ct,.rs,.pg,.pc,.out .ct,.out .g>*,.out .row,.out .pd,.mat .ct,.mat .pd,.mat .row,.mat .ft>*';
var PER=0.0275,PURGE=12.5;
var SH=[['1','18,500','700','J. Park'],['2','20,200','600','M. Diaz']];
var STEPS=[['10','Dry and blend','Dryer D-2'],['20','Mold','Press'],['30','Trim and inspect','Bench T-1'],['40','Pack','Pack line 2']];
var S;
function f1(n){return n.toLocaleString('en-US',{minimumFractionDigits:1,maximumFractionDigits:1});}
function f2(n){return n.toLocaleString('en-US',{minimumFractionDigits:2,maximumFractionDigits:2});}
function int(v){v=String(v).trim().replace(/,/g,'');return /^\d{1,6}$/.test(v)?parseInt(v,10):-1;}
function exp(){return Math.round(S.q*PER*10)/10;}
function good(){return S.lg.reduce(function(a,x){return a+x[1];},0);}
function scrap(){return S.lg.reduce(function(a,x){return a+x[2];},0);}
function molded(){return good()+scrap();}
function val(i){return String($(i).value).trim();}
function render(){
var r='<div class="ct"><span>Run <span class="mono">RUN-7720</span></span><span class="ch '+(S.rel?(S.done?'c-ok':'c-info'):'c-idle')+'">'+(S.done?'Complete':S.rel?'Released':'Planned')+'</span></div><div class="g">'+
'<label class="fld" id="fq"><small>Caps, CAP-38</small><input id="iq" value="'+S.v.q+'" inputmode="numeric" autocomplete="off"'+(S.rel?' disabled':'')+'></label>'+
'<label class="fld"><small>Compound</small><input value="BLK-PP-92" disabled></label>'+
'<label class="fld" id="fp"><small>Press</small><input id="ip" value="'+S.v.p+'" autocomplete="off"'+(S.rel?' disabled':'')+'></label>'+
'<label class="fld" id="fm"><small>Mold</small><input id="im" value="'+S.v.m+'" autocomplete="off" spellcheck="false"'+(S.rel?' disabled':'')+'><span class="em">Press 3, 4 or 6 and a mold like M-0412</span></label></div>'+
'<div class="ft">'+(S.rel?'<button type="button" class="bt done" disabled>Released to '+S.p+'</button>':'<button type="button" class="bt pri" id="rel">Release run</button>')+'</div>';
$('rf').innerHTML=r;
var stt=function(i){if(!S.rel)return['c-idle','Not started'];if(S.done)return['c-ok','Done'];var m=molded();
if(i===0)return m>0?['c-ok','Done']:['c-info','Ready'];if(i===1)return m>=S.q?['c-ok','Done']:m>0?['c-warn','In progress']:['c-info','Ready'];if(i===2)return m>=S.q?['c-info','Ready']:['c-idle','Waiting'];return['c-idle','Waiting'];};
var t='<div class="ct">Routing<span class="mut" style="font-weight:500">CAP-38 on BOM v4</span></div><div class="rs">'+STEPS.map(function(x,i){var s=stt(i);return (i?'<span class="ar">&#8594;</span>':'')+'<div class="st'+(S.rel?' on':'')+(S.anim?' in':'')+'" style="animation-delay:'+(i*160)+'ms"><small>'+x[0]+'</small><b>'+x[1]+'</b><span>'+(i===1?(S.rel?S.p+', '+S.m:'Press, mold'):x[2])+'</span><span class="ch '+s[0]+'">'+s[1]+'</span></div>';}).join('')+'</div>';
if(S.rel)t+='<div class="pg"><span class="mut">Molded</span><span class="bar"><i style="width:'+Math.min(100,Math.round(molded()/S.q*100))+'%"></i></span><span class="mono" id="prog">'+n0(molded())+' of '+n0(S.q)+'</span><span class="ch '+(S.done?'c-ok':'c-info')+'" id="res">'+(S.done?f1(Math.round((exp()+PURGE)*10)/10)+' lb of BLK-PP-92 issued':f1(exp())+' lb of BLK-PP-92 reserved')+'</span></div>';
else t+='<div class="pg"><span class="mut">Release the run to reserve its compound and open its steps.</span></div>';
$('rtg').innerHTML=t;
var P=[['Press 3','Running','c-info','RUN-7717, CAP-28 white','Mold M-0388'],['Press 4',S.done?'Open':S.rel?'Running':'Open',S.done?'c-idle':S.rel?'c-info':'c-idle',S.done?'RUN-7720 complete':S.rel?'RUN-7720, CAP-38 black':'Next: RUN-7720',S.rel&&!S.done?'Mold '+S.m:'No mold set'],['Press 6','Planned','c-idle','RUN-7722, CAP-38 black','Mold M-0420 on 11/11']];
$('prs').innerHTML=P.map(function(x){return '<div class="cd pc'+(x[0]===S.p&&S.rel&&!S.done?' cur':'')+'"><div class="l1">'+x[0]+'<span class="ch '+x[2]+'">'+x[1]+'</span></div><div class="l2">'+x[3]+'</div><div class="l2 mut">'+x[4]+'</div></div>';}).join('');
var o='<div class="ct">Output log<span class="mut" style="font-weight:500">Logged at the press</span></div>';
var n=S.lg.length;
if(!S.rel)o+='<div class="pd"><span class="mut" style="font-size:9.4px">Release a run to log its output here, shift by shift.</span></div>';
else if(n<2)o+='<div class="g frm"><span class="sh">Shift '+SH[n][0]+'</span><label class="fld" id="fg"><small>Good caps</small><input id="ig" value="'+S.v.g+'" inputmode="numeric" autocomplete="off"></label><label class="fld" id="fs"><small>Scrap</small><input id="is" value="'+S.v.s+'" inputmode="numeric" autocomplete="off"></label>'+
'<label class="fld" id="fo"><small>Operator</small><input id="io" value="'+S.v.o+'" autocomplete="off" spellcheck="false"><span class="em">Whole caps in both boxes</span></label><button type="button" class="bt pri" id="ls'+(n+1)+'">Log shift '+(n+1)+'</button></div>';
else o+='<div class="pd"><span class="ch '+(S.done?'c-ok':'c-info')+'">'+n0(molded())+' of '+n0(S.q)+' molded, '+n0(good())+' good and '+n0(scrap())+' scrap</span></div>';
o+='<div class="row h"><span>Date</span><span>Run</span><span>Shift and operator</span><span>Good</span><span>Scrap</span><span></span></div>';
S.lg.slice().reverse().forEach(function(x,i){o+='<div class="row in"><span class="mono">Today</span><span class="mono">RUN-7720</span><span>Shift '+x[0]+', '+x[3]+'</span><span class="mono" id="g'+x[0]+'">'+n0(x[1])+'</span><span class="mono">'+n0(x[2])+'</span><span><span class="ch c-ok">Logged</span></span></div>';});
[['11/06','RUN-7717','Shift 2, A. Lin','19,600','450'],['11/06','RUN-7717','Shift 1, J. Park','18,900','520'],['11/05','RUN-7715','Shift 2, M. Diaz','20,400','380'],['11/05','RUN-7715','Shift 1, A. Lin','17,800','610'],['11/04','RUN-7713','Shift 2, J. Park','15,200','300'],['11/04','RUN-7713','Shift 1, M. Diaz','16,100','420'],['11/03','RUN-7711','Shift 2, A. Lin','19,300','510'],['11/03','RUN-7711','Shift 1, J. Park','18,700','560']].forEach(function(x){o+='<div class="row"><span class="mono mut">'+x[0]+'</span><span class="mono mut">'+x[1]+'</span><span class="mut">'+x[2]+'</span><span class="mono mut">'+x[3]+'</span><span class="mono mut">'+x[4]+'</span><span></span></div>';});
$('out').innerHTML=o;
var m='<div class="ct">Expected vs actual<span class="mut" style="font-weight:500">RUN-7720</span></div>';
if(!S.cmp)m+='<div class="pd"><div class="empt" id="me"><b>Nothing to compare yet</b><span>Once the run is molded, compare parts and material with the plan.</span></div></div><div class="ft"><button type="button" class="bt'+(S.lg.length===2?' pri':'')+'" id="cmp">Expected vs actual</button></div>';
else{var a=Math.round((exp()+PURGE)*10)/10;m+='<div class="row h"><span></span><span>Expected</span><span>Actual</span></div><div class="row in"><span>Good caps</span><span class="mono">'+n0(S.q)+'</span><span class="mono" id="ag">'+n0(good())+'</span></div><div class="row in"><span>Scrap caps</span><span class="mono">0</span><span class="mono" id="as">'+n0(scrap())+'</span></div>'+
'<div class="row in"><span>Compound, lb</span><span class="mono" id="ec">'+f1(exp())+'</span><span class="mono" id="ac">'+f1(a)+'</span></div><div class="row t in"><span>Compound over</span><span></span><span class="mono" id="ov">'+f1(Math.round((a-exp())*10)/10)+' lb</span></div>'+
'<div class="ft"><span class="mut" style="font-size:9px;line-height:1.4">The extra '+f1(PURGE)+' lb is purge at start up. Scrap is '+f2(Math.round(scrap()*PER*100)/100)+' lb, ground to regrind.</span>';
m+=S.done?'<span class="ch c-ok" id="fl">FL-7720, '+n0(good())+' caps to stock</span><span class="ch c-info">'+f1(a)+' lb compound deducted</span><span class="ch c-info" id="rg">'+f2(Math.round(scrap()*PER*100)/100)+' lb to regrind REG-PP</span>':'<button type="button" class="bt pri" id="cpl">Complete run</button>';m+='</div>';}
$('mat').innerHTML=m;
$('hst').textContent=S.done?'RUN-7720 complete':S.rel?'RUN-7720 on '+S.p:'RUN-7720 planned';$('hst').className='ch '+(S.done?'c-ok':S.rel?'c-info':'c-idle');
S.anim=false;}
$('rf').addEventListener('input',function(e){var k={iq:'q',ip:'p',im:'m'}[e.target.id];if(k)S.v[k]=e.target.value;});
$('out').addEventListener('input',function(e){var k={ig:'g',is:'s',io:'o'}[e.target.id];if(k)S.v[k]=e.target.value;});
function setShift(n){S.v.g=SH[n][1];S.v.s=SH[n][2];S.v.o=SH[n][3];}
function resetState(){S={rel:false,cmp:false,done:false,anim:false,q:40000,p:'Press 4',m:'M-0412',lg:[],v:{q:'40,000',p:'Press 4',m:'M-0412'}};setShift(0);render();}
function okRel(){var q=int(val('iq')),p=/^press [346]$/i.test(val('ip')),m=/^M-\d{4}$/i.test(val('im')),b=!(q>0&&p&&m);['fq','fp','fm'].forEach(function(i){$(i).classList.toggle('err',b);});return !b;}
function okShift(){var g=int(val('ig')),s=int(val('is')),b=!(g>=0&&s>=0&&g+s>0);['fg','fs','fo'].forEach(function(i){$(i).classList.toggle('err',b);});return !b;}
function logShift(){var n=S.lg.length;S.lg.push([SH[n][0],int(val('ig')),int(val('is')),val('io')||SH[n][3]]);if(S.lg.length<2)setShift(1);render();}
var CAPAT=function(hh){return{l:14,t:visH()-hh-14};};
var ST=[
{id:'rel',target:function(){return $('rel');},prompt:'Click Release run',where:'below',ok:okRel,
 run:function(){S.q=int(val('iq'));S.p='Press '+val('ip').slice(-1);S.m=val('im').toUpperCase();S.rel=true;S.anim=true;render();},
 after:function(){return['Each run carries its steps, its press, its mold and its material',n0(S.q)+' caps on '+S.p+' with mold '+S.m+'. '+f1(exp())+' lb of compound reserved.'];}},
{id:'ls1',target:function(){return $('ls1');},prompt:'Click Log shift 1',where:'below',ok:okShift,run:function(){logShift();},
 after:function(){var x=S.lg[0];return['The operator logs output at the press from a tablet','Shift 1: '+n0(x[1])+' good and '+n0(x[2])+' scrap. '+n0(molded())+' of '+n0(S.q)+' molded.'];}},
{id:'ls2',target:function(){return $('ls2');},prompt:'Click Log shift 2',where:'below',ok:okShift,run:function(){logShift();},
 after:function(){return['A second shift adds to the same run, with a record of who logged what',n0(molded())+' of '+n0(S.q)+' molded, '+n0(good())+' good and '+n0(scrap())+' scrap in all.'];}},
{id:'cmp',target:function(){return $('cmp');},prompt:'Click Expected vs actual',where:'above',run:function(){S.cmp=true;render();},
 after:function(){return['Compare what you expected with what the run really made and used','Good caps '+n0(good())+' against '+n0(S.q)+'. Compound '+f1(exp()+PURGE)+' lb against '+f1(exp())+', over by '+f1(PURGE)+' lb.'];}},
{id:'cpl',target:function(){return $('cpl');},prompt:'Click Complete run',where:'above',run:function(){S.done=true;render();},
 after:function(){return['Completing a run books the finished lot, deducts the material and credits the regrind','FL-7720 adds '+n0(good())+' caps to stock and '+f2(Math.round(scrap()*PER*100)/100)+' lb goes to regrind.'];}}];
'''
