import argparse
import csv
import json
import math
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from astropy.io import fits
from astropy.timeseries import BoxLeastSquares
from scipy.ndimage import uniform_filter1d
from scipy.signal import find_peaks

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2] if (HERE.parents[2]/"sky/data/qlp-sb-p20-60").is_dir() else HERE.parent/"inputs/workspace"
parser = argparse.ArgumentParser()
parser.add_argument('--fits-dir', type=Path, default=ROOT/'sky/data/qlp-sb-p20-60')
parser.add_argument('--prior-dir', type=Path, default=ROOT/'Astra/made/binary-exploration-2026-11-04/bulk-results')
parser.add_argument('--mask', type=Path, default=ROOT/'sky/mixed-fold-2026-11-24/cadence-controls/flagged-exposures.csv')
args = parser.parse_args()
plots = HERE/'plots'
plots.mkdir(exist_ok=True)


def rows(path):
    with path.open(newline='', encoding='utf-8-sig') as stream:
        return list(csv.DictReader(stream))


def save(name, records):
    with (HERE/name).open('w', newline='', encoding='utf-8') as stream:
        writer = csv.DictWriter(stream, records[0].keys())
        writer.writeheader()
        writer.writerows(records)


def continuum(t, f, step=0.3, scale=1.8):
    grid = np.arange(t[0], t[-1]+step, step)
    i0 = np.searchsorted(t, grid-scale/2)
    i1 = np.searchsorted(t, grid+scale/2)
    baseline = np.array([np.median(f[a:b]) if b-a>=5 else np.nan for a,b in zip(i0,i1)])
    ok = np.isfinite(baseline)
    return f/np.interp(t, grid[ok], baseline[ok])-1


def window(t, signal, center, width, cadence):
    d = t-center
    core = abs(d)<=width/2
    left = (d>=-1.75*width)&(d<-.65*width)
    right = (d>.65*width)&(d<=1.75*width)
    n = np.array([core.sum(), left.sum(), right.sum()])
    coverage = n*cadence/width
    if min(n)<2 or min(coverage)<.55:
        return np.nan, np.nan, n[0], min(coverage)
    med = [np.median(signal[m]) for m in (left,right)]
    time = [np.median(d[m]) for m in (left,right)]
    model = np.interp(d[core], time, med)
    residual = np.concatenate([signal[m]-np.interp(d[m], time, med)
                               for m in (left,right)])
    sigma = max(1e-6, 1.4826*np.median(abs(residual-np.median(residual))))
    return 1000*np.median(model-signal[core]), 1000*sigma, n[0], min(coverage)


mask = {}
for row in rows(args.mask):
    if row['screen_flag'].lower()=='true' and row['pipeline']=='QLP':
        mask.setdefault((int(row['sector']),int(row['camera'])),set()).add(int(row['cadenceno']))

