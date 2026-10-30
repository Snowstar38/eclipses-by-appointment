# Re-run of archive checks after the container restart: VizieR cones validated with a positive control
# per catalogue (a row found in a wide cone around the target is re-found by a 60" cone at its own
# position), SIMBAD (Harvard mirror) and ExoFOP.
import requests, re, time
V='https://vizier.idia.ac.za/viz-bin/asu-tsv'
stars={'15855794':(61.98479061937,22.75262439668),'92881948':(83.23743198367,-22.99121122673)}
cats=[('B/vsx/vsx',60),('J/ApJS/258/16',60),('J/A+A/652/A120',60),('I/358/veb',60),('I/357/varisum',60),('B/sb9/main',60)]
def get(params,timeout=90,tries=3):
    for k in range(tries):
        try: return requests.get(V,params=params,timeout=timeout)
        except Exception as ex: err=ex; time.sleep(3)
    raise err
def data_rows(txt):
    L=[l for l in txt.splitlines() if l.strip() and not l.startswith('#')]
    return L[0] if L else '', L[3:] if len(L)>3 else []
for name,(ra,dec) in stars.items():
    print('=====',name,ra,dec,flush=True)
    for cat,rad in cats:
        try:
            r=get({'-source':cat,'-c':f'{ra} {dec}','-c.rs':rad,'-out.all':'','-out.add':'_r','-sort':'_r'})
            hdr,data=data_rows(r.text)
            print(f'  {cat} r<{rad}": HTTP {r.status_code}, {len(data)} rows',flush=True)
            for l in data[:3]: print('     ',hdr[:300]); print('     ',l[:300])
            # positive control: wide cone (5 deg), take nearest row's RAJ2000/DEJ2000 or _RA/_DE, re-cone at 60"
            r2=get({'-source':cat,'-c':f'{ra} {dec}','-c.rd':5,'-out':'_RAJ2000 _DEJ2000','-out.max':3,'-sort':'_r'},timeout=120)
            h2,d2=data_rows(r2.text)
            if d2:
                c=d2[0].split('\t'); cra,cdec=c[0].strip(),c[1].strip()
                r3=get({'-source':cat,'-c':f'{cra} {cdec}','-c.rs':60,'-out':'_RAJ2000 _DEJ2000'})
                h3,d3=data_rows(r3.text)
                print(f'     control: nearest row within 5 deg at {cra} {cdec}; 60" cone there returns {len(d3)} rows -> cone {"WORKS" if d3 else "FAILS"}',flush=True)
            else: print('     control: no row within 5 deg (catalogue sparse here); control not done',flush=True)
        except Exception as ex: print('  ',cat,'ERR',ex,flush=True)
    try:
        r=get({'-c':f'{ra} {dec}','-c.rs':5,'-out.add':'_r'},timeout=150)
        tabs=re.findall(r'#Name: (\S+)',r.text)
        print('  ALL-CAT r<5": HTTP',r.status_code,len(tabs),'tables:',' '.join(tabs),flush=True)
        var=[t for t in tabs if t.split('/')[0] in ('B','J') or t.startswith(('I/358','I/357','II/366','J/'))]
        print('  ALL-CAT non-astrometric/variability-type tables:',' '.join(var) if var else 'none')
    except Exception as ex: print('  ALL ERR',ex)
for tic,(ra,dec) in stars.items():
    for url,params,lab in [('https://simbad.harvard.edu/simbad/sim-coo',{'Coord':f'{ra} {dec}','Radius':10,'Radius.unit':'arcsec','output.format':'ASCII'},'sim-coo 10"'),
                           ('https://simbad.harvard.edu/simbad/sim-id',{'Ident':f'TIC {tic}','output.format':'ASCII'},'sim-id TIC')]:
        try:
            r=requests.get(url,params=params,timeout=60)
            print('===== SIMBAD',lab,tic,'HTTP',r.status_code); print(r.text[:2000])
        except Exception as ex: print('SIMBAD ERR',ex)
    try:
        r=requests.get(f'https://exofop.ipac.caltech.edu/tess/target.php?id={tic}',timeout=60)
        t=r.text
        print('===== ExoFOP',tic,'HTTP',r.status_code,'len',len(t),'TOI mentions:',len(re.findall(r'TOI[- ]?\d',t)),'CTOI mentions:',len(re.findall(r'CTOI',t)))
        for m in sorted(set(re.findall(r'(TOI[- ]?\d+\.\d+|CTOI[^<]{0,60})',t)))[:10]: print('    ',m)
        tt=re.sub(r'<[^>]+>',' ',t); tt=re.sub(r'\s+',' ',tt)
        i=tt.find('TOI'); print('    context:',tt[max(0,i-150):i+250] if i>=0 else 'no "TOI" string')
    except Exception as ex: print('ExoFOP ERR',ex)
