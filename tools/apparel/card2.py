"""Apparel card 2: Fabric Rolls & Dye Lots. Layout: a roll list with a yardage bar for each roll and a movement log on the left; receiving, allocation and cutting table panels on the right."""
SUMMARY = 'Fabric Rolls & Dye Lots (receive a roll with its dye lot, allocate yardage to a cut from one dye lot, a wrong lot flagged at the cutting table, leftover back to the roll)'
ARIA = 'Interactive product screen: receive navy fabric roll R-4417, allocate 195 yards of dye lot NAV-2611 to cut order CUT-0412, scan rolls at the cutting table, then return the leftover yardage to its roll'
STEPS = 5
STUDIO = dict(lede='A typical fabric roll screen, built on your Sutton data with Studio. Want it different? Describe the change.',
              examples=['A shade match report', 'A roll aging view', 'A leftover yardage list', 'A fabric reorder screen'],
              built_on='Rolls, dye lots, cut orders and receiving', change='Roll fields, checks and views')

CSS = (
 '.b2{display:grid;grid-template-columns:392px 1fr;gap:12px;padding:12px 40px 0 16px;height:596px}'
 '.col{display:flex;flex-direction:column;gap:10px;min-height:0}'
 '.kp{display:grid;grid-template-columns:repeat(3,1fr);gap:8px}.kp .cd{padding:8px 10px;display:flex;flex-direction:column;gap:3px}.kp small{color:#71717A;font-size:8.9px}.kp b{font-family:"JetBrains Mono",ui-monospace,monospace;font-size:15px;font-weight:600}'
 '.rl .row{grid-template-columns:52px 64px 1fr 58px;min-height:42px}.rl .row.h{min-height:24px}.rl .row.gone{opacity:.55}'
 '.dl{font-family:"JetBrains Mono",ui-monospace,monospace;font-size:9.4px}.rl .sub{display:block;color:#71717A;font-size:8.6px;margin-top:2px;font-family:Inter,sans-serif}'
 '.ym{position:relative;height:12px;background:#F4F4F5;border-radius:3px;overflow:hidden}.ym i{position:absolute;top:0;bottom:0;transition:width .6s cubic-bezier(.22,.9,.28,1),left .6s cubic-bezier(.22,.9,.28,1)}.ym .fr{left:0;background:#A1A1AA}.ym .al{background:#18181B}'
 '.lg{flex:1 1 0;min-height:0}.lg .row{grid-template-columns:38px 1fr;min-height:24px;font-size:9.4px}.lg .row.new{animation:exflash 1.4s ease}'
 '.frm .g{display:grid;grid-template-columns:1fr 1fr;gap:7px;padding:9px 11px}.frm .ft{display:flex;justify-content:flex-end;padding:2px 11px 10px}'
 '.al2 .row{grid-template-columns:1fr 70px 60px;min-height:24px;font-size:9.6px}.al2 .row.t{background:#FAFAFA;font-weight:600}'
 '.sc{padding:8px 11px;display:flex;flex-direction:column;gap:6px}.sc .bts{display:flex;gap:6px;flex-wrap:wrap}'
 '.res{display:flex;align-items:flex-start;gap:7px;padding:7px 9px;border-radius:7px;font-size:9.6px;line-height:1.4}.res.bad{background:#FEF2F2;color:#B91C1C;border:1px solid #FECACA}.res.ok{background:#F0FDF4;color:#166534;border:1px solid #BBF7D0}.res b{font-family:"JetBrains Mono",ui-monospace,monospace}'
 '.mm{color:#B91C1C;font-weight:700;text-decoration:underline}'
 '.dlr{flex:1 1 0;min-height:0}.dlr .row{grid-template-columns:70px 1fr 60px;min-height:30px;font-size:9.6px}.dn{padding:8px 11px;display:flex;align-items:center;justify-content:space-between;gap:8px}'
)

WIN = (
 '<div class="hd"><svg width="16" height="16" viewBox="0 0 16 16" fill="none" aria-hidden="true"><ellipse cx="5" cy="8" rx="2.6" ry="5.5" stroke="#18181B" stroke-width="1.2"/><path d="M5 2.5h7.5M5 13.5h7.5M12.5 2.5v11" stroke="#18181B" stroke-width="1.2" stroke-linecap="round"/></svg>'
 '<span class="tt">Fabric <span class="mono">FAB-NVY</span></span><span class="ch c-idle" id="hst">2 rolls</span><span class="sb grow">Navy cotton jersey, 180 gsm</span></div>'
 '<div class="b2"><div class="col">'
 '<div class="kp"><div class="cd"><small>On hand</small><b id="koh"></b></div><div class="cd"><small>Allocated</small><b id="kal"></b></div><div class="cd"><small>Dye lots</small><b id="kdl"></b></div></div>'
 '<div class="cd rl"><div class="ct">Rolls<span class="mut" style="font-weight:500">Length left in each roll</span></div><div class="row h"><span>Roll</span><span>Dye lot</span><span>Yardage</span><span class="r">Yards</span></div><div id="rows"></div></div>'
 '<div class="cd lg"><div class="ct">Movements<span class="mut" style="font-weight:500">FAB-NVY</span></div><div id="lg"></div></div>'
 '</div><div class="col" id="rc"></div></div>'
)

