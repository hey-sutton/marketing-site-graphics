#!/usr/bin/env python3
"""Turn the exact code of existing Webflow embeds into a graphic file for this repo.

Usage:
  python3 tools/fragments-to-card.py "Title" graphics/<key>/card-<n>.js embed1.html embed2.html ...

List the embeds in the same order they sit in the card visual in Webflow. The code is
kept byte for byte and mounted in that order, so the graphic behaves exactly as it did
as embeds. If any element id from the embeds already exists on the page (the old embeds
are still visible), the file does nothing, so the cutover is safe.
"""
import json, sys

TEMPLATE = r"""/* __TITLE__
   Original embed code, mounted in order by the site loader. */
(function(){
var F=__FRAGMENTS__;
var c=document.currentScript&&document.currentScript.sxCard;
if(!c||c.hasAttribute('data-sxg-mounted'))return;
var probe=document.createElement('template');probe.innerHTML=F.join('');
var ids=[].slice.call(probe.content.querySelectorAll('[id]'));
for(var i=0;i<ids.length;i++){if(document.getElementById(ids[i].id))return;}
c.setAttribute('data-sxg-mounted','1');
F.forEach(function(h){
var w=document.createElement('div');
w.className='w-embed'+(/^\s*<script/i.test(h)?' w-script':'');
c.appendChild(w);
var t=document.createElement('template');t.innerHTML=h;
[].slice.call(t.content.childNodes).forEach(function(n){
if(n.nodeName==='SCRIPT'){
var s=document.createElement('script');
[].slice.call(n.attributes).forEach(function(a){s.setAttribute(a.name,a.value);});
s.text=n.textContent;
w.appendChild(s);
}else{w.appendChild(n);}
});
});
})();
"""

def main():
    if len(sys.argv) < 4:
        print(__doc__); sys.exit(1)
    title, out, files = sys.argv[1], sys.argv[2], sys.argv[3:]
    frags = [open(f, encoding='utf-8').read() for f in files]
    js = TEMPLATE.replace('__TITLE__', title).replace('__FRAGMENTS__', json.dumps(frags))
    open(out, 'w', encoding='utf-8').write(js)
    print('wrote', out, len(js), 'chars from', len(frags), 'embeds')

if __name__ == '__main__':
    main()
