# TIC 288160281 (TYC 4564-1186-1, Gaia DR3 1715865311931719680): per-object vet

**Verdict: CONFIRMED.** The eclipsing binary is the Gaia SB1 itself, grazing, with both eclipses detected. One open tension: the eclipse durations want e sin ω ≈ 0, which is 2.5–3.3σ from Gaia's value.

Wave 4, 2026-10-20/21. The first subagent was killed; the second resumed, as for TIC 142240367. (Saved by the parent session; the file-write tool refused REPORT.md for the subagent.)

## Deciding numbers
- **Primary eclipse, 41 events in 13 sectors (s014–s075):**
  - Every event has S/N 16–56.
  - Weighted depth is 16.18 ± 0.07 ppt (QLP SAP). Depth constancy χ² is 70.8 for 40 degrees of freedom.
  - Sector means run from 15.5 to 17.3 ppt; even and odd events give 16.19 and 16.20.
  - T14 is 1.92 h, with best T12/T14 of 0.4.
- **Secondary eclipse, 41 events, S/N 4.8–21:**
  - Phase **0.50726 ± 0.00005** (from the two ephemerides).
  - Depth 6.71 ± 0.07 ppt; T14 1.92 h (1σ range 1.88–1.98).
  - Fixed-shape test: S/N 32.1 at the measured phase. The look-elsewhere controls (518 phases) have rms 0.94 and a maximum of 2.8.
  - At Gaia's predicted phase, 0.5154, the test finds nothing (−4.9σ, sitting on the wings), so the measured phase is where the secondary is.
- **Ephemerides:**
  - Primary: P = 7.063961 ± 0.000002 d, T0 = 2597.74250 ± 0.00016 BTJD (E = 21), O−C rms 1.6 min.
  - Secondary: P = 7.063962 ± 0.000004 d; P2 − P1 = +0.24σ.
  - Against Gaia's P = 7.063673 ± 0.000331 d: **+0.87σ**.
- **Gaia conjunctions:**
  - The primary sits on **conjunction A**: +1.06 h (+1.55σ) at the Gaia epoch.
  - Within sectors the offset grows from +0.014 to +0.024 in phase (1.1–1.3σ). The growth comes from Gaia's P error, not from the eclipses (the wave-3 lesson).
  - The secondary sits on conjunction B: −0.32 h (−0.39σ).
- **Orbit shape:**
  - e cos ω = +0.0108 ± 0.0002, against Gaia's +0.0242 ± 0.0130 (−1.0σ).
  - The durations are equal (ratio 1.00, range 0.98–1.03). In the grazing model that gives **e sin ω ≈ 0 ± about 0.005**.
  - Gaia's e sin ω is −0.0325 ± 0.0099. At that value the model predicts T_B ≈ 2.6 h against the observed 1.92 h; a non-grazing chord would still predict a ratio of 0.94.
  - So the tension is 2.5–3.3σ. The likely cause is Gaia's eccentricity being biased high for a nearly circular orbit (Lucy–Sweeney): if e sin ω ≈ 0, then e ≈ 0.011 against Gaia's 0.043 ± 0.010.
  - This is a flagged open tension, like 1260529. It does not affect attribution: P, conjunction A timing and e cos ω all agree with Gaia.
- **Which star is in front:** the companion is in front at conjunction A, and that is where the deeper eclipse is.
- **Background and systematics:**
  - The unit-free fake-ppt regression gives median 0.06 ppt and maximum 2.54 ppt for the primaries (E −8, s040), far below 16 ppt.
  - One secondary, E 120 in s073, has fake 20 ppt and 15 flagged cadences. It is discounted; it has S/N 4.8 and is not needed.
  - The `dBKG` columns in `vet.py` and `check.py` have broken units here, as BRIEF-ADAPT warns, and are not used.
  - Five primaries include bit-32 cadences; their depths are normal.
  - No event falls within 0.5 d of a sector-wide systematic, and centroid shifts are 0.1 mpix or less on average.
- **Blind dip census:**
  - Of 96 dips at S/N ≥ 4, 40 are primaries.
  - All 4 off-ephemeris dips deeper than half the primary depth are secondaries (phase −0.493).
  - Everything else is 2.3 ppt or shallower, apart from three dips in noisy windows: 3300.53 (15.8 ppt, S/N 4.7 — the same flagged window as the discounted E 120 secondary) and 3346.39 (8.6 ppt, S/N 4.3, beside a primary).
- **Raw re-check (`check-out.txt`):**
  - 41 primaries, all positive, with sector medians of 15.0–16.8 ppt (central-depth estimator).
  - 37 secondaries, all positive, with a weighted depth of 6.31 ppt.

