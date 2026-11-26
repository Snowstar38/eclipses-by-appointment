"""Clock model for the house's TESS eclipse times (tests in timing/qlp_barycentre.py and
timing/clock_model_check.py).

QLP FFI light curves claim barycentric TDB times in every sector; the TIME column is not
that in three regimes:
  sectors 100, 101 : the barycentric correction was computed once, at TBJD 4069.5, and that
                     constant written into every cadence. Subtract roemer(t) - roemer(4069.5).
                     Shapes good to about 2 s; the absolute epoch keeps about 15 s of slack.
  sectors >= 102   : no barycentric correction at all. Subtract roemer(t).
  sectors 14, 15   : a barycentric correction for the wrong sky position, different per star.
                     Use the TESS-SPOC re-time of the same star and sector where one exists
                     (timing/s1415-tspoc-times.csv: the per-star mean shift is applied); otherwise
                     fall back to 1.5 times the Roemer delay, which leaves 1.6 min rms against the
                     re-times (timing/clock_model_check.py), so
                     those times also get S1415_FALLBACK_ERR_MIN added in quadrature.
  everything else  : barycentric (BTJD).
SPOC two-minute and TESS-SPOC times are barycentric in every sector; pass spoc=True for them.
correction_min(sector, btjd, ra, dec, tic=None, spoc=False) returns the minutes to subtract;
extra_err_min(sector, tic=None, spoc=False) the timing error to add in quadrature.
"""
import os
import numpy as np
import pandas as pd

FROZEN_BTJD = 4069.5
S1415_FALLBACK_FACTOR = 1.5
S1415_FALLBACK_ERR_MIN = 1.6
_HERE = os.path.dirname(os.path.abspath(__file__))


def roemer_min(btjd, ra, dec):
    """Sun-geocentre vector dotted with the star's direction, in light-minutes (low-precision solar ephemeris).
    A time that skipped the barycentric correction runs late by this much."""
    n = np.asarray(btjd, float) + 2457000 - 2451545.0
    L = np.radians(280.460 + 0.9856474 * n); g = np.radians(357.528 + 0.9856003 * n)
    lam = L + np.radians(1.915) * np.sin(g) + np.radians(0.020) * np.sin(2 * g)
    R = 1.00014 - 0.01671 * np.cos(g) - 0.00014 * np.cos(2 * g); eps = np.radians(23.439 - 4e-7 * n)
    s = R * np.array([np.cos(lam), np.cos(eps) * np.sin(lam), np.sin(eps) * np.sin(lam)])
    a, d = np.radians(ra), np.radians(dec)
    nv = np.array([np.cos(d) * np.cos(a), np.cos(d) * np.sin(a), np.sin(d)])
    return 8.3167 * np.tensordot(nv, s, 1)


def _load_tspoc():
    t = pd.read_csv(os.path.join(_HERE, 's1415-tspoc-times.csv'))
    t = t[t.flag == 'ok']
    w = 1 / t.err_s ** 2
    g = t.assign(w=w, ws=w * t.shift_s).groupby([t.tic.astype(str), 'sector'])
    return {k: (v.ws.sum() / v.w.sum()) / 60 for k, v in g}


S1415_SHIFT_MIN = _load_tspoc()


def correction_min(sector, btjd, ra, dec, tic=None, spoc=False):
    sector = np.atleast_1d(np.asarray(sector)); btjd = np.atleast_1d(np.asarray(btjd, float))
    spoc = np.broadcast_to(np.asarray(spoc, bool), sector.shape)
    rm = roemer_min(btjd, ra, dec)
    c = np.where(sector >= 102, rm, 0.0)
    c = np.where((sector == 100) | (sector == 101), rm - roemer_min(FROZEN_BTJD, ra, dec), c)
    for s_ in (14, 15):
        sh = S1415_SHIFT_MIN.get((str(tic), s_)) if tic is not None else None
        c = np.where(sector == s_, -sh if sh is not None else S1415_FALLBACK_FACTOR * rm, c)
    return np.where(spoc, 0.0, c)


def extra_err_min(sector, tic=None, spoc=False):
    sector = np.atleast_1d(np.asarray(sector))
    fb = np.isin(sector, (14, 15)) & ~np.asarray(spoc, bool)
    if tic is not None:
        fb &= ~np.array([(str(tic), int(s)) in S1415_SHIFT_MIN for s in sector])
    return np.where(fb, S1415_FALLBACK_ERR_MIN, 0.0)


def positions():
    pos, rid = {}, {}
    for f in ('overview/systems.csv', 'scientific-review-register.csv', 'accepted-systems.csv'):
        t = pd.read_csv(f)
        t['tic'] = t.tic.astype(str)
        if 'ra_deg' in t:
            pos.update({k: (r, d) for k, r, d in zip(t.tic, t.ra_deg, t.dec_deg) if np.isfinite(r)})
        rid.update(dict(zip(t.tic, t.review_id)))
    return pos, rid
