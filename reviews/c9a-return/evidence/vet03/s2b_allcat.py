import requests, re
stars={'Algol(sanity)':(47.04221,40.95564),'70665829':(155.384788090706,17.2035145893056),'331293467':(212.403511923353,-60.1143106920448)}
for k,(ra,dec) in stars.items():
    t=requests.get(f'https://vizier.idia.ac.za/viz-bin/asu-tsv?-c={ra}%20{dec}&-c.rs=5&-out.max=5',timeout=180).text
    names=re.findall(r'^#Table\s+(\S+)',t,re.M) or re.findall(r'^#Name: (\S+)',t,re.M)
    print(k,len(names)); print('  ',' '.join(names))
    var=[n for n in names if re.match(r'(B/vsx|J/ApJS/258|J/A\+A/652/A120|I/358|I/357|B/sb9|B/gcvs|J/AJ|J/MNRAS|J/A\+A|II/366|J/ApJ)',n)]
    print('  variability/EB-like or journal tables:',var)
for tic in ['70665829','331293467']:
    e=requests.get(f'https://exofop.ipac.caltech.edu/tess/target.php?id={tic}',timeout=60).text
    for m in re.finditer(r'.{0,80}(TOI|CTOI).{0,80}',e): 
        s=re.sub('<[^>]+>',' ',m.group(0)); print(tic,'|',' '.join(s.split())[:160])
