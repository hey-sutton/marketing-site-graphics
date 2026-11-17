"""Coffee roasting test setup: the Automotive harness (tools/automotive/auto_tests.py) pointed at graphics/coffee-roasting,
with the words this page may not show added to the banned list: claim words (validated, HACCP, SQF, FDA, FSMA, fair trade,
audit ready), size words, concept tags, and real coffee brands, importers, roasters, retailers and carriers."""
import os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(HERE), 'automotive'))
import auto_tests  # noqa: E402
from auto_tests import run_card, finish, js, pill, testlib  # noqa: E402,F401

testlib.KEY = 'coffee-roasting'
testlib.SHOTS = os.environ.get('GFX_SHOTS', '/tmp/coffee_shots')
os.makedirs(testlib.SHOTS, exist_ok=True)
testlib.EXTRA_CLAIMS = re.compile(
    testlib.EXTRA_CLAIMS.pattern
    + r'|(?i:\bvalidat\w*|\bHACCP\b|\bSQF\b|\bFDA\b|\bFSMA\b|audit ready|fair ?trade|rainforest alliance|\bbulk\b|\bmid\b|concept)'
    + r'|\b(?:Starbucks|Peet|Folgers|Maxwell|Dunkin|Lavazza|Illy|Nespresso|Blue Bottle|Intelligentsia|Stumptown|Counter Culture|La Colombe|Tim Hortons|Costco|Walmart|Kroger|Whole Foods|Trader Joe|Amazon|Royal Coffee|Cafe Imports|Olam|Volcafe|Sucafina|UPS|FedEx|USPS|DHL|Probat|Loring|Diedrich)\b')


def ids(pg, *names):
    return js(pg, "return %r.map(function(i){var e=r.getElementById(i);return e?e.textContent:null}).join('|')" % list(names))


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
