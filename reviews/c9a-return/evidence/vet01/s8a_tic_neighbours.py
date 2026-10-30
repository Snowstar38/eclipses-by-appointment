# s8a: TIC v8.2 cone (120") around each target for Tmag of all neighbours; cross-match to neighbours_90as.csv (Gaia G<18)
from astroquery.mast import Catalogs
import numpy as np, csv
T={'195865529':(310.726437212619,43.3062048382287),'468181994':(315.803516095103,-85.598149670046)}
for tic,(ra,dec) in T.items():
    t=Catalogs.query_region(f'{ra} {dec}',radius=120/3600,catalog='TIC')
    t['dstArcSec']=t['dstArcSec'].astype(float)
    t.sort('dstArcSec')
    keep=t[(t['Tmag']<19)]
    cols=['ID','ra','dec','Tmag','GAIA','GAIAmag','Teff','rad','contratio','dstArcSec','objType','disposition','duplicate_id']
    keep[cols].write(f'tic_neighbours_{tic}.csv',overwrite=True,format='csv')
    print(tic,'TIC rows within 120" with Tmag<19:',len(keep))
    for r in keep[:25]: print('  ',r['ID'],f"{r['dstArcSec']:7.2f}\" T={r['Tmag']:.3f} G={r['GAIAmag']} GaiaID={r['GAIA']} Teff={r['Teff']} rad={r['rad']} disp={r['disposition']} dup={r['duplicate_id']}")
