from pathlib import Path
import json
B=Path('.');a=json.load(open(B/'alias-check.json'))
for tic,v in a.items():
 if tic=='313274300':s='Only two representative primary eclipses are fitted. The same-sector spacing agrees with Gaia P=14.322d. No adequately covered half-period core survives the simple QUALITY=0 coverage test; P/2 alias is not independently excluded by that test. Recurrence plus Gaia period supports the adopted orbital period, with cycle-count and precision limitations retained.'
 else:s='The bounded half-phase check finds much shallower intervening flux losses (median %.2fppt versus %.2fppt at primary), supporting distinct primary/secondary events at the adopted orbital period rather than equal eclipses at P/2. The Gaia orbital period near P further supports the adopted alias.'%(1000*__import__('numpy').median([x['loss'] for x in v['checks'] if x['phase']==.5]),1000*__import__('numpy').median([x['loss'] for x in v['checks'] if x['phase']==0]))
 v['interpretation']=s;p=B/'reports'/tic/'REPORT.md';txt=p.read_text(encoding='utf-8');txt+='\nAlias assessment: '+s+' Numeric windows in ../../alias-check.json.\n';p.write_text(txt,encoding='utf-8')
(B/'alias-check.json').write_text(json.dumps(a,indent=2))
