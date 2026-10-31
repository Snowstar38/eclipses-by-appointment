from pathlib import Path
import csv,json,hashlib
b=Path(__file__).parent
for p in b.glob('*/REPORT.md'):
 s=p.read_text(encoding='utf-8'); s=s.replace(chr(195)+chr(130)+'+/-','+/-').replace(chr(194)+'+/-','+/-');p.write_text(s,encoding='utf-8')
q=list(csv.DictReader(open(b/'queue.csv'))); ms={r['tic']:json.load(open(b/r['tic']/'measurements.json')) for r in q}
print('excluded',[(t,e['sector'],e['cycle'],e.get('timing_failure_reason')) for t,m in ms.items() for e in m['events'] if not e.get('timing_usable',False)])
print('pairs',[(t,a['within_sector_same_kind_pairs']) for t,a in json.load(open(b/'alias-audit.json')).items()])
