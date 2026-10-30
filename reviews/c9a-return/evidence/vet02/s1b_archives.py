# Follow-up: ExoFOP CTOI context; full all-catalogue 5" table list (no table cap).
import requests, re
T={'470235665':(345.747449371502,81.6998220902246),'379251709':(29.7546213215801,67.5461688632913)}
for tic,(ra,dec) in T.items():
    e=requests.get(f"https://exofop.ipac.caltech.edu/tess/target.php?id={tic}",timeout=90).text
    print(tic,'ExoFOP CTOI contexts:')
    for m in re.finditer('CTOI',e): print('   ...',re.sub(r'\s+',' ',re.sub('<[^>]+>',' ',e[max(0,m.start()-150):m.end()+150]))[:300])
    print('   TOI table rows "TOI " count:',len(re.findall(r'>\s*\d{3,5}\.\d\d\s*<',e)))
    t=requests.get(f"https://vizier.idia.ac.za/viz-bin/asu-tsv?-c={ra}%20{dec}&-c.rs=5&-out.max=1&-meta.max=1000",timeout=180).text
    tabs=re.findall(r'#Name: (\S+)', t)
    print(tic,'all-catalogue 5" tables (%d):'%len(tabs),' '.join(tabs))
    var=[x for x in tabs if re.match(r'(B/vsx|J/ApJS/258|I/358|I/357|B/sb9|J/A\+A/652|II/366|J/MNRAS|J/AJ|J/ApJ)',x)]
    print('   variability/journal tables:',var)
