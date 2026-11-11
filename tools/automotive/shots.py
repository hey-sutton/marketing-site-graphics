#!/usr/bin/env python3
"""Quick look: step one card through Try it and save a screenshot per step.
Run: python3 tools/automotive/shots.py N [card widths...]. Screenshots go to GFX_SHOTS (default /tmp/automotive_shots)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from auto_tests import testlib
from playwright.sync_api import sync_playwright

n = int(sys.argv[1]); widths = [int(a) for a in sys.argv[2:]] or [604, 358]
with sync_playwright() as p:
    b = testlib.browser(p)
    for cw in widths:
        pg, errs = testlib.open_card(b, n, 1300 if cw > 560 else cw + 32, cw)
        pg.locator('#cv').scroll_into_view_if_needed(); pg.wait_for_timeout(300)
        testlib.shot(pg, 'q%d_%d_0.png' % (n, cw))
        pg.locator('#cv .mtg [data-m="try"]').click()
        NS = int(pg.locator('#cv #sn').text_content().split(' of ')[1])
        for i in range(NS):
            pg.wait_for_timeout(1500)
            testlib.shot(pg, 'q%d_%d_%dp.png' % (n, cw, i + 1))
            if i == 0 and pg.locator('#cv [data-sample]').count():
                pg.locator('#cv [data-sample]').first.click(); pg.wait_for_timeout(200)
            pg.locator('#cv .hint').first.click(); pg.wait_for_timeout(1300)
            testlib.shot(pg, 'q%d_%d_%d.png' % (n, cw, i + 1))
        print(cw, 'pill', testlib.pill(pg), 'errors', errs)
        pg.close()
    b.close()
