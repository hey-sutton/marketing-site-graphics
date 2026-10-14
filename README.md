# marketing-site-graphics

Interactive product graphics for the Sutton marketing site. Webflow loads them from here through jsDelivr. This repo is public by design, so never put anything internal in it.

## How it works

1. The Industries template in Webflow has one small loader embed (see `loader.html`).
2. The loader reads the page's Graphic Key from the `data-sx-industry` attribute (bound to the Graphic Key field in the Industries CMS) and falls back to the URL slug.
3. It fetches `manifest.json` and, for the cards listed there, loads `graphics/<key>/card-<n>.js` only when that card is within about 800 pixels of the screen. Nothing downloads for graphics nobody scrolls to.
4. Each file mounts its graphic into the matching card visual. If anything fails to load, the card shows its normal CMS image.

Page weight stays flat no matter how many industries we add.

## Layout

```
manifest.json                      which cards have a graphic, per Graphic Key
loader.html                        the embed pasted into Webflow (one copy, in the template)
graphics/<key>/card-<n>.js         one file per graphic, n is the card number 1 to 4
tools/fragments-to-card.py         wraps existing Webflow embed code into a graphic file
```

## Two ways to make a graphic file

* **Standalone.** The file builds its own shadow DOM (see `graphics/food-beverage/card-1.js`). Use this for new graphics.
* **Wrapped embeds.** For graphics that already exist as Webflow embeds, run `tools/fragments-to-card.py` on the embeds, listed in card order. The original code is kept byte for byte and mounted in that order (see `graphics/additive-manufacturing` and `graphics/food-beverage/card-2.js`, `card-4.js`). If the old embeds are still on the page, the file does nothing, so moving a graphic over is safe.

## Add or change a graphic

1. Create a branch and add or edit `graphics/<key>/card-<n>.js`.
2. List the card in `manifest.json` under its key, for example `"food-beverage": [1, 2, 3]`.
3. Open a pull request, review it and merge.
4. Create a release with a new tag, for example `v1.0.1`.
5. In Webflow, change the version in the loader's `BASE` line to the new tag. That one edit goes live for every page.

Two industries can share a graphic by giving them the same Graphic Key in the CMS.

When a graphic moves over from old Webflow embeds, hide those embeds in the template first, check the page, and delete them later. Hiding keeps a way back.

## Rules

* Pin the loader to a tag, never `main`. jsDelivr caches branches for hours, and an unreviewed push would go live.
* Changes reach `main` only through a pull request.
* To roll back, point the loader's `BASE` at the previous tag.
* No secrets, customer names or internal data. Graphic data is illustrative.
* Keep ranking copy in native Webflow fields. These graphics are visual only.
