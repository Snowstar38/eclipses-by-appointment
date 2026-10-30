# Catalogue cones: VSX (60"), Prsa+2022, IJspeert+2021, Gaia DR3 veb/varisum, SB9 (VizieR mirror);
# all-catalogue 5" cone; SIMBAD (Harvard mirror); Gaia DR3 vari tables via Heidelberg TAP for target + bright neighbours.
import requests, csv, io, sys, json
V='https://vizier.idia.ac.za/viz-bin/asu-tsv'
T={}
for r in csv.DictReader(open('../targets.csv')):
    T[r['tic']]=r
NB=[r for r in csv.DictReader(open('../neighbours_90as.csv'))]
tics=['372683900','13106408','372683622','319185391','62328710']
cats=[('B/vsx/vsx',60),('J/ApJS/258/16',60),('J/A+A/652/A120',60),('I/358/veb',60),('I/357/varisum',30),('B/sb9/main',60)]
def viz(src,ra,dec,rs):
    p={'-c':f'{ra} {dec}','-c.rs':str(rs),'-out.all':'','-out.add':'_r','-sort':'_r'}
    if src: p['-source']=src
    r=requests.get(V,params=p,timeout=120)
    lines=[l for l in r.text.splitlines() if l and not l.startswith('#')]
    return lines
out=open('s2_catalogs.txt','w')
def P(*a):
    s=' '.join(str(x) for x in a); print(s); out.write(s+'\n')
# sanity: a known object (V* AI Dra-like known EB): use Algol coordinates for VSX
P('SANITY VSX Algol:', viz('B/vsx/vsx',47.04221,40.95565,30)[:4])
for t in tics:
    ra,dec=T[t]['tic_ra'],T[t]['tic_dec']
    P('='*20,'TIC',t,ra,dec)
    for src,rs in cats:
        L=viz(src,ra,dec,rs)
        P(f'--- {src} r<{rs}": {len(L)} lines'); 
        for l in L[:12]: P('   ',l[:400])
    L=viz(None,ra,dec,5)
    tabs=sorted(set(l.split('\t')[0] for l in L if l))
    P('--- all-catalogue 5": raw lines',len(L))
    for l in L[:200]:
        if 'Gaia' in l or l.count('\t')<3: continue
    # print table names: VizieR TSV with multiple tables has '#Table' comments; re-fetch keeping comments
    p={'-c':f'{ra} {dec}','-c.rs':'5'}
    r=requests.get(V,params=p,timeout=180)
    names=[l for l in r.text.splitlines() if l.startswith('#RESOURCE') or l.startswith('#Name:')]
    P('    tables:', '; '.join(n.replace('#Name: ','') for n in names if n.startswith('#Name')))
    s=requests.get('https://simbad.harvard.edu/simbad/sim-coo',params={'Coord':f'{ra} {dec}','Radius':'10','Radius.unit':'arcsec','output.format':'ASCII'},timeout=60).text
    P('--- SIMBAD 10":'); 
    for l in s.splitlines()[:60]:
        if l.strip() and ('Object' in l or 'Bibcodes' in l or 'Identifiers' in l or '|' in l or 'Number of' in l or l.startswith('TIC') or 'Gaia DR3' in l or 'TYC' in l or 'V*' in l): P('   ',l[:300])
# Gaia vari tables for target and neighbours G<15.5 within 90"
ids=[]
for t in tics:
    for n in NB:
        if n['tic']==t and float(n['Gmag'])<15.5: ids.append((t,n['source_id'],n['Gmag'],n['sep_arcsec']))
idl=','.join(i[1] for i in ids)
TAP='https://gaia.ari.uni-heidelberg.de/tap/sync'
for tab,cols in [('gaiadr3.vari_summary','*'),('gaiadr3.vari_classifier_result','source_id,classifier_name,best_class_name,best_class_score'),('gaiadr3.vari_eclipsing_binary','source_id,frequency,global_ranking,model_type,derived_primary_ecl_depth,derived_secondary_ecl_depth'),('gaiadr3.vari_rotation_modulation','source_id,best_rotation_period'),('gaiadr3.vari_short_timescale','source_id,frequency'),('gaiadr3.vari_ms_oscillator','source_id,frequency1,amplitude1')]:
    q=f'SELECT {cols} FROM {tab} WHERE source_id IN ({idl})'
    r=requests.post(TAP,data={'REQUEST':'doQuery','LANG':'ADQL','FORMAT':'csv','QUERY':q},timeout=300)
    P('--- Gaia',tab); 
    for l in r.text.splitlines()[:30]: P('   ',l[:500])
P('ids queried:',ids)
