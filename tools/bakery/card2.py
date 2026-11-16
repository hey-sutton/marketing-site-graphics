"""Bakery card 2: Bake Plan & Ingredient Check.
Layout: the bake list (three product rows with a status chip) and an allocation panel on the left, a column of horizontal
stock gauges on the right (needed against available), and a purchase order strip along the bottom.
Products are allocated in list order, so the ingredient that runs out holds back the last product. The gap becomes a
purchase order, and when it is received the product clears and the list goes to the floor.
Every number is computed from the data arrays below (grams and units), so sums are exact."""
from frame_auto import header

SUMMARY = "Bake Plan & Ingredient Check (load tomorrow's bake list, check every ingredient and pack against stock in list order, turn the butter gap into a purchase order, receive it and send the list to the floor)"
ARIA = "Interactive product screen: load tomorrow's bake list, check flour, butter, bags and boxes against stock, see Cinnamon Roll held back 16.000 kg of butter short, raise PO-7210 and receive it, then send three work orders to the floor"
STEPS = 5
STUDIO = dict(lede='A typical bake plan check, built on your Sutton data with Studio. Want it different? Describe the change.',
              examples=['Allocate by shop priority', 'Suggest a swap to another product', 'Check oven and mixer hours', 'Send the PO by email'],
              built_on='Bake lists, BOMs, stock and purchase orders', change='Checks, rules and actions')

ICON = '<rect x="2.5" y="2.5" width="11" height="11" rx="1.5"/><path d="M5 5.8h6M5 8h6M5 10.2h3.5"/>'

