#!/usr/bin/env python3
"""Build graphics/recycling/card-1.js to card-4.js from card1.py to card4.py.
Uses the shared Watch and Try it frame in tools/electronics/frame.py with the recycling key, and opts in to its
app shell (SHELL) and phone layout (PHONE). Set PHONE = False below to ship the shrink to fit version instead.
Run from anywhere: python3 tools/recycling/build.py [card numbers]"""
import importlib, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(1, os.path.join(os.path.dirname(HERE), 'electronics'))
import frame  # noqa: E402
frame.KEY = 'recycling'
frame.LABEL = 'Recycling'
PHONE = True


def main(nums):
    for n in nums:
        m = importlib.import_module('card%d' % n)
        st = frame.studio(**m.STUDIO)
        win = frame.shell('Cedar Valley Recycling', 'Plastics processor') + m.WIN
        size = frame.build(n, m.SUMMARY, m.ARIA, win, m.CSS, m.JS, m.STEPS, st, shell=True, phone=PHONE)
        print('graphics/recycling/card-%d.js  %.1f KB' % (n, size / 1024))
        assert size < 85 * 1024, 'card %d is over 85 KB' % n

if __name__ == '__main__':
    main([int(a) for a in sys.argv[1:]] or [1, 2, 3, 4])
