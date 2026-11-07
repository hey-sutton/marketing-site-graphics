# Distribution graphics

Four interactive product demos for `/industries/distribution-management-software` (Graphic Key `distribution-management-software`). The company is Ridgeway Supply, a distributor with two warehouses, Atlanta (WH-ATL) and Dallas (WH-DAL). The items are shared across the cards, so each card picks up where the last one stopped. All data is invented and illustrative, and every company name is made up.

The source of truth is `tools/distribution/`. Edit the generator there, rebuild, test, then open a pull request. Don't hand edit `card-N.js`.

## How each card runs

Each card has one step list, and it runs in two modes, the same engine as Electronics and Apparel (Simon, November 6, 2026).

* **Watch** is the default. The steps run on their own with a gray `Watching n of N` pill, and the card loops.
* **Try it** starts when the reader clicks the product window or picks `Try it` in the toggle. It restarts at step 1 with a yellow `Your turn n of N` pill. A dimmed screen, a pulsing target, a prompt and a caption guide each step, and the pill turns green at `Done`.
* **Shared controls:** Replay, the step arrows and the toggle work in both modes.
* **Reduced motion:** the card starts in Try it and nothing plays on its own.

## The four cards

| Card | Layout | Steps |
|---|---|---|
| 1 Inventory Control & Planning | Bin map of both warehouses, item list and stock moves; SKU panel with Locations, Availability and Plan tabs; transfer and delivery forms | Find SKU (GL-210, prefilled), Availability tab, Low stock, Transfer (30 boxes Dallas to Atlanta, prefilled), Scan delivery in (PO-4402, 120 boxes, prefilled), Plan tab |
| 2 Lot & Serial Traceability | Supply network map (suppliers, warehouses, customers) with the traced path drawn bold; trace form, activity log, unit or lot panel | Trace serial (SN-7714), Open lot (L-24091), Where it is now, Place on hold, Export customer list |
| 3 Procurement Management | Reorder suggestions grouped by vendor, approval rules and purchase orders; status strip, purchase order and landed cost panel | Reorder suggestions, Create PO (200 at 4.10, ship to Atlanta, prefilled), Send for approval, Approve as purchasing manager, Receive delivery (120 of 200, prefilled), Add freight and duty (96.00 and 24.00, prefilled) |
| 4 Advanced Order Management | Order inbox with channel chips (Rep, Portal, Marketplace, EDI); order detail with its price list; pick route with scanning and a shipping panel | All channels, open SO-6201, Release to pick, Scan item (TW-331, flagged), Scan correct items, Pack and ship (1 pallet, LTL, prefilled) |

## Numbers the cards compute

The tests assert every one of these.

* **Card 1.**
  * GL-210 bins: 120 + 60 + 40 = 220 on hand. Available to sell: 220 − 150 = 70.
  * Low stock: 3 of 5 items are below their reorder point (GL-210 70 vs 100, BT-118 40 vs 80, PK-077 18 vs 40).
  * Transfer TO-0931: Atlanta 180 + 30 = 210, Dallas 40 − 30 = 10, still 220 in all.
  * Delivery PO-4402: 220 + 120 = 340 on hand, 340 − 150 = 190 available, so the low stock flag clears.
  * Plan: BT-118 160 + 80 − 40 = 200 units, PK-077 90 + 40 − 18 = 112 rolls.
* **Card 2.**
  * Lot L-24091: 120 + 80 + 100 + 60 = 360 shipped of 400 received, so 40 remain.
  * On the shelf: Atlanta A-04-2 30 + Dallas D-02-3 10 = 40.
  * Hold: GL-210 available to sell drops from 190 to 150.
* **Card 3.**
  * PO-4410: 200 × 4.10 = 820.00, over the 500.00 approval limit.
  * Receiving: 120 of 200, 80 still on order, BT-118 on hand 60 to 180.
  * Landed cost: (96.00 + 24.00) / 120 = 1.00 a unit, 4.10 + 1.00 = 5.10, 120 × 5.10 = 612.00. The order value stays 820.00.
* **Card 4.**
  * SO-6201: 24 + 12 + 6 = 42 pieces in 3 stops.
  * Amounts: 24 × 7.40 = 177.60, 12 × 18.00 = 216.00, 6 × 9.50 = 57.00, total 450.60.
  * Contract saving: 24 × (8.50 − 7.40) = 26.40.
  * No stock figures are shown after shipping.

The backgrounds `bg-1.jpg` to `bg-4.jpg` are unchanged from the October cards.
