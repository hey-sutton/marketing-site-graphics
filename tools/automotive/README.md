# Automotive graphics: generator and tests

This folder is the source for `graphics/automotive/card-1.js` to `card-4.js`. The Graphic Key is `automotive`.

* **Frame and engine:** the shared Watch and Try it frame in `tools/electronics/frame.py`, through `frame_auto.py`, which adds the November 11, 2026 UI rules without changing the shared frame for other industries:
  * Replay is an icon only button (circular arrow, `aria-label` and `title` "Replay").
  * The control row runs Studio chip, Watch and Try it toggle, step counter, Replay at every width. Under 600 px of card width it wraps to two lines: Studio and Replay on line 1, the toggle and the counter on line 2, with the previous and next arrows either side of the counter. These controls are drawn at a fixed CSS size outside the scaled window, 40 CSS px or more, so they work by touch at 390 and 340 px.
  * The window keeps its 716 by 640 size and bleeds past the card's right and bottom edges at every width. Under 600 px the card visual gets taller so the window starts below the two control lines.
  * The Studio popover keeps its four examples and three rows on a phone, set smaller. Its "Get help" row says "From the Sutton team" (no plan wording).
  * No side nav and no profile on any card. Every window starts with the same header from `frame_auto.header()`: icon, title, subtitle.
* **Build:** `python3 tools/automotive/build.py` rebuilds all four, or pass card numbers.
* **Cards:** `card1.py` to `card4.py` each hold one card: CSS, window HTML, data, render code and the step list.
* **Tests:** `test_card1.py` to `test_card4.py` run `auto_tests.py` (built on `tools/electronics/testlib.py`). Each first asserts the brief's numbers in Python, derived independently of the card, then checks in the browser:
  * the start screen shows nothing derived from the input, the walkthrough starts within 1.5 s and the first result is up within 4 s
  * Watch, the take over, Try it with a wrong click and an invalid input, every caption and every number, the arrows, Replay, the toggle, the Studio popover and reduced motion
  * typing works and Enter submits (card 1); invalid dates and splits show inline errors (cards 2 and 4)
  * the window runs past the right and bottom edges at 1300, 1024, 768 and 390 px with a square corner and no empty band
  * the control row at card widths 604, 480, 390, 358 and 340: order, two lines under 600 px, 40 px targets, inside the card, uncovered, no overlap, and Studio, Try it, the arrows and Replay by tap
  * every step at 390 and 340 px, a text scan (dashes, "Digit", "recipe", price, plan or trial wording, claim words, real OEM and supplier names), card size and the background standard
* **UI check on preview pages:** `check_demo_ui.py --html previewN.html --widths 1300 390 340` and `check_demo_ui.py --cards preview1.html preview2.html preview3.html preview4.html` (nav and profile the same on all four, the same header). Widths under 640 are card widths. It also runs Try it through every step and fails on colliding text inside the window.
* `shots.py N [card widths]` steps one card through Try it and saves a screenshot per step.

Run with `pip install playwright pillow` first. Set `PW_CHROME` to use a Chromium binary already on the machine. Screenshots go to `GFX_SHOTS` (default `/tmp/automotive_shots`).

Preview page: `python3 tools/electronics/make_preview_page.py --card graphics/automotive/card-1.js --bg graphics/automotive/bg-1.jpg --out preview1.html`.

All data in the cards is illustrative.
