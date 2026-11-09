"""Furniture and woodworking card 4: Estimated vs Actual Job Margin. A bar chart plus variance table: project P-0412 with paired
estimated and actual cost bars per sub job, project totals (37.4% estimated, 33.5% actual, 3,188 over), the Kitchen variance
by cost line, labor by department from the time logs, the Build entries, and the Closet that beat its estimate.
Labor at 52 per hour. Margins to 0.1 percent."""
SUMMARY = 'Estimated vs Actual Job Margin (paired estimated and actual cost bars per sub job, project totals, variance by cost line, labor hours by department from the time logs)'
ARIA = 'Interactive product screen: load project P-0412, compare estimated and actual cost for the Kitchen, Primary closet and Mudroom, see the project run 3,188 over, open the Kitchen variance and its labor by department'
STEPS = 7
HEADLINE = 'Estimated vs Actual Job Margin'
STUDIO = dict(lede='A typical job costing report, built on your Sutton data with Studio. Want it different? Describe the change.',
              examples=['Add an overhead rate by workstation', 'Flag sub jobs below target margin', 'Split labor by installer', 'Email a weekly margin summary'],
              built_on='Work orders, time logs and costing', change='Cost lines, targets and views')
STORY = [('Project margin', 'rep', 'text input', 'top left'), ('Project margin', 'rep', 'suggestion', 'top center'),
         ('Project margin', 'rep', 'table row', 'bottom'), ('Kitchen variance', 'rep', 'chart bar', 'center'),
         ('Labor: Kitchen', 'pro', 'link', 'right'), ('Labor: Kitchen', 'pro', 'table row', 'center'),
         ('Project margin', 'rep', 'nav item', 'top left')]
RATE = 52
# sub job: revenue, estimate (materials, labor hours, other), actual (materials, labor hours, other)
SUBS = [('Kitchen', 52000, (19800, 220, 2100), (21350, 248, 2240)),
        ('Primary closet', 18500, (6900, 70, 600), (6650, 64, 590)),
        ('Mudroom', 9800, (3300, 40, 380), (3520, 47, 410))]
DEPTS = [('Mill', 56, 60), ('Build', 66, 76), ('Finish', 46, 52), ('Assemble', 52, 60)]
BUILD_LOG = [('Nov 10', 'DS', 'Face frames', 8.0), ('Nov 11', 'DS', 'Door panels', 7.5), ('Nov 12', 'KM', 'Door rework, two doors', 6.5), ('Nov 13', 'DS', 'Drawer boxes', 8.0)]
BUILD_REST = (7, 46.0)   # entries and hours not listed

