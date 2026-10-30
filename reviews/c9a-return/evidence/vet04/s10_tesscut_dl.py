from astroquery.mast import Tesscut
from astropy.coordinates import SkyCoord
import os
D='/tmp/claude-0/-home-user-eclipses-paper-review/55c92ff4-798a-544f-be03-9888c6804905/scratchpad/data/vet04'
want={'283532878':(327.869175189832,57.9849184374285,[16,17,56,57,76,77,83,84]),
      '407877153':(275.783436380745,-79.3525721366319,[12,13,39,93,94,100,102])}
for tic,(ra,dec,secs) in want.items():
    c=SkyCoord(ra,dec,unit='deg'); od=os.path.join(D,tic,'tesscut'); os.makedirs(od,exist_ok=True)
    for sec in secs:
        if any(f'-s{sec:04d}-' in f for f in os.listdir(od)): print('have',tic,sec); continue
        for att in range(3):
            try:
                m=Tesscut.download_cutouts(coordinates=c,size=11,sector=sec,path=od)
                print(tic,sec,list(m['Local Path'])); break
            except Exception as ex: print('retry',tic,sec,repr(ex)[:200])
