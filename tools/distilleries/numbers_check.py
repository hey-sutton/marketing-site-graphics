"""Every sum in the distilleries brief, asserted in Python before a card is built (build.py imports this module).
The cards compute the same numbers in JavaScript; the tests then read them off the screen. All data is invented."""
from decimal import Decimal as D

# ---- card 1: mash bill, distillate, blend and bottle cost ----
MASH = [('Corn', 1400, D('0.14')), ('Rye', 400, D('0.22')), ('Malted barley', 200, D('0.31'))]
LB = sum(m[1] for m in MASH)
assert LB == 2000
assert [m[1] * 100 // LB for m in MASH] == [70, 20, 10] and sum(m[1] * 100 // LB for m in MASH) == 100
GRAIN = sum(m[1] * m[2] for m in MASH)
assert [m[1] * m[2] for m in MASH] == [D('196.00'), D('88.00'), D('62.00')]
assert GRAIN == D('346.00')
BATCH_L, YEAST, LABOR = 500, D('24.00'), D('1630.00')
BATCH = GRAIN + YEAST + LABOR
assert BATCH == D('2000.00') and BATCH / BATCH_L == D('4.00')
PER_L = BATCH / BATCH_L
DIST_ML, WATER_ML = 450, 300
assert DIST_ML + WATER_ML == 750
DIST_SHARE = PER_L * DIST_ML / 1000
assert DIST_SHARE == D('1.80')
BOTTLE_PARTS = [DIST_SHARE, D('0.92'), D('0.18'), D('0.09'), D('0.04'), D('0.22')]
BOTTLE = sum(BOTTLE_PARTS)
assert BOTTLE == D('3.25')
assert BOTTLE * 6 == D('19.50') and BOTTLE * 6 + D('0.85') == D('20.35')
SCALE = [(n, lb * 2, p) for n, lb, p in MASH]
assert [s[1] for s in SCALE] == [2800, 800, 400] and sum(s[1] for s in SCALE) == 4000
assert sum(s[1] * s[2] for s in SCALE) == D('692.00')
# yield scales with the mash: 500 L to 1,000 L, so 1,111 then 2,222 whole bottles at 450 ml of distillate each
assert BATCH_L * 1000 // DIST_ML == 1111 and BATCH_L * 2 * 1000 // DIST_ML == 2222

# ---- card 2: rickhouse, sample barrel, the ten barrel dump ----
LOT = 120
GAUGES = [D(x) for x in ('51.2', '51.0', '50.8', '51.4', '51.1', '50.9', '51.3', '51.0', '51.2', '51.1')]
assert len(GAUGES) == 10 and sum(GAUGES) == D('511.0') and LOT - len(GAUGES) == 110
FILL, GAUGE = D('53.0'), D('51.2')
LOSS = FILL - GAUGE
assert LOSS == D('1.8') and (LOSS / FILL * 100).quantize(D('0.1')) == D('3.4')
assert GAUGES[8] == GAUGE   # the sample barrel is position 9 on level 3
# row 4 holds 5 levels of 10 barrels from lot DS-0412, row 5 holds the other 70
assert 5 * 10 + 70 == LOT

# ---- card 3: trace of botanical lot BT-2209 ----
RUNS = {'A': [60, 12, 8], 'B': [30, 40]}
assert sum(RUNS['A']) == 80 and sum(RUNS['B']) == 70
assert sum(RUNS['A']) + sum(RUNS['B']) == 150 and sum(sum(v) for v in RUNS.values()) == 150

# ---- card 4: release allocation and dry goods ----
STOCK, EXPECTED, COMMITTED = 900, 300, 640
AVAIL = STOCK + EXPECTED - COMMITTED
assert AVAIL == 560
SPLIT = [400, 100, 60]
assert sum(SPLIT) == 560 and AVAIL - sum(SPLIT) == 0 and COMMITTED + sum(SPLIT) == 1200
NEED, ON_HAND = 1800, 1500
SHORT = NEED - ON_HAND
assert SHORT == 300 and SHORT * D('0.92') == D('276.00')
