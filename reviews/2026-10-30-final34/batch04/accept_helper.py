from pathlib import Path
import json
B=Path('.');a=json.load(open(B/'alias-check.json'))
old='supporting distinct primary/secondary events at the adopted orbital period rather than equal eclipses at P/2.';new='supporting unequal flux losses at the adopted orbital period rather than equal eclipses at P/2. Window losses alone do not establish a resolved secondary-eclipse shape.'
for tic,v in a.items():
 v['interpretation']=v['interpretation'].replace(old,new);p=B/'reports'/tic/'REPORT.md';p.write_text(p.read_text(encoding='utf-8').replace(old,new),encoding='utf-8')
(B/'alias-check.json').write_text(json.dumps(a,indent=2))
p=B/'LEAD-AUDIT.md';s=p.read_text(encoding='utf-8').replace('Provisional result four CONFIRMED','Final lead result four CONFIRMED').replace('Await independent helper audit before final acceptance.','Independent Terra helper audit accepted all four; non-blocking half-phase wording correction was applied. See HELPER-AUDIT.md for independently recalculated periods and source assessment.');p.write_text(s,encoding='utf-8')
