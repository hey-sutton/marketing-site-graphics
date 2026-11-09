#!/usr/bin/env python3
"""Build graphics/plastics/card-1.js to card-4.js from card1.py to card4.py.
Uses the shared Watch and Try it frame and engine in tools/electronics/frame.py with the plastics key.
Run from anywhere: python3 tools/plastics/build.py [card numbers]"""
import importlib, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(1, os.path.join(os.path.dirname(HERE), 'electronics'))
import frame  # noqa: E402
frame.KEY = 'plastics'
frame.LABEL = 'Plastics'

def main(nums):
    for n in nums:
        m = importlib.import_module('card%d' % n)
        st = frame.studio(**m.STUDIO)
        size = frame.build(n, m.SUMMARY, m.ARIA, m.WIN, m.CSS, m.JS, m.STEPS, st)
        print('graphics/%s/card-%d.js  %.1f KB' % (frame.KEY, n, size / 1024))
        assert size < 80 * 1024, 'card %d is over 80 KB' % n

if __name__ == '__main__':
    main([int(a) for a in sys.argv[1:]] or [1, 2, 3, 4])
