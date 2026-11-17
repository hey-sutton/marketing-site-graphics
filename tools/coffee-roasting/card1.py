"""Coffee roasting card 1: Roast Planning & Scheduling.
Layout: board. A day strip and a Day, Week, Month toggle on top, an order tray on the left, the roast day board with four
stage columns (Pick, Roast, Rest, Pack) in the middle, and packing stations plus a rush panel along the bottom.
Drop a wholesale order on Thursday and it becomes three roast batches; switch views over the same schedule; fill the
packing stations by bag size; pull a rush order forward and read which batches move. Every number is computed."""
from frame_auto import header

SUMMARY = 'Roast Planning & Scheduling (open a roast day board, drop a wholesale order to create roast batches, switch day, week and month views, fill packing stations by bag size, pull a rush order forward)'
ARIA = 'Interactive product screen: Thursday November 19 roast board; order SO-5120 becomes three roast batches, the week and month views show the same stage counts, packing stations fill by bag size, and a rush order moves two later batches by one slot'
STEPS = 5
STUDIO = dict(lede='A typical roast day board, built on your Sutton data with Studio. Want it different? Describe the change.',
              examples=['Add a second roaster', 'Plan by green lot on hand', 'Set rest time by roast level', 'Block packing until rest ends'],
              built_on='Orders, roast batches, BOMs and stations', change='Stages, slots and columns')

ICON = '<rect x="2" y="3" width="12" height="10.5" rx="1.5"/><path d="M5.5 3v10.5M9 3v10.5M12.5 6.5"/>'

