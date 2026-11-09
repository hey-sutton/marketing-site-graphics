# Furniture and woodworking graphics: generator and tests

This folder is the source for `graphics/furniture-woodworking/card-1.js` to `card-4.js`. The Graphic Key is `furniture-woodworking`.

* **Frame and engine:** the shared Watch and Try it frame in `tools/electronics/frame.py`, with the app shell (`shell=True`) and the phone layout (`phone=True`) that Recycling introduced. `build.py` swaps in the shop's own six modules (`frame.MODS`).
* **Build:** `python3 tools/furniture-woodworking/build.py` rebuilds all four, or pass card numbers.
* **Cards:** `card1.py` to `card4.py` each hold one card: headline, CSS, data, render code for desktop and phone, the step list and `STORY` (screen, module, target type, position per step). Card 1 narrows the nav to icons so the calendar gets the width. Card 3's step 3 takes three clicks (White oak, 72 in, Matte lacquer); its `ok()` picks one option per click and the step moves on when all three are set.
* **Tests:** `test_card1.py` to `test_card4.py`, set up by `furniture_tests.py`, which reuses the shared harness (`tools/electronics/testlib.py`) and the Recycling shell and phone checks (`tools/recycling/recycling_tests.py`). They check:
  * Watch and Try it, the take over, every caption and computed number, a wrong click, invalid input, Replay, the toggle, the arrows, reduced motion and the Studio popover
  * layout at 1300, 1024, 768 and 390 px (right and bottom edges hidden, square bottom right corner, no empty band) and the 340 px top bar
  * the phone stage at 390 and 480 px: every target inside the phone window, one line captions, nothing cut off
  * the navigation walk: screen, breadcrumb and active nav item after every step
  * variety (`tools/recycling/variety_check.py`), real typing with Enter on cards 2 and 4, the start screen rule, and a text scan for dashes, "recipe", "Digit", market size words, concept or illustrative tags and CAD product names
  * card 3 prices all 27 option combinations against the formula
* One variety rule is reported but not failed: on card 3 the brief puts "Create sales order" at step 5 of 8, before the last three steps.

Run a test with `pip install playwright pillow` first, then `python3 tools/furniture-woodworking/test_card1.py`. Set `PW_CHROME` to use a Chromium binary already on the machine. Screenshots go to `GFX_SHOTS` (default `/tmp/furniture_shots`).

To build a review page: `python3 tools/electronics/make_preview_page.py --card graphics/furniture-woodworking/card-1.js --bg graphics/furniture-woodworking/bg-1.jpg --out preview.html`.

All data in the cards is illustrative.
