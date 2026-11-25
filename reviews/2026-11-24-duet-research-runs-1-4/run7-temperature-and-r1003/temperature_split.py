"""Run 7a (Duet): does the circularisation of run 6d depend on stellar temperature?

Uses run 6d's |e cos w| table, joined by Fable 5 to TIC 8.2 and Gaia DR3 GSP-Phot temperatures
(duet-teff-secondaries.csv, in this folder), and the November 23 host table for the secondary
depths and visual notes.  Standard library only.  Run from the repository root:
    python3 reviews/2026-11-24-duet-research-runs-1-4/run7-temperature-and-r1003/temperature_split.py
Temperature: GSP-Phot where it exists (it fits extinction), TIC otherwise.  Giants (TIC
luminosity class) are left out.  'Eccentric' means |e cos w| > 0.05 (secondary displaced from
phase 0.5 by more than 0.032), a lower bound on e.  a/R1 uses TIC mass and radius with a
mass ratio of 1 (a changes as (1+q)^(1/3), so q = 0.5 would shrink it by 9%)."""
import csv, math, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = sys.argv[1] if len(sys.argv) > 1 else os.path.normpath(os.path.join(HERE, '../../..'))
rows = list(csv.DictReader(open(os.path.join(HERE, 'duet-teff-secondaries.csv'))))
host = {x['review_id']: x for x in csv.DictReader(open(
    os.path.join(REPO, 'reviews/2026-11-23-pipeline-and-survey-review/host-stars.csv')))}
G = 2.959122e-4            # AU^3 Msun^-1 d^-2
AU_RSUN = 215.032
CUT = 6250.0               # the Kraft break: radiative envelopes above, convective below
HEDGE = ('possible', 'difficult', 'displaced', 'unclear', 'marginal', 'weak')

def num(v):
    try: return float(v)
    except (TypeError, ValueError): return None

def lnC(n, k): return math.lgamma(n + 1) - math.lgamma(k + 1) - math.lgamma(n - k + 1)

def fisher_greater(a, n1, c, n2):
    """One-sided Fisher exact p: chance that group 1 has >= a successes given the margins."""
    K, N = a + c, n1 + n2
    return sum(math.exp(lnC(n1, x) + lnC(n2, K - x) - lnC(N, K)) for x in range(a, min(n1, K) + 1))

def solid(rid):
    """Conservative: secondary >= 1 ppt and >= 5% of the primary, and no hedging in the note."""
    h = host[rid]
    s, p = num(h['secondary_depth_ppt']), num(h['depth_ppt'])
    if s is None or p is None or s < 1.0 or s / p < 0.05: return False
    return not any(w in h['visual_reason'].lower() for w in HEDGE)

pts = []
for x in rows:
    if x['dropped_6a'] != 'False' or x['tic_lumclass'] == 'GIANT': continue
    T = num(x['teff_gspphot']) or num(x['teff_tic'])
    if T is None: continue
    P, M, R = float(x['P_d']), num(x['tic_mass']), num(x['tic_rad'])
    aR = (G * 2 * M * P * P / (4 * math.pi ** 2)) ** (1 / 3) * AU_RSUN / R if (M and R) else None
    pts.append(dict(id=x['review_id'], P=P, e=float(x['abs_ecosw']), T=T, aR=aR,
                    hot=T >= CUT, src='gspphot' if num(x['teff_gspphot']) else 'tic'))
hot = [p for p in pts if p['hot']]; cool = [p for p in pts if not p['hot']]
print('dwarf secondaries with a temperature: %d (%d hot >= %d K, %d cool)' % (len(pts), len(hot), CUT, len(cool)))

def table(key, bins, label):
    print('\n%s      cool: n  frac ecc     hot: n  frac ecc' % label)
    for a, b in zip(bins, bins[1:]):
        out = []
        for g in (cool, hot):
            s = [p['e'] for p in g if p[key] is not None and a <= p[key] < b]
            out.append('%5d   %5s' % (len(s), '%.2f' % (sum(e > 0.05 for e in s) / len(s)) if s else '  -  '))
        print('%6g-%-6g   %s      %s' % (a, b, out[0], out[1]))
table('P', [0, 2, 3, 4, 6, 10, 20, 200], 'P (d)      ')
table('aR', [0, 4, 7, 10, 15, 25, 1000], 'a/R1       ')

def test(label, sel, ecc=lambda p: p['e'] > 0.05):
    h = [p for p in hot if sel(p)]; c = [p for p in cool if sel(p)]
    he, ce = sum(map(ecc, h)), sum(map(ecc, c))
    print('%-46s hot %2d/%-3d = %.2f   cool %2d/%-3d = %.2f   p = %.2g' % (
        label, he, len(h), he / len(h), ce, len(c), ce / len(c), fisher_greater(he, len(h), ce, len(c))))
print('\nOne-sided Fisher tests (hot more often eccentric than cool):')
test('4 <= a/R1 < 10', lambda p: p['aR'] and 4 <= p['aR'] < 10)
test('4 <= a/R1 < 10, conservative secondaries', lambda p: p['aR'] and 4 <= p['aR'] < 10,
     lambda p: p['e'] > 0.05 and solid(p['id']))
test('4 <= P < 10 d', lambda p: 4 <= p['P'] < 10)
test('4 <= P < 6 d', lambda p: 4 <= p['P'] < 6)
test('10 <= P < 40 d (expect no excess)', lambda p: 10 <= p['P'] < 40)
for cut in (6000, 6500):
    h = [p for p in pts if p['T'] >= cut and 4 <= p['P'] < 10]; c = [p for p in pts if p['T'] < cut and 4 <= p['P'] < 10]
    he, ce = sum(p['e'] > 0.05 for p in h), sum(p['e'] > 0.05 for p in c)
    print('%-46s hot %2d/%-3d = %.2f   cool %2d/%-3d = %.2f   p = %.2g' % (
        'cut at %d K, 4 <= P < 10 d' % cut, he, len(h), he / len(h), ce, len(c), ce / len(c), fisher_greater(he, len(h), ce, len(c))))
