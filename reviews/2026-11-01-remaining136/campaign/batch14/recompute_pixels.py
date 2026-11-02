import json,subprocess,shutil,numpy as np
from pathlib import Path
b=Path('Astra/made/remaining136-2026-11-01/batch14').resolve();orig=Path('Fable 5/made/sb1-scale/diffimg').resolve()
for p in b.glob('*/measurements.json'):
 tic=p.parent.name;m=json.load(open(p));h=p.parent/'historical';h.mkdir(exist_ok=True);src=next((orig/tic).glob('diff_s*.json'));d=json.load(open(src))
 for f in [src,src.with_suffix('.png'),src.parent/'gaia.json']:shutil.copy2(f,h/f.name)
 out=p.parent/'fresh-pixels';out.mkdir(exist_ok=True);shutil.copy2(src.parent/'gaia.json',out/'gaia.json')
 dur=np.median([e['duration_days'] for e in m['events'] if e.get('timing_usable')])*24
 z=subprocess.run(['python',str(b/'diffstack-primitive.py'),tic,str(d['sector']),str(m['period_days']),str(m['primary_epoch_btjd']),str(dur),str(m['depth_ppt']/1000),'fresh'],cwd=out,capture_output=True,text=True)
 (out/'run.log').write_text(z.stdout+z.stderr);print(tic,z.returncode)
