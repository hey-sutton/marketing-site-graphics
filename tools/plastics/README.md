# Plastics graphics: generator and tests

This folder is the source for `graphics/plastics/card-1.js` to `card-4.js`. The Graphic Key is `plastics`.

* **Frame and engine:** shared with Electronics, Apparel and Distribution, in `tools/electronics/frame.py`. `build.py` points it at the plastics key. To change how the cards feel (timing, pill words), edit the `TUNE` object in that frame. The change applies to every industry on the frame, so rebuild them all and run all their test sets.
* **Cards:** `card1.py` to `card4.py` each hold one card: window HTML, CSS, data, render code and the step list. Every step is `{id, target(), prompt, run(), after, back(), ok()}`. The rounding rule for each card is in its docstring.
* **Build:** `python3 tools/plastics/build.py` rebuilds all four, or pass card numbers.
* **Tests:** `test_card1.py` to `test_card4.py` run the shared harness in `tools/electronics/testlib.py`, set up by `plastics_tests.py`. They check:
  * both modes, the take over, every caption and number, a wrong click, invalid input, Replay, the toggle and the arrows
  * the neutral start screen: inputs prefilled, derived results hidden until their step
  * reduced motion and the Studio popover
  * layout at 1300, 1024, 768 and 390 px, the 340 px top bar and popover, and every step at 390 px
  * a text scan for dashes, "Digit", "recipe", "formula", compliance and certification names, machine monitoring words, size words, prices with a dollar sign, and real resin brands and customers

Run a test with `pip install playwright pillow` first, then `python3 tools/plastics/test_card1.py`. Set `PW_CHROME` to use a Chromium binary already on the machine. Screenshots go to `GFX_SHOTS` (default `/tmp/plastics_shots`).

To build a review page: `python3 tools/electronics/make_preview_page.py --card graphics/plastics/card-1.js --bg graphics/plastics/bg-1.jpg --out preview.html`.

All data in the cards is illustrative.
