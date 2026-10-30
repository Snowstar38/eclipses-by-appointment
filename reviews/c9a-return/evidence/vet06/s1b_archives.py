# Follow-up: Gaia DR3 variability tables (I/358/vari summary, vclassre, veb) and NSS orbit table (I/357/tbosb1); ExoFOP CTOI context.
import requests, re, time
T={'468827621':(91.9386505142516,69.034466660429),'416285595':(287.318165074913,24.0684959972507)}
VIZ='https://vizier.idia.ac.za/viz-bin/asu-tsv'
def get(url):
    for i in range(4):
        try:
            r=requests.get(url,timeout=90)
            if r.ok: return r.text
        except Exception as e: print('ERR',e)
        time.sleep(3)
for tic,(ra,dec) in T.items():
    print('='*10,tic)
    for c in ['I/358/vari','I/358/vclassre','I/358/veb','I/357/tbosb1','I/358/vst']:
        t=get(f"{VIZ}?-source={c}&-c={ra}%20{dec}&-c.rs=10&-out.all&-sort=_r")
        lines=[l for l in (t or '').splitlines() if l and not l.startswith('#')]
        print(f'--- {c} r<10": {max(0,len(lines)-3)} rows')
        for l in lines[:5]: print('   ',l[:700])
    e=get(f"https://exofop.ipac.caltech.edu/tess/target.php?id={tic}") or ''
    for m in re.finditer(r'CTOI',e): print('   ctx:',re.sub(r'\s+',' ',re.sub('<[^>]+>',' ',e[max(0,m.start()-150):m.end()+150]))[:300])
