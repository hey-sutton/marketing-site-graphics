# Food brand inventory graphics: generator and tests

This folder is the source for `graphics/food-brand-inventory/card-1.js` to `card-4.js`, for the page /industries/food-brand-inventory-management-software. The Graphic Key is `food-brand-inventory` (the CMS slug differs, so the Graphic Key field must be set explicitly). The key is not in `manifest.json` yet: the release owner adds `"food-brand-inventory": [1, 2, 3, 4]`, bumps the version and tags the release.

* **Frame:** the same as Pharmaceutical and Coffee roasting. `build.py` uses `tools/automotive/frame_auto.py` on the shared Watch and Try it frame (`tools/electronics/frame.py`, built on the Brewery scaffold with the 716 by 640 window, step arrows, ripple hotspots, Studio badge and popover, Replay, aria labels, reduced motion). It changes the key and label and moves the first action to 900 ms.
* **Build:** `python3 tools/food-brand-inventory/build.py` rebuilds all four, or pass card numbers.
* **Cards** (each layout used once, each background used once):
  1. Stock at Every Location, record form with a side summary. Background 1.
  2. Outsourced Production Orders, list and detail. Background 2.
  3. Shelf Life & Retailer Dating, board (lots move between Lots on hand, Pick list and On hold by click). Background 3.
  4. Reorder Planning & Demand, stage chain with running totals. Background 4.
* **Read only demos:** every input (Trail Mix Case on card 1, Greenfield Grocers and 120 days on card 3, PO-7760 on card 4) is prefilled, `readonly`, `tabindex="-1"`, gray, with no pointer events. No typing, no typing animation, no sample buttons, no error messages. Quantities are preset chips (card 1 transfer 500, 1,000, 1,500; card 2 receipt 1,900, 1,950, 2,000). On those two steps the prompt points at the chip first, then at Transfer or Receive.
* **Tests:** `test_card1.py` to `test_card4.py` run the Automotive harness through `fb_tests.py`. Each first asserts every sum, conversion and percentage from the page README in Python, then checks the start screen (prefilled read only inputs, no editable input, textarea or contenteditable, nothing derived shown), timing, Watch and Try it with every caption and number, Replay, the toggle, the arrows, the Studio popover by click and touch, reduced motion, both window edges at four widths, the control row at five widths, every step at 390 and 340 px, a text scan (dashes, "recipe", claim and certification words, real retailer and carrier names), the card size and the background standard, plus a keyboard only walk and a mouse only walk at 604 and 358 px.
* `shots.py N [card widths]` steps one card through Try it and saves a screenshot per step.
* `tools/automotive/check_demo_ui.py` clicks the hint once per step, so it reports cards 1 and 2 as not reaching Done: their chip steps take two clicks by design. `tools/check_click_only.py food-brand-inventory` (which allows multi click steps) passes all four.

Run with `pip install playwright pillow` first. Set `PW_CHROME` to use a Chromium binary already on the machine. Screenshots go to `GFX_SHOTS` (default `/tmp/fb_shots`).

**Numbers note:** card 1 compares the partner's last report (3,100, Nov 17) with on hand on that date (3,400, before the transfer), so the difference is 300 as the README asks even though the co-packer holds 2,400 after the transfer.

The backgrounds are copies of `graphics/food-co-packing/bg-1.jpg` to `bg-4.jpg` (604 by 540, progressive JPEG, about 50 KB). All names, quantities and readings in these demos are invented sample data for illustration.
