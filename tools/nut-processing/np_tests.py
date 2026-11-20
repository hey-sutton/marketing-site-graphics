"""Nut processing test setup: the Automotive harness (tools/automotive/auto_tests.py) pointed at
graphics/nut-processing, with this page's rules added.

Read only demos (the page README, November 2026): every input is prefilled and read only, nothing is typed, there are
no sample buttons and no error messages, and the reader only clicks. So:
  * readonly_checks() fails if any editable input, textarea or contenteditable exists, and checks every input holds
    its prefilled value, is readonly, has tabindex -1, a gray background and no pointer events.
  * Some steps take more than one click: none on the nut processing cards. Every click before the last carries data-pick. click_step() keeps
    clicking the pulsing target while it carries data-pick, then clicks the last one. The harness's
    run_card is reused with its two "click the hint once" lines swapped for click_step (asserted below), so every
    other check stays exactly as the other industries run it.
Banned words: the Automotive list plus claim words (FDA, FSMA, SOC 2, ISO, SQF, HACCP, certified, validated, audit
ready), "recipe", "native", "API", size words, concept tags, and real nut brand, grower, processor, grocer and carrier names."""
import inspect, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(HERE), 'automotive'))
import auto_tests  # noqa: E402
from auto_tests import finish, js, pill, testlib  # noqa: E402,F401
from playwright.sync_api import sync_playwright  # noqa: E402

testlib.KEY = 'nut-processing'
testlib.SHOTS = os.environ.get('GFX_SHOTS', '/tmp/np_shots')
os.makedirs(testlib.SHOTS, exist_ok=True)
testlib.EXTRA_CLAIMS = re.compile(
    testlib.EXTRA_CLAIMS.pattern
    + r'|(?i:\bvalidat\w*|\bFSMA\b|\bSOC ?2\b|\bISO\b|\bSQF\b|\bHACCP\b|audit ready|\brecipe|\bnative\b|\bAPI\b|built with studio|\bmid\b|concept)'
    + r'|\b(?:Blue Diamond|Wonderful|Planters|Diamond of California|Fisher|Kirkland|Olam|Hormel|Mauna Loa|Sun-Maid|Sunsweet|Sanfilippo|Setton|Paramount|Harris Woolf|Select Harvests|Walmart|Costco|Kroger|Target|Whole Foods|Trader Joe|Amazon|Sysco|UNFI|KeHE|Sprouts|Publix|Albertsons|Safeway|Wegmans|Aldi|UPS|FedEx|USPS|DHL)\b')


def click_step(pg):
    """Click the pulsing target, and keep going while it carries data-pick (the prompt moves on to the next click)."""
    for _ in range(4):
        h = pg.locator('#cv .hint').first
        pick = h.get_attribute('data-pick') is not None
        h.click()
        if not pick:
            return
        pg.wait_for_timeout(350)


_src = inspect.getsource(auto_tests.run_card)
assert _src.count('hints.first.click()') == 1 and _src.count("pg.locator('#cv .hint').first.click()") == 1
_src = _src.replace('hints.first.click()', 'click_step(pg)').replace("pg.locator('#cv .hint').first.click()", 'click_step(pg)')
_ns = dict(vars(auto_tests))
_ns['click_step'] = click_step
exec(compile(_src, auto_tests.__file__, 'exec'), _ns)
run_card = _ns['run_card']

RO = '''return [].map.call(r.querySelectorAll('.fwin input'),function(i){var cs=getComputedStyle(i);
return [i.id,i.value,i.readOnly,i.getAttribute('tabindex'),cs.pointerEvents,cs.backgroundColor].join('|');});'''
EDIT = "return r.querySelectorAll('input:not([readonly]),textarea,select,[contenteditable]:not([contenteditable=\"false\"])').length"


def readonly_checks(pg, f, want, when):
    """want: {input id: prefilled value}. Every input is prefilled, read only, out of the tab order, gray, no pointer events."""
    f.check(js(pg, EDIT) == 0, '%s: no editable input, textarea or contenteditable' % when)
    got = {}
    for row in js(pg, RO):
        i, v, ro, ti, pe, bg = row.split('|')
        got[i] = v
        f.check(ro == 'true' and ti == '-1' and pe == 'none' and bg not in ('rgb(255, 255, 255)', 'rgba(0, 0, 0, 0)'), '%s: input %s is read only, tabindex -1, no pointer events, gray (%s %s %s %s)' % (when, i, ro, ti, pe, bg))
    f.check(got == want, '%s: inputs hold their prefilled values %s' % (when, got))
    f.check(js(pg, "return r.querySelectorAll('[data-sample],.em').length") == 0, '%s: no sample buttons and no error lines' % when)


def ids(pg, *names):
    return js(pg, "return %r.map(function(i){var e=r.getElementById(i);return e?e.textContent:null}).join('|')" % list(names))


def keyboard_walk(f, n, steps):
    """Try it with the keyboard only: focus each pulsing target and press Enter (twice where a chip comes first)."""
    with sync_playwright() as p:
        b = testlib.browser(p)
        pg, errs = testlib.open_card(b, n, 1300)
        pg.locator('#cv').scroll_into_view_if_needed()
        pg.locator('#cv .mtg [data-m="try"]').focus(); pg.keyboard.press('Enter'); pg.wait_for_timeout(500)
        f.check('Your turn1 of %d' % steps in pill(pg), 'keyboard: Enter on Try it starts Try it')
        for i in range(steps):
            pg.wait_for_timeout(1600)
            for _ in range(4):
                if 'Your turn%d of' % (i + 1) not in pill(pg):
                    break
                ok = js(pg, "var h=r.querySelector('.hint');if(!h)return false;h.focus();return r.activeElement===h")
                f.check(ok, 'keyboard step %d: the target takes focus' % (i + 1))
                pg.keyboard.press('Enter'); pg.wait_for_timeout(500)
        pg.wait_for_timeout(400)
        f.check('Done' in pill(pg), 'keyboard: every step completes with Enter (%s)' % pill(pg))
        f.check(not errs, 'keyboard: no page errors')
        b.close()


def clicks_only(f, n, picks, card_w=604, vw=1300):
    """Try it with the mouse only, from a fresh start: click only the pulsing target, never type. Done in exactly
    steps + picks clicks (picks: the number of extra data-pick clicks)."""
    with sync_playwright() as p:
        b = testlib.browser(p)
        pg, errs = testlib.open_card(b, n, vw, card_w)
        pg.locator('#cv').scroll_into_view_if_needed()
        pg.locator('#cv .mtg [data-m="try"]').click()
        ns = int(pg.locator('#cv #sn').text_content().split(' of ')[1])
        clicks = 0
        for i in range(ns):
            pg.wait_for_timeout(1600)
            for _ in range(5):
                if 'Your turn%d of' % (i + 1) not in pill(pg):
                    break
                pg.locator('#cv .hint').first.click(); clicks += 1; pg.wait_for_timeout(450)
        f.check('Done' in pill(pg) and clicks == ns + picks, 'card %d at %d px: mouse only, Done in %d clicks (%s)' % (n, card_w, clicks, pill(pg)))
        f.check(js(pg, EDIT) == 0, 'card %d at %d px: still no editable field at the end' % (n, card_w))
        f.check(not errs, 'card %d at %d px: mouse only, no page errors %s' % (n, card_w, errs[:1]))
        b.close()
