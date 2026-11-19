# Sauce manufacturing graphics: generator and tests

This folder is the source for `graphics/sauce-manufacturing/card-1.js` to `card-4.js`, for the page /industries/sauce-manufacturing-software. The Graphic Key is `sauce-manufacturing` (the CMS slug differs, so the Graphic Key field must be set explicitly). The key is not in `manifest.json` yet: the release owner adds `"sauce-manufacturing": [1, 2, 3, 4]`, bumps the version and tags the release.

* **Frame:** the same as Food brand inventory, Pharmaceutical and Coffee roasting. `build.py` uses `tools/automotive/frame_auto.py` on the shared Watch and Try it frame (`tools/electronics/frame.py`, built on the Brewery scaffold with the 716 by 640 window, step arrows, ripple hotspots, Studio badge and popover, Replay, aria labels, reduced motion). It changes the key and label and moves the first action to 900 ms.
* **Build:** `python3 tools/sauce-manufacturing/build.py` rebuilds all four, or pass card numbers.
* **Cards** (each layout used once, each background used once):
  1. Batch Scaling & Conversions, record form with a side summary. Background 1.
  2. Kettle & Tank Batch Records, stage chain (Cook, Hold, Fill) with running volumes. Background 2.
  3. Bulk Sauce to Filled Units, list and detail. Background 3.
  4. Ingredient Lots & Allergen Control, board (lot, batches, filled lots, customers; run order with a cleaning card moved in by click). Background 4.
* **Read only demos:** every input (500 gal on card 1, the three readings on card 2, SP-LOT-5530 on card 4) is prefilled, `readonly`, `tabindex="-1"`, gray, with no pointer events. No typing, no typing animation, no sample buttons, no error messages. Steps with more than one click mark every click but the last with `data-pick`: card 2 Hold then Sign off and release, card 3 Fill on each of the three allocations, card 4 Check next batch then Log cleaning.
* **Tests:** `test_card1.py` to `test_card4.py` run the Automotive harness through `sm_tests.py`. Each first asserts every sum, conversion and percentage from the page README in Python, then checks the start screen (prefilled read only inputs, no editable input, textarea or contenteditable, nothing derived shown), timing, Watch and Try it with every caption and number, Replay, the toggle, the arrows, the Studio popover by click and touch, reduced motion, both window edges at four widths, the control row at five widths, every step at 390 and 340 px, a text scan, the card size and the background standard, plus a keyboard only walk and a mouse only walk at 604 and 358 px.
* `shots.py N [card widths]` steps one card through Try it and saves a screenshot per step.
* `tools/automotive/check_demo_ui.py` clicks the hint once per step, so it reports cards 2, 3 and 4 as not reaching Done: their multi click steps are by design. `tools/check_click_only.py sauce-manufacturing` passes all four.

Run with `pip install playwright pillow` first. Set `PW_CHROME` to use a Chromium binary already on the machine. Screenshots go to `GFX_SHOTS` (default `/tmp/sm_shots`).

**Numbers notes:** card 1 keeps the kettle lines as gallons and density (soy sauce 40 gal at 9.0 lb per gal is 360 lb; the six lines are 500 gal and 4,455 lb, factor 222.75 from the 20 lb test pot). Card 3's README asks for "two flavors and three jar sizes", but its data has two jar sizes (12 oz and 32 oz) across three allocations; the card follows the data. Jar counts are whole jars at 128 fl oz per gallon (200 gal is 2,133 jars of 12 oz).

The backgrounds are copies of `graphics/food-co-packing/bg-1.jpg` to `bg-4.jpg` (604 by 540, progressive JPEG, about 50 KB). All names, quantities and readings in these demos are invented sample data for illustration.
