"""One ledger of the catalogue and paper changes these findings propose, one row per change.
Run from the repository root:  python3 reviews/duet-findings/ledger.py  [out.csv]

status: proposed   evidence is firm; the change is not applied yet
        favoured   the evidence leans this way; one more check would settle it
        open       the evidence does not decide yet; the basis says what would
        for decision  a choice for whoever owns that table or text
A period proposal whose target the host table already holds is marked applied.
"""
import sys
import pandas as pd

HT = 'reviews/2026-11-23-pipeline-and-survey-review/host-stars.csv'
D = 'reviews/duet-findings/host-table/'
h = pd.read_csv(HT).set_index('review_id')
acc = set(pd.read_csv('accepted-systems.csv').review_id)
rows = {}   # (id, field) -> row; later entries replace earlier ones


SHOW = {'adopted_period_days', 'adopted_epoch_btjd', 'depth_ppt', 'secondary_phase', 'secondary_depth_ppt'}


def cur(rid, col):
    if rid in h.index and col in SHOW:
        v = h.loc[rid, col]
        return '' if pd.isna(v) else v
    return ''


def put(rid, field, col, proposed, status, basis, evidence, target='host-stars.csv'):
    rows[(rid, field)] = dict(id=rid, target=target, column=col, current=cur(rid, col) if target == 'host-stars.csv' else '',
                              proposed=proposed, status=status, basis=basis, evidence=evidence)


def P(rid):
    return float(h.loc[rid, 'adopted_period_days'])


# 1. Rows that adopt 2P but leave the secondary columns blank
c = pd.read_csv(D + 'nov23-column-flags.csv')
for r in c[c.check == '2P adopted, secondary columns blank'].itertuples():
    put(r.review_id, 'secondary', 'secondary_phase, secondary_depth_ppt', 'fill from the alternate-dip measurement',
        'proposed', '2P adopted because alternate eclipses differ, so a secondary was measured', D + 'nov23-column-flags.csv')

# 2. Double-lined rows whose text prefers 2P while the table adopts P
for r in c[c.check == 'text prefers 2P, table adopts P'].itertuples():
    put(r.review_id, 'text', 'period_resolution, limitation', 'reword: "P adopted; 2P if the components are twins"',
        'for decision', 'text argues 2P, table adopts P; adopt 2P only after a fold shows no off-phase secondary',
        D + 'nov23-column-flags.csv')

# 3. Secondary columns that contradict their own rows
f = pd.read_csv(D + 'secondary-column-flags.csv')
for r in f.itertuples():
    rid = r.review_id
    if rid in ('R1003', 'R1132'):
        continue                      # real eccentric secondaries; keep the columns
    if rid == 'R1796':
        put(rid, 'secondary', 'secondary_phase', 0.79, 'proposed', 'column holds 1 - phase', D + 'secondary-column-flags.csv')
    elif rid in ('R1349', 'R1421', 'R1459'):
        put(rid, 'secondary', 'secondary_phase', '1 - current phase, if the fold agrees', 'open',
            'phase looks mirrored, as in R1796; check the fold', D + 'secondary-column-flags.csv')
    else:
        put(rid, 'secondary', 'secondary_phase, secondary_depth_ppt', 'blank, or refit', 'proposed',
            str(r.flags), D + 'secondary-column-flags.csv')

# 4. Secondaries the visual review saw but the table lacks (P is the orbit)
MEAS = {'R1022': 0.292, 'R1029': 0.839, 'R1034': 0.544, 'R1634': 0.462, 'R1727': 0.771, 'R1757': 0.746}
s = pd.read_csv(D + 'secondary-seen-not-tabled.csv')
for r in s.itertuples():
    put(r.review_id, 'period', 'period_resolution', 'P: secondary seen; drop the 2P alternative', 'proposed',
        'visual note describes a secondary at P', D + 'secondary-seen-not-tabled.csv')
    if r.review_id in MEAS:
        put(r.review_id, 'secondary', 'secondary_phase, secondary_depth_ppt',
            f'phase {MEAS[r.review_id]}; depth from a fit', 'proposed', 'measured off the review sheet',
            D + 'secondary-seen-not-tabled.csv')

