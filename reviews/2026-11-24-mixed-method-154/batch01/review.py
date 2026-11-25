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

SCRIPT_DIR = Path(__file__).resolve().parent
ROOT = SCRIPT_DIR.parents[2] if (SCRIPT_DIR.parents[2]/"sky/data/qlp-sb-p20-60").is_dir() else SCRIPT_DIR.parent/"inputs/workspace"
parser = argparse.ArgumentParser()
parser.add_argument('--batch-dir',type=Path,default=SCRIPT_DIR)
parser.add_argument('--output-dir',type=Path)
parser.add_argument('--target')
parser.add_argument('--seed',type=float,action='append',default=[])

parser.add_argument('--fits-dir', type=Path, default=ROOT/'sky/data/qlp-sb-p20-60')
parser.add_argument('--prior-dir', type=Path, default=ROOT/'Astra/made/binary-exploration-2026-11-04/bulk-results')
parser.add_argument('--mask', type=Path, default=ROOT/'sky/mixed-fold-2026-11-24/cadence-controls/flagged-exposures.csv')
args = parser.parse_args()
BATCH = args.batch_dir.resolve()
HERE = args.output_dir.resolve() if args.output_dir else BATCH
if args.target and HERE==BATCH:
    parser.error('--target requires a separate --output-dir to preserve the batch outputs')
plots = HERE/'plots'
plots.mkdir(exist_ok=True,parents=True)


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
        mask.setdefault((int(row['sector']),int(row['camera']),row['flux_column']),set()).add(int(row['cadenceno']))

