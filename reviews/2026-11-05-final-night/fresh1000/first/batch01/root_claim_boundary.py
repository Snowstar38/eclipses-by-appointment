from pathlib import Path
import csv,re
b=Path(__file__).resolve().parent
p=b/'RESULTS.csv';rr=list(csv.DictReader(p.open()))
for r in rr:
 if r['tic'] in ['1269035','71295367','92872537']:
  r['source_eligibility']='HOST_UNCERTAIN';r['association']='UNRESOLVED_CLOSE_BLEND';r['limitations']=r['limitations'].replace('selected-source eligibility HOLD','selected host uncertain; root decides claim eligibility').replace('selected-source attribution is on hold','selected host uncertain; no positive off-target identification')
 r['claim_eligibility']='ROOT_OWNED'
with p.open('w',newline='',encoding='utf8') as f:w=csv.DictWriter(f,fieldnames=rr[0]);w.writeheader();w.writerows(rr)
for p in list(b.glob('*/REPORT.md'))+[b/'LEAD-AUDIT.md']:
 s=p.read_text();s=s.replace('UNRESOLVED_CLOSE_SOURCE_HOLD','UNRESOLVED_CLOSE_BLEND').replace('Publication/source eligibility: HOLD.','Host attribution: uncertain; claim eligibility is root owned.').replace('Source eligibility HOLD:','Host attribution uncertain:').replace('source eligibility HOLD','host attribution uncertain').replace('selected-source eligibility HOLD','selected host uncertain').replace('source HOLD','host uncertainty').replace('selected-source attribution is on hold','selected source is uncertain').replace('the selected Gaia source is not established','the selected Gaia source is uncertain').replace('a selected-target claim is not accepted','root decides claim eligibility under the paper standard').replace('cannot be silently counted as selected-target claims','require explicit root adjudication under the paper standard').replace('retain source eligibility HOLD','retain host uncertainty')
 s+='\n\nClaim adjudication: unresolved blends do not positively identify a neighbor-owned eclipse. Root applies the paper standard to P systems with host uncertainty separately from physical review. Only Z008 has a positive off-target attribution refutation. No automatic exclusion or novelty decision is made here.\n'
 if p.parent.name=='1269035':s+='\nZ001 target WCS(5.523,5.701), neighbor(5.939,5.133), centroid(5.676,5.210). The shift points toward a capable0.70pixel-separated neighbor, but no calibrated PRF fit establishes ownership.\n'
 if p.parent.name=='92872537':s+='\nZ005 target WCS(5.593,5.422), neighbor(5.770,4.765), centroid(5.498,5.472). The shift is mildly opposite the0.68pixel-separated neighbor, but no calibrated PRF fit excludes it.\n'
 p.write_text(s,encoding='utf8')
