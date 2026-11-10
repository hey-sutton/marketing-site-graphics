"""Furniture and woodworking card 1: Stage Scheduling & Capacity. A swimlane calendar: five jobs with their stage bars across
four weeks and a weekly Finish room capacity row, the over capacity week, one move that fixes it, then the job drawer where
an operator closes Stain and clocks into Finish, and back to the board. Hours to 0.1."""
SUMMARY = 'Stage Scheduling & Capacity (stage bars per job across four weeks, the Finish room booked 92 of 80 hours, one move that fits both weeks, a job drawer with clock in that advances the stage)'
ARIA = 'Interactive product screen: show four weeks of stage bars, open the Finish room week of Nov 23 booked 92 of 80 hours, move J-2421 finish to Nov 30 so both weeks fit, open job J-2417 and clock into Finish'
STEPS = 8
HEADLINE = 'Stage Scheduling & Capacity'
STUDIO = dict(lede='A typical production calendar, built on your Sutton data with Studio. Want it different? Describe the change.',
              examples=['Add a drying buffer between stain and finish', 'Show install crews on the same calendar', 'Alert the shop lead when a stage slips two days', 'Color stages by room'],
              built_on='Work orders, routings and capacity', change='Stages, rooms, colors and alerts')
# storyboard: screen, module, target type, position (the tests read this and check the built card against it)
STORY = [('Schedule board', 'sch', 'segmented control', 'top right'), ('Finish capacity', 'sch', 'capacity cell', 'bottom center'),
         ('Schedule board', 'sch', 'suggestion button', 'right'), ('Schedule board', 'sch', 'capacity cell', 'bottom right'),
         ('Job J-2417', 'sch', 'table row', 'left'), ('Job J-2417', 'sch', 'action button', 'right'),
         ('Job J-2417', 'sch', 'primary button', 'bottom right'), ('Schedule board', 'sch', 'close button', 'top right')]

