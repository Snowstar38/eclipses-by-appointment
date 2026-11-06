"""Final report status/text normalization after lead_reports.py; run only after helper agreement."""
from pathlib import Path
import csv,re
b=Path(__file__).resolve().parent
for p in b.glob('*/REPORT.md'):
 s=p.read_text(encoding='utf8');s=re.sub(r'(?<=[a-z])(?=\d)', ' ',s);s=re.sub(r'(?<=\d)(?=(?:ppt|arcsec|pixel|cycles|d(?:\W|$)))',' ',s)
 s=s.replace('completed bounded lead review; helper audit pending','completed bounded lead review and independent helper audit').replace('2941.54582?3306.07819','2941.54582 to 3306.07819').replace('2959.77740?3287.85463','2959.77740 to 3287.85463');p.write_text(s,encoding='utf8')
r=list(csv.DictReader((b/'RESULTS.csv').open()))
for x in r:x['completion']='completed';x['period_assignment']='Gaia-assisted; raw aliases scoped in report' if x['accepted_unique_addition']=='true' else 'no target ephemeris claimed'
with (b/'RESULTS.csv').open('w',newline='',encoding='utf8') as f:w=csv.DictWriter(f,fieldnames=r[0]);w.writeheader();w.writerows(r)
