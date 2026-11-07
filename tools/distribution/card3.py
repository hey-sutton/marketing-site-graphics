"""Distribution card 3: Procurement Management. Layout: reorder suggestions grouped by vendor and the open purchase orders on the left,
a status strip, the purchase order and a landed cost panel on the right."""
SUMMARY = 'Procurement Management (reorder suggestions grouped by vendor, a purchase order made from them, approval by the purchasing manager, a partial delivery received, freight and duty spread into landed cost)'
ARIA = 'Interactive product screen: review reorder suggestions grouped by vendor, create purchase order PO-4410 for Atlas Fastener Co, send it for approval, approve it, receive 120 of 200 kits and add freight and duty to see landed cost per unit'
STEPS = 6
STUDIO = dict(lede='A typical purchasing screen, built on your Sutton data with Studio. Want it different? Describe the change.',
              examples=['A vendor lead time board', 'A freight allocation rule', 'PO approval by buyer', 'A price break check'],
              built_on='Vendors, items, purchase orders and receipts', change='Rules, fields and views')

CSS = (
 '.b3{display:grid;grid-template-columns:292px 1fr;gap:12px;padding:12px 40px 0 16px;height:596px}'
 '.col{display:flex;flex-direction:column;gap:10px;min-height:0}'
 '.sug{flex:none}.sug .pd{padding:10px 11px}.vg+.vg{border-top:1px solid #E4E4E7}.vh{display:flex;align-items:center;gap:6px;min-height:28px;padding:0 11px;background:#FAFAFA;font-size:10px;font-weight:600}.vh .mut{font-weight:400;font-size:9px}'
 '.sug .row{grid-template-columns:48px 1fr 66px;min-height:24px;font-size:9.6px}.sug .fs{display:grid;grid-template-columns:52px 52px 1fr auto;gap:6px;align-items:end;padding:6px 11px 8px}'
 '.ops{flex:1 1 0;min-height:0}.ops .row{grid-template-columns:52px 1fr 88px;min-height:23px;font-size:9.6px;white-space:nowrap}.rul{flex:none}.rul .row{grid-template-columns:1fr auto;min-height:23px;font-size:9.6px}'
 '.stg{display:flex;align-items:center;gap:4px;padding:0 2px;height:28px;flex:none}.stg .s{display:flex;align-items:center;gap:5px;font-size:9.4px;color:#A1A1AA;white-space:nowrap}.stg .s i{width:15px;height:15px;border-radius:50%;border:1px solid #D4D4D8;display:flex;align-items:center;justify-content:center;font-style:normal;font-size:8px;background:#fff}'
 '.stg .s.dn{color:#166534}.stg .s.dn i{background:#DCFCE7;border-color:#BBF7D0}.stg .s.cu{color:#18181B;font-weight:600}.stg .s.cu i{background:#18181B;border-color:#18181B;color:#fff}.stg .ln{flex:1;height:1px;background:#E4E4E7;min-width:8px}'
 '.po{flex:none}.po .pd{padding:10px 11px}.po .kvs{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;padding:8px 11px;border-bottom:1px solid #F0F0F1}'
 '.po .row{grid-template-columns:1fr 34px 40px 56px 64px;white-space:nowrap;min-height:24px;font-size:9.6px}.po .row.t{font-weight:600;background:#FAFAFA}'
 '.po .ac{display:flex;align-items:center;gap:7px;padding:7px 11px;border-top:1px solid #F0F0F1;min-height:40px}.po .ac .fld{width:58px}.po .ac .nt{font-size:9px;color:#71717A;line-height:1.35}'
 '.lc{flex:1 1 0;min-height:0}.lc .fs{display:grid;grid-template-columns:70px 70px auto;gap:7px;align-items:end;padding:8px 11px}.lc .row{grid-template-columns:1fr auto;min-height:23px;font-size:9.6px}.lc .row.t{font-weight:600;background:#FAFAFA}.lc .pd{padding:2px 11px 10px}'
)

WIN = (
 '<div class="hd"><svg width="16" height="16" viewBox="0 0 16 16" fill="none" aria-hidden="true"><path d="M3 2.5h7l3 3v8H3z" stroke="#18181B" stroke-width="1.2" stroke-linejoin="round"/><path d="M5.5 7.5h5M5.5 10h5M10 2.5v3h3" stroke="#18181B" stroke-width="1.2"/></svg>'
 '<span class="tt">Purchasing</span><span class="ch c-idle" id="hst">No draft</span><span class="sb grow">Ridgeway Supply, buyer R. Okafor</span></div>'
 '<div class="b3"><div class="col"><div class="cd sug" id="sug"></div><div class="cd rul"><div class="ct">Approval rules<span class="mut" style="font-weight:500">Purchase orders</span></div><div class="row"><span>Up to 500.00</span><span class="mut">Buyer sends it</span></div><div class="row"><span>Over 500.00</span><span>Purchasing manager, D. Reyes</span></div><div class="row"><span>New vendor</span><span>Purchasing manager first</span></div></div><div class="cd ops" id="ops"></div></div>'
 '<div class="col"><div class="stg" id="stg"></div><div class="cd po" id="po"></div><div class="cd lc" id="lc"></div></div></div>'
)

