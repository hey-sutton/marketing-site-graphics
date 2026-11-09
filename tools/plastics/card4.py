"""Plastics card 4: Shortages & Resin Purchasing. Layout: a status strip across the top, a planning grid with coverage bars and the demand by run
for the chosen item on the left, the purchase order and the approval rules on the right. Rounding: whole pounds, money to cents."""
SUMMARY = 'Shortages & Resin Purchasing (shortages across scheduled runs, the runs competing for the same resin, a purchase order from the shortage, approval, a partial receipt by gaylord)'
ARIA = 'Interactive product screen: filter the planning grid to shortages, open PP-100 to see demand by run, create purchase order PO-4520 for 14,000 lb from Northfield Polymers, send it for approval, approve it and receive 6 gaylords'
STEPS = 6
STUDIO = dict(lede='A typical material planning screen, built on your Sutton data with Studio. Want it different? Describe the change.',
              examples=['A resin lead time board', 'A colorant reorder rule', 'A PO approval by buyer', 'A gaylord receiving screen'],
              built_on='Items, runs, BOMs and purchase orders', change='Rules, fields and views')

CSS = (
 '.b4{display:flex;flex-direction:column;gap:10px;padding:10px 40px 0 16px;height:596px}'
 '.stg{display:flex;align-items:center;gap:4px;height:24px;flex:none}.stg .s{display:flex;align-items:center;gap:5px;font-size:9.4px;color:#A1A1AA;white-space:nowrap}.stg .s i{width:15px;height:15px;border-radius:50%;border:1px solid #D4D4D8;display:flex;align-items:center;justify-content:center;font-style:normal;font-size:8px;background:#fff}'
 '.stg .s.dn{color:#166534}.stg .s.dn i{background:#DCFCE7;border-color:#BBF7D0}.stg .s.cu{color:#18181B;font-weight:600}.stg .s.cu i{background:#18181B;border-color:#18181B;color:#fff}.stg .ln{flex:1;height:1px;background:#E4E4E7;min-width:10px}.stg .po{margin-left:10px;font-size:9.4px;color:#71717A}'
 '.cols{display:grid;grid-template-columns:minmax(0,1fr) 248px;gap:12px;flex:1 1 0;min-height:0}.col{display:flex;flex-direction:column;gap:10px;min-height:0;min-width:0}'
 '.flt{display:flex;align-items:center;gap:6px}.fc{border:1px solid #E4E4E7;border-radius:999px;background:#fff;padding:3px 9px;font-size:9.4px;cursor:pointer;transition:background-color .2s,border-color .2s,color .2s}.fc b{font-weight:600;margin-left:4px}.fc.on{background:#18181B;border-color:#18181B;color:#fff}'
 '.pln{flex:none}.pln .row{grid-template-columns:92px 50px 52px 62px 52px 1fr;min-height:30px;font-size:9.6px;white-space:nowrap;gap:6px}.pln .row span:nth-child(n+2):nth-child(-n+5){text-align:right}.pln .neg{color:#B91C1C;font-weight:600}'
 '.cov{height:6px;border-radius:3px;background:#F4F4F5;overflow:hidden}.cov i{display:block;height:100%;border-radius:3px;transition:width .5s ease,background-color .35s}'
 '.dem{flex:1 1 0;min-height:0}.dem .pd{padding:10px 11px}.dem .row{grid-template-columns:62px 40px 1fr 56px 60px 74px;min-height:27px;font-size:9.6px;white-space:nowrap;gap:6px}.dem .row span:nth-child(4),.dem .row span:nth-child(5){text-align:right}'
 '.db{height:8px;border-radius:2px;background:#E4E4E7}.db.cv{background:#18181B}.db.sh{background:#F87171}.db.oo{background:#93C5FD}.dem .nt{padding:7px 11px;font-size:9.2px;color:#52525B;line-height:1.45;border-top:1px solid #F0F0F1}'
 '.po2{flex:none}.po2 .pd{padding:10px 11px}.po2 .g{display:flex;flex-direction:column;gap:6px;padding:8px 10px}.po2 .two{display:grid;grid-template-columns:1fr 1fr;gap:6px}.po2 .bw{padding:0 10px 9px}.po2 .bw .bt{width:100%}'
 '.po2 .kvs{display:grid;grid-template-columns:1fr 1fr;gap:7px 8px;padding:8px 10px;border-bottom:1px solid #F0F0F1}.po2 .ac{padding:8px 10px;display:flex;flex-direction:column;gap:6px}.po2 .ac .bt{width:100%}.po2 .ac .nt{font-size:9px;color:#71717A;line-height:1.35}.po2 .ac .ch{align-self:flex-start}'
 '.rul{flex:none}.rcp{flex:1 1 0;min-height:0}.rcp .row{grid-template-columns:36px 64px 1fr;min-height:23px;font-size:9.4px;white-space:nowrap}.rul .row{grid-template-columns:1fr auto;min-height:23px;font-size:9.4px;white-space:nowrap}'
)

