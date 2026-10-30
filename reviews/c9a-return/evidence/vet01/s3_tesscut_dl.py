# s3: download 11x11 TESScut cubes for every sector of both targets (by coordinates)
from astroquery.mast import Tesscut
from astropy.coordinates import SkyCoord
import os, time
D='/tmp/claude-0/-home-user-eclipses-paper-review/55c92ff4-798a-544f-be03-9888c6804905/scratchpad/data/vet01'
T={'195865529':(310.726437212619,43.3062048382287,[15,41,55,56,75,76,82,83]),
   '468181994':(315.803516095103,-85.598149670046,[12,13,27,39,66,67,93,94])}
for tic,(ra,dec,secs) in T.items():
    c=SkyCoord(ra,dec,unit='deg')
    for s in secs:
        out=f'{D}/{tic}/tesscut'; os.makedirs(out,exist_ok=True)
        if any(f'-s{s:04d}-' in f for f in os.listdir(out)): print('have',tic,s); continue
        for k in range(3):
            try:
                m=Tesscut.download_cutouts(coordinates=c,size=11,sector=s,path=out)
                print(tic,s,list(m['Local Path']),flush=True); break
            except Exception as e:
                print('retry',tic,s,e,flush=True); time.sleep(10)
