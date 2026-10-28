#!/usr/bin/env python3
"""
Local test harness for Sutton industry page graphics.

Serves a checkout of the marketing-site-graphics repo, builds a stub industry page with
four spotlight cards, mounts the real loader.html against the local files, and reports
per card: did it mount, how big is it, and any page errors. Saves one screenshot per card.

Usage:
  python3 test_graphics.py --repo /path/to/marketing-site-graphics --key food-beverage --out /tmp/gfx
Needs: pip install playwright (and `playwright install chromium`).
Tip: git clone https://github.com/hey-sutton/marketing-site-graphics  (or download the files from raw.githubusercontent.com)
"""
import argparse, json, os, re, sys, threading, http.server, socketserver
from playwright.sync_api import sync_playwright

ap = argparse.ArgumentParser()
ap.add_argument("--repo", required=True, help="path to the repo checkout")
ap.add_argument("--key", required=True, help="graphic key, e.g. food-beverage")
ap.add_argument("--out", default="/tmp/gfx_test", help="folder for screenshots")
ap.add_argument("--port", type=int, default=8791)
ap.add_argument("--slug", default=None, help="the industry's CMS slug, to warn when the key differs from it")
a = ap.parse_args()

repo = os.path.abspath(a.repo)
os.makedirs(a.out, exist_ok=True)
manifest = json.load(open(os.path.join(repo, "manifest.json")))
cards = manifest.get("graphics", {}).get(a.key)
if not cards:
    sys.exit(f"FAIL: key '{a.key}' is not in manifest.json ({list(manifest.get('graphics', {}))})")
def fname(n): return "hero.js" if n == "hero" else f"card-{n}.js"
nums = [n for n in cards if n != "hero"]
missing = [n for n in cards if not os.path.exists(os.path.join(repo, "graphics", a.key, fname(n)))]
if missing:
    sys.exit(f"FAIL: missing files for cards {missing}")

loader = open(os.path.join(repo, "loader.html"), encoding="utf-8").read()
warnings = []
m = re.search(r"marketing-site-graphics@(v[0-9.]+)/", loader)
if m and m.group(1) != "v" + str(manifest.get("version")):
    warnings.append(f"loader.html BASE is {m.group(1)} but manifest.json version is {manifest.get('version')}. Bump both together when cutting a release.")
if a.slug and a.slug != a.key:
    warnings.append(f"graphic key {a.key!r} differs from the CMS slug {a.slug!r}. Set the CMS Graphic Key to the key explicitly, or the loader (which falls back to the slug) will find nothing.")
legacy, bgfiles = [], {}
for n in cards:
    src = open(os.path.join(repo, "graphics", a.key, fname(n)), encoding="utf-8", errors="ignore").read()
    if "website-files.com" in src and re.search(r"\.(avif|png|jpg|webp)", src):
        legacy.append(n)
    mm = re.search(r"new URL\('((?:bg-\d|hero-bg)\.jpg)'", src)
    bgfiles[n] = mm.group(1) if mm else None
    if bgfiles[n] and not os.path.exists(os.path.join(repo, "graphics", a.key, bgfiles[n])):
        warnings.append(f"card {n} references {bgfiles[n]} but that file is not in the folder.")
if legacy:
    warnings.append(f"cards {legacy} still load a background from Webflow (legacy). The standard is a repo hosted bg-N.jpg in the folder, resolved from the script address.")
for n in cards:
    if bgfiles[n] is None and n not in legacy:
        warnings.append(f"card {n} has no recognizable background reference.")
local = f"http://127.0.0.1:{a.port}/"
loader, n = re.subn(r"https://cdn\.jsdelivr\.net/gh/hey-sutton/marketing-site-graphics@[^/']+/", local, loader)
if n != 1:
    sys.exit(f"FAIL: expected one BASE url in loader.html, found {n}")

