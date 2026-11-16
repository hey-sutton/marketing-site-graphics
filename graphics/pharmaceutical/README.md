# Pharmaceutical graphics

Four interactive product demos for `/industries/pharmaceutical` (Graphic Key `pharmaceutical`). The cards follow one product, CP-050, a 50 mg capsule sold in bottles of 100 (fill weight 400 mg, batch size 200,000 capsules unless stated), with supplier Alder Ridge Supply and customers Kestrel Wellness and Bayline Compounding. All data is invented and illustrative, every name is made up, and no card shows a side nav or a profile. Everything inside the demos says "BOM" or "formula", never "recipe", and no card claims validation, an electronic batch record, Part 11, GMP or FDA status.

The source of truth is `tools/pharmaceutical/`. Edit the generator there, rebuild, test, then open a pull request. Don't hand edit `card-N.js`.

| Card | Feature | Layout | Walkthrough |
|---|---|---|---|
| 1 | Supplier Lot to Batch Trace | Supplier lot card and batch list on the left, batch dossier with Inputs, Shipments and Status tabs on the right | Type EX-3307, B-2611 (68.996 kg) and B-2614 (34.498 kg) affected, B-2609 not, 46.506 kg on hand; B-2611 inputs by supplier lot (80.000 kg blend); 3,000 made, 1,800 shipped, 1,200 on site; hold: 2 batches, 2 customers, 1,200 bottles and 46.506 kg held |
| 2 | Quarantine & Release | Three lane release board (Quarantine, In test, Released) with a lot history log, receiving, availability and a pick list on the right | Receive PO-4420, shortage of 2.408 kg; test with certificate (assay 98.0%, expiry 2028-10-31, retest 2027-10-31); pick blocked "Lot is in quarantine"; sign off JL 10:42; 48.000 on hand, 20.408 committed, 27.592 available |
| 3 | Formulas & Unit Conversion | Formula workbench: formula picker, batch size and unit converter on top, ingredient ledger on the left, v3 and v4 comparison with a cost strip on the right | Select CP-050, scale to 200,000 (10.000, 0.800, 69.200 kg), assay 98.0% (10.204 and 68.996 kg), compare v3 (0.400, 69.396 kg), cost $8,253.63, $4.13 a bottle, +$1.00 against v3. Any batch size from 10,000 to 1,000,000 in hundreds scales |
| 4 | Digital Production Records | Operator tablet: order input and a rail of five step tiles on the left, a record sheet that fills line by line on the right | Open MO-7210 (B-2620); three lot scans by MK (80.000 kg); blend 08:10 to 08:40 and 198,400 filled of 200,000; fill weight 399.6 mg, Pass; 1,984 bottles, 16 returned, yield 99.2%, posted to QA-01, record complete, waiting for release |

Backgrounds `bg-1.jpg` to `bg-4.jpg` are the repo's shared landscapes (604 by 540, progressive JPEG, about 50 KB), one per card.
