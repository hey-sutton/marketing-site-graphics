"""Distribution card 2: Lot & Serial Traceability. Layout: a supply network map across the top (suppliers, the two warehouses, customers)
with the traced path drawn bold, a trace form and an activity log on the left, and the unit or lot panel on the right."""
SUMMARY = 'Lot & Serial Traceability (a serial traced from supplier to customer, a lot opened to every customer, the same lot found on the shelf in both warehouses, a hold, the customer list exported)'
ARIA = 'Interactive product screen: trace pallet jack SN-7714 from Tenor Equipment to Calder Clinic, open lot L-24091 of nitrile gloves, find the 40 boxes still on the shelf in Atlanta and Dallas, place them on hold and export the list of affected customers'
STEPS = 5
STUDIO = dict(lede='A typical trace screen, built on your Sutton data with Studio. Want it different? Describe the change.',
              examples=['A recall notice by customer', 'A lot expiry watch', 'A supplier quality view', 'A warranty lookup by serial'],
              built_on='Lots, serials, receipts and shipments', change='Maps, fields and views')

CSS = (
 '.b2{display:flex;flex-direction:column;gap:10px;padding:12px 40px 0 16px;height:596px}'
 '.net .cv{position:relative;height:170px;margin:6px 0 4px}.net svg{position:absolute;left:0;top:0;width:100%;height:100%;overflow:visible}'
 '.net path{fill:none;stroke:#E4E4E7;stroke-width:1.2;transition:stroke .35s,stroke-width .35s}.net path.on{stroke:#18181B;stroke-width:2.4}.net path.hd2{stroke-dasharray:4 3}'
 '.nd{position:absolute;border:1px solid #E4E4E7;border-radius:7px;background:#fff;padding:3px 8px;display:flex;flex-direction:column;justify-content:center;transition:opacity .35s,border-color .35s,box-shadow .35s}'
 '.nd small{font-size:7.8px;color:#A1A1AA;line-height:1.2}.nd b{font-size:9.6px;font-weight:600;white-space:nowrap;line-height:1.25}.nd .bd{position:absolute;right:6px;top:50%;transform:translateY(-50%)}'
 '.net.act .nd{opacity:.45}.net.act .nd.on{opacity:1;border-color:#18181B;box-shadow:0 1px 0 rgba(0,0,0,.04)}'
 '.el{position:absolute;transform:translate(-50%,-50%);background:#fff;border:1px solid #18181B;border-radius:4px;padding:1px 5px;font-family:"JetBrains Mono",ui-monospace,monospace;font-size:8.2px;white-space:nowrap}'
 '.cols{display:grid;grid-template-columns:236px 1fr;gap:12px;flex:1 1 0;min-height:0}.col{display:flex;flex-direction:column;gap:10px;min-height:0}'
 '.trc .grp{padding:8px 10px;display:flex;align-items:flex-end;gap:7px}.trc .grp+.grp{border-top:1px solid #F0F0F1}.trc .fld{flex:1}.trc .bt{width:84px}'
 '.log{flex:1 1 0;min-height:0}.log .row{grid-template-columns:36px 1fr;min-height:23px;font-size:9.4px}'
 '.det{flex:1 1 0;min-height:0;display:flex;flex-direction:column}.det .pd{padding:9px 11px}.det .lh{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;padding:8px 11px;border-bottom:1px solid #F0F0F1}'
 '.det .row{grid-template-columns:1fr 62px 46px 40px;min-height:22px;font-size:9.6px}.det .row.t{font-weight:600;background:#FAFAFA}.det .sh{padding:5px 11px 3px;font-size:8.8px;color:#71717A;font-weight:600;border-top:1px solid #F0F0F1}'
 '.det .ev .row{grid-template-columns:40px 1fr}.det .ca{display:flex;align-items:center;gap:6px}.det .ca .bt{padding:3px 9px}.det .sh{display:flex;align-items:center;min-height:22px}'
)

