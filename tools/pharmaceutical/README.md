# Pharmaceutical graphics: generator and tests

This folder is the source for `graphics/pharmaceutical/card-1.js` to `card-4.js`. The Graphic Key is `pharmaceutical`.

* **Frame:** the same as Automotive and Frozen food. `build.py` uses `tools/automotive/frame_auto.py` on the shared Watch and Try it frame (`tools/electronics/frame.py`) and only changes the key and label. That layer applies the November 11, 2026 UI rules: icon only Replay, control row order Studio, toggle, step counter, Replay, two lines with 40 px controls under 600 px, no plan wording in the Studio popover, and no nav or profile.
* **Build:** `python3 tools/pharmaceutical/build.py` rebuilds all four, or pass card numbers.
* **Cards:** `card1.py` to `card4.py` each hold one card: CSS, window HTML, data, render code and the step list. Every number on screen is computed from the data in the card (grams for kilograms, so sums are exact), not typed in as text. Card 3 computes from milligrams per capsule, the batch size and the assay, so any valid batch size scales.
* **No typing (November 16, 2026):** every input (EX-3307, PO-4420, 200,000, MO-7210) is prefilled and read only. There are no sample buttons, no typing animation and no input error messages; the reader only clicks the button beside the field, in Watch and in Try it.
* **Tests:** `test_card1.py` to `test_card4.py` run the Automotive harness (`tools/automotive/auto_tests.py`) through `ph_tests.py`, which adds claim words (validated, Part 11, GMP, eBR, audit ready), size words and real pharma and distributor names to the banned words. Each first asserts every sum from the brief in Python, then checks the empty start screen, timing, Watch and Try it with every caption and number, the prefilled read only inputs, Replay, the toggle, the arrows, the Studio popover by click and by touch, reduced motion, both window edges at four widths, the control row at five card widths, every step at 390 and 340 px, a text scan, the card size and the background standard.
* **UI check:** `python3 tools/automotive/check_demo_ui.py --html previewN.html --widths 1300 390 340`, and `--cards` on the four previews (none on all four for nav and profile).
* `shots.py N [card widths]` steps one card through Try it and saves a screenshot per step.

Run with `pip install playwright pillow` first. Set `PW_CHROME` to use a Chromium binary already on the machine. Screenshots go to `GFX_SHOTS` (default `/tmp/pharma_shots`).

Preview page: `python3 tools/electronics/make_preview_page.py --card graphics/pharmaceutical/card-1.js --bg graphics/pharmaceutical/bg-1.jpg --out preview1.html`.

All data in the cards is illustrative.
