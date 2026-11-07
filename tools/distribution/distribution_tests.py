"""Distribution test setup: points the shared harness (tools/electronics/testlib.py) at graphics/distribution-management-software and adds the distribution banned words."""
import os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(HERE), 'electronics'))
import testlib  # noqa: E402
testlib.KEY = 'distribution-management-software'
testlib.SHOTS = os.environ.get('GFX_SHOTS', '/tmp/distribution_shots')
os.makedirs(testlib.SHOTS, exist_ok=True)
# claim words from the brief, plus retailer and EDI provider names (case sensitive so plain words like "target" pass)
testlib.EXTRA_CLAIMS = re.compile(r'\d\s?%|(?i:percent|savings of|set up in|data residency|hosted in|certified|compliant)|\$\d|Walmart|Target|Home Depot|Lowe|Costco|Amazon|Grainger|Fastenal|McKesson|Kroger|SPS Commerce|TrueCommerce|Orderful|Cleo\b|Digit')
run_card, js = testlib.run_card, testlib.js
