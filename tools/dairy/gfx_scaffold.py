"""
Shared builder for industry card files (graphics/<key>/card-N.js).

It takes the Brewery card as the scaffold (shadow DOM host, Studio badge and popover, Replay, hint pill, ghost cursor,
captions, visibility observer) and applies the rules from the skill:
  * window 716 by 640 design px, so no border or corner shows at the right or bottom edge
  * the card container's bottom right corner is squared through the injected style
  * step arrows, ripple hotspots, walkthrough starts 900 ms after the card is visible
  * the background is the repo hosted bg-N.jpg
You supply, per card: the window HTML, the extra CSS, and the card specific JavaScript (data, render, steps, script).

Usage from a build script:
    from gfx_scaffold import Scaffold
    sc = Scaffold('/path/to/marketing-site-graphics checkout')
    sc.build(key='dairy', n=2, summary='...', aria='...', win_inner=HTML, studio=sc.studio(...), css_extra=CSS, custom=JS, out_dir='out')
"""
import json, os, re

COMMON_CSS = (
 '.ft-h{display:flex;justify-content:space-between;align-items:center;font-weight:600;font-size:10px;padding:0 10px;margin-bottom:6px}'
 '.stg{position:relative}.emp{position:absolute;left:0;right:0;top:0;bottom:0;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:4px;text-align:center;color:#71717A;border:1px dashed #E4E4E7;border-radius:9px;background:#FAFAFA}'
 '.emp svg{margin-bottom:4px}.emp b{font-size:11px;font-weight:600;color:#18181B}.emp span{font-size:9.4px;max-width:320px;line-height:1.35}'
 '.fw-body:not(.off) .emp{display:none}.rv{transition:opacity .35s ease}.fw-body.off .rv{opacity:0;visibility:hidden;pointer-events:none}'
 '.lgd{display:flex;align-items:center;gap:14px;color:#52525B;font-size:8.6px;margin-top:-2px;white-space:nowrap}.lgd span{display:inline-flex;align-items:center;gap:5px}.lgd i{width:12px;height:8px;border-radius:2px;border:1px solid #E4E4E7;background:#fff;flex:none}'
 '.hs{position:absolute;z-index:55;pointer-events:none;border:2px solid #FFB92B;border-radius:9px;opacity:0;transition:opacity .25s ease}.hs.on{opacity:1;animation:hsr 1.6s ease-out infinite}@keyframes hsr{0%{box-shadow:0 0 0 0 rgba(255,185,43,.6)}70%,100%{box-shadow:0 0 0 9px rgba(255,185,43,0)}}'
 '.stp{position:absolute;right:44px;bottom:44px;z-index:56;display:flex;align-items:center;gap:6px}.stp button{width:24px;height:24px;padding:0;border:1px solid #E4E4E7;border-radius:7px;background:#fff;color:#18181B;cursor:pointer;display:grid;place-items:center;transition:background-color .2s}.stp button:hover:not(:disabled){background:#F4F4F5}.stp button:disabled{opacity:.35;cursor:default}.stp button:focus-visible{outline:2px solid #18181B;outline-offset:2px}.stp svg{width:12px;height:12px}.stp .sn{min-width:38px;text-align:center;color:#71717A;font-size:9px}'
)
TAIL_CSS = '.cap{max-width:360px}.cap.turn{max-width:360px}.tr-act{min-height:48px}.cap{z-index:80}'

ENGINE = r'''var pv=$('pv'),nx=$('nx'),sn=$('sn'),hs=$('hs'),cur=1,NS=@NS@;
function showHot(el){if(!el){hs.classList.remove('on');return;}var r=rel(el);hs.style.left=(r.l-3)+'px';hs.style.top=(r.t-3)+'px';hs.style.width=(r.w+6)+'px';hs.style.height=(r.h+6)+'px';hs.classList.add('on');}
function marker(i){cur=i;sn.textContent=i+' of '+NS;pv.disabled=i<=1;nx.disabled=i>=NS;}
function showStep(i,auto){var s=ST[i-1];marker(i);say(i,s.m,s.s);moveGhost(winPos(s.tg(),s.dx,s.dy));if(!auto){ghost.classList.add('on');showHot(s.hot?s.hot():null);}}
function goStep(i){if(i<1||i>NS)return;if(!engaged){engaged=true;cancelAll();}turnOff();applyState(i);showStep(i,false);}
pv.addEventListener('click',function(e){e.stopPropagation();goStep(cur-1);});
nx.addEventListener('click',function(e){e.stopPropagation();goStep(cur+1);});
function onCancel(){[].slice.call(root.querySelectorAll('.fakehover,.press')).forEach(function(b){b.classList.remove('fakehover','press');});}
function click(get,fn,t){later(function(){var el=get();ghost.classList.add('press');if(el)el.classList.add('fakehover','press');},t);later(function(){var el=get();ghost.classList.remove('press');if(el)el.classList.remove('fakehover','press');fn();},t+330);}
'''

