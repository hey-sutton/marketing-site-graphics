#!/usr/bin/env python3
"""Build graphics/electronics/card-1.js to card-4.js from card1.py to card4.py with the shared frame and engine.
Run from anywhere: python3 tools/electronics/build.py [card numbers]"""
import importlib, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import frame  # noqa: E402

def main(nums):
    for n in nums:
        m = importlib.import_module('card%d' % n)
        st = frame.studio(**m.STUDIO)
        size = frame.build(n, m.SUMMARY, m.ARIA, m.WIN, m.CSS, m.JS, m.STEPS, st)
        print('graphics/electronics/card-%d.js  %.1f KB' % (n, size / 1024))
        assert size < 80 * 1024, 'card %d is over 80 KB' % n

if __name__ == '__main__':
    main([int(a) for a in sys.argv[1:]] or [1, 2, 3, 4])
