"""Food distributors card 4: Scan Verified Picking & Shipping. Layout: a board.
Top: the read only sales order field (SO-3110) with Open pick list. Three columns: the pick list (lines sorted by bin,
Complete pick at the bottom), the scan panel (the line to pick, the read only case barcode with Scan item, the match or
mismatch result with the item pictures, the scan log) and the shipment (stock on hand before and after, the documents).
Bottom strip: running totals (lines confirmed, cases picked, wrong scans caught, documents).
A wrong scan never confirms a line: line 2 stays open until the Lavender case is scanned."""
import json
from frame_auto import header

SUMMARY = 'Scan Verified Picking & Shipping (open the SO-3110 pick list in bin order, scan Lime to confirm A-02-1, a Lime scan on the Lavender line is caught, complete the pick so on hand drops by 270 cases, generate the packing slip and bill of lading)'
ARIA = 'Interactive product screen: open a pick list sorted by bin, scan each case to confirm the line, see a warning when a similar variant is scanned, complete the pick to update stock on hand and generate the packing slip and bill of lading'
STEPS = 5
STUDIO = dict(lede='A typical pick and ship screen on your Sutton data. Want it different? Describe the change.',
              examples=['Pick by zone or by wave', 'A photo check on each case', 'Lot and expiry on every scan', 'Carrier labels per pallet'],
              built_on='Orders, bins, items and shipments', change='Checks, documents and views')

ICON = '<path d="M2 4V2.5h2M12 2.5h2V4M14 12v1.5h-2M4 13.5H2V12"/><path d="M5 5v6M7 5v6M9.5 5v6M11 5v6"/>'

