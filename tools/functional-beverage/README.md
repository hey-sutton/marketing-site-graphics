# Functional beverage graphics: generator and tests

This folder is the source for `graphics/functional-beverage/card-1.js` to `card-4.js`, for the page /industries/functional-beverage-manufacturing-software. The Graphic Key is `functional-beverage` (the CMS slug differs, so the Graphic Key field must be set explicitly). The key is not in `manifest.json` yet: the release owner adds `"functional-beverage": [1, 2, 3, 4]`, bumps the version and tags the release on the merged main commit.

* **Frame:** the same as Food brand inventory and Sauce manufacturing. `build.py` uses `tools/automotive/frame_auto.py` on the shared Watch and Try it frame (`tools/electronics/frame.py`, built on the Brewery scaffold with the 716 by 640 window, step arrows, ripple hotspots, Studio badge and popover, Replay, aria labels, reduced motion). It changes the key and label and moves the first action to 900 ms.
* **Build:** `python3 tools/functional-beverage/build.py` rebuilds all four, or pass card numbers.
* **Cards** (each layout used once, each background used once):
  1. Dosing & Label Claims, record form with a side summary. Background 1.
  2. Ingredient Lots & Certificates, list and detail. Background 2.
  3. Formula Versions & Reformulation, board (History, In production, Draft; versions move by click). Background 3.
  4. Batch Testing & Release, stage chain (Filled, Hold, Tests, Release) with running can counts. Background 4.
* **Read only demos:** every input (12 oz can on card 1, Focus Citrus Sparkling on card 3, the three results on card 4) is prefilled, `readonly`, `tabindex="-1"`, gray, with no pointer events. No typing, no typing animation, no sample buttons, no error messages. Card 1's potency is a preset chip (5.0, 4.5, 4.0 percent). Card 4's second result set is a preset toggle (Result set 1 or 2). Card 2 step 3 is two clicks: open ASH-2305 (marked `data-pick`), then Hold.
* **Tests:** `test_card1.py` to `test_card4.py` run the Automotive harness through `fv_tests.py`. Each first asserts every number and rule from the page README in Python, then checks the start screen (prefilled read only inputs, no editable input, textarea or contenteditable, nothing derived shown), timing, Watch and Try it with every caption and number, Replay, the toggle, the arrows, the Studio popover by click and touch, reduced motion, both window edges at four widths, the control row at five widths, every step at 390 and 340 px, a text scan, the card size and the background standard, plus a keyboard only walk and a mouse only walk at 604 and 358 px. Card 4 also switches to result set 2 and checks that only yeast and mold is flagged and Release is disabled.
* `shots.py N [card widths]` steps one card through Try it and saves a screenshot per step.
* `tools/automotive/check_demo_ui.py` clicks the hint once per step, so it reports card 2 as not reaching Done: its two click step is by design. `tools/check_click_only.py functional-beverage` passes all four.

Run with `pip install playwright pillow` first. Set `PW_CHROME` to use a Chromium binary already on the machine. Screenshots go to `GFX_SHOTS` (default `/tmp/fv_shots`).

**Numbers notes:** card 3 costs are kept in cents (v7: 9 + 12 + 38 + 25 = 84; v8: 7 + 9 + 38 + 25 = 79), so the change is minus 5 cents, minus 6.0 percent. Card 1's other actives (L-theanine, lemon balm) carry no label claim in the README, so only withanolides are checked.

The backgrounds are copies of `graphics/food-co-packing/bg-1.jpg` to `bg-4.jpg` (604 by 540, progressive JPEG, about 50 KB). All names, quantities and readings in these demos are invented sample data for illustration.
