"""Plastics card 2: Resin Lot Traceability. Layout: a left to right trace diagram (material lots, runs, finished lots, customers) with the traced
path drawn bold, a trace form and an activity log on the left, and a detail panel on the right. Rounding: whole pounds and whole caps."""
SUMMARY = 'Resin Lot Traceability (a finished lot traced back to its resin lot, the runs that used it, forward to every customer, what is still on hand, a hold, the customer list exported)'
ARIA = 'Interactive product screen: trace finished lot FL-7714 back to resin lot L-55120, open the lot and its three runs, trace forward to three customers, find the resin and caps still on hand, place them on hold and export the affected customer list'
STEPS = 6
STUDIO = dict(lede='A typical lot trace screen, built on your Sutton data with Studio. Want it different? Describe the change.',
              examples=['A recall notice by customer', 'A resin lot age report', 'A supplier quality view', 'A hold release approval'],
              built_on='Lots, runs, receipts and shipments', change='Diagrams, fields and views')

CSS = (
 '.b2{display:flex;flex-direction:column;gap:10px;padding:12px 40px 0 16px;height:596px}'
 '.net .hdr{display:grid;grid-template-columns:166px 146px 160px 1fr;padding:6px 6px 0;font-size:8.4px;color:#A1A1AA;font-weight:600;text-transform:uppercase;letter-spacing:.04em}'
 '.net .cv{position:relative;height:176px;margin:4px 0 6px}.net svg{position:absolute;left:0;top:0;width:100%;height:100%;overflow:visible}'
 '.net path{fill:none;stroke:#E4E4E7;stroke-width:1.2;transition:stroke .35s,stroke-width .35s}.net path.on{stroke:#18181B;stroke-width:2.4}'
 '.nd{position:absolute;border:1px solid #E4E4E7;border-radius:7px;background:#fff;padding:2px 8px;display:flex;flex-direction:column;justify-content:center;transition:opacity .35s,border-color .35s,background-color .35s,color .35s}'
 '.nd small{font-size:7.8px;color:#A1A1AA;line-height:1.2;white-space:nowrap}.nd b{font-size:9.6px;font-weight:600;white-space:nowrap;line-height:1.25}.nd b.mono{font-size:9.2px}.nd .bd{position:absolute;right:6px;top:50%;transform:translateY(-50%)}.nd.fg{border-style:dashed}'
 '.net.act .nd{opacity:.42}.net.act .nd.on{opacity:1;border-color:#18181B}.net .nd.key{background:#18181B;border-color:#18181B;color:#fff}.net .nd.key small{color:#D4D4D8}'
 '.el{position:absolute;transform:translate(-50%,-50%);background:#fff;border:1px solid #18181B;border-radius:4px;padding:1px 5px;font-family:"JetBrains Mono",ui-monospace,monospace;font-size:8.2px;white-space:nowrap}'
 '.cols{display:grid;grid-template-columns:236px 1fr;gap:12px;flex:1 1 0;min-height:0}.col{display:flex;flex-direction:column;gap:10px;min-height:0}'
 '.trc .g{padding:8px 10px;display:flex;align-items:flex-end;gap:7px}.trc .fld{flex:1}'
 '.log{flex:1 1 0;min-height:0}.log .row{grid-template-columns:36px 1fr;min-height:23px;font-size:9.4px}'
 '.det{flex:1 1 0;min-height:0;display:flex;flex-direction:column}.det .pd{padding:9px 11px}.det .lh{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;padding:8px 11px;border-bottom:1px solid #F0F0F1}'
 '.det .row{grid-template-columns:78px 1fr 1fr 66px;min-height:24px;font-size:9.6px;white-space:nowrap}.det .row.sel{background:#FAFAFA;box-shadow:inset 3px 0 0 #18181B}.det .row.t{font-weight:600;background:#FAFAFA}'
 '.det .ca{display:flex;align-items:center;gap:6px}.det .ca .bt{padding:3px 9px}.det .nt{padding:8px 11px;font-size:9.2px;color:#71717A;line-height:1.4}'
)

