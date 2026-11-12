# Textile graphics

Four interactive product demos for `/industries/textile` (Graphic Key `textile`). The cards follow one navy twill, TW-5810, dyed as lot DL-2611-B (shade NVY-204, 20 rolls, 2,352 yd) from greige batch GR-1177 woven on WO-5520. All data is invented and illustrative, every name is made up, and no card shows a side nav or a profile.

The source of truth is `tools/textile/`. Edit the generator there, rebuild, test, then open a pull request. Don't hand edit `card-N.js`.

| Card | CMS headline | Layout | Walkthrough |
|---|---|---|---|
| 1 | Roll & Dye Lot Control | Roll table with a label and record panel | Scan a roll, reserve 360 yd from one dye lot, block a mixed lot pick, split a roll |
| 2 | Production Stages & Outsourced Steps | Five column stage board | WO-5520 through yarn, weaving, outside dyeing, finishing and inspection |
| 3 | Cutting & Yield Verification | Split view with a roll length bar | Wrong lot rejected, three lays, 109 yd used, 10 yd remnant, within tolerance |
| 4 | Fiber to Fabric Traceability | Two direction genealogy graph | R-48211 back to yarn lots and suppliers, forward to shipments, audit pack |

Backgrounds `bg-1.jpg` to `bg-4.jpg` are the repo's shared landscapes (604 by 540, progressive JPEG, about 50 KB), one per card. Card 2's vendor side value of fabric and card 3's cut table screen are Studio built screens.
