# Electronics graphics

Four interactive product demos for `/industries/electronics` (Graphic Key `electronics`). The product is a PCS-200 motor controller. All data is invented and illustrative. Company and customer names are made up.

The source of truth is `tools/electronics/`. Edit the generator there, rebuild, test, then open a pull request. Don't hand edit `card-N.js`.

## How each card runs

Each card has one step list, and it runs in two modes (Simon, November 6, 2026).

* **Watch** is the default when the card scrolls into view. Every step runs on its own: the cursor moves, a ripple marks the click, and a caption says what happened. The gray pill reads `Watching n of N`. After the last step the card holds about 2.5 seconds, resets and loops.
* **Try it** starts when the reader clicks anywhere in the product window, or picks `Try it` in the top bar toggle. It restarts at step 1 and the cursor leaves. The yellow pill reads `Your turn n of N`. The rest of the screen dims, the target pulses and a prompt sits below it. Each click shows a caption, and the next prompt follows about 1.4 seconds later. At the end the pill turns green and reads `Done`.
* **Replay** restarts the current mode. The step arrows jump to the start of any step, in both modes. With reduced motion turned on, the card starts in Try it and nothing plays on its own.

## The four cards

| Card | Layout | Steps |
|---|---|---|
| 1 BOM Changes & Cost Roll-Up | BOM tree, change request and open builds on the left. Lines, Cost and Revisions tabs on the right | Open PCBA-210, Cost, New revision (CAP-1006 to CAP-1007, prefilled), Check open builds, Release rev D, Cost again |
| 2 Shortages & Purchase Orders | Parts table with supply bars and a filter chip, builds and suppliers below, a detail panel on the right | Shortages only, MCU-STM32, Create PO (800 at $4.60, prefilled), Send for approval, Approve as purchasing manager |
| 3 Routing, Kitting & Test Steps | Station board with five lanes, a rework strip and a batch log, with the scan and test forms on the right | Scan reel (prefilled), Release batch to SMT, Move to test, Record test SN-004212 (pass), Record test SN-004213 (fail), Close batch |
| 4 Serial Genealogy & RMA | Node graph whose right side swaps for a customer list, an RMA card and a rework traveler, with a record panel below | Trace serial (SN-004187, prefilled), lot 2631 node, Trace forward, Open RMA, Create rework order, Record retest, Close RMA and ship |

## Numbers the cards compute

The tests assert every one of these.

* **Card 1.** Board material 3.20 + 4.60 + 2.16 + 0.64 + 2.70 + 2.70 = 16.00. Board 20.50, unit 38.15. Rev D: material 16.54, board 21.04, unit 38.69, up 0.54. The extra cost is 135.00 on MO-3102 (250 units) and 216.00 on MO-3110 (400 units), 351.00 together.
* **Card 2.** Available stock: MCU-STM32 −730, CAP-1006 720, RES-0402 7,000, IC-PWR −320, CON-J12 150. MCU-STM32 demand 250 + 120 + 400 + 380 = 1,150, and MO-3110 is the first build to run short. The PO is 800 × 4.60 = 3,680.00, which leaves +70 available.
* **Card 3.** 10 units = 9 good + 1 rework. Components deducted: CAP-1006 180, MCU-STM32 10, and the kit is 6 of 6 lines.
* **Card 4.** Lot 2631 went to 6 + 5 + 3 = 14 units for 3 customers. Rework is 0.5 h × 42.00 = 21.00, plus the 0.12 part, for 21.12.

The backgrounds `bg-1.jpg` to `bg-4.jpg` are the standard industry landscapes, one per card. Each is 604 by 540 px and about 50 KB.
