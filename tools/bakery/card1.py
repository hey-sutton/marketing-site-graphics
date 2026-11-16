"""Bakery card 1: BOM scaling and cost roll up (page headline: Recipe Scaling & Cost Roll-Up).
Layout: three stacked layer panels (Dough, Filling, Glaze) on the left, a version toggle, an ingredient price and the scaled
batch on the right, and a cost waterfall strip along the bottom.
Pick Cinnamon Roll, scale it to 750 rolls, roll the cost up, compare BOM v4 with v3, then change the butter price.
Every number is computed from the data arrays below, in grams and cents, so sums are exact."""
from frame_auto import header

SUMMARY = 'BOM scaling and cost roll up (pick a layered product, scale every layer to a batch, roll the cost up to a cost per roll, compare BOM versions, change an ingredient price)'
ARIA = 'Interactive product screen: load the Cinnamon Roll BOM, scale dough, filling and glaze to 750 rolls, roll the cost up to $0.776 per roll, compare BOM v4 with v3, then change the butter price'
STEPS = 5
STUDIO = dict(lede='A typical BOM scaling screen, built on your Sutton data with Studio. Want it different? Describe the change.',
              examples=['Show allergens on every layer', 'Compare any two BOM versions', 'Add oven time to labor', 'Flag a price change above 5%'],
              built_on='BOMs, ingredient costs and labor rates', change='Layers, columns and cost lines')

ICON = '<path d="M2.5 5.2L8 2.5l5.5 2.7L8 7.9z"/><path d="M2.5 8L8 10.7 13.5 8"/><path d="M2.5 10.8L8 13.5l5.5-2.7"/>'

