# Automotive graphics

Four interactive product demos for `/industries/automotive` (Graphic Key `automotive`). The cards follow one supplier making bracket assembly BA-5520 for two customer plants, Plant North and Plant South, with fasteners from Ridgefield Fasteners. All data is invented and illustrative, every name is made up, and no card shows a side nav or a profile.

The source of truth is `tools/automotive/`. Edit the generator there, rebuild, test, then open a pull request. Don't hand edit `card-N.js`.

| Card | Feature (working title) | Layout | Walkthrough |
|---|---|---|---|
| 1 | Component Genealogy & Containment | Genealogy graph with a containment summary | Type lot SL-4471, work orders, finished lots, shipments, hold 900 on hand |
| 2 | BOM Revisions & Engineering Changes | Side by side Rev C and Rev D table with an approval stepper | Open ECO-0192, compare, roll up $4.82 to $5.04, set Dec 1 effectivity, approve and release |
| 3 | Release Driven Scheduling | Week board with a capacity line | Import REL-4410, place demand, level to 700 a day, check material, draft a PO for 1,600 |
| 4 | Quality, Non Conformance & Audit Records | Measurement chart, NCR record panel, 8D timeline and audit checklist | WO-7108 bore readings, 17 in and 3 out, NCR-0318, rework 90 and scrap 50, audit record 5 of 5 |

The card headlines are working titles. Match them to the CMS fields `usp-1---headline` to `usp-4---headline` once the page copy is approved.

Backgrounds `bg-1.jpg` to `bg-4.jpg` are the repo's shared landscapes (604 by 540, progressive JPEG, about 50 KB), one per card.
