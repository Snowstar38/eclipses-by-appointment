import csv, pathlib, numpy as np, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
base=pathlib.Path(__file__).resolve().parent.parent; out=base/'terra'; rows=list(csv.DictReader(open(base/'batch.csv')))
for row in rows:
 tic=row['tic']; sectors=row['sectors'].split('|'); fig,axes=plt.subplots(len(sectors),1,figsize=(14,3.2*len(sectors)),squeeze=False)
 for ax,sec in zip(axes[:,0],sectors):
  f=base/'sol'/'cadences'/f'{tic}-{sec}.npz'
  if not f.exists(): ax.text(.5,.5,'Missing archive data',transform=ax.transAxes); continue
  a=np.load(f); t=a['t']; y=a['pdc']; ok=np.isfinite(t)&np.isfinite(y); t=t[ok]; y=y[ok]; y=(y/np.median(y)-1)*1000
  ax.plot(t,y,'.',ms=.65,alpha=.45,color='#264e70',rasterized=True)
  # show same robust scale procedure on each sector, with at least +-30 ppt
  lo,hi=np.percentile(y,[.1,99.9]); span=min(100, max(30, abs(lo)*1.2,abs(hi)*1.2)); ax.set_ylim(-span,span)
  ax.axhline(-10,color='#cb6d50',lw=.8,ls='--'); ax.axhline(0,color='gray',lw=.5)
  ax.set_title(f'TIC {tic}  |  Sector {sec}  |  PDCSAP, quality = 0',loc='left',fontsize=10); ax.set_ylabel('relative flux (ppt; clipped at plot limits)'); ax.set_xlabel('BTJD (days)'); ax.grid(alpha=.18)
 fig.tight_layout(); fig.savefig(out/f'{tic}.png',dpi=150); plt.close(fig)
