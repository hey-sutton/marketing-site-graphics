"""Builds Dairy cards 2 to 4. Usage: GFX_REPO=/path/to/checkout-with-brewery GFX_OUT=/path/to/output-repo python3 build.py [2 3 4]"""
import os,sys,importlib
HERE=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,HERE)
from gfx_scaffold import Scaffold
REPO=os.environ.get('GFX_REPO','marketing-site-graphics'); OUT=os.environ.get('GFX_OUT','out')
sc=Scaffold(REPO)
want=[int(a) for a in sys.argv[1:]] or [2,3,4]
for n in want:
    m=importlib.import_module('card%d'%n)
    size=sc.build('dairy',n,m.SUMMARY,m.ARIA,m.WIN,Scaffold.studio(m.LEDE,m.EXAMPLES,m.BUILT_ON),m.CSS,m.JS,OUT,steps=5)
    print('card',n,size,'bytes')
