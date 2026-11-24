#!/usr/bin/env python3
"""Build graphics/beverage-distributors/card-1.js to card-4.js from card1.py to card4.py.

Uses the shared Watch and Try it frame in tools/electronics/frame.py (the Brewery scaffold at 716 by 640, Studio badge
and popover, Replay, hint pill, ghost cursor, captions, step arrows, ripple hotspots, visibility observer, aria live
region) with the app shell (SHELL) and the phone layout (PHONE), like Footwear. On top of that, for beverage distributors:
  * the Studio popover's "Get help" row says "From the Sutton team" (no plan wording, November 11, 2026 rule);
  * no step arrows and no status pill (Watching, Your turn, Done) at any width: the Watch and Try it toggle, Replay,
    the ghost cursor, the ripple and the prompts inside the window stay;
  * on the phone stage the strip under the window is 10 px of photo instead of 36 px;
  * the top bar controls are 40 px tall on the phone stage.
Before writing anything, every number in the brief is asserted in numbers_check.py.
Run from anywhere: python3 tools/beverage-distributors/build.py [card numbers]"""
import importlib, json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(1, os.path.join(os.path.dirname(HERE), 'electronics'))
import frame  # noqa: E402
import numbers_check  # noqa: E402,F401  (asserts the brief's sums on import)

frame.KEY = 'beverage-distributors'
frame.LABEL = 'Beverage distributors'
COMPANY, SUB = 'Saltline Beverage Co', 'Beer, seltzer and juice'
GET_HELP = 'From the Sutton team'

# the app shell's modules for a beverage distributor (hidden on screen, but the breadcrumb and tests use the ids) (id, label, icon path)
frame.MODS = [('inv', 'Inventory', '<path d="M2.5 5.2L8 2.5l5.5 2.7v5.6L8 13.5l-5.5-2.7z M2.5 5.2L8 8l5.5-2.8M8 8v5.5"/>'),
              ('pur', 'Purchasing', '<path d="M1.8 2.5h2l1.6 7.5h7l1.4-5.2H4.6"/><circle cx="6.2" cy="12.6" r="1"/><circle cx="11.6" cy="12.6" r="1"/>'),
              ('whs', 'Warehouse', '<path d="M2 6.5L8 3l6 3.5V13.5H2z"/><path d="M5 13.5V9h6v4.5M5 11.2h6"/>'),
              ('trc', 'Traceability', '<circle cx="3.5" cy="8" r="1.6"/><circle cx="12.5" cy="4" r="1.6"/><circle cx="12.5" cy="12" r="1.6"/><path d="M5.1 8h2.4M7.5 8l3.4-3.6M7.5 8l3.4 3.6"/>'),
              ('sal', 'Sales', '<path d="M2.5 8.6V2.5h6.1l5 5-6.1 6.1z"/><circle cx="5.4" cy="5.4" r="1"/>'),
              ('dlv', 'Delivery', '<path d="M1.5 4h8v6.5h-8zM9.5 6.5h2.8l2.2 2.2v1.8h-5z"/><circle cx="4.2" cy="11.6" r="1.3"/><circle cx="11.6" cy="11.6" r="1.3"/>')]

# no step arrows and no status pill at any width (November 24, 2026); the phone stage keeps a 10 px strip of photo
# under the window and 40 px top bar controls
PHONE_STRIP_OLD = 'wh=Math.round((H-48-36)/s)'
PHONE_STRIP_NEW = 'wh=Math.round((H-48-10)/s)'
PHONE_CSS = (
 '.stp,.tbar .mode{display:none!important}'
 # no module nav (November 24, 2026): the side nav on desktop and the bottom bar on the phone stage are hidden, so the
 # window shows only the app screen with its breadcrumb and header
 '.rail,.bn,.shot.ph .bn{display:none!important}.app,.shot.ph .app{grid-template-columns:1fr}'
 '.shot.ph .studio{top:4px;left:8px}.shot.ph .studio-chip{height:40px}.shot.ph .tbar{top:4px}.shot.ph .mtg{height:40px}.shot.ph .mtg button{min-width:44px}'
 '.shot.ph .mode{height:40px}.shot.ph .tbar .rp{height:40px;min-width:40px;justify-content:center}'
 '.xw{display:none}.shot.ph .xw{display:block}.shot.ph.nar .xw .row:nth-child(n+3){display:none}.shot.ph.nar .xw.nn{display:none}.xw .row{grid-template-columns:1fr auto;font-size:10px}.xw .row span:last-child{font-family:"JetBrains Mono",ui-monospace,monospace}'
 '.shot.ph .bi{width:44px;height:40px}.shot.ph .mtg{height:auto;padding:0;gap:0}.shot.ph .mtg button{height:40px}'
 '.shot.ph.nar .studio-chip{padding:0 10px}.shot.ph.nar .studio-chip>span:nth-child(2){position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0)}'
)