CSS = (
 # compact icon rail: this card is the dense one, so the calendar gets the width
 '.app{grid-template-columns:46px 1fr}.rail{padding:10px 6px}.rail .ni span,.co span:last-child{display:none}.ni{justify-content:center;padding:0}.co{justify-content:center;padding:2px 0 12px}'
 '.seg{display:inline-flex;height:26px;padding:2px;gap:2px;border:1px solid #E4E4E7;border-radius:7px;background:#FAFAFA}.seg button{border:0;border-radius:5px;background:none;padding:0 9px;font-size:9.8px;color:#52525B;cursor:pointer}.seg button.on{background:#fff;color:#18181B;font-weight:600;box-shadow:0 0 0 1px #E4E4E7}.seg button.fakehover{background:#F0F0F1}'
 '.bd{border:1px solid #E4E4E7;border-radius:8px;overflow:hidden;position:relative;flex:none}'
 '.brow{display:grid;grid-template-columns:142px 1fr;border-top:1px solid #F0F0F1;min-height:40px}.brow.h{border-top:0;min-height:34px;background:#FAFAFA}'
 '.lc{display:flex;flex-direction:column;justify-content:center;gap:2px;padding:0 9px;border-right:1px solid #E4E4E7;min-width:0}.lc small{font-size:8.6px;color:#71717A;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}'
 'button.lc{border:0;border-right:1px solid #E4E4E7;background:#fff;text-align:left;cursor:pointer;transition:background-color .2s}button.lc:hover,button.lc.fakehover{background:#FAFAFA}.lc .t1{display:flex;align-items:center;gap:6px;font-size:10px}'
 '.trk{position:relative;overflow:hidden;background-image:repeating-linear-gradient(90deg,transparent 0,transparent calc(var(--dw) - 1px),#F4F4F5 calc(var(--dw) - 1px),#F4F4F5 var(--dw))}'
 '.trk .wkl{position:absolute;top:0;bottom:0;border-left:1px solid #E4E4E7}.trk .tdy{position:absolute;top:0;bottom:0;width:2px;margin-left:-1px;background:#18181B;opacity:.55;z-index:2}'
 '.bh .trk{background-image:none}.wh{position:absolute;top:4px;font-size:9.4px;font-weight:600;padding-left:5px;white-space:nowrap}.dl{position:absolute;bottom:3px;font-size:8px;color:#A1A1AA;text-align:center}'
 '.bar{position:absolute;top:9px;height:22px;border-radius:5px;font-size:8.8px;font-weight:600;display:flex;align-items:center;padding:0 5px;white-space:nowrap;overflow:hidden;box-shadow:inset 0 0 0 1px rgba(0,0,0,.06)}'
 '.bar.mv{transition:left .9s cubic-bezier(.4,0,.2,1)}.bar.lit{box-shadow:inset 0 0 0 1.5px #18181B}'
 '.ccrow{display:grid;grid-template-columns:142px 1fr;border-top:1px solid #E4E4E7;min-height:42px;background:#FAFAFA}.ccrow .trk{background-image:none}'
 '.cc{position:absolute;top:6px;bottom:6px;margin-left:3px;border-radius:6px;border:1px solid transparent;font-family:"JetBrains Mono",ui-monospace,monospace;font-size:9.6px;font-weight:600;cursor:pointer;display:flex;align-items:center;justify-content:center;gap:5px;transition:background-color .4s,color .4s,border-color .4s}'
 '.cc.ok{background:#DCFCE7;color:#166534;border-color:#BBF7D0}.cc.ov{background:#FEF3C7;color:#92400E;border-color:#FDE68A}.cc.pst{background:#F4F4F5;color:#A1A1AA;cursor:default;font-family:Inter,sans-serif;font-weight:500}.cc.sel{box-shadow:0 0 0 2px #18181B}.cc.fakehover{filter:brightness(.97)}.cc:focus-visible{outline:2px solid #18181B;outline-offset:1px}'
 '.lgd2{display:flex;flex-wrap:wrap;gap:6px 12px;font-size:9px;color:#52525B;flex:none}.lgd2 span{display:inline-flex;align-items:center;gap:5px}.lgd2 i{width:20px;height:10px;border-radius:3px;font-style:normal;font-size:7px;font-weight:700;display:grid;place-items:center}'
 '.cpn{position:absolute;right:0;top:0;bottom:0;width:236px;z-index:6;background:#fff;border-left:1px solid #E4E4E7;box-shadow:-10px 0 24px rgba(0,0,0,.08);display:flex;flex-direction:column;animation:cpin .35s cubic-bezier(.22,.9,.28,1) both}@keyframes cpin{from{transform:translateX(24px);opacity:0}}'
 '.cpn .row{grid-template-columns:52px 1fr 40px;font-size:9.8px}.cpn .tot{font-weight:600;background:#FFFBEB}.sug{margin:10px;border:1px solid #E4E4E7;border-radius:8px;padding:9px 10px;display:flex;flex-direction:column;gap:6px;font-size:9.6px;line-height:1.4}.sug b{font-size:10px}'
 '.pgw{position:relative;flex:none}'
 '.fl .row{grid-template-columns:52px 1fr 70px 96px;font-size:9.8px;white-space:nowrap;min-height:31px}.fl .row>span:last-child{text-align:right}'
 '.sl .row{grid-template-columns:78px 86px 1fr 62px;min-height:31px;font-size:9.8px;white-space:nowrap}.sl .row>span:last-child{text-align:right}.sl .row.cur{background:#FAFAFA}'
 '.pbar{height:6px;border-radius:3px;background:#F0F0F1;overflow:hidden;min-width:24px}.pbar i{display:block;height:100%;background:#18181B;border-radius:3px;transition:width .6s ease}'
 '.op{display:inline-grid;place-items:center;width:18px;height:18px;border-radius:50%;background:#18181B;color:#fff;font-size:7.6px;font-weight:600;margin-right:5px;vertical-align:middle}'
 '.jg{display:grid;grid-template-columns:1fr 196px;gap:10px;flex:none}.jg .side{display:flex;flex-direction:column;gap:10px}'
 '.ck{padding:10px 11px;display:flex;flex-direction:column;gap:7px;font-size:9.8px;line-height:1.4}.ck .bt{align-self:flex-start}.ck .wl{display:flex;justify-content:space-between;font-size:9.8px}.ck .wl b{font-family:"JetBrains Mono",ui-monospace,monospace}'
 # phone
 '.wks{display:grid;gap:6px}.wks .cc{position:relative;inset:auto;margin:0;height:38px;flex-direction:column;gap:1px;font-size:10.4px}.wks .cc small{font-family:Inter,sans-serif;font-size:8.6px;font-weight:500}'
 '.pj .row{grid-template-columns:50px 1fr auto;min-height:28px;font-size:10.2px;white-space:nowrap}.pj .row>span:nth-child(2){overflow:hidden;text-overflow:ellipsis}'
 '.pn{font-size:9.8px;padding:5px 9px;border-radius:7px;background:#F0FDF4;border:1px solid #BBF7D0;color:#166534}'
 '.shot.ph .sl .row{grid-template-columns:78px 1fr 58px;min-height:22px;font-size:9.8px}.shot.ph .ck{padding:7px 9px;gap:5px}.shot.ph .cpn{position:static;width:auto;box-shadow:none;border:1px solid #E4E4E7;border-radius:8px;animation:none}.shot.ph .sug{margin:0;padding:7px 9px}'
)

