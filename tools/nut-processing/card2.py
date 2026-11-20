"""Nut processing card 2: Stage Yield & Loss. Layout: a stage chain (a flow of boxes with running totals).
Top: the read only raw lot field with Open lot. Middle: the chain Raw lot, Shelling, Roasting, Blanching, Packing,
each box with weight in, weight out, loss and the running yield. Bottom left: loss by stage as bars with the yield
product. Bottom right: yield by origin and season against the 56 percent expected yield, with the flag.
Every weight, loss and yield is computed from the stage weights below."""
from frame_auto import header

SUMMARY = 'Stage Yield & Loss (raw lot L-2417, 20,000 lb in shell almonds, shelling 12,800 out at 36% loss, roasting 12,160 at 5%, blanching 11,552 at 5%, total yield 57.76% = 0.64 x 0.95 x 0.95, origin B at 55.0% flagged under the 56% expected)'
ARIA = 'Interactive product screen: open a raw lot and follow it through shelling, roasting and blanching, see weight in and out at each stage, read the loss by stage, compare yield across origins and seasons and flag a lot below the expected yield'
STEPS = 5
STUDIO = dict(lede='A typical yield screen on your Sutton data. Want it different? Describe the change.',
              examples=['Expected yield by variety', 'Loss split into shells and skins', 'A weekly yield email', 'Yield by grower and block'],
              built_on='Lots, work orders, BOMs and stage weights', change='Stages, limits and views')

ICON = '<path d="M2 4h3v8H2zM6.5 6h3v6h-3zM11 8h3v4h-3z"/>'

