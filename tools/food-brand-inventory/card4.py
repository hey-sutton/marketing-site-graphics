"""Food brand inventory card 4: Reorder Planning & Demand. Layout: a stage chain.
Top: five boxes with running totals (on hand, six weeks of open demand from sales orders and EDI orders, safety stock,
the draft PO, the barcode receipt). Middle: the item table with an On hand and Weekly view toggle; the flagged pouch
opens into one row per location. Bottom: lead time against the date needed, the draft PO, and the receipt with a read
only barcode field and Scan. Every number comes from the data below: projection = on hand less cumulative demand."""
import json
from frame_auto import header

SUMMARY = 'Reorder Planning & Demand (weekly view, spot the Stand Up Pouch shortage in week 3, compare the 3 week lead time, draft a 14,000 pouch PO, receive it by barcode)'
ARIA = 'Interactive product screen: switch to weekly availability for every location, open the Stand Up Pouch shortage, compare the supplier lead time with the week needed, create a draft purchase order for 14,000 pouches and receive it by barcode scan'
STEPS = 5
STUDIO = dict(lede='A typical reorder screen on your Sutton data. Want it different? Describe the change.',
              examples=['Demand by retailer and channel', 'A min and max per location', 'A PO split across two suppliers', 'A weekly email of shortages'],
              built_on='Items, sales orders, EDI orders and POs', change='Weeks, rules and views')

ICON = '<path d="M2 12.5h12M3.5 10l3-3.2 2.4 2 3.6-4.6"/><path d="M10.2 4.2h2.3v2.3"/>'

