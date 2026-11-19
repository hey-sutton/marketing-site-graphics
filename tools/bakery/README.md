# Bakery graphics: generator and tests

This folder is the source for `graphics/bakery/card-1.js` to `card-4.js`. The Graphic Key is `bakery`. The page is for commercial production bakeries with a central bakery supplying shops and franchise locations.

* **Frame:** the same as Automotive, Frozen food and Pharmaceutical. `build.py` uses `tools/automotive/frame_auto.py` on the shared Watch and Try it frame (`tools/electronics/frame.py`) and only changes the key and label. That layer applies the November 11, 2026 UI rules: icon only Replay, control row order Studio, toggle, step counter, Replay, two lines with 40 px controls under 600 px, no plan wording in the Studio popover, and no nav or profile.
* **Build:** `python3 tools/bakery/build.py` rebuilds all four, or pass card numbers.
* **Cards:** `card1.py` to `card4.py` each hold one card: CSS, window HTML, data, render code and the step list. Every number on screen is computed from the data in the card (grams and cents, so sums are exact), not typed in as text.
  1. BOM scaling and cost roll up (page headline: Recipe Scaling & Cost Roll-Up): three stacked layer panels (Dough, Filling, Glaze), a version toggle, an ingredient price and the scaled batch, and a cost waterfall strip. Background 1.
  2. Bake Plan & Ingredient Check: bake list with status chips, an allocation panel, stock gauges and a purchase order strip. Background 2.
  3. Lot Trace & Allergen Response: allergen grid (products by allergen), batch strip, recipient cards and a hold panel. Background 3.
  4. Central Bakery to Shops: four stage transfer pipeline (Commit, Pick, Ship, Receive), a card per location and a rack tag strip. Background 4.
* **Inputs are real inputs:** typing works and Enter submits, with a sample button where there is a field (Cinnamon Roll and the batch size and butter price on card 1, AF-1042 on card 3, the Eastgate portal quantities on card 4). Invalid input shows an inline error and does not advance.
* **Tests:** `test_card1.py` to `test_card4.py` run the Automotive harness (`tools/automotive/auto_tests.py`) through `bk_tests.py`, which adds claim words (validated, HACCP, SQF, FDA, FSMA, audit ready), size words, POS, route truck, van, return and nutrition wording, and real bakery and supplier brand names to the banned words. Each first asserts every sum from the brief in Python, then checks the empty start screen, timing, Watch and Try it with every caption and number, typing and Enter, Replay, the toggle, the arrows, the Studio popover by click and by touch, reduced motion, both window edges at four widths, the control row at five card widths, every step at 390 and 340 px, a text scan, the card size and the background standard. Card 2 also checks that a short product can not be sent to the floor; card 4 that nothing is picked before approval and nothing is received before it ships.
* **UI check:** `python3 tools/automotive/check_demo_ui.py --html previewN.html --widths 1300 390 340`, and `--cards` on the four previews (none on all four for nav and profile).
* `shots.py N [card widths]` steps one card through Try it and saves a screenshot per step.

Run with `pip install playwright pillow` first. Set `PW_CHROME` to use a Chromium binary already on the machine. Screenshots go to `GFX_SHOTS` (default `/tmp/bakery_shots`).

Preview page: `python3 tools/electronics/make_preview_page.py --card graphics/bakery/card-1.js --bg graphics/bakery/bg-1.jpg --out preview1.html`.

The backgrounds are copies of `graphics/dairy/bg-1.jpg` to `bg-4.jpg` (604 by 540, progressive JPEG, about 50 KB). All data in the cards is illustrative.

**Mouse only (November 19, 2026).** A reader never has to type to move a demo forward. In Try it, clicking the highlighted button with its field left empty (or, for a number that starts filled in, left untouched) uses the sample value, so every step is one click. Typing still works, Enter still submits, and an unknown value still shows an inline error. `python3 tools/check_click_only.py bakery` checks it at 604 and 358 px.