WIN = (
 '<div class="hd"><svg width="16" height="16" viewBox="0 0 16 16" fill="none" aria-hidden="true"><circle cx="3" cy="8" r="1.8" stroke="#18181B" stroke-width="1.2"/><circle cx="8" cy="8" r="1.8" stroke="#18181B" stroke-width="1.2"/><circle cx="13" cy="4" r="1.8" stroke="#18181B" stroke-width="1.2"/><circle cx="13" cy="12" r="1.8" stroke="#18181B" stroke-width="1.2"/><path d="M4.8 8h1.4M9.6 7.2l1.8-2.2M9.6 8.8l1.8 2.2" stroke="#18181B" stroke-width="1.2"/></svg>'
 '<span class="tt">Lot trace</span><span class="ch c-idle" id="hst">Nothing traced</span><span class="sb grow">Ridgeway Plastics, resin to customer</span></div>'
 '<div class="b2"><div class="cd net" id="net"><div class="ct">Trace<span class="mut" style="font-weight:500" id="nsub">Material lots, runs, finished lots and customers</span></div>'
 '<div class="hdr"><span>Material lot</span><span>Run</span><span>Finished lot</span><span>Customer or stock</span></div><div class="cv" id="cvn"></div></div>'
 '<div class="cols"><div class="col">'
 '<div class="cd trc"><div class="ct">Trace back</div><div class="g frm"><label class="fld" id="ffl"><small>Finished lot a customer reported</small><input id="ifl" value="FL-7714" autocomplete="off" spellcheck="false"><span class="em">Use FL-7714</span></label><button type="button" class="bt pri" id="tb">Trace back</button></div></div>'
 '<div class="cd log" id="log"></div>'
 '</div><div class="cd det" id="det"></div></div></div>'
)

