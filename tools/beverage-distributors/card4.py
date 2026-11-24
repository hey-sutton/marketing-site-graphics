"""Beverage distributors card 4: Orders, deposits and delivery status. An order form with a deposit line above a four
column status board, inside the app shell. Start: the account field (prefilled Pier 9 Bar, read only), an empty order
form and the board with its baseline counts (Open 5, Picked 4, Loaded 3, Delivered 11, 23 orders). Walkthrough: use the
account (its price list applies to the SKU chips), tap three SKUs to add lines (40 Harbor Lager at $24.50 = $980.00,
20 Cold Brew RTD at $19.00 = $380.00, 2 half barrel kegs at $165.00 = $330.00), each line checks available stock (760
covers 40, 780 covers 20) and the keg deposit lands as its own line (2 at $30.00 = $60.00), create the order (goods
$1,690.00 + deposit $60.00 = $1,750.00, Open 6, 24 orders), then move it across the board to Delivered (Open 5,
Picked 4, Loaded 3, Delivered 12). Money is held in cents. Numbers are asserted in numbers_check.py."""
SUMMARY = 'Orders, deposits and delivery status (an account picked, its price list applied, three SKUs tapped into lines with a stock check each, the keg deposit as its own line, the order created and moved across a four column board to delivered)'
ARIA = 'Interactive product screen: pick Pier 9 Bar, add Harbor Lager, Cold Brew and two half barrel kegs with their deposit, create the $1,750.00 order, then move it across the status board to delivered'
STEPS = 4
STUDIO = dict(lede='A typical order desk and delivery board, built on your Sutton data with Studio. Want it different? Describe the change.',
              examples=['Add a deposit type', 'Change the price list rule', 'Add a delivery route field', 'Add a driver column'],
              built_on='Accounts, price lists, orders and deliveries', change='Fields, rules and columns')
STORY = [('Order form', 'sal', 'inline button', 'top right'), ('Order form', 'sal', 'sku chip', 'center left'),
         ('Order form', 'sal', 'primary button', 'center right'), ('Delivery board', 'dlv', 'board card', 'bottom left')]

