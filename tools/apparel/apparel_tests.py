"""Apparel test setup: points the shared harness (tools/electronics/testlib.py) at graphics/apparel and adds the apparel banned words."""
import os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(HERE), 'electronics'))
import testlib  # noqa: E402
testlib.KEY = 'apparel'
# claim words from the brief, plus retailer and EDI provider names (case sensitive so plain words like "target" pass)
testlib.EXTRA_CLAIMS = re.compile(r'GOTS|OEKO|\bWRAP\b|(?i:customs compliant|tariff compliant|certified)|Walmart|Target|Nordstrom|Macy|Amazon|Costco|Kohl|Zara|SPS Commerce|TrueCommerce|Orderful|Cleo\b')
run_card, js = testlib.run_card, testlib.js
