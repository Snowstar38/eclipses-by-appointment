# s14: final ephemerides (from s7 / ephem.json) and the next three primary (and secondary) eclipses after 2026-10-30,
# given as BJD_TDB/BTJD and as geocentric UTC with the barycentric light-time correction REMOVED (astropy builtin ephemeris).
import json, numpy as np
from astropy.time import Time
from astropy.coordinates import SkyCoord, EarthLocation
import astropy.units as u
EP=json.load(open('ephem.json'))
C={'195865529':SkyCoord(310.726437212619,43.3062048382287,unit='deg'),'468181994':SkyCoord(315.803516095103,-85.598149670046,unit='deg')}
SEC={'195865529':(0.49999,0.00007),'468181994':(0.4956,0.0012)}
geo=EarthLocation.from_geocentric(0,0,0,unit=u.m)
now=Time('2026-10-30T00:00:00',scale='utc').tdb.jd-2457000
for tic in C:
    T0,eT0,P,eP=EP[tic]['T0'],EP[tic]['eT0'],EP[tic]['P'],EP[tic]['eP']
    print('='*20,tic)
    print(f'  P = {P:.7f} +- {eP:.7f} d ; T0 = BTJD {T0:.5f} +- {eT0:.5f} = BJD_TDB {T0+2457000:.5f} (E={int(EP[tic]["Eref"])} in the s6 numbering)')
    n0=int(np.ceil((now-T0)/P))
    for lab,ph,eph in (('primary',0.0,0.0),('secondary',SEC[tic][0],SEC[tic][1])):
        for n in range(n0,n0+3):
            tb=T0+(n+ph)*P; et=np.sqrt(eT0**2+((n+ph)*eP)**2+(eph*P)**2)
            t=Time(tb+2457000,format='jd',scale='tdb')
            ltt=t.light_travel_time(C[tic],kind='barycentric',location=geo,ephemeris='builtin')
            tg=(t-ltt)
            print(f'  {lab:9s} n=+{n} cycles from T0: BTJD {tb:.4f} +- {et:.4f} d ({et*1440:.1f} min) | BJD_TDB as UTC (no LTT) {t.utc.iso[:16]} | geocentric UTC (LTT {ltt.to(u.min).value:+.1f} min removed) {tg.utc.iso[:16]}')
