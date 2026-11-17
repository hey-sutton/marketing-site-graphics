"""Food co-packing card 2: Run Scheduling & Changeovers.
Layout: board. A week strip, a day timeline for Line 2 with run blocks and cleaning gaps, a run order table you can move
runs in, a totals panel and a run sheet.
Runs are ordered by allergen group and the cleaning time between them comes from a changeover matrix. Moving a run changes
the cleaning time and the end of day before you commit; a rush run shows what it displaces. Every number is computed."""
from frame_auto import header

SUMMARY = 'Run Scheduling & Changeovers (open a line day, see allergen groups, reorder runs and read the cleaning time saved, add a rush run and see what it displaces, print the run sheet)'
ARIA = 'Interactive product screen: Line 2 on Wednesday November 18 with runs for four brands; swapping two runs cuts cleaning from 130 to 95 minutes, a rush peanut run moves the granola run to Thursday, and the run sheet prints'
STEPS = 5
STUDIO = dict(lede='A typical line schedule, built on your Sutton data with Studio. Want it different? Describe the change.',
              examples=['Suggest the order with least cleaning', 'Add a second line', 'Show crew per run', 'Block a run until stock arrives'],
              built_on='Runs, allergen groups, lines and BOMs', change='Groups, cleaning times and columns')

ICON = '<rect x="2" y="3" width="12" height="10.5" rx="1.5"/><path d="M2 6.5h12M5.5 2v2.5M10.5 2v2.5M4.5 9h3M8.5 11h3"/>'

CSS = (
 '.c2{padding:10px 40px 0 16px;display:flex;flex-direction:column;gap:10px}'
 '.wk{height:40px;flex:none;display:flex;align-items:center;gap:6px;padding:0 10px}.wk .lb{font-size:10px;font-weight:600;margin-right:6px;white-space:nowrap}'
 '.dy{font:inherit;font-size:9.6px;padding:5px 10px;border:1px solid #E4E4E7;border-radius:6px;background:#fff;color:#52525B;cursor:pointer;white-space:nowrap}.dy.on{background:#18181B;border-color:#18181B;color:#fff}.dy.fakehover:not(.on){background:#F4F4F5}.dy:focus-visible{outline:2px solid #18181B;outline-offset:2px}'
 '.tl2{height:160px;flex:none}.tl2 .empt{margin:8px 10px;height:110px;padding:8px}'
 '.ax{position:relative;height:18px;margin:6px 11px 0;font-size:8.4px;color:#A1A1AA}.ax span{position:absolute;top:0;transform:translateX(-50%);font-family:"JetBrains Mono",ui-monospace,monospace}.ax span:first-child{transform:none}.ax span:last-child{transform:translateX(-100%)}'
 '.ln{position:relative;height:58px;margin:0 11px;border-radius:7px;background:repeating-linear-gradient(90deg,#FAFAFA 0 62px,#F4F4F5 62px 63px)}'
 '.bk{position:absolute;top:6px;bottom:6px;border-radius:6px;background:#E4E4E7;border:1px solid #D4D4D8;padding:4px 5px;display:flex;flex-direction:column;justify-content:center;overflow:hidden;font-size:8.4px;line-height:1.25;white-space:nowrap;transition:left .5s cubic-bezier(.22,.9,.28,1),width .5s}'
 '.bk b{font-family:"JetBrains Mono",ui-monospace,monospace;font-size:8.6px}.bk.g-GF{background:#DCFCE7;border-color:#86EFAC}.bk.g-PN{background:#FEF3C7;border-color:#FCD34D}.bk.g-TN{background:#E8EEFC;border-color:#A5B4FC}.bk.rush{box-shadow:0 0 0 2px #F87171}'
 '.co{position:absolute;top:14px;bottom:14px;border-radius:4px;background:repeating-linear-gradient(135deg,#FECACA 0 3px,#fff 3px 6px);display:grid;place-items:center;font-size:7.8px;font-family:"JetBrains Mono",ui-monospace,monospace;color:#991B1B;transition:left .5s cubic-bezier(.22,.9,.28,1),width .5s}'
 '.lgd2{display:flex;gap:12px;padding:8px 11px 0;font-size:8.8px;color:#52525B}.lgd2 span{display:inline-flex;align-items:center;gap:5px}.lgd2 i{width:12px;height:8px;border-radius:2px;display:inline-block}'
 '.c2m{display:grid;grid-template-columns:384px 266px;gap:10px;height:300px;flex:none}.c2r{display:flex;flex-direction:column;gap:8px;min-width:0}'
 '.ro .empt,.dtt .empt,.rs .empt{margin:8px 10px;height:calc(100% - 46px);padding:8px}'
 '.ro .row{grid-template-columns:20px 1fr 70px 46px 60px;min-height:40px;padding:0 10px;font-size:9.4px;gap:7px}.ro .row.h{min-height:22px}.ro .row .mono{font-size:9.2px}'
 '.ro .rn{display:flex;flex-direction:column;gap:1px;min-width:0}.ro .rn b{font-weight:600;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}.ro .rn small{font-size:8.6px;color:#71717A;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}'
 '.ro .bt{font-size:8.8px;padding:3px 6px}.ro .row.mv{background:#FFFBEB}.ro .row.rush{background:#FEF2F2}.ro .ft{padding:6px 10px;font-size:8.8px;color:#71717A;border-top:1px solid #F0F0F1}'
 '.dtt{height:176px;flex:none}.tg{display:grid;grid-template-columns:1fr 1fr;gap:8px;padding:8px 11px}.tg .kv small{font-size:8.6px}.tg .kv b{font-family:"JetBrains Mono",ui-monospace,monospace;font-size:13px}.tg .kv b.gd{color:#166534}'
 '.tnote{margin:0 11px;padding:5px 8px;border-radius:6px;background:#FEF2F2;border:1px solid #FECACA;font-size:8.8px;color:#7F1D1D;line-height:1.35}'
 '.rs{flex:1 1 auto}.rsl{padding:6px 11px 0;font-size:8.8px;font-family:"JetBrains Mono",ui-monospace,monospace;color:#3F3F46;line-height:1.55}'
)

