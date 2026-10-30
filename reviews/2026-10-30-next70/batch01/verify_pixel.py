from astropy.io import fits
from astropy.wcs import WCS
from pathlib import Path
import json,hashlib,shutil,subprocess,sys,numpy as np
B=Path('[local working path omitted; see provenance receipts]');r=json.loads((B/'raw-evidence/raw-events.json').read_text())['414008363'];p=Path('[local working path omitted; see provenance receipts]');T=json.loads((B.parent/'targets-selected.json').read_text())['414008363'];receipt={}
with fits.open(p) as h:
 w=WCS(h[2].header);x,y=w.all_world2pix(float(T['gaia']['ra']),float(T['gaia']['dec']),0);receipt=dict(path=str(p),sha256=hashlib.sha256(p.read_bytes()).hexdigest(),sector=h[0].header.get('SECTOR'),shape=list(h[1].data['FLUX'].shape),target_xy=[float(x),float(y)],quality_present='QUALITY'in h[1].data.columns.names)
assert receipt['sector']==91 and 0<x<15 and 0<y<15
(B/'414008363-pixel-provenance.json').write_text(json.dumps(receipt,indent=2))
script=B/'raw-evidence'/'rerun_diffstack.py';shutil.copyfile('[local working path omitted; see provenance receipts] 5/made/sb1-scale/diffimg/diffstack.py',script)
wd=B/'raw-evidence/414008363';shutil.copyfile('[local working path omitted; see provenance receipts] 5/made/sb1-scale/diffimg/414008363/gaia.json',wd/'gaia.json')
ep=r['representative_ephemeris'];ev=[e for e in r['events'] if 'duration_d'in e];cmd=[sys.executable,str(script),'414008363','91',str(ep['period_d']),str(ep['epoch_btjd']),str(np.median([e['duration_d'] for e in ev])*24),str(np.median([e['depth'] for e in ev])),'rechecked']
z=subprocess.run(cmd,cwd=wd,capture_output=True,text=True);(B/'pixel-rerun-log.txt').write_text(z.stdout+z.stderr);print(z.returncode,z.stdout[:1000])

