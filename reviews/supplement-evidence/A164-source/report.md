# TIC 200745563 (TYC 8062-84-1, Gaia DR3 4749248636894211840): per-object vet

Opus 5.5 subagent, 2026-10-21. This resumes a wave-4 session that was killed before it wrote a report. Its receipts were re-checked rather than copied: T0 − 184P reproduces the E=0 time to 1 min, and the QLP depths re-measured with indep.py match vet.py. (Saved by the parent session; the file-write tool refused REPORT.md for the subagent.)

## Verdict: CONFIRMED. One eclipse per orbit, at Gaia conjunction B. Only one eclipse kind is seen, and the geometry predicts the other one misses.

Deciding numbers:
- **Eclipses:** 10 individual events in s003, s004, s030, s031 and s097, each at S/N 49–110. Weighted depth 18.45 ± 0.07 ppt (QLP SAP, Q==0). T14 5.10 h, T12 1.78 h.
- **Period:** P = 10.998961 ± 0.000002 d against Gaia's 10.997818 ± 0.001256 d, a difference of **+0.91σ**.
- **Timing:** every sector's eclipse lands on Gaia conjunction B, at +0.56σ to +0.78σ. Conjunction A is 11σ to 43σ away.
- **On target:**
  - The eclipse appears in QLP, TESS-SPOC FFI, SPOC 2-min and TGLC at 17.5–22.5 ppt.
  - The target is the best single-star fit in all 6 difference images.
  - Every Gaia neighbour would need a dip larger than 100% of its own light.
- **Conjunction A is empty:** −0.04 ± 0.07 ppt, 95% upper limit 0.23 ppt. That is what the geometry predicts:
  - Conjunction B is near periastron (r = 0.785a), with impact parameter 0.72–0.80 (R1+R2).
  - Conjunction A is at r = 1.195a, so the impact parameter scales to 1.09–1.21 (R1+R2). It misses by 0.25–0.67 R☉.

## 1. Archives (queried 2026-10-20/21)
- **cats.py --r 60** (re-run, same result): no hits in VSX, ASAS-SN, Prša+2022, IJspeert+2024 or Kostov+2025 t2/t3/t4. SIMBAD has only TYC 8062-84-1, typed [SB*].
- **Gaia DR3** vari_summary and vari_eclipsing_binary: empty.
- **SB9, WDS, J/AJ/160/111:** no entry.
- **ExoFOP:** no TOI, CTOI, imaging, spectroscopy or companions.
- **Extra VizieR cones at 30″** (ATLAS, ZTF and WISE variables, GCVS, VSX copy, ROSAT, 2RXS, 4XMM, ASAS-SN, LAMOST DR7, APOGEE DR17, Prša+2022): no rows; each control cone returned rows, so the queries worked.
  - J/A+A/674/A16 turned out not to be an EB table; it returns mixed sub-tables.
  - Incidentally, one of its rows is a G 11.76 star 453″ away with the same proper motion and parallax (17.0/−10.6 mas/yr, ϖ 2.66 vs 2.68). It is a likely wide co-moving companion, far outside any aperture.
- **Web search** on "TYC 8062-84-1" and "TIC 200745563": no relevant hits.
- **Batch receipts:**
  - c4-ebcats: none of the vetted or unvetted EB tables.
  - c4-vetsum: dphi −0.428/+0.009, ATTR.
  - diffrun-c4 s097: peak on target, deficit−target 4.16″.
- **No prior art.** This is a new eclipsing identification of a known Gaia SB1.

## 2. Eclipse measurements (vet-out.txt; raw QLP SAP_FLUX, Q==0, no trimming)

| E | sector | tc (BTJD) | ± (min) | depth (ppt) | S/N |
|---|---|---|---|---|---|
| 0 | s003 | 1388.3085 | 1.1 | 19.45 ± 0.39 | 50 |
| 1 | s003 | 1399.3064 | 1.4 | 19.33 ± 0.40 | 49 |
| 4 | s004 | 1432.3042 | 0.7 | 19.47 ± 0.23 | 85 |
| 67 | s030 | 2125.2377 | 0.7 | 19.93 ± 0.23 | 88 |
| 69 | s031 | 2147.2365 | 0.7 | 18.72 ± 0.22 | 85 |
| 71 | s031 | 2169.2333 | 0.7 | 19.31 ± 0.23 | 86 |
| 232 | s097 | 3940.0663 | 0.4 | 17.70 ± 0.16 | 110 |
| 233 | s097 | 3951.0662 | 0.4 | 17.86 ± 0.18 | 100 |
| 235 | s097 | 3973.0646 | 0.7 | 18.24 ± 0.21 | 86 |
| 236 | s097 | 3984.0625 | 0.4 | 17.54 ± 0.17 | 100 |

