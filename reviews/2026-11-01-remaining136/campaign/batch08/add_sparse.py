from pathlib import Path
import json,requests,hashlib
b=Path(__file__).parent;t=json.load(open(b.parent/'targets-selected.json'))['297956126'];sec,uri=next(x for x in t['qlp'] if x[0]==66);d=b/'additional-qlp';d.mkdir(exist_ok=True);p=d/'297956126_s066.fits'
if not p.exists():
 r=requests.get('httplocal-source/omitted
json.dump(dict(tic='297956126',sector=sec,uri=uri,path=str(p),sha256=hashlib.sha256(p.read_bytes()).hexdigest()),open(b/'additional-download-receipt.json','w'),indent=2)
s=(b/'review_measure.py').read_text().replace("sorted((BASE.parent/'shared-qlp').glob(tic+'_s*.fits'))","sorted(list((BASE.parent/'shared-qlp').glob(tic+'_s*.fits'))+list((BASE/'additional-qlp').glob(tic+'_s*.fits')))")
(b/'review_measure.py').write_text(s)