## Archives
- **VSX:** Gaia DR3 1715865311931719680 is typed ROT at 0″, from the Gaia classifier. That is a type revision to EB, not prior art.
- **Kostov+2025 table 2:** flagged at 0.001″. This is an unvetted ML list and does not count as catalogued.
- SIMBAD lists TYC 4564-1186-1 as [SB*].
- ASAS-SN, SB9, WDS and J/AJ/160/111: none.
- ExoFOP: no TOI or CTOI; no imaging or spectroscopy.
- **Gaia DR3:**
  - phot_variable_flag is VARIABLE, with G std 0.0072 mag and range 0.036 mag. That fits the eclipses.
  - It is in the classification results but not in vari_eclipsing_binary, and vari_eb is empty.
- A web search for "TYC 4564-1186-1" (2026-10-21) found nothing.
- **There is no prior eclipse classification, so this is new.**

## Independence
- **TESS-SPOC light curves, all 13 sectors (`indep-out.txt`):**
  - PDCSAP: 15.1–16.2 ppt.
  - SAP: 13.8–15.0 ppt.
- **Difference images, TESS-SPOC TPFs for 7 sectors (s040, 41, 48, 53, 60, 73, 74):**
  - In every sector the loss peaks on the central pixel (S/N 19–44).
  - The single-star fit always prefers the target over the 6.5″ neighbour: χ² 536 vs 890, 510 vs 1366, 322 vs 1082, 355 vs 888, 194 vs 434, 495 vs 981, and 389 vs 718.
  - The target's implied own dip is 12–14 ppt.
  - The 30-min sectors s014–s026 crashed in `tpfdiff.py` (an empty slice) and were not redone; the 7 consistent sectors suffice.
  - The batch diffimg (s040) puts the deficit 0.13″ from the light centroid, with the peak on target.
- **Neighbour dilution:**
  - Gaia 1715865311931719552 is G 14.15, 6.5″ away (Δm 2.68).
  - To produce these eclipses it would need dips of about **190 ppt** (primary) and **80 ppt** (secondary).
  - It is unrelated to the target: parallax 1.12 vs 4.55 mas, proper motion (6.7, −7.8) vs (−31.2, 0.2) mas/yr.
  - It is rejected by the difference-image χ² in all 7 sectors, by the centroid, and above all by the period: it would have to eclipse at Gaia's SB1 period to 0.9σ and at Gaia's conjunction A, with the secondary at Gaia's e cos ω.
  - TIC contratio is 0.075.

## Physics
- **Mass function and companion:**
  - f(m) = 0.109 M☉.
  - With M1 = 0.96 ± 0.12 and R1 = 1.11 ± 0.06 (a G8–K0 dwarf, Teff 5481 K): m2(i = 90°) = 0.61–0.70 M☉ and a ≈ 18 R☉.
- **Grazing geometry:**
  - A central chord would last about 5.3 h.
  - The observed 1.92 h gives b ≈ 1.5 and i ≈ 84.7°, so the eclipse is strongly grazing.
- **Predicted against observed depths (uniform disks, main-sequence companion):**
  - Primary: 10–14 ppt predicted; 13.8–16.2 observed, depending on the pipeline's dilution correction.
  - Secondary: 3–5.6 ppt predicted, 6.3–6.7 observed.
  - That is agreement within a factor of about 1.3. A grazing depth is steeply sensitive to R2 and b, and the model ignores limb darkening, so this is consistent but not a precision check.
- **Companion temperature and light:**
  - The depth ratio of 0.415 implies Teff2 ≈ 4380 K, against 4180 K for a main-sequence star of m2(i = 90°).
  - L2/L1 is about 0.13–0.17, still compatible with Gaia treating it as SB1.
- **Out-of-eclipse terms are small:** ellipsoidal (−c2) about −0.34 ppt, c1 about −0.8 ppt.
- **No heartbeat:** e = 0.043 and the depth is 16 ppt, so the heartbeat route is excluded.

## Next predicted eclipses (BTJD)
Errors are formal; the O−C rms is 1.6 min for the primary and 2.9 min for the secondary.
- **Primary (conjunction A):**
  - 4335.4770, 4342.5409, 4349.6049 (±0.8 min).
  - 4406.1166, 4413.1805, 4420.2445.
- **Secondary (conjunction B):**
  - 4339.0605, 4346.1244, 4353.1884 (±1.4 min).
  - 4402.6361, 4409.7001, 4416.7641.

## What would settle it further
The eclipse attribution is settled. Two things would resolve the open questions:
- An RV re-fit with e fixed near 0.011, or an independent RV orbit. That would test whether Gaia's e = 0.043 (e sin ω = −0.033) is the biased quantity.
- A light-curve model with limb darkening. It would close the factor-1.3 depth gap and give i, R2/R1 and the companion's temperature.