events, clocks, predictions, files = [], [], [], []
fit_durations = [.06,.12,.24,.48,.96]
for row in rows(BATCH/'batch.csv'):
    tic = row['tic']
    if args.target and tic!=args.target:
        continue
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
            bad = np.isin(z['CADENCENO'], list(mask.get((sector,cam,correction),())))
            t, sap, cor = (np.asarray(z[name][good&~bad],float) for name in ('TIME','SAP_FLUX',correction))
            if len(t)<15:
                continue
            cadence = np.median(np.diff(t))
            if sector in sectors:
                continue
            sectors[sector] = (t, sap/np.median(sap)-1, cor/np.median(cor)-1,cadence)
            files.append(dict(tic=tic,sector=sector,camera=cam,ccd=ccd,file=path.name,corrected_column=correction,start=t[0],end=t[-1],cadence=cadence,n=len(t),masked=int((bad&good).sum())))
    t_search, y_search, e_search = [], [], []
    raw_search, raw_errors = [], []
    prior = []
    for s,(t,sap,cor,cadence) in sectors.items():
        residual = continuum(t,cor+1)
        raw_residual = continuum(t,sap+1)
        sigma = max(.00003,1.4826*np.median(abs(residual-np.median(residual))))
        take = slice(None,None,max(1,round(.021/cadence)))
        t_search.extend(t[take])
        y_search.extend(np.clip(residual[take], -10*sigma, 6*sigma))
        e_search.extend(np.full(len(t[take]),sigma))
        raw_sigma = max(.00003,1.4826*np.median(abs(raw_residual-np.median(raw_residual))))
        raw_search.extend(np.clip(raw_residual[take], -10*raw_sigma, 6*raw_sigma))
        raw_errors.extend(np.full(len(t[take]),raw_sigma))
        for entry in known:
            if s!=entry['sector']:
                continue
            for hit in entry.get('windows',[]):
                if hit['kind']=='dip' and hit['flag']:
                    prior.append((s,hit['time'],hit['duration']))
    bls = BoxLeastSquares(t_search,y_search,e_search)
    pg = float(row['gaia_period_days'])
    pilot = float(row.get('pilot_period_d') or 'nan')
    fixed_names = ['Gaia','Gaia/2','2*Gaia']
    fixed_periods = [pg,pg/2,pg*2]
    if np.isfinite(pilot):
        fixed_names.extend(['Pilot','Pilot/2','Pilot/3','Pilot/4','2*Pilot'])
        fixed_periods.extend([pilot,pilot/2,pilot/3,pilot/4,pilot*2])
    archived_fold = float(row.get('fold_screening_period_days') or 'nan')
    if np.isfinite(archived_fold):
        fixed_names.append('Archive fold')
        fixed_periods.append(archived_fold)
    fixed = bls.power(fixed_periods,fit_durations,oversample=8,objective='snr')
    solutions = [(name,fixed,i) for i,name in enumerate(fixed_names)]
    periodogram = bls.autopower([.08,.16,.32,.55],minimum_period=1.5,maximum_period=65,frequency_factor=3300,oversample=4,objective='snr')
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
    for name, subset in (('Raw early',ds<100),('Raw late',ds>max(ds)-100)):
        if sum(subset)<400:
            continue
        span = BoxLeastSquares(np.asarray(t_search)[subset],np.asarray(raw_search)[subset],np.asarray(raw_errors)[subset])
        local_search = span.autopower([.08,.16,.32,.55],minimum_period=.65,maximum_period=25,frequency_factor=18,oversample=4,objective='snr')
        solutions.append((name,local_search,np.argmax(local_search.power)))
    segment_pairs = {
        group: [float(result.period[i]) for name,result,i in solutions if name in names]
        for group,names in (('corrected',('Early','Late')),('raw',('Raw early','Raw late')))
    }
    seeds = [pilot] if np.isfinite(pilot) else []
    for segment_periods in segment_pairs.values():
        if len(segment_periods)==2:
            early,late = segment_periods
            if abs(early-late)/early<.015 and all(abs(early-v)/early>.008 for v in seeds):
                seeds.extend([early,early/2])
    seeds.append(peaks[0])
    seeds.extend(args.seed)
    for num, seed in enumerate(seeds,1):
        span = max(t_search)-min(t_search)
        step = .018*seed**2/span
        grid = np.arange(seed*.997,seed*1.003,step)
        durations = [w for w in (.04,.06,.08,.12,.16,.25,.36,.55) if w<.70*min(grid)]
        fine = bls.power(grid,durations,oversample=6,objective='snr')
        solutions.append((f'Fine {num}',fine,np.argmax(fine.power)))
    previous = []
    for s,c,w in prior:
        t,sap,cor,dt = sectors[s]
        cd, cs, n, cov = window(t,cor,c,w,dt)
        rd, rs, *_ = window(t,sap,c,w,dt)
        events.append(dict(tic=tic,sector=s,center_btjd=c,width_d=w,core_n=n,coverage=cov,corrected_depth_ppt=cd,corrected_scatter_ppt=cs,raw_depth_ppt=rd,raw_scatter_ppt=rs))
        previous.append((s,c,w))
    collections = [('prior',previous)] if previous else []
    trial_ephemerides = [(name, *(float(getattr(result,j)[ind]) for j in ('period','transit_time','duration','power')))
                        for name,result,ind in solutions]
    anchor = float(row['best_window_btjd'])
    width = float(row['best_window_duration_days'])
    if np.isfinite(pilot):
        trial_ephemerides.extend((f'Pilot anchored / {k}',pilot/k,anchor,width,np.nan)
                                 for k in range(1,5))
    _, period, epoch, width, _ = trial_ephemerides[len(solutions)-1]
    trial_ephemerides.extend((f'Refined alias {d:g}',period*d,epoch,width,np.nan) for d in (.5,2))
    for name,p,c,w,snr in trial_ephemerides:
        clocks.append(dict(tic=tic,clock=name,period_d=p,epoch_btjd=c,width_d=w,snr=snr))
        local = []
        if name==f'Fine {len(seeds)}' or (name.startswith('Fine') and name!='Fine 1' and len(seeds)<=3):
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
                if n>=2 and (name in ('Gaia','BLS 1','Pilot','Archive fold','Fine 1') or (name.startswith('Fine') and len(local)<24)):
                    local.append((s0,center,w))
            coverage_status = ('outside sector spans' if s0 is None else
                               'insufficient core or shoulders' if not np.isfinite(cd) else 'measured')
            predictions.append(dict(tic=tic,clock=name,cycle=cycle,center_btjd=center,
                                    sector=s0,core_n=n,coverage=cov,status=coverage_status,
                                    corrected_depth_ppt=cd,corrected_scatter_ppt=cs,raw_depth_ppt=rd,raw_scatter_ppt=rs))
        if local:
            collections.append((name.replace(' ','_'),local))
    for label, collection in collections:
        cap = 32 if label=='prior' else 20
        if len(collection)>cap:
            take = np.unique(np.linspace(0,len(collection)-1,cap).astype(int))
            collection = [collection[i] for i in take]
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
    print(tic,','.join(f'{a["clock"]}={a["period_d"]:.5f}/{a["snr"]:.1f}' for a in clocks if a['tic']==tic),flush=True)
    for trial in [r for r in clocks if r['tic']==tic and (r['clock'].startswith('Fine') or r['clock']=='BLS 1')]:
        hit = [r for r in predictions if r['tic']==tic and r['clock']==trial['clock'] and r['status']=='measured']
        if len(hit)<5:
            continue
        both = [min(r['corrected_depth_ppt'],r['raw_depth_ppt']) for r in hit]
        strong = sum(v>.45 for v in both)
        if strong>=5 or trial['snr']>20:
            print('  windows',trial['clock'],len(hit),strong,'median both',round(float(np.median(both)),3),flush=True)

save('files.csv',files)
save('events.csv',events)
save('clocks.csv',clocks)
save('predictions.csv',predictions)
coverage_summary = []
grouped = {}
for row in predictions:
    grouped.setdefault((row['tic'],row['clock']),[]).append(row)
for (tic,clock),group in grouped.items():
    outside = sum(row['status']=='outside sector spans' for row in group)
    for quality in (.55,.80,.95):
        measured = [row for row in group if row['status']=='measured' and row['coverage']>=quality]
        depth = [min(row['raw_depth_ppt'],row['corrected_depth_ppt']) for row in measured]
        coverage_summary.append(dict(tic=tic,clock=clock,min_window_coverage=quality,
                                     all_cycles=len(group),outside_sector_spans=outside,
                                     insufficient_in_sector=len(group)-outside-len(measured),
                                     measured=len(measured),weak_in_either=sum(x<=.75 for x in depth),
                                     depth_over_2_ppt_both=sum(x>2 for x in depth)))
save('coverage-summary.csv',coverage_summary)
