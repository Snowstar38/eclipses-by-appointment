"""Run 9a: polish a differential-evolution fit with Nelder-Mead (same chi^2, same data),
so chi^2 values at different e_out are compared at converged minima.
Usage: [JOINT=1] python3 a73_polish.py a73-secondary-phases.csv fit.json out.json"""
import sys, json
import numpy as np
from scipy.optimize import minimize
import a73_fit as F
t, ph, dep = F.load(sys.argv[1]); r = json.load(open(sys.argv[2])); e_out = r['e_out']
x0 = np.array([r['params'][k] for k in F.NAMES])
lo = np.array([b[0] for b in F.BOUNDS]); hi = np.array([b[1] for b in F.BOUNDS])
if 'm3_range' in r: lo[2], hi[2] = r['m3_range']
def f(x):
    if np.any(x[[0, 2, 5]] < lo[[0, 2, 5]]) or np.any(x[[0, 2, 5]] > hi[[0, 2, 5]]): return 1e6
    return F.chi2(x, e_out, t, ph, dep if F.JOINT else None)
m = minimize(f, x0, method='Nelder-Mead', options=dict(maxfev=900, xatol=1e-4, fatol=0.05, adaptive=True))
r2 = dict(r, chi2=float(m.fun), chi2_de=r['chi2'], params=dict(zip(F.NAMES, map(float, m.x))), polished=True)
json.dump(r2, open(sys.argv[3], 'w')); print(json.dumps(r2))