CSS = (
 '.k2{padding:10px 40px 0 16px;display:flex;flex-direction:column;gap:10px}'
 '.k2m{display:grid;grid-template-columns:350px 300px;gap:10px;height:430px;flex:none}'
 '.k2l{display:flex;flex-direction:column;gap:10px;min-width:0}'
 '.kbl{height:164px;flex:none}.kbl .empt{margin:10px;height:112px}.kbl .row{grid-template-columns:1fr 88px 96px;min-height:36px;font-size:10px}.kbl .row.h{min-height:22px;font-size:9px}'
 '.kbl .row .kpn{display:flex;flex-direction:column;gap:1px}.kbl .row .kpn b{font-weight:600}.kbl .row .kpn small{font-size:8.6px;color:#71717A;font-family:"JetBrains Mono",ui-monospace,monospace}.kbl .row>span:nth-child(2){text-align:right}.kbl .row>span:last-child{text-align:right}'
 '.kal{flex:1 1 auto;min-height:0}.kal .empt{margin:10px;height:200px}'
 '.kat{padding:8px 11px 0}.kat .row{grid-template-columns:1fr 70px 76px;min-height:22px;padding:0 6px;font-size:9.6px}.kat .row.h{min-height:20px;font-size:8.8px}.kat .row>span:not(:first-child){text-align:right}.kat .row.ksel{background:#F4F4F5}.kat .row.ksel.kxs{background:#FEF2F2}.kat .row.kxs .mono:last-child{color:#B91C1C;font-weight:600}'
 '.kmsg{margin:8px 11px 0;padding:7px 9px;border-radius:7px;background:#FEF2F2;border:1px solid #FECACA;font-size:9.8px;color:#7F1D1D;line-height:1.4}.kmsg.kgo{background:#F0FDF4;border-color:#BBF7D0;color:#14532D}.kmsg b{font-weight:600}'
 '.knd{display:flex;gap:6px;flex-wrap:wrap;padding:7px 11px 0}.knd span{font-size:9px;padding:2px 7px;border-radius:999px;background:#F4F4F5;color:#3F3F46;font-family:"JetBrains Mono",ui-monospace,monospace}.knd span.kx{background:#FEE2E2;color:#B91C1C}'
 '.kac{display:flex;align-items:center;gap:8px;padding:8px 11px 0;font-size:9.4px;color:#71717A}'
 '.kgs .empt{margin:10px;height:368px}.kgl{padding:4px 12px 0}.kg{padding:8px 0 7px;border-bottom:1px solid #F4F4F5}.kg:last-child{border-bottom:0}'
 '.kg .kgt{display:flex;justify-content:space-between;align-items:baseline;font-size:10px}.kg .kgt b{font-weight:600}.kg .kgt span{font-family:"JetBrains Mono",ui-monospace,monospace;font-size:9.6px}'
 '.kgb{position:relative;height:9px;margin:6px 0 4px;border-radius:5px;background:#F4F4F5;overflow:visible}.kgb i{position:absolute;left:0;top:0;bottom:0;border-radius:5px;background:#52525B;transform-origin:left;animation:kgw .7s cubic-bezier(.22,.9,.28,1) both}'
 '.kgb i.kov{background:#EF4444}.kgb u{position:absolute;top:-3px;bottom:-3px;width:2px;margin-left:-1px;background:#18181B;border-radius:1px}@keyframes kgw{from{transform:scaleX(0)}}'
 '.kgs2{display:flex;justify-content:space-between;font-size:8.8px;color:#71717A}.kgs2 .kred{color:#B91C1C;font-weight:600}.kgs2 .kgrn{color:#166534}'
 '.kgf{padding:6px 12px;font-size:9px;color:#71717A;display:flex;gap:12px;border-top:1px solid #F0F0F1}.kgf span{display:inline-flex;align-items:center;gap:5px}.kgf i{display:inline-block;width:12px;height:6px;border-radius:3px;background:#52525B}.kgf u{display:inline-block;width:2px;height:10px;background:#18181B}'
 '.kpo{height:108px;flex:none}.kpo .empt{margin:8px 10px;height:58px;padding:8px}'
 '.kps{display:grid;grid-template-columns:150px 150px 110px 1fr;gap:12px;padding:9px 11px 0;align-items:start;animation:kup .5s cubic-bezier(.22,.9,.28,1) both}@keyframes kup{from{opacity:0;transform:translateY(14px)}}'
 '.kps .kv small{font-size:8.6px}.kps .kv b{font-size:10.6px}.kps .kv .mono{font-weight:600}.kps .kv em{font-style:normal;font-size:9px;color:#71717A}'
 '.kps .kpa{display:flex;flex-direction:column;align-items:flex-end;gap:5px}'
 '.kwo{font-family:"JetBrains Mono",ui-monospace,monospace;font-size:8.6px;color:#1E3A8A}'
)

WIN = (
 header(ICON, 'Bake plan', 'Central bakery, ingredient and pack check', '<span class="ch c-idle" id="kst">Nothing loaded</span>')
 + '<div class="k2"><div class="k2m"><div class="k2l"><div class="cd kbl" id="kbl"></div><div class="cd kal" id="kal"></div></div>'
 '<div class="cd kgs" id="kgs"></div></div><div class="cd kpo" id="kpo"></div></div>'
)