CSS = (
 '.fld input[readonly]{background:#F4F4F5;color:#3F3F46;cursor:default;pointer-events:none}'
 '.g4{display:grid;grid-template-columns:1fr;grid-template-rows:104px 226px 190px;gap:10px;padding:10px 44px 0 16px;width:716px}'
 '.chain{display:grid;grid-template-columns:120px 14px 120px 14px 120px 14px 120px 14px 120px;align-items:stretch}'
 '.stg{border:1px solid #E4E4E7;border-radius:8px;background:#fff;padding:8px 9px;display:flex;flex-direction:column;gap:2px;transition:background-color .35s,border-color .35s}'
 '.stg small{font-size:8.7px;color:#71717A}.stg b{font-family:"JetBrains Mono",ui-monospace,monospace;font-size:15px;font-weight:600;letter-spacing:-.02em}.stg .sub{font-size:8.4px;color:#71717A;line-height:1.35}'
 '.stg .run{margin-top:auto;padding-top:4px;border-top:1px dashed #E4E4E7;font-size:8.6px;color:#52525B;display:flex;justify-content:space-between}.stg .run em{font-style:normal;font-family:"JetBrains Mono",ui-monospace,monospace;font-weight:600;color:#18181B}'
 '.stg .sk{display:block;width:62px;height:13px;margin:3px 0 2px;border-radius:3px;background:#F4F4F5}.stg.e b{color:#D4D4D8}.stg.ok{background:#F0FDF4;border-color:#BBF7D0}.stg.bad .run em{color:#B91C1C}'
 '.arw{display:grid;place-items:center;color:#A1A1AA}.arw svg{width:10px;height:10px}'
 '.tb{display:flex;flex-direction:column}.seg{display:inline-flex;padding:2px;gap:2px;border:1px solid #E4E4E7;border-radius:7px;background:#FAFAFA}.seg button{font:inherit;font-size:9.2px;font-weight:500;padding:2px 8px;border:0;border-radius:5px;background:transparent;color:#52525B;cursor:pointer}.seg button.on{background:#18181B;color:#fff}.seg button:focus-visible{outline:2px solid #18181B;outline-offset:1px}'
 '.tb .ct .lc{font-size:9px;font-weight:400;color:#71717A;margin-left:8px}'
 '.it .row{grid-template-columns:150px 62px repeat(6,1fr) 58px;font-size:9.2px;min-height:27px;gap:4px}.it .row>span:nth-child(n+2){text-align:right;font-family:"JetBrains Mono",ui-monospace,monospace}.it .row.h>span{font-family:inherit!important}'
 '.it.oh .row{grid-template-columns:150px 70px 70px 1fr 70px}.it.oh .row>span:nth-child(4){text-align:left;font-family:inherit}'
 '.it .nm{display:flex;align-items:center;gap:5px}.it .nm b{font-weight:600}.it .row.sub{min-height:21px;background:#FCFCFC;color:#52525B;font-size:8.8px}.it .row.sub .nm{padding-left:12px}'
 '.it .lo{color:#B45309;font-weight:600}.it .ng{color:#B91C1C;font-weight:600}.it .up{color:#166534;font-weight:600}'
 '.bot{display:grid;grid-template-columns:1fr 1fr 1fr;gap:10px}.bc{display:flex;flex-direction:column}.bc>.empt{margin:9px;flex:1;padding:10px}.bc .ct .bt{font-size:9.2px;padding:3px 8px}'
 '.bc .kg{display:grid;grid-template-columns:1fr 1fr;gap:6px 8px;padding:8px 10px}.bc .kg .kv b{font-size:10.4px}.bc .wide{grid-column:span 2}'
 '.tl{margin:2px 10px 0;position:relative;height:34px}.tl .ax{position:absolute;left:0;right:0;top:14px;height:2px;background:#E4E4E7}.tl .sp{position:absolute;top:10px;height:10px;border-radius:5px;background:#18181B}.tl .nd{position:absolute;top:4px;width:2px;height:22px;background:#B45309}'
 '.tl .lb{position:absolute;top:24px;font-size:8px;color:#71717A;transform:translateX(-50%)}'
 '.mth{margin:0 10px;padding:6px 8px;border-radius:6px;background:#FAFAFA;border:1px solid #F0F0F1;font-family:"JetBrains Mono",ui-monospace,monospace;font-size:8.5px;white-space:nowrap;letter-spacing:-.02em}'
 '.scn{display:flex;align-items:flex-end;gap:6px;padding:8px 10px 2px}.scn .fld{flex:1}.scn .bt{font-size:9.4px;padding:4px 10px}.ctx{padding:2px 10px 0;font-size:8.6px;color:#71717A}'
 '.rcd{margin:8px 10px 0;padding:7px 9px;border-radius:7px;background:#F0FDF4;border:1px solid #BBF7D0;font-size:9.2px;color:#166534;line-height:1.45}.rcd b{font-family:"JetBrains Mono",ui-monospace,monospace}'
 '.bc .ft{margin-top:auto;padding:7px 10px;border-top:1px solid #F0F0F1;font-size:8.6px;color:#71717A;background:#FAFAFA}'
)

ARW = '<div class="arw" aria-hidden="true"><svg viewBox="0 0 10 10" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"><path d="M2 5h6M5.5 2.5L8 5 5.5 7.5"/></svg></div>'

WIN = (
 header(ICON, 'Reorder planning', 'Sales orders, EDI orders and lead times against stock at every location')
 + '<div class="g4"><div class="chain" id="chn"></div><div class="cd tb" id="tb"></div><div class="bot"><div class="cd bc" id="b1"></div><div class="cd bc" id="b2"></div>'
 '<div class="cd bc" id="b3"><div class="ct"><span>Receive</span><span id="rst"></span></div><div class="scn"><label class="fld"><small>PO barcode</small>'
 '<input id="ibc" value="PO-7760" readonly tabindex="-1" autocomplete="off" spellcheck="false"></label><button type="button" class="bt pri" id="scn">Scan</button></div>'
 '<div class="ctx">From the Brightfold pallet label</div><div id="rbx"></div><div class="ft">Scans post the receipt to the PO and the lot.</div></div></div></div>'
)

