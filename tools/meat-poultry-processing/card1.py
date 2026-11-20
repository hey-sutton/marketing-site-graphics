"""Meat and poultry card 1: Yield Loss by Stage. Layout: a stage chain (a flow of boxes with running weights).
Top: the read only batch field with Open batch. Middle: the chain Weight in, Drained, Trimmed, Dried, each box with its
weight, its share of the raw weight and, once shown, its own loss line. Bottom left: loss by stage as bars with the
total loss. Bottom right: the expected yield from the BOM spec, then the actual yield set against it with the gap.
Every loss, total and percent is computed from the stage weights below."""
from frame_auto import header

SUMMARY = 'Yield Loss by Stage (jerky batch JRK-3310, 1,000 kg raw beef, spec 45% so 450 kg expected, drained 950, trimmed 900, dried 420, losses 50 + 50 + 480 = 580 kg, actual yield 42.0% against 45.0%, 30 kg short)'
ARIA = 'Interactive product screen: open a jerky batch and its expected yield, record the weight after drainage, trim and drying, see each loss as its own line and compare the actual yield with the spec'
STEPS = 5
STUDIO = dict(lede='A typical yield screen on your Sutton data. Want it different? Describe the change.',
              examples=['Yield spec by product', 'A scale reading at each stage', 'A weekly loss report', 'An alert under spec'],
              built_on='Batches, BOMs, lots and stage weights', change='Stages, limits and views')

ICON = '<path d="M2 13h12M3.5 13V8M6.5 13V5M9.5 13V7M12.5 13V10"/>'

CSS = (
 '.fld input[readonly]{background:#F4F4F5;color:#3F3F46;cursor:default;pointer-events:none}'
 '.g2{display:grid;grid-template-columns:316px 330px;grid-template-rows:60px 206px 254px;gap:10px;padding:10px 44px 0 16px;width:716px}'
 '.top{grid-column:1/3;display:flex;flex-direction:column;justify-content:center;gap:5px;padding:0 12px}.top .frm{display:flex;align-items:flex-end;gap:8px}.top .fld{width:236px}.top .ctx{font-size:8.9px;color:#71717A}.top .rs{margin-left:auto;display:flex;gap:6px;align-items:center}'
 '.cw{grid-column:1/3;display:flex;flex-direction:column}.cw>.empt{margin:9px;flex:1;padding:8px}.ct .bt{font-size:9px;padding:2px 9px}.ct .bt:disabled,.sg .bt:disabled{opacity:.45;cursor:not-allowed}'
 '.chain{display:grid;grid-template-columns:1fr 16px 1fr 16px 1fr 16px 1fr;padding:9px 9px;flex:1}.arw{display:grid;place-items:center;color:#A1A1AA}.arw svg{width:10px;height:10px}'
 '.sg{border:1px solid #E4E4E7;border-radius:8px;background:#fff;display:flex;flex-direction:column;overflow:hidden;transition:background-color .35s,border-color .35s}'
 '.sg .sh{display:flex;align-items:center;justify-content:space-between;gap:4px;padding:6px 8px;border-bottom:1px solid #F0F0F1;font-weight:600;font-size:9.9px}'
 '.sg .mt{padding:5px 8px 0;font-size:8.3px;color:#71717A;line-height:1.35}'
 '.sg .wv{padding:6px 8px 0}.sg .wv small{display:block;font-size:8.1px;color:#71717A}.sg .wv b{font-family:"JetBrains Mono",ui-monospace,monospace;font-size:15px;font-weight:600}.sg .wv b.wh{color:#D4D4D8;font-size:11px;font-family:inherit}'
 '.sg .ls{padding:5px 8px 0;min-height:22px}.sg .ft{margin-top:auto;padding:6px 8px;border-top:1px dashed #E4E4E7;font-size:8.3px;color:#52525B;display:flex;justify-content:space-between;align-items:center;min-height:30px}.sg .ft em{font-style:normal;font-family:"JetBrains Mono",ui-monospace,monospace;font-weight:600;color:#18181B}'
 '.sg .ft .bt{font-size:9px;padding:3px 8px;width:100%}.sg.dn{border-color:#BBF7D0}.sg.dn .sh{background:#F0FDF4}.sg.nx{border-style:dashed;border-color:#A1A1AA}'
 '.lp,.op{display:flex;flex-direction:column}.lp>.empt,.op>.empt{margin:9px;flex:1;padding:8px}'
 '.lb2{padding:10px 11px 0;display:flex;flex-direction:column;gap:9px}.lr{display:grid;grid-template-columns:70px 1fr 48px;gap:8px;align-items:center;font-size:9.2px}.lr small{display:block;font-size:8px;color:#71717A}'
 '.lr .bar{height:14px;border-radius:4px;background:#F4F4F5;position:relative;overflow:hidden}.lr .bar i{position:absolute;left:0;top:0;bottom:0;background:#F59E0B;border-radius:4px;transition:width .5s cubic-bezier(.22,.9,.28,1)}.lr .mono{text-align:right;font-weight:600}'
 '.lr.t{border-top:1px solid #E4E4E7;padding-top:7px;font-weight:600}.lr.t .bar i{background:#18181B}'
 '.calc{margin:9px 11px 0;padding:6px 9px;border-radius:7px;background:#FAFAFA;border:1px solid #F0F0F1;font-family:"JetBrains Mono",ui-monospace,monospace;font-size:9.2px;text-align:center;line-height:1.6}'
 '.ys{margin:9px 11px 0;display:grid;grid-template-columns:1fr 1fr 1fr;gap:6px}.ys div{border:1px solid #E4E4E7;border-radius:7px;padding:5px 7px}.ys div.w{border-color:#FECACA;background:#FEF2F2}.ys small{display:block;font-size:8.2px;color:#71717A}.ys b{font-family:"JetBrains Mono",ui-monospace,monospace;font-size:12px}'
 '.cmp{padding:10px 11px 0;display:flex;flex-direction:column;gap:8px}.cr{display:grid;grid-template-columns:64px 1fr 60px;gap:8px;align-items:center;font-size:9.2px}.cr small{display:block;font-size:8px;color:#71717A}'
 '.cr .bar{height:16px;border-radius:4px;background:#F4F4F5;position:relative}.cr .bar i{position:absolute;left:0;top:0;bottom:0;border-radius:4px;background:#A1A1AA}.cr.ac .bar i{background:#DC2626}.cr .mono{text-align:right;font-weight:600}'
 '.note{margin:9px 11px 0;padding:6px 8px;border-radius:7px;font-size:8.9px;line-height:1.45;background:#FAFAFA;border:1px solid #F0F0F1;color:#52525B}.note.w{background:#FEF2F2;border-color:#FECACA;color:#991B1B}'
 '.bom{margin:9px 11px 0;border:1px solid #E4E4E7;border-radius:8px;overflow:hidden}.bom .row{grid-template-columns:1fr 70px;font-size:9px;min-height:24px;padding:0 8px}.bom .row span:last-child{text-align:right;font-family:"JetBrains Mono",ui-monospace,monospace}'
 '.kp{margin:8px 11px 0;display:flex;flex-direction:column;gap:4px}.kp div{display:flex;justify-content:space-between;align-items:center;font-size:9px;color:#3F3F46}'
 '.tot{margin-top:auto;padding:8px 11px;border-top:1px solid #E4E4E7;font-size:9px;color:#52525B;line-height:1.4;background:#FAFAFA}.op .tot{padding-right:90px}'
)