WIN = (
 '<div class="hd"><svg width="16" height="16" viewBox="0 0 16 16" fill="none" aria-hidden="true"><path d="M2.5 13.5h11" stroke="#18181B" stroke-width="1.2"/><rect x="3.5" y="8" width="2" height="5.5" stroke="#18181B" stroke-width="1.1"/><rect x="7" y="5" width="2" height="8.5" stroke="#18181B" stroke-width="1.1"/><rect x="10.5" y="2.5" width="2" height="11" stroke="#18181B" stroke-width="1.1"/></svg>'
 '<span class="tt">Material planning</span><span class="ch c-idle" id="hst">4 materials</span><span class="sb grow">Ridgeway Plastics, scheduled runs through 11/18</span></div>'
 '<div class="b4"><div class="stg" id="stg"></div><div class="cols"><div class="col"><div class="cd pln" id="pln"></div><div class="cd dem" id="dem"></div></div>'
 '<div class="col"><div class="cd po2" id="po"></div><div class="cd rul"><div class="ct">Approval rules<span class="mut" style="font-weight:500">Purchase orders</span></div>'
 '<div class="row"><span>Up to 5,000.00</span><span class="mut">Buyer sends it</span></div><div class="row"><span>Over 5,000.00</span><span>Purchasing manager</span></div><div class="row"><span>New supplier</span><span>Purchasing manager first</span></div><div class="row"><span>Resin lot on receipt</span><span>Quality checks the lot</span></div></div>'
 '<div class="cd rcp"><div class="ct">Recent receipts<span class="mut" style="font-weight:500">Materials</span></div><div class="row"><span class="mono mut">11/06</span><span class="mono">L-55188</span><span>PP-100, 20 gaylords</span></div><div class="row"><span class="mono mut">11/04</span><span class="mono">MB-3324</span><span>COL-BLK, 500 lb</span></div>'
 '<div class="row"><span class="mono mut">10/29</span><span class="mono">UV-0911</span><span>UV-02, 50 lb</span></div><div class="row"><span class="mono mut">10/24</span><span class="mono">L-55160</span><span>PP-100, 16 gaylords</span></div><div class="row"><span class="mono mut">10/20</span><span class="mono">CB-1180</span><span>CTN-1000, 1,200 cartons</span></div><div class="row"><span class="mono mut">10/09</span><span class="mono">UV-0907</span><span>UV-02, 50 lb</span></div><div class="row"><span class="mono mut">10/08</span><span class="mono">MB-3318</span><span>COL-BLK, 400 lb</span></div><div class="row"><span class="mono mut">10/06</span><span class="mono">L-55120</span><span>PP-100, 20 gaylords</span></div></div></div></div></div>'
)

