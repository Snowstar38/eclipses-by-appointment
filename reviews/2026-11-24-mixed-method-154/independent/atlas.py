"""Plot fixed-period folds for trials that recover in later sectors."""
import argparse
import csv
import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import binned_statistic

from search import HERE, read


def main(cache):
    records=[]
    for f in sorted((HERE/'trials').glob('*.json')):
        obj=json.loads(f.read_text())
        good=[c for c in obj['clocks'] if c['test_covered']>=2 and c['train_covered']>=3
              and c['test_hits']>=.8*c['test_covered'] and c['train_hits']>=.75*c['train_covered']]
        if good:
            records.append((obj,max(good,key=lambda c:(c['test_hits']/c['test_covered'],
                                                       c['train_hits']/c['train_covered']))))
    summary=[]
    for k in range(0,len(records),8):
        fig,axes=plt.subplots(4,2,figsize=(12,10),layout='constrained')
        for ax,(obj,c) in zip(axes.flat,records[k:k+8]):
            tic=obj['tic']
            summary.append(dict(tic=tic,**c))
            files=[read(f) for f in sorted(cache.glob(tic+'_s*.fits'))]
            for istrain,color,label in [(True,'#7555a8','early'),(False,'#098476','later')]:
                parts=[a for a in files if a is not None and (a[0] in obj['train_sectors'])==istrain]
                t=np.concatenate([a[1] for a in parts])
                y=np.concatenate([a[2][int(c['channel']=='corrected')] for a in parts])
                phase=(t-c['epoch_btjd'])/c['period_d']
                ph=((phase+.5)%1)-.5
                edges=np.linspace(-.5,.5,81)
                med=binned_statistic(ph,y,'median',edges)[0]
                ax.plot((edges[:-1]+edges[1:])/2,med,color=color,label=label,lw=1.6)
            ax.axvline(0,color='gray',lw=.6)
            ax.set_title(f"TIC {tic}     {c['period_d']:.5f} d     {c['channel']}")
            ax.set_xlabel('Phase from fitted event')
            ax.set_ylabel('Flux residual (ppt)')
        for ax in axes.flat[len(records[k:k+8]):]:ax.set_visible(False)
        axes[0,0].legend()
        fig.savefig(HERE/f'folds-{1+k//8}.png',dpi=135)
        plt.close(fig)
    with (HERE/'later-repeats.csv').open('w',newline='') as f:
        w=csv.DictWriter(f,summary[0],lineterminator='\n')
        w.writeheader()
        w.writerows(summary)


if __name__=='__main__':
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('cache',type=Path)
    main(ap.parse_args().cache)
