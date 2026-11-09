"""Plastics test setup: points the shared harness (tools/electronics/testlib.py) at graphics/plastics and adds the plastics banned words."""
import os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(HERE), 'electronics'))
import testlib  # noqa: E402
testlib.KEY = 'plastics'
testlib.SHOTS = os.environ.get('GFX_SHOTS', '/tmp/plastics_shots')
os.makedirs(testlib.SHOTS, exist_ok=True)
# compliance and certification names, machine monitoring words, size words, prices, "formula" as a noun, real resin brands and real customers
# (case sensitive brand list so plain words pass)
testlib.EXTRA_CLAIMS = re.compile(
    r'IATF|\bISO\b|PPAP|\bFDA\b|\bOEE\b|\bPLC\b|(?i:cycle time|downtime|monitoring|telemetry|energy use|shot count|maintenance|\bformula\b|\bsmall\b|mid-sized|midsize|affordable|certified|compliant|savings of|set up in)'
    r'|\$\d|Dow\b|ExxonMobil|Exxon|LyondellBasell|SABIC|Borealis|INEOS|Braskem|Chevron|Formosa|TotalEnergies|Ampacet|Clariant|Avient|PolyOne|Marlex|Pro-fax|Coca|Pepsi|Nestl|Kraft|Unilever|Walmart|Target\b|Digit')
run_card, js = testlib.run_card, testlib.js
