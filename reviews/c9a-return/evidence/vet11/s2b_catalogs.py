# Resume of s2_catalogs.py (which died on a VizieR chunked-encoding reset at TIC 372683622):
# VizieR-mirror cones with retries for the three stars not yet done, SIMBAD, then Gaia DR3 vari tables
# (Heidelberg TAP) for all five targets and their neighbours with G<15.5 within 90".
import requests, csv, time, sys
V='https://vizier.idia.ac.za/viz-bin/asu-tsv'
VET='[local path omitted]'
T={r['tic']:r for r in csv.DictReader(open(f'{VET}/targets.csv'))}
NB=list(csv.DictReader(open(f'{VET}/neighbours_90as.csv')))
alltics=['372683900','13106408','372683622','319185391','62328710']
tics=sys.argv[1:] if len(sys.argv)>1 else ['372683622','319185391','62328710']
cats=[('B/vsx/vsx',60),('J/ApJS/258/16',60),('J/A+A/652/A120',60),('I/358/veb',60),('I/357/varisum',30),('B/sb9/main',60)]
out=open(f'{VET}/vet11/s2b_catalogs.txt','a')
def P(*a):
    s=' '.join(str(x) for x in a); print(s,flush=True); out.write(s+'\n'); out.flush()
def get(url,params,timeout=120,post=False):
    for k in range(5):
        try:
            r=(requests.post if post else requests.get)(url,params=None if post else params,data=params if post else None,timeout=timeout)
            if r.status_code==200: return r.text
        except Exception as e: err=e
        time.sleep(5*(k+1))
    return f'#FAILED after 5 tries'
def viz(src,ra,dec,rs):
    p={'-c':f'{ra} {dec}','-c.rs':str(rs),'-out.all':'','-out.add':'_r','-sort':'_r'}
    if src: p['-source']=src
    txt=get(V,p)
    if txt.startswith('#FAILED'): return None
    return [l for l in txt.splitlines() if l and not l.startswith('#')]
for t in tics:
    ra,dec=T[t]['tic_ra'],T[t]['tic_dec']
    P('='*20,'TIC',t,ra,dec)
    for src,rs in cats:
        L=viz(src,ra,dec,rs)
        if L is None: P(f'--- {src} r<{rs}": QUERY FAILED'); continue
        P(f'--- {src} r<{rs}": {max(0,len(L)-3)} rows')
        for l in L[3:12]: P('   ',l[:400])
    txt=get(V,{'-c':f'{ra} {dec}','-c.rs':'5'},timeout=180)
    names=[l.replace('#Name: ','') for l in txt.splitlines() if l.startswith('#Name:')]
    P('--- all-catalogue 5" tables:', '; '.join(names) if names else txt[:80])
    s=get('https://simbad.harvard.edu/simbad/sim-coo',{'Coord':f'{ra} {dec}','Radius':'10','Radius.unit':'arcsec','output.format':'ASCII'},60)
    P('--- SIMBAD 10":')
    for l in s.splitlines()[:40]:
        if l.strip() and ('Object' in l or 'Bibcodes' in l or 'Identifiers' in l or '|' in l or 'Number of' in l): P('   ',l[:300])
if 'gaia' in tics or len(sys.argv)==1:
    ids=[(n['tic'],n['source_id'],n['Gmag'],n['sep_arcsec']) for n in NB if n['tic'] in alltics and float(n['Gmag'])<15.5]
    idl=','.join(i[1] for i in ids)
    TAP='https://gaia.ari.uni-heidelberg.de/tap/sync'
    for tab,cols in [('gaiadr3.vari_summary','source_id,num_selected_g_fov,mean_mag_g_fov,std_dev_mag_g_fov,range_mag_g_fov,in_vari_classification_result,in_vari_eclipsing_binary,in_vari_rotation_modulation,in_vari_short_timescale,in_vari_ms_oscillator'),
                     ('gaiadr3.vari_classifier_result','source_id,classifier_name,best_class_name,best_class_score'),
                     ('gaiadr3.vari_eclipsing_binary','source_id,frequency,global_ranking,model_type,derived_primary_ecl_depth,derived_secondary_ecl_depth'),
                     ('gaiadr3.vari_rotation_modulation','source_id,best_rotation_period'),
                     ('gaiadr3.vari_short_timescale','source_id,frequency'),
                     ('gaiadr3.vari_ms_oscillator','source_id,frequency1,amplitude1')]:
        q=f'SELECT {cols} FROM {tab} WHERE source_id IN ({idl})'
        txt=get(TAP,{'REQUEST':'doQuery','LANG':'ADQL','FORMAT':'csv','QUERY':q},300,post=True)
        P('--- Gaia',tab)
        for l in txt.splitlines()[:30]: P('   ',l[:500])
    P('ids queried (tic, source_id, G, sep"):',ids)
