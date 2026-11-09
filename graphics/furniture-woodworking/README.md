# Furniture and woodworking graphics

Four interactive product demos for `/industries/furniture-woodworking` (Graphic Key `furniture-woodworking`). The shop is Larchmont Woodworks, a maker of cabinets and furniture. The cards share jobs and IDs (J-2417 is the Kitchen cabinets job on cards 1 and 2), so the page reads as one shop. All data is invented and illustrative, and every name is made up.

The source of truth is `tools/furniture-woodworking/`. Edit the generator there, rebuild, test, then open a pull request. Don't hand edit `card-N.js`.

Each card runs inside the app shell (a nav of six modules: Schedule, Production, Inventory, Sales, Purchasing, Reports), moves across at least three screens, and switches to the phone layout under 520 px of card width. The Watch and Try it engine is the same as the other industries.

## The four cards

| Card | Headline | Layout | Screens | Steps (target) |
|---|---|---|---|---|
| 1 | Stage Scheduling & Capacity | Swimlane calendar, compact icon nav | Schedule board, Finish capacity panel, Job J-2417 | 4 weeks toggle; amber Nov 23 Finish cell; Move J-2421 finish to Nov 30; Nov 30 cell; row J-2417; Clock in to Finish; Start Finish; Back to board |
| 2 | Offcuts & Remnants | Cut diagram (SVG hero) plus tables | Cut planner, Cut list J-2417, Sheet layout, Inventory | Stock row PLY-MPL-34; Try J-2417 (or type and Enter); Nest on sheet; the leftover; Book remnant to stock; Inventory in the nav; Width 24 in or more |
| 3 | Quote to Configured Order | Split configurator | Configurator, Production order MO-3306, Sales order SO-1184, Change order CO-1184-1 | Customer field; Dining table; White oak, 72 in, Matte lacquer (three clicks, one step); Price tab; Create sales order; SO-1184 link; Apply change order; Production in the nav |
| 4 | Estimated vs Actual Job Margin | Bar chart plus variance table | Project margin, Kitchen variance, Labor: Kitchen | Project field; P-0412 (or type and Enter); project row; Kitchen bars; View labor entries; Build row; Reports in the nav |

## Numbers the cards compute

The tests assert every one of these.

* **Card 1.** Finish room, week of Nov 23: 32 + 20 + 24 + 16 = 92 of 80 h (over by 12). After the move: 92 − 16 = 76 of 80 h, and Nov 30 28 + 16 = 44 of 80 h. Stain 6.5 + 3.5 = 10 of 10 h.
* **Card 2.** Sheet 96 × 48 = 4,608 sq in. Parts 720 + 720 + 864 + 864 + 900 = 4,068, remnant 540, 4,068 + 540 = 4,608, and no part overlaps. Yield 4,068 / 4,608 = 88.3%, remnant 11.7%, 540 / 144 = 3.75 sq ft. Stock 12 to 11 sheets, 2 to 3 remnants. Kerf is not modeled.
* **Card 3.** Price = cost / (1 − 0.38), rounded to the dollar, checked for all 27 option combinations. Default: 700 + 54 + 42 + 936 = 1,732.00, price 2,794. Change to 84 in: +100.00 lumber, +104.00 labor, cost 1,936.00, price 3,123, delta 329. Lumber on MO-3306 56 to 64 bf. Department hours 4 + 8 + 3 + 3 = 18 (20 after the change).
* **Card 4.** Every sub job's lines sum to its cost, margin = revenue − cost, percentages round as shown, project rows are the sums (80,300, 50,240, 53,428, 37.4%, 33.5%, 3,188 over). Kitchen variance 1,550 + 1,456 + 140 = 3,146. Labor 56 + 66 + 46 + 52 = 220 and 62 + 74 + 52 + 60 = 248. Build entries 8.0 + 7.5 + 6.5 + 8.0 + 44.0 = 74 h.

The backgrounds `bg-1.jpg` to `bg-4.jpg` are copies of the shared landscapes 1 to 4 (the same files as `brewery` bg-1 to bg-4), each used once.