CSS = (
 '.fld input[readonly]{background:#F4F4F5;color:#3F3F46;cursor:default;pointer-events:none}'
 '.g3{display:grid;grid-template-columns:196px 232px 208px;grid-template-rows:62px 398px 60px;gap:10px;padding:10px 44px 0 16px}'
 '.top{grid-column:1/4;display:flex;flex-direction:column;justify-content:center;gap:5px;padding:0 12px}.top .frm{display:flex;align-items:flex-end;gap:8px}.top .fld{width:150px}.top .ctx{font-size:8.9px;color:#71717A}.top .rs{margin-left:auto}'
 '.col{display:flex;flex-direction:column;min-width:0}.col>.empt{margin:9px;flex:1;padding:10px}'
 '.pl{display:flex;flex-direction:column;gap:6px;padding:8px}'
 '.pk{border:1px solid #E4E4E7;border-radius:8px;padding:6px 8px;display:grid;grid-template-columns:24px 1fr;grid-template-rows:auto auto;column-gap:7px;row-gap:2px;transition:background-color .35s,border-color .35s}'
 '.pk .pc{grid-row:1/3;display:grid;place-items:center}.pk .t1{display:flex;align-items:center;justify-content:space-between;gap:4px}.pk .t1 b{font-family:"JetBrains Mono",ui-monospace,monospace;font-size:10px}'
 '.pk .t2{font-size:9px;color:#3F3F46;line-height:1.3}.pk .t2 em{font-style:normal;font-family:"JetBrains Mono",ui-monospace,monospace;color:#18181B;font-weight:600}'
 '.pk.cur{border-color:#18181B;box-shadow:inset 3px 0 0 #18181B}.pk.ok{background:#F0FDF4;border-color:#86EFAC}.pk.bad{background:#FEF2F2;border-color:#FCA5A5;box-shadow:inset 3px 0 0 #DC2626}'
 '.pd{margin:2px 9px 0;display:grid;grid-template-columns:1fr 1fr;gap:6px;padding:7px 8px;border:1px solid #F0F0F1;border-radius:8px;background:#FAFAFA}.srt{padding:0 9px;font-size:8.6px;color:#71717A}.cpw{margin-top:auto;padding:8px 9px;border-top:1px solid #F0F0F1;display:flex;flex-direction:column;gap:5px}.cpw .bt{width:100%}.cpw .bt:disabled{opacity:.45;cursor:not-allowed}.cpw small{font-size:8.5px;color:#71717A}'
 '.sc{display:flex;flex-direction:column;gap:7px;padding:8px 9px}'
 '.cl{display:grid;grid-template-columns:26px 1fr;gap:7px;align-items:center;border:1px solid #E4E4E7;border-radius:8px;padding:6px 8px;background:#FAFAFA}.cl small{display:block;font-size:8.4px;color:#71717A}.cl b{font-size:9.6px}.cl .mono{font-size:9px}'
 '.sc .frm{display:flex;align-items:flex-end;gap:6px}.sc .fld{flex:1}.sc .bt:disabled{opacity:.45;cursor:not-allowed}.sc .ctx{font-size:8.6px;color:#71717A;margin-top:-3px}'
 '.res{border-radius:8px;padding:7px 8px;font-size:9px;line-height:1.4;border:1px solid #F0F0F1;background:#FAFAFA;color:#52525B}.res.g{background:#F0FDF4;border-color:#BBF7D0;color:#166534}.res.w{background:#FEF2F2;border-color:#FECACA;color:#991B1B}'
 '.res .vs{display:grid;grid-template-columns:1fr 1fr;gap:6px;margin:5px 0}.res .vi{display:flex;align-items:center;gap:6px;background:#fff;border:1px solid #FECACA;border-radius:6px;padding:4px 6px;color:#18181B}.res .vi small{display:block;font-size:8px;color:#71717A}.res .vi b{font-size:8.8px;font-weight:600;line-height:1.25}.res .vi.x{border-color:#DC2626}'
 '.lg .row{grid-template-columns:44px 1fr 56px;font-size:8.8px;min-height:21px;padding:0 2px}.lg .row span:nth-child(2){font-family:"JetBrains Mono",ui-monospace,monospace;font-size:8.4px}.lg .row span:last-child{text-align:right}.lg .row.h{font-size:8.4px}'
 '.sh2{display:flex;flex-direction:column;gap:7px;padding:8px 9px;flex:1}.sh2 .two{display:grid;grid-template-columns:1fr 1fr;gap:6px}'
 '.oh .row{grid-template-columns:1fr 44px 44px;font-size:9px;min-height:23px;padding:0 2px}.oh .row span:nth-child(2),.oh .row span:nth-child(3){text-align:right;font-family:"JetBrains Mono",ui-monospace,monospace}.oh .row.h span{font-family:inherit}.oh .dn{color:#166534;font-weight:600}'
 '.dcs{display:flex;flex-direction:column;gap:5px;margin-top:auto}.dcs .lb{display:flex;align-items:center;justify-content:space-between;font-size:9.4px;font-weight:600}.dcs .bt{font-size:9.2px;padding:3px 9px}.dcs .bt:disabled{opacity:.45;cursor:not-allowed}'
 '.doc{display:flex;align-items:center;gap:7px;border:1px solid #BBF7D0;background:#F0FDF4;border-radius:8px;padding:5px 7px}.doc svg{flex:none}.doc b{display:block;font-size:9.2px}.doc small{display:block;font-size:8.4px;color:#52525B}'
 '.dph{border:1px dashed #E4E4E7;border-radius:8px;background:#FAFAFA;padding:9px;font-size:8.8px;color:#A1A1AA;text-align:center}'
 '.strip{grid-column:1/4;display:grid;grid-template-columns:repeat(4,1fr);gap:8px;align-items:center;padding:0 12px}.strip .kv b{font-size:12px;font-family:"JetBrains Mono",ui-monospace,monospace}.strip .wait{grid-column:1/5;font-size:9.2px;color:#A1A1AA}'
)

WIN = (
 header(ICON, 'Pick and ship', 'Every case scanned against its line before it ships')
 + '<div class="g3"><div class="cd top"><div class="frm"><label class="fld"><small>Sales order</small>'
 '<input id="iso" value="SO-3110" readonly tabindex="-1" autocomplete="off" spellcheck="false"></label>'
 '<button type="button" class="bt pri" id="opb">Open pick list</button><span class="rs" id="rs"></span></div><div class="ctx">Greenfield Market, ships Nov 20 from the main warehouse</div></div>'
 '<div class="cd col" id="c1"></div><div class="cd col" id="c2"></div><div class="cd col" id="c3"></div><div class="cd strip" id="stp"></div></div>'
)

