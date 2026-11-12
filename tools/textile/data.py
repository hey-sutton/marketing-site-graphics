"""Shared data for the four textile cards, with the assertions from the brief.
Every card that shows one of these figures takes it from here, so the figures are the same everywhere on the page.
Importing this module runs the assertions (build.py and every test import it)."""
from decimal import Decimal, ROUND_HALF_UP

LOT = 'DL-2611-B'
SHADE = 'NVY-204'
LOT_ROLLS = 20
LOT_YD = 2352

# shipped from the dye lot
SHIP = [('SO-3301', 'Linden Apparel Works', 360), ('SO-3322', 'Harbor Home Textiles', 744), ('SO-3329', 'Pell Street Furnishings', 480)]
SHIPPED = sum(q for _, _, q in SHIP)

# in stock: five available rolls and two held rolls
AVAIL = [('R-48211', 120, 'C-05'), ('R-48212', 118, 'C-05'), ('R-48213', 122, 'C-06'), ('R-48214', 119, 'C-07'), ('R-48215', 121, 'C-07')]
HELD = [('R-48216', 84, 'Q-02'), ('R-48217', 84, 'Q-02')]
AVAIL_YD = sum(q for _, q, _ in AVAIL)
HELD_YD = sum(q for _, q, _ in HELD)
STOCK_YD = AVAIL_YD + HELD_YD
STOCK_ROLLS = len(AVAIL) + len(HELD)

OTHER = ('R-48330', 'DL-2611-C', 'NVY-206', 124)
WIDTH_IN = 58

assert 120 + 118 + 122 + 119 + 121 == AVAIL_YD == 600
assert 84 + 84 == HELD_YD == 168
assert 600 + 168 == STOCK_YD == 768 and STOCK_ROLLS == 7
assert 360 + 744 + 480 == SHIPPED == 1584
assert 1584 + 768 == SHIPPED + STOCK_YD == LOT_YD == 2352
assert 360 + 744 + 480 + 768 == 2352

# card 1: reserve, block, split
SO = ('SO-3318', 360)
RESERVE = ['R-48211', 'R-48212', 'R-48213']
_yd = dict((r, q) for r, q, _ in AVAIL)
assert sum(_yd[r] for r in RESERVE) == 120 + 118 + 122 == SO[1] == 360
SPLIT = ('R-48215', 60, 61)
assert SPLIT[1] + SPLIT[2] == _yd['R-48215'] == 121
LEFT = _yd['R-48214'] + _yd['R-48215']
assert 119 + 121 == LEFT == 240 and AVAIL_YD - SO[1] == LEFT

# card 2: work order WO-5520 through the stages
WARP_KG, WEFT_KG = 300, 180
YARN_KG = WARP_KG + WEFT_KG
GREIGE_ROLLS, GREIGE_PER = 6, 400
GREIGE_YD = GREIGE_ROLLS * GREIGE_PER
DYED_ROLLS, DYED_PER = 6, 392
DYED_YD = DYED_ROLLS * DYED_PER
SHRINK_YD = GREIGE_YD - DYED_YD
FINISH_LOSS = 12
MEASURED = DYED_YD - FINISH_LOSS
assert 300 + 180 == YARN_KG == 480
assert 6 * 400 == GREIGE_YD == 2400
assert 6 * 392 == DYED_YD == 2352 == LOT_YD
assert SHRINK_YD == 48 and Decimal(SHRINK_YD) / Decimal(GREIGE_YD) * 100 == Decimal('2.0')
assert 2352 - 12 == MEASURED == 2340

# card 2: costs. Dyeing is charged on the greige yards sent, finishing on the dyed yards received.
YARN_RATE, DYE_RATE, FIN_RATE = Decimal('14.20'), Decimal('0.85'), Decimal('0.30')
COST_YARN = YARN_RATE * YARN_KG
COST_DYE = DYE_RATE * GREIGE_YD
COST_FIN = FIN_RATE * DYED_YD
COST_TOTAL = COST_YARN + COST_DYE + COST_FIN
assert COST_YARN == Decimal('6816.00') and COST_DYE == Decimal('2040.00') and COST_FIN == Decimal('705.60')
assert COST_TOTAL == Decimal('9561.60')
BOM_SHRINK_PCT = 1        # the BOM estimate assumes 1 percent loss from greige to finished
BOM_YD = GREIGE_YD * (100 - BOM_SHRINK_PCT) // 100
assert BOM_YD == 2376


def cents(x):
    return x.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)


PER_YD_BOM = cents(COST_TOTAL / BOM_YD)
PER_YD_ACT = cents(COST_TOTAL / MEASURED)
assert PER_YD_BOM == Decimal('4.02') and PER_YD_ACT == Decimal('4.09')

# card 3: cutting order CO-771 on roll R-48214
LAYS, LAY_YD = 3, 36
PLANNED = LAYS * LAY_YD
USED = 109
WASTE = USED - PLANNED
REMNANT = _yd['R-48214'] - USED
TOL = Decimal(PLANNED) * Decimal('0.015')
assert 36 * 3 == PLANNED == 108 and 109 - 108 == WASTE == 1 and 119 - 109 == REMNANT == 10
assert TOL == Decimal('1.620') and WASTE <= TOL

# card 4: genealogy
GREIGE_BATCH = 'GR-1177'
YARN_LOTS = [('YL-7702', 'Warp', WARP_KG, 'Calder Fiber'), ('YL-7715', 'Weft', WEFT_KG, 'Northfield Spinning')]
assert sum(q for _, _, q, _ in YARN_LOTS) == 480
assert SHIPPED + STOCK_YD == 2352