print('\nEccentric systems at a/R1 < 10:')
for p in sorted([p for p in pts if p['aR'] and p['aR'] < 10 and p['e'] > 0.05], key=lambda p: (not p['hot'], p['aR'])):
    h = host[p['id']]
    print('  %-6s %-4s T=%5.0f (%s) P=%7.3f a/R1=%4.1f |ecosw|=%.3f sec %s / pri %s ppt %s' % (
        p['id'], 'hot' if p['hot'] else 'cool', p['T'], p['src'], p['P'], p['aR'], p['e'],
        h['secondary_depth_ppt'], h['depth_ppt'], '' if solid(p['id']) else '[not conservative]'))

# Logistic transition in log P: P(ecc) = fmax / (1 + exp(-(log P - l0) / w)), grid ML, bootstrap.
import random
def nll(s, l0, w, fm):
    L = 0.0
    for p in s:
        pr = min(max(fm / (1 + math.exp(-(math.log10(p['P']) - l0) / w)), 1e-6), 1 - 1e-6)
        L -= math.log(pr) if p['e'] > 0.05 else math.log(1 - pr)
    return L
def fit(s):
    return min((nll(s, l0 / 100, w, fm), l0 / 100) for l0 in range(0, 160, 2)
               for w in (0.03, 0.06, 0.12, 0.18) for fm in (0.6, 0.8, 1.0))[1]
lc, lh = fit(cool), fit(hot)
print('\nLogistic midpoint: cool %.1f d, hot %.1f d' % (10 ** lc, 10 ** lh))
random.seed(1); NB = int(os.environ.get('NBOOT', '100'))
d = sorted(fit([random.choice(hot) for _ in hot]) - fit([random.choice(cool) for _ in cool]) for _ in range(NB))
print('bootstrap (%d) of log P_mid(hot) - log P_mid(cool): median %.2f, 68%% %.2f..%.2f, 95%% %.2f..%.2f' % (
    NB, d[NB // 2], d[int(.16 * NB)], d[int(.84 * NB)], d[int(.025 * NB)], d[int(.975 * NB)]))


# Figure: |e cos w| against a/R1, hot and cool (writes ecosw-vs-aR-by-teff.svg next to this script).
W, H, L, B, Tm, R = 680, 420, 64, 52, 24, 24
lo, hi = math.log10(2), math.log10(60)
X = lambda a: L + (math.log10(min(max(a, 2), 60)) - lo) / (hi - lo) * (W - L - R)
Y = lambda e: H - B - min(e, 0.6) / 0.6 * (H - B - Tm)
COOL, HOT = '#2c6fbb', '#d1495b'
svg = ['<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d" font-family="sans-serif" font-size="12">' % (W, H),
       '<rect width="100%" height="100%" fill="white"/>',
       '<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="black"/>' % (L, H - B, W - R, H - B),
       '<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="black"/>' % (L, Tm, L, H - B),
       '<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" stroke="#999" stroke-dasharray="4 3"/>' % (L, Y(0.05), W - R, Y(0.05)),
       '<text x="%d" y="%.1f" fill="#666">0.05</text>' % (W - R - 30, Y(0.05) - 4)]
for a in (2, 3, 5, 10, 20, 30, 60):
    svg.append('<line x1="%.1f" y1="%d" x2="%.1f" y2="%d" stroke="black"/><text x="%.1f" y="%d" text-anchor="middle">%g</text>' % (
        X(a), H - B, X(a), H - B + 5, X(a), H - B + 20, a))
for e in (0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6):
    svg.append('<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" stroke="black"/><text x="%d" y="%.1f" text-anchor="end">%.1f</text>' % (
        L - 5, Y(e), L, Y(e), L - 8, Y(e) + 4, e))
svg.append('<text x="%d" y="%d" text-anchor="middle">a / R1 (TIC mass and radius, q = 1)</text>' % ((L + W - R) / 2, H - 12))
svg.append('<text x="16" y="%d" transform="rotate(-90 16 %d)" text-anchor="middle">|e cos ω| from secondary phase</text>' % ((Tm + H - B) / 2, (Tm + H - B) / 2))
for p in sorted(pts, key=lambda p: p['hot']):
    if p['aR'] is None: continue
    c = HOT if p['hot'] else COOL
    svg.append('<circle cx="%.1f" cy="%.1f" r="%s" fill="%s" fill-opacity="0.75"/>' % (X(p['aR']), Y(p['e']), '3.2' if p['hot'] else '2.4', c))
svg.append('<circle cx="%d" cy="%d" r="4" fill="%s"/><text x="%d" y="%d">Teff ≥ 6250 K (%d)</text>' % (L + 16, Tm + 10, HOT, L + 26, Tm + 14, sum(1 for p in hot if p['aR'])))
svg.append('<circle cx="%d" cy="%d" r="4" fill="%s"/><text x="%d" y="%d">Teff &lt; 6250 K (%d)</text>' % (L + 16, Tm + 28, COOL, L + 26, Tm + 32, sum(1 for p in cool if p['aR'])))
svg.append('</svg>')
open(os.path.join(HERE, 'ecosw-vs-aR-by-teff.svg'), 'w').write('\n'.join(svg))
print('\nwrote ecosw-vs-aR-by-teff.svg')