CSS = (
 '.k1{padding:10px 40px 0 16px;display:flex;flex-direction:column;gap:10px}'
 '.kbar{height:46px;flex:none;display:flex;align-items:center;gap:10px;padding:0 10px;overflow:visible}'
 '.kf{display:flex;align-items:center;gap:7px}.kf .fld{flex-direction:row;align-items:center;gap:7px;position:relative}.kf .fld small{font-size:10px;color:#18181B;font-weight:600;white-space:nowrap}'
 '.kf .fld .em{position:absolute;left:0;top:30px;white-space:nowrap;z-index:3;background:#fff;padding:1px 4px;border-radius:4px}'
 '#kpi{width:128px;font-size:10.4px;padding:6px 8px}#kri{width:58px;font-size:10.4px;padding:6px 8px;text-align:right}#kri:disabled{background:#FAFAFA;color:#A1A1AA}'
 '.ksmp{display:inline-flex;align-items:center;gap:5px;font-size:9.4px;color:#71717A}.ksmp .bt{font-size:9.6px;padding:4px 8px}'
 '.kdv{width:1px;height:24px;background:#E4E4E7;flex:none;margin:0 2px}.kf .mut{font-size:9.6px}'
 '.kmain{display:grid;grid-template-columns:420px 230px;gap:10px;height:336px;flex:none}'
 '.klay{display:flex;flex-direction:column;gap:6px;min-width:0}.klay .empt{height:100%}'
 '.kpn .ct{height:27px}.kpn .ct .kln{display:flex;align-items:center;gap:8px}.kpn .ct .mut{font-weight:400;font-size:9.4px}.kpn .ct .ktt{display:flex;align-items:center;gap:10px;font-family:"JetBrains Mono",ui-monospace,monospace;font-size:10px}'
 '.kpn .row{grid-template-columns:1fr 60px 70px 46px 58px;min-height:20px;font-size:9.6px;gap:6px}.kpn .row.h{min-height:19px;font-size:8.8px}'
 '.kpn .row>span:not(:first-child){text-align:right}.kpn .row .mono{font-size:9.6px}.kpn .row .kn{display:flex;align-items:center;gap:6px;white-space:nowrap;min-width:0}'
 '.ksk{font-size:8.4px;padding:1px 5px;border-radius:4px;background:#E8EEFC;color:#1E3A8A;white-space:nowrap}.kpn .row.kchg{background:#FFFBEB}.kpn .row.kchg .kv{color:#92400E}.kpn .row.kpx{background:#FFF7ED}'
 '.kside{display:flex;flex-direction:column;gap:8px;min-width:0}.kside .empt{height:100%}.kside.kof>.cd{display:none}.kside:not(.kof)>.empt{display:none}.klay .kpn,.kside .cd{flex:none}'
 '.kver{height:120px}.kseg{display:flex;gap:4px;padding:9px 11px 6px}.kvb{flex:1;font-size:10px;padding:6px 0;border:1px solid #E4E4E7;border-radius:6px;background:#fff;color:#52525B;cursor:pointer;font-weight:500;transition:background-color .2s,color .2s}'
 '.kvb.on{background:#18181B;border-color:#18181B;color:#fff}.kvb.fakehover:not(.on){background:#F4F4F5}.kvb:focus-visible{outline:2px solid #18181B;outline-offset:2px}'
 '.kvl{padding:2px 11px;font-size:9.4px;color:#52525B;line-height:1.5}.kvl b{font-family:"JetBrains Mono",ui-monospace,monospace;font-weight:600;color:#18181B}.kvl .kdl{display:inline-block;margin-top:3px}'
 '.kprc{height:106px}.kpf{display:flex;align-items:center;gap:6px;padding:9px 11px 4px}.kpf .kpn2{font-size:10px;font-weight:600;flex:1}.kpf .fld{position:relative}.kpf .fld .em{position:absolute;right:0;top:27px;white-space:nowrap;background:#fff}'
 '#kpr{width:52px;text-align:right;font-size:10.2px;padding:5px 6px}.kpl{padding:3px 11px;font-size:9.2px;color:#71717A;line-height:1.45}.kpl b{color:#18181B;font-weight:600}'
 '.kbat{flex:1 1 auto;display:flex;flex-direction:column}.kbg{display:grid;grid-template-columns:1fr 1fr;gap:6px;padding:8px 11px}.kbg .kv2{display:flex;flex-direction:column;gap:1px}.kbg small{font-size:8.6px;color:#71717A}.kbg b{font-family:"JetBrains Mono",ui-monospace,monospace;font-size:11px;font-weight:600}'
 '.kwf{height:140px;flex:none}.kwf .ct .mut{font-weight:400}.kwf .empt{margin:8px 10px;height:90px}'
 '.kwb{display:grid;grid-template-columns:repeat(4,104px) 1fr;gap:10px;padding:8px 11px 0}'
 '.kwc{display:flex;flex-direction:column;gap:1px}.kwc small{font-size:8.8px;color:#71717A}.kwc b{font-family:"JetBrains Mono",ui-monospace,monospace;font-size:11.2px;font-weight:600}'
 '.kwa{position:relative;height:52px;margin-top:5px;border-bottom:1px solid #E4E4E7}.kwa i{position:absolute;left:0;right:22px;border-radius:3px 3px 0 0;background:#D4D4D8;transform-origin:bottom;animation:kgrow .6s cubic-bezier(.22,.9,.28,1) both}'
 '.kwa i.kti{background:#18181B}.kwa i.kup{background:#F59E0B}@keyframes kgrow{from{transform:scaleY(0)}}'
 '.kwr{border-left:1px solid #F0F0F1;padding-left:12px;display:flex;flex-direction:column;gap:2px}.kwr small{font-size:8.8px;color:#71717A}.kwr .big{font-family:"JetBrains Mono",ui-monospace,monospace;font-size:21px}.kwr em{font-style:normal;font-size:9px;color:#52525B}'
 '.kflash{animation:kfl 1.2s ease}@keyframes kfl{0%{background:#FFF4D6}100%{background:transparent}}'
)

