from astroquery.mast import Tesscut
from astropy.coordinates import SkyCoord
import os
D='/tmp/claude-0/-home-user-eclipses-paper-review/55c92ff4-798a-544f-be03-9888c6804905/scratchpad/data/vet03'
want={'70665829':((155.384788090706,17.2035145893056),[46,48,72]),'331293467':((212.403511923353,-60.1143106920448),[38,99,100,101])}
for tic,((ra,dec),secs) in want.items():
    c=SkyCoord(ra,dec,unit='deg')
    print(tic, Tesscut.get_sectors(coordinates=c))
    for s in secs:
        p=f'{D}/{tic}/tesscut'; os.makedirs(p,exist_ok=True)
        try:
            m=Tesscut.download_cutouts(coordinates=c,size=11,sector=s,path=p); print('got',s,list(m['Local Path']))
        except Exception as e: print('fail',s,e)