- **Shape:** T14 5.10 h (1σ range 5.10–5.16 h), T12 1.78 h, flat bottom 1.53 h. A pure V shape is worse by Δχ² +90.
- **Depth by sector:** s097 gives 17.8 ppt against 19.0–19.9 ppt in s003–s031. Crowding-corrected SPOC PDCSAP gives 18.3–19.1 ppt in the early sectors. Read as a QLP dilution difference between sectors.
- **Background:** the unit-free regression (bkgreg-out.txt) implies |ΔF| ≤ 0.07 ppt per sector, against a dip of 11–13 ppt in the same windows. Faking the eclipse would take +171 e⁻/s of background; the median in−out is −8 e⁻/s.
- **Centroids:** dX −0.23 ± 0.29 mpix, dY +0.30 ± 0.10 mpix.
- **Quality flags:** one event (E=67) has a single bit-32 cadence, and its depth matches the others. No event is within 0.5 d of a listed sector-wide systematic.
- **Blind dip census:** 11 of the 25 dips at S/N ≥ 4 are on the ephemeris.
  - **3967.406** (s097, 5.2 ppt): a pre-gap slide. Flux drops into flagged cadences (bits 32 and 30), X drifts, then a gap and a pointing jump (dip_3967.4.png). The same phase in other s097 cycles gives +0.18 ± 0.18 and −0.19 ± 0.19 ppt. It is a systematic.
  - **3950.766:** a matched-filter edge artefact next to the 3951.07 primary and flagged bit-29 cadences.
  - All other census dips are ≤ 1.8 ppt.
- **Control phases** 0.125–0.875: |depth| ≤ 0.16 ppt.

## 3. Ephemeris and orbit
- **Observed eclipse (conjunction B):** T0 = 3412.11666 ± 0.00017 BTJD (E = 184), P = 10.998961 ± 0.000002 d.
  - χ²/dof 16.6/8 (errors scaled ×1.44); O−C rms 0.8 min.
- **Against Gaia's B prediction** (Monte Carlo with corr_vec):

  | sector | measured − predicted |
  |---|---|
  | s003 | +2.2 h (+0.56σ) |
  | s004 | +2.2 h (+0.57σ) |
  | s030 | +4.0 h (+0.68σ) |
  | s031 | +4.0 h (+0.68σ) |
  | s097 | +8.6 h (+0.78σ) |

  The drift is Gaia's P being 0.9σ short.
- **Gaia orbit:** e cos ω = +0.097 ± 0.015, e sin ω = −0.207 ± 0.011. B − A in phase = 0.563 ± 0.010.
- **e cos ω and e sin ω can't be measured from the photometry here**, because only one eclipse kind is visible.
- **Duration test instead:**
  - At B (ν = 335°) a central chord would last 7.4–8.4 h for R1 = 2.0–2.5 R☉.
  - The observed 5.1 h implies b ≈ 0.72–0.80 (R1+R2) and i ≈ 83°.
  - At A, with the orbital separation ×1.52 larger, the projected separation is 1.09–1.21 (R1+R2), so there is no eclipse.
- **Fixed-shape test at the predicted A phase** (0.429 ± 0.010, scanned ±3σ, secA-out.txt):

  | duration | depth at predicted phase |
  |---|---|
  | T14 ×1 | −0.04 ± 0.07 ppt |
  | T14 ×1.5 | −0.05 ± 0.07 ppt |
  | T14 ×2 | +0.07 ± 0.06 ppt |

  The best S/N inside the window is 1.5–2.6, below the median of the control windows (2.3–3.1). 95% upper limits: 0.23, 0.22 and 0.37 ppt.

## 4. Independence
- **Second pipelines** (indep-out.txt, same ephemeris), depth in ppt:

  | pipeline | s003 | s004 | s030 | s031 |
  |---|---|---|---|---|
  | TESS-SPOC PDCSAP | 19.13 ± 0.18 | 19.10 ± 0.22 | 18.78 ± 0.15 | 18.43 ± 0.14 |
  | SPOC 2-min PDCSAP | — | — | 18.70 ± 0.13 | 18.26 ± 0.13 |
  | TGLC aperture | 21.6 | 22.5 | — | — |
  | QLP | 19.4 | 19.0 | 19.4 | 19.0 |

