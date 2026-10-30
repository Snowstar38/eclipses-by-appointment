# Shared target table for the c9a vets: TIC row, Gaia DR3 NSS orbit (VizieR I/357), neighbours (VizieR I/355), sectors.
import warnings, csv, io, time, requests
warnings.filterwarnings('ignore')
from astroquery.mast import Catalogs, Observations, Tesscut
from astropy.coordinates import SkyCoord
roster=list(csv.DictReader(open('../bundle/ROSTER.csv')))
VIZ='https://vizier.idia.ac.za/viz-bin/asu-tsv'
def viz(source, ra, dec, rs, extra=''):
    url=f"{VIZ}?-source={source}&-c={ra}%20{dec}&-c.rs={rs}&-out.all&-out.max=200&-sort=_r{extra}"
    for i in range(4):
        try:
            r=requests.get(url,timeout=90)
            if r.ok: break
        except Exception as e: err=e
        time.sleep(3)
    else: raise RuntimeError(f'vizier {source} failed')
    lines=[l for l in r.text.splitlines() if l and not l.startswith('#')]
    if len(lines)<3: return []
    hdr=lines[0].split('\t'); data=[l for l in lines[3:] if l.strip()]
    return [dict(zip(hdr,[v.strip() for v in l.split('\t')])) for l in data]
out=[]; nb_all=[]
for r in roster:
    tic=r['tic']; row=dict(tic=tic, sheet=r['sheet'], panel=r['panel'], best_tag=r['best_tag'], best_period_days=r['best_period_days'], best_depth_ppm=r['best_depth_ppm'], roster_gaia_period=r['gaia_period_days'])
    t=Catalogs.query_criteria(catalog='TIC', ID=int(tic))[0]
    for c in ('ra','dec','Tmag','GAIA','Teff','rad','mass','contratio','plx','Vmag','Jmag','lum','logg'):
        row['tic_'+c]=t[c]
    ra,dec=float(t['ra']),float(t['dec'])
    nss=[x for x in viz('I/357/tbosb1',ra,dec,3) if x.get('Source')]
    if not nss:
        for cat in ('I/357/tbosb2','I/357/tbosb1c','I/357/tbosb2c','I/357/tboasb1c'):
            nss=[x for x in viz(cat,ra,dec,3) if x.get('Source')]
            if nss: break
    if nss:
        n=nss[0]
        for k in ('Source','NSSmodel','Per','e_Per','Tperi','e_Tperi','ecc','e_ecc','omega','e_omega','K1','e_K1','Vcm','e_Vcm','goodness','Signi','Flags','_r'):
            row['gaia_'+k]=n.get(k,'')
        try: row['gaia_tperi_btjd']=float(n['Tperi'])+389.0
        except: row['gaia_tperi_btjd']=''
        row['gaia_n_solutions_3as']=len(nss)
    else:
        row['gaia_NSSmodel']='NONE_FOUND'
    nb=[x for x in viz('I/355/gaiadr3',ra,dec,90,'&Gmag=%3C18') if x.get('Source')]
    for x in nb: nb_all.append(dict(tic=tic, source_id=x.get('Source'), ra=x.get('RA_ICRS'), dec=x.get('DE_ICRS'), Gmag=x.get('Gmag'), BP_RP=x.get('BP-RP'), plx=x.get('Plx'), RUWE=x.get('RUWE'), VarFlag=x.get('VarFlag'), sep_arcsec=x.get('_r')))
    tgt=[x for x in nb if float(x['_r'])<1.5]
    if tgt:
        g=tgt[0]; row['gaia_source_id']=g.get('Source'); row['gaia_Gmag']=g.get('Gmag'); row['gaia_BP_RP']=g.get('BP-RP'); row['gaia_plx']=g.get('Plx'); row['gaia_RUWE']=g.get('RUWE'); row['gaia_VarFlag']=g.get('VarFlag')
    others=[x for x in nb if float(x['_r'])>=1.5]
    row['n_neighbours_90as_G18']=len(others)
    row['brightest_neighbour_G']=min([float(x['Gmag']) for x in others if x.get('Gmag')], default='')
    row['nearest_neighbour_arcsec']=min([float(x['_r']) for x in others], default='')
    obs=Observations.query_criteria(target_name=tic, obs_collection='HLSP', provenance_name=['QLP','TESS-SPOC'])
    row['qlp_sectors']=' '.join(str(int(s)) for s in sorted(set(obs['sequence_number'][obs['provenance_name']=='QLP']))) if len(obs) else ''
    row['tessspoc_sectors']=' '.join(str(int(s)) for s in sorted(set(obs['sequence_number'][obs['provenance_name']=='TESS-SPOC']))) if len(obs) else ''
    obs2=Observations.query_criteria(target_name=tic, obs_collection='TESS', dataproduct_type='timeseries')
    row['spoc2min_sectors']=' '.join(str(int(s)) for s in sorted(set(obs2['sequence_number']))) if len(obs2) else ''
    try:
        s=Tesscut.get_sectors(coordinates=SkyCoord(ra,dec,unit='deg')); row['tesscut_sectors']=' '.join(str(int(x)) for x in s['sector'])
    except Exception as e: row['tesscut_sectors']='ERR '+type(e).__name__
    out.append(row)
    print(tic, row.get('gaia_NSSmodel'), 'P', str(row.get('gaia_Per',''))[:9], 'e', str(row.get('gaia_ecc',''))[:6], 'w', str(row.get('gaia_omega',''))[:6], '| QLP', row['qlp_sectors'], '| TS', row['tessspoc_sectors'], '| 2min', row['spoc2min_sectors'], '| nb', row['n_neighbours_90as_G18'], 'brightest G', row['brightest_neighbour_G'], flush=True)
keys=[]; [keys.append(k) for r in out for k in r if k not in keys]
with open('targets.csv','w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=keys); w.writeheader(); w.writerows(out)
with open('neighbours_90as.csv','w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(nb_all[0].keys())); w.writeheader(); w.writerows(nb_all)
print('wrote targets.csv', len(out), 'rows; neighbours', len(nb_all))
