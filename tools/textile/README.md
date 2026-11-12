# Textile graphics: generator and tests

This folder is the source for `graphics/textile/card-1.js` to `card-4.js`. The Graphic Key is `textile`.

* **Frame and engine:** the shared Watch and Try it frame in `tools/electronics/frame.py`, through the Automotive layer `tools/automotive/frame_auto.py` (November 11, 2026 control row: icon only Replay, Studio, toggle, step counter, two lines under 600 px, 40 px touch targets, no side nav, one header). `frame_textile.py` only sets the key and shortens the dwell per step from 2.9 s to 2.4 s, so each four step walkthrough runs in about 14 seconds.
* **Shared data:** `data.py` holds every figure used on the page (dye lot DL-2611-B, the rolls, shipments, WO-5520, the costs, CO-771) and asserts the brief's sums on import: 120+118+122+119+121 = 600, 600+168 = 768, 360+744+480 = 1,584, 1,584+768 = 2,352, 360 reserved, 60+61 = 121, 119+121 = 240, 300+180 = 480, 6×400 = 2,400, 6×392 = 2,352, 48 yd shrink (2.0%), 2,352−12 = 2,340, costs $6,816.00 + $2,040.00 + $705.60 = $9,561.60, $4.02 (BOM estimate, 2,376 yd) and $4.09 (measured, 2,340 yd) per yd, 36×3 = 108, 109−108 = 1, 119−109 = 10, tolerance 1.62.
* **Build:** `python3 tools/textile/build.py` rebuilds all four, or pass card numbers.
* **Cards:** `card1.py` to `card4.py` each hold one card: CSS, window HTML, render code and the step list.

| Card | Feature | Layout | Walkthrough |
|---|---|---|---|
| 1 | Roll & Dye Lot Control | Roll table with a label and record panel | Scan R-48214, reserve 360 yd for SO-3318 from DL-2611-B, R-48330 blocked, split R-48215 into 60 and 61 |
| 2 | Production Stages & Outsourced Steps | Five column stage board | Pick WO-5520, open the Dyeing column, receive 6 rolls of 392 yd, confirm 2,340 yd and $4.09 per yd |
| 3 | Cutting & Yield Verification | Split view with a roll length bar | R-48330 rejected, R-48214 accepted, three lays of 36 yd, 109 yd used, remnant R-48214-R1 10 yd |
| 4 | Fiber to Fabric Traceability | Two direction genealogy graph | Trace R-48211 back to yarn lots, open YL-7702 files, follow DL-2611-B forward to 2,352 yd, package the record |

* **Tests:** `test_card1.py` to `test_card4.py` run `textile_tests.py` (a copy of `tools/automotive/auto_tests.py` with the textile key and word list, built on `tools/electronics/testlib.py`). Each asserts the brief's numbers in Python, derived independently of the card, then checks in the browser: the empty start screen, start within 1.5 s and first result within 4 s, Watch through every step and the loop, the take over, Try it with a wrong click and invalid input, every caption and number, typing and Enter, the sample buttons, the arrows, Replay, the toggle, the Studio popover, reduced motion, the window past the right and bottom edges at 1300, 1024, 768 and 390 px with a square corner and no empty band, the control row at card widths 604 to 340, touch, a text scan, card size and the background standard.
* `shots.py N [card widths]` steps one card through Try it and saves a screenshot per step.

Run with `pip install playwright pillow` first. Set `PW_CHROME` to use a Chromium binary already on the machine. Screenshots go to `GFX_SHOTS` (default `/tmp/textile_shots`).

Preview page: `python3 tools/electronics/make_preview_page.py --card graphics/textile/card-1.js --bg graphics/textile/bg-1.jpg --out preview1.html`.

All data in the cards is illustrative and every name is made up.