CSS = (
 '.tb{display:flex;align-items:flex-end;gap:10px;flex:none;position:relative}.tb .fld{width:210px}.tb .fld input{font-size:11px;padding:6px 8px}.smp{height:28px;padding:0 9px;border:1px dashed #A1A1AA;border-radius:6px;background:#fff;font-size:9.8px;cursor:pointer;display:inline-flex;align-items:center;gap:5px}.smp:hover,.smp.fakehover{background:#F4F4F5}.smp .mono{font-weight:600}'
 '.dd{position:absolute;left:0;top:50px;z-index:12;width:300px;background:#fff;border:1px solid #E4E4E7;border-radius:8px;box-shadow:0 8px 22px rgba(0,0,0,.12);padding:4px}.dd button{display:flex;width:100%;gap:8px;align-items:baseline;text-align:left;border:0;background:none;padding:7px 8px;border-radius:5px;font-size:10px;cursor:pointer}.dd button:hover,.dd button.fakehover{background:#F4F4F5}.dd small{color:#71717A;font-size:8.8px}'
 '.tl{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;flex:none}.tile{border:1px solid #E4E4E7;border-radius:8px;padding:7px 10px;display:flex;flex-direction:column;gap:2px}.tile small{font-size:8.8px;color:#71717A}.tile b{font-family:"JetBrains Mono",ui-monospace,monospace;font-size:15px;font-weight:600}.tile span{font-size:8.8px;color:#52525B}'
 '.ch4{border:1px solid #E4E4E7;border-radius:10px;padding:10px 14px 8px;flex:none;display:flex;flex-direction:column;gap:6px}.ch4 .ct2{display:flex;justify-content:space-between;align-items:center;font-size:10.4px;font-weight:600}'
 '.plot{position:relative;display:grid;grid-template-columns:repeat(3,1fr);gap:28px;padding:0 6px 0 46px;border-bottom:1px solid #D4D4D8}'
 '.gl{position:absolute;left:46px;right:0;border-top:1px dashed #F0F0F1}.gl span{position:absolute;left:-46px;top:-6px;font-family:"JetBrains Mono",ui-monospace,monospace;font-size:8px;color:#A1A1AA;width:40px;text-align:right}'
 '.grp{position:relative;display:flex;align-items:flex-end;justify-content:center;gap:8px;border:0;background:none;padding:0 6px;cursor:pointer;border-radius:8px 8px 0 0;transition:background-color .25s}.grp:hover,.grp.fakehover{background:#FAFAFA}.grp.sel{background:#F4F4F5}.grp.win{background:#F0FDF4}'
 '.br{width:46px;border-radius:5px 5px 0 0;position:relative;transform-origin:bottom}.br.e{background:#E4E4E7}.br.a{background:#3F3F46}.grp.win .br.a{background:#15803D}.anim .br{animation:grow .7s cubic-bezier(.22,.9,.28,1) both}@keyframes grow{from{transform:scaleY(0)}}'
 '.br b{position:absolute;top:-14px;left:50%;transform:translateX(-50%);font:600 8.6px "JetBrains Mono",ui-monospace,monospace;color:#52525B;white-space:nowrap}'
 '.xl{display:grid;grid-template-columns:repeat(3,1fr);gap:28px;padding:0 6px 0 46px}.xl div{display:flex;flex-direction:column;align-items:center;gap:3px;font-size:9.8px;font-weight:600}'
 '.lk{display:flex;gap:14px;font-size:9px;color:#52525B}.lk span{display:inline-flex;align-items:center;gap:5px}.lk i{width:10px;height:10px;border-radius:2px}'
 '.vt .row{grid-template-columns:1fr 66px 66px 66px 62px 62px;font-size:9.8px;min-height:26px;white-space:nowrap}.vt .row>span:nth-child(n+2){text-align:right}.vt .row.pj{font-weight:600}'
 '.vp .row{grid-template-columns:1fr 92px 92px 74px;font-size:9.8px;min-height:28px}.vp .row>span:nth-child(n+2){text-align:right}.vp .row.tt{font-weight:600}.up{color:#B91C1C}.dn{color:#166534}'
 '.lt .row{grid-template-columns:90px 60px 60px 60px 1fr;font-size:9.8px;min-height:30px;white-space:nowrap}.lt .row>span:nth-child(n+2):nth-child(-n+4){text-align:right}'
 '.hb{position:relative;height:8px;border-radius:4px;background:#F0F0F1;margin-left:12px}.hb i{position:absolute;left:0;top:0;bottom:0;border-radius:4px;background:#D4D4D8}.hb em{position:absolute;top:0;bottom:0;border-radius:0 4px 4px 0;background:#3F3F46}'
 '.le .row{grid-template-columns:54px 30px 1fr 50px;font-size:9.8px;min-height:27px}.le .row>span:last-child{text-align:right}'
 '.ini{display:inline-grid;place-items:center;width:20px;height:20px;border-radius:50%;background:#18181B;color:#fff;font-size:7.6px;font-weight:600}'
 '.src{display:flex;align-items:center;gap:8px;font-size:10px;flex:none}'
 '.lnk{border:0;background:none;padding:2px 3px;margin:0 -3px;border-radius:4px;font:inherit;color:#18181B;font-weight:600;cursor:pointer;text-decoration:underline;text-decoration-color:#A1A1AA;text-underline-offset:2px}.lnk.fakehover,.lnk:hover{background:#F4F4F5}'
 # phone: a vertical list of paired bars
 '.pl{display:flex;flex-direction:column;gap:3px}.pr4{display:flex;flex-direction:column;gap:2px;border:0;background:none;padding:2px 4px;border-radius:7px;text-align:left;cursor:pointer;width:100%}.pr4.sel{background:#F4F4F5}.pr4.win{background:#F0FDF4}.pr4.fakehover{background:#FAFAFA}'
 '.pr4 .nm{display:flex;justify-content:space-between;font-size:10px;font-weight:600}.hr{display:flex;align-items:center;gap:6px;line-height:10px;font:500 8.4px "JetBrains Mono",ui-monospace,monospace;color:#52525B}.hr i{height:6px;border-radius:2px;display:block}.anim .hr i{animation:grw .7s cubic-bezier(.22,.9,.28,1) both;transform-origin:left}@keyframes grw{from{transform:scaleX(0)}}'
 '.shot.ph .tb .fld{width:auto;flex:1}.shot.ph .dd{width:100%}.shot.ph .tile{padding:3px 8px;gap:0}.shot.ph .tile b{font-size:12px}.shot.ph .pr4 .ch{padding:0 5px}.shot.ph .vp .row{grid-template-columns:1fr 74px;min-height:23px}.shot.ph .lt .row{grid-template-columns:62px 40px 40px 1fr;min-height:24px}.shot.ph .le .row{min-height:23px}'
)