WIN = (
 header(ICON, 'Line schedule', 'Line 2, runs by brand and allergen group', '<span class="ch c-idle" id="wst">No day open</span>')
 + '<div class="c2"><div class="cd wk" id="wk"><span class="lb">Line 2, week of Nov 16</span>'
 + ''.join('<button type="button" class="dy" id="dy%d">%s</button>' % (i, d) for i, d in enumerate(['Mon 16', 'Tue 17', 'Wed 18', 'Thu 19', 'Fri 20']))
 + '</div><div class="cd tl2" id="tl2"></div><div class="c2m"><div class="cd ro" id="ro"></div><div class="c2r"><div class="cd dtt" id="tt"></div><div class="cd rs" id="rs"></div></div></div></div>'
)

JS = r'''
var FOC='.hd>*,.wk>*,.tl2,.ro,.dtt,.rs';
var GRP={GF:['Gluten free','#86EFAC'],PN:['Peanut','#FCD34D'],TN:['Tree nut','#A5B4FC']};
/* cleaning minutes from one allergen group to the next; the same group needs a 15 minute line clean */
var CO={GFGF:15,PNPN:15,TNTN:15,GFPN:20,GFTN:20,PNGF:90,PNTN:60,TNGF:75,TNPN:45};
var RN={A:{id:'R-6101',b:'Brightfield Snacks',p:'Puffed rice bites',m:120,g:'GF'},B:{id:'R-6102',b:'Oakline Foods',p:'Peanut butter bars',m:150,g:'PN'},
D:{id:'R-6104',b:'Harborview Kitchen',p:'Rice crackers',m:100,g:'GF'},C:{id:'R-6103',b:'Kettlewood Brands',p:'Granola clusters',m:90,g:'TN'},X:{id:'R-6109',b:'Oakline Foods',p:'Peanut butter bites',m:60,g:'PN',rush:1}};
var START=360,END=960,PX=630/600,INIT=['A','B','D','C'];
var S;
function hm(t){var h=Math.floor(t/60),m=t%60;return (h<10?'0':'')+h+':'+(m<10?'0':'')+m;}
function cos(o){var s=0;for(var i=1;i<o.length;i++)s+=CO[RN[o[i-1]].g+RN[o[i]].g];return s;}
function runM(o){return o.reduce(function(s,k){return s+RN[k].m;},0);}
function endOf(o){return START+runM(o)+cos(o);}
function plan(o){var t=START,out=[];o.forEach(function(k,i){if(i){var c=CO[RN[o[i-1]].g+RN[k].g];out.push({co:1,s:t,m:c});t+=c;}out.push({k:k,s:t,m:RN[k].m});t+=RN[k].m;});return out;}
/* a rush run goes after the last run of its own group (cheapest clean); runs that no longer fit by END move to the next day */
function addRush(o){var g=RN.X.g,at=o.length;for(var i=o.length-1;i>=0;i--){if(RN[o[i]].g===g){at=i+1;break;}}var n=o.slice(0,at).concat(['X'],o.slice(at)),moved=[];while(endOf(n)>END&&n.length){var last=n[n.length-1];if(last==='X')break;moved.unshift(last);n.pop();}return {o:n,moved:moved,would:endOf(o.slice(0,at).concat(['X'],o.slice(at)))};}
function render(){
[].forEach.call($('wk').querySelectorAll('.dy'),function(b,i){b.classList.toggle('on',S.day&&i===2);});
var T=$('tl2');
if(!S.day)T.innerHTML='<div class="ct"><span>Day timeline</span></div><div class="empt"><b>No day open</b><span>Pick a day to see the runs on Line 2, with cleaning between them.</span></div>';
else{var ax='';for(var h=6;h<=16;h+=2)ax+='<span style="left:'+((h*60-START)*PX).toFixed(1)+'px">'+(h<10?'0':'')+h+':00</span>';
var bl=plan(S.o).map(function(x){var l=((x.s-START)*PX).toFixed(1),w=(x.m*PX).toFixed(1);if(x.co)return '<span class="co" style="left:'+l+'px;width:'+w+'px">'+x.m+'</span>';var r=RN[x.k];return '<span class="bk'+(S.grp?' g-'+r.g:'')+(r.rush?' rush':'')+'" style="left:'+l+'px;width:'+w+'px" id="bk'+x.k+'"><b>'+r.id+'</b><span>'+r.m+' min</span></span>';}).join('');
T.innerHTML='<div class="ct"><span>Wednesday Nov 18 <span class="mut" style="font-weight:400">06:00 to 16:00</span></span>'+(S.grp?'<span class="ch c-info">Allergen groups on</span>':'<button type="button" class="bt pri" id="wgr">Show allergen groups</button>')+'</div><div class="ax">'+ax+'</div><div class="ln">'+bl+'</div>'
+(S.grp?'<div class="lgd2">'+Object.keys(GRP).map(function(g){return '<span><i style="background:'+GRP[g][1]+'"></i>'+GRP[g][0]+'</span>';}).join('')+'<span><i style="background:repeating-linear-gradient(135deg,#FECACA 0 3px,#fff 3px 6px)"></i>Cleaning, minutes</span></div>':'<div class="lgd2"><span>Cleaning gaps in minutes between runs</span></div>');}
var R=$('ro');
if(!S.day)R.innerHTML='<div class="ct"><span>Run order</span></div><div class="empt"><b>No runs yet</b><span>Runs for each brand, in the order they go on the line.</span></div>';
else{R.innerHTML='<div class="ct"><span>Run order</span>'+(S.grp&&!S.rush?'<button type="button" class="bt'+(S.mv?' pri':'')+'" id="wrs">Add rush run</button>':S.rush?'<span class="ch c-bad">Rush added</span>':'')+'</div><div class="row h"><span>#</span><span>Run</span><span>Group</span><span>Min</span><span></span></div>'
+S.o.map(function(k,i){var r=RN[k];return '<div class="row'+(S.mv&&k==='D'?' mv':'')+(r.rush?' rush':'')+'"><span class="mono">'+(i+1)+'</span><span class="rn"><b>'+r.b+'</b><small>'+r.id+', '+r.p+'</small></span><span>'+(S.grp?'<span class="ch" style="background:'+GRP[r.g][1]+'33;color:#3F3F46" id="gc'+k+'">'+GRP[r.g][0]+'</span>':'<span class="mut">Hidden</span>')+'</span><span class="mono">'+r.m+'</span><span>'+(i?'<button type="button" class="bt" id="up'+k+'">Move up</button>':'')+'</span></div>';}).join('')
+'<div class="ft">'+(S.moved.length?S.moved.map(function(k){return RN[k].id+' '+RN[k].p.toLowerCase();}).join(', ')+' moved to Thu 19, first on Line 2':'Line hours 06:00 to 16:00, 600 minutes')+'</div>';}
var U=$('tt');
if(!S.day)U.innerHTML='<div class="ct"><span>Day totals</span></div><div class="empt"><b>No totals yet</b><span>Cleaning minutes and the end of day show before you commit a change.</span></div>';
else{var now=cos(S.o);U.innerHTML='<div class="ct"><span>Day totals</span><span class="ch '+(S.rush?'c-warn':S.mv?'c-ok':'c-idle')+'">'+(S.rush?'Rush planned':S.mv?'Change ready':'As planned')+'</span></div><div class="tg">'
+'<span class="kv"><small>Cleaning before</small><b id="tb">'+cos(INIT)+' min</b></span><span class="kv"><small>Cleaning now</small><b id="tn">'+now+' min</b></span>'
+'<span class="kv"><small>Saved by reorder</small><b class="gd" id="tsv">'+S.saved+' min</b></span><span class="kv"><small>End of day</small><b id="te">'+hm(endOf(S.o))+'</b></span></div>'
+(S.rush?'<div class="tnote" id="tdn">With the rush run the day would end at '+hm(S.would)+'. '+S.moved.map(function(k){return RN[k].p;}).join(', ')+' moves to Thursday.</div>':'');}
var P=$('rs');
if(!S.print)P.innerHTML='<div class="ct"><span>Run sheet</span>'+(S.rush?'<button type="button" class="bt pri" id="wpr">Print run sheet</button>':'')+'</div><div class="empt"><b>Not printed</b><span>Times, cleaning and BOM for each run.</span></div>';
else P.innerHTML='<div class="ct"><span>Run sheet, Line 2</span><span class="ch c-ok" id="wps">Sent to printer</span></div><div class="rsl" id="rsl">'+plan(S.o).filter(function(x){return !x.co;}).map(function(x){return hm(x.s)+' to '+hm(x.s+x.m)+'  '+RN[x.k].id;}).join('<br>')+'</div>';
var st=$('wst');st.textContent=S.print?'Run sheet printed':S.rush?'Rush run added':S.mv?'Order changed':S.day?'Wed 18, '+S.o.length+' runs':'No day open';st.className='ch '+(S.day?'c-info':'c-idle');}
function moveUp(k){var i=S.o.indexOf(k);if(i<1)return;var o=S.o.slice(),b=cos(S.o);o[i]=o[i-1];o[i-1]=k;S.o=o;S.mv=true;S.saved+=b-cos(o);render();}
winEl.addEventListener('click',function(e){var t=e.target.closest&&e.target.closest('[id^="up"]');if(!t||mode!=='done')return;moveUp(t.id.slice(2));});
function resetState(){S={day:false,grp:false,mv:false,rush:false,print:false,o:INIT.slice(),moved:[],would:0,saved:0};render();}
var CAPAT=function(hh){return cur<=1?{l:14,t:visH()-hh-14}:{l:410,t:60};};
var ST=[
{id:'day',target:function(){return $('dy2');},prompt:'Open Wednesday Nov 18',where:'below',run:function(){S.day=true;render();},
 after:function(){return['Open the day for Line 2','Wednesday Nov 18: '+S.o.length+' runs for '+S.o.length+' brands, '+runM(S.o)+' minutes of running and '+cos(S.o)+' of cleaning, done at '+hm(endOf(S.o))+'.'];}},
{id:'grp',target:function(){return $('wgr');},prompt:'Click Show allergen groups',where:'below',run:function(){S.grp=true;render();},
 after:function(){return['Every run shows its allergen group','Gluten free, peanut and tree nut. Going from peanut back to gluten free needs a '+CO.PNGF+' minute full wash.'];}},
{id:'mv',target:function(){return $('upD');},prompt:'Move the rice crackers run up',where:'below',run:function(){moveUp('D');},
 after:function(){var n=cos(S.o);return['Reorder runs and read the cleaning saved','Rice crackers move ahead of the peanut bars: cleaning drops from '+cos(INIT)+' to '+n+' minutes, '+(cos(INIT)-n)+' saved, done at '+hm(endOf(S.o))+'.'];}},
{id:'rush',target:function(){return $('wrs');},prompt:'Click Add rush run',where:'above',run:function(){var r=addRush(S.o);S.o=r.o;S.moved=r.moved;S.would=r.would;S.rush=true;render();},
 after:function(){return['A rush run shows what it displaces',RN.X.id+' peanut butter bites goes after the peanut bars with a '+CO.PNPN+' minute clean. '+S.moved.map(function(k){return RN[k].p;}).join(', ')+' moves to Thursday.'];}},
{id:'print',target:function(){return $('wpr');},prompt:'Click Print run sheet',where:'above',run:function(){S.print=true;render();},
 after:function(){return['Print the run sheet for the line',S.o.length+' runs from '+hm(START)+' to '+hm(endOf(S.o))+' with '+cos(S.o)+' minutes of cleaning, sent to the Line 2 printer.'];}}];
'''