- **Difference images** (6 TPFs: TESS-SPOC s003/4/30/31 and SPOC 2-min s030/31):
  - The pixel with the largest flux loss is the target pixel every time, at S/N 30–52.
  - The best single-star PSF fit is the target every time, with an implied own dip of 14.8–17.4 ppt.
  - The 4.4″ neighbour (G 15.88) is next best by Δχ² +77 to +600, but would need a 1100–1500 ppt dip.
- **Dilution table** (needed dip = 18.45 ppt × 10^(0.4ΔG)):

  | neighbour | ΔG | needed dip |
  |---|---|---|
  | G 15.88 at 4.4″ | 4.87 | 1630 ppt |
  | G 15.37 at 28.7″ | 4.36 | 1020 ppt |
  | G 15.92 at 34.8″ | 4.91 | 1690 ppt |
  | G 16.43 at 44.7″ | 5.42 | 2700 ppt |

  None of them can produce the signal.

## 5. Physics (phys-out.txt, occfit-out.txt, occfit-vfix-out.txt)
- **Mass function** f(M) = 0.0804 M☉. Taking M1 = 0.96–1.2 M☉ (TIC: 0.96 ± 0.12 M☉, R1 2.27 ± 0.12 R☉, Teff 5500 K, a subgiant):
  - m2 at i = 90° is 0.57–0.65 M☉.
  - a = 24.0–25.6 R☉.
  - Central durations: 11.2–12.8 h at A, 7.4–8.4 h at B.
- **Which star is in front.** In Gaia's convention the primary is the nearer star at B, so the observed event is the companion being occulted.
  - Physical straight-chord fits to the 7 short-cadence events can't separate occultation from transit (Δχ² 0.0–0.5).
  - Fixing R1 from the orbital speed at B (v_t = 17.0 R☉/d, R1 = 2.27 R☉) breaks the tie:
    - **Occultation** needs k = 0.28 (R2 ≈ 0.64 R☉), b = 0.93 R1, and a companion light fraction of 3.0%. A 0.57–0.62 M☉ K dwarf is expected at R2 0.61–0.65 R☉ and 2.7–3.5% of the TESS light. This is self-consistent with the Gaia SB1 companion.
    - **Transit** at the same R1 needs the primary to supply only 48% of the light. It becomes physical only for R1 ≳ 2.7 R☉.
  - With the occultation solution, the projected separation at A is 1.42 R1, beyond 1 + k = 1.28, so A misses. A transit at A would have been 25–75 ppt deep, which the data exclude.
- **Heartbeat check.** B lies 25° from periastron, with e = 0.23.
  - A tidal signal would be about 1 ppt, spread over a periastron passage of roughly a day.
  - The fitted orbital harmonics are all under 0.7 ppt.
  - The observed event is 18 ppt, 5.1 h long and flat-bottomed. It is not a heartbeat.

## 6. Next predicted times (BTJD)
- **Observed eclipse** (companion occulted, conjunction B): **4336.0294, 4347.0283, 4358.0273** (± 0.0002 d), then every 10.998961 d.
- **Conjunction A** (no eclipse expected; upper limit 0.23 ppt): **4340.79, 4351.79, 4362.79** (± 0.13 d). This is phase 0.433 ± 0.012 after the observed eclipse.

## What would settle it further
- A high-S/N spectrum might show the companion. A K dwarf at about 3% of the light could appear as a cross-correlation bump, which would show directly that B is the occultation.
- Multi-colour eclipse depths: an occulted companion should give a deeper eclipse in redder bands.
- More TESS coverage of conjunction A would tighten the null.

## Files
- **Scripts:** vet.py, vetlib.py, indep.py (now also reads SPOC 2-min `*s_lc.fits`), tpfdiff.py, secA.py, occfit.py, phys_ecc.py, bkgreg.py, gaiatap.py, mastlc.py, morecats.py, extracats.py.
- **Outputs:** vet-out.txt, indep-out.txt, tpfdiff-out.txt, tpfdiff_*.png, secA-out.txt, secA-dips-out.txt, dip_3967.4.png, dip_3950.8.png, phys-out.txt, occfit-out.txt, occfit-vfix-out.txt, occfit_ph0.00.png, extracats-out.txt, cats-out2.txt.
- **Data:** `C:\Home\sky\data\qlp-sb-p20-60\pervet200745563\`.