CSS = (
 '.sk{display:flex;gap:6px;padding:8px 11px;border-bottom:1px solid #F0F0F1;flex-wrap:wrap}.chp{display:inline-flex;align-items:center;gap:7px;height:28px;padding:0 10px;border:1px solid #E4E4E7;border-radius:999px;background:#fff;font:inherit;font-size:9.8px;font-weight:500;color:#18181B;cursor:pointer;white-space:nowrap;transition:border-color .2s,background-color .2s,opacity .2s}'
 '.chp b{font-family:var(--mn);font-weight:500;font-size:9.4px;color:#52525B}.chp:hover,.chp.fakehover{border-color:#18181B;background:#F4F4F5}.chp:focus-visible{outline:2px solid #18181B;outline-offset:1px}.chp.on{background:#F4F4F5;color:#71717A;cursor:default}.chp.on b{color:#A1A1AA}.chp:disabled{opacity:.5;cursor:default}'
 '.ln4 .row{grid-template-columns:1fr 44px 62px 72px 116px;font-size:9.8px;min-height:27px;white-space:nowrap}.ln4 .row>span:nth-child(n+2):nth-child(-n+4){text-align:right;font-family:var(--mn)}.ln4 .row.h>span{font-family:Inter,sans-serif}.ln4 .row>span:last-child{text-align:right}'
 '.ln4 .row.dep{background:#FAFAFA;color:#52525B}.ln4 .row.new{animation:exin .45s cubic-bezier(.22,.9,.28,1) both}.tg{font-size:8px;font-weight:600;color:#1E3A8A;background:#E8EEFC;border-radius:3px;padding:1px 4px;margin-left:5px}'
 '.sc4{display:inline-flex;align-items:center;gap:5px;font-size:9px;color:#166534}.sc4 i{width:6px;height:6px;border-radius:50%;background:#16A34A}.sc4 .mono{color:#52525B}'
 '.ft{display:flex;align-items:center;gap:14px;padding:8px 11px;border-top:1px solid #F0F0F1;font-size:9.8px;color:#71717A}.ft b{font-family:var(--mn);color:#18181B;font-size:10.2px}.ft .tot b{font-size:12px}.ft .bt{margin-left:auto}'
 '.e4{padding:30px 11px;font-size:9.8px;color:#71717A;text-align:center;line-height:1.45}'
 '.bd{display:grid;grid-template-columns:repeat(4,1fr);gap:8px}.bcl{border:1px solid #E4E4E7;border-radius:8px;background:#FAFAFA;padding:7px;display:flex;flex-direction:column;gap:5px;min-width:0}'
 '.bcl>header{display:flex;justify-content:space-between;align-items:center;font-size:9.6px;font-weight:600;padding:0 2px}.bcl>header b{font-family:var(--mn);font-size:11px;transition:color .3s}.bcl.chg>header b{animation:exflash 1.2s ease}'
 '.oc{border:1px solid #E4E4E7;border-radius:6px;background:#fff;padding:5px 7px;display:flex;flex-direction:column;gap:1px;font:inherit;text-align:left;color:#18181B;line-height:1.3;min-width:0}.oc b{font-family:var(--mn);font-size:9.4px;font-weight:600}.oc span{font-size:8.6px;color:#71717A;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}'
 '.oc.me{border-color:#18181B;box-shadow:0 0 0 1px #18181B;animation:exin .45s cubic-bezier(.22,.9,.28,1) both}button.oc{cursor:pointer}button.oc:hover,button.oc.fakehover{background:#F4F4F5}button.oc:focus-visible{outline:2px solid #18181B;outline-offset:1px}.oc.dn{border-color:#BBF7D0;box-shadow:0 0 0 1px #BBF7D0}'
 '.mr4{font-size:8.6px;color:#A1A1AA;padding:0 3px;white-space:nowrap}.bth{display:flex;justify-content:space-between;align-items:center;font-size:10.6px;font-weight:600;padding:0 2px}.bth span{font-weight:500;font-size:9.4px;color:#71717A}'
 '.kg{display:grid;grid-template-columns:repeat(5,1fr);gap:8px 12px;padding:9px 11px}.tl4{display:flex;flex-direction:column;gap:4px;padding:9px 11px}.tl4 .st{display:grid;grid-template-columns:64px 1fr 60px;font-size:9.6px;align-items:center}.tl4 .st i{width:7px;height:7px;border-radius:50%;background:#D4D4D8;display:inline-block;margin-right:6px}.tl4 .st.ok i{background:#16A34A}.tl4 .st span:last-child{text-align:right;font-family:var(--mn);color:#71717A}'
 '.dp4{display:grid;grid-template-columns:1fr 236px;gap:10px}.rts .row{grid-template-columns:70px 1fr 60px 50px;font-size:9.6px;white-space:nowrap}.rts .row span:last-child{text-align:right}.ln4.cp .row{grid-template-columns:1fr 30px 56px 62px}.ln4.cp .row>span:nth-child(5){display:none}.tl4 .st{grid-template-columns:72px 1fr 36px}'
 '.shot.ph .sk{padding:6px;gap:5px;flex-wrap:nowrap}.shot.ph .chp{height:40px;flex:1;justify-content:center;padding:0 6px;font-size:10px}.shot.ph .chp b{display:none}'
 '.shot.ph .ln4 .row{grid-template-columns:1fr 70px;min-height:21px;font-size:10px}.shot.ph .ln4 .row>span:nth-child(2),.shot.ph .ln4 .row>span:nth-child(3),.shot.ph .ln4 .row>span:nth-child(5){display:none}.shot.ph .ln4 .row.h{display:none}'
 '.shot.ph .ft{padding:6px 9px;gap:8px}.shot.ph .ft .gd{display:none}.shot.ph .bt.w{width:100%;min-height:40px;font-size:10.6px}'
 '.bt4{display:grid;grid-template-columns:1fr 1fr;gap:6px}.tile{border:1px solid #E4E4E7;border-radius:8px;padding:4px 9px;display:flex;flex-direction:column;background:#fff;min-height:38px}.tile small{font-size:8.8px;color:#71717A}.tile b{font-family:var(--mn);font-size:13px;font-weight:600}.tile.chg b{animation:exflash 1.2s ease}'
 '.shot.ph button.oc{min-height:40px;flex-direction:row;align-items:center;justify-content:space-between}.shot.ph.nar .xn{display:none}.shot.ph .e4{padding:10px}.shot.ph.nar .e4{padding:6px 8px}'
)

