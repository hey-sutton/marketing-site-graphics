#!/usr/bin/env python3
"""Build graphics/nut-processing/card-1.js to card-4.js from card1.py to card4.py.
Uses the shared Watch and Try it frame (tools/electronics/frame.py, itself built on the Brewery scaffold with the 716 by
640 window) through tools/automotive/frame_auto.py, which applies the November 11, 2026 UI rules (icon only Replay,
control row order, two lines with 40 px controls under 600 px, no plan wording in the Studio popover, no nav or profile).
Only the key and label differ, and the first action moves to 900 ms (the ghost cursor appears at startDelay 750 plus 150).
Run from anywhere: python3 tools/nut-processing/build.py [card numbers]"""
import importlib.util, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(HERE), 'automotive'))
import frame_auto  # noqa: E402
frame_auto.frame.KEY = 'nut-processing'
frame_auto.frame.LABEL = 'Nut processing'
frame_auto.frame.TOOLS = 'nut-processing'
assert frame_auto.frame.ENGINE_JS.count('startDelay:600') == 1
frame_auto.frame.ENGINE_JS = frame_auto.frame.ENGINE_JS.replace('startDelay:600', 'startDelay:750')


def load(n):
    """Load card<n>.py from this folder by path (other tools folders have files with the same names)."""
    spec = importlib.util.spec_from_file_location('np_card%d' % n, os.path.join(HERE, 'card%d.py' % n))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def main(nums):
    for n in nums:
        size = frame_auto.build(n, load(n))
        print('graphics/nut-processing/card-%d.js  %.1f KB' % (n, size / 1024))
        assert size < 80 * 1024, 'card %d is over 80 KB' % n


if __name__ == '__main__':
    main([int(a) for a in sys.argv[1:]] or [1, 2, 3, 4])
