#!/usr/bin/env python3
"""
Build a self-contained HTML preview of one graphic card, so the user can see and click it before anything is released.

Usage:
  python3 make_preview_page.py --card graphics/dairy/card-1.js --bg graphics/dairy/bg-1.jpg --out preview.html --title "Dairy card 1: Milk Lot Traceability"
  Several cards: --card card-1.js card-2.js card-3.js card-4.js --bg bg-1.jpg bg-2.jpg bg-3.jpg bg-4.jpg  (shown in a grid, one source box per card)

The page runs the real card file (the background is embedded so nothing is fetched), has a desktop and phone width switch,
and shows the JavaScript underneath. Publish the result as an artifact (see SKILL.md, Step 5).
"""
import argparse, base64, html, os, re
ap = argparse.ArgumentParser()
ap.add_argument("--card", required=True, nargs="+"); ap.add_argument("--bg", required=True, nargs="+")
ap.add_argument("--out", required=True); ap.add_argument("--title", default="Graphic preview")
a = ap.parse_args()
assert len(a.card) == len(a.bg), "give one --bg per --card"
codes = []; bgs = []
for cf, bf in zip(a.card, a.bg):
    with open(cf, encoding="utf-8") as f: code = f.read()
    assert "</script" not in code.lower()
    assert re.search(r"var BGU=SRC\?new URL\('[^']+',SRC\)\.href:'';", code), "BGU line not found, the card must use the repo hosted background pattern"
    with open(bf, "rb") as f: bgs.append(base64.b64encode(f.read()).decode())
    codes.append(code)
T = html.escape(a.title)
GIF = "data:image/gif;base64,R0lGODlGAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw=="
stages = "".join('<div class="stage"><div class="capabilities_card-visual" id="cv%d"><img class="capabilities_visual-bg" alt="" src="%s" style="display:block;width:100%%;aspect-ratio:604/540"></div></div>' % (i, GIF) for i in range(len(codes)))
srcs = "".join('<details><summary>View the JavaScript for %s (%s KB)</summary><pre id="srcview%d"></pre></details>' % (html.escape(os.path.basename(cf)), round(len(c.encode()) / 1024, 1), i) for i, (cf, c) in enumerate(zip(a.card, codes)))
blobs = "".join('<script type="text/plain" id="card-src%d">%s</script><script type="text/plain" id="card-bg%d">data:image/jpeg;base64,%s</script>' % (i, c, i, b) for i, (c, b) in enumerate(zip(codes, bgs)))
page = r"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover"><title>@T@</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
<style>
:root{color-scheme:light;--bg:#F6F6F4;--ink:#1B1B1A;--mut:#5E5E59;--line:#DDDDD8;--panel:#FFFFFF;--btn:#1B1B1A;--btnink:#FFFFFF;box-sizing:border-box;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){color-scheme:dark;--bg:#161615;--ink:#F1F1EE;--mut:#A4A49D;--line:#35352F;--panel:#1F1F1D;--btn:#F1F1EE;--btnink:#161615}}
:root[data-theme="dark"]{color-scheme:dark;--bg:#161615;--ink:#F1F1EE;--mut:#A4A49D;--line:#35352F;--panel:#1F1F1D;--btn:#F1F1EE;--btnink:#161615}
html{scroll-padding-top:env(safe-area-inset-top,0px)}body{margin:0;background:var(--bg);color:var(--ink);font:16px/1.5 Inter,ui-sans-serif,system-ui,sans-serif}
main{max-width:1300px;margin:0 auto;padding:36px 20px 64px}h1{font-size:26px;line-height:1.2;font-weight:600;margin:0 0 6px}.sub{margin:0 0 24px;color:var(--mut);max-width:70ch}
.bar{display:flex;gap:8px;align-items:center;margin:0 0 14px;flex-wrap:wrap}.bar span{color:var(--mut);font-size:14px;margin-right:4px}
.bar button{font:inherit;font-size:14px;font-weight:500;padding:6px 12px;border:1px solid var(--line);border-radius:8px;background:var(--panel);color:var(--ink);cursor:pointer}
.bar button[aria-pressed="true"]{background:var(--btn);color:var(--btnink);border-color:var(--btn)}.bar button:focus-visible{outline:2px solid var(--ink);outline-offset:2px}
#grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(min(100%,604px),604px));gap:24px;align-items:start}
.stage{width:604px;max-width:100%;transition:width .3s ease}#grid.phone .stage{width:340px}#grid.phone{grid-template-columns:repeat(auto-fill,340px)}
.capabilities_card-visual{position:relative;overflow:hidden;border-radius:8px}
details{margin-top:14px;border:1px solid var(--line);border-radius:10px;background:var(--panel);max-width:760px}summary{cursor:pointer;padding:12px 16px;font-weight:500}
pre{margin:0;padding:14px 16px;max-height:420px;overflow:auto;border-top:1px solid var(--line);font:12px/1.5 "JetBrains Mono",ui-monospace,monospace;white-space:pre}
@media (prefers-reduced-motion:reduce){.stage{transition:none}}
</style></head><body><main><h1>@T@</h1>
<p class="sub">Live copies of the card files. Each runs its own walkthrough when it scrolls into view, so wait a few seconds or click a card to take over. Use Replay to restart one.</p>
<div class="bar" role="group" aria-label="Preview width"><span>Width</span><button type="button" id="wd" aria-pressed="true">Desktop card</button><button type="button" id="wp" aria-pressed="false">Phone card</button></div>
<div id="grid">@STAGES@</div>@SRCS@</main>@BLOBS@
<script>(function(){var n=@N@;for(var i=0;i<n;i++){(function(i){var code=document.getElementById('card-src'+i).textContent;document.getElementById('srcview'+i).textContent=code;
var bg=document.getElementById('card-bg'+i).textContent.trim();var run=code.replace(/var BGU=SRC\?new URL\('[^']+',SRC\)\.href:'';/,'var BGU='+JSON.stringify(bg)+';');
var s=document.createElement('script');s.textContent=run;s.sxCard=document.getElementById('cv'+i);document.head.appendChild(s);})(i);}
var g=document.getElementById('grid'),wd=document.getElementById('wd'),wp=document.getElementById('wp');
function set(p){g.classList.toggle('phone',p);wd.setAttribute('aria-pressed',p?'false':'true');wp.setAttribute('aria-pressed',p?'true':'false');}
wd.addEventListener('click',function(){set(false);});wp.addEventListener('click',function(){set(true);});})();</script></body></html>"""
page = page.replace("@T@", T).replace("@STAGES@", stages).replace("@SRCS@", srcs).replace("@BLOBS@", blobs).replace("@N@", str(len(codes)))
with open(a.out, "w", encoding="utf-8") as f: f.write(page)
print("wrote", a.out, round(len(page.encode()) / 1024), "KB,", len(codes), "card(s)")
