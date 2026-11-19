#!/usr/bin/env python3
"""Mouse only check for every Watch and Try it card (November 18, 2026 rule: a reader should not have to leave the
mouse or trackpad to move a demo forward, even in Try it).

For each card built on the shared frame (tools/electronics/frame.py), the check opens the card, switches to Try it and
only ever clicks the highlighted target. It never types and never uses a sample button. A card passes when it reaches
Done with no page errors. Steps that need more than one click (for example three option picks) are allowed, up to
MAX_PER_STEP clicks, and are listed so they stay visible.

Cards on the older engines (no Try it toggle) are skipped: they move forward with the next arrow and fill in their own
sample values.

Run: python3 tools/check_click_only.py [industry ...]   (default: every industry in manifest.json with cards 1 to 4)
Set PW_CHROME to a Chromium binary if Playwright's own browser is missing."""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, 'electronics'))
import testlib  # noqa: E402
from playwright.sync_api import sync_playwright  # noqa: E402

MAX_PER_STEP = 3
SIZES = ((1300, 604), (390, 358))


def run(b, key, n, vw, cw):
    testlib.KEY = key
    try:
        pg, errs = testlib.open_card(b, n, vw, cw)
    except Exception:
        return None, 'skipped (no frame host)'
    try:
        if not pg.locator('#cv .mtg [data-m="try"]').count():
            return None, 'skipped (older engine)'
        pg.locator('#cv').scroll_into_view_if_needed()
        pg.locator('#cv .mtg [data-m="try"]').click()
        ns = int(pg.locator('#cv #sn').text_content().split(' of ')[1])
        extra = []
        for i in range(ns):
            want = 'Your turn%d of %d' % (i + 1, ns)
            pg.wait_for_timeout(1500)
            if want not in testlib.pill(pg):
                return False, 'step %d never reached (%s)' % (i + 1, testlib.pill(pg))
            k = 0
            while k < MAX_PER_STEP and want in testlib.pill(pg):
                pg.locator('#cv .hint').first.click()
                k += 1
                pg.wait_for_timeout(600)
            if want in testlib.pill(pg):
                prompt = testlib.js(pg, "var t=r.querySelector('.cap.turn');return t?t.innerText.replace(/\\s+/g,' '):''")
                return False, 'step %d does not move on with clicks only: %s' % (i + 1, prompt)
            if k > 1:
                extra.append('step %d takes %d clicks' % (i + 1, k))
        pg.wait_for_timeout(400)
        ok = 'Done' in testlib.pill(pg) and not errs
        return ok, ('Done' if 'Done' in testlib.pill(pg) else testlib.pill(pg)) + (', ' + ', '.join(extra) if extra else '') + (' ERROR ' + errs[0][:100] if errs else '')
    finally:
        pg.close()


def main(keys):
    if not keys:
        m = json.load(open(os.path.join(os.path.dirname(HERE), 'manifest.json')))
        keys = [k for k, v in m['graphics'].items() if v == [1, 2, 3, 4]]
    bad = []
    with sync_playwright() as p:
        b = testlib.browser(p)
        for key in keys:
            for n in (1, 2, 3, 4):
                for vw, cw in SIZES:
                    ok, msg = run(b, key, n, vw, cw)
                    print('  %s %s card %d at %d px: %s' % ({True: 'ok  ', False: 'FAIL', None: '--  '}[ok], key, n, cw, msg), flush=True)
                    if ok is False:
                        bad.append('%s card %d at %d px' % (key, n, cw))
                    if ok is None:
                        break
        b.close()
    print('\n%d failing' % len(bad) + (': ' + '; '.join(bad) if bad else ''))
    sys.exit(1 if bad else 0)


if __name__ == '__main__':
    main(sys.argv[1:])
