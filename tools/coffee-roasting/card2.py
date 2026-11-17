"""Coffee roasting card 2: Green Lots & Roast Yield.
Layout: record form with a side summary panel. The green lot record and a roast batch form on the left, a summary panel
on the right with the lot balance, shrink by origin and roast level, and a trace back from the roasted lot.
Open a green lot, log a 60.000 kg roast and watch the balance drop by exactly 60.000 kg, record 51.600 kg roasted out for
a 14.0% loss, compare shrink by origin and roast level, and trace the roasted lot back. Every number is computed in grams."""
from frame_auto import header

SUMMARY = 'Green Lots & Roast Yield (open a green coffee lot, log a roast batch and watch the lot balance drop, record roasted weight and read the roast loss, compare shrink by origin and roast level, trace a roasted lot back)'
ARIA = 'Interactive product screen: green lot GL-2207 Ethiopia Yirgacheffe with 840.000 kg on hand; a 60.000 kg roast drops it to 780.000 kg, 51.600 kg roasted out is a 14.0% loss, shrink is compared by origin and roast level, and roasted lot RL-1119-4 traces back to the green lot'
STEPS = 5
STUDIO = dict(lede='A typical green lot and roast log, built on your Sutton data with Studio. Want it different? Describe the change.',
              examples=['Alert when shrink runs high', 'Add moisture at receiving', 'Log roast profile and charge temp', 'Split a lot by warehouse'],
              built_on='Green lots, roast batches and suppliers', change='Fields, levels and alerts')

ICON = '<path d="M8 2.2c3 1.6 3 10 0 11.6M8 2.2C4.6 3.4 3.3 6 3.3 8s1.3 4.6 4.7 5.8M8 2.2c3.4 1.2 4.7 3.8 4.7 5.8S11.4 12.6 8 13.8"/>'

CSS = (
 '.q2{padding:10px 40px 0 16px;display:grid;grid-template-columns:420px 230px;gap:10px}'
 '.q2l{display:flex;flex-direction:column;gap:10px;min-width:0}.q2r{display:flex;flex-direction:column;gap:10px;min-width:0}'
 '.qlf{height:150px;flex:none}.qrow{display:flex;align-items:center;gap:7px;padding:8px 11px 4px;position:relative}.qrow .fld{flex-direction:row;align-items:center;gap:6px;position:relative}.qrow .fld small{font-size:9.6px;color:#18181B;font-weight:600;white-space:nowrap}'
 '.qrow .fld .em{position:absolute;left:0;top:28px;white-space:nowrap;background:#fff;padding:1px 4px;z-index:3}'
 '#qli{width:118px;font-size:10.2px;padding:5px 7px}.qsmp{display:inline-flex;align-items:center;gap:5px;font-size:9px;color:#71717A}.qsmp .bt{font-family:"JetBrains Mono",ui-monospace,monospace;font-size:9.4px;padding:4px 7px}'
 '.qg{display:grid;grid-template-columns:repeat(3,1fr);gap:0;padding:4px 11px 0}.qg .kv{padding:6px 0;border-top:1px solid #F4F4F5}.qg .kv b{font-size:10.2px}.qg .kv b.mono{font-size:10px}'
 '.qlf .qem{margin:6px 11px;padding:14px;border:1px dashed #E4E4E7;border-radius:7px;background:#FAFAFA;text-align:center;font-size:9.6px;color:#71717A}'
 '.qrb{height:160px;flex:none}.qrb .qbox{padding:8px 11px 0;display:grid;grid-template-columns:1fr 1fr;gap:8px 14px}'
 '.qrb .fld input{font-size:10.2px;padding:5px 7px;text-align:right}.qrb .fld input:disabled{background:#FAFAFA;color:#A1A1AA}.qrb .qfr{display:flex;align-items:flex-end;gap:6px}.qrb .qfr .fld{flex:1}'
 '.qlv{display:inline-flex;gap:2px;padding:2px;border:1px solid #E4E4E7;border-radius:6px;background:#FAFAFA}.qlv button{font:inherit;font-size:9.2px;padding:3px 8px;border:0;border-radius:4px;background:transparent;color:#52525B;cursor:pointer}.qlv button.on{background:#fff;color:#18181B;font-weight:600;box-shadow:0 0 0 1px #E4E4E7}'
 '.qres{grid-column:1/-1;display:flex;gap:16px;padding-top:6px;border-top:1px solid #F4F4F5;font-size:9.4px;color:#52525B;min-height:26px;align-items:center}.qres b{font-family:"JetBrains Mono",ui-monospace,monospace;color:#18181B}.qres .qbig{font-size:15px}'
 '.qhist{height:200px;flex:none;display:flex;flex-direction:column}.qft9{margin-top:auto;padding:6px 11px;border-top:1px solid #F0F0F1;font-size:8.8px;color:#71717A}.qhist .row{grid-template-columns:76px 64px 72px 72px 1fr;min-height:23px;font-size:9.2px;gap:6px}.qhist .row>span:nth-child(n+3){text-align:right}.qhist .row.qnw{background:#FFFBEB}'
 '.qbal{height:118px;flex:none;padding:0}.qbal .qbv{padding:8px 11px 0}.qbal .big{font-family:"JetBrains Mono",ui-monospace,monospace;font-size:21px}.qbal small{display:block;font-size:9px;color:#71717A;margin-top:2px}.qbal .qdl{font-size:9.4px;color:#B91C1C;font-family:"JetBrains Mono",ui-monospace,monospace;margin-top:4px;min-height:13px}'
 '.qbar{height:7px;border-radius:4px;background:#F4F4F5;margin:6px 11px 0;overflow:hidden}.qbar i{display:block;height:100%;background:#52525B;transition:width .6s cubic-bezier(.22,.9,.28,1)}'
 '.qsh{height:178px;flex:none}.qsh .empt{margin:8px;height:120px;padding:8px}.qsh table{width:100%;border-collapse:collapse;font-size:9.2px;margin-top:4px}.qsh th{font-size:8.6px;color:#71717A;font-weight:500;height:20px}.qsh td{height:26px;text-align:center;font-family:"JetBrains Mono",ui-monospace,monospace;border-top:1px solid #F4F4F5}'
 '.qsh td:first-child,.qsh th:first-child{text-align:left;padding-left:10px;font-family:inherit}.qsh td.qhi{background:#FEF3C7;font-weight:700}.qsh td.qup{background:#FFFBEB;box-shadow:inset 0 0 0 1px #F59E0B}.qsh .qft{padding:4px 10px;font-size:8.6px;color:#71717A}'
 '.qtc{flex:1 1 auto;min-height:0}.qtc .empt{margin:8px;height:100px;padding:8px}.qtch{padding:7px 10px 0;display:flex;flex-direction:column;gap:0}'
 '.qtn{border:1px solid #E4E4E7;border-radius:6px;padding:4px 7px;font-size:8.8px;line-height:1.35;color:#52525B}.qtn b{font-family:"JetBrains Mono",ui-monospace,monospace;font-size:9.2px;color:#18181B}.qtn.qh{border-color:#F59E0B;background:#FFFBEB}'
 '.qtk{width:1px;height:9px;background:#D4D4D8;margin-left:14px}'
)