WIN = ''

JS = r'''
var FOC='.rail .ni,.bc,.phd>*,.bn .bi,.pg .rof,.pg .ct,.pg .sk,.pg .row,.pg .ft,.pg .e4,.pg .bcl,.pg .bth,.pg .kg,.pg .tl4,.pg .tile,.pg .bt,.pg .oc';
var AC='Pier 9 Bar',SO='SO-5131',DEP=3000;
var SKU=[['hl','Harbor Lager 24 pack','Lager',40,2450,760],['cb','Cold Brew RTD 4 pack','Cold Brew',20,1900,780],['kg','Half barrel keg','Keg',2,16500,36]];
var COLS=['Open','Picked','Loaded','Delivered'],BASE=[5,4,3,11];
var CARDS=[[['SO-5124','Greenline Market'],['SO-5126','Northgate Grocers'],['SO-5127','Dockside Taproom']],[['SO-5119','Elm Street Liquor'],['SO-5117','Dockside Taproom'],['SO-5116','Greenline Market']],[['SO-5112','Greenline Market'],['SO-5110','Harbor Hall'],['SO-5109','Elm Street Liquor']],[['SO-5108','Pier 9 Bar'],['SO-5103','Northgate Grocers'],['SO-5101','Greenline Market']]];
var S;
function ln(i){return SKU[i][3]*SKU[i][4];}
function goods(){var t=0;S.l.forEach(function(i){t+=ln(i);});return t;}
function dep(){return S.l.indexOf(2)>-1?SKU[2][3]*DEP:0;}
function c(v){return m2(v/100);}
function cnt(k){var n=BASE.slice();if(S.made)n[Math.min(S.st,3)]++;return n[k];}
function allIn(){return S.l.length===3;}
function nextChip(){for(var i=0;i<3;i++)if(S.l.indexOf(i)<0)return i;return -1;}
function chips(P){return '<div class="sk">'+SKU.map(function(x,i){var on=S.l.indexOf(i)>-1,pk=!on&&nextChip()===i&&S.l.length<2;return '<button type="button" class="chp'+(on?' on':'')+'" id="ch-'+x[0]+'"'+(pk?' data-pick':'')+(S.acc?'':' disabled')+'>'+(P?x[2]:x[1])+(S.acc?' <b>'+c(x[4])+'</b>':'')+'</button>';}).join('')+'</div>';}
function lines(P,cp){var h='<div class="ln4'+(cp?' cp':'')+'">'+(P?'':'<div class="row h"><span>Item</span><span>Qty</span><span>Price</span><span>Amount</span><span>Stock check</span></div>');
 S.l.forEach(function(i){var x=SKU[i],nw=S.nw===i?' new':'';h+='<div class="row'+nw+'"><span>'+(P?x[3]+' '+x[2]:x[1])+'</span><span>'+x[3]+'</span><span>'+c(x[4])+'</span><span id="la-'+x[0]+'">'+c(ln(i))+'</span><span><span class="sc4" id="sk-'+x[0]+'"><i></i><span class="mono">'+n0(x[5])+'</span> available, covers '+x[3]+'</span></span></div>';
  if(i===2)h+='<div class="row dep'+nw+'"><span>'+(P?'Keg deposit':'Keg deposit, half barrel')+(P?'':'<span class="tg">Deposit</span>')+'</span><span>2</span><span>'+c(DEP)+'</span><span id="la-dep">'+c(dep())+'</span><span class="mut" style="font-size:9px">Refunded on return</span></div>';});
 return h+'</div>';}
function foot(P){return '<div class="ft"><span class="gd">Goods <b id="o-g">'+c(goods())+'</b></span><span class="gd">Deposits <b id="o-d">'+c(dep())+'</b></span><span class="tot">Total <b id="o-t">'+c(goods()+dep())+'</b></span>'+(P?'':'<button type="button" class="bt pri" id="mk"'+(allIn()?'':' disabled')+'>Create order</button>')+'</div>';}
function form(P){var h='<div class="cd">'+(P&&!S.acc?'':'<div class="ct">'+(P?(S.l.length?AC:'Price list'):'Order lines')+(S.acc?'<span class="ch c-info" id="pl">Bar and restaurant prices</span>':'<span class="mut" style="font-weight:500">No account yet</span>')+'</div>');
 if(!S.acc)return h+'<div class="e4">Pick an account to load its price list, then tap SKUs to add lines.</div></div>';
 h+=(P&&allIn()?'':chips(P));if(!S.l.length)return h+'<div class="e4">Tap a SKU to add a line. Each line checks available stock.</div></div>';
 return h+lines(P)+foot(P)+'</div>';}
function card(o,k){return '<div class="oc"><b>'+o[0]+'</b><span>'+o[1]+'</span></div>';}
function board(P){var me='<'+(S.st<3?'button type="button"':'div')+' class="oc '+(S.st>=3?'dn':'me')+'" id="me"><b>'+SO+'</b><span>'+AC+', $1,750.00</span></'+(S.st<3?'button':'div')+'>';
 if(P)return '<div class="bt4">'+COLS.map(function(t,k){return '<div class="tile'+(S.chg&&(k===0||k===3)?' chg':'')+'"><small>'+t+'</small><b id="bd-'+k+'">'+cnt(k)+'</b></div>';}).join('')+'</div>';
 return '<div class="bth">Delivery board<span>Today, '+'<span id="bd-t">'+(cnt(0)+cnt(1)+cnt(2)+cnt(3))+'</span> orders</span></div><div class="bd">'+COLS.map(function(t,k){var mine=S.made&&(S.st===k||(S.st>=3&&k===3)),cs=CARDS[k].slice(0,(S.scr==='form'&&!S.l.length?3:2)-(mine?1:0)),n=cnt(k)-cs.length-(mine?1:0);
  return '<div class="bcl'+(S.chg&&(k===0||k===3)?' chg':'')+'"><header>'+t+'<b id="bd-'+k+'">'+cnt(k)+'</b></header>'+(mine?me:'')+cs.map(card).join('')+(n>0?'<div class="mr4">+'+n+' more</div>':'')+'</div>';}).join('')+'</div>';}
function render(){var P=ph(),h='';
if(S.scr==='form'){setNav({m:'sal',bc:['Sales',['Orders','cb-or'],'New order'],t:'New order',chip:['c-idle','Draft'],scr:'Order form',pa:S.acc?'<span class="mut" style="font-size:9.6px">Route 3, delivers Nov 17</span>':''});
 if(P){h=S.l.length?'':rof({l:'Account',id:'ia',v:AC,b:S.acc?'Applied':'Use account',bid:'ua'});
  if(!S.acc)h+=form(P)+board(P);
  else{h+=form(P);if(S.l.length)h+='<button type="button" class="bt pri w" id="mk"'+(allIn()?'':' disabled')+'>Create order</button>';}}
 else{h=rof({l:'Account',id:'ia',v:AC,b:S.acc?'Applied':'Use account',bid:'ua',cx:'On premise, route 3'})+form(P)+board(P);
  if(!S.l.length)h+='<div class="cd rts"><div class="ct">Routes today<span class="mut" style="font-weight:500">Orders by route</span></div><div class="row h"><span>Route</span><span>Area</span><span>Truck</span><span>Orders</span></div>'+[['Route 1','Harborfront and Pier district','Truck 1',7],['Route 2','Northgate and Elm Street','Truck 2',9],['Route 3','Downtown bars and taprooms','Truck 3',7]].map(function(r){return '<div class="row"><span>'+r[0]+'</span><span class="mut">'+r[1]+'</span><span class="mono">'+r[2]+'</span><span class="mono">'+r[3]+'</span></div>';}).join('')+'</div>';}}
else{var done=S.st>=3;setNav({m:'dlv',bc:['Delivery',['Board','cb-bd'],SO],t:SO+', '+AC,chip:done?['c-ok','Delivered']:['c-info',COLS[S.st]],scr:'Delivery board',back:1});
 if(P){h=board(P)+'<div class="cd">'+(done?'':'<button type="button" class="oc me" id="me" style="width:100%;border:0;box-shadow:none"><b>'+SO+'</b><span>Move to delivered</span></button>')+'<div class="ln4">'+[['Goods',c(goods())],['Keg deposit',c(dep())],['Total',c(goods()+dep())]].map(function(r,i){return '<div class="row"'+(i===2?' style="font-weight:600"':'')+'><span>'+r[0]+'</span><span></span><span></span><span'+(i===2?' id="o-t"':'')+'>'+r[1]+'</span><span></span></div>';}).join('')+'</div></div>';}
 else{h='<div class="cd"><div class="kg">'+[['Account',AC],['Order',SO],['Lines','3 plus deposit'],['Total','<span id="o-t">'+c(goods()+dep())+'</span>'],['Delivers','Nov 17, route 3']].map(function(k){return '<div class="kv"><small>'+k[0]+'</small><b>'+k[1]+'</b></div>';}).join('')+'</div></div>'+board(P);
  h+='<div class="dp4"><div class="cd">'+lines(false,1)+'</div><div class="cd"><div class="tl4">'+COLS.map(function(t,k){var ok=k<=S.st;return '<div class="st'+(ok?' ok':'')+'"><span><i></i>'+t+'</span><span class="mut">'+['Created','Bay 2','Truck 3','Signed, D. Ortiz'][k]+'</span><span>'+(ok?['9:12','9:40','10:05','11:32'][k]:'')+'</span></div>';}).join('')+'</div></div></div>';}}
if(P)h+=xw(S.scr==='form'?(S.acc?[['Deposit','$30.00 a keg'],['Delivers','Nov 17, route 3']]:[['Price list','Applies on pick'],['Route','3, delivers Nov 17'],['Orders today',String(cnt(0)+cnt(1)+cnt(2)+cnt(3))]]):[['Board today',(cnt(0)+cnt(1)+cnt(2)+cnt(3))+' orders'],['Delivers','Nov 17, route 3'],['Driver','D. Ortiz']],1);
$('pg').innerHTML=h;S.nw=-1;S.chg=false;}
function resetState(){S={scr:'form',acc:false,l:[],nw:-1,made:false,st:0,chg:false};render();}
function addNext(){var i=nextChip();if(i<0)return;S.l.push(i);S.nw=i;render();}
var CAPAT=function(hh){return ph()?{l:8,t:5}:{l:14,t:visH()-hh-40};};
var ST=[
{id:'acct',target:function(){return $('ua');},prompt:'Use account Pier 9 Bar',where:'below',run:function(){S.acc=true;render();},
 after:['The account’s price list applies','Pier 9 Bar is on bar and restaurant prices: Harbor Lager $24.50, Cold Brew RTD $19.00, half barrel keg $165.00.'],pc:'Pier 9 Bar prices applied'},
{id:'lines',target:function(){var i=nextChip();return $('ch-'+SKU[i<0?2:i][0]);},prompt:function(){var i=nextChip();return 'Tap '+SKU[i<0?2:i][1]+(i<2?' ('+(i+1)+' of 3)':' (3 of 3)');},where:'below',
 ok:function(){addNext();return allIn();},
 run:function(q){if(q){while(!allIn())addNext();return;}if(allIn()){S.nw=2;render();return;}addNext();if(!allIn())later(function(){addNext();if(!allIn())later(addNext,420);},420);},
 after:['Three lines, each with a stock check, and the deposit on its own line','Harbor Lager 40 at $24.50 and Cold Brew 20 at $19.00, both covered (760 and 780 available). 2 kegs at $165.00 plus a $60.00 deposit.'],pc:'3 lines and a $60.00 keg deposit'},
{id:'make',target:function(){return $('mk');},prompt:'Create the order',where:function(){return ph()?'above':'below';},run:function(){S.made=true;S.st=0;S.scr='board';S.chg=true;render();},
 after:['The order lands on the board','$1,690.00 in goods plus $60.00 in deposits: $1,750.00. Open goes from 5 to 6, 24 orders today.'],pc:'$1,750.00, Open now 6'},
{id:'move',target:function(){return $('me');},prompt:'Move SO-5131 to delivered',where:function(){return ph()?'below':'above';},run:function(q){if(q){S.st=3;render();return;}S.st=1;render();later(function(){S.st=2;render();},380);later(function(){S.st=3;S.chg=true;render();},760);},
 after:['Picked, loaded, delivered','SO-5131 moves across the board: Open 5, Picked 4, Loaded 3, Delivered 12. Still 24 orders today.'],pc:'Delivered: now 12 of 24'}];
ST.forEach(function(s){['prompt','where'].forEach(function(k){if(typeof s[k]==='function'){var f=s[k];Object.defineProperty(s,k,{get:f});}});});
'''
