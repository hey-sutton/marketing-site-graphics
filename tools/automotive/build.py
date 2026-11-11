#!/usr/bin/env python3
"""Build graphics/automotive/card-1.js to card-4.js from card1.py to card4.py.
Uses the shared Watch and Try it frame (tools/electronics/frame.py) through frame_auto.py, which adds the
November 11, 2026 control row rules. No side nav and no profile on any automotive card.
Run from anywhere: python3 tools/automotive/build.py [card numbers]"""
import importlib.util, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import frame_auto  # noqa: E402


def load(n):
    """Load card<n>.py from this folder by path (tools/electronics has files with the same names)."""
    spec = importlib.util.spec_from_file_location('automotive_card%d' % n, os.path.join(HERE, 'card%d.py' % n))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def main(nums):
    for n in nums:
        m = load(n)
        size = frame_auto.build(n, m)
        print('graphics/automotive/card-%d.js  %.1f KB' % (n, size / 1024))
        assert size < 80 * 1024, 'card %d is over 80 KB' % n


if __name__ == '__main__':
    main([int(a) for a in sys.argv[1:]] or [1, 2, 3, 4])
