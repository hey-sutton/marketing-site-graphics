# Recycling storyboards

## Card 1: Weighed Receiving (complex)

| # | Screen | Module | Target | Target type | Position | Action | Result | Caption | Phone screen |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Inbound loads | Receiving | Row LD-2291, mixed PP scrap | table row | center | Open the load | The scale ticket opens for LD-2291 | Open any inbound load from the list. | List, then ticket |
| 2 | Scale ticket | Receiving > LD-2291 | Gross field (41,260 lb from the scale, prefilled) | prefilled field | left | Accept the reading | Gross 41,260, default tare 14,980, net 26,280 lb | The scale reading drops in, and tare and net weight work themselves out. | Ticket |
| 3 | Load detail | Receiving > LD-2291 | Tab "Photos and notes" | tab | top center | Open the tab | Three photos and a note: metal inserts in two pallets | Photos and a contamination note stay with the load. | Load detail |
| 4 | Load detail | Receiving > LD-2291 | Toggle "Receive without a PO" | toggle | right | Switch it on | PO-7710 created from the load, supplier Harlan Plastics | Received first, and the purchase order follows from what arrived. | Load detail |
| 5 | Labels | Receiving > Labels | Menu item "Print 12 pallet labels" in the more menu | menu item | top right | Choose it | 12 serialized labels, each 2,190 lb | Every pallet gets its own serialized label with weight and grade. | Labels |
| 6 | Inventory by grade | Inventory | Nav item "Inventory" | nav item | top left | Switch module | PP mixed scrap now 67,780 lb, 26,280 lb added in bin Y1-03 | The load lands in stock by grade and bin. | Inventory |

## Card 2: Sorting & Processing Jobs (complex)

| # | Screen | Module | Target | Target type | Position | Action | Result | Caption | Phone screen |
|---|---|---|---|---|---|---|---|---|---|
| 1 | New job | Processing > New | Load chips LD-2291 and LD-2275 dragged into the job's input list | drag and drop | left to center | Drag both loads in | Job PJ-0318 with 45,000 lb of input | Pull mixed loads together into one processing job. | New job |
| 2 | Job PJ-0318 | Processing > PJ-0318 | Tab "Hand sort" | tab | top center | Open the tab | The sort station with an empty contamination log | Move from the job to the sorting station. | Job, then sort |
| 3 | Hand sort | Processing > PJ-0318 > Hand sort | Contamination field (1,350 lb, prefilled) and reason chips | prefilled field | bottom | Accept the entry | 1,350 lb out as metal, paper and film | Log what you pull out as you sort it. | Hand sort |
| 4 | Conversion | Processing > PJ-0318 > Conversion | Output node "Natural regrind" in the flow diagram | graph node | right | Open the output | 32,400 lb of natural regrind and 9,000 lb of mixed color regrind | See where each pound of input went. | Conversion |
| 5 | Yield report | Reports | Nav item "Reports" | nav item | top left | Switch module | 41,400 of 45,000 lb usable, yield 92.0%, 2,250 lb lost | Yield and loss, in the open, for this job. | Yield report |
| 6 | Job PJ-0318 | Processing > PJ-0318 | Button "Complete job" | primary button | bottom right | Complete the job | Outputs labeled and booked into stock by grade | Completing books the outputs, with labels that trace back to the loads. | Job complete |

## Card 3: Stock by Grade, Bin & Age (complex)

| # | Screen | Module | Target | Target type | Position | Action | Result | Caption | Phone screen |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Inventory by grade | Inventory | Heatmap cell "PP mixed color, 61 to 90 days, 6,100 lb" | heatmap cell | center | Open the cell | Aging detail for PP mixed color regrind | See which grade has been sitting, and for how long. | Grade list, then aging |
| 2 | Aging: PP mixed color | Inventory > Aging | Chip "Older than 60 days" | filter chip | top left | Apply the filter | 9,400 lb in two bins | Filter to material that has sat too long. | Aging |
| 3 | Bin map | Inventory > Bins | Bin cell Y1-04 | map cell | right | Open the bin | 36,800 of 40,000 lb with a near capacity alert | See a bin nearing capacity before it blocks receiving. | Bin screen |
| 4 | Partner aging | Reports > Partners | Breadcrumb "Reports" then row Harlan Plastics | breadcrumb | top | Follow the breadcrumb and open the partner | Harlan Plastics: 4,200 lb older than 60 days | Open a supplier's aging report. | Partner report |
| 5 | Move stock | Inventory > Move | Tile "6,100 lb PP mixed color" dragged to bin Y2-11 | drag and drop | center to right | Drag the tile | Y1-04 now 30,700 lb, Y2-11 now 20,300 lb, move logged | Move aged stock to another bin with one drag. | Move |

## Card 4: Sell & Ship with Paperwork (complex)

| # | Screen | Module | Target | Target type | Position | Action | Result | Caption | Phone screen |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Sales orders | Sales | Row SO-8841, Brightfield Extrusion | table row | center | Open the order | The order opens with 32 gaylords of natural regrind | Open a buyer's order. | List, then order |
| 2 | Order detail | Sales > SO-8841 | Price field (0.46 per lb, prefilled) | prefilled field | right | Accept the price | 40,000 lb at 0.46, total 18,400.00 | The price is set for this load, not a default. | Order |
| 3 | Pick | Shipping > Pick | Scan field (gaylord G-4412) | scan input | bottom | Scan the gaylord | 32 of 32 gaylords picked, 1,250 lb each | Scan to pick the right gaylords for the order. | Pick |
| 4 | Weigh out | Shipping > Weigh out | Toggle "Use weighed amount" | toggle | top right | Switch it on | Net 40,320 lb, order corrected to 18,547.20 | Correct the order to what the scale says. | Weigh out |
| 5 | Documents | Shipping > Documents | Tab "Bill of lading" | tab | top center | Open the tab | BL-5520 with the weighed lines and your branding | The bill of lading prints from the order. | Documents |
| 6 | Documents | Shipping > Documents | Button "Ship and invoice" | primary button | bottom right | Ship the order | Shipped, certificate CR-1190 issued, invoice created | One click ships it, with the certificate attached. | Shipped |