WIN = (
 header(ICON, 'Green lots', 'Roastery stock and roast yield', '<span class="ch c-idle" id="qst">No lot open</span>')
 + '<div class="q2"><div class="q2l">'
 '<div class="cd qlf"><div class="qrow frm" id="qfa"><label class="fld" id="qfl"><small>Green lot</small><input id="qli" value="" placeholder="Lot number" autocomplete="off" spellcheck="false" aria-label="Green lot number"><span class="em" id="qle">No lot found. Try GL-2207</span></label>'
 '<button type="button" class="bt pri" id="qop">Open</button><span class="qsmp">Sample<button type="button" class="bt" id="qsm" data-sample>GL-2207</button></span></div><div id="qlg"></div></div>'
 '<div class="cd qrb" id="qrb"><div class="ct"><span>Roast batch</span><span class="ch c-idle" id="qbc">Not started</span></div><div class="qbox">'
 '<div class="qfr frm" id="qfb"><label class="fld" id="qfg"><small>Green in, kg</small><input id="qgi" value="" inputmode="decimal" placeholder="0.000" autocomplete="off" aria-label="Green weight in, kg" disabled><span class="em" id="qge">Enter up to the lot balance</span></label><button type="button" class="bt pri" id="qlb">Log batch</button></div>'
 '<div class="qfr frm" id="qfc"><label class="fld" id="qfo"><small>Roasted out, kg</small><input id="qro" value="" inputmode="decimal" placeholder="0.000" autocomplete="off" aria-label="Roasted weight out, kg" disabled><span class="em" id="qoe">Enter less than the green in</span></label><button type="button" class="bt" id="qrc">Record</button></div>'
 '<div style="display:flex;align-items:center;gap:8px;font-size:9.4px;color:#52525B">Roast level<span class="qlv" role="group" aria-label="Roast level"><button type="button" id="qL" class="on">Light</button><button type="button" id="qM">Medium</button><button type="button" id="qD">Dark</button></span></div>'
 '<div></div><div class="qres" id="qres"></div></div></div>'
 '<div class="cd qhist" id="qhi"></div></div>'
 '<div class="q2r"><div class="cd qbal" id="qbl"></div><div class="cd qsh" id="qsh"></div><div class="cd qtc" id="qtc"></div></div></div>'
)