events, clocks, predictions, files = [], [], [], []
single_event_checks = []
fine_seeds = {'410900361':[3.0911], '329642297':[.86107], '137417837':[.5895], '253463221':[1.0832,1.0885], '193630960':[2.277], '137203172':[19.6611,60.9446]}
for row in rows(HERE/'batch.csv'):
    tic = row['tic']
    known = json.loads((args.prior_dir/f'{tic}.json').read_text())['files']
    paths = set(args.fits_dir.glob(f'{tic}_s*.fits'))
    for entry in known:
        old = Path(entry['path'].replace('\\','/'))
        for path in (old, ROOT.joinpath(*old.parts[2:]), args.fits_dir/old.name):
            if path.is_file():
                paths.add(path.resolve())
                break
    sectors = {}
    for path in sorted(set(p.resolve() for p in paths)):
        with fits.open(path) as hdu:
            sector = hdu[0].header['SECTOR']
            cam = hdu[0].header['CAMERA']
            ccd = hdu[0].header['CCD']
            z = hdu[1].data
            correction = next((key for key in ('KSPSAP_FLUX','PDCSAP_FLUX','DET_FLUX') if key in z.names),None)
            if correction is None:
                print(path.name,z.names,flush=True)
                continue
            good = (z['QUALITY']==0)&np.isfinite(z['TIME'])&np.isfinite(z['SAP_FLUX'])&np.isfinite(z[correction])
            bad = np.isin(z['CADENCENO'], list(mask.get((sector,cam),())))
            t, sap, cor = (np.asarray(z[name][good&~bad],float) for name in ('TIME','SAP_FLUX',correction))
            cadence = np.median(np.diff(t))
            if sector in sectors:
                continue
            sectors[sector] = (t, sap/np.median(sap)-1, cor/np.median(cor)-1,cadence)
            files.append(dict(tic=tic,sector=sector,camera=cam,ccd=ccd,file=path.name,corrected_column=correction,start=t[0],end=t[-1],cadence=cadence,n=len(t),masked=int((bad&good).sum())))
    t_search, y_search, e_search = [], [], []
    prior = []
    for s,(t,sap,cor,cadence) in sectors.items():
        residual = continuum(t,cor+1)
        if tic=='137203172':
            for width in (.04,.06,.09,.12):
                for indices in np.split(np.arange(len(t)), np.flatnonzero(np.diff(t)>2.5*cadence)+1):
                    npoint = max(2,round(width/cadence))
                    if len(indices)<5*npoint:
                        continue
                    smoothed = uniform_filter1d(residual[indices],size=npoint,mode='nearest')
                    candidates,_ = find_peaks(-smoothed,height=.002,distance=3*npoint)
                    for i in candidates:
                        c = t[indices[i]]
                        cd, cs, n, cov = window(t,cor,c,width,cadence)
                        rd, rs, *_ = window(t,sap,c,width,cadence)
                        if cd>=2 and rd>=2:
                            single_event_checks.append(dict(tic=tic,sector=s,center_btjd=c,width_d=width,
                                                       core_n=n,coverage=cov,corrected_depth_ppt=cd,
                                                       corrected_scatter_ppt=cs,raw_depth_ppt=rd,raw_scatter_ppt=rs))
        sigma = max(.00003,1.4826*np.median(abs(residual-np.median(residual))))
        take = slice(None,None,max(1,round(.021/cadence)))
        t_search.extend(t[take])
        y_search.extend(np.clip(residual[take], -10*sigma, 6*sigma))
        e_search.extend(np.full(len(t[take]),sigma))
        for entry in known:
            if s!=entry['sector']:
                continue
            for hit in entry.get('windows',[]):
                if hit['kind']=='dip' and hit['flag']:
                    prior.append((s,hit['time'],hit['duration']))
    bls = BoxLeastSquares(t_search,y_search,e_search)
    pg = float(row['gaia_period_days'])
    fixed = bls.power([pg,pg/2,pg*2],[.08,.16,.32,.55],oversample=8,objective='snr')
    solutions = [(name,fixed,i) for i,name in enumerate(('Gaia','Gaia/2','2*Gaia'))]
    periodogram = bls.autopower([.08,.16,.32,.55],minimum_period=1.5,maximum_period=65,frequency_factor=2500,oversample=4,objective='snr')
    peaks = []
    for ind in np.argsort(periodogram.power)[::-1]:
        p = periodogram.period[ind]
        if all(abs(p-other)/other>.002 for other in peaks):
            peaks.append(p)
            solutions.append((f'BLS {len(peaks)}',periodogram,ind))
        if len(peaks)==4:
            break
    ds = np.array(t_search)-min(t_search)
    for name, subset in (('Early',ds<100),('Late',ds>max(ds)-100)):
        if sum(subset)<400:
            continue
        span = BoxLeastSquares(np.asarray(t_search)[subset],np.asarray(y_search)[subset],np.asarray(e_search)[subset])
        local_search = span.autopower([.08,.16,.32,.55],minimum_period=.65,maximum_period=25,frequency_factor=12,oversample=4,objective='snr')
        solutions.append((name,local_search,np.argmax(local_search.power)))
    for num, seed in enumerate(fine_seeds.get(tic,()),1):
        span = max(t_search)-min(t_search)
        step = .024*seed**2/span
        grid = np.arange(seed*.997,seed*1.003,step)
        fine = bls.power(grid,[.06,.08,.12,.16,.25,.36,.55],oversample=6,objective='snr')
        solutions.append((f'Fine {num}',fine,np.argmax(fine.power)))
    previous = []
    for s,c,w in prior:
        t,sap,cor,dt = sectors[s]
        cd, cs, n, cov = window(t,cor,c,w,dt)
        rd, rs, *_ = window(t,sap,c,w,dt)
        events.append(dict(tic=tic,sector=s,center_btjd=c,width_d=w,core_n=n,coverage=cov,corrected_depth_ppt=cd,corrected_scatter_ppt=cs,raw_depth_ppt=rd,raw_scatter_ppt=rs))
        previous.append((s,c,w))
    collections = [('prior',previous)]
    trial_ephemerides = [(name, *(float(getattr(result,j)[ind]) for j in ('period','transit_time','duration','power')))
                        for name,result,ind in solutions]
    if tic=='410900361':
        _,p,c,w,_ = next(x for x in trial_ephemerides if x[0]=='Fine 1')
        trial_ephemerides.extend([('Fine 1 half',p/2,c,w,np.nan),('Fine 1 double',2*p,c,w,np.nan)])
    for name,p,c,w,snr in trial_ephemerides:
        clocks.append(dict(tic=tic,clock=name,period_d=p,epoch_btjd=c,width_d=w,snr=snr))
        local = []
        if name in ('Fine 1','Fine 2','Fine 1 double'):
            fig, axes = plt.subplots(len(sectors),2,figsize=(11,1.45*len(sectors)),squeeze=False,layout='constrained',sharex=True)
            edges = np.linspace(-.5,.5,101)
            for (sector,(t,sap,cor,dt)), (ar,ac) in zip(sectors.items(),axes):
                ph = (t-c+p/2)%p/p-.5
                for ax,f in ((ar,sap),(ac,cor)):
                    f = continuum(t,1+f,scale=max(1.8,3*w))
                    binmed = np.array([np.median(f[(ph>=a)&(ph<b)]) if np.any((ph>=a)&(ph<b)) else np.nan for a,b in zip(edges[:-1],edges[1:])])
                    ax.scatter(ph,1000*f,s=.6,color='gray',alpha=.2)
                    ax.plot((edges[:-1]+edges[1:])/2,1000*binmed,color='black',lw=1)
                    lo, hi = np.nanpercentile(f,[.7,99.3])*1000
                    ax.set_ylim(min(lo,-1),max(hi,1))
                    ax.axvline(0,color='orange',lw=.8)
                ar.set_ylabel(f'S{sector}',fontsize=8)
            axes[0,0].set_title('Raw SAP')
            axes[0,1].set_title('Pipeline corrected')
            fig.suptitle(f'TIC {tic}, {name}, P={p:.7f} d, epoch={c:.5f} BTJD, locally normalized ppt')
            fig.savefig(plots/f'{tic}-{name.replace(" ","_")}-phase.png',dpi=110)
            plt.close(fig)
        for cycle in range(math.floor((min(t_search)-c)/p),math.ceil((max(t_search)-c)/p)+1):
            center = c+cycle*p
            if center < min(t_search) or center > max(t_search):
                continue
            s0 = next((s for s,(t,*_) in sectors.items() if t[0]-w/2<=center<=t[-1]+w/2),None)
            cd=cs=rd=rs=np.nan
            n=cov=0
            if s0 is not None:
                t,sap,cor,dt=sectors[s0]
                cd,cs,n,cov=window(t,cor,center,w,dt)
                rd,rs,*_=window(t,sap,center,w,dt)
                if n>=2 and (name in ('Gaia','BLS 1') or (name in ('Fine 1','Fine 2') and len(local)<24)):
                    local.append((s0,center,w))
            coverage_status = ('outside sector spans' if s0 is None else
                               'insufficient core or shoulders' if not np.isfinite(cd) else 'measured')
            predictions.append(dict(tic=tic,clock=name,cycle=cycle,center_btjd=center,
                                    sector=s0,core_n=n,coverage=cov,status=coverage_status,
                                    corrected_depth_ppt=cd,corrected_scatter_ppt=cs,raw_depth_ppt=rd,raw_scatter_ppt=rs))
        if local:
            collections.append((name.replace(' ','_'),local))
    for label, collection in collections:
        if len(collection)>30:
            continue
        fig, axes = plt.subplots(math.ceil(len(collection)/4),4,figsize=(13,2.1*math.ceil(len(collection)/4)),squeeze=False,layout='constrained')
        for ax,(s,c,w) in zip(axes.flat,collection):
            t,sap,cor,dt = sectors[s]
            m=abs(t-c)<max(.35,2.4*w)
            for f,color in ((sap,'tab:blue'),(cor,'black')):
                x=t[m]-c
                y=f[m]
                side=(abs(x)>.65*w)&(abs(x)<2*w)
                baseline=np.median(y[side]) if side.any() else np.median(y)
                ax.scatter(x,1000*(y-baseline),s=4,alpha=.55,color=color)
            ax.axvspan(-w/2,w/2,color='tab:orange',alpha=.18)
            ax.set_title(f'S{s}  {c:.3f} BTJD',fontsize=9)
            ax.tick_params(labelsize=7)
        for ax in list(axes.flat)[len(collection):]:
            ax.axis('off')
        fig.suptitle(f'TIC {tic} {label}  |  corrected black, raw blue  |  days, ppt')
        fig.savefig(plots/f'{tic}-{label}.png',dpi=110)
        plt.close(fig)
    print(tic,','.join(f'{a["clock"]}={a["period_d"]:.4f}/{a["snr"]:.1f}' for a in clocks if a['tic']==tic),flush=True)

save('files.csv',files)
save('events.csv',events)
save('clocks.csv',clocks)
save('predictions.csv',predictions)
save('137203172-short-search.csv',single_event_checks)
