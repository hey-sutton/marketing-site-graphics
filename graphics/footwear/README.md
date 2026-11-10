# Footwear graphics

Four interactive product demos for `/industries/footwear-erp-software` (Graphic Key `footwear`). The company is Marlow Shoe Co., a maker of shoes and boots. The cards share styles and IDs (Harbor Runner HR-210, Harbor Boot HB-330, WO-4417, MO-5102), so they read as one business. All data is invented and illustrative, and every company name is made up (Ridgeline Tannery, Northgate Footwear and the retailers).

The source of truth is `tools/footwear/`. Edit the generator there, rebuild, test, then open a pull request. Don't hand edit `card-N.js`.

| Card | Feature | Layout | Second screen |
|---|---|---|---|
| 1 | Size & Color Matrix Inventory | Grid: colors by sizes 7 to 12, Regular and Wide | Shortage detail with the BOM, then the purchase order |
| 2 | Cutting to Finishing Routing | Stage board with five columns and bars | Cutting detail, then the Lasting station tablet |
| 3 | Contract Factory Visibility | Two column split: you supply, factory supplies | Factory purchase order, then receiving |
| 4 | Cost per Pair & Margin | Stacked bar chart with a table | Landed cost from the receipt |

Backgrounds `bg-1.jpg` to `bg-4.jpg` are the repo's shared landscapes (604 by 540, progressive JPEG), one per card.
