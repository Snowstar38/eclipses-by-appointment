"""Collect every TIC v8.2 record cached anywhere in reviews/ (JSON objects with ID, Teff, lumclass) for the accepted systems into
reviews/duet-findings/masses/tic-records.csv, one row per TIC. Run from the repository root."""
import json,glob,csv,subprocess
keys=['ID','GAIA','Tmag','GAIAmag','gaiabp','gaiarp','plx','e_plx','d','ebv','Teff','e_Teff','logg','rad','e_rad','mass','lum','e_lum','lumclass','contratio']
files=subprocess.run(['grep','-rl','--include=*.json','"lumclass"','reviews'],capture_output=True,text=True).stdout.split()
recs={}
def walk(o):
    if isinstance(o,dict):
        if 'ID' in o and 'Teff' in o and 'lumclass' in o:
            recs.setdefault(str(o['ID']),{k:o.get(k) for k in keys})
        for v in o.values(): walk(v)
    elif isinstance(o,list):
        for v in o: walk(v)
for f in sorted(files):
    try: walk(json.load(open(f)))
    except Exception: pass
w=csv.DictWriter(open('reviews/duet-findings/masses/tic-records.csv','w',newline=''),fieldnames=keys)
w.writeheader()
acc={l.split(',')[1] for l in open('accepted-systems.csv').read().split('\n')[1:] if l}
keep=[k for k in sorted(recs,key=int) if k in acc]
for k in keep: w.writerow(recs[k])
print(len(files),'files',len(recs),'TIC records,',len(keep),'of them accepted systems')