JS = r'''
var FOC='.hd>*,.net .ct,.net .hdr,.net .cv,.trc .ct,.trc .fld,.trc .bt,.log,.det .ct>span:first-child,.det .ca>*,.det .lh,.det .row,.det .pd,.det .nt';
var NODES={L:['PP-100 resin','L-55120',4,2,130,36],MB:['COL-BLK masterbatch','MB-3318',4,46,130,36],UV:['UV-02 additive','UV-0907',4,90,130,36],RG:['REG-PP regrind','REG-0412',4,134,130,36],
R08:['Run','RUN-7708',170,14,112,38],R14:['Run','RUN-7714',170,70,112,38],R19:['Run','RUN-7719',170,126,112,38],
F08:['Finished lot','FL-7708',316,14,128,38],F14:['Finished lot','FL-7714',316,70,128,38],F19:['Finished lot','FL-7719',316,126,128,38],
AL:['Customer','Alder Beverage',476,2,164,36],PW:['Customer','Pinewood Foods',476,46,164,36],HD:['Customer','Harbor Dairy',476,90,164,36],FG:['Stock, bin FG-1','On hand',476,134,164,36]};
var EDGES=[['L','R08'],['L','R14'],['L','R19'],['MB','R14'],['UV','R14'],['RG','R14'],['MB','R08'],['RG','R19'],['R08','F08'],['R14','F14'],['R19','F19'],['F08','AL'],['F08','PW'],['F14','AL'],['F14','HD'],['F19','PW'],['F19','HD'],['F19','FG']];
var RUNS=[['RUN-7708','FL-7708',5000,'10/09',180000],['RUN-7714','FL-7714',6500,'10/14',235000],['RUN-7719','FL-7719',3000,'10/21',110000]];
var SHIP=[['Alder Beverage','AL',[['FL-7708',120000,'10/16'],['FL-7714',100000,'10/24']]],['Pinewood Foods','PW',[['FL-7708',60000,'10/18'],['FL-7719',40000,'10/28']]],['Harbor Dairy','HD',[['FL-7714',135000,'10/22'],['FL-7719',30000,'10/30']]]];
var BINS=[['Resin','RES-02','L-55120',2500,'lb'],['Resin','RES-05','L-55120',3000,'lb'],['Finished','FG-1','FL-7719',40000,'caps']];
var RCV=20000,S;
function used(){return RUNS.reduce(function(a,x){return a+x[2];},0);}
function made(){return RUNS.reduce(function(a,x){return a+x[4];},0);}
function cust(c){return c[2].reduce(function(a,x){return a+x[1];},0);}
function shipped(){return SHIP.reduce(function(a,c){return a+cust(c);},0);}
function resinLeft(){return BINS[0][3]+BINS[1][3];}
function mid(a,b){var A=NODES[a],B=NODES[b];return{x:(A[2]+A[4]+B[2])/2,y:(A[3]+A[5]/2+B[3]+B[5]/2)/2};}
function pth(a,b){var A=NODES[a],B=NODES[b],x1=A[2]+A[4],y1=A[3]+A[5]/2,x2=B[2],y2=B[3]+B[5]/2,c=(x2-x1)/2;return 'M'+x1+' '+y1+'C'+(x1+c)+' '+y1+' '+(x2-c)+' '+y2+' '+x2+' '+y2;}
function lit(){var e={},n={};function E(a,b,l){e[a+'-'+b]=l||'';n[a]=1;n[b]=1;}
if(S.view==='back'){['L','MB','UV','RG'].forEach(function(k){E(k,'R14');});E('R14','F14');}
else if(S.view){E('L','R08','5,000 lb');E('L','R14','6,500 lb');E('L','R19','3,000 lb');
if(S.fwd){E('R08','F08');E('R14','F14');E('R19','F19');E('F08','AL');E('F08','PW');E('F14','AL');E('F14','HD');E('F19','PW');E('F19','HD');if(S.now)E('F19','FG');}}
return{e:e,n:n};}
function badge(k){var rk={R08:0,R14:1,R19:2}[k];if(rk!==undefined)return S.view&&S.view!=='back'?'<span class="mono bd" style="font-size:8.8px;color:#52525B">'+n0(RUNS[rk][2])+' lb</span>':'';if(!S.fwd)return '';for(var i=0;i<SHIP.length;i++)if(SHIP[i][1]===k)return '<span class="mono bd" style="font-size:9.4px;font-weight:600">'+n0(cust(SHIP[i]))+'</span>';
if(S.now&&k==='FG')return '<span class="ch bd '+(S.hold?'c-bad':'c-warn')+'">'+(S.hold?'Hold ':'')+'40,000</span>';
if(S.now&&k==='L')return '<span class="ch bd '+(S.hold?'c-bad':'c-warn')+'" style="right:4px">'+(S.hold?'Hold':n0(resinLeft())+' lb')+'</span>';return '';}
function render(){var L=lit(),act=!!S.view;
var h='<svg viewBox="0 0 660 176" preserveAspectRatio="none" aria-hidden="true">'+EDGES.map(function(e){var k=e[0]+'-'+e[1];return '<path d="'+pth(e[0],e[1])+'"'+(k in L.e?' class="on"':'')+'/>';}).join('')+'</svg>';
Object.keys(NODES).forEach(function(k){var n=NODES[k],key=k==='L'&&S.view;h+='<div class="nd'+(L.n[k]?' on':'')+(key?' key':'')+(k==='FG'?' fg':'')+'" style="left:'+n[2]+'px;top:'+n[3]+'px;width:'+n[4]+'px;height:'+n[5]+'px"><small>'+n[0]+'</small><b'+(/^(L|MB|UV|RG|R..|F..)$/.test(k)?' class="mono"':'')+'>'+n[1]+'</b>'+badge(k)+'</div>';});

$('cvn').innerHTML=h;$('net').classList.toggle('act',act);
$('nsub').textContent=S.view==='back'?'FL-7714 back to its material lots':S.view?(S.fwd?'L-55120 forward to every customer':'L-55120 into its runs'):'Material lots, runs, finished lots and customers';
var b=$('tb');b.disabled=!!S.view;b.className='bt '+(S.view?'done':'pri');b.textContent=S.view?'Traced':'Trace back';
$('hst').textContent=S.hold?'L-55120 on hold':S.view?(S.view==='back'?'FL-7714 traced':'L-55120 open'):'Nothing traced';$('hst').className='ch '+(S.hold?'c-bad':S.view?'c-info':'c-idle');
$('log').innerHTML='<div class="ct">Activity<span class="mut" style="font-weight:500">Quality</span></div>'+S.lg.map(function(m){return '<div class="row'+(m[2]?' in':'')+'"><span class="mono mut">'+m[0]+'</span><span>'+m[1]+'</span></div>';}).join('');
var d='',an=S.anim?' in':'';function ttl(t,ac){return '<div class="ct"><span>'+t+'</span><span class="ca">'+ac+'</span></div>';}function bt(id,t){return '<button type="button" class="bt pri" id="'+id+'">'+t+'</button>';}
function kv(a){return '<div class="lh'+an+'">'+a.map(function(x){return '<div class="kv"><small>'+x[0]+'</small><b class="mono"'+(x[2]?' id="'+x[2]+'"':'')+'>'+x[1]+'</b></div>';}).join('')+'</div>';}
if(!S.view)d='<div class="ct">Details</div><div class="pd"><div class="empt"><b>Nothing traced yet</b><span>Start from a finished lot a customer reported and trace it back to the resin it was made from.</span></div></div>';
else if(S.view==='back'){d=ttl('Finished lot <span class="mono">FL-7714</span>',bt('ol','Open lot L-55120'))+kv([['Caps','235,000'],['Made on','RUN-7714'],['Molded','10/14']])+'<div class="row h"><span>Lot</span><span>Material</span><span>Supplier</span><span></span></div>'+
[['L-55120','PP-100 polypropylene','Northfield Polymers'],['MB-3318','COL-BLK masterbatch','Kestrel Color'],['UV-0907','UV-02 additive','Kestrel Color'],['REG-0412','REG-PP regrind','Own regrind']].map(function(x,i){return '<div class="row'+(i?'':' sel')+an+'" style="animation-delay:'+(i*60)+'ms"><span class="mono">'+x[0]+'</span><span>'+x[1]+'</span><span>'+x[2]+'</span><span>'+(i?'':'<span class="ch c-warn">Resin lot</span>')+'</span></div>';}).join('');}
else if(!S.fwd){d=ttl('Resin lot <span class="mono">L-55120</span>, PP-100',bt('tf','Trace forward'))+kv([['Received 10/06',n0(RCV)+' lb','rcv'],['Used in 3 runs',n0(used())+' lb','usd'],['Left',n0(RCV-used())+' lb','lft']])+'<div class="row h"><span>Run</span><span>Finished lot</span><span>Molded</span><span class="r">Resin used</span></div>'+
RUNS.map(function(x,i){return '<div class="row'+an+'" style="animation-delay:'+(i*60)+'ms"><span class="mono">'+x[0]+'</span><span class="mono">'+x[1]+'</span><span class="mono">'+x[3]+'</span><span class="mono r">'+n0(x[2])+' lb</span></div>';}).join('')+'<div class="row t"><span>Used</span><span></span><span></span><span class="mono r">'+n0(used())+' lb</span></div>';}
else if(!S.now){d=ttl('Customers from <span class="mono">L-55120</span>',bt('wn','Where it is now'))+kv([['Finished caps',n0(made()),'mad'],['Shipped',n0(shipped()),'shp'],['Customers',String(SHIP.length)]])+'<div class="row h"><span>Customer</span><span>Finished lots</span><span></span><span class="r">Caps</span></div>'+
SHIP.map(function(c,i){return '<div class="row'+an+'" style="animation-delay:'+(i*60)+'ms;grid-template-columns:110px 1fr 0 66px"><span>'+c[0]+'</span><span class="mono">'+c[2].map(function(x){return x[0];}).join(', ')+'</span><span></span><span class="mono r" id="c-'+c[1]+'">'+n0(cust(c))+'</span></div>';}).join('');}
else if(!S.exp){d=ttl('Where <span class="mono">L-55120</span> is now',S.hold?bt('ex','Export customer list'):bt('ph','Place on hold'))+kv([['Resin left',n0(resinLeft())+' lb','rl'],['Finished on hand','40,000 caps','fh'],['Places','3']])+'<div class="row h"><span>Bin</span><span>Lot</span><span class="r">Quantity</span><span class="r">Status</span></div>'+
BINS.map(function(x,i){return '<div class="row'+an+'" style="animation-delay:'+(i*60)+'ms"><span><span class="mono">'+x[1]+'</span> <span class="mut">'+x[0]+'</span></span><span class="mono">'+x[2]+'</span><span class="mono r">'+n0(x[3])+' '+x[4]+'</span><span class="r"><span class="ch '+(S.hold?'c-bad':'c-idle')+'">'+(S.hold?'Hold':'Free')+'</span></span></div>';}).join('')+
(S.hold?'<div class="nt in"><span class="ch c-bad" id="hn">'+n0(resinLeft())+' lb and 40,000 caps out of available stock</span></div>':'');}
else{d=ttl('Affected customers',(S.hold?'<span class="ch c-bad">On hold</span>':'')+'<span class="ch c-ok" id="file">L-55120-customers.csv, '+SHIP.length+' customers</span>')+'<div class="row h"><span>Customer</span><span>Shipments</span><span></span><span class="r">Caps</span></div>'+
SHIP.map(function(c,i){return '<div class="row in" style="animation-delay:'+(i*60)+'ms;grid-template-columns:110px 1fr 0 66px"><span>'+c[0]+'</span><span class="mono">'+c[2].map(function(x){return x[0]+' '+x[2];}).join(', ')+'</span><span></span><span class="mono r">'+n0(cust(c))+'</span></div>';}).join('')+
'<div class="row t" style="grid-template-columns:110px 1fr 0 66px"><span>Shipped</span><span></span><span></span><span class="mono r">'+n0(shipped())+'</span></div><div class="nt">Each row lists the finished lots, ship dates and caps, ready to send to quality and to the customers.</div>';}
$('det').innerHTML=d;S.anim=false;}
$('ifl').addEventListener('input',function(e){S.v=e.target.value;});
function resetState(){S={view:'',fwd:false,now:false,hold:false,exp:false,anim:false,v:'FL-7714',lg:[['11/06','Lot L-55188 received, PP-100, 20,000 lb'],['11/05','Hold released on FL-7702 after review'],['11/04','Lot MB-3324 received, COL-BLK, 500 lb'],['11/03','FL-7711 shipped to Alder Beverage'],['11/02','Resin lot age check, nothing past 180 days'],['11/01','Regrind REG-0418 ground from RUN-7713']]};
$('ifl').value='FL-7714';$('ffl').classList.remove('err');render();}
function addLg(t){S.lg.unshift(['Now',t,1]);S.lg=S.lg.slice(0,7);}
var CAPAT=function(hh){return{l:14,t:visH()-hh-14};};
var ST=[
{id:'tb',target:function(){return $('tb');},prompt:'Click Trace back',where:'below',ok:function(){var b=String($('ifl').value).trim().toUpperCase()!=='FL-7714';$('ffl').classList.toggle('err',b);return !b;},
 run:function(){S.view='back';S.anim=true;addLg('Traced FL-7714 back to its material lots');render();},after:['Start from a part a customer reports and see exactly which resin lot it came from','FL-7714 was molded on RUN-7714 from four material lots. Its resin is lot L-55120.']},
{id:'ol',target:function(){return $('ol');},prompt:'Click Open lot L-55120',where:'below',run:function(){S.view='lot';S.anim=true;addLg('Opened resin lot L-55120');render();},
 after:function(){return['Open a resin lot and see every run that used it','Received '+n0(RCV)+' lb, used '+n0(used())+' lb across three runs, '+n0(RCV-used())+' lb left.'];}},
{id:'tf',target:function(){return $('tf');},prompt:'Click Trace forward',where:'below',run:function(){S.view='fwd';S.fwd=true;S.anim=true;render();},
 after:function(){return['Going the other way, you find every customer that got parts made from the same lot','Alder Beverage 220,000, Pinewood Foods 100,000 and Harbor Dairy 165,000 caps, '+n0(shipped())+' shipped.'];}},
{id:'wn',target:function(){return $('wn');},prompt:'Click Where it is now',where:'below',run:function(){S.now=true;S.anim=true;render();},
 after:function(){return['The same lot is still on the shelf, and you know where',n0(resinLeft())+' lb of resin in RES-02 and RES-05, and 40,000 finished caps in FG-1.'];}},
{id:'ph',target:function(){return $('ph');},prompt:'Click Place on hold',where:'below',run:function(){S.hold=true;addLg('Hold placed on L-55120 and FL-7719 stock');render();},
 after:function(){return['Held stock cannot be picked, run or shipped until someone releases it','The '+n0(resinLeft())+' lb and 40,000 caps drop out of available stock.'];}},
{id:'ex',target:function(){return $('ex');},prompt:'Click Export customer list',where:'below',run:function(){S.exp=true;addLg('Exported customer list for L-55120');render();},after:['The list of affected customers is ready to send','Three customers with their caps and ship dates, in L-55120-customers.csv.']}];
'''
