#!/usr/bin/env python3
"""Quick look: step one card through Try it at a desktop and a phone width and save a screenshot per step.
Run: python3 tools/footwear/shots.py N [card widths...]. Screenshots go to GFX_SHOTS (default /tmp/footwear_shots)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from footwear_tests import testlib, js
from playwright.sync_api import sync_playwright

n = int(sys.argv[1]); widths = [int(a) for a in sys.argv[2:]] or [604, 358]
with sync_playwright() as p:
    b = testlib.browser(p)
    for cw in widths:
        pg, errs = testlib.open_card(b, n, 1300 if cw > 520 else cw + 32, cw)
        pg.locator('#cv').scroll_into_view_if_needed(); pg.wait_for_timeout(300)
        testlib.shot(pg, 'q%d_%d_0.png' % (n, cw))
        pg.locator('#cv .mtg [data-m="try"]').click()
        NS = js(pg, 'return r.querySelectorAll(".stp").length') and int(pg.locator('#cv .stp .sn').text_content().split(' of ')[1])
        for i in range(NS):
            pg.wait_for_timeout(1500)
            testlib.shot(pg, 'q%d_%d_%dp.png' % (n, cw, i + 1))
            pg.locator('#cv .hint').first.click(); pg.wait_for_timeout(900)
            testlib.shot(pg, 'q%d_%d_%d.png' % (n, cw, i + 1))
        print(cw, 'pill', testlib.pill(pg), 'errors', errs)
        pg.close()
    b.close()
