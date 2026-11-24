# marketing-site-graphics

Interactive product graphics for the Sutton marketing site. Webflow loads them from here through jsDelivr. This repo is public by design, so never put anything internal in it.

## How it works

1. The Industries template in Webflow has one small loader embed (see `loader.html`).
2. The loader reads the page's Graphic Key from the `data-sx-industry` attribute (bound to the Graphic Key field in the Industries CMS) and falls back to the URL slug.
3. It fetches `manifest.json`. After the page finishes loading it downloads the listed card files quietly in the background, then mounts each graphic when its card is within about 1,600 pixels of the screen. A failed download is retried up to three times, and each graphic fades in over the card photo.
4. Each file mounts its graphic into the matching card visual. If anything fails to load, the card shows its normal CMS image.

Page weight stays flat no matter how many industries we add.

## Layout

```
manifest.json                      which cards have a graphic, per Graphic Key
loader.html                        the embed pasted into Webflow (one copy, in the template)
graphics/<key>/card-<n>.js         one file per graphic, n is the card number 1 to 4
loader-blog.html                   the embed pasted into the Blog Posts Template: maps each blog post to its graphic and wraps it in the Sutton banner frame
assets/                            shared images, for example sutton-logo-color.png (the official logo, used in the blog banner)
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

Every industry gets its own Graphic Key, its own folder, its own four cards and its own backgrounds. Industries never share a graphic, and a child page never reuses its parent's.

**Backgrounds are repo hosted.** Each card's background is a JPG in its folder, `graphics/<key>/bg-<n>.jpg` (604 by 540 pixels, progressive JPEG, about 50 KB, n matches the card number). The card finds it relative to its own script address, so the image ships inside the release tag and does not depend on any Webflow asset. The pattern, copied from `graphics/distribution-management-software/card-2.js`, is `var SRC=document.currentScript&&document.currentScript.src;var BGU=SRC?new URL('bg-2.jpg',SRC).href:'';`, with the CSS holding a `__BG__` placeholder that is replaced with `BGU`. The older Food and beverage and Additive Manufacturing cards still load Webflow hosted backgrounds and will be migrated later.

The `version` in `manifest.json`, the `BASE` tag in `loader.html` and the release tag must all match.

When a graphic moves over from old Webflow embeds, hide those embeds in the template first, check the page, and delete them later. Hiding keeps a way back.

## Feature pages

Feature pages (`/features/<slug>`) are static pages, not CMS items, and they use the same capabilities card classes as the Industries template. Their Graphic Key is `features-<slug>`, for example `features-traceability`, and the folder is `graphics/features-<slug>/`. A feature page can list up to six cards.

The loader is not in a template for feature pages. Each feature page carries it in its own page custom code:

1. Inside `<head>`: `feature-page-head.html`. It sets the demo size before the first paint, so the section does not jump when the graphics load.
2. Before `</body>`: `loader.html`, unchanged. The loader reads the key from the `/features/<slug>` address. A page can also set it with `data-sxg-key` on any element or `window.SXG_KEY`.

A feature page can also have an interactive hero. List `"hero"` after the card numbers in the manifest (for example `[1, 2, 3, 4, 5, 6, "hero"]`) and add `hero.js` plus `hero-bg.jpg` to the folder. The loader mounts it into `.feature-hero_visual` after the page has finished loading, so the hero image stays the page's first paint. Set the page's Hero Background in Webflow to the same clean landscape, so visitors never see an old screenshot before the demo fades in.

When the loader version changes, update it on every feature page that carries it, as well as in the Industries template.

## Rules

* Pin the loader to a tag, never `main`. jsDelivr caches branches for hours, and an unreviewed push would go live.
* Changes reach `main` only through a pull request.
* To roll back, point the loader's `BASE` at the previous tag.
* No secrets, customer names or internal data. Graphic data is illustrative.
* Keep ranking copy in native Webflow fields. These graphics are visual only.

## Demo card rules

These hold for every new card built on the shared frame (`tools/electronics/frame.py`). The reference build is `tools/distilleries`: copy it for a new industry and change the key, label, company name, Studio chips and the four card files.

* **What the card shows.** The Studio chip and popover (four example chips, rows "Built on", "Change" and "Get help: From the Sutton team"), the Watch and Try it toggle, Replay, the ghost cursor, the ripple on the next target, captions, and the yellow prompt inside the window in Try it mode.
* **What it does not show (since November 24, 2026).** No step arrows, no status pill (Watching, Your turn, Done) and no app module nav (the side nav on desktop, the icon bar on phones). The window shows only the app screen with its breadcrumb and header. No plan or tier wording, and no "Concept screen", "Live demo" or "Illustrative" tags.
  * Hide them in the industry's own `build.py`, the way `tools/distilleries/build.py` does (`.stp,.tbar .mode{display:none!important}` and `.rail,.bn{display:none!important}` with a one column `.app`). Don't edit the shared frame for one industry; other industries still use it as it is.
  * Cards built before Distilleries still show the arrows and the pill. Their arrows follow the older rule: the frame's `placeStp()` keeps them inside cards shorter than 604 by 540, and `testlib.run_card` checks that.
* **Phone layout.** Under 520 px of card width (measured on the card, not the viewport) the card becomes a phone stage: square up to 400 px, then 1 to 0.88 tall from 401 to 520 px, with the window laid out at a fixed scale of 0.95 and about 10 px of photo at the sides and bottom. Each step has its own compact phone screen (three column tables, an opened item as its own screen with a back button, one line captions), controls are 40 px tap targets, and short screens get a few rows of real detail instead of an empty band. Test at 340, 390 and 480 px as well as 768, 1024 and 1300.
* **Window edges.** On desktop the window runs past the card's right and bottom edges at 1300, 1024, 768 and 390 px, and the card's bottom right corner is square.
* **Numbers.** Every sum in the brief is asserted in Python before the build (`tools/distilleries/numbers_check.py`), and the tests read each number off the screen.
* **Size.** Each card file is 40 to 65 KB, never above 80 KB. `prune()` in `tools/distilleries/build.py` drops scaffold CSS a card never uses.
* **Release tags start with `v`** (for example `v1.26.2`). The loader's `BASE` is built around `@v...`, and the tag must be on the merged `main` commit whose `manifest.json` version matches it. Bump the version in the same pull request as the cards, and push every commit before it is merged.

## After a release

jsDelivr pulls each file from GitHub the first time anyone requests it, and that first request can be slow or fail. After creating a release, open each industry page once. The loader downloads that page's files, which warms the CDN so the first real visitor doesn't wait.

## Debugging

Add `?sxgdebug=1` to any industry page URL. A black box at the bottom of the screen lists what the loader did: the key it found, whether the manifest loaded, each card's load, retries and the server's answer to any failure. Visitors never see it.

## The loader and this repo

`loader.html` here is a copy of the embed in the Webflow Industries template. Webflow holds the live one, so when you change the loader, change both. Only the version in `BASE` needs to change for a new release.
