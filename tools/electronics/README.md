# Electronics graphics: generator and tests

This folder is the source for `graphics/electronics/card-1.js` to `card-4.js`.

* `frame.py` holds the shared frame and the Watch and Try it engine. The frame is the Brewery card's frame at 716 by 640, built through `tools/dairy/gfx_scaffold.py`, with a squared bottom right corner, step arrows and ripple hotspots. To change how the cards feel, edit the `TUNE` object at the top of the engine: start delay, cursor lead, dwell per step, hold before the loop, delay before the next prompt, and the pill words.
* `card1.py` to `card4.py` each hold one card: window HTML, CSS, data, render code and the step list. Every step is written once, as `{id, target(), prompt, run(), after, back(), ok()}`. Watch mode calls `run()` after moving the cursor to `target()`. Try it mode calls `run()` from the reader's click. `back()` points the prompt to a way back when the reader leaves the screen the step needs. `ok()` validates the prefilled inputs and shows an inline error.
* `build.py` rebuilds the cards: `python3 tools/electronics/build.py` for all four, or pass card numbers (`python3 tools/electronics/build.py 2 4`).
* `test_card1.py` to `test_card4.py` run the click through on `testlib.py`. Each one checks:
  * both modes, the take over, every step's caption and numbers, a wrong click, invalid input, Replay, the toggle and the arrows
  * reduced motion and the Studio popover
  * layout at 1300, 1024, 768 and 390 px: right and bottom edge hidden, a square corner, no empty band
  * the 340 px top bar and popover, and every step at 390 px
  * a text scan for dashes, "Digit", "recipe" and claim words
  * card size
* `make_preview_page.py` builds a review page for one card, with a desktop and phone width switch.

Run a test with `pip install playwright pillow` first, then `python3 tools/electronics/test_card1.py`. Set `PW_CHROME` to use a Chromium binary already on the machine. Screenshots go to `GFX_SHOTS`, which defaults to `/tmp/electronics_shots`.

The repo harness works too: `python3 tools/test_graphics.py --repo . --key electronics`.

All data in the cards is illustrative.