JS = r'''
var FOC='.hd>*,.rcp,.stg,.pln .ct>span:first-child,.flt>*,.pln .row,.dem,.po2 .ct,.po2 .pd,.po2 .g>*,.po2 .bw,.po2 .kvs,.po2 .ac>*,.rul';
var IT0=[['PP-100','lb','Polypropylene',11000,0,24500],['COL-BLK','lb','Black masterbatch',150,0,340],['UV-02','lb','UV additive',40,0,38],['CTN-1000','cartons','Caps carton',600,0,480]];
var RUNS=[['RUN-7720','11/10',1100],['RUN-7722','11/12',9200],['RUN-7725','11/14',8400],['RUN-7731','11/18',5800]];
var STG=['Draft','Awaiting approval','Sent to supplier','Partly received'],LIM=5000,GAY=1000;
var S;
function r2(n){return Math.round((n+1e-9)*100)/100;}
function f2(n){return n.toLocaleString('en-US',{minimumFractionDigits:2,maximumFractionDigits:2});}
function sg(n){return (n<0?'−':'')+n0(Math.abs(n));}
function net(x){return x[3]+x[4]-x[5];}
function pp(){return S.it[0];}
function val(i){return String($(i).value).trim();}
function int(v){v=String(v).replace(/,/g,'').trim();return /^\d{1,6}$/.test(v)?parseInt(v,10):-1;}
function num(v){return /^\d{1,3}(\.\d{1,4})?$/.test(String(v).trim())?parseFloat(v):-1;}
function tot(){return r2(S.q*S.p);}
function nShort(){return S.it.filter(function(x){return net(x)<0;}).length;}
function render(){
$('stg').innerHTML=STG.map(function(t,i){var c=!S.po?'':i<S.st?' dn':i===S.st?' cu':'';return (i?'<span class="ln"></span>':'')+'<span class="s'+c+'"><i>'+(c===' dn'?'&#10003;':i+1)+'</i>'+t+'</span>';}).join('')+'<span class="po mono">'+(S.po?'PO-4520':'No PO yet')+'</span>';
var rows=S.it.filter(function(x){return !S.sh||net(x)<0||(S.sel&&x[0]==='PP-100');});
var g='<div class="ct"><span>Materials for scheduled runs</span><span class="flt"><button type="button" class="fc'+(S.sh?'':' on')+'">All<b>4</b></button><button type="button" class="fc'+(S.sh?' on':'')+'" id="fsh">Shortages only'+(S.sh?'<b id="nsh">'+nShort()+'</b>':'')+'</button></span></div>'+
'<div class="row h"><span>Item</span><span>On hand</span><span>On order</span><span>Committed</span><span>Net</span><span>Coverage</span></div>';
rows.forEach(function(x){var n=net(x),c=Math.min(1,(x[3]+x[4])/x[5]),sel=S.sel&&x[0]==='PP-100';
g+='<button type="button" class="row'+(sel?' sel':'')+(S.anim?' in':'')+'" id="r-'+x[0]+'"><span><span class="mono">'+x[0]+'</span> <span class="mut">'+x[1]+'</span></span><span class="mono" id="oh-'+x[0]+'">'+n0(x[3])+'</span><span class="mono" id="oo-'+x[0]+'">'+n0(x[4])+'</span><span class="mono">'+n0(x[5])+'</span><span class="mono'+(n<0?' neg':'')+'" id="nt-'+x[0]+'">'+sg(n)+'</span><span class="cov"><i style="width:'+Math.round(c*100)+'%;background:'+(c<1?'#F87171':'#22C55E')+'"></i></span></button>';});
$('pln').innerHTML=g;
var d='<div class="ct"><span>Demand by run'+(S.sel?', <span class="mono">PP-100</span>':'')+'</span><span class="mut" style="font-weight:500">'+(S.sel?'On hand '+n0(pp()[3])+' lb':'Scheduled runs')+'</span></div>';
if(!S.sel)d+='<div class="row h" style="grid-template-columns:62px 40px 1fr 80px"><span>Run</span><span>Date</span><span>Part</span><span>Press</span></div>'+[['RUN-7720','11/10','CAP-38 black','Press 4'],['RUN-7722','11/12','CAP-38 black','Press 6'],['RUN-7725','11/14','CAP-28 white','Press 3'],['RUN-7731','11/18','CAP-38 black','Press 4']].map(function(x){return '<div class="row" style="grid-template-columns:62px 40px 1fr 80px"><span class="mono">'+x[0]+'</span><span class="mono mut">'+x[1]+'</span><span>'+x[2]+'</span><span class="mut">'+x[3]+'</span></div>';}).join('')+'<div class="nt" id="dh">Click a material in the grid to see how much each run needs and where stock runs out.</div>';
else{var cum=0,mx=9200,first='';d+='<div class="row h"><span>Run</span><span>Date</span><span>Needs</span><span>Lb</span><span>Running</span><span></span></div>';
RUNS.forEach(function(x,i){cum+=x[2];var shortRun=cum>pp()[3],covered=cum<=pp()[3]+pp()[4];if(shortRun&&!first)first=x[0];var cls=!shortRun?'cv':covered?'oo':'sh';
var tag=!shortRun?'<span class="ch c-ok">Covered</span>':covered?'<span class="ch c-info">On order</span>':(x[0]===first?'<span class="ch c-bad" id="first">First run short</span>':'<span class="ch c-bad">Short</span>');
d+='<div class="row'+(S.anim?' in':'')+'" style="animation-delay:'+(i*70)+'ms"><span class="mono">'+x[0]+'</span><span class="mono mut">'+x[1]+'</span><span><span class="db '+cls+'" style="display:block;width:'+Math.round(x[2]/mx*100)+'%"></span></span><span class="mono">'+n0(x[2])+'</span><span class="mono" id="cu-'+x[0]+'">'+n0(cum)+'</span><span>'+tag+'</span></div>';});
d+='<div class="nt">'+(pp()[4]?'PO-4520 has '+n0(pp()[4])+' lb on order, so every run is covered. Net after all four runs: '+n0(net(pp()))+' lb.':'On hand '+n0(pp()[3])+' lb covers RUN-7720 and RUN-7722. The running total passes it at RUN-7725, so four runs compete for the same resin.')+'</div>';}
$('dem').innerHTML=d;
var p='<div class="ct">Purchase order'+(S.po?'<span class="ch '+['c-idle','c-warn','c-info','c-info'][S.st]+'" id="pst">'+STG[S.st]+'</span>':'')+'</div>';
if(!S.sel)p+='<div class="pd"><div class="empt"><b>No order yet</b><span>Open a short material and buy for it from here.</span></div></div>';
else if(!S.po)p+='<div class="g frm"><label class="fld" id="fsu"><small>Supplier</small><input id="isu" value="'+S.v.su+'" autocomplete="off" spellcheck="false"></label><div class="two"><label class="fld" id="fq"><small>PP-100, lb</small><input id="iq" value="'+S.v.q+'" inputmode="numeric" autocomplete="off"></label><label class="fld" id="fp"><small>Price per lb</small><input id="ip" value="'+S.v.p+'" inputmode="decimal" autocomplete="off"></label></div><span class="fld" id="fe"><span class="em">A supplier, whole pounds and a price</span></span></div><div class="bw"><button type="button" class="bt pri" id="mk">Create PO</button></div>';
else{p+='<div class="kvs'+(S.anim?' in':'')+'"><div class="kv"><small>PO</small><b class="mono">PO-4520</b></div><div class="kv"><small>Supplier</small><b>'+S.su+'</b></div><div class="kv"><small>PP-100</small><b class="mono">'+n0(S.q)+' lb</b></div><div class="kv"><small>Gaylords</small><b class="mono">'+(S.q/GAY)+' of 1,000 lb</b></div><div class="kv"><small>Price per lb</small><b class="mono">'+S.p.toFixed(2)+'</b></div><div class="kv"><small>Total</small><b class="mono" id="pot">'+f2(tot())+'</b></div></div><div class="ac">';
if(S.st===0)p+='<button type="button" class="bt pri" id="snd">Send for approval</button><span class="nt">Orders over '+f2(LIM)+' go to the purchasing manager</span>';
else if(S.st===1)p+='<button type="button" class="bt pri" id="apv">Approve as purchasing manager</button><span class="nt">Waiting on R. Hale'+(tot()>LIM?', over '+f2(LIM):'')+'</span>';
else if(S.st===2)p+='<div class="two frm" style="display:grid;grid-template-columns:1fr 1fr;gap:6px"><label class="fld" id="fgy"><small>Gaylords arrived</small><input id="igy" value="'+S.v.gy+'" inputmode="numeric" autocomplete="off"></label><label class="fld" id="flt"><small>Resin lot</small><input id="ilt" value="'+S.v.lt+'" autocomplete="off" spellcheck="false"><span class="em">Up to '+(S.q/GAY)+', lot like L-55212</span></label></div><button type="button" class="bt pri" id="rcv">Receive '+S.v.gy+' gaylords</button>';
else p+='<span class="ch c-ok" id="rg">'+S.gy+' of '+(S.q/GAY)+' gaylords received, lot '+S.lt+'</span><span class="ch c-warn" id="oo2">'+n0(pp()[4])+' lb still on order</span>';
p+='</div>';}
$('po').innerHTML=p;
$('hst').textContent=S.po?'PO-4520 '+STG[S.st].toLowerCase():S.sh?nShort()+' short':'4 materials';$('hst').className='ch '+(S.po?'c-info':S.sh?'c-bad':'c-idle');
S.anim=false;}
$('po').addEventListener('input',function(e){var k={isu:'su',iq:'q',ip:'p',igy:'gy',ilt:'lt'}[e.target.id];if(k)S.v[k]=e.target.value;if(k==='gy'&&$('rcv'))$('rcv').textContent='Receive '+e.target.value+' gaylords';});
function resetState(){S={sh:false,sel:false,po:false,st:0,anim:false,it:IT0.map(function(x){return x.slice();}),v:{su:'Northfield Polymers',q:'14,000',p:'0.74',gy:'6',lt:'L-55212'}};render();}
function okPo(){var b=!(val('isu').length>2&&int(val('iq'))>0&&int(val('iq'))%GAY===0&&num(val('ip'))>0);['fsu','fq','fp','fe'].forEach(function(i){$(i).classList.toggle('err',b);});return !b;}
function okR(){var n=int(val('igy')),b=!(n>0&&n*GAY<=S.q&&/^L-\d{5}$/i.test(val('ilt')));['fgy','flt'].forEach(function(i){$(i).classList.toggle('err',b);});return !b;}
var CAPAT=function(hh){return{l:14,t:visH()-hh-14};};
var ST=[
{id:'sh',target:function(){return $('fsh');},prompt:'Click Shortages only',where:'below',run:function(){S.sh=true;S.anim=true;render();},
 after:function(){return['One filter shows every material that will stop a run, across all scheduled runs','PP-100 is short '+n0(-net(S.it[0]))+' lb and COL-BLK is short '+n0(-net(S.it[1]))+' lb.'];}},
{id:'sel',target:function(){return $('r-PP-100');},prompt:'Click the PP-100 row',where:'below',run:function(){S.sel=true;S.anim=true;render();},
 after:['You see which runs are competing for the same resin, not just a stock count','RUN-7720 and RUN-7722 need 10,300 lb of the 11,000 on hand. RUN-7725 is the first run short.']},
{id:'mk',target:function(){return $('mk');},prompt:'Click Create PO',where:'below',ok:okPo,
 run:function(){S.su=val('isu');S.q=int(val('iq'));S.p=num(val('ip'));S.po=true;S.st=0;S.anim=true;render();},
 after:function(){return['The shortage becomes a purchase order with supplier, quantity and price already in','Draft PO-4520: '+n0(S.q)+' lb, '+(S.q/GAY)+' gaylords at '+S.p.toFixed(2)+', total '+f2(tot())+'.'];}},
{id:'snd',target:function(){return $('snd');},prompt:'Click Send for approval',where:'below',run:function(){S.st=1;render();},
 after:function(){return['Approval rules send larger orders to the right person first',tot()>LIM?f2(tot())+' is over '+f2(LIM)+', so it waits on the purchasing manager.':'It waits on the purchasing manager.'];}},
{id:'apv',target:function(){return $('apv');},prompt:'Click Approve as purchasing manager',where:'below',run:function(){S.st=2;S.it[0][4]=S.q;render();},
 after:function(){return['Approved and on its way. The grid now counts the resin on order','PP-100 on order '+n0(pp()[4])+' lb, net '+sg(net(pp()))+' lb.'];}},
{id:'rcv',target:function(){return $('rcv');},prompt:'Click Receive 6 gaylords',where:'below',ok:okR,
 run:function(){var n=int(val('igy'));S.gy=n;S.lt=val('ilt').toUpperCase();S.st=3;S.it[0][3]+=n*GAY;S.it[0][4]-=n*GAY;render();},
 after:function(){return['A partial delivery is received gaylord by gaylord, and the rest stays on order','On hand '+n0(pp()[3])+', on order '+n0(pp()[4])+', net still '+sg(net(pp()))+'. COL-BLK is still short '+n0(-net(S.it[1]))+'.'];}}];
'''
