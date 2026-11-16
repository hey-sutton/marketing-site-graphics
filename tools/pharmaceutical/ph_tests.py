"""Pharmaceutical test setup: the Automotive harness (tools/automotive/auto_tests.py) pointed at graphics/pharmaceutical,
with the words this page may not show added to the banned list: claim words (validated, Part 11, GMP, eBR, audit ready),
size words, and real drug, pharma and distributor names."""
import os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(HERE), 'automotive'))
import auto_tests  # noqa: E402
from auto_tests import run_card, finish, js, pill, testlib  # noqa: E402,F401

testlib.KEY = 'pharmaceutical'
testlib.SHOTS = os.environ.get('GFX_SHOTS', '/tmp/pharma_shots')
os.makedirs(testlib.SHOTS, exist_ok=True)
testlib.EXTRA_CLAIMS = re.compile(
    testlib.EXTRA_CLAIMS.pattern
    + r'|(?i:\bvalidat\w*|part 11|\bGMP\b|\beBR\b|electronic batch record|audit ready|\bbulk\b|\bsmall\b|\bmid\b|\blarge\b)'
    + r'|\b(?:Pfizer|Merck|Novartis|Roche|Sanofi|AbbVie|Bayer|Lonza|Catalent|Teva|Mylan|Viatris|Avantor|McKesson|Cardinal|Cencora|AmerisourceBergen|CVS|Walgreens|Avicel|Capsugel)\b')


def ids(pg, *names):
    return js(pg, "return %r.map(function(i){var e=r.getElementById(i);return e?e.textContent:null}).join('|')" % list(names))


def enter_submits(f, n, inp_sel, value, want_pill):
    """Try it, type value into the input and press Enter: the step completes."""
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        b = testlib.browser(p)
        pg, errs = testlib.open_card(b, n, 1300)
        pg.locator('#cv').scroll_into_view_if_needed()
        pg.locator('#cv .mtg [data-m="try"]').click(); pg.wait_for_timeout(400)
        inp = pg.locator('#cv ' + inp_sel); inp.click(); inp.fill(''); inp.press_sequentially(value); inp.press('Enter'); pg.wait_for_timeout(500)
        f.check(want_pill in pill(pg), 'Enter submits the typed value (%s)' % pill(pg))
        b.close()
