"""Nut processing card 4: Allergen Segregation & Scheduling. Layout: a board.
Top: the read only line field with Open week. Middle: the week board for Line 1, one day column per run, with the
changeover cleaning minutes between the columns and the week's cleaning total. Bottom left: the move preview (the
proposed order, its cleaning and the extra minutes, shown before anything is committed). Bottom right: the changeover
cleaning record with the read only sign off field. A run stays blocked until the cleaning before it is signed.
Cleaning minutes come from the changeover table below, never typed in."""
from frame_auto import header

SUMMARY = 'Allergen Segregation & Scheduling (Line 1 week R1 free from, R3 tree nut, R4 free from, R2 peanut: cleaning 30 + 45 + 60 = 135 minutes, moving the peanut run after R1 gives 60 + 120 + 45 = 225, 90 more, the cleaning sign off unblocks R3 and R4 stays blocked)'
ARIA = 'Interactive product screen: open the week schedule for a line, see the allergen group of every run, move a peanut run and see the extra cleaning it adds before committing, record a changeover cleaning with a sign off and see a run blocked until the cleaning before it is signed'
STEPS = 5
STUDIO = dict(lede='A typical line schedule on your Sutton data. Want it different? Describe the change.',
              examples=['Cleaning times by line', 'A swab photo on every sign off', 'Sesame as its own group', 'A daily changeover report'],
              built_on='Work orders, lines, items and cleaning records', change='Groups, times and views')

ICON = '<rect x="2" y="3" width="12" height="11" rx="1.5"/><path d="M2 6.5h12M5.5 1.8v2.4M10.5 1.8v2.4"/>'

