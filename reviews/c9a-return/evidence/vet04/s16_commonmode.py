# Common-mode test: QLP light curves of other stars within ~0.5 deg (same camera/CCD) in one sector per star that holds
# secondary eclipses; measure each star's raw-SAP (QUALITY==0) deficit in the target's in-eclipse windows (inner part)
# relative to a local out-of-window baseline, exactly as for the target.
import time, lightkurve as lk, numpy as np, json, os, sys, warnings; warnings.filterwarnings('ignore')
from astropy.coordinates import SkyCoord
from astroquery.mast import Observations; import astropy.units as u
D='/tmp/claude-0/-home-user-eclipses-paper-review/55c92ff4-798a-544f-be03-9888c6804905/scratchpad/data/vet04/commonmode'
cfg={'283532878':(327.869175189832,57.9849184374285,[57,84]),'407877153':(275.783436380745,-79.3525721366319,[93,101])}
sh=json.load(open('s08_shape_oddeven.json'))
res={}
for tic,(ra,dec,secs) in cfg.items():
    eph=json.load(open(f's05_ephem_{tic}.json')); P=eph['P']
    for sec in secs:
        # lightkurve's cone search sends coordinates to the (unreachable) name resolver, so query MAST by coordinates directly
        obs=None
        for att in range(4):
            try: obs=Observations.query_criteria(coordinates=SkyCoord(ra,dec,unit='deg'),radius=0.5*u.deg,provenance_name='QLP',sequence_number=sec); break
            except Exception as ex: print('   retry query',repr(ex)[:100],flush=True); time.sleep(10)
        names=[str(n) for n in obs['target_name']]
        oth=[i for i,n in enumerate(names) if n.lstrip('0')!=tic][:15]; tg=[i for i,n in enumerate(names) if n.lstrip('0')==tic]
        print(f'===== {tic} s{sec}: {len(obs)} QLP lcs within 30 arcmin; using {len(oth)} others',flush=True)
        def get(ii):
            out=[]
            for i in ii:
                for att in range(4):   # the proxy occasionally resets connections
                    try:
                        pr=Observations.filter_products(Observations.get_product_list(obs[i]),productSubGroupDescription='LLC')
                        if len(pr)==0: break
                        m=Observations.download_products(pr[:1],download_dir=os.path.join(D,tic))
                        out.append(lk.read(m['Local Path'][0])); break
                    except Exception as ex: print('   retry',repr(ex)[:100],flush=True); time.sleep(5)
            return out
        lcs=get(oth); targ=get(tg)
        for lab,coll in (('TARGET',targ),('other',lcs)):
            for lc in coll:
                q=np.array(lc['quality'])==0; t=np.array(lc.time.value)[q]; f=np.array(lc['sap_flux'].value,float)[q]; g=np.isfinite(f)&np.isfinite(t); t,f=t[g],f[g]; f=f/np.median(f)
                row=[]
                for k in 'PS':
                    T0=eph['T0P'] if k=='P' else eph['T0S']; s_=sh[tic]['shape'][k]; T14=s_['T14']; hin=0.5*s_['r23']*T14+0.25*(1-s_['r23'])*T14
                    for n in range(int((t.min()-T0)/P)-1,int((t.max()-T0)/P)+2):
                        tc=T0+n*P; inn=np.abs(t-tc)<hin; o=(np.abs(t-tc)>T14/2+0.05)&(np.abs(t-tc)<T14/2+0.6)
                        if inn.sum()<5 or np.sum(o&(t<tc))<5 or np.sum(o&(t>tc))<5: continue
                        c=np.polyfit(t[o]-tc,f[o],1); r=f/np.polyval(c,t-tc)
                        dep=1-np.mean(r[inn]); e=np.std(r[o])/np.sqrt(inn.sum())
                        row.append(f'{k}{n}@{tc:.2f}: {1e3*dep:+.2f}±{1e3*e:.2f}')
                        res.setdefault(f'{tic}_s{sec}_{k}{n}',[]).append(dict(lab=lab,tic=str(lc.meta.get("OBJECT")),dep=float(dep),e=float(e)))
                print(f'  {lab:6s} {lc.meta.get("OBJECT")} Tmag {lc.meta.get("TESSMAG")}: '+' | '.join(row),flush=True)
for k,v in res.items():
    o=[x['dep'] for x in v if x['lab']=='other']; tt=[x['dep'] for x in v if x['lab']=='TARGET']
    if o: print(f'SUMMARY {k}: target {1e3*tt[0] if tt else np.nan:+.2f} ppt; {len(o)} others median {1e3*np.median(o):+.2f} ppt, range {1e3*min(o):+.2f}..{1e3*max(o):+.2f}; target rank (deepest=1) {1+sum(np.array(o)>(tt[0] if tt else 9))}')
json.dump(res,open('s16_commonmode.json','w'),indent=1)
