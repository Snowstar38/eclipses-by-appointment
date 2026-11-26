"""Check counts stated in paper.html against the release tables.

1. Abstract method totals against current-accounting.json (accepted_all_method_totals).
2. That the accounting's method totals sum to accepted-systems.csv.
3. The A-labelled table (A-number, TIC, name, G, method, status) against accepted-systems.csv:
   method counts among counted A claims, and status mismatches.
4. Repeats of the stale G 11-11.5 yield sentence.
Usage: python3 reviews/duet-findings/paper-text/paper_counts.py
"""
import re, html, json, collections
import pandas as pd

raw = open('paper.html', encoding='utf-8').read()
body = re.sub(r'<(script|style)[^>]*>.*?</\1>', '', raw, flags=re.S)
text = re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', body)))
acc = json.load(open('current-accounting.json'))
tot = acc['accepted_all_method_totals']
rel = pd.read_csv('accepted-systems.csv')

print('1. Abstract method totals')
ab = text[text.index('Abstract'):text.index('Introduction')]
checks = [('Gaia-orbit period folds contribute (\\d+)', 'Gaia_period_fold'),
          ('period-free follow-up contributes (\\d+)', 'period_free_dip_screening'),
          ('faint-band conjunction and raw-event search contributes (\\d+)', 'faint_band_conjunction_and_raw_event'),
          ('and (\\d+) are accepted claims \\(', 'period_free_dip_screening')]
for pat, key in checks:
    m = re.search(pat, ab)
    v = int(m.group(1)) if m else None
    print(f'  "{pat[:45]}": abstract {v}, accounting {key} = {tot[key]}', '' if v == tot[key] else '  <-- differs')

s = sum(tot.values())
print(f'2. Accounting method totals sum to {s}; accepted-systems.csv has {len(rel)}'
      f' ({(rel.tier=="confirmed").sum()} confirmed, {(rel.tier=="probable").sum()} probable)')

print('3. A-labelled table')
rows = re.findall(r'<tr><td>(A\d+)</td><td>(\d+)</td><td>(.*?)</td><td>([\d.]+)</td><td>(.*?)</td><td>(.*?)</td></tr>', raw)
tab = {r[0]: (html.unescape(r[4]), html.unescape(r[5]), int(r[1])) for r in rows}
A = rel[rel.review_id.str.startswith('A')].set_index('review_id')
print(f'  {len(tab)} table rows; {len(A)} counted A claims; all counted rows present: {set(A.index) <= set(tab)}')
print('  methods among counted A claims:', dict(collections.Counter(tab[k][0] for k in A.index)))
print('  status differs from the release:', [(k, tab[k][1], A.tier[k]) for k in A.index if tab[k][1] != A.tier[k]])
print('  uncounted rows not marked "not counted":',
      [k for k in tab if k not in A.index and 'not counted' not in tab[k][1]])

print('4. Stale yield sentence')
stale = 'At G 11–11.5 the first twenty of fifty candidates re-analysed were all eclipsing systems'
print(f'  occurrences in paper.html text: {text.count(stale)}')