CSS = (
 '.q1{padding:10px 40px 0 16px;display:flex;flex-direction:column;gap:10px}'
 '.qtb{height:42px;flex:none;display:flex;align-items:center;gap:5px;padding:0 10px}.qtb .qlb{font-size:10px;font-weight:600;margin-right:4px;white-space:nowrap}'
 '.qdc{font:inherit;font-size:9.4px;padding:5px 8px;border:1px solid #E4E4E7;border-radius:6px;background:#fff;color:#52525B;cursor:pointer;white-space:nowrap}.qdc.on{background:#18181B;border-color:#18181B;color:#fff}.qdc.fakehover:not(.on){background:#F4F4F5}'
 '.qvs{display:inline-flex;gap:2px;padding:2px;border:1px solid #E4E4E7;border-radius:7px;background:#FAFAFA}.qvs button{font:inherit;font-size:9.4px;padding:4px 9px;border:0;border-radius:5px;background:transparent;color:#52525B;cursor:pointer}.qvs button.on{background:#fff;color:#18181B;font-weight:600;box-shadow:0 0 0 1px #E4E4E7}.qvs button:disabled{color:#C4C4C8;cursor:default}.qvs button.fakehover{background:#F4F4F5}'
 '.qdc:focus-visible,.qvs button:focus-visible,.qoc:focus-visible{outline:2px solid #18181B;outline-offset:2px}'
 '.qm{display:grid;grid-template-columns:128px 522px;gap:10px;height:318px;flex:none}'
 '.qtr{display:flex;flex-direction:column}.qtr .ct{height:28px}.qtl{padding:7px;display:flex;flex-direction:column;gap:7px}'
 '.qoc{font:inherit;text-align:left;border:1px dashed #A1A1AA;border-radius:7px;background:#fff;padding:7px 8px;display:flex;flex-direction:column;gap:2px;cursor:grab;font-size:9px;line-height:1.35;color:#3F3F46}'
 '.qoc b{font-family:"JetBrains Mono",ui-monospace,monospace;font-size:9.4px;color:#18181B}.qoc.qdone{border-style:solid;border-color:#BBF7D0;background:#F0FDF4;cursor:default}.qoc.qrush{border-color:#F87171}.qoc.fakehover{background:#FAFAFA}'
 '.qtr .qhint{margin-top:auto;padding:7px 8px;font-size:8.6px;color:#71717A;border-top:1px solid #F0F0F1;line-height:1.35}'
 '.qbd{position:relative;overflow:hidden}.qbd .empt{margin:10px;height:calc(100% - 20px)}.qbd.qdrop{box-shadow:0 0 0 2px #FFB92B}'
 '.qcols{display:grid;grid-template-columns:repeat(4,1fr);height:100%}.qcol{border-right:1px solid #F0F0F1;display:flex;flex-direction:column;min-width:0}.qcol:last-child{border-right:0}'
 '.qch{height:28px;flex:none;display:flex;align-items:center;justify-content:space-between;padding:0 8px;border-bottom:1px solid #E4E4E7;font-size:10px;font-weight:600}.qch .qn{font-family:"JetBrains Mono",ui-monospace,monospace;font-size:9px;padding:1px 6px;border-radius:999px;background:#F4F4F5;color:#3F3F46}'
 '.qcb{padding:5px;display:flex;flex-direction:column;gap:4px}'
 '.qit{height:34px;flex:none;border:1px solid #E4E4E7;border-radius:6px;background:#fff;padding:3px 6px;display:flex;flex-direction:column;justify-content:center;font-size:8.4px;line-height:1.3;color:#52525B;white-space:nowrap;overflow:hidden;transition:background-color .4s,border-color .4s}'
 '.qit b{font-family:"JetBrains Mono",ui-monospace,monospace;font-size:8.8px;color:#18181B;font-weight:600}.qit.qnew{background:#FFFBEB;border-color:#FCD34D}.qit.qmv{background:#FEF2F2;border-color:#FCA5A5}.qit.qrs{background:#E8EEFC;border-color:#A5B4FC}'
 '.qwk{width:100%;border-collapse:collapse;font-size:9.6px}.qwk th,.qwk td{height:34px;border-bottom:1px solid #F0F0F1;text-align:center}.qwk th{font-size:9px;color:#71717A;font-weight:500;height:30px}.qwk td:first-child,.qwk th:first-child{text-align:left;padding-left:12px;font-weight:600;color:#18181B}'
 '.qwk td{font-family:"JetBrains Mono",ui-monospace,monospace}.qwk .qsel{background:#FFFBEB;font-weight:700}'
 '.qmo{display:grid;grid-template-columns:repeat(5,1fr);gap:4px;padding:6px 8px}.qmo .qdh{font-size:8.6px;color:#71717A;text-align:center;height:14px}'
 '.qmc{height:44px;border:1px solid #F0F0F1;border-radius:5px;padding:3px 5px;font-size:8.2px;color:#52525B;display:flex;flex-direction:column;line-height:1.3}.qmc b{font-size:8.6px;color:#18181B}.qmc.qsel{border-color:#F59E0B;background:#FFFBEB}.qmc.qoff{visibility:hidden}'
 '.qsum{position:absolute;left:10px;right:10px;bottom:8px;padding:6px 9px;border-radius:6px;background:#F4F4F5;font-size:9.4px;color:#3F3F46}.qsum b{color:#18181B}'
 '.qbt{display:grid;grid-template-columns:320px 330px;gap:10px;height:162px;flex:none}.qbt .empt{margin:8px 10px;height:84px;padding:8px}.qs{display:flex;flex-direction:column}.qft9{margin-top:auto;padding:6px 11px;border-top:1px solid #F0F0F1;font-size:8.8px;color:#71717A}'
 '.qsts{padding:8px 11px 0;display:flex;flex-direction:column;gap:10px}.qs .qst1{display:flex;justify-content:space-between;font-size:9.8px}.qs .qst1 b{font-weight:600}.qs .qst1 span{font-family:"JetBrains Mono",ui-monospace,monospace;font-size:9.4px}'
 '.qsb{position:relative;height:9px;border-radius:5px;background:#F4F4F5;margin-top:5px;overflow:hidden}.qsb i{position:absolute;left:0;top:0;bottom:0;border-radius:5px;background:#52525B;transition:width .6s cubic-bezier(.22,.9,.28,1)}.qsb i.qr{background:#F59E0B}'
 '.qs small{display:block;font-size:8.6px;color:#71717A;margin-top:3px}'
 '.qmvb{padding:8px 11px 0;display:flex;flex-direction:column;gap:5px;font-size:9.4px}.qmvr{display:flex;align-items:center;gap:8px}.qmvr .mono{font-weight:600}.qmvr .qar{color:#A1A1AA}'
 '.qmvb .qnote{color:#71717A;font-size:9px}'
)