WIN = (
 header(ICON, 'Yield by stage', 'Batch weights from raw to dried, with every loss')
 + '<div class="g2"><div class="cd top"><div class="frm"><label class="fld"><small>Batch</small>'
 '<input id="ibt" value="JRK-3310, Beef Jerky, 1,000 kg raw" readonly tabindex="-1" autocomplete="off" spellcheck="false"></label>'
 '<button type="button" class="bt pri" id="obb">Open batch</button><span class="rs" id="rs"></span></div><div class="ctx">Jerky batch on dehydrator line 2, started this morning</div></div>'
 '<div class="cd cw" id="cw"></div><div class="cd lp" id="lp"></div><div class="cd op" id="op"></div></div>'
)

JS = r'''
var FOC='.hd>*,.top .fld,.top .ctx,#obb,.cw .ct,.cw .sg,.cw>.empt,.lp .ct,.lp>*:not(.ct),.op .ct,.op>*:not(.ct)';
var MI=String.fromCharCode(8722),RAW=1000,SPEC=45.0;
var STG=[{k:'dr',nm:'Drained',lab:'Drainage',st:'Drain table 2',w:950,bt:'Log drainage'},{k:'tr',nm:'Trimmed',lab:'Trim',st:'Trim line 1',w:900,bt:'Log trim'},{k:'dy',nm:'Dried',lab:'Drying',st:'Dehydrator 3, 9 h',w:420,bt:'Log drying'}];
var S;
function inW(i){return i===0?RAW:STG[i-1].w;}
function loss(i){return inW(i)-STG[i].w;}
function totLoss(){return STG.reduce(function(a,s,i){return a+loss(i);},0);}
function out(){return STG[2].w;}
function exp(){return RAW*SPEC/100;}
function act(){return out()/RAW*100;}
function pc(x){return x.toFixed(1)+'%';}
function logged(i){return S.lg[i];}
var ARW='<div class="arw" aria-hidden="true"><svg viewBox="0 0 10 10" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"><path d="M2 5h6M5.5 2.5L8 5 5.5 7.5"/></svg></div>';
function nextI(){for(var i=0;i<3;i++)if(!S.lg[i])return i;return -1;}
function box(i){
if(i<0)return '<div class="sg dn in" id="s-in"><div class="sh"><span>Weight in</span><span class="ch c-ok">Weighed</span></div><div class="mt">Raw beef, lot BEEF-24-0731<br>Receiving scale 1</div><div class="wv"><small>kg</small><b id="win">'+n0(RAW)+'</b></div><div class="ls"></div><div class="ft"><span>Of raw</span><em>100%</em></div></div>';
var s=STG[i],d=logged(i),nx=nextI()===i;
var ft=d?'<span>Of raw</span><em id="pr-'+s.k+'">'+pc(s.w/RAW*100)+'</em>':'<button type="button" class="bt'+(nx?' pri':'')+'" id="b-'+s.k+'"'+(i===1?' data-pick="1"':'')+(nx?'':' disabled')+'>'+s.bt+'</button>';
return '<div class="sg in'+(d?' dn':nx?' nx':'')+'" id="s-'+s.k+'"><div class="sh"><span>'+s.nm+'</span>'+(d?'<span class="ch c-ok">Logged</span>':'<span class="ch c-idle">Open</span>')+'</div><div class="mt">'+s.st+'<br>'+(d?'Weighed at '+['9:10','10:25','7:40 pm'][i]:'Not weighed yet')+'</div>'+
'<div class="wv"><small>kg</small>'+(d?'<b id="w-'+s.k+'">'+n0(s.w)+'</b>':'<b class="wh">No weight</b>')+'</div>'+
'<div class="ls">'+(S.ll&&d?'<span class="ch c-warn" id="lo-'+s.k+'">Loss '+n0(loss(i))+' kg</span>':'')+'</div><div class="ft">'+ft+'</div></div>';}
function render(){
$('obb').className='bt '+(S.op?'done':'pri');$('obb').textContent=S.op?'Opened':'Open batch';
$('rs').innerHTML=!S.op?'':'<span class="ch c-idle mono">BOM BJ-07</span>'+(S.cp?'<span class="ch c-bad">Under spec</span>':'<span class="ch c-info">In progress</span>');
var c='<div class="ct"><span>Stage chain'+(S.op?', JRK-3310':'')+'</span>'+(S.op?'<span class="ch c-idle">'+S.lg.filter(Boolean).length+' of 3 stages logged</span>':'')+'</div>';
if(!S.op)c+='<div class="empt"><b>No batch open</b><span>Open a batch to weigh it in, then after drainage, trim and drying.</span></div>';
else c+='<div class="chain">'+box(-1)+ARW+box(0)+ARW+box(1)+ARW+box(2)+'</div>';
$('cw').innerHTML=c;
var all=S.lg.every(Boolean);
var l='<div class="ct"><span>Loss by stage</span>'+(S.op?'<button type="button" class="bt '+(S.ll?'done':'pri')+'" id="llb"'+(all?'':' disabled')+'>'+(S.ll?'Shown':'Show loss lines')+'</button>':'')+'</div>';
if(!S.ll)l+='<div class="empt"><b>No loss lines yet</b><span>Each stage gets its own loss line once its weight is logged.</span></div>';
else{l+='<div class="lb2 in" id="ll">'+STG.map(function(s,i){return '<div class="lr"><span>'+s.lab+'<small>'+n0(inW(i))+' to '+n0(s.w)+' kg</small></span><span class="bar"><i style="width:'+(loss(i)/RAW*100/0.6).toFixed(1)+'%"></i></span><span class="mono" id="ln-'+s.k+'">'+n0(loss(i))+' kg</span></div>';}).join('')+
'<div class="lr t"><span>Total loss</span><span class="bar"><i style="width:'+(totLoss()/RAW*100/0.6).toFixed(1)+'%"></i></span><span class="mono" id="lt">'+n0(totLoss())+' kg</span></div></div>'+
'<div class="calc in" id="lcal">'+STG.map(function(s,i){return n0(loss(i));}).join(' + ')+' = '+n0(totLoss())+' kg<br>'+n0(RAW)+' '+MI+' '+n0(totLoss())+' = '+n0(RAW-totLoss())+' kg out</div>';}
l+='<div class="tot">Loss is the weight in minus the weight out at each stage.</div>';
$('lp').innerHTML=l;
var o='<div class="ct"><span>Yield against spec</span>'+(S.op?'<button type="button" class="bt '+(S.cp?'done':'pri')+'" id="cpb"'+(S.ll?'':' disabled')+'>'+(S.cp?'Compared':'Compare')+'</button>':'')+'</div>';
if(!S.op)o+='<div class="empt"><b>No spec loaded</b><span>The expected yield comes from the BOM once a batch is open.</span></div>';
else{o+='<div class="ys in"><div><small>Spec yield</small><b id="spy">'+pc(SPEC)+'</b></div><div><small>Expected, kg</small><b id="spk">'+n0(exp())+'</b></div>'+(S.cp?'<div class="w"><small>Actual, kg</small><b id="ack">'+n0(out())+'</b></div>':'<div><small>Actual, kg</small><b class="mut" style="font-family:inherit;font-size:10px">After drying</b></div>')+'</div>';
if(!S.cp)o+='<div class="bom in"><div class="row h"><span>BOM BJ-07, Beef jerky</span><span>Per batch</span></div><div class="row"><span>Beef inside round, raw</span><span>1,000 kg</span></div><div class="row"><span>Jerky spice blend</span><span>25 kg</span></div><div class="row"><span>Cure</span><span>5 kg</span></div></div>';
else o+='<div class="cmp in" id="cmp"><div class="cr"><span>Spec<small>From the BOM</small></span><span class="bar"><i style="width:'+(SPEC/50*100).toFixed(1)+'%"></i></span><span class="mono" id="cs">'+pc(SPEC)+'</span></div><div class="cr ac"><span>Actual<small>JRK-3310</small></span><span class="bar"><i style="width:'+(act()/50*100).toFixed(1)+'%"></i></span><span class="mono" id="ca">'+pc(act())+'</span></div></div>'+
'<div class="note w in" id="gap">'+n0(out())+' kg against '+n0(exp())+' kg expected: <b>'+n0(exp()-out())+' kg</b> under spec. Drying is the largest loss at '+n0(loss(2))+' kg.</div>'+
'<div class="kp in"><div><span>Stage weights</span><span class="ch c-ok">4 of 4 kept</span></div><div><span>Scale</span><span>Floor scale 2</span></div><div><span>Reviewed by</span><span>QA, M. Okafor</span></div></div>';}
o+='<div class="tot">Actual yield is the dried weight over the raw weight.</div>';
$('op').innerHTML=o;
}
function resetState(){S={op:false,lg:[false,false,false],ll:false,cp:false};render();}
winEl.addEventListener('click',function(e){var b=e.target.closest&&e.target.closest('#b-tr');if(b&&b.hasAttribute('data-pick')&&S.lg[0]&&!S.lg[1]){S.lg[1]=true;render();}});
var ST=[
{id:'op',target:function(){return $('obb');},prompt:'Open batch JRK-3310',where:'below',run:function(){S.op=true;render();},
 after:function(){return['A batch with its expected yield','JRK-3310, '+n0(RAW)+' kg raw. The spec is '+pc(SPEC)+', so '+n0(exp())+' kg is expected.'];}},
{id:'dr',target:function(){return $('b-dr');},prompt:'Log drainage',where:'below',run:function(){S.lg[0]=true;render();},
 after:function(){return['Weight in and after drainage',n0(RAW)+' kg in, '+n0(STG[0].w)+' kg after drainage.'];}},
{id:'tc',target:function(){return $('b-dy');},back:function(){return S.lg[1]?null:[$('b-tr'),'Log trim','below'];},prompt:'Log drying',where:'below',run:function(){S.lg=[true,true,true];render();},
 after:function(){return['Trim and cook weights logged',n0(STG[1].w)+' kg after trim, '+n0(STG[2].w)+' kg out of the dehydrator.'];}},
{id:'ll',target:function(){return $('llb');},prompt:'Show each loss line',where:'below',run:function(){S.ll=true;render();},
 after:function(){return['Each loss on its own line','Drainage '+loss(0)+', trim '+loss(1)+', drying '+loss(2)+': '+n0(totLoss())+' kg lost in total.'];}},
{id:'cp',target:function(){return $('cpb');},prompt:'Compare with the spec',where:'below',run:function(){S.cp=true;render();},
 after:function(){return['Actual yield against the spec',n0(out())+' kg is '+pc(act())+' against a '+pc(SPEC)+' spec of '+n0(exp())+' kg: '+n0(exp()-out())+' kg short.'];}}];
'''