class Scaffold:
    def __init__(self, repo):
        src = open(os.path.join(repo, 'graphics/brewery/card-1.js'), encoding='utf-8').read()
        line = src.split('\n')[5]
        css = line[line.index('"') + 1:line.rindex('"')].replace('\\"', '"').replace('\\\\', '\\')
        css = css[:css.index('.pl-two{')]
        a1 = '.win-host{position:absolute;left:7.4%;top:9%;width:686px;height:604px'
        a2 = '.fwin{position:relative;width:686px;height:604px'
        assert css.count(a1) == 1 and css.count(a2) == 1
        css = css.replace(a1, '.win-host{position:absolute;left:7.4%;top:9%;width:716px;height:640px').replace(a2, '.fwin{position:relative;width:716px;height:640px')
        self.css = css
        a = src.index('function boot(root){'); b = src.index("var tree=$('tree'),INTRO=tree")
        sc = src[a:b]; assert sc.count('setTimeout(tour,2200)') == 1
        self.scaffold = sc.replace('setTimeout(tour,2200)', 'setTimeout(tour,900)')
        self.tail = src[src.index("host.removeEventListener('pointerdown',engage,true)"):]
        self.pre = src[src.index("var c=document.currentScript&&document.currentScript.sxCard;"):a]

    @staticmethod
    def studio(lede, examples, built_on):
        ex = ''.join('<li style="--i:%d">%s</li>' % (i, e) for i, e in enumerate(examples))
        arrow = '<svg viewBox="0 0 12 12" aria-hidden="true"><path d="M2 6h8M6.5 2.5L10 6 6.5 9.5" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>'
        return ('<div class="studio" data-studio><button class="studio-chip" type="button" aria-expanded="false" aria-controls="pop1"><span class="wand" aria-hidden="true"><svg viewBox="0 0 20 20" aria-hidden="true"><path class="stick" d="M3 17L12 8" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/><path class="sp sp1" d="M15 1.5L16.2 3.8L18.5 5L16.2 6.2L15 8.5L13.8 6.2L11.5 5L13.8 3.8Z"/><path class="sp sp2" d="M17 10.2L17.6 11.4L18.8 12L17.6 12.6L17 13.8L16.4 12.6L15.2 12L16.4 11.4Z"/><path class="sp sp3" d="M7 1.4L7.6 2.4L8.6 3L7.6 3.6L7 4.6L6.4 3.6L5.4 3L6.4 2.4Z"/></svg></span><span>Studio</span><span class="more"><span class="more-inner"><span class="more-text">Learn more' + arrow + '</span></span></span></button>'
                '<div class="pop" id="pop1" role="dialog" aria-label="About Studio apps"><h3>Start here, make it yours</h3><p class="lede">' + lede + '</p><ul class="examples">' + ex + '</ul>'
                '<dl class="rows"><div><dt>Built on</dt><dd>' + built_on + '</dd></div><div><dt>Change</dt><dd>Fields, wording and workflow</dd></div><div><dt>Get help</dt><dd>Depends on your plan</dd></div></dl>'
                '<a class="go" href="/studio">See what you can build in Studio' + arrow + '</a></div></div>')

    @staticmethod
    def chevrons():
        return ('<span class="hs" id="hs" aria-hidden="true"></span><div class="stp" role="group" aria-label="Walkthrough steps"><button type="button" id="pv" aria-label="Previous step" disabled><svg viewBox="0 0 12 12" aria-hidden="true"><path d="M7.5 2.5L4 6l3.5 3.5" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg></button><span class="sn" id="sn">1 of 5</span><button type="button" id="nx" aria-label="Next step"><svg viewBox="0 0 12 12" aria-hidden="true"><path d="M4.5 2.5L8 6 4.5 9.5" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg></button></div>')

    def build(self, key, n, summary, aria, win_inner, studio, css_extra, custom, out_dir, steps=5):
        css = self.css + COMMON_CSS + css_extra + TAIL_CSS
        body = ('<div class="sx-stage"><div class="shot"><div class="shot-img"><div class="win-host" role="group" aria-label="' + aria + '"><div class="fwin">'
                + win_inner + self.chevrons().replace('1 of 5', '1 of %d' % steps) + '</div></div></div>' + studio + '</div></div>')
        pre = self.pre
        rule = '.capabilities_card-visual[data-sx-industry*="%s"]{border-bottom-right-radius:0}' % key
        assert pre.count("{aspect-ratio:604/523}}'") == 1
        pre = pre.replace("{aspect-ratio:604/523}}'", "{aspect-ratio:604/523}}" + rule + "'")
        pre = pre.replace("'brewery'", "'%s'" % key).replace('sx-brewery-card-css', 'sx-%s-card-css' % key).replace('data-sx-industry*="brewery"', 'data-sx-industry*="%s"' % key)
        assert 'brewery' not in pre
        custom = custom + '\n' + ENGINE.replace('@NS@', str(steps))
        out = ['/* ' + summary + '\n   Loaded by the site loader. Mounts into the card visual passed in by the loader.\n   Source of truth for this graphic: edit here, open a pull request, then release a new tag. */',
               '(function(){',
               "var SRC=document.currentScript&&document.currentScript.src;var BGU=SRC?new URL('bg-%d.jpg',SRC).href:'';" % n,
               'var CSS=' + json.dumps(css) + ".replace('__BG__',BGU);",
               'var BODY=' + json.dumps(body) + ';',
               pre.rstrip('\n'), self.scaffold.rstrip('\n'), custom.rstrip('\n'), self.tail.rstrip('\n')]
        res = '\n'.join(out) + '\n'
        d = os.path.join(out_dir, 'graphics', key); os.makedirs(d, exist_ok=True)
        open(os.path.join(d, 'card-%d.js' % n), 'w', encoding='utf-8').write(res)
        return len(res.encode())
