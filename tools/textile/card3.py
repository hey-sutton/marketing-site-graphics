"""Textile card 3: Cutting & Yield Verification. Layout: split view with bars.
Left, cutting order CO-771, the scan panel and the lay list with the yards used. Right, a horizontal length bar for the
roll that segments into lays, waste and remnant as lays are confirmed, and a small consumption table.
Scan the wrong dye lot first (rejected, no bar), then R-48214, confirm three lays, record 109 yd used.
Every figure comes from tools/textile/data.py, where the brief's sums are asserted."""
import data as D
from frame_textile import header

SUMMARY = 'Cutting & Yield Verification (scan a roll at the cut table, block the wrong dye lot, confirm three lays, record yards used, waste and remnant)'
ARIA = 'Interactive demo: scan a roll at the cut table, confirm lays and record yardage used and remnant.'
STEPS = 4
STUDIO = dict(lede='A typical cut table screen, built on your Sutton data with Studio. Want it different? Describe the change.',
              examples=['Width based allocation of rolls', 'A marker efficiency field', 'A second scan from the cutter', 'Remnants sent to a sale bin'],
              built_on='Cutting orders, rolls and serialized inventory', change='Checks, fields and tolerances')

ICON = '<circle cx="4" cy="4.2" r="2"/><circle cx="4" cy="11.8" r="2"/><path d="M5.6 5.4L14 12M5.6 10.6L14 4"/>'

CSS = (
 '.g3{padding:10px 0 0 16px;display:grid;grid-template-columns:252px 394px;gap:10px;width:672px;height:546px}'
 '.col{display:flex;flex-direction:column;gap:10px;min-width:0;height:100%}'
 '.co{height:118px;flex:none}.kg{display:grid;grid-template-columns:1fr 1fr;gap:6px 10px;padding:8px 11px}.kg .kv b{font-size:9.8px}'
 '.sc{height:124px;flex:none;display:flex;flex-direction:column}.scr{display:flex;align-items:center;gap:6px;padding:8px 11px 0}.scr .fld{flex:1;position:relative}.scr .fld input{font-size:10.4px;padding:6px 8px}'
 '.scr .fld .em{position:absolute;left:0;top:30px;white-space:nowrap}.smp{display:flex;align-items:center;gap:5px;padding:6px 11px 0;font-size:9px;color:#71717A}.smp .bt{font-family:"JetBrains Mono",ui-monospace,monospace;font-size:9.2px;padding:3px 8px}'
 '.chk{margin:7px 11px 0;display:flex;align-items:center;gap:6px;font-size:9.2px;border-radius:6px;padding:5px 8px;line-height:1.3}.chk svg{flex:none}'
 '.chk.bad{background:#FEF2F2;color:#991B1B;border:1px solid #FECACA}.chk.ok{background:#F0FDF4;color:#166534;border:1px solid #BBF7D0}.chk.idle{color:#71717A;border:1px dashed #E4E4E7}'
 '.ly{flex:1;display:flex;flex-direction:column;min-height:0}.ly .row{grid-template-columns:44px 1fr 46px 66px;font-size:9.4px;min-height:27px}'
 '.ly .ac{padding:7px 11px;border-top:1px solid #F0F0F1;display:flex;align-items:center;gap:6px}'
 '.ur{display:flex;align-items:flex-end;gap:6px;padding:8px 11px;border-top:1px solid #F0F0F1}.ur .fld{width:74px;position:relative}.ur .fld .em{position:absolute;top:-13px;left:0;white-space:nowrap}.ur .mut{font-size:8.8px;padding-bottom:5px}'
 '.rmn{margin:auto 11px 10px;border:1px dashed #D4D4D8;border-radius:6px;padding:6px 9px;display:grid;grid-template-columns:1fr auto;gap:4px 8px;align-items:center}'
 '.rmn .bcd{grid-column:1/3;width:100%;height:18px;fill:#18181B}.rmn .lid{font-size:12px;font-weight:600}.rmn small{grid-column:1/3;font-size:8.4px;color:#71717A}'
 '.nts{margin:auto 11px 10px;padding:7px 9px;border-radius:6px;background:#FAFAFA;border:1px solid #F0F0F1;font-size:8.8px;color:#52525B;line-height:1.4;display:flex;flex-direction:column;gap:2px}.nts b{font-size:9.2px;color:#18181B;font-weight:600}'
 '.ch.lot{font-family:"JetBrains Mono",ui-monospace,monospace;font-size:9px}'
 '.rb{height:250px;flex:none;display:flex;flex-direction:column}.rbh{display:flex;align-items:center;gap:8px;padding:8px 11px 0;font-size:9.4px;color:#52525B}.rbh b{font-family:"JetBrains Mono",ui-monospace,monospace;color:#18181B;font-size:11px}'
 '.bar{position:relative;margin:14px 11px 0;height:44px;border-radius:6px;background:#F4F4F5;border:1px solid #E4E4E7;overflow:hidden;display:flex}'
 '.sg{height:100%;display:flex;align-items:center;justify-content:center;font-size:8.6px;font-weight:600;color:#fff;white-space:nowrap;overflow:hidden;transition:width .5s cubic-bezier(.22,.9,.28,1);border-right:1px solid rgba(255,255,255,.7);box-sizing:border-box}'
 '.sg.l1{background:#1E3A8A}.sg.l2{background:#2B4C9E}.sg.l3{background:#3B5FB3}.sg.ws{background:#DC2626;border-right:0}.sg.rm{background:repeating-linear-gradient(135deg,#BBF7D0 0 4px,#DCFCE7 4px 8px);color:#166534}'
 '.sg.pl{background:repeating-linear-gradient(135deg,#E0E7FF 0 4px,#EEF2FF 4px 8px);color:#3730A3;border-right:1px dashed #A5B4FC}'
 '.tks{position:relative;height:18px;margin:3px 11px 0}.tk{position:absolute;top:0;font-family:"JetBrains Mono",ui-monospace,monospace;font-size:8.2px;color:#71717A;transform:translateX(-50%)}.tk::before{content:"";position:absolute;left:50%;top:-3px;height:3px;border-left:1px solid #D4D4D8}'
 '.lgd2{display:flex;flex-wrap:wrap;gap:6px 12px;padding:4px 11px 0;font-size:8.6px;color:#52525B}.lgd2 span{display:inline-flex;align-items:center;gap:4px}.lgd2 i{width:10px;height:8px;border-radius:2px;display:inline-block}'
 '.tri{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;margin:auto 11px 10px}.tri div{border:1px solid #F0F0F1;border-radius:7px;background:#FAFAFA;padding:6px 9px;display:flex;flex-direction:column;gap:2px}.tri small{font-size:8.6px;color:#71717A}.tri b{font-size:14px;font-weight:600}'
 '.rb .empt,.cs .empt{margin:10px;flex:1}.rb .empt.bad{border-color:#FECACA;background:#FEF2F2;color:#991B1B}.rb .empt.bad b{color:#991B1B}'
 '.cs{flex:1;display:flex;flex-direction:column;min-height:0}.cs .row{grid-template-columns:1fr 70px 1fr;font-size:9.4px;min-height:26px}'
 '.flg{margin-top:auto;padding:8px 11px 10px;border-top:1px solid #F0F0F1;display:flex;align-items:center;gap:8px;font-size:9px;color:#52525B;white-space:nowrap}'
)

