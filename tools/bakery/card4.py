"""Bakery card 4: Central Bakery to Shops.
Layout: a four stage transfer pipeline across the top (Commit, Pick, Ship, Receive) with a count under each stage, a card per
location with its order lines and a status badge, and a rack tag preview strip along the bottom.
Eastgate Franchise places an order in its ordering portal, the central bakery approves and commits stock, picks by lot,
prints rack tags and ships, and Maple Street receives with lot history intact. Every number is computed from the data below."""
from frame_auto import header

SUMMARY = 'Central Bakery to Shops (a franchise orders in its portal, the central bakery commits stock, picks by lot, prints rack tags and ships, and each shop receives with lot history intact)'
ARIA = 'Interactive product screen: Eastgate Franchise places SO-3303, the central bakery commits 100 of 120 loaf crates and 50 of 60 bun crates across three orders, picks lots L-5120 and L-5121 onto 10 racks, ships, and Maple Street receives'
STEPS = 5
STUDIO = dict(lede='A typical central bakery order flow, built on your Sutton data with Studio. Want it different? Describe the change.',
              examples=['A cutoff time per shop', 'Barcodes on rack tags', 'Order by the rack', 'A portal for every shop'],
              built_on='Transfer orders, lots and stock', change='Stages, fields and portal screens')

ICON = '<path d="M2 13.5V6l6-3.5L14 6v7.5"/><path d="M5.5 13.5V9h5v4.5"/><path d="M2 13.5h12"/>'