# 5. Equal-dip rows that are twins at 2P (a companion able to make the eclipse would show a secondary)
t = pd.read_csv(D + 'equal-dips-2P-test.csv')
for r in t.itertuples():
    if str(r.P_excluded_strict) == 'True':
        put(r.review_id, 'period', 'adopted_period_days', round(2 * r.P_d, 7), 'proposed',
            f'twin at 2P: P excluded (ratio {r.excl_ratio:.1f}, strict)', D + 'equal-dips-2P-test.csv')
    elif str(r.P_excluded_default) == 'True':
        put(r.review_id, 'period', 'period_resolution', f'2P favoured ({2 * r.P_d:.7g} d)', 'favoured',
            f'P excluded under default assumptions only (ratio {r.excl_ratio:.1f})', D + 'equal-dips-2P-test.csv')

# 6. Individual readings, which replace the general rules above
TW = D + 'twins-premise-output.txt'
for rid, why in [('R1253', 'parity 37 sigma; alternate eclipses differ by 2.5%, so not twins'),
                 ('R1697', 'odd/even 99.9 vs 76.0 ppt; the visual "secondary" is the alternate eclipse')]:
    put(rid, 'period', 'adopted_period_days', round(2 * P(rid), 7), 'proposed', why, TW)
for rid, why in [('R1405', 'phase-0.5 events 26.6 ppt median against 14.6 ppt needed at P; P not excluded'),
                 ('R1352', 'reviewer saw a shallower secondary; read the sheet'),
                 ('R1042', 'reviewer saw a weaker secondary; best feature 13.4 ppt at 0.60 is 78 h wide; read the sheet')]:
    put(rid, 'period', 'adopted_period_days', 'P or 2P', 'open', why, TW)
put('R1488', 'period', 'period_resolution', f'2P favoured ({2 * P("R1488"):.7g} d)', 'favoured',
    'odd/even mid-times differ 9.5 min overall, but per-sector signs disagree', TW)
put('R1040', 'period', 'adopted_period_days', 'leave P; fill the secondary from a fit', 'proposed',
    'reviewer saw a weaker feature at the secondary phase, which the SB2 text asks for', TW)
put('R1684', 'period', 'period_resolution', 'P: drop the 2P alternative', 'proposed',
    'Earthshine: equal primaries (28.5, 28.6 ppt) and an eclipse-shaped secondary', TW)
put('R1684', 'secondary', 'secondary_phase, secondary_depth_ppt', 'phase 0.520, 1.7 ppt', 'proposed',
    'Earthshine fit', TW)
put('R1692', 'period', 'period_resolution', 'P or 2P', 'open', 'visual note ambiguous; needs a fold', D + 'secondary-seen-not-tabled.csv')
put('R1022', 'period', 'period_resolution', 'P or 2P: odd cycles fall in the s91 gap', 'open',
    'alternate dips were never compared; 6.822 and 13.644 d both fit', D + 'secondary-seen-not-tabled.csv')
for rid, lo in [('R1727', 19), ('R1757', 24)]:
    put(rid, 'period', 'period_resolution', f'alias-limited; P >= about {lo} d', 'proposed',
        'one primary and one secondary per sector, years apart', D + 'secondary-seen-not-tabled.csv')
for rid in ['R991', 'R1084', 'R1120', 'R1529']:
    put(rid, 'period', 'adopted_period_days', round(2 * P(rid), 7), 'proposed',
        'TCE period is 2P and Earthshine parity confirms', D + 'tce-doubled-equal-dip-rows.csv')
put('R1090', 'period', 'period_resolution', f'2P favoured ({2 * P("R1090"):.7g} d)', 'favoured',
    'TCE period is 2P; parity untestable; twin test favours 2P', D + 'tce-doubled-equal-dip-rows.csv')
put('R1556', 'period', 'adopted_period_days', 'P or 2P', 'open', 'TCE period is 2P; parity does not confirm',
    D + 'tce-doubled-equal-dip-rows.csv')
put('R946', 'text', 'period_resolution', 'match the adopted 0.942508 d (Gaia SB2 orbit)', 'proposed',
    'text describes the shorter period; TCE and Gaia SB2 give the adopted one', D + 'tce-doubled-equal-dip-rows.csv')
put('R1737', 'period', 'adopted_period_days', 80.93, 'favoured',
    'a 252-ppt eclipse at 40.46 d needs a 96-ppt secondary that is not seen', D + 'twins-premise-output.txt')
