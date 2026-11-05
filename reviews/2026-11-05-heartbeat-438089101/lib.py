"""vet438089101 helpers (Opus 5.5 referee, own code, 2026-11-04): MAST, Gaia TAP, FITS loading, Kepler, models.

Model conventions (derived here, checked on HD 193389 in s3a):
  Gaia / RV convention: omega = argument of periastron of the PRIMARY; the primary's line-of-sight distance
  (positive away from observer) is z1 = r1 sin(nu + omega) sin i, so v_r1 = K1 [cos(nu+omega) + e cos omega].
  Conjunctions: nu + omega = 90 deg -> primary farthest (behind), companion in front ("A");
                nu + omega = 270 deg -> primary in front ("B").
  Equilibrium tide (Kumar et al. 1995, Thompson et al. 2012 form):
     dF/F = S [1 - 3 sin^2 i sin^2(nu+omega)] / R^3,   R = r/a = (1-e^2)/(1+e cos nu)
  The tidal bulge points along the line of centres; cos(psi) between the bulge axis and the line of sight is
  sin i sin(nu+omega). The l=2 flux perturbation goes as -P2(cos psi) ~ 1 - 3 cos^2 psi (up to constants), so for
  S > 0 the star is faintest end-on (conjunctions) and brightest at quadrature. Invariant under omega -> omega+180.
  Doppler beaming (photon-counting): dF/F = -Bm * v_r1/K1 = -Bm [cos(nu+omega) + e cos omega]; Bm = beta K1 / c > 0.
  Brighter when approaching (v_r < 0). Changes sign under omega -> omega + 180, so it breaks the degeneracy.
"""
import os, json, csv, io, urllib.request, urllib.parse
import numpy as np

TIC = "438089101"
GAIA_ID = "5307278653764442880"
RA, DEC = 142.1202972504142, -55.64082239552683           # Gaia DR3 epoch 2016
OUT = os.path.dirname(os.path.abspath(__file__))
DL = os.path.join(os.environ["TEMP"], "heartbeats", "vet438089101")
os.makedirs(DL, exist_ok=True)
GAIA_OFF = 389.0                                          # BTJD = Gaia time (BJD - 2457389) + 389
C_KMS = 299792.458
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) vet438089101"}

API = "https://mast.stsci.edu/api/v0/invoke"
def mast(req, timeout=300):
    data = urllib.parse.urlencode({"request": json.dumps(req)}).encode()
    with urllib.request.urlopen(urllib.request.Request(API, data, headers=UA), timeout=timeout) as r:
        return json.load(r)

def tap(q, url="https://gea.esac.esa.int/tap-server/tap/sync", timeout=300):
    data = urllib.parse.urlencode({"REQUEST": "doQuery", "LANG": "ADQL", "FORMAT": "csv", "QUERY": q}).encode()
    txt = urllib.request.urlopen(urllib.request.Request(url, data, headers=UA), timeout=timeout).read().decode()
    return list(csv.DictReader(io.StringIO(txt)))

def download(uri, path):
    if os.path.exists(path):
        return path
    urllib.request.urlretrieve("https://mast.stsci.edu/api/v0.1/Download/file?uri=" + uri, path + ".part")
    os.replace(path + ".part", path)
    return path

def gaia():
    return json.load(open(os.path.join(OUT, "gaia.json")))

def say_to(fh):
    def say(*a):
        s = " ".join(str(x) for x in a); print(s, flush=True); fh.write(s + "\n"); fh.flush()
    return say

# ---------------- light curves -----------------
def load_qlp(path, allq=False):
    """Raw QLP SAP_FLUX. Returns t, f (normalised by median), q (quality), bkg."""
    from astropy.io import fits
    with fits.open(path) as h:
        d = h[1].data
        t = np.array(d["TIME"], float); f = np.array(d["SAP_FLUX"], float)
        q = np.array(d["QUALITY"], int); b = np.array(d["SAP_BKG"], float)
    m = np.isfinite(t) & np.isfinite(f) & (f > 0)
    if not allq:
        m &= (q == 0)
    t, f, q, b = t[m], f[m], q[m], b[m]
    return t, f / np.median(f), q, b

def load_spoc(path, col="SAP_FLUX"):
    from astropy.io import fits
    with fits.open(path) as h:
        d = h[1].data
        t = np.array(d["TIME"], float); f = np.array(d[col], float); q = np.array(d["QUALITY"], int)
    m = np.isfinite(t) & np.isfinite(f) & (f > 0) & (q == 0)
    return t[m], f[m] / np.median(f[m])

# ---------------- orbit -----------------
def kepler_E(M, e):
    M = np.mod(np.asarray(M, float), 2 * np.pi)
    E = M + e * np.sin(M) if e < 0.8 else np.full_like(M, np.pi)
    for _ in range(50):
        E = E - (E - e * np.sin(E) - M) / (1 - e * np.cos(E))
    return E

def true_anom(t, tp, P, e):
    E = kepler_E(2 * np.pi * (np.asarray(t, float) - tp) / P, e)
    return 2 * np.arctan2(np.sqrt(1 + e) * np.sin(E / 2), np.sqrt(1 - e) * np.cos(E / 2))

def M_of_nu(nu, e):
    E = 2 * np.arctan2(np.sqrt(1 - e) * np.sin(nu / 2), np.sqrt(1 + e) * np.cos(nu / 2))
    return np.mod(E - e * np.sin(E), 2 * np.pi)

def conj_phase(e, w_deg, kind):
    """Phase after periastron (0..1) of conjunction A (nu+w=90) or B (nu+w=270)."""
    nu = np.radians((90.0 if kind == "A" else 270.0) - w_deg)
    return M_of_nu(nu, e) / (2 * np.pi)

def tide(t, tp, P, e, w, inc, S):
    nu = true_anom(t, tp, P, e)
    R = (1 - e * e) / (1 + e * np.cos(nu))
    return S * (1 - 3 * np.sin(inc) ** 2 * np.sin(nu + w) ** 2) / R ** 3

def beam(t, tp, P, e, w, Bm):
    nu = true_anom(t, tp, P, e)
    return -Bm * (np.cos(nu + w) + e * np.cos(w))

def beaming_factor(teff):
    """Photon-weighted beaming factor <5 + dlnF_lambda/dln lambda> for a blackbody in a 600-1000 nm top-hat
    (TESS-like, photon counting; Bloemen et al. 2011 eq. 3 form). dF/F = factor * v/c."""
    h, c, k = 6.626e-34, 2.998e8, 1.381e-23
    lam = np.linspace(600e-9, 1000e-9, 801)
    x = h * c / (lam * k * teff)
    Fl = lam ** -5 / np.expm1(x)
    dln = -5 + x * np.exp(x) / np.expm1(x)          # dlnF_lambda/dln lambda
    wgt = lam * Fl
    return float(np.sum(wgt * (5 + dln)) / np.sum(wgt))

def binstat(x, y, edges, minn=3):
    idx = np.digitize(x, edges) - 1
    xb, yb, eb, nb = [], [], [], []
    for i in range(len(edges) - 1):
        m = idx == i
        if m.sum() < minn:
            continue
        v = y[m]
        xb.append(x[m].mean()); yb.append(v.mean()); eb.append(v.std(ddof=1) / np.sqrt(m.sum())); nb.append(m.sum())
    return np.array(xb), np.array(yb), np.array(eb), np.array(nb)