WIN = ''

JS = r'''
var FOC='.rail .ni,.bc,.phd>*,.bn .bi,.tb>*,.dd button,.pg .tile,.ch4 .ct2,.ch4 .grp,.ch4 .xl,.ch4 .lk,.pg .cd>*,.pg .cd .row,.pl>*,.pg .src>*,.pg .empt';
var RATE=__RATE__,SUBS=__SUBS__,DEPTS=__DEPTS__,BLOG=__BLOG__,BREST=__BREST__;
var S;
function cost(p){return p[0]+p[1]*RATE+p[2];}
function sub(i){var s=SUBS[i],e=cost(s[2]),a=cost(s[3]);return {nm:s[0],rev:s[1],e:e,a:a,em:(s[1]-e)/s[1]*100,am:(s[1]-a)/s[1]*100};}
function proj(){var r=0,e=0,a=0;SUBS.forEach(function(s){r+=s[1];e+=cost(s[2]);a+=cost(s[3]);});return {rev:r,e:e,a:a,em:(r-e)/r*100,am:(r-a)/r*100};}
function p1(v){return v.toFixed(1)+'%';}
function d0(n){return (n<0?'-':'')+'$'+n0(Math.abs(n));}
function sg(n){return (n>0?'+':n<0?'-':'')+'$'+n0(Math.abs(n));}
function tiles(P){var p=proj();return '<div class="tl in"'+(P?' style="grid-template-columns:1fr 1fr"':'')+'>'+(P?'':'<div class="tile"><small>Revenue</small><b>'+d0(p.rev)+'</b><span>3 sub jobs</span></div>')+'<div class="tile"><small>Margin, est to actual</small><b id="pm">'+p1(p.em)+' to '+p1(p.am)+'</b>'+(P?'':'<span>Estimated '+p1(p.em)+', actual '+p1(p.am)+'</span>')+'</div><div class="tile"><small>Cost vs estimate</small><b id="gap">'+d0(p.a-p.e)+' over</b>'+(P?'':'<span>'+d0(p.e)+' estimated, '+d0(p.a)+' actual</span>')+'</div></div>';}
function chart(){var mx=40000,h=S.tot?132:178,g='';[0,10000,20000,30000,40000].forEach(function(v){g+='<div class="gl" style="bottom:'+(v/mx*h)+'px"><span>'+(v/1000)+'k</span></div>';});
 return '<div class="ch4"><div class="ct2"><span>Cost by sub job</span><span class="lk"><span><i style="background:#E4E4E7"></i>Estimated</span><span><i style="background:#3F3F46"></i>Actual</span></span></div><div class="plot'+(S.anim?' anim':'')+'" style="height:'+h+'px">'+g+SUBS.map(function(s,i){var x=sub(i),k=['k','c','m'][i];
  return '<button type="button" class="grp'+(S.sel===i?' sel':'')+(S.win&&i===1?' win':'')+'" id="g-'+k+'" aria-label="'+x.nm+' estimated and actual cost"><span class="br e" style="height:'+(x.e/mx*h)+'px;animation-delay:'+(i*.12)+'s"><b>'+n0(x.e)+'</b></span><span class="br a" style="height:'+(x.a/mx*h)+'px;animation-delay:'+(i*.12+.08)+'s"><b>'+n0(x.a)+'</b></span></button>';}).join('')+'</div>'+
  '<div class="xl">'+SUBS.map(function(s,i){var x=sub(i),up=x.am>x.em;return '<div>'+x.nm+'<span class="ch '+(up?'c-ok':'c-warn')+'" id="mc-'+i+'">'+p1(x.em)+' to '+p1(x.am)+'</span></div>';}).join('')+'</div></div>';}
function vtable(){var p=proj();return '<div class="cd vt" style="flex:1 1 0"><div class="row h"><span>Sub job</span><span>Revenue</span><span>Est cost</span><span>Actual</span><span>Est margin</span><span>Margin</span></div>'+SUBS.map(function(s,i){var x=sub(i);return '<div class="row"><span>'+x.nm+'</span><span class="mono">'+n0(x.rev)+'</span><span class="mono">'+n0(x.e)+'</span><span class="mono">'+n0(x.a)+'</span><span class="mono mut">'+p1(x.em)+'</span><span class="mono">'+p1(x.am)+'</span></div>';}).join('')+
 '<button type="button" class="row pj'+(S.tot?' sel':'')+'" id="r-p"><span>Project P-0412</span><span class="mono">'+n0(p.rev)+'</span><span class="mono">'+n0(p.e)+'</span><span class="mono">'+n0(p.a)+'</span><span class="mono mut">'+p1(p.em)+'</span><span class="mono">'+p1(p.am)+'</span></button></div>';}
function lines(i){var s=SUBS[i],e=s[2],a=s[3];return [['Materials',e[0],a[0]],['Labor, '+e[1]+' to '+a[1]+' h',e[1]*RATE,a[1]*RATE],['Other',e[2],a[2]]];}
function vpanel(P){var L=lines(0),t=L.reduce(function(a,l){return a+l[2]-l[1];},0);
 return '<div class="cd vp in"'+(P?'':' style="flex:1 1 0"')+'><div class="ct">Kitchen variance by cost line<button type="button" class="lnk" id="lab">View labor entries</button></div>'+(P?'':'<div class="row h"><span>Cost line</span><span>Estimated</span><span>Actual</span><span>Variance</span></div>')+
 L.map(function(l,k){return '<div class="row"><span>'+(P?l[0].split(',')[0]:l[0])+'</span>'+(P?'':'<span class="mono">'+n0(l[1])+'</span><span class="mono">'+n0(l[2])+'</span>')+'<span class="mono up" id="vv-'+k+'">'+sg(l[2]-l[1])+'</span></div>';}).join('')+
 '<div class="row tt"><span>Kitchen total</span>'+(P?'':'<span class="mono">'+n0(sub(0).e)+'</span><span class="mono">'+n0(sub(0).a)+'</span>')+'<span class="mono up" id="vt">'+sg(t)+'</span></div></div>';}
function plist(){var mx=40000;return '<div class="pl'+(S.anim?' anim':'')+'">'+SUBS.map(function(s,i){var x=sub(i),k=['k','c','m'][i],up=x.am>x.em;
 return '<button type="button" class="pr4'+(S.sel===i?' sel':'')+(S.win&&i===1?' win':'')+'" id="g-'+k+'"><span class="nm"><span>'+x.nm+'</span><span class="ch '+(up?'c-ok':'c-warn')+'" id="mc-'+i+'">'+p1(x.em)+' to '+p1(x.am)+'</span></span><span class="hr"><i style="width:'+(x.e/mx*190)+'px;background:#D4D4D8"></i>'+n0(x.e)+'</span><span class="hr"><i style="width:'+(x.a/mx*190)+'px;background:'+(S.win&&i===1?'#15803D':'#3F3F46')+'"></i>'+n0(x.a)+'</span></button>';}).join('')+'</div>';}
function render(){var P=ph(),h='',scr=S.scr;
if(scr==='m'||scr==='kv'){var kv=scr==='kv';
 setNav({m:'rep',bc:kv?['Reports','Job margin','P-0412','Kitchen']:['Reports','Job margin'].concat(S.load?['P-0412']:[]),t:S.load?(P?'P-0412':'P-0412 Residential kitchen and primary suite'):'Job margin',chip:S.tot?['c-warn',d0(proj().a-proj().e)+' over']:null,scr:kv?'Kitchen variance':'Project margin',back:P&&kv?1:0});
 var tb='<div class="tb frm"><label class="fld" id="fp"><small>Project</small><input id="ip" value="'+S.vp+'" placeholder="Type a project, like P-0412" autocomplete="off" spellcheck="false"><span class="em">Try P-0412</span></label><button type="button" class="smp" id="smp">Try <span class="mono">P-0412</span></button>'+
  (S.dd?'<div class="dd in"><button type="button" id="sg"><span class="mono" style="font-weight:600">P-0412</span><span>Residential kitchen and primary suite</span></button><button type="button"><span class="mono">P-0409</span><span>Lake house vanities <small>Open</small></span></button></div>':'')+'</div>';
 if(!S.load){h=tb+'<div class="empt" style="'+(P?'flex:1 1 0':'flex:none;height:150px')+'"><b>No project chosen</b><span>Choose a project to compare estimate and actual.</span></div>'+(P?'':'<div class="cd" style="flex:1 1 0"><div class="ct">Projects<span class="mut" style="font-weight:500">Costed from work orders and time logs</span></div>'+[['P-0412','Residential kitchen and primary suite','3 sub jobs','Closed Nov 20','c-idle'],['P-0411','Restaurant banquettes','2 sub jobs','Closed Nov 13','c-idle'],['P-0410','Library shelving','4 sub jobs','In production','c-info'],['P-0409','Lake house vanities','2 sub jobs','In production','c-info'],['P-0408','Office reception and conference','3 sub jobs','Closed Nov 6','c-idle'],['P-0407','Walnut dining set','1 sub job','Closed Oct 30','c-idle'],['P-0405','Mudroom and laundry','2 sub jobs','Closed Oct 23','c-idle'],['P-0404','Wine room racking','1 sub job','Closed Oct 16','c-idle']].map(function(x){return '<div class="row" style="grid-template-columns:54px 1fr 72px 92px;font-size:9.8px;min-height:31px;white-space:nowrap"><span class="mono">'+x[0]+'</span><span>'+x[1]+'</span><span class="mut">'+x[2]+'</span><span style="text-align:right"><span class="ch '+x[4]+'">'+x[3]+'</span></span></div>';}).join('')+'</div>');}
 else if(!P){h=(S.tot?tiles(P):'')+chart()+(kv?vpanel(P):vtable());}
 else if(kv)h=vpanel(P);
 else h=(S.tot?tiles(P):'')+plist()+(S.tot?'':'<div class="cd"><button type="button" class="row" id="r-p" style="grid-template-columns:1fr auto;min-height:28px"><span style="font-weight:600">Project P-0412 total</span><span class="mono">'+n0(proj().rev)+'</span></button></div>');}
else{var bo=S.bo;setNav({m:'pro',bc:['Production','Time logs','P-0412 Kitchen'],t:P?'Kitchen labor':'Labor: P-0412 Kitchen',chip:['c-warn',(DEPTS.reduce(function(a,d){return a+d[2]-d[1];},0))+' h over'],scr:'Labor: Kitchen',back:P?1:0});
 var te=0,ta=0;DEPTS.forEach(function(d){te+=d[1];ta+=d[2];});
 var dt='<div class="cd lt"><div class="row h"><span>Department</span><span>Estimate</span><span>Actual</span><span>Over</span>'+(P?'':'<span style="padding-left:12px">Actual vs estimate</span>')+'</div>'+DEPTS.map(function(d){var b=d[0]==='Build';return '<button type="button" class="row'+(b&&bo?' sel':'')+'" id="d-'+d[0].toLowerCase()+'"><span>'+d[0]+'</span><span class="mono mut">'+d[1]+' h</span><span class="mono">'+d[2]+' h</span><span class="mono up">+'+(d[2]-d[1])+' h</span>'+(P?'':'<span class="hb"><i style="width:'+(d[1]/80*100)+'%"></i><em style="left:'+(d[1]/80*100)+'%;width:'+((d[2]-d[1])/80*100)+'%"></em></span>')+'</button>';}).join('')+
  '<div class="row" style="font-weight:600"><span>Total</span><span class="mono" id="lte">'+te+' h</span><span class="mono" id="lta">'+ta+' h</span><span class="mono up" id="lto">+'+(ta-te)+' h</span>'+(P?'':'<span class="mono mut" style="padding-left:12px">'+n0(ta*RATE)+' at '+RATE+' an hour</span>')+'</div></div>';
 var le='<div class="cd le in"'+(P?'':' style="flex:1 1 0"')+'><div class="ct">Build entries<span class="mono mut" style="font-weight:500" id="bsum">'+(BLOG.reduce(function(a,x){return a+x[3];},0)+BREST[1])+' h, '+(BLOG.length+BREST[0])+' entries</span></div>'+BLOG.slice(0,P?3:4).map(function(x){return '<div class="row"><span class="mono mut">'+x[0]+'</span><span><span class="ini">'+x[1]+'</span></span><span>'+x[2]+(x[2].indexOf('rework')>-1?' <span class="ch c-warn">Rework</span>':'')+'</span><span class="mono">'+x[3].toFixed(1)+' h</span></div>';}).join('')+(P?'':'<div class="row"><span></span><span></span><span class="mut">'+BREST[0]+' more entries</span><span class="mono">'+BREST[1].toFixed(1)+' h</span></div>')+'</div>';
 if(P)h=bo?le:dt;
 else h='<div class="src"><span class="mut">From time logs on work orders for</span><span class="mono" style="font-weight:600">P-0412 Kitchen</span><span class="mut">, labor at '+RATE+' an hour</span></div>'+dt+(bo?le:'<div class="cd" style="flex:1 1 0"><div class="ct">Where the hours came from</div><div class="empt" style="border:0;background:none;padding:16px"><b>Pick a department</b><span>Its time entries show here, with who logged them and on which step.</span></div></div>');}
$('pg').innerHTML=h;S.anim=false;}
$('pg').addEventListener('input',function(e){if(e.target.id==='ip')S.vp=e.target.value;});
function resetState(){S={scr:'m',dd:false,load:false,tot:false,sel:null,bo:false,win:false,anim:false,vp:''};render();}
function okP(){var v=String($('ip').value).trim(),b=!(v===''||/^P-?0412$/i.test(v));$('fp').classList.toggle('err',b);return !b;}
var CAPAT=function(hh){return ph()?{l:8,t:5}:{l:14,t:visH()-hh-40};};
var ST=[
{id:'fld',target:function(){return $('ip');},prompt:'Click the project field',where:'below',run:function(){S.dd=true;render();},after:['Pick a project to see how it really went','Open projects show as you type.'],pc:'Pick a project to see how it went'},
{id:'load',target:function(){return $('sg');},prompt:'Type P-0412 and press Enter, or click P-0412',where:'right',ok:okP,run:function(q){S.vp='P-0412';S.dd=false;S.load=true;S.anim=!q;render();},after:['Estimate and actual, side by side','Kitchen, Primary closet and Mudroom, each with its margin.']},
{id:'tot',target:function(){return $('r-p');},prompt:'Click the project row',where:'above',run:function(){S.tot=true;render();},
 after:function(){var p=proj();return['The project ran '+d0(p.a-p.e)+' over','Margin '+p1(p.em)+' estimated, '+p1(p.am)+' actual.'];}},
{id:'kit',target:function(){return $('g-k');},prompt:'Click the Kitchen bars',where:'right',run:function(){S.sel=0;S.scr='kv';render();},
 after:function(){var L=lines(0);return['The Kitchen is where the margin went','Materials '+sg(L[0][2]-L[0][1])+', labor '+sg(L[1][2]-L[1][1])+', other '+sg(L[2][2]-L[2][1])+'.'];},pc:'The Kitchen is where the margin went'},
{id:'lab',target:function(){return $('lab');},prompt:'Click View labor entries',where:'below',run:function(){S.scr='lab';render();},after:['Labor shows which departments ran long','248 hours against 220 estimated, by department.'],pc:'Labor shows which departments ran long'},
{id:'bld',target:function(){return $('d-build');},prompt:'Click the Build row',where:'below',run:function(){S.bo=true;render();},after:['Build ran ten hours over, the most of any department','76 h against 66, including 6.5 h of door rework.'],pc:'Build ran ten hours over'},
{id:'back',target:function(){return $(ph()?'bn-rep':'nv-rep');},prompt:'Click Reports',where:'right',run:function(){S.scr='m';S.sel=null;S.win=true;render();},
 after:function(){var x=sub(1);return['Some jobs beat the estimate. Now you know which','Primary closet: '+p1(x.am)+' actual margin against '+p1(x.em)+' estimated.'];},pc:'Some jobs beat the estimate'}];
'''
JS = (JS.replace('__RATE__', repr(RATE)).replace('__SUBS__', repr([[s[0], s[1], list(s[2]), list(s[3])] for s in SUBS]).replace("'", '"'))
      .replace('__DEPTS__', repr([list(d) for d in DEPTS]).replace("'", '"')).replace('__BLOG__', repr([list(b) for b in BUILD_LOG]).replace("'", '"'))
      .replace('__BREST__', repr(list(BUILD_REST))))
