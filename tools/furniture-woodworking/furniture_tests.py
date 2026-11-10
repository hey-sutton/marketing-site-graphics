"""Furniture and woodworking test setup.

Points the shared harness (tools/electronics/testlib.py) at graphics/furniture-woodworking and reuses the Recycling checks
for the app shell and the phone layout (tools/recycling/recycling_tests.py): layout at 1300, 1024, 768 and 390 px, the
phone stage under 520 px, the navigation walk at 1300, 480 and 390 px, and the variety rules on each card's STORY.

Two changes for these cards:
  * a step can need more than one click (card 3, step 3: White oak, then 72 in, then Matte lacquer). Every Try it click in
    the harness goes through adv(), which clicks the pulsing target until the step moves on.
  * variety: the brief puts "Create sales order" at step 5 of 8 on card 3, so the "primary button only in the last three
    steps" rule is reported but not failed. Every other variety rule still applies.
Text scan adds the brief's banned words: market size words, concept and illustrative tags, CAD product names.
"""
import importlib, inspect, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
TOOLS = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(TOOLS, 'electronics'))
sys.path.insert(0, os.path.join(TOOLS, 'recycling'))
sys.path.insert(0, HERE)
import testlib  # noqa: E402
testlib.KEY = 'furniture-woodworking'
testlib.SHOTS = os.environ.get('GFX_SHOTS', '/tmp/furniture_shots')
os.makedirs(testlib.SHOTS, exist_ok=True)
import recycling_tests as rt  # noqa: E402  (installs the phone aware layout_checks on testlib)
sys.path.insert(0, HERE)   # recycling_tests puts its own folder first; our card modules must win
for _m in ('card1', 'card2', 'card3', 'card4'):
    sys.modules.pop(_m, None)
import variety_check  # noqa: E402
from playwright.sync_api import sync_playwright  # noqa: E402

testlib.KEY = 'furniture-woodworking'
testlib.SHOTS = os.environ.get('GFX_SHOTS', '/tmp/furniture_shots')
testlib.EXTRA_CLAIMS = re.compile(
    r'(?i:\bsmall\b|mid-size|midsize|\benterprise\b|\blarge\b|\bSMB\b|startup|concept screen|live product demo|illustrative|\brecipe|compliance|compliant|certified)'
    r'|SketchUp|AutoCAD|Cabinet Vision|Mozaik|Microvellum|KCD|SolidWorks|Fusion 360|Digit')
js, pill = testlib.js, testlib.pill
# the template's loader makes the card shorter at 1440 px and wider; the test page does the same
testlib.PAGE = testlib.PAGE.replace('.capabilities_visual-bg{', '@media (min-width:1440px){.capabilities_card-visual{aspect-ratio:604/523}}.capabilities_visual-bg{', 1)
# a page that sets text styles the card must not inherit (Webflow sites often set these on body)
HOSTILE = 'body{letter-spacing:.06em;word-spacing:3px;font-size:19px;line-height:1.9;text-transform:uppercase;font-family:Georgia,serif}'


def adv(pg):
    """Click the pulsing target until the step moves on (most steps take one click)."""
    before = pill(pg)
    for _ in range(4):
        pg.locator('#cv .hint').first.click()
        pg.wait_for_timeout(350)
        if pill(pg) != before or not pg.locator('#cv .hint').count():
            return
        pg.wait_for_timeout(250)


def _patch(fn, names):
    src = inspect.getsource(fn)
    for a in ("pg.locator('#cv .hint').first.click()", 'hints.first.click()'):
        src = src.replace(a, 'adv(pg)')
    ns = dict(vars(sys.modules[fn.__module__]))
    ns['adv'] = adv
    ns.update(names)
    exec(compile(src, fn.__code__.co_filename, 'exec'), ns)
    return ns[fn.__name__]


run_card = _patch(testlib.run_card, {})
testlib.run_card = run_card


def variety(n, f):
    m = importlib.import_module('card%d' % n)
    head = ['#', 'screen', 'target type', 'position']
    rows = [[str(i + 1), s, t, p] for i, (s, _, t, p) in enumerate(m.STORY)]
    probs = variety_check.check('card %d' % n, head, rows)
    soft = [p for p in probs if 'before the last 3 steps' in p]
    hard = [p for p in probs if p not in soft]
    f.check(not hard, 'variety: %d steps, %d screens, %d target types, %d positions %s' % (
        len(rows), len({r[1] for r in rows}), len({r[2] for r in rows}), len({r[3] for r in rows}), hard or ''))
    if soft:
        print('  note ' + '; '.join(soft) + ' (kept, the brief orders the steps this way)')
    f.check(len(m.STORY) == m.STEPS, 'variety: the storyboard has one row per step')
    return m.STORY


