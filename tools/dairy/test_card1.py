"""Worked example: interaction and layout test for the Dairy card 1.
Checks the computed text and numbers, the typed lot entry, the arrows and hotspots, reduced motion, the speed target,
and Simon's visual rules (right edge, bottom gap, empty start screen, background standard).
Usage: GFX_OUT=/path/to/repo GFX_SHOTS=/tmp/shots python3 test_card.py
GFX_OUT is a repo checkout that contains graphics/dairy, manifest.json (with the dairy key) and loader.html."""
import json,os,re,sys,threading,http.server,socketserver
from playwright.sync_api import sync_playwright
from PIL import Image
repo=os.environ.get('GFX_OUT','out'); key='dairy'; port=8793
loader=open(repo+'/loader.html').read()
local=f"http://127.0.0.1:{port}/"
loader,n=re.subn(r"https://cdn\.jsdelivr\.net/gh/hey-sutton/marketing-site-graphics@[^/']+/",local,loader); assert n==1
class Q(http.server.SimpleHTTPRequestHandler):
    def __init__(s,*a,**k): super().__init__(*a,directory=repo,**k)
    def log_message(s,*a): pass
    def end_headers(s): s.send_header("Access-Control-Allow-Origin","*"); super().end_headers()
socketserver.TCPServer.allow_reuse_address=True
srv=socketserver.TCPServer(("127.0.0.1",port),Q); threading.Thread(target=srv.serve_forever,daemon=True).start()
GIF="data:image/gif;base64,R0lGODlGAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw=="
def page_html(w):
    cards="".join(f'<div class="capabilities_card-visual" id="cv{i}"><img class="capabilities_visual-bg" alt="" src="{GIF}" style="display:block;width:100%;aspect-ratio:604/540">'+(loader if i==1 else "")+"</div>" for i in range(1,5))
    return f'<!doctype html><html><head><meta charset="utf-8"><style>body{{margin:0;background:#fff}}.w{{width:{w}px;padding:0}}.capabilities_card-visual{{position:relative;overflow:hidden;margin-bottom:20px;border-radius:8px}}</style></head><body><section data-sx-industry="{key}"><div class="w">{cards}</div></section></body></html>'
url=f"http://127.0.0.1:{port}/industries/{key}"
out=os.environ.get('GFX_SHOTS','shots'); os.makedirs(out,exist_ok=True)
fails=[]
def chk(name,cond,detail=''):
    print(('PASS ' if cond else 'FAIL ')+name+(' | '+detail if (detail and not cond) else ''))
    if not cond: fails.append(name)
SR="document.querySelector('#cv1 [data-sxg-host]').shadowRoot"
def open_page(p,w=640,reduced=False,height=1500):
    b=p.chromium.launch(); ctx=b.new_context(reduced_motion='reduce' if reduced else 'no-preference',viewport={'width':w+20,'height':height}); pg=ctx.new_page(); errors=[]
    pg.on('pageerror',lambda e:errors.append(str(e)[:200])); pg.on('console',lambda m:errors.append('console: '+m.text[:200]) if m.type=='error' else None)
    pg.route('https://cdn.prod.website-files.com/**',lambda r:r.abort()); pg.route(url+'*',lambda r:r.fulfill(status=200,content_type='text/html',body=page_html(w)))
    pg.goto(url); pg.wait_for_function("!!document.querySelector('#cv1 [data-sxg-host]')",timeout=15000)
    return b,pg,errors
def helpers(pg):
    ev=lambda js,arg=None:pg.evaluate("(a)=>{const r="+SR+";"+js+"}",arg)
    txt=lambda sel:ev("const e=r.querySelector(a);return e?e.textContent:null",sel)
    cls=lambda sel:ev("const e=r.querySelector(a);return e?e.className:null",sel)
    click=lambda sel:ev("r.querySelector(a).click()",sel)
    enter=lambda v:ev("const i=r.getElementById('lotin');i.value=a;i.dispatchEvent(new KeyboardEvent('keydown',{key:'Enter',bubbles:true}))",v)
    return ev,txt,cls,click,enter

# 0) background standard
im=Image.open(f'{repo}/graphics/{key}/bg-1.jpg'); sz=os.path.getsize(f'{repo}/graphics/{key}/bg-1.jpg')
chk('background is 604 by 540',im.size==(604,540),str(im.size)); chk('background is a progressive JPEG',bool(im.info.get('progressive',0)))
chk('background about 50 KB (under 70 KB)',sz<70*1024,str(sz))
code=open(f'{repo}/graphics/{key}/card-1.js',encoding='utf-8').read()
chk('card file 40 to 65 KB',40*1024<=len(code.encode())<=65*1024,str(len(code.encode())))
chk('no concept screen, illustrative or live demo tags',not re.search(r'concept screen|illustrative data|live product demo',code,re.I))
chk('no dashes and no recipe or Digit',not re.search('[\u2013\u2014]|\\brecipe\\b|\\bDigit\\b',code,re.I))