CSS = (
 '.k4{padding:10px 40px 0 16px;display:flex;flex-direction:column;gap:10px}'
 '.kpp{height:96px;flex:none;display:grid;grid-template-columns:repeat(4,1fr);gap:0;padding:0}'
 '.kpg{position:relative;padding:9px 12px 8px 14px;display:flex;flex-direction:column;gap:2px;border-right:1px solid #F0F0F1;min-width:0}.kpg:last-child{border-right:0}'
 '.kpg:not(:last-child)::after{content:"";position:absolute;right:-6px;top:38px;width:10px;height:10px;border-top:1px solid #D4D4D8;border-right:1px solid #D4D4D8;background:#fff;transform:rotate(45deg);z-index:1}'
 '.kpg .kpt{display:flex;align-items:center;justify-content:space-between;gap:6px;font-size:10.4px;font-weight:600}.kpg .kpt .ksn{font-size:8.6px;color:#A1A1AA;font-weight:500;font-family:"JetBrains Mono",ui-monospace,monospace}'
 '.kpg .kpc{font-family:"JetBrains Mono",ui-monospace,monospace;font-size:20px;font-weight:600;line-height:1.1;height:22px}.kpg .kps{font-size:8.8px;color:#71717A;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;height:12px}'
 '.kpg .bt{position:absolute;right:12px;bottom:8px;font-size:9.4px;padding:4px 8px}.kpg.kact{background:#FAFAFA}.kpg.kdone .kpc{color:#18181B}.kpg .kpc:empty::before{content:"";display:inline-block;width:26px;height:16px;border-radius:4px;background:#F4F4F5;vertical-align:middle}'
 '.klc{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;height:250px;flex:none}'
 '.kloc{display:flex;flex-direction:column;min-width:0}.kloc .ct{height:30px;padding:0 9px}.kloc .ct>span:first-child{white-space:nowrap;overflow:hidden;text-overflow:ellipsis}'
 '.ksub{display:flex;justify-content:space-between;align-items:center;height:22px;padding:0 9px;font-size:8.8px;color:#71717A;border-bottom:1px solid #F4F4F5}.ksub .mono{color:#18181B;font-weight:600;font-size:9.4px}'
 '.kln2{padding:5px 9px;border-bottom:1px solid #F4F4F5;display:flex;flex-direction:column;gap:2px;font-size:9.6px}.kln2 .kl1{display:flex;justify-content:space-between}.kln2 .mono{font-weight:600}.kln2 .klt{font-size:8.6px;color:#71717A;height:11px}.kln2 .klt .mono{color:#1E3A8A;font-weight:500}'
 '.ktt{display:flex;justify-content:space-between;padding:5px 9px;font-size:9.2px;color:#52525B}.ktt .mono{color:#18181B;font-weight:600}'
 '.khis{margin:2px 9px 0;padding:5px 7px;border-radius:6px;background:#F0FDF4;border:1px solid #BBF7D0;font-size:8.8px;color:#14532D;line-height:1.4}.khis .mono{font-weight:600}'
 '.kla{margin-top:auto;padding:0 9px 9px;display:flex;align-items:center;gap:6px;font-size:8.8px;color:#71717A}.kla .bt{font-size:9.4px;padding:4px 9px}'
 '.kloc .empt{margin:8px;flex:1;padding:8px}'
 '.kptl{padding:8px 9px 0;display:flex;flex-direction:column;gap:7px}.kptl .ksub{border:0;padding:0;height:auto}.kpf{display:flex;align-items:center;gap:6px;font-size:9.6px}.kpf>span:first-child{flex:1}'
 '.kpf .fld{flex-direction:row;align-items:center}.kpf input{width:44px!important;text-align:right;font-size:10px;padding:4px 6px}.kptl .kerr{display:none;color:#B91C1C;font-size:8.6px}.kptl.err .kerr{display:block}.kptl.err input{border-color:#F87171;background:#FEF2F2}'
 '.kptl .ksp{display:flex;align-items:center;gap:5px;font-size:8.8px;color:#71717A}.kptl .ksp .bt{font-size:9px;padding:3px 7px}'
 '.krt{height:170px;flex:none}.krt .empt{margin:8px 10px 0;height:96px;padding:8px}'
 '.ktg{display:flex;gap:5px;padding:8px 11px 0}.ktg .kgp{width:8px;flex:none}'
 '.ktag{width:56px;height:80px;white-space:nowrap;flex:none;border:1px solid #E4E4E7;border-radius:6px;background:#fff;padding:5px 5px 4px;display:flex;flex-direction:column;gap:1px;font-size:8px;line-height:1.3;position:relative;overflow:hidden}'
 '.ktag::before{content:"";position:absolute;left:0;right:0;top:0;height:3px;background:var(--kc,#18181B)}.ktag .mono{font-weight:600;font-size:8.2px;margin-top:2px}.ktag .kbc{margin-top:auto;height:6px;background:repeating-linear-gradient(90deg,#18181B 0 1px,transparent 1px 3px,#18181B 3px 5px,transparent 5px 6px)}'
 '.ktag .kq{font-family:"JetBrains Mono",ui-monospace,monospace;font-size:8.4px}.ktag .kmu{color:#71717A}'
 '.krf{padding:7px 11px 0;font-size:9.2px;color:#52525B}.krf b{font-family:"JetBrains Mono",ui-monospace,monospace;color:#18181B}'
)

WIN = (
 header(ICON, 'Shop orders', 'Central bakery to shops and franchise', '<span class="ch c-idle" id="kst">No orders today</span>')
 + '<div class="k4"><div class="cd kpp" id="kpp"></div><div class="klc"><div class="cd kloc" id="kl0"></div><div class="cd kloc" id="kl1"></div><div class="cd kloc" id="kl2"></div></div>'
 '<div class="cd krt" id="krt"></div></div>'
)

PORTAL = ('<div class="ct"><span>Eastgate Franchise</span><span class="ch c-idle">Ordering portal</span></div>'
 '<div class="kptl frm" id="kptl"><div class="ksub"><span>Order from the central bakery</span><span>Crates</span></div>'
 '<div class="kpf"><span>Sandwich Loaf</span><label class="fld"><input id="kq0" value="" inputmode="numeric" placeholder="0" autocomplete="off" aria-label="Sandwich Loaf crates"></label></div>'
 '<div class="kpf"><span>Brioche Bun</span><label class="fld"><input id="kq1" value="" inputmode="numeric" placeholder="0" autocomplete="off" aria-label="Brioche Bun crates"></label></div>'
 '<span class="kerr" id="kqe">Enter whole crates</span><span class="ksp">Sample<button type="button" class="bt" id="ksm" data-sample>Usual order</button></span>'
 '<span style="display:flex"><button type="button" class="bt pri" id="kpl">Place order</button></span></div>')

