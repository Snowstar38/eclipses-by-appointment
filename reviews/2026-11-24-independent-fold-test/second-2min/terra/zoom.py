import pathlib,numpy as np,matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
base=pathlib.Path(__file__).resolve().parent.parent; out=base/'terra'
jobs={'167710':[(38,2344.15)],'113655666':[(43,2491.3)],'187261476':[(59,2912.25),(59,2913.4),(59,2917.7),(59,2926.4)]}
for tic,events in jobs.items():
 fig,axes=plt.subplots(len(events),1,figsize=(10,2.6*len(events)),squeeze=False)
 for ax,(sec,c) in zip(axes[:,0],events):
  a=np.load(base/'sol'/'cadences'/f'{tic}-{sec}.npz'); t=a['t']; f=a['pdc']; valid=np.isfinite(t)&np.isfinite(f); t=t[valid]; f=f[valid]; y=(f/np.median(f)-1)*1000; m=abs(t-c)<.6
  ax.plot(t[m],y[m],'.',ms=2,color='#264e70'); ax.axhline(-10,color='#cb6d50',ls='--',lw=.8); ax.set_title(f'TIC {tic}, sector {sec}, BTJD near {c}',loc='left'); ax.set_xlabel('BTJD (days)'); ax.set_ylabel('ppt'); ax.grid(alpha=.2)
 fig.tight_layout(); fig.savefig(out/f'{tic}-zoom.png',dpi=150); plt.close(fig)
