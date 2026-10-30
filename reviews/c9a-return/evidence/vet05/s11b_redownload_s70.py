# Re-fetch the s70 cube of TIC 15855794 (deleted after s11) to redo its difference image without the end-of-orbit event E124
from astroquery.mast import Tesscut
from astropy.coordinates import SkyCoord
D='/tmp/claude-0/-home-user-eclipses-paper-review/55c92ff4-798a-544f-be03-9888c6804905/scratchpad/data/vet05'
m=Tesscut.download_cutouts(coordinates=SkyCoord(61.9846420339577,22.7526773515837,unit='deg'),size=11,sector=70,path=f'{D}/15855794/tesscut')
print(list(m['Local Path']))
