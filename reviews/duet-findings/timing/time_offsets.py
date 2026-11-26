"""Clock model for the house's TESS eclipse times (see timing/qlp_barycentre.py for the tests).

  sectors 14, 15  : carry about 1.5 times the Roemer delay (30-min data; tentative)
  other <= 100    : barycentric (BTJD), no offset
  sector 101      : barycentric but 3.5 min early: subtract -3.47 min (one 200 s cadence
                    is 3.33 min)
  sectors >= 102  : not barycentric: subtract the Roemer delay roemer_min()
correction_min(sector, btjd, ra, dec) returns the minutes to subtract from a time.
"""
import numpy as np
import pandas as pd

S101_OFFSET_MIN = -3.47
ROEMER_FACTOR = {14: 1.5, 15: 1.5}


def roemer_min(btjd, ra, dec):
    """Sun-geocentre vector dotted with the star's direction, in light-minutes (low-precision solar ephemeris)."""
    n = np.asarray(btjd, float) + 2457000 - 2451545.0
    L = np.radians(280.460 + 0.9856474 * n); g = np.radians(357.528 + 0.9856003 * n)
    lam = L + np.radians(1.915) * np.sin(g) + np.radians(0.020) * np.sin(2 * g)
    R = 1.00014 - 0.01671 * np.cos(g) - 0.00014 * np.cos(2 * g); eps = np.radians(23.439 - 4e-7 * n)
    s = R * np.array([np.cos(lam), np.cos(eps) * np.sin(lam), np.sin(eps) * np.sin(lam)])
    a, d = np.radians(ra), np.radians(dec)
    nv = np.array([np.cos(d) * np.cos(a), np.cos(d) * np.sin(a), np.sin(d)])
    return 8.3167 * np.tensordot(nv, s, 1)


def correction_min(sector, btjd, ra, dec):
    sector = np.asarray(sector); btjd = np.asarray(btjd, float)
    k = np.where(sector >= 102, 1.0, 0.0)
    for s_, f in ROEMER_FACTOR.items():
        k = np.where(sector == s_, f, k)
    return k * roemer_min(btjd, ra, dec) + np.where(sector == 101, S101_OFFSET_MIN, 0.0)


def positions():
    pos, rid = {}, {}
    for f in ('overview/systems.csv', 'scientific-review-register.csv', 'accepted-systems.csv'):
        t = pd.read_csv(f)
        t['tic'] = t.tic.astype(str)
        if 'ra_deg' in t:
            pos.update({k: (r, d) for k, r, d in zip(t.tic, t.ra_deg, t.dec_deg) if np.isfinite(r)})
        rid.update(dict(zip(t.tic, t.review_id)))
    return pos, rid