JS = r'''
var FOC='.hd>*,.top .fld,.top .ctx,#opb,.col>.ct,.pk,.srt,.cpw,.cl,.sc .frm,.sc .ctx,.res,.lg,.sh2>*,.col>.empt,.strip';
var ORDER=[{bin:'B-12-3',it:'Penne Pasta 20 lb',sh:'Penne',q:200,oh:700,bc:'085034120207',col:'#F59E0B',box:1},
{bin:'A-02-1',it:'Dish Soap Lime 12 pk',sh:'Lime',q:40,oh:500,bc:'085012340412',col:'#84CC16'},
{bin:'A-04-2',it:'Dish Soap Lavender 12 pk',sh:'Lavender',q:30,oh:300,bc:'085012340429',col:'#A78BFA'}];
var PICK=ORDER.slice().sort(function(a,b){return a.bin<b.bin?-1:a.bin>b.bin?1:0;});
var L1=PICK[0],L2=PICK[1],L3=PICK[2];
var S;
function fbc(c){return c.charAt(0)+' '+c.substr(1,5)+' '+c.substr(6,5)+' '+c.charAt(11);}
function pic(l,s){s=s||22;if(l.box)return '<svg width="'+s+'" height="'+s+'" viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="4" width="18" height="17" rx="2" fill="'+l.col+'"/><rect x="6" y="8" width="12" height="7" rx="1.5" fill="#fff" opacity=".9"/><path d="M8 13l2-3M11 13l2-3M14 13l2-3" stroke="#D97706" stroke-width="1.4" stroke-linecap="round"/></svg>';
return '<svg width="'+s+'" height="'+s+'" viewBox="0 0 24 24" aria-hidden="true"><rect x="9.5" y="1.5" width="5" height="4" rx="1" fill="#52525B"/><rect x="6" y="5.5" width="12" height="17" rx="3.5" fill="'+l.col+'"/><rect x="8" y="11" width="8" height="6" rx="1.2" fill="#fff" opacity=".88"/></svg>';}
function total(){return PICK.reduce(function(a,l){return a+l.q;},0);}
function picked(){return PICK.slice(0,S.c).reduce(function(a,l){return a+l.q;},0);}
function warn(){return S.wrong>0&&S.c===1;}
function inHand(){return S.c===0?L1:S.c===1?(warn()?L2:L1):L3;}
function lstat(i){if(i<S.c)return ['Picked','c-ok','ok'];if(i===1&&warn())return ['Wrong item','c-bad','bad'];if(i===S.c&&!S.done)return ['Next','c-info','cur'];return ['Open','c-idle',''];}
function scan(){if(S.c===0)S.c=1;else if(S.c===1&&!S.wrong)S.wrong=1;else if(S.c<3)S.c++;}
function after(l){return l.oh-l.q;}
function render(){
var opb=$('opb');opb.className='bt '+(S.op?'done':'pri');opb.textContent=S.op?'Opened':'Open pick list';
$('rs').innerHTML=!S.op?'':S.gen?'<span class="ch c-ok" id="rst">Ready to ship</span>':S.done?'<span class="ch c-ok" id="rst">Picked</span>':'<span class="ch c-warn" id="rst">Picking</span>';
var h='<div class="ct"><span>Pick list</span>'+(S.op?'<span class="ch c-idle" id="plc">'+S.c+' of 3</span>':'')+'</div>';
if(!S.op)h+='<div class="empt"><span>Open a sales order to build its pick list, sorted by bin.</span></div>';
else{h+='<div class="pl" id="pl">'+PICK.map(function(l,i){var s=lstat(i);return '<div class="pk in '+s[2]+'" id="p-'+l.bin+'"><span class="pc">'+pic(l)+'</span><div class="t1"><b>'+l.bin+'</b><span class="ch '+s[1]+'" id="s-'+l.bin+'">'+s[0]+'</span></div><div class="t2">'+l.it+', <em>'+n0(l.q)+'</em> cases</div></div>';}).join('')+'</div>';
h+='<div class="srt">Walk path sorted by bin, A aisle first.</div><div class="pd in"><div class="kv"><small>Picker</small><b>Dana K.</b></div><div class="kv"><small>Zones</small><b>A, then B</b></div></div>';
h+='<div class="cpw"><button type="button" class="bt '+(S.done?'done':'pri')+'" id="cpb"'+(S.c<3&&!S.done?' disabled':'')+'>'+(S.done?'Pick completed':'Complete pick')+'</button><small>Opens once every line is scanned.</small></div>';}
$('c1').innerHTML=h;
var s='<div class="ct"><span>Scan</span>'+(S.op?'<span class="ch '+(warn()?'c-bad':S.c===3?'c-ok':'c-info')+'" id="scc">'+(S.c===3?'All lines confirmed':'Line '+(S.c+1)+' of 3')+'</span>':'')+'</div>';
if(!S.op)s+='<div class="empt"><span>Scan each case against its line. A wrong item never confirms a line.</span></div>';
else{var cl=PICK[Math.min(S.c,2)],ih=inHand(),pk=S.c>=1&&S.c<3&&S.wrong;
s+='<div class="sc">'+(S.c<3?'<div class="cl in"><span>'+pic(cl,24)+'</span><div><small>Pick from <span class="mono">'+cl.bin+'</span></small><b>'+cl.it+'</b><small>'+n0(cl.q)+' cases</small></div></div>':'<div class="cl in"><span>'+pic(L3,24)+'</span><div><small>Last line</small><b>All 3 lines scanned</b><small>'+n0(total())+' cases confirmed</small></div></div>');
s+='<div class="frm"><label class="fld"><small>Case barcode</small><input id="ibc" value="'+fbc(ih.bc)+'" readonly tabindex="-1" autocomplete="off" spellcheck="false"></label><button type="button" class="bt pri" id="scb"'+(pk?' data-pick="1"':'')+(S.c>=3?' disabled':'')+'>Scan item</button></div>';
s+='<div class="ctx">'+(S.c>=3?'Scanner idle':warn()?'Case swapped, now in hand at '+L2.bin:'Case in hand at '+cl.bin)+'</div>';
if(warn())s+='<div class="res w in" id="wn"><b>Wrong variant scanned.</b><div class="vs"><div class="vi x">'+pic(L1,20)+'<div><small>Scanned</small><b>'+L1.it+'</b></div></div><div class="vi">'+pic(L2,20)+'<div><small>Expected</small><b>'+L2.it+'</b></div></div></div>'+L1.sh+' against '+L2.sh+'. Line '+L2.bin+' stays open until '+L2.sh+' is scanned.</div>';
else if(S.c>0){var lc=PICK[S.c-1];s+='<div class="res g in" id="okn"><b>Match.</b> '+lc.it+' confirmed at '+lc.bin+', '+n0(lc.q)+' cases picked.</div>';}
else s+='<div class="res" id="idl">Scan the case to check it against line 1.</div>';
var lg=[];if(S.c>=1)lg.push([L1.bin,L1.bc,'Match','c-ok']);if(S.wrong)lg.push([L2.bin,L1.bc,'Wrong','c-bad']);if(S.c>=2)lg.push([L2.bin,L2.bc,'Match','c-ok']);if(S.c>=3)lg.push([L3.bin,L3.bc,'Match','c-ok']);
s+='<div class="lg"><div class="row h"><span>Bin</span><span>Barcode</span><span>Result</span></div>'+(lg.length?lg.map(function(x){return '<div class="row in"><span class="mono">'+x[0]+'</span><span>'+fbc(x[1])+'</span><span><span class="ch '+x[3]+'">'+x[2]+'</span></span></div>';}).join(''):'<div class="row"><span></span><span class="mut">No scans yet</span><span></span></div>')+'</div></div>';}
$('c2').innerHTML=s;
var d='<div class="ct"><span>Shipment</span>'+(S.op?'<span class="ch c-idle">SO-3110</span>':'')+'</div>';
if(!S.op)d+='<div class="empt"><span>Stock on hand and the shipping documents show here.</span></div>';
else{d+='<div class="sh2"><div class="two in"><div class="kv"><small>Customer</small><b>Greenfield Market</b></div><div class="kv"><small>Ship date</small><b>Nov 20</b></div><div class="kv"><small>Carrier</small><b>Ridgeway Freight</b></div><div class="kv"><small>Dock</small><b>Door 4</b></div></div>';
d+='<div class="oh in"><div class="row h"><span>On hand, cases</span><span>Before</span><span>After</span></div>'+PICK.map(function(l){return '<div class="row"><span>'+l.sh+'</span><span id="o-'+l.sh+'">'+n0(l.oh)+'</span><span id="a-'+l.sh+'" class="'+(S.done?'dn':'mut')+'">'+(S.done?n0(after(l)):'')+'</span></div>';}).join('')+'</div>';
d+='<div class="dcs"><div class="lb"><span>Documents</span><button type="button" class="bt '+(S.gen?'done':'pri')+'" id="gnb"'+(!S.done&&!S.gen?' disabled':'')+'>'+(S.gen?'Generated':'Generate')+'</button></div>';
d+=S.gen?'<div class="doc in" id="d-ps"><svg width="18" height="18" viewBox="0 0 16 16" fill="none" stroke="#166534" stroke-width="1.2"><path d="M4 1.5h5.5L12 4v10.5H4z"/><path d="M6 7h4M6 9.5h4M6 12h2.5"/></svg><div><b>Packing slip PS-3110</b><small>3 lines, '+n0(total())+' cases</small></div></div><div class="doc in" id="d-bol"><svg width="18" height="18" viewBox="0 0 16 16" fill="none" stroke="#166534" stroke-width="1.2"><path d="M1.5 4.5h8v6h-8zM9.5 7h3l2 2v1.5h-5"/><circle cx="4.5" cy="12" r="1.3"/><circle cx="12" cy="12" r="1.3"/></svg><div><b>Bill of lading BOL-3110</b><small>'+n0(total())+' cases to Greenfield Market</small></div></div>':'<div class="dph">Packing slip and bill of lading generate once the pick is complete.</div>';
d+='</div></div>';}
$('c3').innerHTML=d;
$('stp').innerHTML=S.op?'<div class="kv in"><small>Lines confirmed</small><b id="k-ln">'+S.c+' of 3</b></div><div class="kv in"><small>Cases picked</small><b id="k-cs">'+n0(picked())+' of '+n0(total())+'</b></div><div class="kv in"><small>Wrong scans caught</small><b id="k-wr">'+S.wrong+'</b></div><div class="kv in"><small>Documents</small><b id="k-dc">'+(S.gen?2:0)+' of 2</b></div>':'<div class="wait">Lines confirmed, cases picked and wrong scans caught show here.</div>';
}
function resetState(){S={op:false,c:0,wrong:0,done:false,gen:false};render();}
function finish(){if(S.c<3){S.c=3;}S.done=true;render();}
winEl.addEventListener('click',function(e){var t=e.target.closest&&e.target.closest('#scb');if(t&&mode==='try'&&cur===3&&S.c>=1&&S.c<3&&S.wrong){scan();render();}});
function capN(){var i=cap.querySelector('.m i');return i?+i.textContent:1;}
var CAPAT=function(hh){var w=cap.offsetWidth;return capN()>=4?{l:16,t:58}:{l:visW()-w-14,t:58};};
var ST=[
{id:'op',target:function(){return $('opb');},prompt:'Open the pick list',where:'below',run:function(){S.op=true;render();},
 after:function(){return['A pick list in bin order','SO-3110: '+PICK.map(function(l){return l.bin;}).join(', ')+', '+n0(total())+' cases in all.'];}},
{id:'s1',target:function(){return $('scb');},prompt:'Scan item for '+L1.bin,where:'below',run:function(){S.op=true;if(S.c<1)S.c=1;render();},
 after:function(){return['Right item, line confirmed',L1.it+' matches '+L1.bin+'. '+n0(L1.q)+' cases picked.'];}},
{id:'s2',target:function(){return $('scb');},prompt:'Scan item for '+L2.bin,where:'below',run:function(){S.wrong=1;render();},
 after:function(){return['A similar variant, caught',L1.sh+' scanned for the '+L2.sh+' line. '+L2.bin+' stays open until the right case is scanned.'];}},
{id:'cp',target:function(){if(mode==='watch'&&S.wrong&&S.c===1){S.c=2;render();later(function(){if(S.c===2){S.c=3;render();}},450);}return $('cpb');},
 back:function(){return S.c<3?[$('scb'),S.c===1?'Scan the '+L2.sh+' case':'Scan the '+L3.sh+' case','below']:null;},prompt:'Complete the pick',where:'above',run:function(){finish();},
 after:function(){return['Pick complete, stock updated',n0(total())+' cases picked. On hand: '+PICK.map(function(l){return l.sh+' '+n0(l.oh)+' to '+n0(after(l));}).join(', ')+'.'];}},
{id:'gen',target:function(){return $('gnb');},prompt:'Generate the documents',where:'above',run:function(){S.gen=true;render();},
 after:function(){return['Packing slip and bill of lading','PS-3110 and BOL-3110 for '+n0(total())+' cases, ready to print.'];}}];
'''
