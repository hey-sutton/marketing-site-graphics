#!/usr/bin/env python3
"""Build graphics/footwear/card-1.js to card-4.js from card1.py to card4.py.
Uses the shared Watch and Try it frame in tools/electronics/frame.py with the footwear key, its app shell (SHELL) with
footwear modules, and its phone layout (PHONE). Set PHONE = False below to ship the shrink to fit version instead.
Run from anywhere: python3 tools/footwear/build.py [card numbers]"""
import importlib, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(1, os.path.join(os.path.dirname(HERE), 'electronics'))
import frame  # noqa: E402
frame.KEY = 'footwear'
frame.LABEL = 'Footwear'
PHONE = True
COMPANY, SUB = 'Marlow Shoe Co.', 'Shoes and boots'

# the app shell's modules for a footwear maker (id, label, icon path)
frame.MODS = [('inv', 'Inventory', '<path d="M2.5 5.2L8 2.5l5.5 2.7v5.6L8 13.5l-5.5-2.7z M2.5 5.2L8 8l5.5-2.8M8 8v5.5"/>'),
              ('pro', 'Production', '<circle cx="8" cy="8" r="2.2"/><path d="M8 1.8v2M8 12.2v2M1.8 8h2M12.2 8h2M3.6 3.6l1.4 1.4M11 11l1.4 1.4M3.6 12.4L5 11M11 5l1.4-1.4"/>'),
              ('pur', 'Purchasing', '<path d="M1.8 2.5h2l1.6 7.5h7l1.4-5.2H4.6"/><circle cx="6.2" cy="12.6" r="1"/><circle cx="11.6" cy="12.6" r="1"/>'),
              ('sal', 'Sales', '<path d="M2.5 8.6V2.5h6.1l5 5-6.1 6.1z"/><circle cx="5.4" cy="5.4" r="1"/>'),
              ('cst', 'Costing', '<circle cx="8" cy="8" r="5.6"/><path d="M9.9 6.1c-.4-.6-1.1-.9-1.9-.9-1 0-1.8.5-1.8 1.3 0 1.8 3.8.9 3.8 2.8 0 .8-.8 1.4-2 1.4-.9 0-1.6-.4-2-1M8 4v1.2M8 10.8V12"/>'),
              ('rep', 'Reports', '<path d="M2.5 13.5h11M4 11.5V8M7 11.5V4.5M10 11.5V6.5M13 11.5V3"/>')]


def main(nums):
    for n in nums:
        m = importlib.import_module('card%d' % n)
        st = frame.studio(**m.STUDIO)
        win = frame.shell(COMPANY, SUB) + m.WIN
        size = frame.build(n, m.SUMMARY, m.ARIA, win, m.CSS, m.JS, m.STEPS, st, shell=True, phone=PHONE)
        print('graphics/footwear/card-%d.js  %.1f KB' % (n, size / 1024))
        assert size < 80 * 1024, 'card %d is over 80 KB' % n


if __name__ == '__main__':
    main([int(a) for a in sys.argv[1:]] or [1, 2, 3, 4])