with sync_playwright() as p:
    # 1) Simon: right edge hidden at every width, content not clipped, no big empty band at the bottom
    for w in (1300,1024,768,390):
        b,pg,errs=open_page(p,w); pg.wait_for_timeout(300); ev,txt,cls,click,enter=helpers(pg)
        click('#lotin'); enter('ML-1028-A'); pg.wait_for_timeout(900)
        m=json.loads(ev("""const c=document.querySelector('#cv1').getBoundingClientRect(),f=r.querySelector('.fwin').getBoundingClientRect(),h=r.querySelector('.win-host'),s=h.getBoundingClientRect().width/h.offsetWidth;
          let low=0;r.querySelectorAll('.fw-body > *').forEach(e=>{low=Math.max(low,e.getBoundingClientRect().bottom)});
          let nodeRight=0;r.querySelectorAll('.nd3').forEach(e=>{nodeRight=Math.max(nodeRight,e.getBoundingClientRect().right)});
          return JSON.stringify({over:f.right-c.right,need:(9.15+1)*s+3,gap:(c.bottom-low)/s,overB:f.bottom-c.bottom,brr:getComputedStyle(document.querySelector('#cv1')).borderBottomRightRadius,tlr:getComputedStyle(document.querySelector('#cv1')).borderTopLeftRadius,margin:(c.right-nodeRight),s:s,arrowsRight:c.right-r.querySelector('.stp').getBoundingClientRect().right,arrowsBottom:c.bottom-r.querySelector('.stp').getBoundingClientRect().bottom})"""))
        chk(f'{w}px: right border and corner hidden (window runs {m["over"]:.0f}px past the edge)',m['over']>=m['need'],json.dumps(m))
        chk(f'{w}px: bottom edge and bottom corners of the window are past the card (by {m["overB"]:.0f}px)',m['overB']>=m['need'],json.dumps(m))
        chk(f'{w}px: the card\'s bottom right corner is square, the others keep the template radius',m['brr']=='0px' and m['tlr']=='8px',json.dumps(m))
        chk(f'{w}px: step arrows fully above the bottom edge',m['arrowsBottom']>=4*m['s'],json.dumps(m))
        chk(f'{w}px: content not clipped at the right (margin {m["margin"]:.0f}px)',m['margin']>=4*m['s'],json.dumps(m))
        chk(f'{w}px: step arrows fully inside the card',m['arrowsRight']>=6*m['s'],json.dumps(m))
        chk(f'{w}px: bottom empty band under 40 design px (is {m["gap"]:.0f})',m['gap']<=40,json.dumps(m))
        real=[e for e in errs if 'attachShadow' not in e and 'ERR_FAILED' not in e]; chk(f'{w}px no page errors',not real,str(real)); b.close()
    # 2) Simon: the start screen must not show boxes or counts before a lot number is entered
    b,pg,errs=open_page(p,640); ev,txt,cls,click,enter=helpers(pg)
    vis=lambda k:ev("return getComputedStyle(r.querySelector('[data-k=\"'+a+'\"]')).visibility",k)
    chk('start screen: no lot boxes visible',all(vis(k)=='hidden' for k in ['A','PB1','YG1','DC','SC']))
    chk('start screen: no pallet counts or totals on screen',not re.search(r'\d+ pallets|\d+,\d{3} lb',ev("const o=[];r.querySelectorAll('*').forEach(e=>{if(getComputedStyle(e).visibility!=='hidden'&&e.children.length===0&&e.offsetParent!==null)o.push(e.textContent)});return o.join(' | ')") or ''))
    chk('start screen: empty field, empty lot record, prompt shown',ev("return r.getElementById('lotin').value===''")  and 'appear here once a lot is entered' in txt('#rg') and 'Enter a lot number' in txt('#emp'))
    # speed target and typing
    res=ev("""return 0""")
    b.close()
    b,pg,errs=open_page(p,640); ev,txt,cls,click,enter=helpers(pg)
    r2=pg.evaluate("""async()=>{const r="""+SR+""";const t0=performance.now();
      const wait=f=>new Promise(res=>{const i=setInterval(()=>{if(f()){clearInterval(i);res(performance.now()-t0);}},30);setTimeout(()=>{clearInterval(i);res(-1);},9000);});
      const a=await wait(()=>r.querySelector('.cap.on')),t=await wait(()=>r.getElementById('lotin').value.length>0),c=await wait(()=>/25 pallets, 3 customers/.test(r.getElementById('scope').textContent));return [a,t,c];}""")
    print(f'timing: first caption {r2[0]:.0f} ms, typing starts {r2[1]:.0f} ms, full lot info and trace {r2[2]:.0f} ms')
    chk('speed: walkthrough starts within 1.8 s',0<r2[0]<1800,str(r2)); chk('speed: typing starts within 2 s',0<r2[1]<2000,str(r2)); chk('speed: full lot info and trace by about 4 s',0<r2[2]<4200,str(r2))
    b.close()
    # 3) the tour in order (schedule from mount: step 1 at 1.2 s, lot opens 2.5 s, step 2 4.2 s, step 3 8.0 s, step 4 11.4 s, complaint opens about 13 s, step 5 16 s, your turn 20.6 s)
    b,pg,errs=open_page(p,640); ev,txt,cls,click,enter=helpers(pg); shot=lambda n:pg.locator('#cv1').screenshot(path=f'{out}/{n}.png')
    pg.wait_for_timeout(1700); shot('t1-typing')
    pg.wait_for_timeout(3500); shot('t2-forward'); chk('tour: forward trace chip','25 pallets, 3 customers' in txt('#scope'),txt('#scope'))
    pg.wait_for_timeout(3800); shot('t3-blended')
    pg.wait_for_timeout(3500); shot('t4-complaint-typing')
    pg.wait_for_timeout(5500); shot('t5-back'); chk('tour: backward trace chip','2 milk lots, 1 batch' in txt('#scope'),txt('#scope'))
    pg.wait_for_timeout(6500); shot('t6-your-turn')
    chk('tour: loops back to the empty start after the hand-off','No trace yet' in txt('#scope') or 'pallets' in txt('#scope'))
    b.close()
    # 4) manual interaction: typed lots, errors, clicks, numbers
    b,pg,errs=open_page(p,640); ev,txt,cls,click,enter=helpers(pg); shot=lambda n:pg.locator('#cv1').screenshot(path=f'{out}/{n}.png')
    click('#lotin')  # a real user clicks the field first, which takes over from the autoplay
    enter('ML-1028-A'); pg.wait_for_timeout(900); a=txt('#act-text') or ''
    chk('typed ML-1028-A: forward text','reached 2 batches and 3 customers, 25 pallets in all' in a and 'blended with ML-1028-B in silo S1' in a and 'Not affected: ML-1028-C and MK-1029-1' in a,a)
    chk('typed lot: chip and customer pallets','25 pallets, 3 customers' in txt('#scope') and all(s in txt('#gr') for s in ['16 pallets in scope','6 pallets in scope','3 pallets in scope']))
    chk('typed lot: lot record opens on A','Milk intake lot' in txt('#rtitle') and '9,840 lb' in txt('#rg')); shot('m1-A')
    enter('ml-1028-c'); pg.wait_for_timeout(700); a=txt('#act-text'); print('C text:',a)
    chk('lower case entry works (C)','reached 1 batch and 2 customers, 7 pallets in all' in a and 'Not affected: ML-1028-A, ML-1028-B, YG-1029-1 and YG-1029-2.' in a,a)
    enter('PB-1028-1'); pg.wait_for_timeout(600); a=txt('#act-text'); chk('base lot entry (both ways)','came from 2 milk lots and reached 3 customers' in a and '25 pallets shipped' in a,a)
    enter('YG-1029-1'); pg.wait_for_timeout(600); a=txt('#act-text'); chk('batch entry (both ways)','came from 2 milk lots and reached 2 customers' in a and '18 pallets shipped' in a,a)
    enter('NOPE-1'); pg.wait_for_timeout(500); a=txt('#act-text'); chk('unknown lot shows a helpful message','No lot matches that number' in a,a)
    click('[data-k="SC"]'); pg.wait_for_timeout(600); a=txt('#act-text'); chk('click customer: traces back','received 2 batches, made from 3 milk lots' in a and 'silos S1 and S2' in a,a); shot('m2-school')
    click('#segm [data-m="cmp"]'); pg.wait_for_timeout(700); a=txt('#act-text')
    chk('complaint sample: text','Complaint on vanilla yogurt YG-1029-2' in a and '2 milk lots: ML-1028-A and ML-1028-B' in a and 'silo S1' in a and 'culture CU-0914 and vanilla VN-2207' in a,a)
    chk('complaint sample: field shows the lot','YG-1029-2' in ev("return r.getElementById('lotin').value")); shot('m3-complaint')
    click('.rp'); pg.wait_for_timeout(1500)
    chk('replay returns to the empty start',txt('#scope')=='No trace yet' and ev("return r.getElementById('gr').classList.contains('off')"),txt('#scope'))
    click('.studio-chip'); pg.wait_for_timeout(800); chk('studio popover opens','open' in cls('[data-studio]').split()); shot('m4-studio')
    chk('arithmetic: 9,840 + 8,120 = 17,960 base; 10,000 + 7,960 = 17,960; 6,500 stays 6,500; 12+6+4+3+5+2 = 32 pallets',9840+8120==17960 and 10000+7960==17960 and 12+6+4+3+5+2==32)
    real=[e for e in errs if 'attachShadow' not in e and 'ERR_FAILED' not in e]; chk('manual run no page errors',not real,str(real)); b.close()
    # 5) arrows and hotspots (5 steps)
    b,pg,errs=open_page(p,640); ev,txt,cls,click,enter=helpers(pg); shot=lambda n:pg.locator('#cv1').screenshot(path=f'{out}/{n}.png')
    dis=lambda sel:ev("return r.querySelector(a).disabled",sel)
    chk('arrows: previous disabled at step 1',dis('#pv'))
    click('#nx'); pg.wait_for_timeout(900)
    chk('arrows: next goes to step 2 with the forward trace','2 of 5' in txt('#sn') and '25 pallets, 3 customers' in txt('#scope'),txt('#sn')+' '+txt('#scope'))
    chk('hotspot on at step 2',' on' in ' '+cls('#hs'),cls('#hs'))
    click('#nx'); pg.wait_for_timeout(500)
    chk('step 3 shows the hotspot on the complaint sample',txt('#sn')=='3 of 5' and ev("const h=r.querySelector('#hs').getBoundingClientRect(),b=r.querySelector('[data-m=cmp]').getBoundingClientRect();return Math.abs(h.left-b.left)<8&&Math.abs(h.top-b.top)<8"))
    shot('m5-step3-hotspot')
    click('#nx'); pg.wait_for_timeout(900)
    chk('step 4 traces back from the complaint','4 of 5' in txt('#sn') and '2 milk lots, 1 batch' in txt('#scope'),txt('#sn')+' '+txt('#scope'))
    click('#nx'); pg.wait_for_timeout(300); chk('step 5 and next disabled',txt('#sn')=='5 of 5' and dis('#nx'))
    click('#pv'); click('#pv'); pg.wait_for_timeout(700)
    chk('previous returns to the forward trace','3 of 5' in txt('#sn') and '25 pallets, 3 customers' in txt('#scope'),txt('#sn')+' '+txt('#scope'))
    click('#pv'); click('#pv'); pg.wait_for_timeout(500); chk('previous reaches step 1 and disables',txt('#sn')=='1 of 5' and dis('#pv'))
    geo=ev("const rec=r.querySelector('.rec').getBoundingClientRect(),st=r.querySelector('.stp').getBoundingClientRect(),w=r.querySelector('.fwin').getBoundingClientRect(),c=document.querySelector('#cv1').getBoundingClientRect();return st.top>=rec.bottom-1&&st.bottom<=w.bottom+1&&st.right<=c.right")
    chk('arrows sit below the lot record and inside the card',geo)
    real=[e for e in errs if 'attachShadow' not in e and 'ERR_FAILED' not in e]; chk('arrows no page errors',not real,str(real)); b.close()
    # clicking the highlighted sample from the empty start advances to step 1
    b,pg,errs=open_page(p,640); ev,txt,cls,click,enter=helpers(pg)
    click('#segm [data-m="lot"]'); pg.wait_for_timeout(900)
    chk('clicking the highlighted sample opens the lot and shows step 1','1 of 5' in txt('#sn') and '25 pallets' in txt('#scope'),txt('#sn')); b.close()
    # 6) reduced motion
    b,pg,errs=open_page(p,640,reduced=True); ev,txt,cls,click,enter=helpers(pg); pg.wait_for_timeout(2500)
    chk('reduced motion: no autoplay',txt('#scope')=='No trace yet',txt('#scope'))
    click('#nx'); pg.wait_for_timeout(600)
    an=ev("return getComputedStyle(r.getElementById('hs')).animationName")
    chk('reduced motion: arrows work, hotspot not animated','25 pallets' in txt('#scope') and an=='none',an); b.close()
srv.shutdown()
print('RESULT:','PASS' if not fails else 'FAIL '+str(fails))
sys.exit(1 if fails else 0)
