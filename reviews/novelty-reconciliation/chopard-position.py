import csv,math,pathlib
p=pathlib.Path(r'C:\Home\Fable 5.1\made\paper\work\novelty-reconciliation');e=next((p/'chopard-evidence/extracted').iterdir());
def read(x):
 with x.open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))
a=read(p/'chopard-coverage.csv');t=read(e/'track3_detail.csv');h=[]
for x in a:
 if not x['ra'] or not x['dec']:continue
 for y in t:
  ra,dec=float(x['ra']),float(x['dec']);d=float(y['dec']);sep=3600*math.hypot((ra-float(y['ra']))*math.cos(math.radians((dec+d)/2)),dec-d)
  if sep<=20:h.append(dict(label=x['label'],tic=x['tic'],gaia=y['source_id'],sep_arcsec=round(sep,3),period=y['period']))
with (p/'chopard-positional.csv').open('w',encoding='utf-8',newline='') as f:
 w=csv.DictWriter(f,fieldnames=['label','tic','gaia','sep_arcsec','period']);w.writeheader();w.writerows(h)
print(h)