class Q(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kw): super().__init__(*args, directory=repo, **kw)
    def log_message(self, *a): pass
    def end_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*"); super().end_headers()
socketserver.TCPServer.allow_reuse_address = True
srv = socketserver.TCPServer(("127.0.0.1", a.port), Q)
threading.Thread(target=srv.serve_forever, daemon=True).start()

GIF = "data:image/gif;base64,R0lGODlGAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw=="
html_cards = "".join(
    f'<div class="capabilities_card-visual" id="cv{i}"><img class="capabilities_visual-bg" alt="" src="{GIF}" '
    f'style="display:block;width:100%;aspect-ratio:604/540">' + (loader if i == 1 else "") + "</div>"
    for i in range(1, max(nums + [4]) + 1))
if "hero" in cards:
    html_cards = f'<div class="feature-hero_visual" id="cvhero" style="position:relative;overflow:hidden;width:640px;height:590px;margin-bottom:20px"></div>' + html_cards
page = (f'<!doctype html><html><head><meta charset="utf-8"><style>body{{margin:0;background:#fff}}'
        f'.w{{width:640px;padding:20px}}.capabilities_card-visual{{position:relative;overflow:hidden;margin-bottom:20px}}</style></head>'
        f'<body><section data-sx-industry="{a.key}"><div class="w">{html_cards}</div></section></body></html>')

url = f"http://127.0.0.1:{a.port}/industries/{a.key}"  # same origin as the files, avoids CORS and private network blocks
ok_all = True
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": 700, "height": 3000})
    errors = []
    bg_status = {}
    pg.on("response", lambda r: bg_status.__setitem__(r.url.split("/")[-1], r.status) if re.search(r"/(bg-\d|hero-bg)\.jpg", r.url) else None)
    pg.on("pageerror", lambda e: errors.append(str(e)[:200]))
    pg.on("console", lambda m: errors.append("console: " + m.text[:200]) if m.type == "error" else None)
    pg.route("https://cdn.prod.website-files.com/**", lambda r: r.abort())  # backgrounds are not needed for the test
    pg.route(url + "*", lambda r: r.fulfill(status=200, content_type="text/html", body=page))
    pg.goto(url + "?sxgdebug=0")
    mounted = {}
    for i in cards:
        try:
            pg.wait_for_function(
                "i=>{const c=document.getElementById('cv'+i);return !![...c.querySelectorAll('*')].find(e=>e.shadowRoot)}",
                arg=i, timeout=15000)
            mounted[i] = True
        except Exception:
            mounted[i] = False
    pg.wait_for_timeout(1200)
    print(f"Graphic key: {a.key} | cards in manifest: {cards}")
    for i in cards:
        size = pg.evaluate("i=>{const c=document.getElementById('cv'+i);return Math.round(c.offsetWidth)+'x'+Math.round(c.offsetHeight)}", i)
        shot = os.path.join(a.out, f"{a.key}-card-{i}.png")
        pg.locator(f"#cv{i}").screenshot(path=shot)
        print(f"  card {i}: {'mounted' if mounted[i] else 'DID NOT MOUNT'} | card size {size} | screenshot {shot}")
        ok_all = ok_all and mounted[i]
    for n in cards:
        f = bgfiles[n]
        if f:
            st = bg_status.get(f)
            ok = (st == 200)
            print(f"  card {n} background {f}: {'loaded (200)' if ok else 'NOT LOADED, status ' + str(st)}")
            ok_all = ok_all and ok
        elif n in legacy:
            print(f"  card {n} background: Webflow hosted (legacy)")
    real = [e for e in errors if "attachShadow" not in e and "net::ERR_FAILED" not in e]
    print("  page errors:", real or "none")
    ok_all = ok_all and not real
    b.close()
srv.shutdown()
for w in warnings: print("  WARNING:", w)
print("RESULT:", "PASS" if ok_all else "FAIL", "(with warnings)" if ok_all and warnings else "")
sys.exit(0 if ok_all else 1)
