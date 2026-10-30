# (1) Positive control for the Prsa+2022 cone (row taken from a 30-deg cone at 0,0); (2) Gaia DR3 variability tables
# queried directly at the Heidelberg TAP (vari_summary is I/358/varisum in VizieR, not I/357 which is the NSS part).
import requests
V='https://vizier.idia.ac.za/viz-bin/asu-tsv'
def rows(p):
    r=requests.get(V,params=p,timeout=120); L=[l for l in r.text.splitlines() if l.strip() and not l.startswith('#')]; return L[3:]
d=rows({'-source':'J/ApJS/258/16','-c':'009.335342386589 +22.345825642462','-c.rs':60,'-out':'TIC _RAJ2000 _DEJ2000 Per'})
print('CONTROL J/ApJS/258/16 cone 60" at 009.33534 +22.34583 (row seen in a wide cone):',len(d),'rows',d[:1])
for cat,(ra,de) in [('I/358/veb',('62.1651152711243','+22.8452379516562')),('J/A+A/652/A120',('61.4877817995335','+23.2417621836410'))]:
    d=rows({'-source':cat,'-c':f'{ra} {de}','-c.rs':60,'-out':'_RAJ2000 _DEJ2000'}); print(f'CONTROL {cat} cone 60" at {ra} {de}:',len(d),'rows')
for tic,(ra,de) in {'15855794':(61.98479061937,22.75262439668),'92881948':(83.23743198367,-22.99121122673)}.items():
    for cat in ['I/358/varisum','I/358/veb','J/ApJS/258/16']:
        d=rows({'-source':cat,'-c':f'{ra} {de}','-c.rs':60,'-out.add':'_r','-out':'_r Source'}); print(f'{tic} {cat} 60":',len(d),'rows',d[:2])
T='https://gaia.ari.uni-heidelberg.de/tap/sync'
ids='53541096672533120, 2964506347485091072'
for tab,cols in [('gaiadr3.vari_eclipsing_binary','source_id, frequency, global_ranking'),('gaiadr3.vari_classifier_result','source_id, best_class_name, best_class_score'),
                 ('gaiadr3.vari_summary','source_id, in_vari_eclipsing_binary, in_vari_rotation_modulation, in_vari_classification_result, num_selected_g_fov, range_mag_g_fov, std_dev_mag_g_fov'),
                 ('gaiadr3.vari_rotation_modulation','source_id, best_rotation_period, max_activity_index')]:
    r=requests.post(T,data=dict(REQUEST='doQuery',LANG='ADQL',FORMAT='csv',QUERY=f'SELECT {cols} FROM {tab} WHERE source_id IN ({ids})'),timeout=120)
    print('GAIA',tab,'HTTP',r.status_code); print(r.text.strip())
# positive control for the TAP: a known Gaia DR3 EB row (first row of vari_eclipsing_binary)
r=requests.post(T,data=dict(REQUEST='doQuery',LANG='ADQL',FORMAT='csv',QUERY='SELECT TOP 1 source_id, frequency FROM gaiadr3.vari_eclipsing_binary'),timeout=120)
print('GAIA control TOP 1 vari_eclipsing_binary:',r.text.strip().replace('\n',' | '))
