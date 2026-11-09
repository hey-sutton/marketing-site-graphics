# Plastics graphics

Four interactive product demos for `/industries/plastics` (Graphic Key `plastics`). The plant is Ridgeway Plastics, a molder, and the product is CAP-38, a 38 mm black closure cap at 0.0275 lb per part. The cards share items and numbers, so each card picks up where the last one stopped. All data is invented and illustrative, and every company name is made up. Weights are in pounds.

The source of truth is `tools/plastics/`. Edit the generator there, rebuild, test, then open a pull request. Don't hand edit `card-N.js`.

## How each card runs

Each card has one step list, and it runs in two modes, the same engine as Electronics, Apparel and Distribution (Simon, November 6, 2026).

* **Watch** is the default. The steps run on their own with a gray `Watching n of N` pill, and the card loops.
* **Try it** starts when the reader clicks the product window or picks `Try it` in the toggle. It restarts at step 1 with a yellow `Your turn n of N` pill. A dimmed screen, a pulsing target, a prompt and a caption guide each step, and the pill turns green at `Done`.
* **Shared controls:** Replay, the step arrows and the toggle work in both modes.
* **Reduced motion:** the card starts in Try it and nothing plays on its own.

There is no machine monitoring in these cards: no cycle time, downtime, energy, telemetry or OEE. Card 3 is operator logging and output only.

## The four cards

| Card | Layout | Steps |
|---|---|---|
| 1 BOMs, Blends & Cost Roll-Up | BOM tree (carton, cap, compound, materials) and the runs on the BOM; Blend, Cost and Versions tabs; material prices | Open BOM (CAP-38, prefilled), Scale to batch (1,000 lb, prefilled), Cost tab, Apply +10% on PP-100 (prefilled), Open runs affected, Save as new version |
| 2 Resin Lot Traceability | Left to right trace diagram (material lots, runs, finished lots, customers or stock); trace form, activity log and a detail panel | Trace back (FL-7714, prefilled), Open lot L-55120, Trace forward, Where it is now, Place on hold, Export customer list |
| 3 Production Runs & Output | Run form and work order routing strip, press cards, output log and an expected vs actual panel | Release run (RUN-7720, 40,000 caps, Press 4, mold M-0412, prefilled), Log shift 1 (prefilled), Log shift 2 (prefilled), Expected vs actual, Complete run |
| 4 Shortages & Resin Purchasing | Status strip, planning grid with coverage bars, demand by run; purchase order, approval rules and recent receipts | Shortages only, the PP-100 row, Create PO (Northfield Polymers, 14,000 lb at 0.74, prefilled), Send for approval, Approve as purchasing manager, Receive 6 gaylords (lot L-55212, prefilled) |

## Numbers the cards compute

The tests assert every one of these.

* **Card 1.** Weights to 0.1 lb, money to cents (half up).
  * Batch of 1,000 lb: 925.0 + 25.0 + 5.0 + 45.0 = 1,000.0 lb. PP-100 is 0.925 of a 1,000 lb gaylord.
  * Cost: 684.50 + 53.75 + 20.50 + 13.50 = 772.25, which is 0.77225 a lb.
  * Per 1,000 caps: 27.5 × 0.77225 = 21.236875, shown as 21.24. Then 21.24 + 6.10 + 9.00 = 36.34.
  * PP-100 up 10% to 0.814: 752.95 + 53.75 + 20.50 + 13.50 = 840.70. Compound 27.5 × 0.8407 = 23.12, total 38.22, up 1.88.
  * Runs: RUN-7712 1.88 × 20 = 37.60, RUN-7716 1.88 × 30 = 56.40, 94.00 together.
* **Card 2.** Whole pounds and whole caps.
  * L-55120: 5,000 + 6,500 + 3,000 = 14,500 lb used, 20,000 − 14,500 = 5,500 lb left (2,500 + 3,000 in two bins).
  * Customers: Alder Beverage 220,000, Pinewood Foods 100,000, Harbor Dairy 165,000, so 485,000 shipped.
  * Finished: 180,000 + 235,000 + 110,000 = 525,000. 525,000 − 485,000 = 40,000 on hand in FG-1.
* **Card 3.** Caps whole, compound to 0.1 lb, regrind to 0.01 lb.
  * Shifts: 18,500 + 700 = 19,200 and 20,200 + 600 = 20,800, so 40,000 molded.
  * Totals: 38,700 good and 1,300 scrap.
  * Compound: 40,000 × 0.0275 = 1,100.0 lb expected, 1,112.5 lb issued, over by 12.5 lb.
  * Regrind: 1,300 × 0.0275 = 35.75 lb.
* **Card 4.** Whole pounds, money to cents.
  * Net: PP-100 11,000 − 24,500 = −13,500, COL-BLK −190, UV-02 2, CTN-1000 120.
  * PP-100 demand: 1,100 + 9,200 = 10,300 fits the 11,000 on hand. Adding RUN-7725 makes 18,700, so it is the first run short.
  * PO-4520: 14,000 × 0.74 = 10,360.00. Once sent, the net is 11,000 + 14,000 − 24,500 = 500.
  * After 6 gaylords: on hand 17,000, on order 8,000, net still 500.

The backgrounds `bg-1.jpg` to `bg-4.jpg` are copies of `features-traceability` backgrounds 1, 2, 3 and 6. They are four different landscapes, and neither Packaging nor Additive Manufacturing uses any of them.
