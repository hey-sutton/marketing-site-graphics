"""Coffee roasting card 1: Roast Planning & Scheduling.
Layout: board. A day strip and a Day, Week, Month toggle on top; a stage board (Pick, Roast, Rest, Pack) with the roaster
queue under it; on the right an order tray, the packing stations and a rush order panel.
A wholesale order dropped on the day turns into three roast batches; the same schedule reads the same in the day, week and
month views; packing stations fill by bag size; a rush order shows which batches it moves before you confirm.
Every number is computed from the data below, so the counts in the three views always agree."""
from frame_auto import header

SUMMARY = 'Roast Planning & Scheduling (open a day board by stage, drag a wholesale order on and see its roast batches, switch day, week and month views, fill packing stations by bag size, pull a rush order forward and read what moves)'
ARIA = 'Interactive product screen: the roast day board for Wednesday November 18 with Pick, Roast, Rest and Pack stages; order W-2041 creates three 20 kg roast batches, the week and month views count the day the same, two packing stations fill with 12 oz and 5 lb bags, and rush order R-2055 moves two later batches by one slot'
STEPS = 5
STUDIO = dict(lede='A typical roast day board, built on your Sutton data with Studio. Want it different? Describe the change.',
              examples=['Add a second roaster', 'Block a batch until green arrives', 'Set rest time by roast level', 'Color batches by origin'],
              built_on='Orders, BOMs, roast batches and stations', change='Stages, slots and rules')

ICON = '<rect x="2" y="3" width="12" height="10.5" rx="1.5"/><path d="M2 6.5h12M5.5 2v2.5M10.5 2v2.5M6.5 6.5v7M10 6.5v7"/>'