WIN = (
 header(ICON, 'BOM scaling', 'Layered products, cost per unit', '<span class="ch c-idle" id="kst">No product loaded</span>')
 + '<div class="k1"><div class="cd kbar">'
 '<div class="frm kf" id="kfa"><label class="fld" id="kfp"><small>Product</small><input id="kpi" value="" placeholder="Search a product" autocomplete="off" spellcheck="false" aria-label="Product"><span class="em" id="kpe">No product found. Try Cinnamon Roll</span></label>'
 '<button type="button" class="bt pri" id="kld">Load</button><span class="ksmp">Sample<button type="button" class="bt" id="ksm" data-sample>Cinnamon Roll</button></span></div>'
 '<span class="kdv"></span>'
 '<div class="frm kf" id="kfb"><label class="fld" id="kfr"><small>Batch</small><input id="kri" value="" placeholder="Rolls" inputmode="numeric" autocomplete="off" aria-label="Batch size in rolls" disabled><span class="em" id="kre">Enter whole rolls, 1 to 5,000</span></label><span class="mut">rolls</span>'
 '<button type="button" class="bt" id="ksc">Scale</button></div></div>'
 '<div class="kmain"><div class="klay" id="klay"></div>'
 '<div class="kside kof" id="kside"><div class="empt"><b>No product loaded</b><span>BOM versions, ingredient prices and the scaled batch show here.</span></div>'
 '<div class="cd kver"><div class="ct"><span>BOM version</span><span class="ch c-ok" id="kvc">v4 current</span></div>'
 '<div class="kseg" role="group" aria-label="BOM version"><button type="button" class="kvb on" id="kv4">v4 current</button><button type="button" class="kvb" id="kv3">v3 previous</button></div><div class="kvl" id="kvl"></div></div>'
 '<div class="cd kprc"><div class="ct"><span>Ingredient price</span><span class="ch c-idle">Cedar Dairy Supply</span></div>'
 '<div class="frm kpf"><span class="kpn2">Butter</span><label class="fld" id="kfq"><input id="kpr" value="7.50" inputmode="decimal" autocomplete="off" aria-label="Butter price per kg in dollars"><span class="em" id="kqe">Enter a price, for example 8.00</span></label><span class="mut" style="font-size:9.4px">per kg</span><button type="button" class="bt" id="kupd">Update</button></div>'
 '<div class="kpl" id="kpl"></div></div>'
 '<div class="cd kbat"><div class="ct"><span>Scaled batch</span><span class="ch c-info" id="kbc"></span></div><div class="kbg" id="kbg"></div></div></div></div>'
 '<div class="cd kwf" id="kwf"></div></div>'
)

