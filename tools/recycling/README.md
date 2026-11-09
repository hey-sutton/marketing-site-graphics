# Recycling graphics: generator and tests

This folder is the source for `graphics/recycling/card-1.js` to `card-4.js`. The Graphic Key is `recycling`.

* **Frame and engine:** shared with Electronics, Apparel, Distribution and Plastics, in `tools/electronics/frame.py`. These are the first cards to opt in to two frame options. A card that doesn't pass these options is built exactly as before.
  * **`shell`:** the app shell. A left nav of six modules (Receiving, Processing, Inventory, Sales, Shipping, Reports), a breadcrumb row and a page header with a status chip.
    * Each screen renders into `#pg`.
    * The card calls `setNav({...})`, which moves the active nav item, the breadcrumb, the title and the chip, and sets `data-scr` on the window.
  * **`phone`:** the phone layout, under 520 px of card width.
    * The card visual becomes a phone stage: square up to 400 px, then 1 to 0.88 as tall from 401 to 520 px.
    * The window is laid out to the stage at a scale of 0.95, with the step arrows in a strip under it.
    * The nav becomes a bottom bar of six icons, and captions are one line at the top of the screen.
    * Each card renders its own phone screens when `ph()` is true. A step's `pc` is its short phone caption.
* **Build:** `python3 tools/recycling/build.py` rebuilds all four, or pass card numbers. It wraps each card's screens in `frame.shell(...)` and passes `shell=True, phone=PHONE`. Set `PHONE = False` in `build.py` to ship the shrink to fit version instead.
* **Cards:** `card1.py` to `card4.py` each hold one card: CSS, data, render code for every screen at desktop and phone width, and the step list.
  * Every step is `{id, target(), prompt, run(), after, back(), ok(), pc}`.
  * `STORY` is the card's storyboard: screen, module, target type and position for each step. The tests read it.
* **Tests:** `test_card1.py` to `test_card4.py` run the shared harness in `tools/electronics/testlib.py`, set up by `recycling_tests.py`. They check:
  * both modes, the take over, every caption and number, a wrong click, invalid input, Replay, the toggle and the arrows
  * reduced motion and the Studio popover, and the 340 px top bar and popover
  * layout at 1300 and 768 px with the window running past the card edges; at 1024 px (a 480 px card) and 390 px, the phone stage
  * variety: `variety_check.py` rules run on each card's `STORY`
  * a navigation walk at 1300, 480 and 390 px:
    * after every step, the screen, breadcrumb and active nav item match the storyboard
    * navigation steps change all three
    * on the phone, every target sits inside the window, captions are one line, and nothing overflows sideways or is cut off at the bottom
  * a real pointer drag for the drag and drop steps (cards 2 and 3), at desktop and phone width
  * a text scan for dashes, "Digit", claim words (EPA, DOT, compliance, hazardous, cash, ID scan, market price), scale makers and real company names
* **Storyboards:** `storyboards.md` holds the storyboard tables from the brief. `python3 tools/recycling/variety_check.py tools/recycling/storyboards.md` checks them.

Run a test with `pip install playwright pillow` first, then `python3 tools/recycling/test_card1.py`. Set `PW_CHROME` to use a Chromium binary already on the machine. Screenshots go to `GFX_SHOTS` (default `/tmp/recycling_shots`).

To build a review page: `python3 tools/electronics/make_preview_page.py --card graphics/recycling/card-1.js --bg graphics/recycling/bg-1.jpg --out preview.html`.

All data in the cards is illustrative.
