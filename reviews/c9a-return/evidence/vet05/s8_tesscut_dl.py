# TESScut via astroquery (coordinates; lightkurve's search_tesscut fell back to the http name resolver here)
from astroquery.mast import Tesscut
from astropy.coordinates import SkyCoord
D='/tmp/claude-0/-home-user-eclipses-paper-review/55c92ff4-798a-544f-be03-9888c6804905/scratchpad/data/vet05'
import os
for tic,ra,dec in [('15855794',61.9846420339577,22.7526773515837),('92881948',83.2374971727493,-22.990836995752)]:
    c=SkyCoord(ra,dec,unit='deg')
    sec=Tesscut.get_sectors(coordinates=c)
    print(tic); print(sec,flush=True)
    os.makedirs(f'{D}/{tic}/tesscut',exist_ok=True)
    for s in sec['sector']:
        try:
            m=Tesscut.download_cutouts(coordinates=c,size=11,sector=int(s),path=f'{D}/{tic}/tesscut')
            print('  got',s,list(m['Local Path']),flush=True)
        except Exception as ex: print('  FAIL',s,ex,flush=True)