CSS = (
 '.k1{padding:10px 40px 0 16px;display:flex;flex-direction:column;gap:10px}'
 '.k1t{height:44px;flex:none;display:flex;align-items:center;gap:6px;padding:0 10px}.k1t .lb{font-size:10px;font-weight:600;margin-right:4px;white-space:nowrap}'
 '.dy{font:inherit;font-size:9.6px;padding:5px 9px;border:1px solid #E4E4E7;border-radius:6px;background:#fff;color:#52525B;cursor:pointer;white-space:nowrap}.dy.on{background:#18181B;border-color:#18181B;color:#fff}.dy.fakehover:not(.on){background:#F4F4F5}.dy:focus-visible,.vw:focus-visible{outline:2px solid #18181B;outline-offset:2px}'
 '.vg{margin-left:auto;display:inline-flex;padding:2px;gap:2px;border:1px solid #E4E4E7;border-radius:7px;background:#FAFAFA}'
 '.vw{font:inherit;font-size:9.4px;padding:4px 9px;border:0;border-radius:5px;background:transparent;color:#52525B;cursor:pointer}.vw.on{background:#fff;color:#18181B;font-weight:600;box-shadow:0 0 0 1px #E4E4E7}.vw.fakehover:not(.on){background:#F4F4F5}'
 '.k1m{display:grid;grid-template-columns:432px 218px;gap:10px;height:482px;flex:none}.k1r{display:flex;flex-direction:column;gap:8px;min-width:0}'
 '.brd{display:flex;flex-direction:column}.brd>.empt{margin:10px;flex:1}'
 '.cols{display:grid;grid-template-columns:repeat(4,1fr);gap:6px;padding:8px 9px 0;height:282px;flex:none}'
 '.col{background:#FAFAFA;border:1px solid #F0F0F1;border-radius:7px;padding:5px;display:flex;flex-direction:column;gap:4px;min-width:0}.brd.drop{box-shadow:0 0 0 2px #FCD34D}.brd.drop .col{background:#FFFBEB}'
 '.colh{display:flex;align-items:center;justify-content:space-between;font-size:9.4px;font-weight:600;padding:1px 2px 3px}.colh .ch{font-family:"JetBrains Mono",ui-monospace,monospace}'
 '.it{background:#fff;border:1px solid #E4E4E7;border-radius:6px;padding:4px 6px;display:flex;flex-direction:column;gap:1px;font-size:8.6px;color:#71717A;line-height:1.3}.it b{font-family:"JetBrains Mono",ui-monospace,monospace;font-size:9.2px;color:#18181B;font-weight:600}'
 '.it.nw{border-color:#A5B4FC;background:#F5F7FF}.it.ru{border-color:#FCA5A5;background:#FEF2F2}.it.mv{border-color:#FCD34D;background:#FFFBEB}.col .none{font-size:8.6px;color:#A1A1AA;text-align:center;padding:10px 2px}'
 '.qh{display:flex;justify-content:space-between;align-items:center;padding:9px 11px 4px;font-size:9.8px;font-weight:600}.qh span{font-weight:400;color:#71717A;font-size:8.8px}'
 '.qs{display:grid;grid-template-columns:repeat(5,1fr);gap:5px;padding:0 11px}.sl{height:96px;border:1px dashed #E4E4E7;border-radius:7px;padding:6px;display:flex;flex-direction:column;gap:3px;font-size:8.6px;color:#A1A1AA}'
 '.sl .tm{font-family:"JetBrains Mono",ui-monospace,monospace;font-size:9px;color:#71717A}.sl b{font-family:"JetBrains Mono",ui-monospace,monospace;font-size:10px;color:#18181B}.sl.f{border-style:solid;background:#fff;color:#52525B}.sl.ru{border-color:#FCA5A5;background:#FEF2F2}.sl.mv{border-color:#FCD34D;background:#FFFBEB}'
 '.wt .row{grid-template-columns:70px repeat(4,1fr) 56px;min-height:38px;font-size:9.6px}.wt .row.h{min-height:24px}.wt .row>span:not(:first-child){text-align:right;font-family:"JetBrains Mono",ui-monospace,monospace}.wt .row.on{background:#FFFBEB;font-weight:600}'
 '.cmp{margin:10px 11px 0;border:1px solid #E4E4E7;border-radius:7px;overflow:hidden}.cmp .row{grid-template-columns:70px repeat(4,1fr) 56px;min-height:28px;font-size:9.4px}.cmp .row>span:not(:first-child){text-align:right;font-family:"JetBrains Mono",ui-monospace,monospace}'
 '.cmpn{padding:8px 11px 0;font-size:8.8px;color:#71717A;line-height:1.4}'
 '.mg{display:grid;grid-template-columns:repeat(5,1fr);gap:5px;padding:8px 9px 0}.mg .dh{font-size:8.8px;color:#71717A;text-align:center;padding-bottom:2px}'
 '.mcel{height:94px;border:1px solid #F0F0F1;border-radius:7px;padding:5px 6px;display:flex;flex-direction:column;gap:4px;background:#fff}.mcel.pa{background:#FAFAFA}.mcel.on{border-color:#FCD34D;background:#FFFBEB}'
 '.mcel .dn{font-size:9.6px;font-weight:600}.mcel .tc{font-size:8.6px;color:#71717A}.mcel .sc{display:grid;grid-template-columns:1fr 1fr;gap:2px 4px;font-size:8.4px;color:#52525B}.mcel .sc span{display:flex;justify-content:space-between}.mcel .sc b{font-family:"JetBrains Mono",ui-monospace,monospace}'
 '.kor{height:132px;flex:none}.kps{height:166px;flex:none}.krs{flex:1 1 auto}.kor .empt,.kps .empt,.krs .empt{margin:8px 9px;height:calc(100% - 46px);padding:8px}'
 '.oc{margin:8px 9px 0;width:calc(100% - 18px);font:inherit;text-align:left;border:1px solid #D4D4D8;border-radius:7px;background:#fff;padding:7px 9px;display:flex;flex-direction:column;gap:2px;cursor:grab;font-size:8.8px;color:#71717A}'
 '.oc b{font-family:"JetBrains Mono",ui-monospace,monospace;font-size:10px;color:#18181B}.oc.fakehover{background:#F4F4F5}.oc:focus-visible{outline:2px solid #18181B;outline-offset:2px}.oc.dn{cursor:default;border-style:dashed;background:#FAFAFA}'
 '.st{padding:6px 11px 2px;display:flex;flex-direction:column;gap:3px;font-size:9.2px}.st .l{display:flex;justify-content:space-between}.st .l b{font-family:"JetBrains Mono",ui-monospace,monospace}.st small{font-size:8.4px;color:#71717A}'
 '.bar{height:7px;border-radius:4px;background:#F4F4F5;overflow:hidden}.bar i{display:block;height:100%;border-radius:4px;background:#52525B;transition:width .6s cubic-bezier(.22,.9,.28,1)}'
 '.rsr{padding:7px 11px 4px;font-size:9px;color:#71717A;line-height:1.4}.rsr b{color:#18181B;font-family:"JetBrains Mono",ui-monospace,monospace}'
 '.krs .row{grid-template-columns:44px 1fr;min-height:24px;font-size:8.8px;padding:0 11px}.krs .row .mono{font-weight:600}.krs .row.mv{background:#FFFBEB}.krs .row.ru{background:#FEF2F2}.krs .bt{font-size:9px;padding:4px 8px}.kbt{padding:6px 11px 0;display:flex;gap:6px;align-items:center}'
)

