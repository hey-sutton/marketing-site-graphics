# Food co-packing graphics: generator and tests

This folder is the source for `graphics/food-co-packing/card-1.js` to `card-4.js`. The Graphic Key is `food-co-packing` (the CMS slug is `food-co-packing-erp`, so the Graphic Key field must be set explicitly). The key is not in `manifest.json` yet: the release owner adds `"food-co-packing": [1, 2, 3, 4]` and bumps the version.

* **Frame:** the same as Automotive, Frozen food, Pharmaceutical and Bakery. `build.py` uses `tools/automotive/frame_auto.py` on the shared Watch and Try it frame (`tools/electronics/frame.py`) and only changes the key and label. That layer applies the November 11, 2026 UI rules: icon only Replay, control row order Studio, toggle, step counter, Replay, two lines with 40 px controls under 600 px, no plan wording in the Studio popover, and no nav or profile.
* **Build:** `python3 tools/food-co-packing/build.py` rebuilds all four, or pass card numbers.
* **Cards:** `card1.py` to `card4.py` each hold one card: CSS, window HTML, data, render code and the step list. Every number on screen is computed from the data in the card (grams, cents, minutes), not typed in as text.
  1. Client Inventory & Ownership, list and detail: rice flour lots for three clients and the plant, balance by owner, next runs and finished goods held for clients. Background 1.
  2. Run Scheduling & Changeovers, board: a week strip, a Line 2 day timeline with run blocks and cleaning gaps from an allergen changeover matrix, a run order table, day totals and the run sheet. Background 2.
  3. Cross Client Traceability, stage chain: a vertical chain of four stages with running totals, a stage detail panel and a recall scope by brand. Background 3.
  4. Run Billing & Client Portal, record form with a side summary: run record, billing lines, a fee and materials panel, and an invoice summary that turns into the client portal view. Background 4.
* **Inputs are real inputs:** typing works and Enter submits, with a sample button where there is a field (Rice flour on card 1, SE-3318 on card 3, R-5108 and the fee rate on card 4). Invalid input shows an inline error and does not advance.
* **Tests:** `test_card1.py` to `test_card4.py` run the Automotive harness (`tools/automotive/auto_tests.py`) through `fc_tests.py`, which adds claim words (validated, HACCP, SQF, BRCGS, FDA, FSMA, audit ready), size words, concept tags, and real brand and retailer names to the banned words. Each first asserts every sum, conversion and percentage in Python, then checks the empty start screen, timing, Watch and Try it with every caption and number, typing and Enter, Replay, the toggle, the arrows, the Studio popover by click and by touch, reduced motion, both window edges at four widths, the control row at five card widths, every step at 390 and 340 px, a text scan, the card size and the background standard.
* **UI check:** `python3 tools/automotive/check_demo_ui.py --html previewN.html --widths 1300 390 340`, and `--cards` on the four previews (none on all four for nav and profile).
* `shots.py N [card widths]` steps one card through Try it and saves a screenshot per step.

Run with `pip install playwright pillow` first. Set `PW_CHROME` to use a Chromium binary already on the machine. Screenshots go to `GFX_SHOTS` (default `/tmp/fcp_shots`).

Preview page: `python3 tools/electronics/make_preview_page.py --card graphics/food-co-packing/card-1.js --bg graphics/food-co-packing/bg-1.jpg --out preview1.html`.

The backgrounds are copies of `graphics/frozen-food/bg-1.jpg` to `bg-4.jpg` (604 by 540, progressive JPEG, about 50 KB). All names, quantities and readings are invented sample data for illustration. Several flows are screens built on Studio, so they show what Sutton can be configured to do rather than a fixed shipped screen.

**Mouse only (November 19, 2026).** A reader never has to type to move a demo forward. In Try it, clicking the highlighted button with its field left empty (or, for a number that starts filled in, left untouched) uses the sample value, so every step is one click. Typing still works, Enter still submits, and an unknown value still shows an inline error. `python3 tools/check_click_only.py food-co-packing` checks it at 604 and 358 px.