JS = r'''
var FOC='.hd>*,.qlf,.qrb,.qhist,.qbal,.qsh,.qtc';
/* green lots: id, origin, region, supplier, arrived, bag grams, received bags, on hand grams */
var LOTS=[{id:'GL-2207',o:'Ethiopia',reg:'Yirgacheffe',sup:'Highmark Green Imports',arr:'Oct 28, 2026',bag:60000,rcv:20,bal:840000},
{id:'GL-2211',o:'Colombia',reg:'Huila',sup:'Andes Bean Traders',arr:'Nov 2, 2026',bag:70000,rcv:25,bal:1190000},
{id:'GL-2214',o:'Brazil',reg:'Cerrado',sup:'Serra Verde Exports',arr:'Nov 6, 2026',bag:60000,rcv:30,bal:1500000}];
var LV=['Light','Medium','Dark'];
/* earlier roasts [origin, level, green in g, roasted out g] */
var HIST=[['Ethiopia',0,60000,52200],['Ethiopia',0,60000,51960],['Ethiopia',1,60000,51300],['Ethiopia',1,60000,51420],['Ethiopia',2,60000,50100],
['Colombia',0,70000,61180],['Colombia',0,70000,60900],['Colombia',1,70000,60480],['Colombia',1,70000,60200],['Colombia',2,70000,59080],
['Brazil',0,60000,52500],['Brazil',1,60000,51840],['Brazil',1,60000,51600],['Brazil',2,60000,50400],['Brazil',2,60000,50160]];
var LOTHIST=[['RB-1112-2','Light',60000,52200],['RB-1114-1','Medium',60000,51300],['RB-1117-3','Light',60000,51960]];
var NB={id:'RB-1119-4',rl:'RL-1119-4'};
var S;
function kg(g){return (g/1000).toLocaleString('en-US',{minimumFractionDigits:3,maximumFractionDigits:3});}
function lossPct(i,o){return (Math.round((i-o)*1000/i)/10).toFixed(1);}
function lot(){return LOTS[0];}
function bal(){return lot().bal-(S.log?S.gin:0);}
function rows(){var r=HIST.slice();if(S.out)r.push([lot().o,S.lv,S.gin,S.gout]);return r;}
function avg(o,l){var i=0,x=0;rows().forEach(function(h){if(h[0]===o&&h[1]===l){i+=h[2];x+=h[3];}});return i?lossPct(i,x):'';}
function maxCell(){var best=['',0];LOTS.forEach(function(x){[0,1,2].forEach(function(l){var v=parseFloat(avg(x.o,l));if(v>best[1])best=[x.o+' '+LV[l].toLowerCase(),v];});});return [best[0],best[1].toFixed(1)];}
function render(){var L=lot(),g=$('qlg');
g.innerHTML=S.open?'<div class="qg">'+[['Origin',L.o+', '+L.reg],['Supplier',L.sup],['Arrived',L.arr],['Bags received',L.rcv+' of '+kg(L.bag)+' kg'],['Bags on hand','<span id="qbg">'+(bal()/L.bag)+'</span>'],['On hand','<span class="mono" id="qoh">'+kg(bal())+' kg</span>']].map(function(k){return '<span class="kv"><small>'+k[0]+'</small><b>'+k[1]+'</b></span>';}).join('')+'</div>'
:'<div class="qem">Open a green lot to see its origin, supplier, arrival and bags on hand.</div>';
$('qgi').disabled=!S.open;$('qro').disabled=!S.log;
['qL','qM','qD'].forEach(function(id,i){$(id).classList.toggle('on',S.lv===i);});
var bc=$('qbc');bc.textContent=S.out?NB.id+' recorded':S.log?NB.id+' roasting':'Not started';bc.className='ch '+(S.out?'c-ok':S.log?'c-warn':'c-idle');
$('qres').innerHTML=S.out?'<span>Roast loss <b class="qbig" id="qloss">'+lossPct(S.gin,S.gout)+'%</b></span><span>Green in <b>'+kg(S.gin)+'</b></span><span>Roasted out <b id="qrol">'+kg(S.gout)+'</b></span><span>Lot <b>'+NB.rl+'</b></span>'
:S.log?'<span>Green in <b>'+kg(S.gin)+' kg</b> taken from '+L.id+'. Record the roasted weight when the batch drops.</span>':'<span class="mut">Log a batch against the open lot.</span>';
var h=$('qhi');if(!S.open)h.innerHTML='<div class="ct"><span>Roasts from this lot</span></div><div class="empt" style="margin:8px 10px;height:110px"><b>No lot open</b><span>Every roast batch from the lot is listed here.</span></div><div class="qft9">Weights come from the roaster scale, in kilograms.</div>';
else{var lr=LOTHIST.slice();if(S.log)lr.push([NB.id,LV[S.lv],S.gin,S.out?S.gout:null]);
h.innerHTML='<div class="ct"><span>Roasts from '+L.id+'</span><span class="ch c-idle">'+lr.length+' batches</span></div><div class="row h"><span>Batch</span><span>Level</span><span>Green in</span><span>Roasted</span><span style="text-align:right">Loss</span></div>'
+lr.map(function(r,i){return '<div class="row'+(r[0]===NB.id?' qnw':'')+'"><span class="mono">'+r[0]+'</span><span>'+r[1]+'</span><span class="mono">'+kg(r[2])+'</span><span class="mono">'+(r[3]===null?'roasting':kg(r[3]))+'</span><span class="mono">'+(r[3]===null?'':lossPct(r[2],r[3])+'%')+'</span></div>';}).join('')+'<div class="qft9">Weights come from the roaster scale, in kilograms.</div>';}
var b=$('qbl');b.innerHTML='<div class="ct"><span>Lot balance</span><span class="mut" style="font-weight:400">'+(S.open?L.id:'')+'</span></div><div class="qbv">'+(S.open?'<span class="big" id="qbal">'+kg(bal())+'</span> <span class="mut">kg</span><small>'+(bal()/L.bag)+' bags on hand of '+L.rcv+' received</small><div class="qdl" id="qdl">'+(S.log?'Down '+kg(L.bal-bal())+' kg on '+NB.id:'')+'</div>':'<small>No lot open</small>')+'</div>'+(S.open?'<div class="qbar"><i style="width:'+(bal()/(L.rcv*L.bag)*100).toFixed(1)+'%"></i></div>':'');
var s=$('qsh');if(!S.cmp)s.innerHTML='<div class="ct"><span>Shrink</span>'+(S.out?'<button type="button" class="bt pri" id="qcp">Compare</button>':'')+'</div><div class="empt"><b>Not compared yet</b><span>Average roast loss by origin and roast level.</span></div>';
else{var hi=null,hv=0;LOTS.forEach(function(x){[0,1,2].forEach(function(l){var v=parseFloat(avg(x.o,l));if(v>hv){hv=v;hi=x.o+l;}});});
s.innerHTML='<div class="ct"><span>Shrink by origin</span><span class="ch c-info">Avg loss</span></div><table><tr><th>Origin</th>'+LV.map(function(l){return '<th>'+l+'</th>';}).join('')+'</tr>'
+LOTS.map(function(x){return '<tr><td>'+x.o+'</td>'+[0,1,2].map(function(l){var up=x.o===L.o&&l===S.lv;return '<td id="qa-'+x.o+'-'+l+'" class="'+(hi===x.o+l?'qhi':up?'qup':'')+'">'+avg(x.o,l)+'%</td>';}).join('')+'</tr>';}).join('')+'</table><div class="qft">Outlined: includes '+NB.id+'. Shaded: highest loss.</div>';}
var t=$('qtc');if(!S.tr)t.innerHTML='<div class="ct"><span>Trace</span>'+(S.cmp?'<button type="button" class="bt pri" id="qtb">Trace back</button>':'')+'</div><div class="empt"><b>No trace</b><span>Follow a roasted lot back to its green lot.</span></div>';
else t.innerHTML='<div class="ct"><span>Trace back</span><span class="ch c-ok">1 green lot</span></div><div class="qtch"><div class="qtn qh"><b>'+NB.rl+'</b> '+kg(S.gout)+' kg roasted</div><div class="qtk"></div><div class="qtn"><b>'+NB.id+'</b> '+LV[S.lv].toLowerCase()+', Nov 19</div><div class="qtk"></div><div class="qtn" id="qtg"><b>'+L.id+'</b> '+kg(S.gin)+' kg, '+L.o+' '+L.reg+'</div><div class="qtk"></div><div class="qtn">'+L.sup+', '+L.arr+'</div></div>';
var st=$('qst');st.textContent=S.tr?NB.rl+' traced':S.open?L.id+' open':'No lot open';st.className='ch '+(S.open?'c-info':'c-idle');}
function num(id){var v=String($(id).value).replace(/,/g,'').trim();return /^\d+(\.\d{1,3})?$/.test(v)?Math.round(parseFloat(v)*1000):NaN;}
function typeIn(id,t,done){var i=0;(function k(){$(id).value=t.slice(0,i);if(i<t.length){i++;later(k,60);}else done();})();}
$('qsm').addEventListener('click',function(){$('qli').value='GL-2207';$('qfl').classList.remove('err');});
winEl.addEventListener('click',function(e){var t=e.target.closest&&e.target.closest('#qL,#qM,#qD');if(!t||mode==='watch'||S.out)return;S.lv={qL:0,qM:1,qD:2}[t.id];render();});
function resetState(){S={open:false,log:false,out:false,cmp:false,tr:false,lv:0,gin:0,gout:0};['qli','qgi','qro'].forEach(function(i){$(i).value='';});['qfl','qfg','qfo'].forEach(function(i){$(i).classList.remove('err');});render();}
var CAPAT=function(hh){return cur<=1?{l:14,t:visH()-hh-14}:{l:14,t:56};};
var ST=[
{id:'open',target:function(){return mode==='try'?$('qop'):$('qli');},prompt:'Type GL-2207 or pick the sample, then Open',where:'below',
 ok:function(){var v=String($('qli').value).trim().toUpperCase().replace(/\s/g,''),b=!(v==='GL-2207'||v==='GL2207');$('qle').textContent=v?'No lot found. Try GL-2207':'Enter a lot, for example GL-2207';$('qfl').classList.toggle('err',b);return !b;},
 run:function(quick){var go=function(){$('qli').value='GL-2207';$('qfl').classList.remove('err');S.open=true;$('qgi').value='60.000';render();};if(mode==='watch'&&!quick)typeIn('qli','GL-2207',go);else go();},
 after:function(){var L=lot();return['Open a green lot with origin, supplier and bags',L.id+', '+L.o+' '+L.reg+' from '+L.sup+', arrived '+L.arr+'. '+(L.bal/L.bag)+' bags, '+kg(L.bal)+' kg on hand.'];}},
{id:'log',target:function(){return mode==='try'?$('qlb'):$('qgi');},prompt:'Type 60 as green in, then Log batch',where:'below',
 ok:function(){var v=num('qgi'),b=!(v>0&&v<=lot().bal);$('qfg').classList.toggle('err',b);return !b;},
 run:function(quick){var go=function(){var v=mode==='watch'||!(num('qgi')>0)?60000:num('qgi');$('qgi').value=kg(v);$('qfg').classList.remove('err');S.gin=v;S.log=true;$('qro').value='51.600';render();};if(mode==='watch'&&!quick)typeIn('qgi','60',go);else{if(!$('qgi').value)$('qgi').value='60';go();}},
 after:function(){return['Log a roast batch and watch the lot balance drop',NB.id+' takes '+kg(S.gin)+' kg. '+lot().id+' drops from '+kg(lot().bal)+' to '+kg(bal())+' kg.'];}},
{id:'out',target:function(){return mode==='try'?$('qrc'):$('qro');},prompt:'Type 51.6 as roasted out, then Record',where:'below',
 ok:function(){var v=num('qro'),b=!(v>0&&v<S.gin);$('qfo').classList.toggle('err',b);return !b;},
 run:function(quick){var go=function(){var v=mode==='watch'||!(num('qro')>0)?51600:num('qro');$('qro').value=kg(v);$('qfo').classList.remove('err');S.gout=v;S.out=true;render();};if(mode==='watch'&&!quick)typeIn('qro','51.6',go);else{if(!$('qro').value)$('qro').value='51.6';go();}},
 after:function(){return['Record roasted weight and read the roast loss',kg(S.gin)+' kg in, '+kg(S.gout)+' kg out: '+kg(S.gin-S.gout)+' kg lost, '+lossPct(S.gin,S.gout)+'%.'];}},
{id:'cmp',target:function(){return $('qcp');},prompt:'Click Compare',where:'below',run:function(){S.cmp=true;render();},
 after:function(){var L=lot();return['Compare shrink across origins and roast levels',L.o+' '+LV[S.lv].toLowerCase()+' now averages '+avg(L.o,S.lv)+'%. Highest is '+maxCell()[0]+' at '+maxCell()[1]+'%.'];}},
{id:'tr',target:function(){return $('qtb');},prompt:'Click Trace back',where:'above',run:function(){S.tr=true;render();},
 after:function(){var L=lot();return['Trace a roasted lot back to its green lot',NB.rl+' came from '+kg(S.gin)+' kg of '+L.id+', '+L.o+' '+L.reg+', '+L.sup+'.'];}}];
'''
