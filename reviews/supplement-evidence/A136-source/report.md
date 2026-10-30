# TIC 344947332 (TYC 4004-778-1): per-object vet
Opus-model subagent for Fable 5, 2026-10-18 (saved by Fable from the agent's final message; the write tool refused in-agent). Batch row: G 11.46, P 10.45153 d, 9.0 ppt, 9 events, dphi +0.007.

**Verdict: CONFIRMED.** An M dwarf (about 0.16 Msun, 0.19 Rsun) transits an evolved F star (6200–6400 K, about 2 Rsun) every 10.451460 d. The transit is total and flat-bottomed, 9.0 ppt deep, and falls on Gaia's conjunction A. A **new 0.55 ppt secondary eclipse at phase 0.4845** is the M dwarf being hidden; its depth implies T2 ≈ 3200 K, right for a 0.16 Msun dwarf.

**1. Archives**
- `cats.py --r 60` with APPOINTMENTS_DATA set: no VSX or ASAS-SN entry; nothing in Prša, IJspeert or Kostov t2/t3/t4. SIMBAD: TYC 4004-778-1 [SB*].
- Gaia DR3: no vari_summary or vari_eclipsing_binary row. NSS SB1: P 10.45395±0.00724 d, e 0.081±0.082, ω 351±57°, K1 12.41±1.00 km/s, RUWE 0.86.
- SB9, WDS and J/AJ/160/111: nothing. ExoFOP: no TOI, CTOI, imaging or spectroscopy. Web search: nothing. Uncatalogued as a variable.

**2. Eclipses** (raw QLP SAP_FLUX, QUALITY==0, no trimming)
- All 9 events measured, S/N 18–43. Weighted depth 8.99±0.08 ppt; even 9.03±0.10, odd 8.91±0.14. A 10th event (BTJD 1773.42, s17) falls entirely in flagged cadences.
- Shape (2-min sectors): T14 7.54 h, ingress 54 min, flat bottom 5.73 h. V shape rejected at Δχ² > 700.
- Geometry from the shape: k 0.095, b ≈ 0.55, a/R1 ≈ 10.1.
- Background: SAP_BKG regression accounts for ≤ 0.11 ppt in every sector; in-eclipse centroid shift < 1 mpix; no event near a listed systematic time.
- Blind dip census: the 6 off-ephemeris dips are ≤ 1.3 ppt or sit on s024's post-gap scattered-light ramps (`look_s024.png`).
- **Secondary eclipse:** 0.550±0.083 ppt at phase 0.4845 (0.4840–0.4855) in s57/77/84, Δχ² 43. All 6 individual events positive; control phases give at most |S/N| 2.8; the 30-min sectors (s17+s24) show it independently at 0.50±0.16 ppt.

**3. Ephemeris and Gaia**
- P = 10.451460±0.000014 d, T0 = 2954.44026±0.00080 BTJD, O−C rms 3.2 min. Against Gaia's P: **−0.34σ**.
- Jackknife: dropping any one event moves P by ≤ 1.0e−5 d and depth by ≤ 0.1 ppt; the conjunction-A offset stays at −0.39σ for every drop. Largest timing outlier: s77 E156 (+8.2 min), normal depth and shape.
- Monte Carlo with Gaia's correlations: primary on conjunction A at −0.29 to −0.41σ in every sector; B as the primary's location disfavoured at 1.9–4.8σ. Gaia's A-to-B separation 0.536±0.043 vs TESS 0.4845 (−1.2σ).
- e cos ω from the secondary's phase: −0.0122±0.0008 vs Gaia +0.057±0.068 (−1.0σ). e sin ω from durations too weak to constrain.

**4. Independence**
- TARS s17/24/57/77/84: eclipses at 7.4–8.6 ppt. TESS-SPOC s24 PDCSAP: 9.53±0.18 ppt.
- TESS-SPOC s24 difference image: loss on the target, Δχ² ≈ 27,800 better than the next-best star — agreeing with the batch diffimg receipt (s57, 3.4″).
- Neighbour dips needed: G 13.21 @ 30″ → 45 ppt; G 14.52 @ 15.6″ → 152 ppt; G 15.72 @ 81″ → 460 ppt; G 16.06 @ 55″ → 625 ppt; G 16.49 @ 11.2″ → 93%; G 16.95 @ 19″ → impossible. All excluded by the image.

**5. Physics**
- f(M) = 0.00205 Msun → m2 = 0.15–0.17 Msun for M1 1.1–1.4 at i ≈ 87°.
- Separation ~22–23 Rsun; central transit 7.6–8.0 h, fitting the observed 7.54 h at b 0.55.
- R2 = k·R1 = 0.19–0.21 Rsun — right for a 0.16 Msun dwarf.
- Surface-brightness ratio J = 0.061 → T2 ≈ 3200–3260 K.
- M dwarf in front at conjunction A (deep total transit), F star in front at B (shallow total occultation). One geometry fits everything.

**6. Row notes** (nothing to strike or demote)
- P: 10.451460(14) d (the CSV's 10.45153 is 5σ off at the new precision). T0: 2954.44026(80) BTJD.
- The 9.0 ppt depth is correct; describe it as a flat-bottomed total transit.
- **Add the secondary: phase 0.4845, 0.55 ppt.**
- An F star + M dwarf EB with a planet-like transit; Gaia's K1 rules out a planet.
- "9 events" stands; a 10th exists in flagged s17 cadences.

**Next predicted eclipses (BTJD)**
- Primary: 4407.1932, 4417.6447, 4428.0961 (±3 min).
- Secondary: 4401.806, 4412.257, 4422.708 (±12 min).

**What would settle it further:** a 2-min SPOC light curve for a limb-darkened transit fit, and one RV epoch to pin down ω.
