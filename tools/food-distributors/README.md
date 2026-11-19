# Food distributors graphics: generator and tests

Source for `graphics/food-distributors/card-N.js`, page /industries/food-distributors, Graphic Key `food-distributors`. So far only card 4 is built. Cards 1 to 3 are still to come. The key is not in `manifest.json` yet. The release owner adds `"food-distributors": [1, 2, 3, 4]` after all four cards are merged, bumps the version and tags the release on the merged main commit.

* **Frame:** the same as Functional beverage. `build.py` uses `tools/automotive/frame_auto.py` on the shared Watch and Try it frame (`tools/electronics/frame.py`, 716 by 640 window, step arrows, ripple hotspots, Studio badge and popover, Replay, aria labels, reduced motion), with the first action at 900 ms.
* **Build:** `python3 tools/food-distributors/build.py 4`.
* **Card 4: Scan Verified Picking & Shipping.** Board layout (pick list column, scan panel, shipment column, running totals strip). Background 4.
  1. Open pick list: SO-3110's three lines, entered as Penne, Lime, Lavender, are sorted into bin order A-02-1, A-04-2, B-12-3.
  2. Scan item: the Lime case matches A-02-1, so the line turns green (40 cases).
  3. Scan item: the Lime barcode is scanned for the Lavender line. The warning names both items and shows both pictures, and the line stays open.
  4. Complete pick, which takes 3 clicks in Try it: scan the Lavender case, scan the Penne case (both marked `data-pick`), then Complete pick. 270 cases picked. On hand Lime 500 to 460, Lavender 300 to 270, Penne 700 to 500. In Watch, the two rescans play as the cursor moves to Complete pick.
  5. Generate: Packing slip PS-3110 and Bill of lading BOL-3110.
* **Read only demos:** the sales order (SO-3110) and the case barcode are prefilled, `readonly`, `tabindex="-1"`, gray and ignore the pointer. The barcode shows the case in hand for the current line. There's no typing, no typing animation, no sample buttons and no input errors.
* **Tests:** `test_card4.py` (through `fd_tests.py`, the Automotive harness) first asserts the README's numbers in Python: ascending bin order, 40 + 30 + 200 = 270, each on hand falls by its picked quantity, and valid, distinct UPC check digits. Then it checks the start screen, timing, Watch and Try it with every caption and number, that a wrong scan never confirms a line and Complete pick stays disabled, Replay, the arrows, the Studio popover, reduced motion, edges at four widths, 390 and 340 px, a keyboard only walk, and a mouse only walk at 604 and 358 px (Done in 7 clicks).
* `shots.py 4 [card widths]` saves a screenshot per step.

Run with `pip install playwright pillow`. Set `PW_CHROME` to a Chromium binary already on the machine.

The background is a copy of `graphics/functional-beverage/bg-4.jpg` (604 by 540, progressive JPEG, about 50 KB). All names, quantities and readings are invented sample data for illustration.
