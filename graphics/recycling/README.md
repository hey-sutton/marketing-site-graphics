# Recycling graphics

Four interactive product demos for `/industries/recycling` (Graphic Key `recycling`). The company is Cedar Valley Recycling, a processor of plastic scrap into regrind and bales. The cards share loads, lots and IDs, so each one picks up where the last stopped. All data is invented and illustrative, every company name is made up, and weights are in pounds.

The source of truth is `tools/recycling/`. Edit the generator there, rebuild, test, then open a pull request. Don't hand edit `card-N.js`.

## What is new in these cards

* **They move between screens.** Each card runs inside a mini app with a nav of six modules, a breadcrumb row and a page header.
  * Each card visits five screens.
  * Its clicks land on rows, fields, tabs, toggles, menus, nav items, map and heatmap cells, a breadcrumb and drag and drop.
  * There is at most one primary button per card, always near the end.
* **A phone layout.** Under 520 px of card width the card shows a phone app rather than the desktop window shrunk down:
  * one column and a bottom bar of nav icons
  * a back button on detail screens and three column tables
  * one line captions, with the step arrows under the screen

The Watch and Try it engine is the same as the other industries. Watch plays the steps with a gray `Watching n of N` pill. A click inside, or the toggle, switches to Try it: yellow `Your turn n of N`, then green `Done`. Replay, the arrows and reduced motion work as before.

## The four cards

| Card | Screens | Steps (target) |
|---|---|---|
| 1 Weighed Receiving | Inbound loads, scale ticket, load detail, pallet labels, inventory by grade | Row LD-2291; Use reading on the gross field (41,260 lb, prefilled); Photos and notes tab; Receive without a PO toggle; Print 12 pallet labels in the More menu; Inventory in the nav |
| 2 Sorting & Processing Jobs | New job, job PJ-0318, hand sort, conversion flow, yield report | Drag LD-2291 and LD-2275 into the job; Hand sort tab; Log sort on the pulled out field (1,350 lb, prefilled); Natural regrind node; Reports in the nav; Complete job |
| 3 Stock by Grade, Bin & Age | Inventory by grade (heatmap), aging, bin map, partner aging, move stock | PP mixed color 61 to 90 days cell; Older than 60 days chip; bin Y1-04; Reports in the trail to Harlan Plastics; drag 6,100 lb onto Y2-11 |
| 4 Sell & Ship with Paperwork | Sales orders, order detail, pick, weigh out, documents | Row SO-8841; Use price on the price field (0.46 per lb, prefilled); Scan G-4412; Use weighed amount toggle; Bill of lading tab; Ship and invoice |

## Numbers the cards compute

The tests assert every one of these.

* **Card 1.** 41,260 − 14,980 = 26,280 lb net. 12 pallets × 2,190 = 26,280. PP mixed scrap 41,500 + 26,280 = 67,780 lb.
* **Card 2.**
  * Input: 26,280 + 18,720 = 45,000 lb.
  * Where it went: 1,350 + 32,400 + 9,000 + 2,250 = 45,000.
  * Usable: 32,400 + 9,000 = 41,400, so 41,400 / 45,000 = 92.0%.
* **Card 3.**
  * Grades: 52,400 + 61,300 + 28,900 + 18,200 + 9,800 = 170,600 lb.
  * PP mixed color by age: 11,500 + 8,000 + 6,100 + 3,300 = 28,900, with 6,100 + 3,300 = 9,400 older than 60 days.
  * Harlan Plastics 4,200 of the 9,400.
  * Move: Y1-04 36,800 − 6,100 = 30,700 and Y2-11 14,200 + 6,100 = 20,300.
* **Card 4.**
  * Order: 32 × 1,250 = 40,000 lb, × 0.46 = 18,400.00.
  * Weigh out: 62,540 − 22,220 = 40,320 lb net, × 0.46 = 18,547.20.

The backgrounds `bg-1.jpg` to `bg-4.jpg` are copies of four existing landscapes, each used once: `features-traceability` bg-4 and bg-5, and the shared landscapes 3 and 1 (the same files as `apparel` bg-3 and bg-1).