put('R1758', 'period', 'period_resolution, limitation', 'P settled; drop the 2P twin and "P/2P degenerate"', 'proposed',
    'Earthshine: real 25 ppt secondary at phase 0.308 in odd and even cycles', D + 'earthshine-duration-results.csv')
put('R1758', 'secondary', 'secondary_phase, secondary_depth_ppt', 'phase 0.308, 25 ppt', 'proposed',
    'Earthshine fit', D + 'earthshine-duration-results.csv')
put('R1034', 'epoch', 'adopted_epoch_btjd, depth_ppt, secondary_phase',
    'move T0 by 0.544 P to the deeper (156 ppt) eclipse; record the shallower (~100 ppt) one as the secondary',
    'proposed', 'tabled 296.75 ppt matches neither eclipse; Earthshine fit', D + 'earthshine-duration-results.csv')
put('R1505', 'period', 'limitation', 'eccentric (e sin w >~ 0.3) or a smaller host; an RV orbit decides', 'open',
    'T14 2.56 h against a 4.71 h circular minimum, no secondary', D + 'earthshine-duration-results.csv')
put('R1117', 'period', 'adopted_period_days', 2.636664, 'proposed', 'alternate eclipses differ: B 2.4% shallower in 25 of 27 sectors against local flanks',
    'reviews/duet-findings/triples/r1117-depths-output.txt')
put('R1003', 'period', 'adopted_period_days, adopted_epoch_btjd, depth_ppt, secondary_depth_ppt',
    '2026 ephemeris: P 2.878843 d (s101 clock fault removed), T0 in s100, depths 144.4 / 76.5 ppt; note eclipses absent before 2026', 'proposed',
    'tabled epoch sits in an eclipse-free sector; tabled P is 21 sigma (scaled) off the 2026 one', 'reviews/duet-findings/timing/qlp-barycentre-output.txt')

