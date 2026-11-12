# Frozen food graphics: generator and tests

This folder is the source for `graphics/frozen-food/card-1.js` to `card-4.js`. The Graphic Key is `frozen-food`.

* **Frame:** the same as Automotive. `build.py` uses `tools/automotive/frame_auto.py` on the shared Watch and Try it frame (`tools/electronics/frame.py`) and only changes the key and label. That layer applies the November 11, 2026 UI rules: icon only Replay, control row order Studio, toggle, step counter, Replay, two lines with 40 px controls under 600 px, no plan wording in the Studio popover, and no nav or profile.
* **Build:** `python3 tools/frozen-food/build.py` rebuilds all four, or pass card numbers.
* **Cards:** `card1.py` to `card4.py` each hold one card: CSS, window HTML, data, render code and the step list. Card class names must not reuse the frame's own (for example `.ctl`, `.mc`, `.bn`); the tests catch a hidden step counter or a class read as a nav.
* **Tests:** `test_card1.py` to `test_card4.py` run the Automotive harness (`tools/automotive/auto_tests.py`) through `ff_tests.py`, which adds food brand and grocer names to the banned words. Each asserts the brief's sums in Python first, then checks the empty start screen, timing, Watch and Try it with every caption and number, invalid input, Replay, the toggle, the arrows, the Studio popover, reduced motion, both window edges at four widths, the control row at five card widths and by touch, every step at 390 and 340 px, a text scan and the card size.
* **UI check:** `python3 tools/automotive/check_demo_ui.py --html previewN.html --widths 1300 390 340`, and `--cards` on the four previews.
* `shots.py N [card widths]` steps one card through Try it and saves a screenshot per step.

Run with `pip install playwright pillow` first. Set `PW_CHROME` to use a Chromium binary already on the machine. Screenshots go to `GFX_SHOTS` (default `/tmp/frozen_shots`).

All data in the cards is illustrative.