JS = r'''
var FOC='.hd>*,.kpp>*,.kloc,.krt>*';
var PORTAL=@PORTAL@;
var STK=[{n:'Sandwich Loaf',lot:'L-5120',cr:120},{n:'Brioche Bun',lot:'L-5121',cr:60}],MADE='November 16',RACK=15;
var ORD=[{loc:'Maple Street',kind:'Shop',id:'TO-3301',t:'Transfer order',q:[40,20],c:'#18181B'},{loc:'Harbor Road',kind:'Shop',id:'TO-3302',t:'Transfer order',q:[30,15],c:'#2563EB'},{loc:'Eastgate Franchise',kind:'Franchise',id:'SO-3303',t:'Portal order',q:[30,15],c:'#D97706'}];
var LV=['portal','pending','committed','picked','transit','received'];
var S;
function sum(a){return a.reduce(function(s,x){return s+x;},0);}
function qty(i){return i===2?S.eq:ORD[i].q;}
function crates(i){return sum(qty(i));}
function racks(i){return Math.ceil(crates(i)/RACK);}
function lv(i){return LV.indexOf(S.st[i]);}
function inPlay(){return ORD.map(function(o,i){return i;}).filter(function(i){return lv(i)>=2;});}
function committed(k){return sum(inPlay().map(function(i){return qty(i)[k];}));}
function free(k,skip){return STK[k].cr-sum(ORD.map(function(o,i){return i===skip?0:o.q[k];}));}
/* rack contents: loaf crates first, then bun, 15 crates a rack */
function rackList(i){var q=qty(i).slice(),out=[];while(q[0]+q[1]>0){var r=[0,0],room=RACK;[0,1].forEach(function(k){var t=Math.min(room,q[k]);r[k]=t;q[k]-=t;room-=t;});out.push(r);}return out;}
function badge(i){var s=S.st[i];return {pending:['c-warn','Pending approval'],committed:['c-info','Committed'],picked:['c-info','Picked'],transit:['c-warn','In transit'],received:['c-ok','Received']}[s];}
function stageN(k){return ORD.filter(function(o,i){return lv(i)>=k+2;}).length;}
function render(){var p=$('kpp'),any=lv(0)>=2;
var stg=[['Commit',any?'Loaf '+committed(0)+' of '+STK[0].cr+', bun '+committed(1)+' of '+STK[1].cr:'',''],['Pick',stageN(1)?sum(inPlay().map(racks))+' racks tagged':'',any&&!stageN(1)?'<button type="button" class="bt pri" id="kpk">Pick by lot</button>':''],
['Ship',stageN(2)?stageN(2)+' in transit':'',stageN(1)&&!stageN(2)?'<button type="button" class="bt pri" id="ksh">Ship</button>':''],['Receive',stageN(3)?stageN(3)+' of '+stageN(2)+' received':stageN(2)?'Waiting at the shops':'','']];
p.innerHTML=stg.map(function(s,k){var n=any?stageN(k):null;return '<div class="kpg'+(s[2]?' kact':'')+'"><div class="kpt"><span>'+s[0]+'</span><span class="ksn">'+(k+1)+'</span></div><div class="kpc" id="kpc'+k+'">'+(n===null?'':n)+'</div><div class="kps" id="kps'+k+'">'+s[1]+'</div>'+s[2]+'</div>';}).join('');
ORD.forEach(function(o,i){var el=$('kl'+i),s=S.st[i];
if(s==='portal'){if(i===2){if(!$('kptl'))el.innerHTML=PORTAL;}else el.innerHTML='<div class="ct"><span>'+o.loc+'</span><span class="ch c-idle">'+o.kind+'</span></div><div class="empt"><b>No order yet</b><span>Today\'s transfer order shows here once orders are approved.</span></div>';return;}
var b=badge(i),lots=lv(i)>=3,q=qty(i);
el.innerHTML='<div class="ct"><span>'+o.loc+'</span><span class="ch '+b[0]+'" id="kb'+i+'">'+b[1]+'</span></div><div class="ksub"><span>'+o.t+'</span><span class="mono">'+o.id+'</span></div>'
+STK.map(function(x,k){return '<div class="kln2"><span class="kl1"><span>'+x.n+'</span><span class="mono" id="kq'+i+k+'">'+q[k]+' crates</span></span><span class="klt">'+(lots?'Lot <span class="mono" id="klot'+i+k+'">'+x.lot+'</span>, made '+MADE:'')+'</span></div>';}).join('')
+'<div class="ktt"><span>Total</span><span class="mono" id="ktot'+i+'">'+crates(i)+' crates, '+racks(i)+' racks</span></div>'
+(s==='received'?'<div class="khis" id="khis'+i+'">Lot history kept: <span class="mono">'+STK.map(function(x){return x.lot;}).join(', ')+'</span>, made '+MADE+'</div>':'')
+'<div class="kla">'+(s==='pending'?'<button type="button" class="bt pri" id="kap">Approve</button><span>Placed in the portal</span>':s==='transit'||s==='received'?'<button type="button" class="bt'+(s==='transit'&&i===0?' pri':'')+'" id="krv'+i+'"'+(s==='transit'?'':' disabled')+'>'+(s==='received'?'Received':'Receive')+'</button><span>'+(s==='received'?'Into shop stock':'On the way')+'</span>':'<span>'+(lots?'Picked by lot':'Stock committed')+'</span>')+'</div>';});
var r=$('krt'),pk=inPlay().filter(function(i){return lv(i)>=3;});
if(!pk.length)r.innerHTML='<div class="ct"><span>Rack tags</span></div><div class="empt"><b>No rack tags yet</b><span>One tag per rack, printed when an order is picked.</span></div><div class="krf">15 crates to a rack. Tags carry the order, the location and the lots.</div>';
else{var tg='',all=0;pk.forEach(function(i,gi){var rl=rackList(i);if(gi)tg+='<span class="kgp"></span>';rl.forEach(function(x,j){all++;var lots=STK.filter(function(s,k){return x[k]>0;}).map(function(s){return s.lot;});
tg+='<div class="ktag" style="--kc:'+ORD[i].c+'" data-o="'+i+'"><span class="mono">'+ORD[i].id+'</span><span>'+ORD[i].loc.split(' ')[0]+'</span><span>Rack '+(j+1)+' of '+rl.length+'</span><span class="kq">'+sum(x)+' crates</span><span class="kmu">'+(lots.length>1?'2 lots':lots[0])+'</span><span class="kbc"></span></div>';});});
r.innerHTML='<div class="ct"><span>Rack tags</span><span class="ch c-info" id="ktn">'+all+' tags</span></div><div class="ktg" id="ktg">'+tg+'</div><div class="krf" id="krf">'+pk.map(function(i){return racks(i);}).join(' + ')+' = <b>'+all+' racks</b>, '+sum(pk.map(crates))+' crates, 15 to a rack</div>';}
var st=$('kst'),n=lv(0)>=2;st.textContent=stageN(3)?'1 received, 2 in transit':stageN(2)?'3 in transit':n?'3 orders committed':S.st[2]==='pending'?'1 pending approval':'No orders today';st.className='ch '+(stageN(3)?'c-ok':n||S.st[2]==='pending'?'c-info':'c-idle');}
function qv(id){var v=String($(id).value).trim();return /^\d+$/.test(v)?parseInt(v,10):NaN;}
function typeQ(done){var a=[['kq0','30'],['kq1','15']],k=0;(function nx(){if(k>=a.length){done();return;}var id=a[k][0],t=a[k][1],i=0;(function ch(){$(id).value=t.slice(0,i);if(i<t.length){i++;later(ch,110);}else{k++;later(nx,200);}})();})();}
winEl.addEventListener('click',function(e){var t=e.target.closest&&e.target.closest('#ksm');if(!t)return;$('kq0').value='30';$('kq1').value='15';$('kptl').classList.remove('err');});
winEl.addEventListener('click',function(e){var t=e.target.closest&&e.target.closest('[id^="krv"]');if(!t||mode!=='done')return;var i=+t.id.slice(3);if(S.st[i]==='transit'){S.st[i]='received';render();say2(5,ORD[i].loc+' received','Lot history '+STK.map(function(s){return s.lot;}).join(' and ')+' stays with the order.');}});
function resetState(){S={st:['portal','portal','portal'],eq:[30,15]};$('kl2').innerHTML='';render();$('kq0').value='';$('kq1').value='';}
function setAll(a,b){ORD.forEach(function(o,i){if(S.st[i]===a)S.st[i]=b;});}
var CAPAT=function(hh){return cur<=1?{l:14,t:visH()-hh-14}:{l:14,t:150};};
var ST=[
{id:'place',target:function(){return mode==='try'?$('kpl'):$('kq0');},prompt:'Enter 30 and 15 crates, or pick Usual order, then Place order',where:'above',
 ok:function(){var a=qv('kq0'),b=qv('kq1'),f0=free(0,2),f1=free(1,2),bad=!(a>=0&&b>=0&&a+b>0&&a<=f0&&b<=f1);$('kqe').textContent=(a>f0||b>f1)?'Only '+f0+' loaf and '+f1+' bun crates are free':'Enter whole crates';$('kptl').classList.toggle('err',bad);return !bad;},
 run:function(quick){var go=function(){var a=qv('kq0'),b=qv('kq1');if(mode==='watch'||!(a+b>0)){a=30;b=15;}S.eq=[a,b];S.st[2]='pending';render();};if(mode==='watch'&&!quick)typeQ(go);else{if(!$('kq0').value){$('kq0').value='30';$('kq1').value='15';}go();}},
 after:function(){return['A franchise orders from the central bakery',ORD[2].id+' from Eastgate Franchise: '+S.eq[0]+' crates Sandwich Loaf, '+S.eq[1]+' crates Brioche Bun. Pending approval.'];}},
{id:'approve',target:function(){return $('kap');},prompt:'Approve the portal order',where:'above',run:function(){S.st=S.st.map(function(){return 'committed';});render();},
 after:function(){return['Approve it and stock is committed','3 orders committed: loaf '+committed(0)+' of '+STK[0].cr+' crates, bun '+committed(1)+' of '+STK[1].cr+'. '+(STK[0].cr-committed(0))+' and '+(STK[1].cr-committed(1))+' crates left.'];}},
{id:'pick',target:function(){return $('kpk');},prompt:'Click Pick by lot',where:'below',run:function(){setAll('committed','picked');render();},
 after:function(){return['Pick by lot and print rack tags',STK.map(function(s){return s.lot;}).join(' and ')+' on every order. '+sum(inPlay().map(racks))+' rack tags of 15 crates: '+inPlay().map(racks).join(', ')+'.'];}},
{id:'ship',target:function(){return $('ksh');},prompt:'Click Ship',where:'below',run:function(){setAll('picked','transit');render();},
 after:function(){return['Ship, and every location sees it',ORD.map(function(o){return o.id;}).join(', ')+' are in transit to Maple Street, Harbor Road and Eastgate Franchise.'];}},
{id:'recv',target:function(){return $('krv0');},prompt:'Receive at Maple Street',where:'above',run:function(){if(S.st[0]==='transit')S.st[0]='received';render();},
 after:function(){return['Receive at the shop with lot history intact','Maple Street received '+crates(0)+' crates from '+STK.map(function(s){return s.lot;}).join(' and ')+'. Harbor Road and Eastgate Franchise stay in transit.'];}}];
'''.replace('@PORTAL@', __import__('json').dumps(PORTAL))