WIN = ''

JS = r'''
var FOC='.rail .ni,.bc,.phd>*,.bn .bi,.pg .bh,.pg .brow>*,.pg .ccrow>*,.pg .lgd2,.pg .cd>*,.cpn>*,.cpn .row,.wks>*,.pj .row,.pg .pn';
var STG=[['Mill','Mill','#E7E5E4','#44403C'],['Build fronts','Fronts','#DBEAFE','#1E40AF'],['Stain','Stain','#EADBC8','#6B3F18'],['Finish','Fin','#EDE9FE','#5B21B6'],['Assemble','Asm','#CCFBF1','#115E59'],['Install','Inst','#FCE7F3','#9D174D']];
var WK=['Nov 16','Nov 23','Nov 30','Dec 7'],CAP=80,TODAY=5;
var JOBS=[['J-2417','Kitchen cabinets','Dec 8',[[1,0,3],[2,3,3],[3,6,4],[4,10,3],[5,15,2]],32],
['J-2418','Dining table','Dec 4',[[0,0,2],[2,2,3],[3,5,3],[4,10,2],[5,13,1]],20],
['J-2419','Primary closet built-ins','Dec 11',[[0,0,2],[1,2,3],[2,5,1],[3,6,4],[4,11,3],[5,16,2]],24],
['J-2420','Reception desk','Dec 15',[[0,3,2],[1,5,3],[2,8,2],[3,10,3],[4,15,2],[5,18,2]],28],
['J-2421','Bookcase wall','Dec 18',[[0,0,2],[1,2,2],[2,4,2],[3,7,2],[4,9,2],[5,13,1]],16]];
var STAIN0=6.5,STAINE=10;
var S;
function bars(j){return j[3].map(function(b){var sh=(j[0]==='J-2421'&&S.moved&&b[0]>=3)?5:0;return [b[0],b[1]+sh,b[2],b[1]];});}
function finWeek(j){var f=bars(j).filter(function(b){return b[0]===3;})[0];return Math.floor(f[1]/5);}
function load(w){return JOBS.reduce(function(a,j){return a+(finWeek(j)===w?j[4]:0);},0);}
function booked(w){return JOBS.filter(function(j){return finWeek(j)===w;});}
function status(j){if(j[0]==='J-2417')return S.fin?['c-ok','In Finish']:['c-idle','In Stain'];if(j[0]==='J-2421'&&!S.moved)return ['c-warn','At risk'];return ['c-ok','On time'];}
function chip(c){return '<span class="ch '+c[0]+'">'+c[1]+'</span>';}
function ccell(w,P){if(w===0&&!P)return '<span class="cc pst">Past week</span>';var l=load(w),ov=l>CAP;
 return '<button type="button" class="cc '+(ov?'ov':'ok')+(S.cw===w&&S.scr==='cap'||S.wk===w?' sel':'')+'" id="cc-'+w+'"><span id="cl-'+w+'">'+l+' of '+CAP+' h</span>'+(P?'<small>'+WK[w]+'</small>':(ov&&S.v===2?'<span style="font-family:Inter;font-weight:500">over by '+(l-CAP)+'</span>':''))+'</button>';}
function seg(){return '<div class="seg" role="group" aria-label="Weeks shown"><button type="button" id="v2" class="'+(S.v===2?'on':'')+'">2 weeks</button><button type="button" id="v4" class="'+(S.v===4?'on':'')+'">4 weeks</button></div>';}
function board(){var o=S.v===2?5:0,N=S.v*5,dw='calc(100% / '+N+')',pc=function(d){return ((d-o)/N*100).toFixed(3)+'%';};
 var wl='',wh='',dl='';for(var w=0;w<4;w++){var d=w*5;if(d<o||d>=o+N)continue;wl+=(d>o?'<span class="wkl" style="left:'+pc(d)+'"></span>':'');wh+='<span class="wh" style="left:'+pc(d)+'">Week of '+WK[w]+'</span>';}
 for(var k=o;k<o+N;k++)dl+='<span class="dl" style="left:'+pc(k)+';width:'+(100/N).toFixed(3)+'%">'+'MTWTF'[k%5]+'</span>';
 var tdy='<span class="tdy" style="left:'+pc(TODAY)+'"></span>';
 var h='<div class="bd" id="bd" style="--dw:'+dw+'"><div class="brow h bh"><div class="lc"><b style="font-size:9.6px">Job</b><small>Today is Mon Nov 23</small></div><div class="trk">'+wl+wh+dl+'</div></div>';
 JOBS.forEach(function(j){h+='<div class="brow"><button type="button" class="lc" id="j-'+j[0]+'"><span class="t1"><span class="mono" style="font-weight:600">'+j[0]+'</span>'+chip(status(j))+'</span><small>'+j[1]+'</small></button><div class="trk">'+wl+tdy+
  bars(j).map(function(b){var s=STG[b[0]],mv=j[0]==='J-2421'&&b[0]>=3,from=S.anim&&mv?b[3]:b[1];return '<span class="bar'+(mv?' mv':'')+(mv&&S.moved?' lit':'')+'" data-to="'+pc(b[1])+'" style="left:'+pc(from)+';width:calc('+(b[2]/N*100).toFixed(3)+'% - 3px);margin-left:1.5px;background:'+s[2]+';color:'+s[3]+'">'+(b[2]<2&&N>10?'':s[1])+'</span>';}).join('')+'</div></div>';});
 h+='<div class="ccrow"><div class="lc"><b style="font-size:9.8px">Finish room</b><small>'+CAP+' h a week</small></div><div class="trk">';
 for(w=0;w<4;w++){d=w*5;if(d<o||d>=o+N)continue;h+='<span style="position:absolute;left:'+pc(d)+';width:calc('+(500/N).toFixed(3)+'% - 6px);top:0;bottom:0">'+ccell(w,false)+'</span>';}
 h+='</div></div>';
 if(S.scr==='cap'){var bk=booked(S.cw),l=load(S.cw);h+='<div class="cpn" id="cpn"><div class="ct">Finish room, week of '+WK[S.cw]+'<span class="ch c-warn">'+l+' of '+CAP+' h</span></div>'+
  bk.map(function(j){return '<div class="row"><span class="mono">'+j[0]+'</span><span>'+j[1]+'</span><span class="mono r">'+j[4]+' h</span></div>';}).join('')+
  '<div class="row tot"><span>Booked</span><span class="mut" style="font-weight:500">Over by '+(l-CAP)+' h</span><span class="mono r" id="cpt">'+l+' h</span></div>'+sugg()+'</div>';}
 return h+'</div>';}
function sugg(){return '<div class="sug"><b>Suggested move</b><span class="mut">J-2421 is due Dec 18, so its finish can wait a week. Nov 30 has room.</span><button type="button" class="bt" id="mv">Move J-2421 finish to Nov 30</button></div>';}
function legend(){return '<div class="lgd2">'+STG.map(function(s){return '<span><i style="background:'+s[2]+';color:'+s[3]+'">'+(s[1]===s[0]?'':'')+'</i>'+s[0]+(s[1]!==s[0]?' <span class="mut">('+s[1]+')</span>':'')+'</span>';}).join('')+'<span><i style="background:#18181B;width:2px;height:12px;border-radius:1px"></i>Today</span></div>';}
function floor(){if(S.wk!=null){var bk=booked(S.wk),l=load(S.wk);
  return '<div class="cd fl" style="flex:1 1 0"><div class="ct">Finish room, week of '+WK[S.wk]+'<span class="ch '+(l>CAP?'c-warn':'c-ok')+'">'+l+' of '+CAP+' h</span></div>'+bk.map(function(j){return '<div class="row in"><span class="mono">'+j[0]+'</span><span>'+j[1]+'</span><span class="mut">Finish</span><span class="mono">'+j[4]+' h</span></div>';}).join('')+
  '<div class="row"><span></span><span class="mut">Week of '+WK[1]+'</span><span class="mut">Finish</span><span class="mono" id="w1">'+load(1)+' of '+CAP+' h</span></div><div class="row"><span></span><span class="mut">Week of '+WK[2]+'</span><span class="mut">Finish</span><span class="mono" id="w2">'+load(2)+' of '+CAP+' h</span></div></div>';}
 var rows=[['J-2417','Kitchen cabinets',S.fin?'Finish':'Stain',S.fin?'TR, since 7:42':'TR, 6.5 of 10 h'],['J-2418','Dining table','Finish','AL, starts 8:00'],['J-2419','Primary closet built-ins','Stain','MK, 2.0 of 6 h'],['J-2420','Reception desk','Build fronts','DS, 4.5 of 22 h'],['J-2421','Bookcase wall','Stain','JP, 3.0 of 8 h']];
 return '<div class="cd fl" style="flex:1 1 0"><div class="ct">On the floor today<span class="mut" style="font-weight:500">Mon Nov 23</span></div>'+rows.map(function(x){return '<div class="row"><span class="mono">'+x[0]+'</span><span>'+x[1]+'</span><span class="mut">'+x[2]+'</span><span class="mono mut">'+x[3]+'</span></div>';}).join('')+'</div>';}
function stages(P){var rows=[['Mill','Nov 9 to 11','done','14 of 14 h','JP'],['Build fronts','Nov 16 to 18','done','22 of 22 h','DS'],['Stain','Nov 19 to 23',S.fin?'done':'cur',(S.fin?n1(S.st):'6.5')+' of 10 h','TR'],['Finish','Nov 24 to 27',S.fin?'cur':'wait',S.fin?'TR, since 7:42':'32 h planned',S.fin?'TR':''],['Assemble','Nov 30 to Dec 2','wait','18 h planned',''],['Install','Dec 7 and 8','wait','12 h planned','']];
 return '<div class="cd sl"'+(P?'':' style="flex:none"')+'><div class="ct">Stages<span class="mut" style="font-weight:500">Routing: frameless cabinets</span></div>'+rows.slice(P?1:0).map(function(x){var c=x[2]==='done'?['c-ok','Done']:x[2]==='cur'?['c-info','In progress']:['c-idle','Waiting'];
  var mid=x[2]==='cur'&&x[0]==='Stain'?'<span style="display:flex;align-items:center;gap:6px"><span class="op">TR</span><span class="pbar" style="flex:1"><i style="width:65%"></i></span><span class="mono">6.5 of 10 h</span></span>':'<span class="mono mut">'+(x[4]?'<span class="op">'+x[4]+'</span>':'')+x[3]+'</span>';
  if(P)mid=x[2]==='cur'&&x[0]==='Stain'?'<span class="mono">6.5 of 10 h</span>':'<span class="mono mut">'+x[3]+'</span>';
  return '<div class="row'+(x[2]==='cur'?' cur':'')+'" id="sg-'+x[0].split(' ')[0]+'"><span style="font-weight:'+(x[2]==='cur'?600:400)+'">'+x[0]+'</span>'+(P?'':'<span class="mut">'+x[1]+'</span>')+mid+'<span>'+chip(c)+'</span></div>';}).join('')+'</div>';}
function clock(P){if(S.fin&&P)return '<div class="pn in" id="sd">Stain closed at '+n1(S.st)+' of '+n1(STAINE)+' h, TR in Finish</div>';if(S.fin)return '<div class="cd"><div class="ck"><b>Finish in progress</b><span class="mut">TR clocked in at 7:42 on the finish room tablet.</span><div class="wl"><span>Stain closed</span><b id="sd">'+n1(S.st)+' of '+n1(STAINE)+' h</b></div></div></div>';
 if(!S.sheet&&P)return '<button type="button" class="bt" id="clk" style="height:30px;flex:none">Clock in to Finish</button>';if(!S.sheet)return '<div class="cd"><div class="ck">'+(P?'':'<b>Next step</b><span class="mut">Stain has 3.5 h left on the estimate. Finish is next in the routing.</span>')+'<button type="button" class="bt" id="clk">Clock in to Finish</button></div></div>';
 return '<div class="cd in"><div class="ck frm"><b>Close Stain, start Finish</b><div class="wl"><span>Stain logged</span><b>'+n1(STAIN0)+' h</b></div><label class="fld" id="fs"><small>Stain hours this session, TR</small><input id="is" value="'+S.vs+'" inputmode="decimal" autocomplete="off"><span class="em">Hours between 0.1 and 8</span></label><div class="wl"><span>Stain total</span><b id="stt">'+n1(STAIN0+num(S.vs))+' of '+n1(STAINE)+' h</b></div><button type="button" class="bt pri" id="go">Start Finish</button></div></div>';}
function n1(v){var r=Math.round(v*10)/10;return r%1?r.toFixed(1):String(r);}
function num(v){v=parseFloat(String(v).replace(/\s*h$/i,''));return isFinite(v)?v:0;}
function render(){var P=ph(),h='',scr=S.scr;
if(scr==='board'||scr==='cap'){var cap=scr==='cap';
 setNav({m:'sch',bc:cap?['Schedule','Production board','Finish room, '+WK[S.cw]]:['Schedule','Production board'],t:cap&&P?'Finish, '+WK[S.cw]:'Production board',chip:load(1)>CAP?['c-warn','1 room over']:['c-ok','All rooms fit'],scr:cap?'Finish capacity':'Schedule board',back:cap&&P?1:0,pa:cap&&P?'':seg()});
 if(!P){h=board()+legend()+floor();}
 else if(cap){var bk=booked(S.cw),l=load(S.cw);h='<div class="cpn"><div class="ct">Booked in Finish<span class="ch c-warn">'+l+' of '+CAP+' h</span></div>'+bk.map(function(j){return '<div class="row" style="grid-template-columns:50px 1fr 34px;min-height:24px"><span class="mono">'+j[0]+'</span><span>'+j[1]+'</span><span class="mono r">'+j[4]+' h</span></div>';}).join('')+'</div><button type="button" class="bt" id="mv" style="height:30px">Move J-2421 finish to Nov 30</button>';}
 else{var ws=S.v===2?[1,2]:[1,2,3];h='<div class="wks" style="grid-template-columns:repeat('+ws.length+',1fr)">'+ws.map(function(w){return ccell(w,true);}).join('')+'</div>';
  if(S.wk!=null)h+='<div class="pn in">'+WK[S.wk]+': '+booked(S.wk).map(function(j){return j[0]+' '+j[4]+' h';}).join(', ')+'</div>';
  h+='<div class="cd pj">'+JOBS.filter(function(j){return j[0]!=='J-2420';}).slice(0,S.wk!=null?3:4).map(function(j){return '<button type="button" class="row" id="j-'+j[0]+'"><span class="mono">'+j[0]+'</span><span>'+j[1]+'</span><span>'+chip(status(j))+'</span></button>';}).join('')+'</div>';}}
else{setNav({m:'sch',bc:['Schedule','Production board','J-2417'],t:P?'J-2417':'J-2417 Kitchen cabinets',chip:S.fin?['c-ok','In Finish']:['c-idle','In Stain'],scr:'Job J-2417',back:P?1:0,pa:'<button type="button" class="bt" id="cls">'+(P?'Board':'Back to board')+'</button>'});
 if(P){h=S.sheet?clock(P):stages(P)+clock(P);}
 else{h='<div class="jg"><div>'+stages(P)+'</div><div class="side"><div class="cd"><div class="ct">Job</div><div class="ck"><div class="wl"><span class="mut">Customer</span><span>Hollis residence</span></div><div class="wl"><span class="mut">Due</span><span>Dec 8</span></div><div class="wl"><span class="mut">Finish room</span><span>Booked Nov 24 to 27</span></div></div></div>'+clock(P)+'</div></div>'+
  '<div class="cd fl" style="flex:1 1 0"><div class="ct">Time log<span class="mut" style="font-weight:500">J-2417</span></div>'+(S.fin?'<div class="row in"><span class="mono mut">7:42</span><span>TR clocked in to Finish</span><span class="mut">Tablet 3</span><span class="mono">Started</span></div><div class="row in"><span class="mono mut">7:41</span><span>TR closed Stain</span><span class="mut">Tablet 3</span><span class="mono">'+n1(num(S.vs))+' h</span></div>':'')+
  '<div class="row"><span class="mono mut">Nov 20</span><span>TR on Stain</span><span class="mut">Tablet 3</span><span class="mono">6.5 h</span></div><div class="row"><span class="mono mut">Nov 18</span><span>DS on Build fronts</span><span class="mut">Tablet 1</span><span class="mono">8.0 h</span></div><div class="row"><span class="mono mut">Nov 17</span><span>DS on Build fronts</span><span class="mut">Tablet 1</span><span class="mono">7.5 h</span></div><div class="row"><span class="mono mut">Nov 16</span><span>DS on Build fronts</span><span class="mut">Tablet 1</span><span class="mono">6.5 h</span></div></div>';}}
$('pg').innerHTML=h;
if(S.anim){S.anim=false;setTimeout(function(){[].forEach.call(root.querySelectorAll('.bar.mv'),function(b){b.style.left=b.getAttribute('data-to');});},60);}}
$('pg').addEventListener('input',function(e){if(e.target.id==='is'){S.vs=e.target.value;var t=$('stt');if(t)t.textContent=n1(STAIN0+num(S.vs))+' of '+n1(STAINE)+' h';}});
function resetState(){S={scr:'board',v:2,cw:1,wk:null,moved:false,anim:false,sheet:false,fin:false,st:0,vs:'3.5'};render();}
function okS(){var v=num($('is').value),b=!(v>0&&v<=8);$('fs').classList.toggle('err',b);return !b;}
var CAPAT=function(hh){return ph()?{l:8,t:5}:{l:14,t:visH()-hh-40};};
var ST=[
{id:'view',target:function(){return $('v4');},prompt:'Click 4 weeks',where:'below',run:function(){S.v=4;render();},after:['Every job, every stage, one calendar','Five jobs and six stages, Nov 16 to Dec 11, with the Finish room underneath.'],pc:'Every job and stage on one calendar'},
{id:'cap',target:function(){return $('cc-1');},prompt:'Click the amber week',where:'above',run:function(){S.scr='cap';S.cw=1;render();},
 after:function(){return['Finish is booked '+load(1)+' of '+CAP+' hours this week',booked(1).map(function(j){return j[0]+' '+j[4];}).join(', ')+' hours. Over by '+(load(1)-CAP)+'.'];},pc:'Finish is booked 92 of 80 hours'},
{id:'move',target:function(){return $('mv');},prompt:'Click Move J-2421 finish to Nov 30',where:'below',run:function(q){S.moved=true;S.scr='board';S.anim=!q;render();},after:['Move one stage and capacity updates','J-2421 finish moves to Nov 30, with assemble and install behind it.'],pc:'Move one stage, capacity updates'},
{id:'fit',target:function(){return $('cc-2');},prompt:'Click the Nov 30 week',where:'above',run:function(){S.wk=2;render();},
 after:function(){return['Both weeks now fit','Nov 23 is '+load(1)+' of '+CAP+' hours and Nov 30 is '+load(2)+' of '+CAP+'.'];},pc:'Both weeks now fit'},
{id:'job',target:function(){return $('j-J-2417');},prompt:'Click job J-2417',where:'right',run:function(){S.scr='job';render();},after:['Open any job to see where it stands','Mill and fronts are done, stain is at 6.5 of 10 hours, finish is waiting.'],pc:'Open any job to see where it stands'},
{id:'clk',target:function(){return $('clk');},prompt:'Click Clock in to Finish',where:'below',run:function(){S.sheet=true;render();},after:['Operators clock into a step on any device','TR closes stain with this session\'s hours, then finish starts.'],pc:'Operators clock in on any device'},
{id:'go',target:function(){return $('go');},prompt:'Click Start Finish',where:'above',ok:okS,run:function(){if($('is'))S.vs=$('is').value;S.st=STAIN0+num(S.vs);S.sheet=false;S.fin=true;render();},
 after:function(){return['Stain closes at '+n1(S.st)+' of '+n1(STAINE)+' hours and finish starts','J-2417 moves from stain to finish, clocked in by TR.'];},pc:'Stain closes and finish starts'},
{id:'back',target:function(){return $('cls');},prompt:'Click Back to board',where:'below',run:function(){S.scr='board';S.wk=null;render();},after:['The calendar follows the floor without a status meeting','J-2417 shows In Finish on the board, on time for Dec 8.'],pc:'The calendar follows the floor'}];
'''
