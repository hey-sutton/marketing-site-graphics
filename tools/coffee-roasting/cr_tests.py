"""Coffee roasting test setup: the Automotive harness (tools/automotive/auto_tests.py) pointed at graphics/coffee-roasting,
with this page's banned words. The Automotive list, including "subscription", applies as is (the repo UI checker bans it too,
so card 4 says "web and club orders"). Added: claim words (organic certified, fair trade
certified, FDA, FSMA, SQF, validated, audit ready), "recipe", size words, concept tags, and real roaster, importer and
retailer names."""
import os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(HERE), 'automotive'))
import auto_tests  # noqa: E402
from auto_tests import run_card, finish, js, pill, testlib  # noqa: E402,F401

testlib.KEY = 'coffee-roasting'
testlib.SHOTS = os.environ.get('GFX_SHOTS', '/tmp/cr_shots')
os.makedirs(testlib.SHOTS, exist_ok=True)
testlib.EXTRA_CLAIMS = re.compile(
    r'(?i:\bpricing\b|\bprice plan|\byour plan\b|\bpaid plan|\bplan tier|\bper month\b|/mo\b|free trial|\btrial\b|subscription|\bsmall\b|mid ?size|enterprise|\blarge\b|startup'
    r'|concept|live product demo|illustrative|compliance|compliant|certified|\bvalidat\w*|\bFDA\b|\bFSMA\b|\bSQF\b|\bHACCP\b|audit ready|\bbulk\b|\bmid\b|\brecipe)'
    r'|\b(?:Starbucks|Peet|Folgers|Maxwell|Dunkin|Lavazza|Illy|Intelligentsia|Stumptown|Counter Culture|Blue Bottle|La Colombe|Onyx|Olam|Volcafe|Sucafina|Royal Coffee|Cafe Imports|Walmart|Costco|Kroger|Target|Whole Foods|Trader Joe|Amazon|UPS|FedEx|USPS|DHL|Digit)\b')


def ids(pg, *names):
    return js(pg, "return %r.map(function(i){var e=r.getElementById(i);return e?e.textContent:null}).join('|')" % list(names))


def click_in(pg, sel, wait=400):
    pg.locator('#cv ' + sel).click()
    pg.wait_for_timeout(wait)


def enter_submits(f, n, inp_sel, value, want_pill, prep=None):
    """Try it, type value into the input and press Enter: the step completes."""
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        b = testlib.browser(p)
        pg, errs = testlib.open_card(b, n, 1300)
        pg.locator('#cv').scroll_into_view_if_needed()
        pg.locator('#cv .mtg [data-m="try"]').click(); pg.wait_for_timeout(400)
        if prep:
            prep(pg)
        inp = pg.locator('#cv ' + inp_sel); inp.click(); inp.fill(''); inp.press_sequentially(value); inp.press('Enter'); pg.wait_for_timeout(500)
        f.check(want_pill in pill(pg), 'Enter submits the typed value (%s)' % pill(pg))
        b.close()


def keyboard_walk(f, n, steps, fill=None):
    """Try it with the keyboard only: focus each pulsing target and press Enter (fill(pg, i) types into a field first)."""
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        b = testlib.browser(p)
        pg, errs = testlib.open_card(b, n, 1300)
        pg.locator('#cv').scroll_into_view_if_needed()
        pg.locator('#cv .mtg [data-m="try"]').focus(); pg.keyboard.press('Enter'); pg.wait_for_timeout(500)
        f.check('Your turn1 of %d' % steps in pill(pg), 'keyboard: Enter on Try it starts Try it')
        for i in range(steps):
            pg.wait_for_timeout(1600)
            if fill:
                fill(pg, i)
            ok = js(pg, "var h=r.querySelector('.hint');if(!h)return false;h.focus();return r.activeElement===h")
            f.check(ok, 'keyboard step %d: the target takes focus' % (i + 1))
            pg.keyboard.press('Enter'); pg.wait_for_timeout(700)
        f.check('Done' in pill(pg), 'keyboard: every step completes with Enter (%s)' % pill(pg))
        f.check(not errs, 'keyboard: no page errors')
        b.close()


def clicks_only(f, n, card_w=604, vw=1300):
    """Try it with the mouse only: from a fresh start, click the one highlighted target at each step, never type and
    never use a sample button. The card must reach Done in exactly one click per step (November 18, 2026 rule: a reader
    should not have to leave the mouse or trackpad to move a demo forward)."""
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        b = testlib.browser(p)
        pg, errs = testlib.open_card(b, n, vw, card_w)
        pg.locator('#cv').scroll_into_view_if_needed()
        pg.locator('#cv .mtg [data-m="try"]').click()
        ns = int(pg.locator('#cv #sn').text_content().split(' of ')[1])
        clicks = 0
        for i in range(ns):
            pg.wait_for_timeout(1600)
            want = 'Your turn%d of %d' % (i + 1, ns)
            if want not in pill(pg):
                f.check(False, 'card %d at %d px: mouse only, step %d is reached (%s)' % (n, card_w, i + 1, pill(pg)))
                break
            pg.locator('#cv .hint').first.click()
            clicks += 1
            pg.wait_for_timeout(500)
        typed = js(pg, "return [].map.call(r.querySelectorAll('input'),function(i){return i.value}).join('|')")
        f.check('Done' in pill(pg) and clicks == ns, 'card %d at %d px: mouse only, Done in %d clicks with no typing (%s)' % (n, card_w, clicks, pill(pg)))
        f.check(not errs, 'card %d at %d px: mouse only, no page errors %s' % (n, card_w, errs[:1]))
        b.close()
        return typed