JS = r'''
var FOC='.hd>*,.rul,.sug .ct,.sug .pd,.vh,.sug .row,.sug .fs>*,.ops,.stg,.po .ct,.po .kvs,.po .row,.po .pd,.po .ac>*,.lc .ct,.lc .fs>*,.lc .row,.lc .pd';
var STG=['Draft','Awaiting approval','Sent','Partly received'],LIM=500,OH0=60;
var S;
function f2(n){return n.toLocaleString('en-US',{minimumFractionDigits:2,maximumFractionDigits:2});}
function r2(n){return Math.round(n*100)/100;}
function val(i){return String($(i).value).trim();}
function num(v){return /^\d{1,5}(\.\d{1,2})?$/.test(v)?parseFloat(v):-1;}
function int(v){return /^\d{1,4}$/.test(v)?parseInt(v,10):-1;}
function tot(){return r2(S.q*S.p);}
function lcost(){var add=r2((S.fr+S.du)/S.rc);return{add:add,unit:r2(S.p+add),val:r2(S.rc*r2(S.p+add))};}
function render(){
var u='<div class="ct">Reorder suggestions<span class="mut" style="font-weight:500">From the buying plan</span></div>';
if(!S.sug)u+='<div class="pd"><div class="empt"><b>No suggestions loaded</b><span>Load the buying plan to see what to order, grouped by vendor.</span><button type="button" class="bt pri" id="lsug" style="margin-top:4px">Reorder suggestions</button></div></div>';
else{u+='<div class="vg'+(S.anim?' in':'')+'"><div class="vh">Atlas Fastener Co<span class="mut">Lead time 6 days</span><span class="grow"></span>'+(S.po?'<span class="ch c-info">PO-4410</span>':'')+'</div><div class="row h"><span>SKU</span><span>Item</span><span class="r">Suggested</span></div><div class="row"><span class="mono">BT-118</span><span>Hex bolt kit, 24 piece</span><span class="mono r">200 units</span></div>'+
(S.po?'':'<div class="fs frm"><label class="fld" id="fq"><small>Qty</small><input id="iq" value="'+S.v.q+'" inputmode="numeric" autocomplete="off"></label><label class="fld" id="fp"><small>Unit price</small><input id="ip" value="'+S.v.p+'" inputmode="decimal" autocomplete="off"></label><label class="fld" id="fw"><small>Ship to</small><input id="iw" value="'+S.v.w+'" autocomplete="off" spellcheck="false"><span class="em">Whole units, a price, Atlanta or Dallas</span></label><button type="button" class="bt pri" id="mkpo">Create PO</button></div>')+'</div>'+
'<div class="vg'+(S.anim?' in':'')+'" style="animation-delay:90ms"><div class="vh">Bluepoint Packaging<span class="mut">Lead time 4 days</span></div><div class="row"><span class="mono">PK-077</span><span>Pallet wrap, roll</span><span class="mono r">112 rolls</span></div></div>';}
$('sug').innerHTML=u;
$('ops').innerHTML='<div class="ct">Purchase orders<span class="mut" style="font-weight:500">Last 30 days</span></div><div class="row h"><span>PO</span><span>Vendor</span><span>Status</span></div>'+S.ops.map(function(o){return '<div class="row'+(o[4]?' in':'')+'"><span class="mono">'+o[0]+'</span><span>'+o[1]+'</span><span><span class="ch '+o[3]+'">'+o[2]+'</span></span></div>';}).join('');
$('stg').innerHTML=STG.map(function(t,i){var c=!S.po?'':i<S.st?' dn':i===S.st?' cu':'';return (i?'<span class="ln"></span>':'')+'<span class="s'+c+'"><i>'+(c===' dn'?'&#10003;':i+1)+'</i>'+(i===2&&S.st>=2?'Sent to vendor':t)+'</span>';}).join('');
var p='<div class="ct">Purchase order'+(S.po?'<span class="ch '+['c-idle','c-warn','c-info','c-info'][S.st]+'" id="pst">'+(S.st===2?'Sent to vendor':STG[S.st])+'</span>':'')+'</div>';
if(!S.po)p+='<div class="pd"><div class="empt"><b>No purchase order yet</b><span>Create one from a suggestion and the quantity and price come with it.</span></div></div>';
else{var t=tot();p+='<div class="kvs'+(S.anim?' in':'')+'"><div class="kv"><small>PO</small><b class="mono">PO-4410</b></div><div class="kv"><small>Vendor</small><b>Atlas Fastener Co</b></div><div class="kv"><small>Ship to</small><b>'+S.w+' <span class="mono mut" style="font-weight:500">'+(S.w==='Atlanta'?'WH-ATL':'WH-DAL')+'</span></b></div></div>'+
'<div class="row h"><span>Item</span><span class="r">Qty</span><span class="r">Price</span><span class="r">Amount</span><span class="r">Received</span></div>'+
'<div class="row"><span><span class="mono">BT-118</span> bolt kit</span><span class="mono r">'+S.q+'</span><span class="mono r">'+f2(S.p)+'</span><span class="mono r">'+f2(t)+'</span><span class="mono r" id="rcv">'+(S.st>=3?S.rc+' of '+S.q:'0')+'</span></div>'+
'<div class="row t"><span>Order total</span><span></span><span></span><span class="mono r" id="pot">'+f2(t)+'</span><span></span></div><div class="ac">';
if(S.st===0)p+='<button type="button" class="bt pri" id="snd">Send for approval</button><span class="nt">Orders over '+f2(LIM)+' go to the purchasing manager</span>';
else if(S.st===1)p+='<button type="button" class="bt pri" id="apv">Approve as purchasing manager</button><span class="nt">Waiting on D. Reyes'+(t>LIM?', over '+f2(LIM):'')+'</span>';
else if(S.st===2)p+='<span class="fld frm" id="fr" style="flex-direction:row;align-items:center;gap:6px;width:auto"><small style="white-space:nowrap">Arrived</small><input id="ir" value="'+S.v.r+'" inputmode="numeric" autocomplete="off" style="width:52px"><span class="em" style="position:absolute;margin-top:34px">1 to '+S.q+' units</span></span><button type="button" class="bt pri" id="rcvb">Receive delivery</button><span class="nt">Dock 1, Atlanta</span>';
else p+='<span class="ch c-ok">'+S.rc+' received</span><span class="ch c-warn" id="open">'+(S.q-S.rc)+' still on order</span><span class="ch c-info" id="stk">BT-118 on hand '+OH0+' to '+(OH0+S.rc)+'</span>';
p+='</div>';}
$('po').innerHTML=p;
var l='<div class="ct">Landed cost<span class="mut" style="font-weight:500">Per unit received</span></div><div class="fs frm"><label class="fld" id="ff"><small>Freight</small><input id="if" value="'+S.v.f+'" inputmode="decimal" autocomplete="off"></label><label class="fld" id="fd"><small>Duty</small><input id="id" value="'+S.v.d+'" inputmode="decimal" autocomplete="off"></label>'+
(S.lc?'<button type="button" class="bt done" disabled>Added</button>':'<button type="button" class="bt pri" id="adf">Add freight and duty</button>')+'</div>';
if(!S.lc)l+='<div class="pd"><div class="empt" id="lce"><b>No landed cost yet</b><span>Receive a delivery, then add its freight and duty to see what each unit really cost.</span></div></div>';
else{var c=lcost();l+='<div class="row in"><span>Unit price</span><span class="mono">'+f2(S.p)+'</span></div><div class="row in"><span>Freight and duty, '+f2(S.fr+S.du)+' over '+S.rc+' units</span><span class="mono" id="add">'+f2(c.add)+'</span></div>'+
'<div class="row t in"><span>Landed cost per unit</span><span class="mono" id="lcu">'+f2(c.unit)+'</span></div><div class="row in"><span>Landed value of '+S.rc+' received</span><span class="mono" id="lcv">'+f2(c.val)+'</span></div><div class="row in"><span class="mut">Order value at price</span><span class="mono mut">'+f2(tot())+'</span></div>';}
$('lc').innerHTML=l;
$('hst').textContent=S.po?'PO-4410 '+(S.st===2?'sent':STG[S.st].toLowerCase()):'No draft';$('hst').className='ch '+(S.po?'c-info':'c-idle');
S.anim=false;}
$('sug').addEventListener('input',function(e){var k={iq:'q',ip:'p',iw:'w'}[e.target.id];if(k)S.v[k]=e.target.value;});
$('po').addEventListener('input',function(e){if(e.target.id==='ir')S.v.r=e.target.value;});
$('lc').addEventListener('input',function(e){var k={'if':'f',id:'d'}[e.target.id];if(k)S.v[k]=e.target.value;});
function okPo(){var q=int(val('iq')),p=num(val('ip')),w=val('iw');w=w.charAt(0).toUpperCase()+w.slice(1).toLowerCase();var bad=!(q>0&&p>0&&(w==='Atlanta'||w==='Dallas'));['fq','fp','fw'].forEach(function(i){$(i).classList.toggle('err',bad);});return !bad;}
function okR(){var r=int(val('ir')),bad=!(r>0&&r<=S.q);$('fr').classList.toggle('err',bad);return !bad;}
function okL(){var a=num(val('if')),b=num(val('id')),bad=!(a>=0&&b>=0);['ff','fd'].forEach(function(i){$(i).classList.toggle('err',bad);});return !bad;}
function resetState(){S={sug:false,po:false,st:0,lc:false,anim:false,q:0,p:0,w:'',rc:0,fr:0,du:0,v:{q:'200',p:'4.10',w:'Atlanta',r:'120',f:'96.00',d:'24.00'},
ops:[['PO-4405','Bluepoint Packaging','Sent','c-info',0,'11/11'],['PO-4402','Orion Medical Supply','Received','c-ok',0,'11/07'],['PO-4399','Tenor Equipment','Partly received','c-warn',0,'11/09'],['PO-4396','Keystone Labels','Received','c-ok',0,'11/06'],['PO-4391','Atlas Fastener Co','Closed','c-idle',0,'10/28'],['PO-4388','Tenor Equipment','Closed','c-idle',0,'09/18'],['PO-4384','Bluepoint Packaging','Closed','c-idle',0,'09/12'],['PO-4379','Orion Medical Supply','Closed','c-idle',0,'09/05'],['PO-4372','Keystone Labels','Closed','c-idle',0,'08/29']]};render();}
function setOp(st,c){S.ops[0][2]=st;S.ops[0][3]=c;}
var CAPAT=function(hh){return{l:14,t:visH()-hh-14};};
var ST=[
{id:'sug',target:function(){return $('lsug');},prompt:'Click Reorder suggestions',where:'below',run:function(){S.sug=true;S.anim=true;render();},after:['Reorder suggestions arrive grouped by vendor, ready to order','Atlas Fastener Co: 200 units of BT-118. Bluepoint Packaging: 112 rolls of PK-077.']},
{id:'mkpo',target:function(){return $('mkpo');},prompt:'Click Create PO',where:'below',ok:okPo,
 run:function(){var w=val('iw');S.q=int(val('iq'));S.p=num(val('ip'));S.w=w.charAt(0).toUpperCase()+w.slice(1).toLowerCase();S.po=true;S.st=0;S.anim=true;S.ops.unshift(['PO-4410','Atlas Fastener Co','Draft','c-idle',1,'11/13']);render();},
 after:function(){return['The suggestion becomes a purchase order with quantity and price already in','Draft PO-4410: '+S.q+' at '+f2(S.p)+', total '+f2(tot())+', ship to '+S.w+'.'];}},
{id:'snd',target:function(){return $('snd');},prompt:'Click Send for approval',where:'below',run:function(){S.st=1;setOp('Awaiting approval','c-warn');render();},
 after:function(){return['Approval rules send larger orders to the right person first',tot()>LIM?f2(tot())+' is over '+f2(LIM)+', so it waits on the purchasing manager.':'It waits on the purchasing manager.'];}},
{id:'apv',target:function(){return $('apv');},prompt:'Click Approve as purchasing manager',where:'below',run:function(){S.st=2;setOp('Sent','c-info');render();},after:['Approved and on its way to the vendor','D. Reyes approved PO-4410 and it was sent to Atlas Fastener Co.']},
{id:'rcv',target:function(){return $('rcvb');},prompt:'Click Receive delivery',where:'below',ok:okR,run:function(){okR();S.rc=int(val('ir'));S.st=3;setOp('Partly received','c-warn');render();},
 after:function(){return['A partial delivery is received line by line and the rest stays open',S.rc+' of '+S.q+' received, '+(S.q-S.rc)+' still on order. BT-118 stock goes up by '+S.rc+'.'];}},
{id:'lc',target:function(){return $('adf');},prompt:'Click Add freight and duty',where:'below',ok:okL,run:function(){okL();S.fr=num(val('if'));S.du=num(val('id'));S.lc=true;render();},
 after:function(){var c=lcost();return['Freight and duties are spread across what arrived, so each unit carries what it really cost','('+f2(S.fr)+' + '+f2(S.du)+') / '+S.rc+' = '+f2(c.add)+' a unit. Landed cost '+f2(c.unit)+', '+f2(c.val)+' for the '+S.rc+' received.'];}}];
'''
