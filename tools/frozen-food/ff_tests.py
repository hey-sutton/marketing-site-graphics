"""Frozen food test setup: the Automotive harness (tools/automotive/auto_tests.py) pointed at graphics/frozen-food,
with food brand, grocer and supplier names added to the banned words."""
import os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(HERE), 'automotive'))
import auto_tests  # noqa: E402
from auto_tests import run_card, finish, js, pill, testlib  # noqa: E402,F401

testlib.KEY = 'frozen-food'
testlib.SHOTS = os.environ.get('GFX_SHOTS', '/tmp/frozen_shots')
os.makedirs(testlib.SHOTS, exist_ok=True)
testlib.EXTRA_CLAIMS = re.compile(testlib.EXTRA_CLAIMS.pattern + r'|\b(?:recipes?|Tyson|Nestle|Conagra|Birds Eye|Stouffer|Lean Cuisine|Kraft|Heinz|Pinnacle|Kroger|Walmart|Costco|Sysco|Lineage|Americold|US Foods|Mid)\b', re.I)


def ids(pg, *names):
    return js(pg, "return %r.map(function(i){var e=r.getElementById(i);return e?e.textContent:null}).join('|')" % list(names))
