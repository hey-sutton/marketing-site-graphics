# Frozen food graphics

Four interactive product demos for `/industries/frozen-food` (Graphic Key `frozen-food`). The cards follow one frozen entree, chicken broccoli entree FE-2210, with IQF broccoli from Harvest Ridge Farms and customers Northfield Foods and Coastal Grocers. One pallet holds 100 cases. All data is invented and illustrative, every name is made up, and no card shows a side nav or a profile. Everything inside the demos says "BOM", never "recipe".

The source of truth is `tools/frozen-food/`. Edit the generator there, rebuild, test, then open a pull request. Don't hand edit `card-N.js`.

| Card | Feature | Layout | Walkthrough |
|---|---|---|---|
| 1 | Lot Trace from Ingredient to Pallet | Four column lineage board with connector lines | Type HR-7731, batches, 15 pallets, 9 shipped and 6 in the freezer, hold 6 |
| 2 | Cold Storage by Location | Freezer floor plan, four zones with rack and bin grids, side panel | Scan P-0912, zone lots, move to HB-R1-B4, 3,000 on hand and 1,400 available, hold drops it to 700 |
| 3 | Multi-Level BOM & Cost Roll-Up | BOM tree with allergen chips beside a cost table | FE-2210 at $177.60, chicken to $2.40 is $189.00, 400 lb run $756.00, 378 lb out at $2.00 a lb |
| 4 | Production Stages & Output | Five stage board with expected and actual bars, finished goods and material panels | MO-6105, 22 lb lost against 16, 63 cases to Holding freezer A, chicken 10 lb short for MO-6106 |

Backgrounds `bg-1.jpg` to `bg-4.jpg` are the repo's shared landscapes (604 by 540, progressive JPEG, about 50 KB), one per card.
