# Footwear graphics: generator and tests

This folder is the source for `graphics/footwear/card-1.js` to `card-4.js`. The Graphic Key is `footwear`.

* **Frame and engine:** shared with Electronics, Apparel, Distribution, Plastics and Recycling, in `tools/electronics/frame.py`, with the app shell (`shell=True`) and the phone layout (`phone=True`). `build.py` swaps the shell's modules for footwear ones: Inventory, Production, Purchasing, Sales, Costing, Reports.
* **Build:** `python3 tools/footwear/build.py` rebuilds all four, or pass card numbers.
* **Cards:** `card1.py` to `card4.py` each hold one card: CSS, data, render code for every screen at desktop and phone width, the step list and `STORY`, the storyboard the variety test reads.
* **Tests:** `test_card1.py` to `test_card4.py` run the shared harness (`tools/electronics/testlib.py`) through `footwear_tests.py`. Each test first asserts the brief's numbers in Python, derived independently of the card (half up rounding with `Decimal`), then checks in the browser:
  * Watch and Try it, the take over, every caption and number, a wrong click, invalid input, Replay, the toggle, the step arrows, the Studio popover and reduced motion
  * the start screen shows nothing that depends on the input; the walkthrough starts within 1.5 s and the first result is up within 4 s
  * typing works and Enter submits (cards 1 and 4)
  * layout at 1300, 1024, 768 and 390 px: the window runs past the card's right and bottom edges, the bottom right corner is square, no empty band; under 520 px of card width the phone layout
  * a navigation walk at 1300, 768, 480, 390 and 340 px card widths: screen, breadcrumb and nav follow the storyboard; on the phone every target is inside the window, captions are one line and nothing overflows or is cut off
  * a text scan for dashes, "Digit", "recipe", market size words, concept or illustrative tags and real shoe brands
* `shots.py N [card widths]` steps one card through Try it and saves a screenshot per step, for a quick look.

Run with `pip install playwright pillow` first, then `python3 tools/footwear/test_card1.py`. Set `PW_CHROME` to use a Chromium binary already on the machine. Screenshots go to `GFX_SHOTS` (default `/tmp/footwear_shots`).

Review page: `python3 tools/electronics/make_preview_page.py --card graphics/footwear/card-1.js --bg graphics/footwear/bg-1.jpg --out preview.html`.
