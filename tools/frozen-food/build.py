#!/usr/bin/env python3
"""Build graphics/frozen-food/card-1.js to card-4.js from card1.py to card4.py.
Uses the shared Watch and Try it frame (tools/electronics/frame.py) through tools/automotive/frame_auto.py, which applies
the November 11, 2026 UI rules (icon only Replay, control row order, two lines with 40 px controls under 600 px, no plan
wording in the Studio popover, no nav or profile). Only the key and label differ.
Run from anywhere: python3 tools/frozen-food/build.py [card numbers]"""
import importlib.util, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(HERE), 'automotive'))
import frame_auto  # noqa: E402
frame_auto.frame.KEY = 'frozen-food'
frame_auto.frame.LABEL = 'Frozen food'
frame_auto.frame.TOOLS = 'frozen-food'


def load(n):
    """Load card<n>.py from this folder by path (other tools folders have files with the same names)."""
    spec = importlib.util.spec_from_file_location('frozen_card%d' % n, os.path.join(HERE, 'card%d.py' % n))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def main(nums):
    for n in nums:
        size = frame_auto.build(n, load(n))
        print('graphics/frozen-food/card-%d.js  %.1f KB' % (n, size / 1024))
        assert size < 80 * 1024, 'card %d is over 80 KB' % n


if __name__ == '__main__':
    main([int(a) for a in sys.argv[1:]] or [1, 2, 3, 4])
