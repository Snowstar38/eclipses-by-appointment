import json,numpy as np
from pathlib import Path
from astropy.io import fits
import matplotlib;matplotlib.use('Agg');import matplotlib.pyplot as plt
B=Path(__file__).resolve().parent;C=json.loads((B/'coverage-alias.json').read_text());D=json.loads((B/'SOURCE-SNAPSHOT.json').read_text());fig,axs=plt.subplots(6,1,figsize=(10,12));rows=[]
for ax,(tic,sec,kind,cyc) in zip(axs,[('207780183',65,'half',67),('207780183',99,'half',111),('207780183',99,'half',112),('207780183',100,'half',113),('207780183',102,'half',115),('121277143',53,'same',50)]):
 w=next(x for x in C[tic]['windows'] if x['sector']==sec and x['kind']==kind and x['cycle']==cyc);fp=next(x['path'] for x in D[tic]['target']['file_receipts'] if x['sector']==sec)
 with fits.open(fp) as h:a=h[1].data;t=np.array(a['TIME']);f=np.array(a['SAP_FLUX']);q=np.array(a['QUALITY'])
 x=t-w['predicted_btjd'];z=np.isfinite(x)&np.isfinite(f)&(abs(x)<1.2);base=np.median(f[z&(abs(x)>.8)&(q==0)]);ax.plot(x[z&(q==0)],f[z&(q==0)]/base,'.',ms=2);ax.plot(x[z&(q!=0)],f[z&(q!=0)]/base,'rx',ms=3);ax.set_title(f'{tic} s{sec} cycle {cyc} predicted {w["predicted_btjd"]:.4f}');ax.axvline(0,color='k',lw=.5);ax.set_ylim(.90,1.04);rows.append(w)
fig.tight_layout();fig.savefig(B/'helper-pixels'/'exceptions.png',dpi=130);(B/'helper-pixels'/'exceptions.json').write_text(json.dumps(rows,indent=2)+'\n',encoding='utf8')