WIN = (
 header(ICON, 'Cut table', 'Cutting, roll goods')
 + '<div class="g3"><div class="col"><div class="cd co" id="co"><div class="ct"><span>Cutting order CO-771</span><span class="ch c-info">Released</span></div><div class="kg">'
 '<span class="kv"><small>Item</small><b class="mono">TW-5810</b></span><span class="kv"><small>Needs dye lot</small><b class="mono">' + D.LOT + '</b></span>'
 '<span class="kv"><small>Lays</small><b class="mono">' + str(D.LAYS) + ' of ' + str(D.LAY_YD) + ' yd</b></span><span class="kv"><small>For</small><b>Pell Street Furnishings</b></span></div></div>'
 '<div class="cd sc frm" id="sc"><div class="ct"><span>Scan roll</span><span class="mut" style="font-weight:400;font-size:9px">Cut table 2</span></div><div class="scr"><label class="fld" id="fsc"><input id="sin" value="" placeholder="Scan or type a roll ID" autocomplete="off" spellcheck="false" aria-label="Roll ID">'
 '<span class="em" id="sem">No roll found. Try R-48214</span></label><button type="button" class="bt pri" id="scn">Scan</button></div>'
 '<div class="smp">Sample<button type="button" class="bt" data-sample data-v="R-48214">R-48214</button><button type="button" class="bt" data-sample data-v="R-48330">R-48330</button></div><div id="chk"></div></div>'
 '<div class="cd ly" id="ly"></div></div>'
 '<div class="col"><div class="cd rb" id="rb"></div><div class="cd cs" id="cs"></div></div></div>'
)

