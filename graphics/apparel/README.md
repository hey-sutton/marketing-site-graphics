# Apparel graphics

Four interactive product demos for `/industries/apparel` (Graphic Key `apparel`). All four use the same style: crew tee ST-210 in sizes XS, S, M, L and XL and colors Black, Navy and Sand. Each card picks up where the last one stopped. All data is invented and illustrative, and every company name is made up.

The source of truth is `tools/apparel/`. Edit the generator there, rebuild, test, then open a pull request. Don't hand edit `card-N.js`.

## How each card runs

Each card has one step list, and it runs in two modes, the same engine as Electronics (Simon, November 6, 2026).

* **Watch** is the default. The steps run on their own with a gray `Watching n of N` pill, and the card loops.
* **Try it** starts when the reader clicks the product window or picks `Try it` in the toggle. It restarts at step 1 with a yellow `Your turn n of N` pill. A dimmed screen, a pulsing target, a prompt and a caption guide each step, and the pill turns green at `Done`.
* **Shared controls:** Replay, the step arrows and the toggle work in both modes.
* **Reduced motion:** the card starts in Try it and nothing plays on its own.

## The four cards

| Card | Layout | Steps |
|---|---|---|
| 1 Size & Color Matrix | Style panel, size by color grid, materials panel | Generate grid, Low stock, New production run (360 pieces, prefilled), Calculate materials, Release to cutting |
| 2 Fabric Rolls & Dye Lots | Roll list with yardage bars and a movement log; receiving, cutting table and cut order panels | Receive roll (R-4417, prefilled), Allocate to cut, Scan roll R-4417 (flagged), Scan roll R-4411, Return leftover |
| 3 Cut to Pack Production | Stage board (Cut, Sew, At vendor, Pack) with bundle chips, a held strip and a stage log | Create cut ticket, Scan bundles into sewing, Record sewing, Send to finisher, Receive from finisher, Pack |
| 4 Wholesale & Online Orders | Status strip, order form with a size run grid, stock and payment panels | New wholesale order, Reserve stock, Record deposit, Pick with scanning, Pack and ship |

## Numbers the cards compute

The tests assert every one of these.

* **Card 1.**
  * Low stock: 4 of 15 variants are below the reorder point of 15. They are Black L, Navy L, Sand L and Sand XS.
  * RUN-0412 sizes: 30 + 50 + 80 + 150 + 50 = 360 pieces.
  * RUN-0412 colors: 140 + 130 + 90 = 360 pieces.
  * Fabric: 30.0 + 55.0 + 96.0 + 195.0 + 70.0 = 446.0 yd, plus 360 neck labels.
* **Card 2.**
  * On hand: 140.0 + 120.0 = 260.0 yd, then 410.0 yd after receiving R-4417.
  * Allocation: R-4410 gives 140.0 and R-4411 gives 55.0, for 195.0 yd.
  * Used: 192.0 yd, so 3.0 yd goes back to R-4411.
  * End state: R-4411 holds 68.0 yd and on hand is 218.0 yd.
* **Card 3.**
  * Bundles: 12 bundles hold 360 pieces.
  * Sewing: 354 good and 6 held.
  * Finisher: 354 × 0.85 = 300.90, then 350 pass and 4 held.
  * Packing: 7 cartons of 50, and 350 + 6 + 4 = 360.
* **Card 4.**
  * Order: 56 pieces × 11.50 = 644.00.
  * Deposit: 30% is 193.20, leaving 450.80 due.
  * Shipping: 2 cartons of 28.
  * Navy stock after the reservation: 12, 32, 46, 1 and 25.

The backgrounds `bg-1.jpg` to `bg-4.jpg` are the standard industry landscapes, one per card.