JS = r'''
var FOC='.hd>*,.kbl>*,.kal>*,.kgs>*,.kpo>*';
/* stock on hand and per unit use: flour and butter in grams, packs in units */
var IT=[['flour','Flour','kg',1000000],['butter','Butter','kg',40000],['lbag','Loaf bags','',2500],['bbag','Bun bags','',400],['rbox','Roll boxes','',150]];
var PR=[{n:'Sandwich Loaf',u:'loaves',q:2000,flour:400,butter:10,pk:'lbag',per:1,wo:'WO-5301'},
{n:'Brioche Bun',u:'buns',q:1500,flour:60,butter:12,pk:'bbag',per:6,wo:'WO-5302'},
{n:'Cinnamon Roll',u:'rolls',q:600,flour:100,butter:30,pk:'rbox',per:6,wo:'WO-5303'}];
var PO={id:'PO-7210',sup:'Cedar Dairy Supply',cs:10000,eta:'November 17',it:'butter'};
var S;
function kg(g){return (g/1000).toLocaleString('en-US',{minimumFractionDigits:3,maximumFractionDigits:3});}
function amt(k,v){return k==='flour'||k==='butter'?kg(v)+' kg':n0(v);}
function need(p,k){if(k==='flour'||k==='butter')return p.q*p[k];return p.pk===k?Math.ceil(p.q/p.per):0;}
function avail(k){var a=IT.filter(function(x){return x[0]===k;})[0][3];return a+(S.rcv&&k===PO.it?poQty():0);}
function tot(k){return PR.reduce(function(s,p){return s+need(p,k);},0);}
/* allocation in list order: each product takes what it needs from what is left; the first one that does not fit is short */
function alloc(k){var left=avail(k);return PR.map(function(p){var nd=need(p,k),got=Math.min(nd,left),sh=nd-got;left-=got;return {need:nd,left:left,short:sh};});}
function shortOf(i){var o={};IT.forEach(function(x){var a=alloc(x[0])[i];if(a.short>0)o[x[0]]=a.short;});return o;}
function isShort(i){return Object.keys(shortOf(i)).length>0;}
function anyShort(){return PR.some(function(p,i){return isShort(i);});}
function gap(){return Math.max(0,tot(PO.it)-IT[1][3]);}
function poCases(){return Math.ceil(gap()/PO.cs);}
function poQty(){return poCases()*PO.cs;}
function chip(i){if(S.wo)return '<span class="ch c-info">On the floor</span>';if(!S.chk)return '<span class="ch c-idle">Not checked</span>';return isShort(i)?'<span class="ch c-bad">Short</span>':'<span class="ch c-ok">Clear</span>';}
function render(){var b=$('kbl');
if(!S.ld){b.innerHTML='<div class="ct"><span>Bake list</span></div><div class="empt"><b>No bake list loaded</b><span>Load tomorrow\'s list to check it against stock.</span><button type="button" class="bt pri" id="kld" style="margin-top:4px">Load tomorrow\'s bake list</button></div>';}
else{b.innerHTML='<div class="ct"><span>Bake list <span class="mut" style="font-weight:400">November 17, in list order</span></span><button type="button" class="bt'+(S.rcv&&!S.wo?' pri':'')+'" id="ksf"'+(S.chk&&!anyShort()&&!S.wo?'':' disabled')+'>'+(S.wo?'Sent to floor':'Send to floor')+'</button></div>'
+'<div class="row h"><span>Product</span><span>Quantity</span><span>Status</span></div>'
+PR.map(function(p,i){return '<button type="button" class="row'+(S.sel===i?' sel':'')+(S.an?' in':'')+'" id="kr'+i+'" style="animation-delay:'+(i*80)+'ms"><span class="kpn"><b>'+p.n+'</b>'+(S.wo?'<small class="kwo" id="kw'+i+'">'+p.wo+', '+n0(p.q)+' '+p.u+'</small>':'<small>'+(i+1)+' in line</small>')+'</span><span class="mono">'+n0(p.q)+'</span><span id="kc'+i+'">'+chip(i)+'</span></button>';}).join('');}
var a=$('kal');
if(S.sel===null){a.innerHTML='<div class="ct"><span>Allocation</span></div><div class="empt"><b>No product open</b><span>Open a product to see how stock is shared out in list order.</span></div>';}
else{var i=S.sel,p=PR[i],al=alloc('butter'),so=shortOf(i),sh=so.butter||0;
a.innerHTML='<div class="ct"><span>'+p.n+' <span class="mut" style="font-weight:400">'+n0(p.q)+' '+p.u+'</span></span><span class="ch '+(sh?'c-bad':'c-ok')+'" id="kac">'+(sh?'Held back':'Clear')+'</span></div>'
+'<div class="kat"><div class="row h"><span>Butter, in list order</span><span>Needs</span><span>Left after</span></div>'
+PR.map(function(q,j){var x=al[j];return '<div class="row'+(j===i?' ksel':'')+(x.short?' kxs':'')+'"><span>'+(j+1)+'. '+q.n+'</span><span class="mono">'+kg(x.need)+'</span><span class="mono">'+(x.short?'short '+kg(x.short):kg(x.left))+'</span></div>';}).join('')+'</div>'
+'<div class="kmsg'+(sh?'':' kgo')+'" id="kmsg">'+(sh?'<b>Needs '+kg(al[i].need)+' kg butter, '+kg(al[i].need-sh)+' kg left, short '+kg(sh)+' kg.</b> Flour and roll boxes are covered.':'<b>All ingredients and packs covered.</b> Butter '+kg(avail('butter'))+' kg on hand for '+kg(tot('butter'))+' kg needed.')+'</div>'
+'<div class="knd">'+IT.filter(function(x){return need(p,x[0])>0;}).map(function(x){return '<span'+(so[x[0]]?' class="kx"':'')+'>'+x[1]+' '+amt(x[0],need(p,x[0]))+'</span>';}).join('')+'</div>'
+'<div class="kac">'+(S.po?'<span class="ch c-info">'+PO.id+' raised</span><span>'+poCases()+' cases on the way</span>':'<button type="button" class="bt pri" id="kpb"'+(sh?'':' disabled')+'>Create purchase order</button><span>for the '+kg(gap())+' kg gap</span>')+'</div>';}
var g=$('kgs');
if(!S.ld||!S.chk){g.innerHTML='<div class="ct"><span>Ingredient check</span>'+(S.ld?'<button type="button" class="bt pri" id="kck">Check ingredients</button>':'')+'</div><div class="empt"><b>Not checked yet</b><span>Flour, butter, bags and boxes, needed against what is on hand.</span></div>';}
else{g.innerHTML='<div class="ct"><span>Ingredient check <span class="mut" style="font-weight:400">needed of available</span></span><span class="ch '+(anyShort()?'c-bad':'c-ok')+'">'+(anyShort()?'1 short':'All clear')+'</span></div><div class="kgl">'
+IT.map(function(x){var k=x[0],nd=tot(k),av=avail(k),mx=Math.max(nd,av),ov=nd>av,lf=av-nd;
return '<div class="kg" id="kg-'+k+'"><div class="kgt"><b>'+x[1]+'</b><span id="kgv-'+k+'">'+amt(k,nd)+' of '+amt(k,av)+'</span></div><div class="kgb"><i class="'+(ov?'kov':'')+'" style="width:'+(nd/mx*100).toFixed(1)+'%'+(S.an2?'':';animation:none')+'"></i><u style="left:'+(av/mx*100).toFixed(1)+'%"></u></div><div class="kgs2"><span>'+(k===PO.it&&S.rcv?'Includes '+kg(poQty())+' kg on '+PO.id:k==='flour'||k==='butter'?'On hand '+kg(av)+' kg':'On hand '+n0(av))+'</span><span class="'+(ov?'kred':'kgrn')+'" id="kgs-'+k+'">'+(ov?'Short '+amt(k,nd-av):amt(k,lf)+' left')+'</span></div></div>';}).join('')
+'</div><div class="kgf"><span><i></i>Needed</span><span><u></u>Available</span><span>Allocated in list order</span></div>';}
var o=$('kpo');
if(!S.po){o.innerHTML='<div class="ct"><span>Purchase orders</span></div><div class="empt"><b>No purchase order</b><span>A shortage you raise shows up here, ready to receive.</span></div>';}
else{o.innerHTML='<div class="ct"><span>Purchase order <span class="mono">'+PO.id+'</span></span><span class="ch '+(S.rcv?'c-ok':'c-info')+'" id="kps">'+(S.rcv?'Received':'Sent to supplier')+'</span></div><div class="kps"><span class="kv"><small>Supplier</small><b>'+PO.sup+'</b><em>Butter</em></span>'
+'<span class="kv"><small>Quantity</small><b class="mono" id="kpq">'+poCases()+' cases of '+kg(PO.cs)+' kg</b><em id="kpt">'+kg(poQty())+' kg</em></span><span class="kv"><small>Expected</small><b>'+PO.eta+'</b><em>Before the shift</em></span>'
+'<span class="kpa">'+(S.rcv?'<span class="mut" style="font-size:9.4px">Received into stock, '+kg(avail('butter'))+' kg on hand</span>':'<button type="button" class="bt pri" id="krc">Receive</button>')+'</span></div>';}
var st=$('kst');st.textContent=S.wo?'3 work orders released':S.rcv?'All clear':S.chk?(anyShort()?'1 product short':'All clear'):S.ld?'Not checked':'Nothing loaded';st.className='ch '+(S.wo?'c-info':S.chk?(anyShort()?'c-bad':'c-ok'):'c-idle');
S.an=false;S.an2=false;}
function sendFloor(){if(!S.chk||anyShort()||S.wo)return false;S.wo=true;render();return true;}
winEl.addEventListener('click',function(e){var t=e.target.closest&&e.target.closest('#ksf');if(!t||mode!=='done')return;if(sendFloor()){clearHints();hot(null);turnOff();say2(5,'Three work orders on the floor',PR.map(function(p){return p.wo+' '+p.n;}).join(', ')+'.');}});
function resetState(){S={ld:false,chk:false,sel:null,po:false,rcv:false,wo:false,an:false,an2:false};render();}
var CAPAT=function(hh){return cur<=2?{l:14,t:visH()-hh-14}:{l:356,t:484-hh};};
var ST=[
{id:'load',target:function(){return $('kld');},prompt:'Click Load tomorrow\'s bake list',where:'below',run:function(){S.ld=true;S.an=true;render();},
 after:function(){return['Load tomorrow\'s bake list','3 products for November 17: '+PR.map(function(p){return n0(p.q)+' '+p.n;}).join(', ')+'. Not checked yet.'];}},
{id:'check',target:function(){return $('kck');},prompt:'Click Check ingredients',where:'below',run:function(){S.chk=true;S.an2=true;render();},
 after:function(){return['Check every ingredient and pack against stock','Flour '+kg(tot('flour'))+' of '+kg(avail('flour'))+' kg is clear. Butter needs '+kg(tot('butter'))+' kg and '+kg(avail('butter'))+' kg is on hand.'];}},
{id:'open',target:function(){return $('kr2');},prompt:'Open Cinnamon Roll, the one marked Short',where:'below',run:function(){S.sel=2;render();},
 after:function(){var a=alloc('butter')[2];return['The last product in line is the one held back','Cinnamon Roll needs '+kg(a.need)+' kg butter, '+kg(a.need-a.short)+' kg left after the loaf and the bun, short '+kg(a.short)+' kg.'];}},
{id:'po',target:function(){return $('kpb');},prompt:'Click Create purchase order',where:'above',run:function(){S.po=true;render();},
 after:function(){return['The gap becomes a purchase order',PO.id+' to '+PO.sup+': '+poCases()+' cases of '+kg(PO.cs)+' kg, '+kg(poQty())+' kg of butter, expected '+PO.eta+'.'];}},
{id:'rcv',target:function(){return $('krc');},prompt:'Click Receive',where:'above',run:function(quick){S.rcv=true;render();
 if(mode==='watch'&&!quick){later(function(){var b=$('ksf');if(b){moveGhost(gpos(b));later(function(){ghost.classList.add('pr');b.classList.add('fakehover','press');},700);later(function(){ghost.classList.remove('pr');b.classList.remove('fakehover','press');sendFloor();},1000);}},900);}
 else if(mode==='try'){later(function(){var b=$('ksf');if(mode==='done'&&b&&!S.wo){b.classList.add('hint');hot(b,false);prompt2('Now send the list to the floor',b,'below');}},1600);}},
 after:function(){return['Receive it and the bake list clears','Butter '+kg(avail('butter'))+' kg on hand for '+kg(tot('butter'))+' kg needed, '+kg(avail('butter')-tot('butter'))+' kg spare. Send to floor makes three work orders.'];}}];
'''