WIN = (
 '<div class="hd"><svg width="16" height="16" viewBox="0 0 16 16" fill="none" aria-hidden="true"><circle cx="3.5" cy="8" r="1.8" stroke="#18181B" stroke-width="1.2"/><circle cx="12.5" cy="4" r="1.8" stroke="#18181B" stroke-width="1.2"/><circle cx="12.5" cy="12" r="1.8" stroke="#18181B" stroke-width="1.2"/><path d="M5.3 7.4l5.4-2.6M5.3 8.6l5.4 2.6" stroke="#18181B" stroke-width="1.2"/></svg>'
 '<span class="tt">Trace</span><span class="ch c-idle" id="hst">Nothing traced</span><span class="sb grow">Ridgeway Supply, suppliers to customers</span></div>'
 '<div class="b2"><div class="cd net" id="net"><div class="ct">Supply network<span class="mut" style="font-weight:500" id="nsub">Suppliers, warehouses and customers</span></div><div class="cv" id="cvn"></div></div>'
 '<div class="cols"><div class="col">'
 '<div class="cd trc"><div class="ct">Trace</div>'
 '<div class="grp frm"><label class="fld" id="fsn"><small>Serial number</small><input id="isn" value="SN-7714" autocomplete="off" spellcheck="false"><span class="em">Use SN-7714</span></label><button type="button" class="bt pri" id="trs">Trace serial</button></div>'
 '<div class="grp frm"><label class="fld" id="flt"><small>Lot</small><input id="ilt" value="L-24091" autocomplete="off" spellcheck="false"><span class="em">Use L-24091</span></label><button type="button" class="bt pri" id="opl">Open lot</button></div></div>'
 '<div class="cd log" id="log"></div>'
 '</div><div class="cd det" id="det"></div></div></div>'
)

