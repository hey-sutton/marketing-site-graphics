"""Food co-packing card 4: Run Billing & Client Portal.
Layout: record form with a side summary panel. The completed run record and its billing lines on the left, a fee and
materials panel under them, and an invoice summary on the right that turns into the client's portal view.
A completed run produces its own billing lines; add a conversion fee by unit, hour or batch, post it to the client invoice,
see the client's portal, and reconcile material used against material received. Every number is computed (cents, grams)."""
from frame_auto import header

SUMMARY = 'Run Billing & Client Portal (open a completed run and its billing lines, add a conversion fee by unit, hour or batch, post to the client invoice, see the client portal, reconcile material used against received)'
ARIA = 'Interactive product screen: completed run R-5108 for Brightfield Snacks; add a conversion fee of $0.85 a case for $2,040.00, post invoice INV-3051 for $4,032.00, open the client portal and reconcile rice flour and sunflower oil'
STEPS = 5
STUDIO = dict(lede='A typical run billing screen, built on your Sutton data with Studio. Want it different? Describe the change.',
              examples=['Bill storage by pallet week', 'Add a minimum run charge', 'Show yield in the portal', 'Send the invoice to accounting'],
              built_on='Runs, BOMs, client stock and invoices', change='Fee rules, lines and portal fields')

ICON = '<path d="M3.5 2h7l2 2v10h-9z"/><path d="M5.5 6h5M5.5 8.5h5M5.5 11h3"/>'

CSS = (
 '.c4{padding:10px 40px 0 16px;display:flex;flex-direction:column;gap:10px}'
 '.c4s{height:44px;flex:none;display:flex;align-items:center;gap:8px;padding:0 10px}.c4s .fld{flex-direction:row;align-items:center;gap:8px;position:relative}.c4s .fld small{font-size:10px;color:#18181B;font-weight:600;white-space:nowrap}'
 '#bin{width:140px;font-size:10.4px;padding:6px 8px}.c4s .fld .em{position:absolute;left:0;top:30px;white-space:nowrap;background:#fff;padding:1px 4px;z-index:3}'
 '.bsm{display:inline-flex;align-items:center;gap:5px;font-size:9.4px;color:#71717A}.bsm .bt{font-family:"JetBrains Mono",ui-monospace,monospace;font-size:9.6px;padding:4px 8px}'
 '.c4m{display:grid;grid-template-columns:414px 236px;gap:10px;height:482px;flex:none}.c4l{display:flex;flex-direction:column;gap:8px;min-width:0}'
 '.bh{height:112px;flex:none}.bhg{display:grid;grid-template-columns:repeat(4,1fr);gap:6px 10px;padding:8px 11px}.bhg .kv small{font-size:8.6px}.bhg .kv b{font-size:9.8px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}'
 '.bl{height:204px;flex:none}.bl .row{grid-template-columns:1fr 62px 62px 66px;min-height:26px;padding:0 11px;font-size:9.3px;gap:6px}.bl .row>span:not(:first-child){text-align:right}.bl .row.h{min-height:22px}'
 '.bl .row .ln small{display:block;font-size:8.4px;color:#71717A}.bl .row.new{background:#F0FDF4}.bl .row.tot{font-weight:600;background:#FAFAFA}.bl .row .mono{font-size:9.2px}'
 '.bf{flex:1 1 auto;display:flex;flex-direction:column}.bf .tabs{padding:0 11px}.bft{margin-top:auto;padding:5px 11px;border-top:1px solid #F0F0F1;font-size:8.6px;color:#71717A}'
 '.bh .empt,.bl .empt,.bf .empt,.bs .empt{margin:8px 10px;height:calc(100% - 46px);padding:8px}.bf .empt{height:70px;flex:none}'
 '.fe{display:flex;align-items:center;gap:6px;padding:9px 11px 0;font-size:9.4px}.fsg{display:inline-flex;gap:3px}.fb{font:inherit;font-size:9.2px;padding:4px 8px;border:1px solid #E4E4E7;border-radius:6px;background:#fff;color:#52525B;cursor:pointer}'
 '.fb.on{background:#18181B;border-color:#18181B;color:#fff}.fb.fakehover:not(.on){background:#F4F4F5}.fb:focus-visible{outline:2px solid #18181B;outline-offset:2px}'
 '.fe .fld{position:relative}#brt{width:56px;text-align:right;font-size:10px;padding:4px 6px}.fe .fld .em{position:absolute;left:0;top:26px;white-space:nowrap;background:#fff}'
 '.fcr{padding:6px 11px 0;font-size:8.8px;color:#71717A}.fcr b{font-family:"JetBrains Mono",ui-monospace,monospace;color:#18181B;font-weight:500}'
 '.rc .row{grid-template-columns:1fr 62px 52px 62px 62px 56px;min-height:24px;padding:0 11px;font-size:9px;gap:5px}.rc .row>span:not(:first-child){text-align:right}.rc .row.h{min-height:20px;font-size:8.4px}.rc .row.var{background:#FFFBEB}'
 '.bs{display:flex;flex-direction:column}.sl{display:flex;justify-content:space-between;padding:5px 11px;font-size:9.4px}.sl .mono{font-weight:600}.sl.sub{color:#71717A;font-size:8.8px;padding-top:0}'
 '.stot{margin:6px 11px 0;padding:9px 10px;border-radius:7px;background:#FAFAFA;border:1px solid #F0F0F1}.stot small{display:block;font-size:8.8px;color:#71717A}.stot .big{font-family:"JetBrains Mono",ui-monospace,monospace;font-size:20px}'
 '.sact{display:flex;flex-direction:column;gap:6px;padding:9px 11px 0}.sact .bt{text-align:center}.snote{padding:6px 11px 0;font-size:8.8px;color:#52525B;line-height:1.4}'
 '.pt2{padding:6px 11px 2px;font-size:8.8px;font-weight:600;color:#71717A;text-transform:none}.pr{display:flex;justify-content:space-between;align-items:center;gap:6px;padding:4px 11px;font-size:9.2px}.pr .mono{font-weight:600;font-size:9.2px}'
 '.pbar{margin:0 11px 6px;padding:5px 8px;border-radius:6px;background:#E8EEFC;color:#1E3A8A;font-size:8.8px}'
)

