# Dairy graphics: generators and tests

Source for `graphics/dairy/card-1.js` to `card-4.js`. Edit the generator, rebuild, test, then open a pull request.

* `build_card1.py` builds card 1 (Milk Lot Traceability). `build.py` builds cards 2 to 4 from `card2.py`, `card3.py` and `card4.py` with `gfx_scaffold.py`.
* Rebuild: `GFX_REPO=<checkout that contains graphics/brewery/card-1.js> GFX_OUT=<output checkout> python3 build.py` (and `build_card1.py` for card 1).
* Test (needs playwright and pillow): `GFX_OUT=<checkout with graphics/dairy, manifest.json and loader.html> GFX_SHOTS=/tmp/shots python3 test_card1.py` and `test_card2.py` to `test_card4.py`.
* The tests check the numbers each card computes, the empty start screen, the arrows and hotspots, reduced motion, the speed target, and the layout rules (right and bottom edge hidden, square bottom right corner, no empty band, background standard) at 1300, 1024, 768 and 390 px.
* All data in the cards is illustrative.
