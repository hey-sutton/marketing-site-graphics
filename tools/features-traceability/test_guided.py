#!/usr/bin/env python3
"""
Click-through test for the guided handoff on the six traceability cards.

For each card: the intro runs with the Watching pill, hands off to Your turn on its own, then the test
clicks the one pulsing target at each step and checks the caption, the pill and the numbers on screen.
It also checks that a wrong click re-shows the prompt, that only one target pulses at a time, that the
prefilled input is filled but nothing derived from it shows before the step runs, that Replay resets,
and that nothing throws. Saves a screenshot per step.

  python3 tools/features-traceability/test_guided.py --page preview.html --out /tmp/shots
(Build the page first with the skill's make_preview_page.py, cards 1 to 6 in order.)
"""
import argparse, os, sys
from playwright.sync_api import sync_playwright

ap = argparse.ArgumentParser(); ap.add_argument("--page", required=True); ap.add_argument("--out", default="/tmp/trace_shots")
ap.add_argument("--width", type=int, default=604)
a = ap.parse_args(); os.makedirs(a.out, exist_ok=True)

# per card: total steps, then per guided step (caption title, text that must be on screen after it)
PLAN = {
 1: (4, [("Lot GR-1021A is assigned", "04/19/2027"), ("Actual cost per case, $18.40", "$18.40"), ("Where every case went", "1,200 of 1,200 cases")]),
 2: (5, [("Quantity is filled in", None), ("Both labels stay linked", "LP-00418-2"), ("The new label has its own history", "Split from LP-00418, 40 cases"), ("Filter labels by status", "In transit")]),
 3: (5, [("The supplier COA rides with the lot", "Within spec"), ("QC checks with photos", "D. Nguyen"), ("The FSMA 204 sheet", "Every key data element filled"), ("Sorted, newest first", "Oldest first")]),
 4: (4, [("Oldest best by goes first", "Use first"), ("Cost history on every lot", "9,190 lb, $37,679.00"), ("A heads up before you run short", "below minimum")]),
 5: (4, [("Every PO from this supplier", "PO-1142"), ("The lot, its COA and every batch", "COA-SN-0917.pdf"), ("Compare the older lot", "1,250 lb")]),
 6: (5, [("Traced forward in seconds", "3,250"), ("Everything still here is on hold", "640 cases and 9,190 lb on hold"), ("Who to call", "2,410"), ("4 of 5 recall steps done", "4 of 5 done")]),
}
fails = []
def check(cond, msg):
    print(("  ok   " if cond else "  FAIL ") + msg)
    if not cond: fails.append(msg)

with sync_playwright() as p:
    b = p.chromium.launch(executable_path=os.environ.get("PW_CHROME") or None); pg = b.new_page(viewport={"width": 700, "height": 620 if a.width == 604 else 380})
    errs = []; pg.on("pageerror", lambda e: errs.append(str(e)))
    pg.goto("file://" + os.path.abspath(a.page)); pg.wait_for_timeout(800)
    if a.width != 604:
        pg.click("#wp"); pg.wait_for_timeout(500)
    for i, n in enumerate(sorted(PLAN)):
        total, steps = PLAN[n]; cv = "#cv%d" % i
        print("card-%d" % n)
        pg.locator(cv).scroll_into_view_if_needed()
        mode = pg.locator(cv + " .mode")
        pg.wait_for_timeout(1600)
        check("Watching" in mode.text_content(), "intro shows Watching (%s)" % mode.text_content().replace("\n", " "))
        if n == 5:
            q = pg.locator(cv + " #q").input_value()
            check(q == "Sierra Nut Co", "search is prefilled")
            check("PO-1187" not in pg.locator(cv + " #pos").inner_text(), "nothing derived shows before the search runs")
        if n == 2:
            check(pg.locator(cv + " #spf.on").count() == 0, "split form closed at start")
        pg.locator(cv).screenshot(path=os.path.join(a.out, "card%d-0-intro.png" % n))
        pg.wait_for_function("s=>{const h=document.querySelector(s+' [data-sxg-host]');const m=h&&h.shadowRoot.querySelector('.mode');return m&&m.textContent.indexOf('Your turn')>-1}", arg=cv, timeout=9000)
        check(True, "hands off to Your turn on its own")
        for k, (title, must) in enumerate(steps):
            pg.wait_for_timeout(1700)
            hints = pg.locator(cv + " .hint")
            check(hints.count() == 1, "step %d: exactly one pulsing target (%d)" % (k + 2, hints.count()))
            check(pg.locator(cv + " .fade").count() > 0, "step %d: the rest of the screen is dimmed" % (k + 2))
            check(("%d of %d" % (k + 2, total)) in mode.text_content(), "step %d: pill reads %d of %d" % (k + 2, k + 2, total))
            pg.locator(cv + " .cap.turn.on").wait_for(timeout=3000)
            pg.locator(cv).screenshot(path=os.path.join(a.out, "card%d-%d-prompt.png" % (n, k + 1)))
            if k == 0:  # a click somewhere else re-shows the prompt, does not advance
                pg.locator(cv + " .fw-head").first.click(position={"x": 30, "y": 20}); pg.wait_for_timeout(300)
                check(("%d of %d" % (k + 2, total)) in mode.text_content(), "step 2: a wrong click does not advance")
            hints.first.click(); pg.wait_for_timeout(700)
            cap = pg.locator(cv + " .cap:not(.turn)").inner_text()
            check(title in cap, "step %d caption: %s" % (k + 2, cap.replace(chr(10), " ")[:70]))
            if must:
                check(must in pg.locator(cv + " .fwin").inner_text(), "step %d screen shows '%s'" % (k + 2, must))
            pg.wait_for_timeout(500)
            pg.locator(cv).screenshot(path=os.path.join(a.out, "card%d-%d-after.png" % (n, k + 1)))
        check("Done" in mode.text_content() and ("%d of %d" % (total, total)) in mode.text_content(), "ends on Done %d of %d" % (total, total))
        check(pg.locator(cv + " .hint").count() == 0, "no pulsing target after Done")
        pg.locator(cv + " .rp").click(); pg.wait_for_timeout(1500)
        check("Watching" in mode.text_content(), "Replay restarts the intro")
        pg.locator(cv + " .studio-chip").click(); pg.wait_for_timeout(500)
        check(pg.locator(cv + " .studio.open").count() == 1, "Studio popover opens")
        pg.keyboard.press("Escape")
    check(not errs, "no page errors %s" % errs[:3])
    b.close()
print("\n%d failures" % len(fails)); sys.exit(1 if fails else 0)