WIN = (
 header(ICON, 'Roast schedule', 'Roaster 1 and packing, week of Nov 16', '<span class="ch c-idle" id="kst">No day open</span>')
 + '<div class="k1"><div class="cd k1t" id="k1t"><span class="lb">Roast day</span>'
 + ''.join('<button type="button" class="dy" id="kd%d">%s</button>' % (i, d) for i, d in enumerate(['Mon 16', 'Tue 17', 'Wed 18', 'Thu 19', 'Fri 20']))
 + '<span class="vg" role="group" aria-label="Schedule view"><button type="button" class="vw on" id="kvD" aria-pressed="true">Day</button><button type="button" class="vw" id="kvW" aria-pressed="false">Week</button><button type="button" class="vw" id="kvM" aria-pressed="false">Month</button></span></div>'
 '<div class="k1m"><div class="cd brd" id="kbd"></div><div class="k1r"><div class="cd kor" id="kor"></div><div class="cd kps" id="kps"></div><div class="cd krs" id="krs"></div></div></div></div>'
)

JS = r'''
var FOC='.hd>*,.k1t>*,.brd,.kor,.kps,.krs';
var STG=[['P','Pick'],['R','Roast'],['E','Rest'],['K','Pack']];
var DAYS=['Mon 16','Tue 17','Wed 18','Thu 19','Fri 20'],WD=2;
/* the rest of the week, already planned: Pick, Roast, Rest, Pack counts per day */
var OTHER={0:[2,2,1,2],1:[2,2,2,1],3:[2,2,3,2],4:[1,1,2,2]};
/* past and next weeks for the month view, Pick, Roast, Rest, Pack per weekday */
var MONTH={2:[[2,2,1,2],[2,2,2,2],[1,1,2,1],[2,2,1,2],[1,1,2,2]],9:[[2,2,2,1],[1,1,2,2],[2,2,1,2],[2,2,2,2],[1,1,1,2]],23:[[2,2,0,0],[1,1,0,0],[0,0,0,0],[0,0,0,0],[1,1,0,0]]};
var REST=[{id:'L-1117',t:'Foundry espresso, rested 18 h'},{id:'L-1118',t:'Mesa decaf, rested 20 h'}];
var ORD={id:'W-2041',c:'Larkspur Cafe Group',p:'Foundry espresso',g:60000,b:['B-301','B-302','B-303']};
var RUSH={id:'R-2055',c:'Juniper Street Coffee',p:'Daybreak roast',g:15000,b:'B-305',due:'14:00'};
var STN=[{id:'Station 1',sz:'12 oz',lot:'L-1117',p:'Foundry espresso',n:96,cap:240},{id:'Station 2',sz:'5 lb',lot:'L-1118',p:'Mesa decaf',n:8,cap:40}];
var SLOT0=420,SLOT=45;
var S;
function kg(g){return (g/1000).toFixed(1);}
function hm(t){var h=Math.floor(t/60),m=t%60;return (h<10?'0':'')+h+':'+(m<10?'0':'')+m;}
function batchG(){return ORD.g/ORD.b.length;}
function base(){return S.ord?ORD.b.slice():[];}
function queue(){var q=base();if(S.rush)q.splice(1,0,RUSH.b);return q;}
function slotOf(q,b){return SLOT0+q.indexOf(b)*SLOT;}
function moved(){var a=base(),q=queue();return a.filter(function(b){return q.indexOf(b)!==a.indexOf(b);});}
function wed(){var q=queue();return [q.length,q.length,REST.length,S.stn?STN.length:0];}
function counts(d){return d===WD?wed():OTHER[d];}
function pct(s){return Math.round(s.n/s.cap*100);}
function gOf(b){return b===RUSH.b?RUSH.g:batchG();}
function dayView(){var q=queue(),mv=moved(),c=wed(),col=function(k,i,items){return '<div class="col" id="kcl'+k+'"><div class="colh"><span>'+STG[i][1]+'</span><span class="ch c-idle" id="kc'+k+'">'+c[i]+'</span></div>'+(items.length?items.join(''):'<div class="none">Nothing here yet</div>')+'</div>';};
var pick=q.map(function(b){return '<div class="it'+(b===RUSH.b?' ru':' nw')+'"><b>'+b+'</b>Pick '+kg(gOf(b))+' kg green</div>';});
var roast=q.map(function(b){return '<div class="it'+(b===RUSH.b?' ru':mv.indexOf(b)>=0?' mv':' nw')+'"><b>'+b+'</b>'+hm(slotOf(q,b))+', Roaster 1</div>';});
var rest=REST.map(function(l){return '<div class="it"><b>'+l.id+'</b>'+l.t+'</div>';});
var pack=S.stn?STN.map(function(s){return '<div class="it nw"><b>'+s.sz+'</b>'+s.id+', '+s.lot+'</div>';}):[];
var slots='';for(var i=0;i<5;i++){var b=q[i],cls=b?(' f'+(b===RUSH.b?' ru':mv.indexOf(b)>=0?' mv':'')):'';slots+='<div class="sl'+cls+'" id="ks'+i+'"><span class="tm">'+hm(SLOT0+i*SLOT)+'</span>'+(b?'<b>'+b+'</b><span>'+(b===RUSH.b?RUSH.p:ORD.p)+'</span><span>'+kg(gOf(b))+' kg green</span>':'<span>Open slot</span>')+'</div>';}
return '<div class="cols">'+col('P',0,pick)+col('R',1,roast)+col('E',2,rest)+col('K',3,pack)+'</div><div class="qh">Roaster 1 queue<span>45 minute slots from 07:00</span></div><div class="qs">'+slots+'</div>';}
function row(lbl,c,cls,idp){var t=c.reduce(function(a,b){return a+b;},0);return '<div class="row'+(cls||'')+'"><span>'+lbl+'</span>'+c.map(function(v,i){return '<span'+(idp?' id="'+idp+STG[i][0]+'"':'')+'>'+v+'</span>';}).join('')+'<span>'+t+'</span></div>';}
function weekView(){var h='<div class="row h"><span>Day</span>'+STG.map(function(s){return '<span>'+s[1]+'</span>';}).join('')+'<span>Total</span></div>';
var rows=DAYS.map(function(d,i){return row(d,counts(i),i===WD?' on':'',i===WD?'kw':'');}).join('');
var c=wed();
return '<div class="wt">'+h+rows+'</div><div class="cmp">'+'<div class="row h"><span>Wed 18 in</span>'+STG.map(function(s){return '<span>'+s[1]+'</span>';}).join('')+'<span>Total</span></div>'+row('Day view',c)+row('Week view',counts(WD))+row('Month view',monthCell(16,WD))+'</div><div class="cmpn">One schedule behind every view. Move a batch in any view and the other two follow.</div>';}
function monthCell(w,d){return w===16?counts(d):MONTH[w][d];}
function monthView(){var h=['Mon','Tue','Wed','Thu','Fri'].map(function(d){return '<span class="dh">'+d+'</span>';}).join(''),cells='';
[2,9,16,23].forEach(function(w){for(var d=0;d<5;d++){var c=monthCell(w,d),t=c.reduce(function(a,b){return a+b;},0),on=w===16&&d===WD;
cells+='<div class="mcel'+(w<16?' pa':'')+(on?' on':'')+'"><span class="dn">Nov '+(w+d)+'</span><span class="tc">'+t+' items</span><span class="sc">'+STG.map(function(s,i){return '<span>'+s[1]+'<b'+(on?' id="km'+s[0]+'"':'')+'>'+c[i]+'</b></span>';}).join('')+'</span></div>';}});
return '<div class="mg">'+h+cells+'</div>';}
function render(){
var B=$('kbd'),vn={day:'Day',week:'Week',month:'Month'};
['D','W','M'].forEach(function(k,i){var v=['day','week','month'][i],e=$('kv'+k);e.classList.toggle('on',S.v===v);e.setAttribute('aria-pressed',S.v===v?'true':'false');});
for(var i=0;i<5;i++)$('kd'+i).classList.toggle('on',S.open&&i===WD);
if(!S.open)B.innerHTML='<div class="ct"><span>Roast board</span></div><div class="empt"><b>No day open</b><span>Pick a roast day to load its board: Pick, Roast, Rest and Pack.</span></div>';
else B.innerHTML='<div class="ct"><span>'+(S.v==='day'?'Wed Nov 18, by stage':S.v==='week'?'Week of Nov 16':'November 2026')+'</span><span class="ch c-info">'+vn[S.v]+' view</span></div>'+(S.v==='day'?dayView():S.v==='week'?weekView():monthView());
var O=$('kor');
if(!S.open)O.innerHTML='<div class="ct"><span>Orders to schedule</span></div><div class="empt"><b>Nothing to schedule</b><span>Open a day to see orders waiting for it.</span></div>';
else O.innerHTML='<div class="ct"><span>Orders to schedule</span><span class="ch '+(S.ord?'c-ok':'c-warn')+'">'+(S.ord?'Scheduled':'1 waiting')+'</span></div><button type="button" class="oc'+(S.ord?' dn':'')+'" id="kor1" draggable="'+(S.ord?'false':'true')+'" aria-label="Order '+ORD.id+', drag onto the board or press to schedule"><b>'+ORD.id+', wholesale</b><span>'+ORD.c+'</span><span>'+ORD.p+', '+kg(ORD.g)+' kg green</span><span>'+(S.ord?'On Wed 18, '+ORD.b.length+' batches':'Drag onto the board')+'</span></button>';
var P=$('kps');
if(!S.ord)P.innerHTML='<div class="ct"><span>Packing stations</span></div><div class="empt"><b>No packing planned</b><span>Stations fill by bag size once the day is planned.</span></div>';
else P.innerHTML='<div class="ct"><span>Packing stations</span>'+(S.stn?'<span class="ch c-ok">2 filled</span>':'<button type="button" class="bt pri" id="kfs">Fill stations</button>')+'</div>'+STN.map(function(s,i){return '<div class="st"><span class="l"><span>'+s.id+', '+s.sz+' bags</span><b id="kp'+i+'">'+(S.stn?s.n+' bags':'0 bags')+'</b></span><span class="bar"><i style="width:'+(S.stn?pct(s):0)+'%"></i></span><small id="kq'+i+'">'+(S.stn?s.lot+' '+s.p+', '+pct(s)+'% of '+s.cap+' per shift':'Empty, '+s.cap+' bags per shift')+'</small></div>';}).join('');
var R=$('krs');
if(!S.stn)R.innerHTML='<div class="ct"><span>Rush order</span></div><div class="empt"><b>No rush orders</b><span>A rush order shows what it moves before you confirm.</span></div>';
else if(!S.rush)R.innerHTML='<div class="ct"><span>Rush order</span><span class="ch c-bad">Due '+RUSH.due+'</span></div><div class="rsr"><b>'+RUSH.id+'</b> '+RUSH.c+'<br>'+RUSH.p+', 1 batch of '+kg(RUSH.g)+' kg green</div><div class="kbt"><button type="button" class="bt pri" id="kpf">Pull forward</button></div>';
else{var q=queue(),a=base(),mv=moved();R.innerHTML='<div class="ct"><span>Rush order '+RUSH.id+'</span>'+(S.conf?'<span class="ch c-ok">Confirmed</span>':'<span class="ch c-warn" id="kmv">Moves '+mv.length+'</span>')+'</div><div class="row ru"><span class="mono">'+RUSH.b+'</span><span id="krb">New at '+hm(slotOf(q,RUSH.b))+'</span></div>'+mv.map(function(b,i){return '<div class="row mv"><span class="mono">'+b+'</span><span id="krm'+i+'">'+hm(slotOf(a,b))+' to '+hm(slotOf(q,b))+'</span></div>';}).join('')+(S.conf?'':'<div class="kbt"><button type="button" class="bt" id="kcf">Confirm</button></div>');}
var st=$('kst');st.textContent=S.conf?'Rush confirmed':S.rush?'Rush pending':S.open?'Wed 18 open':'No day open';st.className='ch '+(S.rush&&!S.conf?'c-warn':S.open?'c-info':'c-idle');}
function setView(v){if(!S.open)return;S.v=v;render();}
$('kvD').addEventListener('click',function(){setView('day');});$('kvW').addEventListener('click',function(){setView('week');});$('kvM').addEventListener('click',function(){setView('month');});
winEl.addEventListener('click',function(e){var t=e.target.closest&&e.target.closest('#kcf');if(t&&mode!=='watch'){S.conf=true;render();}});
/* a drag only marks the board: re-rendering the dragged chip mid-drag would cancel the drag */
winEl.addEventListener('dragstart',function(e){if(e.target&&e.target.id==='kor1'&&!S.ord){S.drag=true;try{e.dataTransfer.setData('text/plain',ORD.id);e.dataTransfer.effectAllowed='move';}catch(x){}$('kbd').classList.add('drop');}});
winEl.addEventListener('dragend',function(){S.drag=false;$('kbd').classList.remove('drop');});
winEl.addEventListener('dragover',function(e){if(S.drag&&e.target.closest&&e.target.closest('#kbd'))e.preventDefault();});
winEl.addEventListener('drop',function(e){if(!S.drag)return;e.preventDefault();S.drag=false;$('kbd').classList.remove('drop');if(mode==='try'&&ST[cur].id==='ord')doStep();});
function resetState(){S={open:false,v:'day',ord:false,stn:false,rush:false,conf:false,drag:false};render();}
var ST=[
{id:'day',target:function(){return $('kd2');},prompt:'Open the board for Wed 18',where:'below',run:function(){S.open=true;S.v='day';render();},
 after:function(){return['A day board by stage','Wed 18 opens with Pick, Roast, Rest and Pack. Two lots roasted on Tuesday are resting before packing.'];}},
{id:'ord',target:function(){return $('kor1');},prompt:'Drag order W-2041 onto the board, or click it',where:'below',run:function(){S.ord=true;S.v='day';render();},
 after:function(){return['An order becomes roast batches',ORD.id+' needs '+kg(ORD.g)+' kg of green: '+ORD.b.length+' batches of '+kg(batchG())+' kg on Roaster 1, picked and roasted on Wed 18.'];}},
{id:'view',target:function(){return $('kvW');},prompt:'Switch to the week view',where:'below',run:function(){S.v='week';render();},
 after:function(){var c=wed();return['One schedule, three views','Wed 18 counts the same in the day, week and month views: Pick '+c[0]+', Roast '+c[1]+', Rest '+c[2]+', Pack '+c[3]+'.'];}},
{id:'stn',target:function(){return $('kfs');},prompt:'Fill the packing stations',where:'below',run:function(){S.stn=true;S.v='day';render();},
 after:function(){var a=STN[0],b=STN[1];return['Stations filled by bag size',a.id+' packs '+a.n+' bags of '+a.sz+' ('+pct(a)+'% of its shift). '+b.id+' packs '+b.n+' bags of '+b.sz+' ('+pct(b)+'%).'];}},
{id:'rush',target:function(){return $('kpf');},prompt:'Pull rush order R-2055 forward',where:'above',run:function(){S.rush=true;S.v='day';render();},
 after:function(){var q=queue(),a=base(),m=moved();return['A rush order shows what moves',RUSH.b+' takes the '+hm(slotOf(q,RUSH.b))+' slot. '+m.map(function(b){return b+' moves from '+hm(slotOf(a,b))+' to '+hm(slotOf(q,b));}).join(' and ')+', one slot each.'];}}];
'''