CSS = (
 '.fld input[readonly]{background:#F4F4F5;color:#3F3F46;cursor:default;pointer-events:none}'
 '.g4{display:grid;grid-template-columns:316px 330px;grid-template-rows:60px 214px 246px;gap:10px;padding:10px 44px 0 16px;width:716px}'
 '.top{grid-column:1/3;display:flex;flex-direction:column;justify-content:center;gap:5px;padding:0 12px}.top .frm{display:flex;align-items:flex-end;gap:8px}.top .fld{width:110px}.top .ctx{font-size:8.9px;color:#71717A}.top .rs{margin-left:auto;display:flex;gap:6px}'
 '.bd{grid-column:1/3;display:flex;flex-direction:column}.bd>.empt{margin:9px;flex:1;padding:8px}.ct .bt{font-size:9px;padding:2px 9px}.ct .r3{display:flex;gap:6px;align-items:center}'
 '.wk{display:grid;grid-template-columns:1fr 34px 1fr 34px 1fr 34px 1fr;padding:8px 9px;flex:1}'
 '.dc{display:flex;flex-direction:column;gap:5px;min-width:0}.dc .dy{font-size:9px;color:#71717A;display:flex;justify-content:space-between;padding:0 2px}.dc .dy b{color:#18181B;font-weight:600}'
 '.rn{border:1px solid #E4E4E7;border-radius:8px;padding:7px 8px;display:flex;flex-direction:column;gap:4px;flex:1;background:#fff;transition:background-color .35s,border-color .35s,box-shadow .35s}'
 '.rn .t1{display:flex;justify-content:space-between;align-items:center}.rn .t1 b{font-family:"JetBrains Mono",ui-monospace,monospace;font-size:11px}.rn .nm{font-size:9.6px;font-weight:600;line-height:1.3}.rn .mt{font-size:8.4px;color:#71717A;line-height:1.35}'
 '.rn .ag{min-height:18px}.rn .ft{margin-top:auto;display:flex;flex-direction:column;gap:4px}.rn .ft .bt{font-size:9px;padding:3px 8px;width:100%}.rn .ft .bt:disabled{opacity:.45;cursor:not-allowed}.rn .bk{font-size:8.3px;color:#991B1B;line-height:1.3}'
 '.rn.g-F{box-shadow:inset 0 3px 0 #16A34A}.rn.g-T{box-shadow:inset 0 3px 0 #D97706}.rn.g-P{box-shadow:inset 0 3px 0 #DC2626}.rn.mv{border-style:dashed;border-color:#DC2626}.rn.run{background:#F0FDF4;border-color:#BBF7D0}'
 '.g-c{display:inline-flex}.ag .ch.F{background:#DCFCE7;color:#166534}.ag .ch.T{background:#FEF3C7;color:#92400E}.ag .ch.P{background:#FEE2E2;color:#B91C1C}'
 '.gt{display:flex;flex-direction:column;align-items:center;justify-content:center;gap:4px;color:#A1A1AA}.gt svg{width:10px;height:10px}.gt .cm{writing-mode:vertical-rl;transform:rotate(180deg);font-size:8.6px;font-family:"JetBrains Mono",ui-monospace,monospace;color:#52525B;border:1px solid #E4E4E7;border-radius:6px;padding:6px 2px;background:#FAFAFA;white-space:nowrap}.gt .cm.ok{background:#F0FDF4;border-color:#BBF7D0;color:#166534}'
 '.pv,.cl{display:flex;flex-direction:column}.pv>.empt,.cl>.empt{margin:9px;flex:1;padding:8px}'
 '.po{padding:8px 11px 0;display:flex;flex-direction:column;gap:6px}.po .lb{font-size:8.6px;color:#71717A;display:flex;justify-content:space-between}.po .lb b{font-family:"JetBrains Mono",ui-monospace,monospace;color:#18181B;font-size:9.4px}'
 '.seq{display:flex;align-items:center;gap:3px;flex-wrap:nowrap}.seq .rc{border-radius:5px;padding:2px 6px;font-family:"JetBrains Mono",ui-monospace,monospace;font-size:9px;font-weight:600}.seq .rc.F{background:#DCFCE7;color:#166534}.seq .rc.T{background:#FEF3C7;color:#92400E}.seq .rc.P{background:#FEE2E2;color:#B91C1C}.seq .m{font-size:8.2px;color:#71717A;font-family:"JetBrains Mono",ui-monospace,monospace}'
 '.dlt{margin:8px 11px 0;display:grid;grid-template-columns:1fr 1fr 1fr;gap:6px}.dlt div{border:1px solid #E4E4E7;border-radius:7px;padding:4px 7px}.dlt div.w{border-color:#FECACA;background:#FEF2F2;color:#991B1B}.dlt small{display:block;font-size:8.2px;color:#71717A}.dlt b{font-family:"JetBrains Mono",ui-monospace,monospace;font-size:11.5px}'
 '.ck{padding:7px 11px 0;display:flex;flex-direction:column;gap:3px}.ck div{display:flex;justify-content:space-between;align-items:center;font-size:9px;color:#3F3F46}'
 '.so{display:flex;align-items:flex-end;gap:8px;padding:7px 11px 0}.so .fld{width:110px}.so .ctx{font-size:8.5px;color:#71717A;padding-bottom:6px}.so .rt{margin-left:auto}'
 '.note{margin:7px 11px 0;padding:5px 8px;border-radius:7px;font-size:8.8px;line-height:1.4;background:#FAFAFA;border:1px solid #F0F0F1;color:#52525B}.note.w{background:#FEF2F2;border-color:#FECACA;color:#991B1B}.note.g{background:#F0FDF4;border-color:#BBF7D0;color:#166534}'
 '.tot{margin-top:auto;padding:7px 11px;border-top:1px solid #E4E4E7;font-size:9px;color:#52525B;line-height:1.4;background:#FAFAFA}.cl .tot{padding-right:90px}'
)

WIN = (
 header(ICON, 'Line schedule', 'Runs by allergen group with changeover cleaning')
 + '<div class="g4"><div class="cd top"><div class="frm"><label class="fld"><small>Line</small>'
 '<input id="iln" value="Line 1" readonly tabindex="-1" autocomplete="off" spellcheck="false"></label>'
 '<button type="button" class="bt pri" id="owb">Open week</button><span class="rs" id="rs"></span></div><div class="ctx">Roasting and packing line, week of Nov 23</div></div>'
 '<div class="cd bd" id="bd"></div><div class="cd pv" id="pv2"></div><div class="cd cl" id="cl"></div></div>'
)

