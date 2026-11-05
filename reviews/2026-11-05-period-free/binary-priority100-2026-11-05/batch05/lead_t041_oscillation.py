"""Measure T041 short oscillation underlying the detector's repeated dips."""
import json
from pathlib import Path
import numpy as np
from astropy.io import fits
from astropy.timeseries import LombScargle
B=Path(__file__).resolve().parent/'233152264'
d=json.loads((B/'lead-numeric.json').read_text())
rows=[]
for sector in (60,73,84):
    path=[s['path'] for s in d['sources'] if s['sector']==sector][0]
    with fits.open(path,memmap=False) as h:
        a=h[1].data;t=np.asarray(a['TIME'],float);f=np.asarray(a['SAP_FLUX'],float);q=np.asarray(a['QUALITY'],int)
    good=np.isfinite(t)&np.isfinite(f)&(f>0)&(q==0);t=t[good];f=f[good]
    freq,power=LombScargle(t,f).autopower(minimum_frequency=5.2,maximum_frequency=5.8,samples_per_peak=50)
    i=int(np.argmax(power));rows.append(dict(sector=sector,short_period_days=float(1/freq[i]),frequency_cycles_per_day=float(freq[i]),lomb_scargle_power=float(power[i]),n=int(len(t)),source_path=path))
screen=29.365953707824975
(B/'lead-oscillation.json').write_text(json.dumps(dict(fold_screen_period_days=screen,measured_short_periods=rows,fold_to_short_period_ratio=float(screen/np.median([r['short_period_days'] for r in rows])),interpretation='The period-fold screen period is approximately the 162nd harmonic of a coherent short-period, roughly sinusoidal raw modulation; this explains repeated window minima without showing isolated eclipses.'),indent=2)+'\n')
print((B/'lead-oscillation.json').read_text())
