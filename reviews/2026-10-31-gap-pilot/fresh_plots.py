import pathlib,json,sys
import numpy as np
import matplotlib;matplotlib.use('Agg')
import matplotlib.pyplot as plt
O=pathlib.Path(__file__).parent;sys.path.insert(0,str(O));from plot_pilots import read
N=int(sys.argv[1]) if len(sys.argv)>1 else 48
a=[json.loads(l) for l in open(O/f'fresh-results-{N}.jsonl')]
sel=[r for r in a if r.get('best') and r['best']['snr']>8 and r['best'].get('far') and .6<r['best']['far']<1.6 and r['best']['halves']]
if len(sys.argv)>2 and sys.argv[2]=='new':
 old=set(json.load(open(O/'fresh-targets-48.json')));sel=[r for r in sel if r['tic'] not in old]
for r in sel:
 k=r['tic'];fig,axs=plt.subplots(2,1,figsize=(11,5));b=r['best'];t,f=read(O/'fresh-data'/f"{k}_s{b['sector']:03d}.fits");axs[0].plot(t,(f-1)*1000,'.',ms=1);m=abs(t-b['t'])<3;axs[1].plot(t[m]-b['t'],(f[m]-1)*1000,'.',ms=2);axs[1].axvline(0,c='r',lw=.5);axs[0].set_title(f"TIC{k} P{r['P_gaia']}d {b['kind']} s{b['sector']} offset{b['dphase']}phase z{r.get('z')}")
 fig.tight_layout();fig.savefig(O/f'fresh-{k}.png',dpi=100);plt.close(fig)
# One compact montage for all threshold-selected events.
fig,axs=plt.subplots((len(sel)+2)//3,3,figsize=(15,3*((len(sel)+2)//3)))
for ax,r in zip(axs.flat,sel):
 b=r['best'];t,f=read(O/'fresh-data'/f"{r['tic']}_s{b['sector']:03d}.fits");m=abs(t-b['t'])<3;ax.plot(t[m]-b['t'],(f[m]-1)*1000,'.',ms=1);ax.axvline(0,c='r',lw=.5);ax.set_title(r['tic'],fontsize=9)
fig.tight_layout();fig.savefig(O/f'fresh{N}-montage{"-new" if len(sys.argv)>2 else ""}.png',dpi=110)