WIN = (
 header(ICON, 'Run billing', 'Completed runs, client invoices and portal', '<span class="ch c-idle" id="bst">No run open</span>')
 + '<div class="c4"><div class="cd c4s frm" id="bsf"><label class="fld" id="bfl"><small>Run</small><input id="bin" value="" placeholder="Completed run number" autocomplete="off" spellcheck="false" aria-label="Completed run number"><span class="em" id="bem">No completed run found. Try R-5108</span></label>'
 '<button type="button" class="bt pri" id="bsb">Open</button><span class="bsm">Sample<button type="button" class="bt" id="bsm" data-sample>R-5108</button></span></div>'
 '<div class="c4m"><div class="c4l"><div class="cd bh" id="bh"></div><div class="cd bl" id="bl"></div>'
 '<div class="cd bf" id="bf"><div class="tabs"><button type="button" class="tab on" id="tbf">Conversion fee</button><button type="button" class="tab" id="tbm">Materials</button></div>'
 '<div id="bfx"><div class="empt"><b>No run open</b><span>Set the conversion fee and reconcile client materials here.</span></div></div>'
 '<div class="fe frm" id="bfe" style="display:none"><span>Basis</span><span class="fsg" role="group" aria-label="Fee basis"><button type="button" class="fb on" id="fbu">Per unit</button><button type="button" class="fb" id="fbh">Per hour</button><button type="button" class="fb" id="fbb">Per batch</button></span>'
 '<label class="fld" id="bfr"><input id="brt" value="" placeholder="Rate" inputmode="decimal" autocomplete="off" aria-label="Fee rate in dollars"><span class="em">Enter a rate, for example 0.85</span></label><button type="button" class="bt pri" id="bad">Add fee</button></div>'
 '<div class="fcr" id="bcr" style="display:none"></div><div id="brc"></div>'
 '<div class="bft">Fee bases come from the client contract: per unit, per hour or per batch.</div></div></div>'
 '<div class="cd bs" id="bs"></div></div></div>'
)

