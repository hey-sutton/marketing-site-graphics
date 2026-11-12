"""
Textile layer on the shared Watch and Try it frame.

It reuses the Automotive layer (tools/automotive/frame_auto.py), which applies the November 11, 2026 control row
rules on top of tools/electronics/frame.py, and only changes what is textile specific:
  * the Graphic Key is `textile`, so the card file goes to graphics/textile/ and the injected style squares
    `.capabilities_card-visual[data-sx-industry*="textile"]` at the bottom right;
  * every step dwells 2.4 s instead of 2.9 s, so a four step walkthrough runs in about 14 seconds, as the
    textile brief asks. Nothing else in the shared engine changes.
"""
import os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(HERE), 'automotive'))
import frame_auto  # noqa: E402

frame = frame_auto.frame
header = frame_auto.header

KEY = 'textile'
DWELL_OLD = 'dwell:2900'
DWELL_NEW = 'dwell:2400'


def build(n, m):
    """Build graphics/textile/card-N.js from card module m (SUMMARY, ARIA, WIN, CSS, JS, STEPS, STUDIO)."""
    keep = (frame.KEY, frame.LABEL, frame.TOOLS, frame.ENGINE_JS)
    assert frame.ENGINE_JS.count(DWELL_OLD) == 1
    try:
        frame.KEY, frame.LABEL, frame.TOOLS = KEY, 'Textile', 'textile'
        frame.ENGINE_JS = frame.ENGINE_JS.replace(DWELL_OLD, DWELL_NEW)
        return frame_auto.build(n, m)
    finally:
        frame.KEY, frame.LABEL, frame.TOOLS, frame.ENGINE_JS = keep