# 7. Paper, accepted-systems and methods text
PAPER = [
 ('novelty', 'paper.html, README.md', 'novelty headline',
  'take 49 systems out of "no prior identification" (2,039 -> 1,990) or give them their own row', 'for decision',
  "49 accepted systems are in Chopard-Vilhem's public September list; 6 were never reconciled",
  'reviews/duet-findings/novelty/chopard-september-overlap.csv'),
 ('A73-chopard', 'paper.html', 'Chopard paragraph',
  'say his pipeline flagged seven A73 dips, all on the 17.54 d ephemeris', 'proposed',
  'independent support for the ephemeris and the fade', 'reviews/duet-findings/novelty/a73-chopard-dips.csv'),
 ('table4', 'paper.html', 'Table 4', 'add R716, R752, R787, R789 (24 contradicted orbits)', 'proposed',
  'eclipses land within 1-5 h of Gaia conjunctions at Gaia epoch; Gaia period > 3 sigma off',
  'reviews/duet-findings/gaia-errors/gaia-epoch-test-output.txt'),
 ('A29', 'paper.html', 'Table 4 note', 'note that conjunction B misses by 1.7 d at Gaia epoch', 'proposed',
  'A-sample Gaia-epoch test', 'reviews/duet-findings/gaia-errors/a-epoch-test-output.txt'),
 ('windows', 'paper.html', 'Section 2.2 window clause',
  'windows are about a 4.5-6 sigma correlated window; drop "costs sensitivity rather than correctness"', 'proposed',
  "Gaia's correlated conjunction errors run 1.3-1.7x small on the A sample",
  'reviews/duet-findings/gaia-errors/search-window-budget-output.txt'),
 ('R755', 'paper.html', 'R755 prediction windows', 'widen from +-0.05 d to about +-1 d', 'proposed',
  'third-body timing wander of hours; a two-eclipse prediction misses by a median 8-25 h after about two years',
  'reviews/duet-findings/triples/r755-prediction-miss-output.txt'),
 ('duration_h', 'methods.md', 'duration_h', 'say it is the detection box width, or replace with fitted T14', 'proposed',
  '459 of 855 values sit on 17 grid values; table is 0.41-0.83 of fitted T14',
  'reviews/duet-findings/host-table/nov23-column-flags.csv'),
 ('depth_ppt', 'methods.md', 'depth_ppt', 'say it is the mean depth inside the box (13% below the deepest point typically)',
  'proposed', '24% low for V-shaped eclipses, 2% for flat-bottomed', 'reviews/duet-findings/host-table/depth-column-output.txt'),
 ('tiers-gaia', 'R reviews', 'tier notes R716, R787, R789, R814',
  'Gaia tension no longer argues against association (right binary, wrong Gaia period)', 'for decision',
  'Gaia-epoch conjunction match', 'reviews/duet-findings/gaia-errors/gaia-epoch-test-output.txt'),
 ('tiers-conj', 'R reviews', 'tier notes R740, R816, R723, R755, R833',
  'held at probable for conjunction tension that a dozen confirmed A systems share, and that is within 2 sigma for all five once Gaia errors are scaled by goodness of fit', 'for decision',
  'Gaia-epoch test on the A sample; F2 error scale from 320 conjunctions', 'reviews/duet-findings/gaia-errors/fit-quality-scaling-output.txt'),
 ('R755-precession', 'paper.html', 'R755 note',
  "replace 'precession explanation unproved' with: Gaia's 300.8-d astrometric orbit is inclined at 66.9 deg, so the mutual inclination is >= 20 deg and nodal precession tilts the inner orbit fast enough (0.8-3.9 deg/yr against >= 0.5 needed)", 'favoured',
  'quadrupole precession from Gaia masses and the photocentre orbit; the s110-111 depths will test it', 'reviews/duet-findings/triples/r755-precession-output.txt'),
 ('yield-g11', 'paper.html, paper.pdf', 'Discussion, appointments yield',
  'print the G 11-11.5 sentence once and match Table 1: 45 of 50 reviewed, 42 confirmed, 1.6 per hundred, 5 unreviewed',
  'proposed', 'the sentence ("first twenty of fifty ... 0.8 per hundred ... thirty outstanding") is stale and appears three times in paper.html, twice in paper.pdf',
  'reviews/duet-findings/paper-text/paper-counts-output.txt'),
 ('s101-barycentre', 'review evidence, host tables', 'sector 101-104 eclipse times',
  'correct QLP s102-104 times by the full barycentric correction and s100-101 times by BC(t) - BC(TBJD 4069.5), then refit the 82 ephemerides that use s101+ events (24 move > 3 sigma)', 'proposed',
  's102-104 residuals track the Roemer delay (k = 1.02-1.08); s100-101 carry one correction frozen at TBJD 4069.5 (no free parameter: chi2 11.2/8 and 7.1/7 against 30.4 and 199 as barycentric)', 'reviews/duet-findings/timing/qlp-barycentre-periods.csv'),
 ('s14-15-clock', 'review evidence', 'sector 14 and 15 eclipse times',
  'replace QLP s14-15 eclipse times with TESS-SPOC re-times (45 of 73 done); keep 1.5x Roemer plus 1.6 min error for the rest', 'proposed',
  'the QLP early-sector columns carry a barycentric correction for the wrong position, per star: errors -7.3 to +16.7 min, 0.4-4.1x the delay; a single 1.5x leaves 96 s rms', 'reviews/duet-findings/timing/clock-model-check-output.txt'),
 ('published-ephemerides', 'review tables (period_days, period_error_days, primary_epoch_btjd)', '82 ephemerides using s101+ events',
  'refit with corrected times before publishing predictions: 2028 primaries move a median 6.5 min, > 10 min in 29, beyond 2 sigma in 33', 'proposed',
  'same periods as their measurements.json; corrected periods move > 1 published sigma in 51', 'reviews/duet-findings/timing/published-ephemeris-shifts.csv'),
 ('methods-timing', 'methods.md', 'timing section',
  'state that all times are BJD_TDB and that the QLP s14-15 and s100-104 times were corrected or replaced by TESS-SPOC', 'proposed',
  'those sectors time as if their clocks differ (see s101-barycentre, s14-15-clock)', 'reviews/duet-findings/timing/qlp-barycentre-output.txt'),
 ('A204-etv', 'paper.html', 'A204 note', "replace the open 'third body or a pipeline systematic' with: the s99-s102 swing is the sector 101-102 clock fault in the house's QLP times (5.0 min predicted, about 6 seen)", 'proposed',
  'clock model leaves 0.6 min rms of 1.9', 'reviews/duet-findings/timing/a-system-etvs-output.txt'),
 ('A167-etv', 'paper.html', 'A167 note', 'drop the s100-s101 swing as evidence of a short outer period (it is the frozen s100-101 clock correction); keep the slower +-2 min variation as the third-body hint', 'proposed',
  'the clock predicts a -2.3 min step, seen -2.6 / -2.9', 'reviews/duet-findings/timing/a-system-etvs-output.txt'),
 ('sb2-masses', 'paper.html', 'Section 3.4 or a new table',
  'give dynamical masses for the 35 eclipsing Gaia SB2s whose orbits hold at the eclipse period (median 1.10 Msun per star, 3% errors)', 'for decision',
  "eclipses fix sin i; masses reproduce the paper's A179 and A204 values and agree with TIC masses (median 0.98)",
  'reviews/duet-findings/masses/sb2-masses.csv'),
 ('R729', 'paper.html', 'Table 4', 'add R729 (25 with R716, R752, R787, R789): Gaia SB2 gives 0.30 + 0.31 Msun for a 5,800 K, 4.2 Lsun pair, and its period misses the eclipses',
  'proposed', 'masses 3.4x below the TIC mass; period and conjunctions already in tension',
  'reviews/duet-findings/masses/sb2-masses-output.txt'),
 ('R1819', 'R reviews', 'R1819 note', "say Gaia's SB2 cannot be right (e = 0.61 at 3.63 d; 0.35 Msun each for a BP-RP 0.78, M_G 3.8 pair); the eclipse period is Gaia's but not its K or e",
  'proposed', 'masses about 3x too small for the photometry; no other binary under 3 d is eccentric',
  'reviews/duet-findings/masses/sb2-masses-output.txt'),
 ('A108', 'paper.html', 'A108 note', 'call A108 a probable semi-detached Algol (q = 0.28 companion 1.5-4x its main-sequence radius)', 'favoured',
  'a 0.42 Msun main-sequence star makes at most 6-10% of the 21.4% eclipse; an ellipsoidal signal of about 1-3% at P/2 would settle it',
  'reviews/duet-findings/masses/low-q-sb2-output.txt'),
 ('A45', 'paper.html', 'A45 note', "say the 21.68-d Gaia SB2 is a real 1 Msun twin pair (masses fit, i about 67-83 deg, not eclipsing), so the 31.15-d eclipser is a second pair", 'favoured',
  'M sin3 i 0.98 + 0.93 Msun against a TIC mass of 1.12; unlike A54 the Gaia orbit is physical', 'reviews/duet-findings/masses/sb2-masses.csv'),
 ('A28', 'paper.html', 'A28 note', "note that Gaia's q = 0.50 needs a companion >= 3.6 Rsun (6x main-sequence) or wrong semi-amplitudes", 'open',
  "a 20% eclipse of an 8 Rsun giant; A28's Gaia orbit already fails on period and e cos w",
  'reviews/duet-findings/masses/low-q-sb2-output.txt'),
 ('A119', 'paper.html', 'A119 note', "note that Gaia also fits a 601-d astrometric orbit, so A119 is a triple; its light-travel semi-amplitude must be >= 3.4 min and its systemic velocity must swing by >= 9.8 km/s, which TESS timing cannot test but Gaia DR4's epoch RVs can", 'favoured',
  "same calculation gives 3.25 min for A95 against the measured 3.4 +- 0.3; Earthshine's 44 TESS times give -122 +- 96 s (SAP) or +109 +- 105 s (PDCSAP) at Gaia's orbit, consistent with zero and with the bound",
  'reviews/duet-findings/triples/dr4-gamma-predictions-output.txt'),
 ('A19-A72-A74', 'paper.html', 'A19, A72 and A74 notes', "add that Gaia's astrometric inclinations are edge-on within their errors (91.2 +- 2.4, 91.8 +- 3.0 and 90.3 +- 1.6 deg), as the eclipses require", 'proposed',
  'periods and conjunction times also agree with the eclipses; rms pull 0.91 over 12 checks on four astrometric orbits', 'reviews/duet-findings/gaia-geometry/astrometric-eclipsers-output.txt'),
 ('A95', 'paper.html', 'A95 note', "add that the timing follows Gaia's 541-d astrometric orbit in phase as well as period (amplitude 3.48 +- 0.25 min with Gaia's phase fixed; free phase within 9 deg)", 'proposed',
  "Gaia's elements fixed cut chi2 261.5 -> 61.6 with one parameter; the photocentre lower bound is 3.25 min", 'reviews/duet-findings/triples/a95-ltte-output.txt'),
 ('R630-etv', 'R reviews', 'R630 note', 'note a probable tertiary: curved timing (+-400 s), light-travel P3 1,440-2,580 d, m3 >= 0.54 Msun; the next TESS sector separates it from a period change', 'open',
  'linear chi2 373/18, quadratic 25.5/17, light-travel 14.8/15 on clock-clean times', 'reviews/duet-findings/timing/etv-orbits-output.txt'),
 ('R623-etv', 'R reviews', 'R623 note', "note a tertiary: an eccentric light-travel orbit (P3 >= 2,000 d, e about 0.5, semi-amplitude >= 350 s) fits all 160 TESS-SPOC eclipse times in 11 sectors; the short (2,000-2,500 d) and long (>= 3,500 d) branches part by about 33 min in sectors 121-123 and by 5-13 km/s in systemic velocity in 2018-19 (Gaia DR4)", 'favoured',
  "Earthshine's times: chi2 165/151 against 256,000 for linear ephemerides; Gaia DR3's conjunction and period do not separate the branches; the depths cap a main-sequence tertiary at about 0.4 Msun, so P3 beyond about 5,000 d needs a white dwarf",
  'reviews/duet-findings/timing/r623-gaia-branches-output.txt'),
 ('astrometric-triples', 'R reviews', 'R623, R630, R423 notes', "note that Gaia DR3 flags each as an astrometric binary (RUWE 3.0, 3.7, 1.7), independent evidence for the tertiary the timing shows; only 4 of 275 systems timed in three or more sectors carry the flag", 'proposed',
  'one-sided Fisher p = 4e-4 for 3 of 14 timing-variation candidates; an inner orbit of days cannot move the photocentre measurably', 'reviews/duet-findings/timing/astrometric-flag-output.txt'),
 ('sb1-triple-cut', 'paper.html', 'Discussion, third bodies (and the Limits paragraph)',
  "add that Gaia DR3 publishes SB1 orbits only below goodness of fit 3, so the SB1 input cannot hold an inner pair whose tertiary moves its systemic velocity by more than about one per-epoch RV error over 2014-17: it loses most pairs with a >= 0.5 Msun tertiary inside 2 yr and >= 1 Msun inside 4 yr, the triples with the largest light-travel signals; double-lined inputs have no such cut (A95 and A119 have goodness of fit 23)", 'proposed',
  'none of 1,312 Gaia SB1 rows in the repository reaches 3 (SB2s to 42); simulated DR3 RVs at the sample median N 22 and 3.7 km/s per epoch',
  'reviews/duet-findings/triples/sb1-triple-survival-output.txt'),
 ('R371-etv', 'R reviews', 'R371 note', 'note a possible tertiary: curved timing (+15 min in 2019, -9 min by 2021); if light travel, P3 >= 5.2 yr and m3 >~ 0.7 Msun, since the timing\'s 1.5-yr alternative would have kept Gaia from publishing the SB1', 'open',
  'quadratic chi2 79/23, circular light-travel 19.7/21; the 550-585 d island gives an 11 km/s rms systemic drift over DR3 (published in 1% of simulations)',
  'reviews/duet-findings/triples/sb1-gamma-drift-output.txt'),
 ('R423-etv', 'R reviews', 'R423 note', 'note a probable tertiary: periodic timing (+-150 s, P3 > 4 yr best), m3 >= 0.16 Msun', 'open',
  'linear chi2 1,611/14, quadratic 650/13, circular light-travel 9.2/11', 'reviews/duet-findings/timing/etv-orbits-output.txt'),
 ('abstract-methods', 'paper.html', 'Abstract, method totals',
  'Gaia-orbit period folds contribute 803 (not 804) and the mixed-method period-free follow-up 45 (not 46)', 'proposed',
  "current-accounting.json gives 803 and 45, summing with the other methods to 2,039; the Abstract's own mixed-method sentence says 45",
  'reviews/duet-findings/paper-text/paper-counts-output.txt'),
 ('tableA1-status', 'paper.html', 'A-labelled table, status column',
  'A74 confirmed; A30, A103, A125 and A157 marked as prior-known recoveries, not counted', 'proposed',
  'the release has A74 confirmed and excludes the other four; the column still says probable and confirmed (a note elsewhere explains)',
  'reviews/duet-findings/paper-text/paper-counts-output.txt'),
 ('table4-ecosw', 'paper.html', 'Table 4 and its rule',
  "count an e cos w failure only beyond 3 sigma of Gaia's error scaled by the solution's goodness of fit (1.24 exp(0.18 F2) for SB1s): A145 (4.6 sigma) and A65 (3.6) stand; A21, A63, A159 and A202 become tensions (1.7-2.2); A28 and A30 are SB2s with goodness of fit 14.9 and 23.7, so note that their contradictions are on poorly fitted solutions",
  'for decision', "Gaia's SB1 errors are right at F2 <= -1 and about 2x too small near F2 = 3 (conjunctions of 320 systems; the same scale brings circular short binaries' e/sigma to 0.95); 5.2 chance 3-sigma failures expected among 184 at the flat 1.37, 8 in Table 4",
  'reviews/duet-findings/gaia-errors/fit-quality-scaling-output.txt'),
 ('window-f2', 'paper.html', 'Limits (Gaia error calibration)',
  "add that Gaia DR3's SB1 errors grow with the solution's goodness of fit (about 1.0x at F2 = -1, 1.5x at 1, 2.1x at 3 on conjunctions and eccentricities), so appointment windows built from Gaia's errors are tight for poorly fitted orbits and generous for well-fitted ones; a window scaled by F2 calibrates every F2 quartile",
  'for decision', 'conjunction pulls at Gaia epoch widen with F2 (Spearman p = 0.001 for 155 A systems, 0.007 for 165 R systems); period pulls do not',
  'reviews/duet-findings/gaia-errors/fit-quality-scaling-output.txt'),
  ('yield-depth', 'paper.html', 'Discussion (why the appointments method works, and its yield)',
  "add that the yield is set by eclipse depth and Gaia orbit quality: in the G 11.5-12 cohorts deep eclipses (60 ppt or more) on orbits of significance 30 or more are found at the geometric rate (18 against 18.3 expected), shallow ones at about 0.4 of it and the day-long eclipses of giants at about 0.1, and weak orbits (significance below 15) yield about a fifth; per-hundred yields across magnitude bands mix these with each band's share of giants and weak orbits",
  'for decision', '155 eclipsing systems expected from the Gaia rows against 61 found; deep share of finds 40/61 against 35% expected (p = 1e-6); robust to depth floor, masses, companion radii and coverage',
  'reviews/duet-findings/yield/fresh-band-yield-output.txt'),
  ('faint-band-channel', 'paper.html', 'Methods (faint-band conjunction and raw-event search)',
  "say that the review leads came from visual sheets of the period-free raw-event harvest alone, so all 66 accepted claims carry a raw-event dip flag and none rests on the conjunction windows; the 485 conjunction-only passes were not reviewed (and show no excess of repeated dips at a fixed conjunction offset)",
  'proposed', 'triage_fresh*.py plots only bulk_events.py dip windows; 61 of 61 Gaia-period finds are dip-flagged, 49 also pass the appointment test',
  'reviews/duet-findings/yield/fresh-band-channels-output.txt'),
]
for pid, target, col, prop, st, basis, ev in PAPER:
    put(pid, 'paper', col, prop, st, basis, ev, target=target)

# a period decision replaces the general rewording of the same row
for rid, field in list(rows):
    if field == 'text' and (rid, 'period') in rows:
        del rows[(rid, field)]
L = pd.DataFrame(rows.values())


def applied(r):
    if r.target == 'host-stars.csv' and r.column == 'adopted_period_days':
        try:
            return abs(float(r.current) / float(r.proposed) - 1) < 1e-4
        except (TypeError, ValueError):
            return False
    return False


L.loc[L.apply(applied, axis=1), 'status'] = 'applied'
L['in_accepted'] = [('yes' if i in acc else 'no') if t == 'host-stars.csv' else '' for i, t in zip(L.id, L.target)]
key = L.id.map(lambda v: (0, int(v[1:])) if v[:1] == 'R' and v[1:].isdigit() else (1, 0))
L = L.iloc[key.argsort(kind='stable')]
L.to_csv(sys.argv[1] if len(sys.argv) > 1 else 'reviews/duet-findings/ledger.csv', index=False)
print('changes:', len(L), ' host-table rows touched:', L[L.target == 'host-stars.csv'].id.nunique())
print(L.groupby(['target', 'status']).size().to_string())