JS = r'''
var FOC='.hd>*,.kbar>*,.klay>*,.kside>*,.kwf>*';
/* BOM v4 per standard batch of 250 rolls: [ingredient, grams, cents per kg, flag] (b: butter, bd: butter in the dough, v3 has 5,000 g) */
var STD=250,PKG=5,LABH=2,LABR=2200,SACK=25000,V3BD=5000;
var L=[['Dough',[['Bread flour',25000,90,'f'],['Whole milk',14000,110],['Butter',6000,750,'bd'],['Sugar',3000,120],['Yeast',500,600]]],
['Filling',[['Brown sugar',4000,160],['Cinnamon',250,1400],['Butter',2000,750,'b']]],
['Glaze',[['Powdered sugar',5000,140],['Cream cheese',2500,600],['Milk',1000,110]]]];
var S;
function kg(g){return (g/1000).toLocaleString('en-US',{minimumFractionDigits:3,maximumFractionDigits:3});}
function mc(c){return m2(c/100);}
function pr3(c,R){return (Math.round(c/R*10)/1000).toFixed(3);}
function q250(r,v){return (v===3&&r[3]==='bd')?V3BD:r[1];}
function isB(r){return r[3]==='b'||r[3]==='bd';}
function cpk(r,bp){return isB(r)?bp:r[2];}
function qb(r,v,R){return Math.round(q250(r,v)*R/STD);}
function rowC(r,v,R,bp){return Math.round(qb(r,v,R)*cpk(r,bp)/1000);}
function layG(i,v,R){return L[i][1].reduce(function(s,r){return s+(R===STD?q250(r,v):qb(r,v,R));},0);}
function layC(i,v,R,bp){return L[i][1].reduce(function(s,r){return s+rowC(r,v,R,bp);},0);}
function cost(v,R,bp){var ing=0;L.forEach(function(x,i){ing+=layC(i,v,R,bp);});var pkg=R*PKG,lab=Math.round(R*LABH*LABR/STD);return {ing:ing,pkg:pkg,lab:lab,tot:ing+pkg+lab};}
function butG(v,R){var g=0;L.forEach(function(x){x[1].forEach(function(r){if(isB(r))g+=qb(r,v,R);});});return g;}
function fac(R){var f=R/STD;return f%1===0?String(f):f.toFixed(2);}
function hrs(R){var h=R*LABH/STD;return (h%1===0?String(h):h.toFixed(1))+' hours';}
function sacks(R){var g=qb(L[0][1][0],4,R),n=Math.ceil(g/SACK);return n+(n===1?' sack':' sacks')+' of 25 kg'+(g%SACK?', last one opened':'');}
function render(){var v=S.ver,R=S.R,bp=S.bp,lay=$('klay');
if(!S.p){lay.innerHTML='<div class="empt"><svg width="26" height="26" viewBox="0 0 16 16" fill="none" stroke="#A1A1AA" stroke-width="1.1" stroke-linecap="round" stroke-linejoin="round"><path d="M2.5 5.2L8 2.5l5.5 2.7L8 7.9z"/><path d="M2.5 8L8 10.7 13.5 8"/><path d="M2.5 10.8L8 13.5l5.5-2.7"/></svg><b>No product loaded</b><span>Pick a layered product to see its dough, filling and glaze, scaled to your batch.</span></div>';}
else{lay.innerHTML=L.map(function(x,i){var hd='<div class="ct"><span class="kln">'+x[0]+'<span class="mut">'+kg(layG(i,v,STD))+' kg per 250</span></span><span class="ktt"><span id="kt'+i+'">'+kg(layG(i,v,R))+' kg</span>'+(S.rolled?'<span id="kc'+i+'">'+mc(layC(i,v,R,bp))+'</span>':'')+'</span></div>';
var rows=(i===0?'<div class="row h"><span>Ingredient</span><span>Per 250</span><span>For '+n0(R)+'</span><span>$ per kg</span><span>Cost</span></div>':'')+x[1].map(function(r,j){var chg=v===3&&r[3]==='bd',px=S.px&&isB(r);
return '<div class="row'+(chg?' kchg':'')+(px?' kpx':'')+'" id="kr'+i+j+'"><span class="kn">'+r[0]+(r[3]==='f'?'<span class="ksk" id="ksk">'+sacks(R)+'</span>':'')+'</span><span class="mono kv">'+kg(q250(r,v))+'</span><span class="mono kv" id="kq'+i+j+'">'+kg(qb(r,v,R))+'</span><span class="mono">'+(cpk(r,bp)/100).toFixed(2)+'</span><span class="mono" id="ko'+i+j+'">'+(S.rolled?mc(rowC(r,v,R,bp)):'')+'</span></div>';}).join('');
return '<div class="cd kpn'+(S.an?' in':'')+'" style="animation-delay:'+(i*90)+'ms">'+hd+rows+'</div>';}).join('');}
$('kside').classList.toggle('kof',!S.p);
var st=$('kst');st.textContent=S.p?'Cinnamon Roll, BOM v'+v:'No product loaded';st.className='ch '+(S.p?(v===3?'c-warn':'c-info'):'c-idle');
$('kv4').classList.toggle('on',v===4);$('kv3').classList.toggle('on',v===3);var vc=$('kvc');vc.textContent=v===3?'v3 previous':'v4 current';vc.className='ch '+(v===3?'c-warn':'c-ok');
var c4=cost(4,R,bp),c3=cost(3,R,bp),d=(parseFloat(pr3(c4.tot,R))-parseFloat(pr3(c3.tot,R))).toFixed(3);
$('kvl').innerHTML='Butter in the dough, per 250: <b>'+kg(q250(L[0][1][2],v))+' kg</b><br>'+(S.cmp?'<span class="kdl" id="kdl">v3: <b>'+mc(c3.tot)+'</b> for '+n0(R)+', <b>$'+pr3(c3.tot,R)+'</b> per roll. <b id="kdd">'+(d>=0?'+$'+d:'$'+Math.abs(d).toFixed(3)+' less')+' per roll in v4</b></span>':'<span class="kdl mut">Roll up the cost, then compare versions.</span>');
$('kpl').innerHTML=S.p?'Used in dough and filling, <b id="kbu">'+kg(butG(4,R))+' kg</b> in this batch. '+(S.px?'Was $'+(S.bp0/100).toFixed(2)+' per kg.':'Received at $7.50 per kg.'):'';
$('kbc').textContent=n0(R)+' rolls';
$('kbg').innerHTML='<span class="kv2"><small>Factor on 250</small><b id="kbf">'+fac(R)+'</b></span><span class="kv2"><small>Labor</small><b id="kbl">'+hrs(R)+'</b></span><span class="kv2"><small>Dough to mix</small><b>'+kg(layG(0,v,R))+' kg</b></span><span class="kv2"><small>Flour</small><b>'+sacks(R).split(',')[0]+'</b></span>';
var w=$('kwf'),c=cost(v,R,bp);
if(!S.rolled){w.innerHTML='<div class="ct"><span>Cost roll up</span>'+(S.p?'<button type="button" class="bt pri" id="kru">Roll up cost</button>':'')+'</div><div class="empt"><b>No cost yet</b><span>Ingredients, packaging and labor roll up to a cost per roll here.</span></div>';}
else{var mx=c.tot,H=50;function bar(lo,hi,cls){return '<i class="'+cls+'" style="bottom:'+(lo/mx*H).toFixed(1)+'px;height:'+Math.max(2,(hi-lo)/mx*H).toFixed(1)+'px"></i>';}
var cols=[['Ingredients','kw-ing',c.ing,bar(0,c.ing,'')],['Packaging','kw-pkg',c.pkg,bar(c.ing,c.ing+c.pkg,'')],['Labor','kw-lab',c.lab,bar(c.ing+c.pkg,c.tot,'')],['Total','kw-tot',c.tot,bar(0,c.tot,S.px?'kup':'kti')]];
w.innerHTML='<div class="ct"><span>Cost roll up <span class="mut">BOM v'+v+', '+n0(R)+' rolls</span></span><span class="ch '+(S.px?'c-warn':'c-ok')+'" id="kwc">'+(S.px?'Butter price updated':'Rolled up')+'</span></div><div class="kwb">'+
cols.map(function(x){return '<div class="kwc"><small>'+x[0]+'</small><b id="'+x[1]+'">'+mc(x[2])+'</b><div class="kwa">'+x[3]+'</div></div>';}).join('')+
'<div class="kwr"><small>Cost per roll</small><span class="big" id="kw-per">$'+pr3(c.tot,R)+'</span><em id="kw-note">'+(S.px?'Was $'+pr3(cost(v,R,S.bp0).tot,R)+' at $'+(S.bp0/100).toFixed(2)+' butter':'Packaging $0.05 a roll, labor 2 hours per 250')+'</em></div></div>';}
S.an=false;}
function typeIn(id,t,done){var i=0;(function k(){$(id).value=t.slice(0,i);if(i<t.length){i++;later(k,55);}else done();})();}
function pval(){return String($('kpi').value).trim().toLowerCase().replace(/\s+/g,' ');}
function rval(){var v=String($('kri').value).replace(/,/g,'').trim();return /^\d+$/.test(v)?parseInt(v,10):NaN;}
function qval(){var v=String($('kpr').value).replace(/^\$/,'').trim();return /^\d{1,2}(\.\d{1,2})?$/.test(v)?Math.round(parseFloat(v)*100):NaN;}
$('ksm').addEventListener('click',function(){$('kpi').value='Cinnamon Roll';$('kfp').classList.remove('err');});
$('kv4').addEventListener('click',function(){if(mode==='done'&&S.rolled){S.ver=4;S.cmp=true;render();}});
$('kv3').addEventListener('click',function(){if(mode==='done'&&S.rolled){S.ver=3;S.cmp=true;render();}});
function resetState(){S={p:false,R:STD,rolled:false,ver:4,cmp:false,bp:750,bp0:750,px:false,an:false};$('kpi').value='';$('kri').value='';$('kri').disabled=true;$('kpr').value='7.50';
['kfp','kfr','kfq'].forEach(function(x){$(x).classList.remove('err');});render();}
var CAPAT=function(hh){return cur<=1?{l:14,t:visH()-hh-14}:{l:14,t:visH()-hh-150};};
var ST=[
{id:'load',target:function(){return mode==='try'?$('kld'):$('kpi');},prompt:'Type Cinnamon Roll or pick the sample, then Load',where:'below',
 ok:function(){var b=pval()!=='cinnamon roll';$('kpe').textContent=pval()?'No product found. Try Cinnamon Roll':'Enter a product, for example Cinnamon Roll';$('kfp').classList.toggle('err',b);return !b;},
 run:function(quick){var go=function(){$('kpi').value='Cinnamon Roll';$('kfp').classList.remove('err');S.p=true;S.R=STD;S.an=true;$('kri').disabled=false;$('kri').value=String(STD);render();};if(mode==='watch'&&!quick)typeIn('kpi','Cinnamon Roll',go);else go();},
 after:function(){return['Pick a layered product and every layer loads','Cinnamon Roll, BOM v4, standard batch 250: dough '+kg(layG(0,4,STD))+' kg, filling '+kg(layG(1,4,STD))+' kg, glaze '+kg(layG(2,4,STD))+' kg.'];}},
{id:'scale',target:function(){return mode==='try'?$('ksc'):$('kri');},prompt:'Type 750 as the batch, then Scale',where:'below',
 ok:function(){var R=rval(),b=!(R>=1&&R<=5000);$('kfr').classList.toggle('err',b);return !b;},
 run:function(quick){var go=function(){var R=mode==='watch'?750:rval();if(!(R>=1&&R<=5000))R=750;$('kri').value=n0(R);$('kfr').classList.remove('err');S.R=R;render();['kq00','kq01','kq02','kq03','kq04'].forEach(function(x){var e=$(x);if(e&&!quick)e.classList.add('kflash');});};if(mode==='watch'&&!quick)typeIn('kri','750',go);else go();},
 after:function(){var R=S.R;return['Enter a batch size and every layer scales',n0(R)+' rolls is factor '+fac(R)+': dough '+kg(layG(0,4,R))+' kg, filling '+kg(layG(1,4,R))+' kg, glaze '+kg(layG(2,4,R))+' kg, flour in '+sacks(R)+'.'];}},
{id:'roll',target:function(){return $('kru');},prompt:'Click Roll up cost',where:'above',run:function(){S.rolled=true;render();},
 after:function(){var c=cost(4,S.R,S.bp);return['The cost rolls up to a cost per roll','Ingredients '+mc(c.ing)+', packaging '+mc(c.pkg)+', labor '+mc(c.lab)+'. Total '+mc(c.tot)+', $'+pr3(c.tot,S.R)+' per roll.'];}},
{id:'v3',target:function(){return $('kv3');},prompt:'Switch to v3, the previous BOM',where:'below',run:function(){S.ver=3;S.cmp=true;render();},
 after:function(){var R=S.R,c=cost(3,R,S.bp),d=(parseFloat(pr3(cost(4,R,S.bp).tot,R))-parseFloat(pr3(c.tot,R))).toFixed(3);return['Compare with the previous BOM version','v3 had '+kg(V3BD)+' kg of butter in the dough: '+mc(c.tot)+' for '+n0(R)+', $'+pr3(c.tot,R)+' per roll. v4 is +$'+d+' per roll.'];}},
{id:'price',target:function(){return mode==='try'?$('kupd'):$('kpr');},prompt:'Type 8.00 as the butter price, then Update',where:'below',
 ok:function(){var b=!(qval()>0);$('kfq').classList.toggle('err',b);return !b;},
 run:function(quick){var go=function(){var p=mode==='watch'?800:qval();if(!(p>0))p=800;$('kpr').value=(p/100).toFixed(2);$('kfq').classList.remove('err');S.bp0=S.bp;S.bp=p;S.px=true;S.ver=4;render();};if(mode==='watch'&&!quick){$('kpr').value='';typeIn('kpr','8.00',go);}else go();},
 after:function(){var R=S.R,c=cost(4,R,S.bp),c0=cost(4,R,S.bp0),dd=c.tot-c0.tot;return['Change an ingredient price and watch the cost move','Back on v4. Butter at $'+(S.bp/100).toFixed(2)+' per kg '+(dd>=0?'adds '+mc(dd):'saves '+mc(-dd))+' on '+kg(butG(4,R))+' kg. Total '+mc(c.tot)+', $'+pr3(c.tot,R)+' per roll.'];}}];
'''
