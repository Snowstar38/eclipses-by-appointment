"""Repair Windows-1252 misdecoding introduced by a PowerShell source edit."""
from pathlib import Path
import re
p=Path(__file__).resolve().parent/'write_results.py'
s=p.read_text(encoding='utf-8-sig')
def repair(m):
    return m.group().encode('cp1252').decode('utf8')
s,n=re.subn(r'[\u00e2\u00c3][\u0080-\u00ff\u0152\u0153\u0160\u0161\u0178\u0192\u02c6\u02dc\u2013-\u2026\u2030\u2039\u203a\u20ac\u2122]{1,2}',repair,s)
s=s.replace('\u00c2\u00b1','\u00b1')
p.write_text(s,encoding='utf8',newline='\n')
print('repaired',n,'remaining mojibake heads',s.count('\u00e2'),s.count('\u00c3'))