CSS = (
 '.fld input[readonly]{background:#F4F4F5;color:#3F3F46;cursor:default;pointer-events:none}'
 '.g2{display:grid;grid-template-columns:320px 326px;grid-template-rows:60px 190px 270px;gap:10px;padding:10px 44px 0 16px;width:716px}'
 '.top{grid-column:1/3;display:flex;flex-direction:column;justify-content:center;gap:5px;padding:0 12px}.top .frm{display:flex;align-items:flex-end;gap:8px}.top .fld{width:130px}.top .ctx{font-size:8.9px;color:#71717A}.top .rs{margin-left:auto;display:flex;gap:6px;align-items:center}'
 '.cw{grid-column:1/3;display:flex;flex-direction:column}.cw>.empt{margin:9px;flex:1;padding:8px}.cw .ct .bt,.lp .ct .bt,.op .ct .bt{font-size:9px;padding:2px 9px}.ct .bt:disabled{opacity:.45;cursor:not-allowed}'
 '.chain{display:grid;grid-template-columns:1fr 14px 1fr 14px 1fr 14px 1fr 14px 1fr;padding:8px 9px;flex:1}.arw{display:grid;place-items:center;color:#A1A1AA}.arw svg{width:10px;height:10px}'
 '.sg{border:1px solid #E4E4E7;border-radius:8px;background:#fff;display:flex;flex-direction:column;overflow:hidden;transition:background-color .35s,border-color .35s}'
 '.sg .sh{display:flex;align-items:center;justify-content:space-between;gap:4px;padding:5px 8px;border-bottom:1px solid #F0F0F1;font-weight:600;font-size:9.8px}'
 '.sg .mt{padding:4px 8px 0;font-size:8.3px;color:#71717A;line-height:1.35}'
 '.sg .io{display:grid;grid-template-columns:1fr 1fr;gap:4px;padding:5px 8px 0}.sg .io small{display:block;font-size:8.1px;color:#71717A}.sg .io b{font-family:"JetBrains Mono",ui-monospace,monospace;font-size:10.4px;font-weight:600}'
 '.sg .ls{padding:4px 8px 0;min-height:20px}.sg .run{margin-top:auto;padding:5px 8px;border-top:1px dashed #E4E4E7;font-size:8.3px;color:#52525B;display:flex;justify-content:space-between}.sg .run em{font-style:normal;font-family:"JetBrains Mono",ui-monospace,monospace;font-weight:600;color:#18181B}'
 '.sg.pk{border-color:#BBF7D0;background:#F0FDF4}.sg .wh{color:#D4D4D8}'
 '.lp,.op{display:flex;flex-direction:column}.lp>.empt,.op>.empt{margin:9px;flex:1;padding:8px}'
 '.lb2{padding:9px 11px 0;display:flex;flex-direction:column;gap:9px}.lr{display:grid;grid-template-columns:62px 1fr 42px;gap:8px;align-items:center;font-size:9.2px}.lr small{display:block;font-size:8px;color:#71717A}'
 '.lr .bar{height:14px;border-radius:4px;background:#F4F4F5;position:relative;overflow:hidden}.lr .bar i{position:absolute;left:0;top:0;bottom:0;background:#F59E0B;border-radius:4px;transition:width .5s cubic-bezier(.22,.9,.28,1)}.lr .mono{text-align:right;font-weight:600}'
 '.yp{margin:10px 11px 0;padding:7px 9px;border-radius:7px;background:#FAFAFA;border:1px solid #F0F0F1;font-family:"JetBrains Mono",ui-monospace,monospace;font-size:9.4px;text-align:center}'
 '.ys{margin:8px 11px 0;display:grid;grid-template-columns:1fr 1fr 1fr;gap:6px}.ys div{border:1px solid #E4E4E7;border-radius:7px;padding:5px 7px}.ys small{display:block;font-size:8.2px;color:#71717A}.ys b{font-family:"JetBrains Mono",ui-monospace,monospace;font-size:11px}'
 '.orr{padding:6px 11px 0;display:flex;flex-direction:column;gap:6px}.orw{display:grid;grid-template-columns:96px 1fr 46px;gap:8px;align-items:center;font-size:9.1px;padding:4px 6px;border-radius:7px;border:1px solid transparent;transition:background-color .35s,border-color .35s}.orw small{display:block;font-size:8px;color:#71717A}'
 '.orw .bar{height:14px;border-radius:4px;background:#F4F4F5;position:relative}.orw .bar i{position:absolute;left:0;top:0;bottom:0;background:#18181B;border-radius:4px;opacity:.85}.orw .bar .ex{position:absolute;top:-4px;bottom:-4px;width:2px;background:#DC2626}.orw .mono{text-align:right;font-weight:600}'
 '.orw.fl{background:#FEF2F2;border-color:#FECACA}.orw.fl .bar i{background:#DC2626}.axis{display:flex;justify-content:space-between;padding:0 63px 0 115px;font-size:8px;color:#71717A;font-family:"JetBrains Mono",ui-monospace,monospace}'
 '.note{margin:8px 11px 0;padding:6px 8px;border-radius:7px;font-size:8.9px;line-height:1.45;background:#FAFAFA;border:1px solid #F0F0F1;color:#52525B}.note.w{background:#FEF2F2;border-color:#FECACA;color:#991B1B}'
 '.tot{margin-top:auto;padding:8px 11px;border-top:1px solid #E4E4E7;font-size:9px;color:#52525B;line-height:1.4;background:#FAFAFA}.op .tot{padding-right:90px}'
)

WIN = (
 header(ICON, 'Yield by stage', 'Weight in and out from raw lot to packed')
 + '<div class="g2"><div class="cd top"><div class="frm"><label class="fld"><small>Raw lot</small>'
 '<input id="ilt" value="L-2417" readonly tabindex="-1" autocomplete="off" spellcheck="false"></label>'
 '<button type="button" class="bt pri" id="olb">Open lot</button><span class="rs" id="rs"></span></div><div class="ctx">In shell almonds, origin A, 2026 harvest</div></div>'
 '<div class="cd cw" id="cw"></div><div class="cd lp" id="lp"></div><div class="cd op" id="op"></div></div>'
)

