"""Repair inherited text encoding in lead report generator and record hashes."""
import hashlib,json
from pathlib import Path
B=Path(__file__).resolve().parent;p=B/'write_reports.py'
before=hashlib.sha256(p.read_bytes()).hexdigest()
s=p.read_text(encoding='utf-8')
for wrong,right in [('\u00e2\u20ac\u201d',' - '),('\u00e2\u20ac\u201c','-'),('\u00e2\u2030\u00a5','>='),('\u00c2\u00b1','+/-'),('\u00b1','+/-')]:
    s=s.replace(wrong,right)
s=s.replace('../shared-catalogues/REPORT.md','../../shared-catalogues/REPORT.md')
s=s.replace("p=f\"{k['period_days']:.9f}\"","p=f\"{k['period_days']:.5f}\"")
s=s.replace("err=f\"{k['period_error_days']:.9f}\"","err=f\"{k['period_error_days']:.5f}\"")
s=s.replace("epoch=f\"{k['epoch_btjd']:.8f}\"","epoch=f\"{k['epoch_btjd']:.5f}\"")
p.write_text(s,encoding='utf-8')
after=hashlib.sha256(p.read_bytes()).hexdigest()
(B/'lead-text-conversion.json').write_text(json.dumps({'file':'write_reports.py','before_sha256':before,'after_sha256':after,'action':'Sol lead repaired mojibake source strings, corrected relative shared-catalogue link and rounded CSV display precision; numerical fits unchanged.'},indent=2)+'\n',encoding='utf-8')
print(before,after)