JS = r'''
var FOC='.hd>*,.top .fld,.top .ctx,#owb,.bd .ct,.bd .dc,.bd .gt,.bd>.empt,.pv .ct,.pv>*:not(.ct),.cl .ct,.cl>*:not(.ct)';
var GN={F:'Free from',T:'Tree nut',P:'Peanut'};
var CLEAN={FF:15,FT:30,TF:45,FP:60,PF:120,PT:120,TP:45};
var RUNS={R1:{g:'F',nm:'Seed and fruit mix',q:'1,800 cases',h:'6 h',b:'BOM SF-12'},R2:{g:'P',nm:'Honey roasted peanuts',q:'2,400 cases',h:'8 h',b:'BOM PN-04'},R3:{g:'T',nm:'Roasted almonds, 16 oz',q:'2,000 cases',h:'7 h',b:'BOM AL-16'},R4:{g:'F',nm:'Pumpkin seed snack',q:'1,500 cases',h:'5 h',b:'BOM PS-08'}};
var CUR=['R1','R3','R4','R2'],NEW=['R1','R2','R3','R4'],DAYS=['Mon Nov 23','Tue Nov 24','Wed Nov 25','Thu Nov 26'];
var S;
function cm(a,b){return CLEAN[RUNS[a].g+RUNS[b].g];}
function legs(o){var r=[];for(var i=1;i<o.length;i++)r.push(cm(o[i-1],o[i]));return r;}
function sum(o){return legs(o).reduce(function(a,b){return a+b;},0);}
function seq(o){var l=legs(o);return '<div class="seq">'+o.map(function(id,i){return (i?'<span class="m">'+l[i-1]+'</span>':'')+'<span class="rc '+RUNS[id].g+'">'+id+'</span>';}).join('')+'</div>';}
var ARR='<svg viewBox="0 0 10 10" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"><path d="M2 5h6M5.5 2.5L8 5 5.5 7.5"/></svg>';
function card(id,i){var R=RUNS[id],st,bk='';
if(i===0)st='<span class="ch c-ok">Done</span>';
else if(id==='R3')st=S.go?'<span class="ch c-ok" id="r3s">Running</span>':(S.so?'<span class="ch c-info" id="r3s">Ready</span>':'<span class="ch c-bad" id="r3s">Blocked</span>');
else if(id==='R4'&&S.go)st='<span class="ch c-bad" id="r4s">Blocked</span>';
else st='<span class="ch c-idle">Waiting</span>';
if(S.ag&&id==='R3'&&!S.so)bk='<div class="bk">Waits for the R1 to R3 cleaning sign off</div>';
if(S.go&&id==='R4')bk='<div class="bk" id="r4b">Waits for the R3 to R4 cleaning sign off</div>';
var ft='';
if(id==='R3'&&S.ag)ft='<button type="button" class="bt '+(S.go?'done':'pri')+'" id="r3b"'+(S.so?'':' disabled')+'>'+(S.go?'Started':'Start run')+'</button>';
if(id==='R2'&&S.ag)ft='<button type="button" class="bt '+(S.mv?'done':'')+'" id="mvb">'+(S.mv?'Preview open':'Move after R1')+'</button>';
return '<div class="dc in"><div class="dy"><b>'+DAYS[i].slice(0,3)+'</b><span>'+DAYS[i].slice(4)+'</span></div><div class="rn'+(S.ag?' g-'+R.g:'')+(S.mv&&id==='R2'?' mv':'')+(S.go&&id==='R3'?' run':'')+'" id="c-'+id+'"><div class="t1"><b>'+id+'</b>'+st+'</div><div class="nm">'+R.nm+'</div><div class="mt">'+R.q+', '+R.h+'<br>'+R.b+'</div>'+
'<div class="ag">'+(S.ag?'<span class="ch '+R.g+'" id="g-'+id+'">'+GN[R.g]+'</span>':'')+'</div><div class="ft">'+bk+ft+'</div></div></div>';}
function render(){
$('owb').className='bt '+(S.op?'done':'pri');$('owb').textContent=S.op?'Opened':'Open week';
$('rs').innerHTML=S.op?'<span class="ch c-idle">4 runs</span>':'';
var l=legs(CUR);
var b='<div class="ct"><span>Line 1, week of Nov 23</span>'+(S.op?'<span class="r3">'+(S.ag?'<span class="ch c-idle mono" id="ctot">Cleaning '+sum(CUR)+' min</span>':'')+'<button type="button" class="bt '+(S.ag?'done':'pri')+'" id="agb">'+(S.ag?'Groups shown':'Show allergen groups')+'</button></span>':'')+'</div>';
if(!S.op)b+='<div class="empt"><b>No schedule open</b><span>Open a line to see its runs for the week, in order.</span></div>';
else{b+='<div class="wk">'+CUR.map(function(id,i){return (i?'<div class="gt in"><span>'+ARR+'</span>'+(S.ag?'<span class="cm'+(i===1&&S.so?' ok':'')+'" id="cm'+i+'">'+l[i-1]+' min clean</span>':'')+'</div>':'')+card(id,i);}).join('')+'</div>';}
$('bd').innerHTML=b;
var p='<div class="ct"><span>Move preview</span>'+(S.mv?'<span class="ch c-warn">Not committed</span>':'')+'</div>';
if(!S.mv)p+='<div class="empt"><b>No move in preview</b><span>Move a run to see the cleaning it adds before anything changes.</span></div>';
else{p+='<div class="po in"><div class="lb"><span>Current order</span><b id="pcur">'+sum(CUR)+' min</b></div>'+seq(CUR)+'<div class="lb"><span>With R2 after R1</span><b id="pnew">'+sum(NEW)+' min</b></div>'+seq(NEW)+'</div>'+
'<div class="dlt in"><div><small>Now</small><b>'+sum(CUR)+'</b></div><div><small>After the move</small><b>'+sum(NEW)+'</b></div><div class="w"><small>Extra cleaning</small><b id="pext">+'+(sum(NEW)-sum(CUR))+' min</b></div></div>';}
p+='<div class="tot">'+(S.mv?'Current order kept until you commit a move.':'Cleaning minutes come from the changeover table.')+'</div>';
$('pv2').innerHTML=p;
var c='<div class="ct"><span>Changeover cleaning</span>'+(S.ag?'<span class="ch '+(S.so?'c-ok':'c-warn')+'" id="cst">'+(S.so?'Signed':'Not signed')+'</span>':'')+'</div>';
if(!S.ag)c+='<div class="empt"><b>No changeover selected</b><span>Cleaning between allergen groups is recorded and signed here.</span></div>';
else{c+='<div class="ck in"><div><b style="font-size:9.4px">R1 to R3, free from to tree nut</b><span class="mono">'+cm('R1','R3')+' min</span></div><div><span>Dry clean and vacuum</span><span class="ch c-ok">Done</span></div><div><span>Wet wash and sanitize</span><span class="ch c-ok">Done</span></div><div><span>Swab test</span><span class="ch c-ok">Pass</span></div></div>'+
'<div class="so in"><label class="fld"><small>Signed by</small><input id="isb" value="D. Moreno" readonly tabindex="-1"></label><button type="button" class="bt '+(S.so?'done':'pri')+'" id="sob">'+(S.so?'Signed off':'Sign off')+'</button><span class="ctx">Sanitation lead, shift 2</span></div>';
if(S.go)c+='<div class="note w in" id="nnt">Next: R3 to R4, tree nut to free from, '+cm('R3','R4')+' min. R4 is blocked until it is signed.</div>';
else if(S.so)c+='<div class="note g in" id="snt">Signed 2:40 pm. R3 can start.</div>';}
c+='<div class="tot">No run starts before its cleaning is signed.</div>';
$('cl').innerHTML=c;
}
function resetState(){S={op:false,ag:false,mv:false,so:false,go:false};render();}
var ST=[
{id:'op',target:function(){return $('owb');},prompt:'Open the Line 1 week',where:'below',run:function(){S.op=true;render();},
 after:function(){return['A week schedule by line','Line 1 runs R1, R3, R4 and R2 from Monday to Thursday.'];}},
{id:'ag',target:function(){return $('agb');},prompt:'Show allergen groups',where:'below',run:function(){S.ag=true;render();},
 after:function(){var l=legs(CUR);return['The allergen group of every run','Free from, tree nut, free from, peanut: '+l.join(' + ')+' = '+sum(CUR)+' minutes of cleaning.'];}},
{id:'mv',target:function(){return $('mvb');},prompt:'Move the peanut run after R1',where:'above',run:function(){S.mv=true;render();},
 after:function(){var l=legs(NEW);return['A move shows its extra cleaning first','R1, R2, R3, R4: '+l.join(' + ')+' = '+sum(NEW)+' minutes, '+(sum(NEW)-sum(CUR))+' more, before you commit.'];}},
{id:'so',target:function(){return $('sob');},prompt:'Sign off the cleaning',where:'above',run:function(){S.so=true;render();},
 after:function(){return['A changeover cleaning with a sign off','The R1 to R3 cleaning is recorded and signed by D. Moreno.'];}},
{id:'go',target:function(){return $('r3b');},prompt:'Start run R3',where:'below',run:function(){S.go=true;render();},
 after:function(){return['A run waits for the cleaning before it','R3 starts now that its cleaning is signed. R4 stays blocked until the next one is.'];}}];
'''
