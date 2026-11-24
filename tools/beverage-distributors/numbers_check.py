"""Every sum in the beverage distributors brief, asserted in Python before a card is built (build.py imports this
module). The cards compute the same numbers in JavaScript; the tests then read them off the screen. Money is held in
cents and coverage in tenths of a day so every sum is exact. All names and numbers are invented sample data."""
from datetime import date

# ---- card 1: available stock and peak season planning, 14 day window ----
WINDOW = 14
SKUS = {  # in stock, expected, committed over the window
    'Citrus Seltzer 12 pack': (300, 150, 700),
    'Harbor Lager 24 pack': (1200, 400, 840),
    'Orchard Juice 24 pack': (480, 0, 560),
    'Cold Brew RTD 4 pack': (900, 300, 420),
}


def avail(s):
    st, ex, cm = SKUS[s]
    return st + ex - cm


def per_day(s):
    assert SKUS[s][2] % WINDOW == 0
    return SKUS[s][2] // WINDOW


def cover10(s):   # days of coverage in tenths: in stock / daily demand
    return SKUS[s][0] * 10 // per_day(s)


assert avail('Citrus Seltzer 12 pack') == -250                       # 300 + 150 - 700, a shortage of 250 cases
assert per_day('Citrus Seltzer 12 pack') == 50 and cover10('Citrus Seltzer 12 pack') == 60   # 6.0 days
LOCS = [('Warehouse', 180), ('Cooler', 90), ('3PL', 30)]
assert sum(q for _, q in LOCS) == SKUS['Citrus Seltzer 12 pack'][0] == 300
SHORT = -avail('Citrus Seltzer 12 pack')
PO_CENTS = SHORT * 1140
assert SHORT == 250 and PO_CENTS == 285000                            # 250 cases at 11.40 = 2,850.00
assert (avail('Harbor Lager 24 pack'), per_day('Harbor Lager 24 pack'), cover10('Harbor Lager 24 pack')) == (760, 60, 200)
assert (avail('Orchard Juice 24 pack'), per_day('Orchard Juice 24 pack'), cover10('Orchard Juice 24 pack')) == (-80, 40, 120)
assert (avail('Cold Brew RTD 4 pack'), per_day('Cold Brew RTD 4 pack'), cover10('Cold Brew RTD 4 pack')) == (780, 30, 300)

# ---- card 2: lot dates and oldest first picking, as of Nov 16 ----
AS_OF = date(2026, 11, 16)
LOTS = [('HL-2611-A', date(2026, 12, 14), 180), ('HL-2611-B', date(2027, 1, 25), 420), ('HL-2611-C', date(2027, 3, 8), 600)]
assert [(b - AS_OF).days for _, b, _ in LOTS] == [28, 70, 112]
assert sum(q for _, _, q in LOTS) == 1200 == SKUS['Harbor Lager 24 pack'][0]   # matches card 1 stock
assert [b for _, b, _ in LOTS] == sorted(b for _, b, _ in LOTS)                # oldest first
ORDER = 500
pick, left = [], ORDER
for lot, _, q in LOTS:
    take = min(q, left)
    if take:
        pick.append((lot, take))
    left -= take
assert pick == [('HL-2611-A', 180), ('HL-2611-B', 320)] and sum(t for _, t in pick) == ORDER
THRESHOLD = 30
at_risk = [(l, q) for l, b, q in LOTS if (b - AS_OF).days < THRESHOLD]
assert at_risk == [('HL-2611-A', 180)]
AFTER = {l: q - dict(pick).get(l, 0) for l, _, q in LOTS}
# lot A is under the threshold, so it is offered to Dockside Taproom (takes 14 days) and the 500 case pick moves to B and C
REPICK, left = [], ORDER
for lot, _, q in LOTS[1:]:
    take = min(q, left)
    if take:
        REPICK.append((lot, take))
    left -= take
assert REPICK == [('HL-2611-B', 420), ('HL-2611-C', 80)] and sum(t for _, t in REPICK) == ORDER
assert 1200 - ORDER - 180 == 520 and (date(2026, 12, 14) - date(2026, 11, 17)).days == 27   # delivered Nov 17, 27 days left
assert AFTER == {'HL-2611-A': 0, 'HL-2611-B': 100, 'HL-2611-C': 600} and sum(AFTER.values()) == 1200 - ORDER

# ---- card 3: recall lookup for supplier lot BRW-4471 ----
PALLETS, PER_PALLET = 40, 24
RECEIVED = PALLETS * PER_PALLET
assert RECEIVED == 960
ACCOUNTS = [('Dockside Taproom', 120), ('Greenline Market', 240), ('Pier 9 Bar', 60), ('Northgate Grocers', 300), ('Elm Street Liquor', 60)]
SHIPPED = sum(q for _, q in ACCOUNTS)
ON_HAND = 180
assert len(ACCOUNTS) == 5 and SHIPPED == 780 and SHIPPED + ON_HAND == RECEIVED

# ---- card 4: order with a keg deposit and the delivery board ----
LINES = [('Harbor Lager 24 pack', 40, 2450), ('Cold Brew RTD 4 pack', 20, 1900), ('Half barrel keg', 2, 16500)]
AMTS = [q * p for _, q, p in LINES]
assert AMTS == [98000, 38000, 33000]
GOODS = sum(AMTS)
DEPOSIT = 2 * 3000
assert GOODS == 169000 and DEPOSIT == 6000 and GOODS + DEPOSIT == 175000   # 1,690.00 + 60.00 = 1,750.00
assert avail('Harbor Lager 24 pack') >= 40 and avail('Cold Brew RTD 4 pack') >= 20   # 760 covers 40, 780 covers 20
BOARD = [5, 4, 3, 11]
assert sum(BOARD) == 23
CREATED = [6, 4, 3, 11]
DELIVERED = [5, 4, 3, 12]
assert sum(CREATED) == 24 and sum(DELIVERED) == 24