WIN = (
 header(ICON, 'Roast schedule', 'Roaster 1, week of November 16', '<span class="ch c-idle" id="qst">No day open</span>')
 + '<div class="q1"><div class="cd qtb"><span class="qlb">Roast day</span>'
 + ''.join('<button type="button" class="qdc" id="qd%d" data-d="%d">%s %d</button>' % (d, d, w, d) for w, d in (('Mon', 16), ('Tue', 17), ('Wed', 18), ('Thu', 19), ('Fri', 20)))
 + '<span class="grow"></span><span class="qvs" role="group" aria-label="Schedule view"><button type="button" id="qvD" class="on">Day</button><button type="button" id="qvW">Week</button><button type="button" id="qvM">Month</button></span></div>'
 '<div class="qm"><div class="cd qtr" id="qtr"></div><div class="cd qbd" id="qbd"></div></div>'
 '<div class="qbt"><div class="cd qs" id="qss"></div><div class="cd" id="qmv"></div></div></div>'
)

JS = r'''
var FOC='.hd>*,.qtb>*,.qtr,.qbd,.qs,#qmv';
var GPB=12000,SHRINK=14,OZ12=340194,LB5=2267960;
/* existing Thursday batches [id, slot, product, roasted grams]; pack jobs [customer, bags, size] */
var BASE=[['B-411',1,'Ethiopia Guji',12000],['B-412',2,'Colombia Huila',12000],['B-413',3,'Brazil Cerrado',10000]];
var JOBS=[['Cafe Juniper',24,'12'],['Northside Grocers',6,'5']];
var ORD={id:'SO-5120',cust:'Harbor Lane Cafe',n12:40,n5:8,prod:'House blend',first:4};
var RUSH={id:'SO-5131',cust:'Pinecrest Market',bid:'B-417',prod:'Brazil Cerrado',g:10000,n5:4,slot:5};
var CAP={'12':120,'5':30};
var WEEK={16:[4,2],17:[5,3],18:[3,2],20:[4,2]};
var S;
function kg(g){return (g/1000).toLocaleString('en-US',{minimumFractionDigits:3,maximumFractionDigits:3});}
function mgNeed(){return ORD.n12*OZ12+ORD.n5*LB5;}
function ordBatches(){var left=Math.round(mgNeed()/1000*1000)/1000,out=[],i=0;var g=mgNeed()/1000;while(g>0.0005){var b=Math.min(GPB,g);out.push(['B-'+(414+i),ORD.first+i,ORD.prod,b]);g-=b;i++;}return out;}
function batches(){var b=BASE.slice();if(S.ord)b=b.concat(ordBatches());if(S.rush){b=b.map(function(x){return x[1]>=RUSH.slot?[x[0],x[1]+1,x[2],x[3]]:x;});b.push([RUSH.bid,RUSH.slot,RUSH.prod,RUSH.g]);}return b.sort(function(a,c){return a[1]-c[1];});}
function jobs(){var j=JOBS.slice();if(S.ord){j.push([ORD.cust,ORD.n12,'12']);j.push([ORD.cust,ORD.n5,'5']);}if(S.rush)j.push([RUSH.cust,RUSH.n5,'5']);return j;}
function moved(){if(!S.rush)return [];var pre=BASE.concat(S.ord?ordBatches():[]);return pre.filter(function(x){return x[1]>=RUSH.slot;}).map(function(x){return [x[0],x[1],x[1]+1];});}
function tm(slot){return (6+slot)+':00';}
function ready(slot){var h=slot+19;return h>=24?'Fri '+(h-24)+':00':h+':00';}
function green(g){return Math.round(g*1000/(100-SHRINK)*100)/1000;}
function counts(d){if(d===19){var n=batches().length;return [n,n,n,jobs().length];}if(d===20){var f=WEEK[20][0]-(S.rush?1:0);return [f,f,f,WEEK[20][1]];}if(WEEK[d])return [WEEK[d][0],WEEK[d][0],WEEK[d][0],WEEK[d][1]];var b=3+(d*7)%4;return [b,b,b,2+d%2];}
function bags(sz){return jobs().filter(function(j){return j[2]===sz;}).reduce(function(s,j){return s+j[1];},0);}
function pct(n,c){return (Math.round(n*1000/c)/10).toFixed(1);}
var STG=['Pick','Roast','Rest','Pack'];
function sumLine(){var c=counts(19);return '<b>Thu Nov 19:</b> <span id="qsl">Pick '+c[0]+', Roast '+c[1]+', Rest '+c[2]+', Pack '+c[3]+'</span>';}
function render(){
['qvD','qvW','qvM'].forEach(function(id){var b=$(id);b.disabled=!S.day;b.classList.toggle('on',S.day&&{qvD:'day',qvW:'week',qvM:'month'}[id]===S.view);});
[16,17,18,19,20].forEach(function(d){$('qd'+d).classList.toggle('on',S.day===d);});
var t=$('qtr');t.innerHTML='<div class="ct"><span>To schedule</span></div><div class="qtl">'
+(S.ord?'<div class="qoc qdone"><b>'+ORD.id+'</b><span>'+ORD.cust+'</span><span>On Thu, 3 batches</span></div>':'<button type="button" class="qoc" id="qo1" draggable="true"><b>'+ORD.id+'</b><span>'+ORD.cust+', wholesale</span><span>'+ORD.n12+' × 12 oz, '+ORD.n5+' × 5 lb</span></button>')
+'<div class="qoc qrush'+(S.rush?' qdone':'')+'"><b>'+RUSH.id+'</b><span>'+RUSH.cust+'</span><span>'+(S.rush?'Pulled to Thu '+tm(RUSH.slot):'Rush, planned Fri 7:00')+'</span></div></div><div class="qhint">Drag an order onto the board, or click it.</div>';
var b=$('qbd');
if(!S.day){b.innerHTML='<div class="empt"><b>No roast day open</b><span>Pick a day to see picking, roasting, resting and packing on one board.</span></div>';}
else if(S.view==='day'){var bs=batches(),js=jobs(),mv=moved().map(function(m){return m[0];}),nw=S.ord?ordBatches().map(function(x){return x[0];}):[];
function cls(x){return x[0]===RUSH.bid?' qrs':mv.indexOf(x[0])>=0?' qmv':nw.indexOf(x[0])>=0?' qnew':'';}
var col=[bs.map(function(x){return '<div class="qit'+cls(x)+'"><b>'+x[0]+'</b><span>'+kg(green(x[3]))+' kg green</span></div>';}),
bs.map(function(x){return '<div class="qit'+cls(x)+'" id="qr-'+x[0]+'"><b>'+x[0]+' '+tm(x[1])+'</b><span>'+x[2]+'</span></div>';}),
bs.map(function(x){return '<div class="qit'+cls(x)+'"><b>'+x[0]+' '+kg(x[3])+'</b><span>Ready '+ready(x[1])+'</span></div>';}),
js.map(function(j,i){var nn=(S.ord&&j[0]===ORD.cust)||(S.rush&&j[0]===RUSH.cust);return '<div class="qit'+(nn?' qnew':'')+'"><b>'+j[1]+' × '+(j[2]==='12'?'12 oz':'5 lb')+'</b><span>'+j[0]+'</span></div>';})];
var c=counts(19);
b.innerHTML='<div class="qcols">'+STG.map(function(s,i){return '<div class="qcol"><div class="qch"><span>'+s+'</span><span class="qn" id="qc'+i+'">'+c[i]+'</span></div><div class="qcb">'+col[i].join('')+'</div></div>';}).join('')+'</div>';}
else if(S.view==='week'){var days=[16,17,18,19,20];
b.innerHTML='<table class="qwk"><tr><th>Stage</th>'+days.map(function(d){return '<th class="'+(d===19?'qsel':'')+'">'+['Mon','Tue','Wed','Thu','Fri'][d-16]+' '+d+'</th>';}).join('')+'</tr>'
+STG.map(function(s,i){return '<tr><td>'+s+'</td>'+days.map(function(d){return '<td class="'+(d===19?'qsel':'')+'" id="qw'+i+'-'+d+'">'+counts(d)[i]+'</td>';}).join('')+'</tr>';}).join('')+'</table><div class="qsum" id="qsm">'+sumLine()+'</div>';}
else{var h='<div class="qmo">'+['Mon','Tue','Wed','Thu','Fri'].map(function(w){return '<div class="qdh">'+w+'</div>';}).join('');
[[2,3,4,5,6],[9,10,11,12,13],[16,17,18,19,20],[23,24,25,26,27],[30,0,0,0,0]].forEach(function(w){w.forEach(function(d){if(!d){h+='<div class="qmc qoff"></div>';return;}var c=counts(d);h+='<div class="qmc'+(d===19?' qsel':'')+'" id="qm'+d+'"><b>Nov '+d+'</b><span>'+c[1]+' roasts</span><span>'+c[3]+' packs</span></div>';});});
b.innerHTML=h+'</div><div class="qsum" id="qsm">'+sumLine()+'</div>';}
var s=$('qss'),qft='<div class="qft9">Daily capacity: 12 oz station 120 bags, 5 lb station 30 bags.</div>';
if(!S.st)s.innerHTML='<div class="ct"><span>Packing stations</span>'+(S.ord?'<button type="button" class="bt pri" id="qfs">Fill stations</button>':'')+'</div><div class="empt"><b>Stations not filled</b><span>Pack jobs go to the 12 oz or 5 lb station by bag size.</span></div>'+qft;
else s.innerHTML='<div class="ct"><span>Packing stations <span class="mut" style="font-weight:400">Thu Nov 19</span></span><span class="ch c-info">By bag size</span></div><div class="qsts">'
+[['12','12 oz station'],['5','5 lb station']].map(function(z){var n=bags(z[0]),c=CAP[z[0]];return '<div><div class="qst1"><b>'+z[1]+'</b><span id="qsv'+z[0]+'">'+n+' of '+c+' bags, '+pct(n,c)+'%</span></div><div class="qsb"><i class="'+(S.rush&&z[0]==='5'?'qr':'')+'" style="width:'+(n/c*100).toFixed(1)+'%"></i></div><small>'+jobs().filter(function(j){return j[2]===z[0];}).map(function(j){return j[0]+' '+j[1];}).join(', ')+'</small></div>';}).join('')+'</div>'+qft;
var m=$('qmv');
if(!S.rush)m.innerHTML='<div class="ct"><span>Rush order</span>'+(S.st?'<button type="button" class="bt pri" id="qpf">Pull forward</button>':'')+'</div><div class="empt"><b>'+RUSH.id+' planned Friday 7:00</b><span>Pull it forward to see which batches move before you confirm.</span></div>';
else{var mv2=moved();m.innerHTML='<div class="ct"><span>What moves</span><span class="ch '+(S.conf?'c-ok':'c-warn')+'" id="qmc">'+(S.conf?'Confirmed':mv2.length+' batches move one slot')+'</span></div><div class="qmvb"><div class="qmvr"><span class="mono">'+RUSH.bid+'</span><span>Fri 7:00</span><span class="qar">to</span><span class="mono">Thu '+tm(RUSH.slot)+'</span></div>'
+mv2.map(function(x){return '<div class="qmvr" id="qmv-'+x[0]+'"><span class="mono">'+x[0]+'</span><span>'+tm(x[1])+'</span><span class="qar">to</span><span class="mono">'+tm(x[2])+'</span></div>';}).join('')
+'<div class="qmvr">'+(S.conf?'<span class="qnote">Board published to the roast floor.</span>':'<button type="button" class="bt" id="qcf">Confirm</button><span class="qnote">Nothing moves until you confirm.</span>')+'</div></div>';}
var st=$('qst');st.textContent=S.rush?'Rush pulled forward':S.ord?'Thu, 6 batches':S.day?'Thu Nov 19':'No day open';st.className='ch '+(S.rush?'c-warn':S.day?'c-info':'c-idle');}
function setView(v){if(!S.day)return;S.view=v;render();}
winEl.addEventListener('click',function(e){var t=e.target.closest&&e.target.closest('#qvD,#qvW,#qvM,#qcf');if(!t||mode==='watch')return;
if(t.id==='qcf'){if(S.rush){S.conf=true;render();}return;}setView({qvD:'day',qvW:'week',qvM:'month'}[t.id]);});
winEl.addEventListener('dragstart',function(e){var t=e.target.closest&&e.target.closest('#qo1');if(t&&e.dataTransfer)e.dataTransfer.setData('text/plain',ORD.id);});
winEl.addEventListener('dragover',function(e){if(e.target.closest&&e.target.closest('#qbd')&&S.day&&!S.ord){e.preventDefault();$('qbd').classList.add('qdrop');}});
winEl.addEventListener('dragleave',function(e){if(e.target.closest&&e.target.closest('#qbd'))$('qbd').classList.remove('qdrop');});
winEl.addEventListener('drop',function(e){var b=e.target.closest&&e.target.closest('#qbd');if(!b)return;e.preventDefault();b.classList.remove('qdrop');if(mode==='try'&&cur===1)doStep();});
function resetState(){S={day:null,view:'day',ord:false,st:false,rush:false,conf:false};render();}
var CAPAT=function(hh){return cur<=1?{l:150,t:300}:cur===2?{l:150,t:96}:{l:150,t:300};};
var ST=[
{id:'day',target:function(){return $('qd19');},prompt:'Open Thursday, November 19',where:'below',run:function(){S.day=19;S.view='day';render();},
 after:function(){var c=counts(19);return['Open the roast day board','Thursday November 19: '+c[1]+' batches to pick, roast and rest, '+c[3]+' packing jobs.'];}},
{id:'ord',target:function(){return $('qo1');},prompt:'Drag SO-5120 onto the board, or click it',where:'right',run:function(){S.ord=true;S.view='day';render();},
 after:function(){var o=ordBatches();return['Drop a wholesale order on the day',ORD.id+' needs '+kg(mgNeed()/1000)+' kg roasted: '+o.length+' batches of '+o.map(function(x){return kg(x[3]);}).join(', ')+' kg.'];}},
{id:'view',target:function(){return $('qvW');},prompt:'Switch to the week view',where:'below',run:function(quick){S.view='week';render();if(mode==='watch'&&!quick)later(function(){if(S.view==='week'){S.view='month';render();}},1500);},
 after:function(){var c=counts(19);return['Switch between day, week and month','Thursday reads Pick '+c[0]+', Roast '+c[1]+', Rest '+c[2]+', Pack '+c[3]+' in every view.'];}},
{id:'st',target:function(){return $('qfs');},prompt:'Click Fill stations',where:'above',run:function(){S.st=true;S.view='day';render();},
 after:function(){return['See packing stations filled by bag size','12 oz station '+bags('12')+' of '+CAP['12']+' bags, '+pct(bags('12'),CAP['12'])+'%. 5 lb station '+bags('5')+' of '+CAP['5']+', '+pct(bags('5'),CAP['5'])+'%.'];}},
{id:'rush',target:function(){return $('qpf');},prompt:'Pull the rush order forward',where:'above',run:function(){S.rush=true;S.view='day';render();},
 after:function(){var m=moved();return['Pull a rush order forward and read what moves',RUSH.id+' roasts Thursday '+tm(RUSH.slot)+'. '+m.map(function(x){return x[0]+' moves to '+tm(x[2]);}).join(' and ')+', one slot each.'];}}];
'''