JS = r'''
var FOC='.hd>*,.stg,.tb>.ct,.it .row,.bc>.ct,.bc>*:not(.ct)';
var WK=6,LEAD=3,PO='PO-7760',SUP='Brightfold Packaging';
var POUCH={id:'pouch',nm:'Stand Up Pouch',u:'ea',ss:2000,sup:SUP,loc:[['Fernhill warehouse',4000,1000],['Ridgeway Co-Pack',8000,3000],['Harbor 3PL East',0,0]],so:2500,edi:1500};
var IT=[POUCH,{id:'case',nm:'Shipper Case',ss:300,sup:'Brightfold Packaging',loc:[['All',2400,170]]},{id:'pea',nm:'Peanuts, lb',ss:6000,sup:'Delta Nut Supply',loc:[['All',30000,3000]]},{id:'rai',nm:'Raisins, lb',ss:4000,sup:'Valley Vine Fruit',loc:[['All',18000,2250]]}];
var S;
function oh(it){return it.loc.reduce(function(a,l){return a+l[1];},0);}
function dw(it){return it.loc.reduce(function(a,l){return a+l[2];},0);}
function rq(it){return it===POUCH&&S.rcv?POQ():0;}
function proj(o,d,w,add){return o-d*w+(w>=LEAD?add:0);}
function weeks(it){var o=oh(it),d=dw(it),a=rq(it),r=[];for(var w=1;w<=WK;w++)r.push(proj(o,d,w,a));return r;}
function firstShort(it){for(var w=1;w<=WK;w++)if(proj(oh(it),dw(it),w,0)<it.ss)return w;return 0;}
function dem(){return dw(POUCH)*WK;}
function POQ(){return dem()+POUCH.ss-oh(POUCH);}
function sg(n){return n<0?'−'+n0(-n):n0(n);}
function cls(it,v){return v<0?'ng':v<it.ss?'lo':'';}
function stg(lbl,val,sub,run,c){return '<div class="stg'+(c?' '+c:'')+'"><small>'+lbl+'</small>'+(val===null?'<i class="sk"></i>':'<b>'+val+'</b>')+'<span class="sub">'+sub+'</span>'+(run===null?'':'<span class="run"><span>Running</span><em>'+run+'</em></span>')+'</div>';}
function render(){
var on=!!S.item,o=oh(POUCH),D=dem(),ss=POUCH.ss,Q=POQ();
var c=[on?stg('On hand, all locations','<span id="k-oh">'+n0(o)+'</span>','Warehouse '+n0(POUCH.loc[0][1])+', co-packer '+n0(POUCH.loc[1][1]),'<span id="r1">'+sg(o)+'</span>'):stg('On hand',null,'Open an item to fill the chain',null,'e'),
on?stg('Open demand, '+WK+' weeks','<span id="k-dm">'+sg(-D)+'</span>','Sales orders '+n0(POUCH.so*WK)+', EDI '+n0(POUCH.edi*WK),'<span id="r2">'+sg(o-D)+'</span>','bad'):stg('Open demand',null,'Sales orders and EDI orders',null,'e'),
on?stg('Safety stock','<span id="k-ss">'+sg(-ss)+'</span>','Kept on hand at all times','<span id="r3">'+sg(o-D-ss)+'</span>','bad'):stg('Safety stock',null,'Per item',null,'e'),
S.po?stg('Draft '+PO,'<span id="k-po">+'+n0(Q)+'</span>','Covers the gap','<span id="r4">'+sg(o-D-ss+Q)+'</span>','ok'):stg('Purchase order',null,'Drafted from the shortage',null,'e'),
S.rcv?stg('Received by scan','<span id="k-rc">'+n0(Q)+'</span>','Week '+LEAD+' balance '+n0(proj(o,dw(POUCH),LEAD,0))+' to '+n0(proj(o,dw(POUCH),LEAD,Q)),null,'ok'):stg('Received',null,'Scanned at the dock',null,'e')];
$('chn').innerHTML=c.join(ARW);
var t='<div class="ct"><span>Packaging and ingredients'+(S.wk?'<span class="lc">All locations: warehouse, co-packer, 3PL East</span>':'')+'</span><span class="seg" role="group" aria-label="View"><button type="button" id="ohv" class="'+(S.wk?'':'on')+'" aria-pressed="'+(S.wk?'false':'true')+'">On hand</button><button type="button" id="wkv" class="'+(S.wk?'on':'')+'" aria-pressed="'+(S.wk?'true':'false')+'">Weekly view</button></span></div>';
if(!S.wk){t+='<div class="it oh"><div class="row h"><span>Item</span><span>On hand</span><span>Safety</span><span>Supplier</span><span>Per week</span></div>'+IT.map(function(it){return '<div class="row"><span class="nm"><b>'+it.nm+'</b></span><span>'+n0(oh(it))+'</span><span>'+n0(it.ss)+'</span><span>'+it.sup+'</span><span>'+n0(dw(it))+'</span></div>';}).join('')+'</div>';}
else{t+='<div class="it"><div class="row h"><span>Item</span><span>On hand</span>';for(var w=1;w<=WK;w++)t+='<span>Wk '+w+'</span>';t+='<span>Safety</span></div>';
IT.forEach(function(it){var p=weeks(it),fs=firstShort(it);
t+='<button type="button" class="row'+(S.item&&it===POUCH?' sel':'')+'" id="i-'+it.id+'"><span class="nm"><b>'+it.nm+'</b>'+(fs?'<span class="ch c-warn" id="flg">Short wk '+fs+'</span>':'')+'</span><span>'+n0(oh(it))+'</span>'+p.map(function(v,i){return '<span class="'+(rq(it)&&i+1>=LEAD?'up':cls(it,v))+'" id="w-'+it.id+'-'+(i+1)+'">'+sg(v)+'</span>';}).join('')+'<span>'+n0(it.ss)+'</span></button>';
if(S.item&&it===POUCH)it.loc.forEach(function(l,k){var a=k===1&&S.rcv?POQ():0;t+='<div class="row sub in"><span class="nm">'+l[0]+'</span><span>'+n0(l[1])+'</span>';for(var w=1;w<=WK;w++)t+='<span id="l'+k+'-'+w+'">'+sg(proj(l[1],l[2],w,a))+'</span>';t+='<span></span></div>';});});
t+='</div>';}
$('tb').innerHTML=t;
var b1='<div class="ct"><span>Lead time</span>'+(S.item&&!S.lt?'<button type="button" class="bt" id="ltc">Lead time</button>':S.lt?'<span class="ch c-ok">Order this week</span>':'')+'</div>';
if(!S.lt)b1+='<div class="empt"><span>'+(S.item?'Compare the supplier lead time with the week the pouch is needed.':'Lead times show for the item you open.')+'</span></div>';
else{var need=firstShort(POUCH);b1+='<div class="kg in"><div class="kv"><small>Supplier</small><b>'+SUP+'</b></div><div class="kv"><small>Lead time</small><b id="ltw">'+LEAD+' weeks</b></div><div class="kv"><small>Needed by</small><b id="ndw">Week '+need+'</b></div><div class="kv"><small>Order by</small><b id="obw">'+(need-LEAD<=0?'This week':'Week '+(need-LEAD))+'</b></div></div>'+
'<div class="tl in"><div class="ax"></div><div class="sp" style="left:0;width:'+(LEAD/WK*100)+'%"></div><div class="nd" style="left:'+(need/WK*100)+'%"></div>'+[0,1,2,3,4,5,6].map(function(w){return '<span class="lb" style="left:'+(w/WK*100)+'%">'+(w?w:'Now')+'</span>';}).join('')+'</div>';}
b1+='<div class="ft">Lead times kept per supplier and item.</div>';$('b1').innerHTML=b1;
var b2='<div class="ct"><span>Purchase order</span>'+(S.lt&&!S.po?'<button type="button" class="bt pri" id="cpo">Create PO</button>':S.po?'<span class="ch c-info">Draft</span>':'')+'</div>';
if(!S.po)b2+='<div class="empt"><span>A shortage turns into a draft PO in one step.</span></div>';
else b2+='<div class="kg in"><div class="kv"><small>PO</small><b class="mono">'+PO+'</b></div><div class="kv"><small>Quantity</small><b class="mono" id="poq">'+n0(Q)+'</b></div><div class="kv wide"><small>'+SUP+', arrives week '+LEAD+'</small><b>'+POUCH.nm+'</b></div></div>'+
'<div class="mth in" id="pom">'+n0(D)+' + '+n0(ss)+' − '+n0(o)+' = '+n0(Q)+'</div>';
b2+='<div class="ft">'+WK+' weeks of demand plus safety stock, less on hand.</div>';$('b2').innerHTML=b2;
$('rst').innerHTML=S.rcv?'<span class="ch c-ok">Received</span>':'';
$('rbx').innerHTML=S.rcv?'<div class="rcd in" id="rcd">'+PO+' received: <b>'+n0(Q)+'</b> pouches. Week '+LEAD+' balance <b id="bb">'+n0(proj(o,dw(POUCH),LEAD,0))+'</b> to <b id="ba">'+n0(proj(o,dw(POUCH),LEAD,Q))+'</b>.</div>':'';
}
function resetState(){S={wk:false,item:false,lt:false,po:false,rcv:false};render();}
function capN(){var i=cap.querySelector('.m i');return i?+i.textContent:1;}
var CAPAT=function(hh){var w=cap.offsetWidth,n=capN();return n<=2?{l:visW()-w-14,t:visH()-hh-14}:n===3?{l:visW()-w-14,t:60}:{l:14,t:60};};
var ST=[
{id:'wk',target:function(){return $('wkv');},prompt:'Switch to the weekly view',where:'below',run:function(){S.wk=true;render();},
 after:function(){return['Weekly availability for every location',POUCH.nm+': '+weeks(POUCH).slice(0,3).map(n0).join(', ')+', then below zero from week 4.'];}},
{id:'item',target:function(){return $('i-pouch');},prompt:'Open the flagged pouch',where:'below',run:function(){S.item=true;render();},
 after:function(){return['A projected shortage on a packaging item',n0(oh(POUCH))+' on hand less '+n0(dw(POUCH))+' a week falls under the '+n0(POUCH.ss)+' safety stock in week '+firstShort(POUCH)+'.'];}},
{id:'lt',target:function(){return $('ltc');},prompt:'Click Lead time',where:'above',run:function(){S.lt=true;render();},
 after:function(){return['Lead time against the date needed',SUP+' takes '+LEAD+' weeks. Needed in week '+firstShort(POUCH)+', so the order goes out this week.'];}},
{id:'po',target:function(){return $('cpo');},prompt:'Create the PO',where:'above',run:function(){S.po=true;render();},
 after:function(){return['The shortage becomes a draft PO',n0(dem())+' + '+n0(POUCH.ss)+' − '+n0(oh(POUCH))+' = '+n0(POQ())+' pouches on '+PO+'.'];}},
{id:'rcv',target:function(){return $('scn');},prompt:'Scan the PO barcode',where:'above',run:function(){S.rcv=true;render();},
 after:function(){return['Received by barcode','Scan confirms '+n0(POQ())+' pouches. Week '+LEAD+' goes from '+n0(proj(oh(POUCH),dw(POUCH),LEAD,0))+' to '+n0(proj(oh(POUCH),dw(POUCH),LEAD,POQ()))+', week '+WK+' ends at '+n0(weeks(POUCH)[WK-1])+'.'];}}];
'''
JS = 'var ARW=' + json.dumps(ARW) + ';' + JS