nav_walk = _patch(rt.nav_walk, {'state': rt.state, 'testlib': testlib, 'js': js})


def typed(n, f, prep_steps, field, value, want_scr, want_js=None):
    """Real typing: Try it, do the steps before the field, type the value and press Enter."""
    with sync_playwright() as p:
        b = testlib.browser(p)
        pg, errs = testlib.open_card(b, n, 1300)
        pg.locator('#cv').scroll_into_view_if_needed()
        pg.locator('#cv .mtg [data-m="try"]').click()
        for _ in range(prep_steps):
            pg.wait_for_timeout(1600)
            adv(pg)
        pg.wait_for_timeout(1600)
        inp = pg.locator('#cv #' + field)
        inp.click()
        inp.fill(value)
        inp.press('Enter')
        pg.wait_for_timeout(700)
        f.check(js(pg, "return r.querySelector('.fwin').getAttribute('data-scr')") == want_scr, 'typing %s and Enter loads "%s"' % (value, want_scr))
        if want_js:
            f.check(js(pg, want_js), 'typing: %s' % want_js)
        f.check(not errs, 'typing: no page errors %s' % errs[:2])
        b.close()


def start_rule(pg, f, banned):
    t = js(pg, "return r.getElementById('pg').innerText")
    for s in banned:
        f.check(s not in t, 'start: "%s" is not on the start screen' % s)


def wide(n, f):
    """At 1500 px (card aspect 604/523) on a page with hostile text styles: walk every step and check the step arrows
    stay inside the card and no row pushes a column out of its own box."""
    page = testlib.PAGE
    testlib.PAGE = page.replace('</style>', HOSTILE + '</style>', 1)
    try:
        with sync_playwright() as p:
            b = testlib.browser(p)
            pg, errs = testlib.open_card(b, n, 1500)
            pg.locator('#cv').scroll_into_view_if_needed()
            pg.locator('#cv .mtg [data-m="try"]').click()
            k, bad_stp, bad_rows = 0, [], []
            while True:
                pg.wait_for_timeout(1500)
                d = js(pg, '''var cv=document.getElementById('cv').getBoundingClientRect(),s=r.querySelector('.stp').getBoundingClientRect(),bad=[];
r.querySelectorAll('#pg .row').forEach(function(row){var b=row.getBoundingClientRect();if(b.height<2)return;var kids=[].filter.call(row.children,function(c){return c.getBoundingClientRect().width>0;}),why='';kids.forEach(function(c,i){var x=c.getBoundingClientRect();if(x.right>b.right+1||x.left<b.left-1)why='outside';if(c.scrollWidth>c.clientWidth+1&&getComputedStyle(c).overflow==='hidden')why='clipped';var nx=kids[i+1];if(nx&&nx.getBoundingClientRect().left<x.right-1)why='overlap';});if(why)bad.push(why+' '+(row.id||row.textContent).slice(0,30));});
return {stp:s.bottom<=cv.bottom-2&&s.top>=cv.top,bad:bad,up:getComputedStyle(r.querySelector('.tbar .mode')).textTransform};''')
                if d['up'] != 'none':
                    bad_rows.append('step %d: the top bar inherits text-transform %s' % (k, d['up']))
                if not d['stp']:
                    bad_stp.append(k)
                bad_rows += ['step %d: %s' % (k, x) for x in d['bad']]
                testlib.shot(pg, 'card%d_1500_%d.png' % (n, k))
                if not pg.locator('#cv .hint').count():
                    break
                adv(pg)
                k += 1
            f.check(not bad_stp, '1500 px: step arrows inside the card at every step %s' % bad_stp)
            f.check(not bad_rows, '1500 px with page text styles: no column pushed out, overlapping or clipped %s' % bad_rows[:3])
            f.check(not errs, '1500 px: no page errors %s' % errs[:2])
            b.close()
    finally:
        testlib.PAGE = page


def run_all(n, plan, numbers, extra=None, more=None):
    f = run_card(n, plan, numbers, extra=extra)
    story = variety(n, f)
    nav_walk(n, story, f, 1300, 604, 'desktop')
    nav_walk(n, story, f, 390, 358, 'phone 390')
    nav_walk(n, story, f, 1024, 480, 'phone 480')
    wide(n, f)
    if more:
        more(f)
    return f