# read only inputs (demo input rules, November 2026): every field is prefilled with the walkthrough's value, readonly,
# out of the tab order, gray and ignores the pointer. The reader only clicks the button beside it.
RO_CSS = ('.rof{display:flex;align-items:center;gap:8px}.rof label{flex:1;min-width:0;position:relative;display:flex;flex-direction:column;gap:2px}'
 '.rof label small{font-size:8.8px;color:#71717A}.rof input{font:inherit;font-family:"JetBrains Mono",ui-monospace,monospace;font-size:10.6px;height:30px;padding:0 10px;'
 'border:1px solid #E4E4E7;border-radius:7px;background:#F4F4F5;color:#18181B;width:100%;pointer-events:none}.rof .bt{height:30px;align-self:flex-end}'
 '.rof .cx{font-size:9px;color:#71717A;white-space:nowrap;align-self:flex-end;padding-bottom:9px}'
 '.shot.ph .rof input,.shot.ph .rof .bt{height:40px}.shot.ph .rof .cx{display:none}.shot.ph .rof label small{display:none}')
RO_JS = ("function rof(o){return '<div class=\"rof\"><label><small>'+o.l+'</small><input id=\"'+o.id+'\" value=\"'+o.v+'\" readonly tabindex=\"-1\" aria-label=\"'+o.l+'\"></label>'"
         "+(o.b?'<button type=\"button\" class=\"bt'+(o.pri?' pri':'')+'\" id=\"'+o.bid+'\">'+o.b+'</button>':'')+(o.cx?'<span class=\"cx\">'+o.cx+'</span>':'')+'</div>';}\n")

# a short detail list each card appends to its phone screens, so they have no empty band: three rows on phone
# stages 430 px and wider, two below that; xw(rows, 1) drops it below 430 px on screens that are already full
XW_JS = "function xw(rows,nn){return '<div class=\"xw'+(nn?' nn':'')+'\"><div class=\"cd\">'+rows.map(function(r){return '<div class=\"row\"><span>'+r[0]+'</span><span>'+r[1]+'</span></div>';}).join('')+'</div></div>';}\n"


def prune(n):
    """Drop rules of the shared Brewery scaffold CSS whose classes this card never uses (its markup and script are
    searched as plain text, so anything named anywhere is kept). Only this card's file changes; the shared frame
    does not. Keeps each card near the 65 KB target."""
    from gfx_scaffold import Scaffold   # already importable: frame.py put tools/dairy on the path (at the end)
    path = os.path.join(frame.REPO, 'graphics', frame.KEY, 'card-%d.js' % n)
    lines = open(path, encoding='utf-8').read().split('\n')
    i = [k for k, l in enumerate(lines) if l.startswith('var CSS=')][0]
    rest = '\n'.join(lines[:i] + lines[i + 1:])
    pre, post = 'var CSS=', ".replace('__BG__',BGU);"
    assert lines[i].endswith(post)
    css = json.loads(lines[i][len(pre):-len(post)])
    for sel, body in re.findall(r'([^{}@]+)\{([^{}]*)\}', Scaffold(frame.REPO).css):
        cls = re.findall(r'\.([a-zA-Z][\w-]*)', sel)
        rule = sel + '{' + body + '}'
        if cls and all(c not in rest for c in cls) and css.count(rule) == 1:
            css = css.replace(rule, '')
    lines[i] = pre + json.dumps(css) + post
    out = '\n'.join(lines)
    open(path, 'w', encoding='utf-8').write(out)
    return len(out.encode())


def main(nums):
    assert frame.PHONE_JS.count(PHONE_STRIP_OLD) == 1
    frame.PHONE_JS = frame.PHONE_JS.replace(PHONE_STRIP_OLD, PHONE_STRIP_NEW)
    for n in nums:
        m = importlib.import_module('card%d' % n)
        st = frame.studio(**m.STUDIO)
        assert st.count('<dd>Depends on your plan</dd>') == 1
        st = st.replace('<dd>Depends on your plan</dd>', '<dd>' + GET_HELP + '</dd>')
        win = frame.shell(COMPANY, SUB) + m.WIN
        eng = frame.ENGINE_JS
        for old, new in getattr(m, 'ENGINE_PATCH', []):   # per card timing, for example card 3 types its lot sooner
            assert frame.ENGINE_JS.count(old) == 1
            frame.ENGINE_JS = frame.ENGINE_JS.replace(old, new)
        try:
            css = ':host{--mn:"JetBrains Mono",ui-monospace,monospace}' + (PHONE_CSS + RO_CSS + m.CSS).replace('"JetBrains Mono",ui-monospace,monospace', 'var(--mn)')
            size = frame.build(n, m.SUMMARY, m.ARIA, win, css, XW_JS + RO_JS + m.JS, m.STEPS, st, shell=True, phone=True)
        finally:
            frame.ENGINE_JS = eng
        size = prune(n)
        print('graphics/beverage-distributors/card-%d.js  %.1f KB' % (n, size / 1024))
        assert size < 80 * 1024, 'card %d is over 80 KB' % n


if __name__ == '__main__':
    main([int(a) for a in sys.argv[1:]] or [1, 2, 3, 4])