JS = r'''
var FOC='.hd>*,.kp .cd,.rl .row,.rl .ct,.lg,#rc .ct,#rc .fld,#rc .kv,#rc .bt,#rc .row,#rc .res,#rc .dn>span';
var S;
function y1(n){return (Math.round(n*10)/10).toFixed(1);}
function base(){return[{id:'R-4410',dl:'NAV-2611',sl:'SL-7702',len:140,al:0},{id:'R-4411',dl:'NAV-2611',sl:'SL-7702',len:120,al:0}];}
function roll(id){for(var i=0;i<S.R.length;i++)if(S.R[i].id===id)return S.R[i];}
function onhand(){return S.R.reduce(function(a,r){return a+r.len;},0);}
function render(){var oh=onhand(),al=S.R.reduce(function(a,r){return a+r.al;},0),lots={};S.R.forEach(function(r){if(r.len>0)lots[r.dl]=1;});
$('koh').textContent=y1(oh)+' yd';$('kal').textContent=y1(al)+' yd';$('kdl').textContent=Object.keys(lots).length;
var hs2=$('hst');hs2.textContent=S.R.filter(function(r){return r.len>0;}).length+' rolls';
var h='';S.R.forEach(function(r,i){var w=r.len/150*100,a=r.al/150*100;h+='<div class="row'+(r.len<=0?' gone':'')+(S.anim===r.id?' in':'')+'" data-r="'+r.id+'"><span><b class="mono">'+r.id+'</b><span class="sub">'+r.sl+'</span></span><span class="dl">'+r.dl+'</span><span class="ym"><i class="fr" style="width:'+w+'%"></i><i class="al" style="left:0;width:'+a+'%"></i></span><span class="mono r">'+(r.len<=0?'Used':y1(r.len))+'</span></div>';});
$('rows').innerHTML=h;
$('lg').innerHTML=S.log.slice().reverse().map(function(l,i){return '<div class="row'+(i===0&&S.flash?' new':'')+'"><span class="mut mono">'+l[0]+'</span><span>'+l[1]+'</span></div>';}).join('');
var d='';
if(S.step<2){d+='<div class="cd frm'+(S.step===1?' done1':'')+'"><div class="ct">Receive roll<span class="ch '+(S.step===1?'c-ok':'c-idle')+'">'+(S.step===1?'Received':'PO-2207')+'</span></div>';
if(S.step===0)d+='<div class="g"><label class="fld" id="fr1"><small>Roll</small><input id="ir1" value="R-4417" autocomplete="off" spellcheck="false"><span class="em">Roll ID needed</span></label><label class="fld" id="fr2"><small>Length, yd</small><input id="ir2" value="150.0" inputmode="decimal" autocomplete="off"><span class="em">1.0 to 500.0</span></label><label class="fld" id="fr3"><small>Supplier lot</small><input id="ir3" value="SL-7731" autocomplete="off" spellcheck="false"><span class="em">Supplier lot needed</span></label><label class="fld" id="fr4"><small>Dye lot</small><input id="ir4" value="NAV-2618" autocomplete="off" spellcheck="false"><span class="em">Use the form NAV-0000</span></label></div><div class="ft"><button type="button" class="bt pri" id="rcv">Receive roll</button></div>';
else{var n=roll('R-4417');d+='<div class="dn"><span><b class="mono">'+n.id+'</b>, '+y1(n.len)+' yd, dye lot <span class="mono">'+n.dl+'</span></span><span class="mut">On the list</span></div>';}
d+='</div>';}
else{d+='<div class="cd"><div class="ct">Cutting table 2<span class="ch '+(S.step>=4?'c-ok':'c-info')+'">'+(S.step>=4?'Cut done':'CUT-0412')+'</span></div><div class="sc">'+
'<div class="res ok"><span><b>R-4410</b> scanned 9:12, dye lot <b>NAV-2611</b>, accepted</span></div>'+
(S.step>=3?'<div class="res bad in"><span><b>R-4417</b> flagged. Dye lot <b class="mm">NAV-2618</b> does not match <b>NAV-2611</b>. Set aside.</span></div>':'')+
(S.step>=4?'<div class="res ok in"><span><b>R-4411</b> accepted, dye lot <b>NAV-2611</b>. Cut tied to R-4410 and R-4411.</span></div>':'')+
(S.step<4?'<div class="bts">'+(S.step===2?'<button type="button" class="bt pri" id="sc1">Scan roll R-4417</button>':'')+(S.step===3?'<button type="button" class="bt pri" id="sc2">Scan roll R-4411</button>':'')+'</div>':'')+'</div></div>';}
d+='<div class="cd frm"><div class="ct">Cut order <span class="mono">CUT-0412</span><span class="ch '+(S.step>=5?'c-ok':S.step>=2?'c-info':'c-idle')+'">'+(S.step>=5?'Closed':S.step>=2?'Allocated':'Needs fabric')+'</span></div>';
if(S.step<2)d+='<div class="g"><div class="kv"><small>Cut order</small><b class="mono" style="padding:5px 0">CUT-0412, size L</b></div><label class="fld" id="fa1"><small>Yards</small><input id="ia1" value="195.0" inputmode="decimal" autocomplete="off"><span class="em">CUT-0412 needs 195.0 yd</span></label><label class="fld" id="fa2"><small>Dye lot</small><input id="ia2" value="NAV-2611" autocomplete="off" spellcheck="false"><span class="em">Only NAV-2611 has enough</span></label><div class="kv"><small>Pieces</small><b class="mono" style="padding:5px 0">150 x 1.3 yd</b></div></div><div class="ft"><button type="button" class="bt pri" id="alc">Allocate to cut</button></div>';
else{var r1=S.step>=5?S.u1:140,r2=S.step>=5?S.u2:55;d+='<div class="al2'+(S.step===2&&S.flash?' in':'')+'"><div class="row h"><span>Roll</span><span class="r">'+(S.step>=5?'Used':'Allocated')+'</span><span class="r">Dye lot</span></div><div class="row"><span class="mono">R-4410</span><span class="mono r">'+y1(r1)+' yd</span><span class="mono r">2611</span></div><div class="row"><span class="mono">R-4411</span><span class="mono r">'+y1(r2)+' yd</span><span class="mono r">2611</span></div><div class="row t"><span>Total</span><span class="mono r" id="atot">'+y1(r1+r2)+' yd</span><span></span></div></div>';
if(S.step===4)d+='<div class="g"><label class="fld" id="fu1"><small>Yards used</small><input id="iu1" value="192.0" inputmode="decimal" autocomplete="off"><span class="em">140.1 to 195.0</span></label><div class="kv"><small>Of allocated</small><b class="mono" style="padding:5px 0">195.0 yd</b></div></div><div class="ft"><button type="button" class="bt pri" id="ret">Return leftover</button></div>';
if(S.step>=5)d+='<div class="dn"><span>'+y1(195-S.used)+' yd back to <b class="mono">R-4411</b>, now '+y1(roll('R-4411').len)+' yd</span></div>';}
d+='</div>';
var lots={};S.R.forEach(function(r){if(!lots[r.dl])lots[r.dl]={n:0,y:0};if(r.len>0){lots[r.dl].n++;lots[r.dl].y+=r.len;}});
d+='<div class="cd dlr"><div class="ct">Dye lots<span class="mut" style="font-weight:500">Shade record</span></div><div class="row h"><span>Dye lot</span><span>Shade check</span><span class="r">On hand</span></div>'+Object.keys(lots).map(function(k){var a=k==='NAV-2611';return '<div class="row"><span class="mono">'+k+'</span><span>'+(a?'<span class="ch c-ok">Approved 10/29</span>':'<span class="ch c-warn">Pending</span>')+'</span><span class="mono r">'+y1(lots[k].y)+' yd</span></div>';}).join('')+'<div class="row"><span class="mono mut">NAV-2584</span><span class="mut">Used up 10/12</span><span class="mono r mut">0.0 yd</span></div></div>';
$('rc').innerHTML=d;S.anim=false;S.flash=false;}
function resetState(){S={R:base(),step:0,used:192,u1:140,u2:52,anim:false,flash:false,log:[['09/12','R-4365 received, dye lot NAV-2560, 150.0 yd'],['09/18','R-4365 used up on CUT-0377'],['09/24','Reorder point for FAB-NVY set to 200.0 yd'],['09/30','PO-2207 placed for 150.0 yd, navy jersey'],['10/02','R-4377 received, dye lot NAV-2584, 140.0 yd'],['10/09','R-4380 received, dye lot NAV-2584, 150.0 yd'],['10/12','NAV-2584 used up on CUT-0391'],['10/21','Cycle count, FAB-NVY confirmed'],['10/28','R-4410 and R-4411 received, dye lot NAV-2611, 260.0 yd'],['10/29','Shade check on NAV-2611, signed by A. Kim'],['11/02','R-4392 used up on CUT-0398']]};render();}
function val(id){var e=$(id);return e?String(e.value).trim():'';}
function bad(id,c){var f=$(id);if(f)f.classList.toggle('err',c);return c;}
function num(v){return /^\d+(\.\d+)?$/.test(v)?parseFloat(v):NaN;}
var CAPAT=function(hh){return{l:14,t:visH()-hh-14};};
var ST=[
{id:'rcv',target:function(){return $('rcv');},prompt:'Click Receive roll',where:'below',ok:function(){var L=num(val('ir2')),a=bad('fr1',!val('ir1')),b=bad('fr2',!(L>=1&&L<=500)),c=bad('fr3',!val('ir3')),d=bad('fr4',!/^NAV-\d{4}$/i.test(val('ir4')));return !(a||b||c||d);},
 run:function(){var L=num(val('ir2'));if(!(L>0))L=150;var id=val('ir1')||'R-4417',sl=val('ir3')||'SL-7731',dl=(val('ir4')||'NAV-2618').toUpperCase();var before=onhand();S.R.push({id:'R-4417',dl:dl,sl:sl,len:L,al:0});if(id!=='R-4417')S.R[S.R.length-1].id=id;S.step=1;S.anim=S.R[S.R.length-1].id;S.flash=true;S.log.push(['11/06',S.R[S.R.length-1].id+' received, '+y1(L)+' yd, supplier lot '+sl+', dye lot '+dl]);S.before=before;render();},
 after:function(){var r=S.R[2];return['Each roll arrives with its own dye lot',r.id+', '+y1(r.len)+' yd, dye lot '+r.dl+'. On hand went from '+y1(S.before)+' to '+y1(onhand())+' yd.'];}},
{id:'alc',target:function(){return $('alc');},prompt:'Click Allocate to cut',where:'below',ok:function(){var a=bad('fa1',num(val('ia1'))!==195),b=bad('fa2',val('ia2').toUpperCase()!=='NAV-2611');return !(a||b);},
 run:function(){roll('R-4410').al=140;roll('R-4411').al=55;S.step=2;S.flash=true;S.log.push(['11/06','195.0 yd of NAV-2611 allocated to CUT-0412']);render();},after:['Yardage set aside from one dye lot','R-4410 gives 140.0 and R-4411 gives 55.0, 195.0 yd for CUT-0412.']},
{id:'sc1',target:function(){return $('sc1');},prompt:'Click Scan roll R-4417',where:'below',run:function(){S.step=3;S.flash=true;S.log.push(['11/06',(S.R[2]?S.R[2].id:'R-4417')+' flagged at cutting table 2, wrong dye lot']);render();},after:function(){return['A roll from another dye lot is flagged','R-4417 is dye lot '+(S.R[2]?S.R[2].dl:'NAV-2618')+', not NAV-2611, so it never reaches the cutting table.'];}},
{id:'sc2',target:function(){return $('sc2');},prompt:'Click Scan roll R-4411',where:'below',run:function(){S.step=4;S.flash=true;S.log.push(['11/06','R-4411 accepted, CUT-0412 cut on R-4410 and R-4411']);render();},after:['The right roll goes through','R-4411 is NAV-2611. The cut is done and tied to the two rolls it came from.']},
{id:'ret',target:function(){return $('ret');},prompt:'Click Return leftover',where:'below',ok:function(){var u=num(val('iu1'));return !bad('fu1',!(u>140&&u<=195));},
 run:function(){var u=num(val('iu1'));if(!(u>140&&u<=195))u=192;S.used=u;S.u1=140;S.u2=Math.round((u-140)*10)/10;roll('R-4410').len=0;roll('R-4410').al=0;var r=roll('R-4411');r.len=Math.round((120-S.u2)*10)/10;r.al=0;S.step=5;S.flash=true;S.log.push(['11/06',y1(195-u)+' yd back to R-4411, CUT-0412 closed at '+y1(u)+' yd']);render();},
 after:function(){return['Leftover yardage goes back to the roll',y1(195-S.used)+' yd back to R-4411, which holds '+y1(roll('R-4411').len)+' yd. On hand is '+y1(onhand())+' yd.'];}}];
'''
