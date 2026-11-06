# Traceability feature page: guided handoff

The six cards in `graphics/features-traceability/` rebuilt with the guided walkthrough rules from Simon's Loom (November 6, 2026).

* A short autoplay intro (pill: Watching, 1 of N). Then a hard handoff to the reader (pill: Your turn), and Done at the end.
* One target at a time. It pulses, the rest of the screen dims, and the prompt sits next to it.
* A caption after every click saying what happened. The last caption says what to try next.
* Inputs are prefilled (card 2 split quantity, card 5 supplier search). Nothing that comes from them shows until the reader runs the step.
* Simple cards have 4 steps (1, 4, 5). Complex cards have 5 (2, 3, 6). The screen changes at every step.
* Card 6 walks through the actual recall steps: trace forward, hold on site stock, customer list, then back to the recall steps (4 of 5 done).

| Card | Steps | Reader clicks |
|---|---|---|
| 1 Batch and lot tracking | 4 | Complete order, Cost, Shipments |
| 2 Serialized inventory | 5 | Split label, Split, new label, In transit filter (approved prototype) |
| 3 Regulations and compliance | 5 | View COA, metal detector photo, Export FSMA 204 sheet, Sort by date |
| 4 Inventory control | 4 | Sort by best by, bin RM-A1, Preview alert |
| 5 Supplier traceability | 4 | Search (prefilled), PO-1187, PO-1142 |
| 6 Forward and backward traceability | 5 | Start trace, Hold, Customer list, Close |

The hero (`hero.js`) is unchanged. It is autoplay only by design.

## Files

* `build_guided.py` builds cards 1 and 3 to 6 from their v1.19.0 files and copies card 2 from `card-2-prototype.js`. To rerun it, first restore the v1.19.0 cards: `git checkout v1.19.0 -- graphics/features-traceability`.
* `test_guided.py` clicks through every step on the preview page. It checks the pill, the single target, the dimming, the captions, the computed numbers, the prefill, Replay and the Studio popover. It passes with 0 failures at desktop (604 px) and phone (340 px, `--width 340`). Set `PW_CHROME` to use a preinstalled Chromium.

Every number in the captions is checked against the card data. For example, the cost per case is $22,080.00 / 1,200 = $18.40, and the recall total is 2,410 shipped + 640 on site + 200 in packing = 3,250. Data is illustrative.