JS = r'''
var FOC='.hd>*,.c4s>*,.bh,.bl,.bf,.bs';
var RUN={id:'R-5108',cl:'Brightfield Snacks',p:'Puffed rice bites',d:'Nov 18',cs:2400,hrs:65,bt:3,line:'Line 2'};
/* contract rates in cents; hours are in tenths */
var RATE={u:85,h:31000,b:68000},BAS={u:['Per unit','cases',function(){return RUN.cs;}],h:['Per hour','hours',function(){return RUN.hrs/10;}],b:['Per batch','batches',function(){return RUN.bt;}]};
var PACK=[['Film bags','Plant supplied',28800,4],['Shipper cases','Plant supplied',2400,35]];
var MAT=[['Rice flour','RF-2201',420000,1200000,780000],['Sunflower oil','SO-1440',62500,300000,235000]];
var INV='INV-3051';
var S;
function kg(g){return (g/1000).toLocaleString('en-US',{minimumFractionDigits:3,maximumFractionDigits:3});}
function mc(c){return m2(c/100);}
function fee(bs,r){return Math.round(BAS[bs][2]()*r);}
function packT(){return PACK.reduce(function(s,p){return s+p[2]*p[3];},0);}
function convT(){return S.fee?fee(S.bs,S.rate):0;}
function total(){return packT()+convT();}
function qtyS(bs){var q=BAS[bs][2]();return (q%1?q.toFixed(1):n0(q));}
function rateS(c){return c<100?'$'+(c/100).toFixed(2):m2(c/100);}
function exp(m){return m[3]-m[2];}
function vr(m){return exp(m)-m[4];}
function pct(m){return (vr(m)/exp(m)*100).toFixed(2)+'%';}
function render(){
var H=$('bh');
if(!S.open)H.innerHTML='<div class="ct"><span>Run record</span></div><div class="empt"><b>No run open</b><span>Open a completed run to see its billing lines.</span></div>';
else H.innerHTML='<div class="ct"><span>Run record</span><span class="ch c-ok">Completed</span></div><div class="bhg">'+[['Run',RUN.id],['Client',RUN.cl],['Product',RUN.p],['Completed',RUN.d],['Output',n0(RUN.cs)+' cases'],['Line time',(RUN.hrs/10).toFixed(1)+' hours'],['Batches',String(RUN.bt)],['Line',RUN.line]].map(function(x){return '<span class="kv"><small>'+x[0]+'</small><b>'+x[1]+'</b></span>';}).join('')+'</div>';
var L=$('bl');
if(!S.open)L.innerHTML='<div class="ct"><span>Billing lines</span></div><div class="empt"><b>No billing lines</b><span>Conversion fee, client materials and plant packaging.</span></div>';
else{var rows='<div class="row h"><span>Line</span><span>Qty</span><span>Rate</span><span>Amount</span></div>'
+(S.fee?'<div class="row new"><span class="ln">Conversion fee<small>'+BAS[S.bs][0]+'</small></span><span class="mono">'+qtyS(S.bs)+'</span><span class="mono">'+rateS(S.rate)+'</span><span class="mono" id="blf">'+mc(convT())+'</span></div>':'<div class="row"><span class="ln">Conversion fee<small>Not set yet</small></span><span></span><span></span><span class="mono mut">Not set</span></div>')
+PACK.map(function(p,i){return '<div class="row"><span class="ln">'+p[0]+'<small>'+p[1]+'</small></span><span class="mono">'+n0(p[2])+'</span><span class="mono">'+rateS(p[3])+'</span><span class="mono" id="blp'+i+'">'+mc(p[2]*p[3])+'</span></div>';}).join('')
+MAT.map(function(m){return '<div class="row"><span class="ln">'+m[0]+'<small>Client supplied, not billed</small></span><span class="mono">'+kg(m[2])+'</span><span class="mono">kg</span><span class="mono">$0.00</span></div>';}).join('')
+'<div class="row tot"><span>Total</span><span></span><span></span><span class="mono" id="blt">'+mc(total())+'</span></div>';
L.innerHTML='<div class="ct"><span>Billing lines</span><span class="ch '+(S.post?'c-ok':'c-idle')+'">'+(S.post?'Posted':'Draft')+'</span></div>'+rows;}
var fx=$('bfx'),fe=$('bfe'),cr=$('bcr'),rc=$('brc');
$('tbf').classList.toggle('on',!S.rec);$('tbm').classList.toggle('on',!!S.rec);
fx.style.display=S.open?'none':'';fe.style.display=(!S.open||S.rec||S.fee)?'none':'';cr.style.display=(!S.open||S.rec)?'none':'';
['u','h','b'].forEach(function(k){$('fb'+k).classList.toggle('on',S.bs===k);});
cr.innerHTML=S.fee?'Conversion fee added, '+BAS[S.bs][0].toLowerCase()+': <b>'+mc(convT())+'</b>. At contract rates per hour <b>'+mc(fee('h',RATE.h))+'</b>, per batch <b>'+mc(fee('b',RATE.b))+'</b>.':'Contract rates: <b>$0.85</b> a case, <b>$310.00</b> an hour, <b>$680.00</b> a batch.';
rc.innerHTML=S.rec?'<div class="rc"><div class="row h"><span>Client material</span><span>Received</span><span>Used</span><span>Expected</span><span>Counted</span><span>Variance</span></div>'+MAT.map(function(m,i){return '<div class="row'+(vr(m)?' var':'')+'"><span>'+m[0]+' <span class="mut mono">'+m[1]+'</span></span><span class="mono">'+kg(m[3])+'</span><span class="mono">'+kg(m[2])+'</span><span class="mono" id="rx'+i+'">'+kg(exp(m))+'</span><span class="mono">'+kg(m[4])+'</span><span class="mono" id="rv'+i+'">'+kg(vr(m))+'</span></div>';}).join('')
+'<div class="fcr" id="rcs">Sunflower oil is '+kg(vr(MAT[1]))+' kg short of expected, '+pct(MAT[1])+'. Rice flour matches, '+pct(MAT[0])+'.</div></div>':'';
var Sx=$('bs');
if(!S.open)Sx.innerHTML='<div class="ct"><span>Invoice summary</span></div><div class="empt"><b>Nothing to bill yet</b><span>The invoice total and the client portal view show here.</span></div>';
else if(!S.portal)Sx.innerHTML='<div class="ct"><span>Invoice summary</span><span class="ch '+(S.post?'c-ok':'c-idle')+'" id="bis">'+(S.post?INV+' posted':'Draft')+'</span></div>'
+'<div class="sl" style="padding-top:8px"><span>Conversion fee</span><span class="mono" id="sc">'+mc(convT())+'</span></div><div class="sl"><span>Plant packaging</span><span class="mono" id="sp">'+mc(packT())+'</span></div><div class="sl sub"><span>Film bags and shipper cases</span><span></span></div>'
+'<div class="sl"><span>Client materials</span><span class="mono">$0.00</span></div><div class="sl sub"><span>Supplied by '+RUN.cl+'</span><span></span></div>'
+'<div class="stot"><small>Invoice total</small><span class="big" id="stt">'+mc(total())+'</span></div>'
+'<div class="sact">'+(S.post?'<button type="button" class="bt pri" id="bpv">Client portal view</button>':'<button type="button" class="bt'+(S.fee?' pri':'')+'" id="bpo"'+(S.fee?'':' disabled')+'>Post to invoice</button>')+'</div>'
+'<div class="snote">'+(S.post?INV+' for '+RUN.cl+', due Dec 18.':(S.fee?'Ready to post to the client invoice.':'Add the conversion fee before posting.'))+'</div>'
+'<div class="pt2" style="margin-top:8px">Invoice terms</div>'+[['Terms','Net 30'],['Lines billed',(S.fee?3:2)+' of 5'],['Recorded at $0.00','2 client materials'],['Bill to','Accounts, '+RUN.cl]].map(function(x){return '<div class="pr"><span class="mut">'+x[0]+'</span><span>'+x[1]+'</span></div>';}).join('');
else Sx.innerHTML='<div class="ct"><span>Client portal</span><span class="ch c-info">Preview</span></div><div class="pbar">Signed in as '+RUN.cl+'. Other clients are not visible.</div>'
+'<div class="pt2">Runs</div><div class="pr"><span class="mono">'+RUN.id+'</span><span class="ch c-ok" id="pr1">Completed, invoiced</span></div><div class="pr"><span class="mono">R-5114</span><span class="ch c-info">Scheduled Nov 19</span></div>'
+'<div class="pt2">Invoices</div><div class="pr"><span class="mono">'+INV+'</span><span class="mono" id="pin">'+mc(total())+'</span></div>'
+'<div class="pt2">Stock held at the plant</div>'+MAT.map(function(m,i){return '<div class="pr"><span>'+m[0]+'</span><span class="mono" id="ps'+i+'">'+kg(m[4])+' kg</span></div>';}).join('')+'<div class="pr"><span>Puffed rice bites</span><span class="mono">120 cases</span></div>'
+'<div class="pt2">Run history</div><div class="pr"><span class="mono">R-5099</span><span class="mut">Nov 11, completed</span></div><div class="pr"><span class="mono">R-5091</span><span class="mut">Nov 4, completed</span></div>';
var st=$('bst');st.textContent=S.rec?'Materials reconciled':S.portal?'Portal preview':S.post?INV+' posted':S.open?RUN.id+' completed':'No run open';st.className='ch '+(S.post?'c-ok':S.open?'c-info':'c-idle');}
function val(){return String($('bin').value).trim().toUpperCase().replace(/\s/g,'');}
function rval(){var v=String($('brt').value).replace(/^\$/,'').replace(/,/g,'').trim();return /^\d{1,5}(\.\d{1,2})?$/.test(v)?Math.round(parseFloat(v)*100):NaN;}
$('bsm').addEventListener('click',function(){$('bin').value=RUN.id;$('bfl').classList.remove('err');});
$('bfe').addEventListener('click',function(e){var b=e.target.closest&&e.target.closest('.fb');if(!b||S.fee)return;S.bs=b.id.slice(2);var r={u:'0.85',h:'310.00',b:'680.00'}[S.bs];$('brt').value=r;render();});
function typeIn(id,t,done){var i=0;(function k(){$(id).value=t.slice(0,i);if(i<t.length){i++;later(k,70);}else done();})();}
function resetState(){S={open:false,fee:false,bs:'u',rate:0,post:false,portal:false,rec:false};$('bin').value='';$('brt').value='';$('bfl').classList.remove('err');$('bfr').classList.remove('err');render();}
var CAPAT=function(hh){return cur<=1?{l:14,t:visH()-hh-14}:{l:14,t:96};};
var ST=[
{id:'open',target:function(){return mode==='try'?$('bsb'):$('bin');},prompt:'Click Open to open run R-5108',where:'below',
 ok:function(){if(!val())$('bin').value='R-5108';var v=val(),b=!(v==='R-5108'||v==='R5108');$('bem').textContent=v?'No completed run found. Try R-5108':'Enter a run, for example R-5108';$('bfl').classList.toggle('err',b);return !b;},
 run:function(quick){var go=function(){$('bin').value=RUN.id;$('bfl').classList.remove('err');S.open=true;$('brt').value='0.85';render();};if(mode==='watch'&&!quick)typeIn('bin',RUN.id,go);else go();},
 after:function(){return['Open a completed run and read its billing lines',RUN.id+' for '+RUN.cl+': '+n0(RUN.cs)+' cases. Plant packaging '+mc(packT())+', client materials at $0.00.'];}},
{id:'fee',target:function(){return mode==='try'?$('bad'):$('brt');},prompt:'Click Add fee at 0.85 per unit',where:'above',
 ok:function(){if(!$('brt').value)$('brt').value='0.85';var b=!(rval()>0);$('bfr').classList.toggle('err',b);return !b;},
 run:function(quick){var go=function(){var r=mode==='watch'?RATE.u:rval();if(!(r>0)){r=RATE.u;S.bs='u';}if(mode==='watch')S.bs='u';S.rate=r;S.fee=true;$('bfr').classList.remove('err');render();};if(mode==='watch'&&!quick){S.bs='u';$('brt').value='';typeIn('brt','0.85',go);}else{if(!$('brt').value)$('brt').value='0.85';go();}},
 after:function(){return['Add a conversion fee by unit, hour or batch',BAS[S.bs][0]+': '+qtyS(S.bs)+' '+BAS[S.bs][1]+' at '+rateS(S.rate)+' is '+mc(convT())+'. The run now bills '+mc(total())+'.'];}},
{id:'post',target:function(){return $('bpo');},prompt:'Click Post to invoice',where:'below',run:function(){S.post=true;render();},
 after:function(){return['Post the run to the client invoice',INV+' for '+RUN.cl+': '+mc(convT())+' conversion plus '+mc(packT())+' packaging, '+mc(total())+' in all.'];}},
{id:'portal',target:function(){return $('bpv');},prompt:'Open the client portal view',where:'below',run:function(){S.portal=true;render();},
 after:function(){return['The client checks the portal, not the phone',RUN.cl+' sees '+RUN.id+' completed and invoiced, '+INV+' for '+mc(total())+', and its own stock. No other client is visible.'];}},
{id:'rec',target:function(){return $('tbm');},prompt:'Open Materials to reconcile',where:'above',run:function(){S.rec=true;render();},
 after:function(){var m=MAT[1];return['Reconcile material used against received',m[0]+': '+kg(m[3])+' received, '+kg(m[2])+' used, '+kg(exp(m))+' expected, '+kg(m[4])+' counted. Short '+kg(vr(m))+' kg, '+pct(m)+'.'];}}];
'''