JS = r'''
var FOC='.hd>*,.net .ct,.net .cv,.trc .ct,.trc .fld,.trc .bt,.log,.det .ct,.det .lh,.det .row,.det .sh,.det .ca>*,.det .pd';
var NODES={ten:['Supplier','Tenor Equipment',10,8,140,34],ori:['Supplier','Orion Medical Supply',10,68,140,34],atl:['Supplier','Atlas Fastener Co',10,128,140,34],
ATL:['Warehouse WH-ATL','Atlanta',252,28,150,38],DAL:['Warehouse WH-DAL','Dallas',252,104,150,38],
cal:['Customer','Calder Clinic',500,0,140,30],eas:['Customer','Eastside Dental',500,35,140,30],mar:['Customer','Marlow Health',500,70,140,30],kes:['Customer','Kestrel Dental',500,105,140,30],nor:['Customer','Northgate Retail',500,140,140,30]};
var EDGES=[['ten','ATL'],['ori','ATL'],['ori','DAL'],['atl','DAL'],['atl','ATL'],['ATL','cal'],['ATL','eas'],['ATL','mar'],['ATL','kes'],['DAL','kes'],['DAL','nor'],['DAL','cal'],['ATL','DAL']];
var LOT=[['cal','Calder Clinic','SO-6131',120,'10/16'],['eas','Eastside Dental','SO-6140',80,'10/20'],['mar','Marlow Health','SO-6152',100,'10/24'],['kes','Kestrel Dental','SO-6163',60,'10/29']];
var REM=[['ATL','Atlanta','A-04-2',30],['DAL','Dallas','D-02-3',10]],RCV=400,AV0=190;
var S;
function shipped(){return LOT.reduce(function(a,x){return a+x[3];},0);}
function left(){return REM.reduce(function(a,x){return a+x[3];},0);}
function mid(a,b){var A=NODES[a],B=NODES[b];if(a==='ATL'&&b==='DAL')return{x:A[2]+A[4]/2,y:(A[3]+A[5]+B[3])/2};return{x:(A[2]+A[4]+B[2])/2,y:(A[3]+A[5]/2+B[3]+B[5]/2)/2};}
function pth(a,b){var A=NODES[a],B=NODES[b];if(a==='ATL'&&b==='DAL'){var x=A[2]+A[4]/2;return 'M'+x+' '+(A[3]+A[5])+'L'+x+' '+B[3];}var x1=A[2]+A[4],y1=A[3]+A[5]/2,x2=B[2],y2=B[3]+B[5]/2,c=(x2-x1)/2;return 'M'+x1+' '+y1+'C'+(x1+c)+' '+y1+' '+(x2-c)+' '+y2+' '+x2+' '+y2;}
function onEdges(){if(S.view==='sn')return{'ten-ATL':'09/18 PO-4388','ATL-cal':'10/03 SO-6120'};if(S.view!=='lot')return{};var e={'ori-ATL':'10/12, 400'};LOT.forEach(function(x){e['ATL-'+x[0]]='';});if(S.now)e['ATL-DAL']='10';return e;}
function onNodes(){if(S.view==='sn')return{ten:1,ATL:1,cal:1};if(S.view!=='lot')return{};var n={ori:1,ATL:1};LOT.forEach(function(x){n[x[0]]=1;});if(S.now)n.DAL=1;return n;}
function badge(k){if(S.view!=='lot')return '';for(var i=0;i<LOT.length;i++)if(LOT[i][0]===k)return '<span class="mono bd" style="font-size:9.6px;font-weight:600">'+LOT[i][3]+'</span>';
if(S.now)for(var j=0;j<REM.length;j++)if(REM[j][0]===k)return '<span class="ch bd '+(S.hold?'c-bad':'c-warn')+'">'+(S.hold?'Hold '+REM[j][3]:REM[j][3]+' left')+'</span>';return '';}
function render(){var oe=onEdges(),on=onNodes(),act=S.view!=='';
var svg='<svg viewBox="0 0 660 170" preserveAspectRatio="none" aria-hidden="true">'+EDGES.map(function(e){var k=e[0]+'-'+e[1];return '<path d="'+pth(e[0],e[1])+'"'+(k in oe?' class="on'+(k==='ATL-DAL'?' hd2':'')+'"':'')+'/>';}).join('')+'</svg>';
var h=svg;Object.keys(NODES).forEach(function(k){var n=NODES[k];h+='<div class="nd'+(on[k]?' on':'')+'" style="left:'+n[2]+'px;top:'+n[3]+'px;width:'+n[4]+'px;height:'+n[5]+'px"><small>'+n[0]+'</small><b>'+n[1]+'</b>'+badge(k)+'</div>';});
Object.keys(oe).forEach(function(k){if(!oe[k])return;var p=k.split('-'),m=mid(p[0],p[1]);h+='<span class="el'+(S.anim?' in':'')+'" style="left:'+m.x+'px;top:'+m.y+'px">'+oe[k]+'</span>';});
$('cvn').innerHTML=h;$('net').classList.toggle('act',act);
$('nsub').textContent=S.view==='sn'?'SN-7714, supplier to customer':S.view==='lot'?'Lot L-24091, every unit':'Suppliers, warehouses and customers';
[['trs','sn','Traced','Trace serial'],['opl','lot','Opened','Open lot']].forEach(function(b){var e=$(b[0]),d=S.did[b[1]];e.disabled=!!d;e.className='bt '+(d?'done':'pri');e.textContent=d?b[2]:b[3];});
$('hst').textContent=S.hold?'Lot on hold':S.view==='lot'?'L-24091 open':S.view==='sn'?'SN-7714 traced':'Nothing traced';$('hst').className='ch '+(S.hold?'c-bad':S.view?'c-info':'c-idle');
$('log').innerHTML='<div class="ct">Activity<span class="mut" style="font-weight:500">Quality</span></div>'+S.lg.map(function(m){return '<div class="row'+(m[2]?' in':'')+'"><span class="mono mut">'+m[0]+'</span><span>'+m[1]+'</span></div>';}).join('');
var d='';
if(!S.view)d='<div class="ct">Details</div><div class="pd"><div class="empt"><b>Nothing traced yet</b><span>Trace a serial or open a lot to see where it came from and where it went.</span></div></div>';
else if(S.view==='sn')d='<div class="ct"><span>Pallet jack <span class="mono">SN-7714</span></span><span class="ch c-ok">Shipped</span></div><div class="lh'+(S.anim?' in':'')+'"><div class="kv"><small>Supplier</small><b>Tenor Equipment</b></div><div class="kv"><small>Received</small><b class="mono">PO-4388</b></div><div class="kv"><small>Customer</small><b>Calder Clinic</b></div></div>'+
'<div class="ev">'+[['09/18','Received on PO-4388 from Tenor Equipment, Atlanta dock 1'],['09/18','Put away to bin C-05-1, Atlanta'],['10/02','Picked for SO-6120, scanned SN-7714'],['10/03','Shipped to Calder Clinic, BL-3188']].map(function(e,i){return '<div class="row'+(S.anim?' in':'')+'" style="animation-delay:'+(i*70)+'ms"><span class="mono mut">'+e[0]+'</span><span>'+e[1]+'</span></div>';}).join('')+'</div>';
else{var ac;if(!S.now)ac='<button type="button" class="bt pri" id="wnow">Where it is now</button>';else if(!S.hold)ac='<button type="button" class="bt pri" id="hold">Place on hold</button>';else ac=S.exp?'<span class="ch c-ok" id="file">L-24091-customers.csv, '+LOT.length+' customers</span>':'<button type="button" class="bt pri" id="exp">Export customer list</button>';
d='<div class="ct"><span>Lot <span class="mono">L-24091</span>, GL-210 gloves</span><span class="ca"><span class="ch '+(S.hold?'c-bad':'c-warn')+'">'+(S.hold?'On hold':'Open')+'</span>'+ac+'</span></div>'+
'<div class="lh"><div class="kv"><small>Received 10/12</small><b class="mono" id="rcv">'+RCV+'</b></div><div class="kv"><small>Shipped to customers</small><b class="mono" id="shp">'+shipped()+'</b></div><div class="kv"><small>Still on the shelf</small><b class="mono" id="lft">'+(S.now?left():'Not checked')+'</b></div></div>'+
'<div class="row h"><span>Customer</span><span>Order</span><span class="r">Boxes</span><span class="r">Shipped</span></div>'+
LOT.map(function(x,i){return '<div class="row'+(S.anim?' in':'')+'" style="animation-delay:'+(i*60)+'ms"><span>'+x[1]+'</span><span class="mono">'+x[2]+'</span><span class="mono r">'+x[3]+'</span><span class="mono r">'+x[4]+'</span></div>';}).join('')+
'';
if(S.now){d+='<div class="sh">Where it is now'+(S.hold?'<span class="ch c-bad" style="margin-left:8px">GL-210 available <span class="mono" id="av2">'+AV0+' to '+(AV0-left())+'</span></span>':'')+'</div>'+REM.map(function(x){return '<div class="row in"><span>'+x[1]+'</span><span class="mono">'+x[2]+'</span><span class="mono r">'+x[3]+'</span><span class="r"><span class="ch '+(S.hold?'c-bad':'c-idle')+'">'+(S.hold?'Hold':'Free')+'</span></span></div>';}).join('');}
}
$('det').innerHTML=d;S.anim=false;}
function resetState(){S={view:'',now:false,hold:false,exp:false,did:{},anim:false,lg:[['11/06','Lot L-23987 closed, all units shipped'],['11/05','Received lot L-24102, TW-330, 240 cases'],['11/04','Serial SN-7690 returned, checked and restocked'],['11/03','Lot L-23955 expiry check, nothing due'],['11/02','Received lot L-24088, LB-502, 600 rolls']]};
$('isn').value='SN-7714';$('ilt').value='L-24091';$('fsn').classList.remove('err');$('flt').classList.remove('err');render();}
function addLg(t){S.lg.unshift(['Now',t,1]);S.lg=S.lg.slice(0,6);}
function v(i){return String($(i).value).trim().toUpperCase();}
var CAPAT=function(hh){return{l:14,t:visH()-hh-14};};
var ST=[
{id:'trs',target:function(){return $('trs');},prompt:'Click Trace serial',where:'below',ok:function(){var b=v('isn')!=='SN-7714';$('fsn').classList.toggle('err',b);return !b;},
 run:function(){S.view='sn';S.did.sn=1;S.anim=true;addLg('Traced serial SN-7714');render();},after:['Pick a serial and see its whole path, from supplier to customer','SN-7714 came from Tenor Equipment on 09/18 and shipped to Calder Clinic on 10/03.']},
{id:'opl',target:function(){return $('opl');},prompt:'Click Open lot',where:'below',ok:function(){var b=v('ilt')!=='L-24091';$('flt').classList.toggle('err',b);return !b;},
 run:function(){S.view='lot';S.did.lot=1;S.anim=true;addLg('Opened lot L-24091, GL-210');render();},after:function(){return['Open a lot and see where every unit went',RCV+' boxes received, '+shipped()+' shipped to four customers: 120, 80, 100 and 60.'];}},
{id:'wnow',target:function(){return $('wnow');},prompt:'Click Where it is now',where:'below',run:function(){S.now=true;S.anim=true;render();},after:function(){return['The same lot is still on the shelf in two warehouses','Atlanta A-04-2 holds 30 and Dallas D-02-3 holds 10, '+left()+' boxes in all.'];}},
{id:'hold',target:function(){return $('hold');},prompt:'Click Place on hold',where:'below',run:function(){S.hold=true;addLg('Hold placed on L-24091, '+left()+' boxes');render();},after:function(){return['Held stock cannot be picked or sold until someone releases it','All '+left()+' boxes are on hold, so GL-210 available to sell drops from '+AV0+' to '+(AV0-left())+'.'];}},
{id:'exp',target:function(){return $('exp');},prompt:'Click Export customer list',where:'below',run:function(){S.exp=true;addLg('Exported customer list for L-24091');render();},after:['The list of affected customers is ready to send','Four customers, their orders, boxes and ship dates, in L-24091-customers.csv.']}];
'''
