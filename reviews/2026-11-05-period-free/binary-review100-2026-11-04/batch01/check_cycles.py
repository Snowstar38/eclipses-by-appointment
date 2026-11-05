"""Bounded orbit-cycle and clean-window checks for H002/H008."""
import json, math
from pathlib import Path
import numpy as np
from astropy.io import fits

B=Path(__file__).resolve().parent
for tic, anchor, other, cycles in [('352438536',2040.0819,4106.0797,35),('322217134',3232.1065,3815.162,18)]:
    data=json.loads((B/tic/'raw-inspection.json').read_text())
    P=(other-anchor)/cycles
    result=[]
    for receipt in data['sectors']:
        if 'path' not in receipt: continue
        with fits.open(receipt['path'],memmap=False) as h:
            a=h[1].data;t=np.asarray(a['TIME'],float);f=np.asarray(a['SAP_FLUX'],float);q=np.asarray(a['QUALITY'],int)
        valid=np.isfinite(t)&np.isfinite(f)&(f>0);t=t[valid];f=f[valid];q=q[valid]
        for n in range(math.ceil((min(t)-anchor-2)/P),math.floor((max(t)-anchor+2)/P)+1):
            c=anchor+n*P
            if not min(t)-2<c<max(t)+2: continue
            core=abs(t-c)<(.55 if tic=='322217134' else 1.15)
            left=(t>c-2.8)&(t<c-1.6) if tic=='352438536' else (t>c-1.25)&(t<c-.8)
            right=(t<c+2.8)&(t>c+1.6) if tic=='352438536' else (t<c+1.25)&(t>c+.8)
            clean=core&(q==0);lc=left&(q==0);rc=right&(q==0)
            cadence=receipt['cadence_days']; expected_n=2*(.55 if tic=='322217134' else 1.15)/cadence
            core_times=np.sort(t[clean]);max_gap=float(max(np.diff(core_times))) if len(core_times)>1 else float('inf')
            bins=np.histogram((t-c)[clean],bins=np.linspace(-(.55 if tic=='322217134' else 1.15),(.55 if tic=='322217134' else 1.15),7))[0]
            r={'sector':receipt['sector'],'cycle':n,'predicted_btjd':c,
               'core_quality0':int(sum(clean)),'core_flagged':int(sum(core&(q!=0))),
               'left_quality0':int(sum(lc)),'right_quality0':int(sum(rc)),
               'core_coverage_fraction':float(sum(clean)/max(1,expected_n)),
               'max_internal_core_gap_days':max_gap,'core_six_bin_counts':bins.tolist(),
               'clean_bilateral':bool(sum(clean)>.75*expected_n and sum(lc)>10 and sum(rc)>10 and np.all(bins>0) and max_gap<max(3*cadence,.15*(.55 if tic=='322217134' else 1.15)))}
            if r['clean_bilateral']:
                baseline=float((np.median(f[lc])+np.median(f[rc]))/2)
                r['median_core_deficit_ppt']=float(1000*(1-np.median(f[clean])/baseline))
                r['left_right_baseline_difference_ppt']=float(1000*(np.median(f[lc])-np.median(f[rc]))/baseline)
            result.append(r)
    g=json.loads((B.parent/'source-packets'/tic/'sources.json').read_text())['target']['gaia']
    e=float(g['eccentricity']);w=math.radians(float(g['arg_periastron']));gp=float(g['period']);tp=389+float(g['t_periastron'])
    conjunctions=[]
    for name,nu in [('A',math.pi/2-w),('B',3*math.pi/2-w)]:
        E=2*math.atan2(math.sqrt(1-e)*math.sin(nu/2),math.sqrt(1+e)*math.cos(nu/2))
        base=tp+((E-e*math.sin(E))%(2*math.pi))/(2*math.pi)*gp
        n=round((anchor-base)/gp); pred=base+n*gp
        conjunctions.append({'kind':name,'at_anchor_btjd':pred,'offset_days':anchor-pred,'offset_phase':(anchor-pred)/gp})
    artifact={'tic':tic,'anchor_btjd':anchor,'other_btjd':other,'assumed_same_kind_cycles':cycles,
              'two_event_period_days':P,'gaia_period_days':gp,'gaia_period_error_days':float(g['period_error']),
              'gaia_conjunctions':conjunctions,'selected_period_windows':result,
              'caveat':'Two-event period conditional on chosen cycle count; partial H008 s92 and H002 s103 have uncalibrated center errors. Candidate clean-window medians are diagnostics, not eclipse fits; quality flags excluded.'}
    (B/tic/'cycle-coverage.json').write_text(json.dumps(artifact,indent=2)+'\n')
    print(tic,'P',round(P,5),'Gaia offsets',[(c['kind'],round(c['offset_phase'],4)) for c in conjunctions], 'windows',[(r['sector'],r['cycle'],r['clean_bilateral'],round(r.get('median_core_deficit_ppt',0),1)) for r in result])
