"""Run 9a (Duet): assess the best A73 fits from a73_fit.py.
For each fit_e*.json: chi^2 rescaled to a 0.004 phase floor, rms residual, the model's
secondary-eclipse impact parameter b at each observed secondary (does it turn round in 2024
like the depths?), the predicted phase in 2026-2028, a long stability integration
(WHFast, 2000 outer orbits = 680 yr), and the photocentre a0 the fitted m3 implies.
Usage: python3 a73_assess.py a73-secondary-phases.csv fit_e*.json"""
import sys, json, math
import numpy as np
import rebound
sys.path.insert(0, __import__('os').path.dirname(__file__) or '.')
import a73_fit as F

PLX = 3.6223; L12 = 1.2**4 + 1.0**4
def a0_mas(m3):
    P = F.P_OUT / 365.25; M = F.M1 + F.M2 + m3
    return (M * P**2) ** (1/3) * (m3 / M - m3**4 / (L12 + m3**4)) * PLX, (M * P**2) ** (1/3) * (m3 / M) * PLX

def stable(p, e_out, n_orb=2000):
    sim = F.build(p['e_in'], p['omega_in'], p['m3'], e_out, p['omega_out'], p['M_out'], p['i_mut_deg'], p['phi'])
    sim.integrator = 'whfast'; sim.dt = F.P_IN / 40
    a0 = sim.particles[1].orbit(primary=sim.particles[0]).a
    for k in range(1, 201):
        sim.integrate(n_orb * F.P_OUT * k / 200, exact_finish_time=0)
        o = sim.particles[1].orbit(primary=sim.particles[0]); oo = sim.particles[2].orbit(primary=sim.com(last=2))
        if not (0.8 < o.a / a0 < 1.2) or o.e > 0.95 or oo.e >= 1:
            return f"UNSTABLE after {k / 200 * n_orb:.0f} outer orbits ({k / 200 * n_orb * F.P_OUT / 365.25:.0f} yr)"
    return f"stable for {n_orb} outer orbits"

if __name__ == '__main__':
    t, ph, dep = F.load(sys.argv[1])
    for fn in sys.argv[2:]:
        r = json.load(open(fn)); p = r['params']; e_out = r['e_out']
        x = [p[k] for k in F.NAMES]
        prim, sec = F.model_phases(x, e_out, t, span=3700 + 1000 - F.T_START)
        mph, b = F.phases_at(prim, sec, t)
        res = mph - ph
        b_r = b / (2.4 * 0.00465047)
        cp = float(np.sum((res / F.SIGMA) ** 2)); cd, D0 = F.depth_term(b, dep)
        print(f"\n== {fn}: e_out {e_out}, joint {r.get('joint', False)}: phase chi2 {cp:.1f} (floor 0.002; rms {np.sqrt(np.mean(res**2)):.4f}), depth chi2 {cd:.1f} (floor 0.005, scale {D0:.3f}), total {cp+cd:.1f}")
        print("   " + ", ".join(f"{k} {p[k]:.3f}" for k in F.NAMES))
        a_lum, a_dark = a0_mas(p['m3'])
        print(f"   photocentre a0 implied by m3 = {p['m3']:.2f}: {a_lum:.3f} mas (main-sequence) / {a_dark:.3f} (dark); Gaia 0.719 +/- ~0.06")
        print("   t_sec   obs    model   b_sec(R1+R2)  depth model")
        for i in range(len(t)):
            print(f"   {t[i]:8.1f} {ph[i]:.4f} {mph[i]:.4f}  {b_r[i]:5.2f}       {dep[i]:.3f} {D0*F.covered_fraction(b[i:i+1]/F.RSUN)[0]:.3f}")
        rho = np.corrcoef(np.argsort(np.argsort(b_r)), np.argsort(np.argsort(dep)))[0, 1]
        print(f"   Spearman(model b, observed secondary depth) = {rho:+.2f}  (deeper should mean smaller b: expect strongly negative)")
        # forecast
        st = np.array([s for s, _ in sec]); pt = np.array([q for q, _ in prim])
        for yr, btjd in (('2026.5', 4100.0), ('2027.5', 4465.0), ('2028.5', 4830.0)):
            j = np.argmin(abs(st - btjd)); k = np.searchsorted(pt, st[j]) - 1
            print(f"   forecast {yr}: secondary phase {(st[j]-pt[k])/F.P_IN:.4f}, b {sec[j][1]/(2.4*0.00465047):.2f}")
        print("   " + stable(p, e_out))
