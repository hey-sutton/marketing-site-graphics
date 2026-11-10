#!/usr/bin/env python3
"""Build graphics/furniture-woodworking/card-1.js to card-4.js from card1.py to card4.py.
Uses the shared Watch and Try it frame in tools/electronics/frame.py with the furniture-woodworking key, its app shell
(with the furniture shop's own six modules) and its phone layout under 520 px of card width.
Run from anywhere: python3 tools/furniture-woodworking/build.py [card numbers]"""
import importlib, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(1, os.path.join(os.path.dirname(HERE), 'electronics'))
import frame  # noqa: E402
frame.KEY = 'furniture-woodworking'
frame.LABEL = 'Furniture and woodworking'
# the shop's modules: key, label, 16 px icon paths (stroke icons, drawn inline)
frame.MODS = [
    ('sch', 'Schedule', '<rect x="2" y="3" width="12" height="11" rx="1.5"/><path d="M2 6.5h12M5.5 1.8v2.6M10.5 1.8v2.6M4.5 9h3M4.5 11.5h5"/>'),
    ('pro', 'Production', '<path d="M2 13.5h12M3.5 13.5V7l3 2V7l3 2V4.5h3v9"/>'),
    ('inv', 'Inventory', '<path d="M2.5 5.2L8 2.5l5.5 2.7v5.6L8 13.5l-5.5-2.7z M2.5 5.2L8 8l5.5-2.8M8 8v5.5"/>'),
    ('sal', 'Sales', '<path d="M2.5 8.6V2.5h6.1l5 5-6.1 6.1z"/><circle cx="5.4" cy="5.4" r="1"/>'),
    ('pur', 'Purchasing', '<path d="M1.8 2.5h2l1.6 7.6h7.1l1.4-5.3H4.6"/><circle cx="6.2" cy="12.6" r="1"/><circle cx="11.6" cy="12.6" r="1"/>'),
    ('rep', 'Reports', '<path d="M2.5 13.5h11M4 11.5V8M7 11.5V4.5M10 11.5V6.5M13 11.5V3"/>')]
PHONE = True
# Shared by all four cards, added after staging (Nov 10):
#  * the card visual is shorter on screens 1440 px and wider (aspect 604/523), so the step arrows sit higher;
#  * the shadow host inherits text settings from the page (letter spacing, word spacing and so on), so reset them;
#  * every 1fr track becomes minmax(0,1fr), so a long unwrapped label can never push the other columns out of a row.
FIX_CSS = ('.stp{bottom:66px}'
           '.sx-stage{letter-spacing:normal;word-spacing:normal;text-transform:none;font-style:normal;font-variant:normal;text-indent:0}'
           '.fwin{text-align:left;white-space:normal}.row>span{min-width:0;overflow:hidden;text-overflow:ellipsis}')


def tracks(s):
    return s.replace('1fr', 'minmax(0,1fr)')


def main(nums):
    for n in nums:
        m = importlib.import_module('card%d' % n)
        st = frame.studio(**m.STUDIO)
        win = frame.shell('Larchmont Woodworks', 'Cabinets and furniture') + m.WIN
        size = frame.build(n, m.SUMMARY, m.ARIA, win, tracks(m.CSS) + FIX_CSS, tracks(m.JS), m.STEPS, st, shell=True, phone=PHONE)
        print('graphics/furniture-woodworking/card-%d.js  %.1f KB' % (n, size / 1024))
        assert size < 80 * 1024, 'card %d is over 80 KB' % n


if __name__ == '__main__':
    main([int(a) for a in sys.argv[1:]] or [1, 2, 3, 4])