JS = r'''
var FOC='.hd>*,.top .fld,.top .ctx,#olb,.cw .ct,.cw .sg,.cw>.empt,.lp .ct,.lp>*:not(.ct),.op .ct,.op>*:not(.ct)';
var RAW=20000,EXP=56.0;
var STG=[{nm:'Shelling',ln:'Huller 1',dt:'Nov 3',out:12800,what:'shells and hulls'},{nm:'Roasting',ln:'Roaster 2',dt:'Nov 5',out:12160,what:'moisture'},{nm:'Blanching',ln:'Blancher 1',dt:'Nov 6',out:11552,what:'skins'}];
var ORG=[{k:'A26',nm:'Origin A, 2026',lot:'L-2417',y:null},{k:'B26',nm:'Origin B, 2026',lot:'L-2433',y:55.0},{k:'A25',nm:'Origin A, 2025',lot:'Season average',y:58.1},{k:'B25',nm:'Origin B, 2025',lot:'Season average',y:56.4}];
var S;
function ins(i){return i===0?RAW:STG[i-1].out;}
function loss(i){return (ins(i)-STG[i].out)/ins(i)*100;}
function yld(i){return STG[i].out/RAW*100;}
function total(){return STG[STG.length-1].out/RAW*100;}
function oy(o){return o.y===null?Math.round(total()*10)/10:o.y;}
function flagged(o){return oy(o)<EXP;}
function pc(x,d){return x.toFixed(d===undefined?1:d)+'%';}
var ARW='<div class="arw" aria-hidden="true"><svg viewBox="0 0 10 10" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"><path d="M2 5h6M5.5 2.5L8 5 5.5 7.5"/></svg></div>';
function box(i){
if(i<0)return '<div class="sg in" id="s-raw"><div class="sh"><span>Raw lot</span><span class="ch c-ok">In</span></div><div class="mt">Harvest 2026, Bay 3<br>Received Nov 1</div><div class="io"><div><small>In shell, lb</small>'+(S.w?'<b id="raw">'+n0(RAW)+'</b>':'<b class="wh">On file</b>')+'</div></div><div class="ls"></div><div class="run"><span>Yield</span><em>'+(S.w?'100%':'')+'</em></div></div>';
if(i===3)return '<div class="sg pk in" id="s-pack"><div class="sh"><span>Packing</span><span class="ch c-ok">Packed</span></div><div class="mt">Line 4, 25 lb cases<br>Nov 7</div><div class="io"><div><small>Packed, lb</small>'+(S.w?'<b id="pk">'+n0(STG[2].out)+'</b>':'<b class="wh">On file</b>')+'</div></div><div class="ls"></div><div class="run"><span>Total yield</span><em id="ty">'+(S.w?pc(total(),2):'')+'</em></div></div>';
var s=STG[i];return '<div class="sg in" id="s-'+i+'"><div class="sh"><span>'+s.nm+'</span><span class="ch c-ok">Done</span></div><div class="mt">'+s.ln+', '+s.dt+'</div>'+
'<div class="io"><div><small>In, lb</small>'+(S.w?'<b id="in'+i+'">'+n0(ins(i))+'</b>':'<b class="wh">On file</b>')+'</div><div><small>Out, lb</small>'+(S.w?'<b id="out'+i+'">'+n0(s.out)+'</b>':'<b class="wh">On file</b>')+'</div></div>'+
'<div class="ls">'+(S.l?'<span class="ch c-warn" id="lo'+i+'">Loss '+pc(loss(i))+'</span>':'')+'</div><div class="run"><span>Yield so far</span><em id="ry'+i+'">'+(S.w?pc(yld(i),i===2?2:1):'')+'</em></div></div>';}
function render(){
$('olb').className='bt '+(S.op?'done':'pri');$('olb').textContent=S.op?'Opened':'Open lot';
$('rs').innerHTML=!S.op?'':(S.w?'<span class="ch c-idle mono">'+n0(RAW)+' lb in</span>':'')+'<span class="ch c-ok">Packed</span>';
var c='<div class="ct"><span>Stage chain'+(S.op?', L-2417':'')+'</span>'+(S.op?'<button type="button" class="bt '+(S.w?'done':'pri')+'" id="wtb">'+(S.w?'Weights shown':'Show weights in and out')+'</button>':'')+'</div>';
if(!S.op)c+='<div class="empt"><b>No lot open</b><span>Open a raw lot to follow it through shelling, roasting and blanching to packing.</span></div>';
else c+='<div class="chain">'+box(-1)+ARW+box(0)+ARW+box(1)+ARW+box(2)+ARW+box(3)+'</div>';
$('cw').innerHTML=c;
var l='<div class="ct"><span>Loss by stage</span>'+(S.op?'<button type="button" class="bt '+(S.l?'done':'pri')+'" id="lsb"'+(S.w?'':' disabled')+'>'+(S.l?'Calculated':'Calculate loss')+'</button>':'')+'</div>';
if(!S.l)l+='<div class="empt"><b>No loss calculated</b><span>Loss shows by stage once weights in and out are recorded.</span></div>';
else{l+='<div class="lb2 in">'+STG.map(function(s,i){return '<div class="lr"><span>'+s.nm+'<small>'+n0(ins(i)-s.out)+' lb '+s.what+'</small></span><span class="bar"><i style="width:'+(loss(i)/40*100).toFixed(1)+'%"></i></span><span class="mono" id="lp'+i+'">'+pc(loss(i))+'</span></div>';}).join('')+'</div>'+
'<div class="yp in" id="yp">0.64 \u00d7 0.95 \u00d7 0.95 = '+pc(total(),2)+' yield</div>'+
'<div class="ys in"><div><small>Raw in, lb</small><b>'+n0(RAW)+'</b></div><div><small>Packed, lb</small><b>'+n0(STG[2].out)+'</b></div><div><small>Lost, lb</small><b id="lst">'+n0(RAW-STG[2].out)+'</b></div></div>';}
l+='<div class="tot">Loss is weight in minus weight out over weight in.</div>';
$('lp').innerHTML=l;
var o='<div class="ct"><span>Yield by origin and season</span>'+(S.l?(!S.c?'<button type="button" class="bt pri" id="cob">Compare origins</button>':'<button type="button" class="bt '+(S.f?'done':'pri')+'" id="flb">'+(S.f?'Checked':'Check expected yield')+'</button>'):'')+'</div>';
if(!S.c)o+='<div class="empt"><b>No comparison yet</b><span>Compare packed yield across origins and seasons against the expected yield.</span></div>';
else{o+='<div class="orr in">'+ORG.map(function(r){var fl=S.f&&flagged(r);return '<div class="orw'+(fl?' fl':'')+'" id="o-'+r.k+'"><span>'+r.nm+'<small>'+r.lot+'</small></span><span class="bar"><i style="width:'+((oy(r)-50)/10*100).toFixed(1)+'%"></i><span class="ex" style="left:'+((EXP-50)/10*100).toFixed(1)+'%"></span></span><span class="mono" id="oy-'+r.k+'">'+pc(oy(r))+'</span></div>';}).join('')+'</div>'+
'<div class="axis"><span>50%</span><span>56% expected</span><span>60%</span></div>';
if(S.f)o+='<div class="note w in" id="fnt">'+ORG.filter(function(r){return S.f&&flagged(r);}).map(function(r){return r.lot+', '+'o'+r.nm.slice(1)+': '+pc(oy(r))+' is under the '+pc(EXP)+' expected yield. Flagged for review.';}).join(' ')+'</div>';
else o+='<div class="note in">Expected packed yield for blanched almonds: '+pc(EXP)+'.</div>';}
o+='<div class="tot">Same stages, compared by origin and season.</div>';
$('op').innerHTML=o;
}
function resetState(){S={op:false,w:false,l:false,c:false,f:false};render();}
var ST=[
{id:'op',target:function(){return $('olb');},prompt:'Open raw lot L-2417',where:'below',run:function(){S.op=true;render();},
 after:function(){return['A raw lot through every stage','L-2417 ran through shelling, roasting and blanching to packing.'];}},
{id:'w',target:function(){return $('wtb');},prompt:'Show weights in and out',where:'below',run:function(){S.w=true;render();},
 after:function(){return['Weight in and out at each stage',n0(RAW)+' lb in shell to '+n0(STG[0].out)+', '+n0(STG[1].out)+' and '+n0(STG[2].out)+' lb packed.'];}},
{id:'l',target:function(){return $('lsb');},prompt:'Calculate loss by stage',where:'above',run:function(){S.l=true;render();},
 after:function(){return['Loss by stage','Shelling '+pc(loss(0))+', roasting '+pc(loss(1))+', blanching '+pc(loss(2))+': '+pc(total(),2)+' total yield.'];}},
{id:'c',target:function(){return $('cob');},prompt:'Compare origins',where:'above',run:function(){S.c=true;render();},
 after:function(){return['Yield across origins','Origin A '+pc(oy(ORG[0]))+' and origin B '+pc(oy(ORG[1]))+' this season, against '+pc(EXP)+' expected.'];}},
{id:'f',target:function(){return $('flb');},prompt:'Check against expected yield',where:'above',run:function(){S.f=true;render();},
 after:function(){return['A lot below expected yield is flagged','L-2433 from origin B at '+pc(oy(ORG[1]))+' is under '+pc(EXP)+'. Only that lot is flagged.'];}}];
'''
