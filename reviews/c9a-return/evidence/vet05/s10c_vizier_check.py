# VizieR (idia mirror) cones with diagnostics. s10b gave 0 rows in VSX for 92881948 although s10 had returned
# one row; wide-cone controls failed (timeouts). Here: 60" cones repeated 3x with the raw INFO/error lines kept, and a
# positive control per catalogue = the catalogue's first row (no position constraint) re-found by a 60" cone.
import requests, time
V='https://vizier.idia.ac.za/viz-bin/asu-tsv'
stars={'15855794':(61.98479061937,22.75262439668),'92881948':(83.23743198367,-22.99121122673)}
cats=['B/vsx/vsx','J/ApJS/258/16','J/A+A/652/A120','I/358/veb','I/357/varisum','B/sb9/main']
def q(params):
    try:
        r=requests.get(V,params=params,timeout=120); txt=r.text
    except Exception as ex: return None,[f'EXC {ex}'],[]
    L=[l for l in txt.splitlines() if l.strip()]
    info=[l for l in L if l.startswith('#') and any(k in l for k in ('INFO','Error','error','WARN','Truncated','QUERY_STATUS'))]
    data=[l for l in L if not l.startswith('#')]
    return r.status_code,info,data[3:] if len(data)>3 else []
for cat in cats:
    st,info,d=q({'-source':cat,'-out':'_RAJ2000 _DEJ2000','-out.max':1})
    if d:
        ra,de=d[0].split('\t')[:2]
        st2,info2,d2=q({'-source':cat,'-c':f'{ra.strip()} {de.strip()}','-c.rs':60,'-out':'_RAJ2000 _DEJ2000'})
        print(f'CONTROL {cat}: first row at {ra.strip()} {de.strip()} -> 60" cone returns {len(d2)} rows (HTTP {st2}) {"OK" if d2 else "FAILED"}',info2[:2])
    else: print(f'CONTROL {cat}: could not fetch first row (HTTP {st})',info[:3])
for tic,(ra,dec) in stars.items():
    for cat in cats:
        res=[]
        for k in range(3):
            st,info,d=q({'-source':cat,'-c':f'{ra} {dec}','-c.rs':60,'-out.add':'_r','-out':'_r *' if cat!='B/vsx/vsx' else '_r Name Type Period max min'})
            res.append(len(d)); 
            if d: rows=d
            time.sleep(1)
        print(f'{tic} {cat} 60": rows in 3 tries = {res}', ('first row: '+rows[0][:250]) if max(res)>0 else '', info[:2] if not max(res) else '')