JS = r'''
var FOC='.hd>*,.co,.sc .ct,.scr>*,.smp,.chk,.ly .ct,.ly .row,.ly .ac>*,.ur>*,.rmn,.rb .ct,.rbh,.bar,.tks,.lgd2,.tri,.cs .ct,.cs .row,.flg>*';
var NEED='@LOT@',LAYS=@LAYS@,LYD=@LYD@,USED=@USED@,TOLP=1.5;
var RL={'R-48214':['@LOT@',119],'R-48211':['@LOT@',120],'R-48212':['@LOT@',118],'R-48213':['@LOT@',122],'R-48215':['@LOT@',121],'R-48330':['DL-2611-C',124]};
var S;
function plan(){return LAYS*LYD;}
function tol(){return plan()*TOLP/100;}
function bars(id){var x=0,s='';for(var i=0;i<id.length;i++){var c=id.charCodeAt(i)*7+i*3;for(var k=0;k<4;k++){var w=1+((c>>k)&1)+((c>>(k+4))&1);s+='<rect x="'+x+'" y="0" width="'+w+'" height="18"/>';x+=w+1+((c>>(k+2))&1);}}
return '<svg class="bcd" viewBox="0 0 '+x+' 18" preserveAspectRatio="none" aria-hidden="true">'+s+'</svg>';}
var OK='<svg width="12" height="12" viewBox="0 0 12 12" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M2.5 6.3l2.3 2.2 4.7-5"/></svg>',
NO='<svg width="12" height="12" viewBox="0 0 12 12" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"><path d="M3 3l6 6M9 3l-6 6"/></svg>';
function render(){
var k='';if(S.bad)k='<div class="chk bad in" id="ck">'+NO+'<span><b>Wrong dye lot.</b> This order needs '+NEED+'. '+S.bad+' is '+RL[S.bad][0]+'.</span></div>';
else if(S.roll)k='<div class="chk ok in" id="ck">'+OK+'<span><b>'+S.roll+' accepted.</b> '+NEED+', '+RL[S.roll][1]+' yd.</span></div>';
else k='<div class="chk idle">Every roll is checked against the order’s dye lot.</div>';
$('chk').innerHTML=k;
var y='<div class="ct"><span>Lays</span><span class="ch '+(S.lays?'c-ok':'c-idle')+'">'+(S.lays?LAYS+' of '+LAYS+' confirmed':'0 of '+LAYS+' confirmed')+'</span></div><div class="row h"><span>Lay</span><span>Marker</span><span class="r">Yards</span><span>Status</span></div>';
for(var i=1;i<=LAYS;i++)y+='<div class="row"><span class="mono">'+i+'</span><span class="mono">MK-771-'+i+'</span><span class="mono r">'+LYD+' yd</span><span><span class="ch '+(S.lays?'c-ok':'c-idle')+'">'+(S.lays?'Confirmed':'Planned')+'</span></span></div>';
if(!S.lays)y+='<div class="ac"><button type="button" class="bt pri" id="cfl"'+(S.roll?'':' disabled')+'>Confirm lays 1 to '+LAYS+'</button><span class="mut" style="font-size:8.8px">'+(S.roll?'On roll '+S.roll:'Scan a '+NEED+' roll first')+'</span></div>';
else if(!S.rec)y+='<div class="ur frm" id="urf"><label class="fld" id="fus"><small>Used yd</small><input id="uin" value="'+(S.uv||'')+'" inputmode="numeric" autocomplete="off" aria-label="Yards used"><span class="em" id="uem">Enter '+plan()+' to '+RL[S.roll][1]+'</span></label><button type="button" class="bt pri" id="rec">Record</button><span class="mut">Measured off the roll</span></div>';
else y+='<div class="ur"><span class="ch c-ok">Recorded</span><span class="mut">'+S.used+' yd used on '+S.roll+'</span></div>';
if(!S.rec)y+='<div class="nts"><b>Spreading notes</b><span>Face up, nap one way. Splice only at lay ends. Any remnant over 5 yd gets its own label and goes back to stock.</span></div>';
if(S.rec&&rem()>0)y+='<div class="rmn in" id="rmn">'+bars(S.roll+'-R1')+'<span class="lid mono">'+S.roll+'-R1</span><span class="ch lot c-info">'+NEED+'</span><small>Remnant label, '+rem()+' yd, back to stock in bin C-07</small></div>';
$('ly').innerHTML=y;
var b='<div class="ct"><span>Roll length</span>'+(S.roll?'<span class="ch lot c-info">'+NEED+'</span>':'')+'</div>';
if(S.bad&&!S.roll)b+='<div class="empt bad"><b>'+S.bad+' rejected</b><span>Wrong dye lot, so no bar is drawn and nothing is cut from it.</span></div>';
else if(!S.roll)b+='<div class="empt"><b>No roll scanned</b><span>Scan a roll to draw its length and plan the lays on it.</span></div>';
else{var L=RL[S.roll][1],W=370,px=function(v){return (v*W/L).toFixed(1)+'px';},sg='';
for(var i=1;i<=LAYS;i++)sg+='<span class="sg '+(S.lays?'l'+i:'pl')+'" style="width:'+px(LYD)+';transition-delay:'+(i*120)+'ms">Lay '+i+'</span>';
if(S.rec){if(waste()>0)sg+='<span class="sg ws" style="width:'+px(waste())+'" title="Waste"></span>';if(rem()>0)sg+='<span class="sg rm" style="width:'+px(rem())+'">'+rem()+'</span>';}
b+='<div class="rbh"><b>'+S.roll+'</b><span>'+L+' yd, 58 in</span><span class="grow"></span><span id="rbs">'+(S.rec?S.used+' yd used, '+rem()+' yd left':S.lays?plan()+' yd planned':'Nothing cut yet')+'</span></div>';
b+='<div class="bar" id="bar">'+sg+'</div><div class="tks">'+[0,LYD,2*LYD].concat(S.rec?[S.used]:[3*LYD]).concat([L]).filter(function(v,i,a){return a.indexOf(v)===i;}).map(function(v){return '<span class="tk" style="left:'+(v*W/L)+'px">'+v+'</span>';}).join('')+'</div>';
b+='<div class="lgd2"><span><i style="background:#1E3A8A"></i>Lays</span><span><i style="background:#DC2626"></i>Waste</span><span><i style="background:#BBF7D0"></i>Remnant</span><span><i style="background:#F4F4F5;border:1px solid #E4E4E7"></i>Uncut</span></div>';
b+='<div class="tri"><div><small>Planned</small><b class="mono" id="tp">'+(S.lays?plan()+' yd':'')+'</b></div><div><small>Used</small><b class="mono" id="tu">'+(S.rec?S.used+' yd':'')+'</b></div><div><small>Remnant</small><b class="mono" id="tr">'+(S.rec?rem()+' yd':'')+'</b></div></div>';}
$('rb').innerHTML=b;
var c='<div class="ct"><span>Consumption, CO-771</span>'+(S.rec?'<span class="ch '+(waste()<=tol()?'c-ok':'c-bad')+'">'+(waste()<=tol()?'Within tolerance':'Over tolerance')+'</span>':'')+'</div>';
if(!S.lays)c+='<div class="empt"><b>No lays confirmed</b><span>Planned and actual yards fill in as the lays are confirmed and the roll is measured.</span></div>';
else{var R=[['Planned',plan()+' yd',LAYS+' lays of '+LYD+' yd','u-pl'],['Actual',S.rec?S.used+' yd':'','Measured off '+S.roll,'u-ac'],['Variance',S.rec?(waste()>=0?'+':'−')+Math.abs(waste())+' yd':'',S.rec?'Waste, ends and splices':'','u-va'],
['Remnant',S.rec?rem()+' yd':'',S.rec?S.roll+'-R1 in stock, '+NEED:'','u-rm'],['Tolerance',tol().toFixed(2)+' yd',TOLP+'% of planned','u-tl']];
c+='<div class="row h"><span>Measure</span><span class="r">Yards</span><span>Note</span></div>'+R.map(function(r){return '<div class="row"><span>'+r[0]+'</span><span class="mono r" id="'+r[3]+'">'+r[1]+'</span><span class="mut">'+r[2]+'</span></div>';}).join('');
c+='<div class="flg">'+(S.rec?'<span class="ch '+(waste()<=tol()?'c-ok':'c-bad')+'" id="flg">'+(waste()<=tol()?'Within tolerance':'Over tolerance')+'</span><span>'+Math.abs(waste())+' yd against '+tol().toFixed(2)+' allowed</span>':'<span class="mut">Record the yards used to check the tolerance.</span>')+'</div>';}
$('cs').innerHTML=c;}
function waste(){return S.used-plan();}
function rem(){return RL[S.roll][1]-S.used;}
function norm(v){v=String(v).trim().toUpperCase().replace(/\s/g,'');if(/^R?\d{5}$/.test(v))v='R-'+v.replace(/^R/,'');return v;}
function uVal(){var v=String($('uin').value).replace(/[,\s]/g,'');return /^\d+$/.test(v)?+v:NaN;}
[].forEach.call(root.querySelectorAll('[data-sample]'),function(b){b.addEventListener('click',function(){$('sin').value=b.getAttribute('data-v');$('fsc').classList.remove('err');});});
$('ly').addEventListener('input',function(e){if(e.target&&e.target.id==='uin')S.uv=e.target.value;});
function typeIn(inp,t,done){var i=0;(function k(){inp.value=t.slice(0,i);if(i<t.length){i++;later(k,60);}else done();})();}
function setScan(v){if(RL[v][0]===NEED){S.roll=v;S.bad=null;}else{S.bad=v;S.roll=null;}}
function scanned(v){$('fsc').classList.remove('err');setScan(v);render();}
function resetState(){S={roll:null,bad:null,lays:false,rec:false,used:0,uv:''};$('sin').value='';$('fsc').classList.remove('err');render();}
var CAPAT=function(hh){return cur<2?{l:290,t:410}:{l:14,t:196};};
var ST=[
{id:'bad',target:function(){return mode==='try'?$('scn'):$('sin');},prompt:'Scan R-48330 or pick a sample',where:'below',
 ok:function(){var v=norm($('sin').value),b=!RL[v];$('sem').textContent=v?'No roll found. Try R-48330':'Enter a roll ID, for example R-48330';$('fsc').classList.toggle('err',b);return !b;},
 run:function(quick){var v=mode==='try'&&RL[norm($('sin').value)]?norm($('sin').value):'R-48330';setScan(v);var go=function(){$('sin').value=v;scanned(v);if(S.bad)$('sin').value='R-48214';};if(mode==='watch'&&!quick)typeIn($('sin'),v,go);else go();},
 after:function(){return S.bad?['Scan the roll at the cut table','Wrong dye lot. This order needs '+NEED+', and '+S.bad+' is '+RL[S.bad][0]+'.']:['Scan the roll at the cut table',S.roll+' matches '+NEED+'. The bar shows its '+RL[S.roll][1]+' yd.'];}},
{id:'ok',target:function(){return mode==='try'?$('scn'):$('sin');},prompt:'Now scan R-48214',where:'below',
 ok:function(){var v=norm($('sin').value),b=v!=='R-48214';$('sem').textContent='Scan R-48214, it holds '+NEED;$('fsc').classList.toggle('err',b);return !b;},
 run:function(quick){setScan('R-48214');var go=function(){$('sin').value='R-48214';scanned('R-48214');};if(mode==='watch'&&!quick)typeIn($('sin'),'R-48214',go);else go();},
 after:function(){return['Right lot, the roll is accepted','R-48214 is '+RL['R-48214'][1]+' yd of '+NEED+'. Its length bar is drawn.'];}},
{id:'lay',target:function(){return $('cfl');},prompt:'Confirm lays 1 to '+LAYS,where:'above',run:function(){S.lays=true;render();},
 after:function(){return['Confirm each lay',LAYS+' lays of '+LYD+' yd: '+plan()+' yd planned on R-48214.'];}},
{id:'rec',target:function(){return $('rec');},prompt:'Record the yards actually used',where:'above',
 ok:function(){var v=uVal(),L=RL[S.roll][1],b=!(v>=plan()&&v<=L);$('uem').textContent=isNaN(v)?'Enter a number of yards':'Enter '+plan()+' to '+L;$('fus').classList.toggle('err',b);return !b;},
 run:function(){var v=mode==='try'?uVal():NaN;S.used=v>=plan()&&v<=RL[S.roll][1]?v:USED;S.rec=true;render();},
 after:function(){return['Record what was actually used',S.used+' yd used, '+waste()+' yd waste. '+S.roll+'-R1, '+rem()+' yd, goes back to stock in '+NEED+'.'];}}];
var _r3=ST[2].run;ST[2].run=function(q){_r3(q);S.uv=String(USED);render();};
'''

for k, v in {'@LOT@': D.LOT, '@LAYS@': D.LAYS, '@LYD@': D.LAY_YD, '@USED@': D.USED}.items():
    JS = JS.replace(k, str(v))
assert '@' not in JS
