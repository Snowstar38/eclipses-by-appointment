> Historical report: superseded by the current reconciliation at ../../../reports/262471565/REPORT.md. Its original bytes are preserved in the source archive; this public copy is sanitized.

# TIC 262471565 (CD-36 14457): adversarial check

Gaia DR3 SB1, P 29.38574 ± 0.01343 d, e 0.095 ± 0.022, ω 92.1 ± 25.8°, K1 15.81 km/s, significance 41. G 11.03, BP−RP 1.21, parallax 1.923 mas, RUWE 0.94; TIC Teff 4891 K, R 4.56 R☉ (a giant), d 537 pc. Checked by an Opus checker for Fable 5.1, 2026-10-22 (chunk-3 wave 4, 19:11–19:20). Saved from the checker's final message by Fable 5.1; the file tool refused REPORT.md. Scripts and outputs are in this folder, checkpoints in `progress.md`; downloads in `[local path omitted]

## Verdict: CONFIRMED (A eclipses)

I found no catalogue entry for it. The second eclipse (B) is not detected, and that is the one open question.

## 1. Archives queried and what came back
- **ExoFOP:** HTTP 503 from both curl and `arch2.py`. **CTOIs are unchecked.**
- **NASA Exoplanet Archive TOI table** (TAP, `tid=262471565`): 0 rows, so it is not a TOI.
- **Gaia DR3** (`arch2.py`, `gaia_q.py`):
  - NSS SB1 orbit: P 29.38574 ± 0.01343 d, e 0.095 ± 0.022, ω 92.1 ± 25.8°, K1 15.81 km/s, Tp 8.207 ± 2.04 (J2016-relative), significance 41.
  - `vari_summary` 0 rows, `vari_eclipsing_binary` 0 rows.
  - G 11.03, BP−RP 1.21, parallax 1.923 mas, RUWE 0.94, ipd_frac_multi_peak 0, rv_amplitude_robust 28.7 km/s.
- **VizieR** (TAP in `arch2.py`; asu-tsv 60″ cones in `viz.py`):
  - VSX: one row, the neighbour Gaia DR3 6778562100901726848 at 35.4–36″, G 14.44, type DSCT|GDOR|SXPHE. Nothing at the target.
  - Prša+2022, IJspeert+2024, Kostov t2/t3/t4, ASAS-SN II/366, SB9, WDS, ATLAS, ASAS ACVS: 0 rows each.
  - Gaia vclassre: only the same 36″ δ Sct/γ Dor neighbour.
  - The "Mowlavi+2023" query returned 356 rows, but that is the synthetic-photometry table, not prior art.
- **`cats.py`:** VSX has only the 35″ DSCT neighbour; ASAS-SN none. SIMBAD has CD-36 14457 as [SB*], which is presumably from the Gaia NSS orbit, since nothing else lists it.
- **Web search** for "CD-36 14457" / "TIC 262471565": no source mentions this star. Results were unrelated papers, e.g. [arXiv 2510.27470](http[local path omitted]) and [arXiv 2302.00320](http[local path omitted]).
- **MAST CAOM** (`archives.py`): QLP s1/27/95. Sector 1 also has eleanor-lite, T16, TASOC and TGLC. There is no SPOC 2-min, TESS-SPOC or TARS product. I downloaded TESScut 15×15 cutouts for s1, s27 and s95.
- **Target (TIC):** Tmag 10.40, Teff 4891 K, R 4.56 R☉, a giant, d 537 pc.

## 2. Every eclipse measured
Fits are trapezoid × quadratic baseline on raw SAP, ±1.3 d, no trimming (`ecl2.py` → `ecl2.txt`).

**A eclipses:**

| Event | Source | t0 (BTJD) | Depth | T14 | T12 | Flat part | Notes |
|---|---|---|---|---|---|---|---|
| s1 A | QLP, q==0 | 1337.4310 ± 0.08 h | 0.436% | 20.6 h | 2.5 h | 15.7 h | BKG flat (ΔBKG −9, sd 127); Δcentroid +0.001/+0.004 px (sd 0.0025) |
| s1 A | QLP, all cadences | 1337.4329 | 0.418% | | | | |
| s1 A | eleanor-lite | 1337.434 | 0.51% | | | | |
| s1 A | TASOC | 1337.470 | 0.37% | | | | |
| s1 A | TGLC aperture | 1337.442 | 0.55% | | | | |
| s1 A | TGLC PSF | 1337.445 | 0.47% | | | | |
| s27 A | QLP, q==0 | 2042.5424 ± 0.08 h | 0.448% | 21.4 h | 3.2 h | | all-cadence fit identical |
| s95 A | QLP, q==0 | 3893.4893 ± 0.06 h | 0.347% | 20.4 h | 2.3 h | | all cadences: 3893.483, 0.32% |

Notes on the events:
- **s1:** the T16 file's time column is unusable, so I skipped it.
- **s27:** QLP's SAP_BKG drops from about 57,000 to 0 at 2041.6, with a 0.02 px SAP_X step and a brief return at about 2042.3. The flux has no step there, so this is QLP background bookkeeping, not the eclipse. My own-background TESScut photometry reproduces the event.
- **s95:** QLP's SAP_BKG rises about 150 e⁻/s from 3892.8 through the event, into the flagged pre-gap scattered light, and the centroid moves about 0.006 px. This is the one worrying coincidence. However:
  - my own TESScut photometry, with its own background (the faintest 40% of pixels), gives t0 3893.4906 (+2 min) and 0.40%;
  - the time was predicted from s1 and s27 to within 2 minutes.
- **Own TESScut photometry** (`tcphot.py`, 3×3 aperture): 1337.442 / 2042.549 / 3893.491 at 0.47 / 0.45 / 0.40%.
- **Blind census** (`lcview.py`, 0.25-d box, >0.2%, q==0): only the three A events, plus s95 3899.98, which is an orbit-end scattered-light descent and not at any conjunction.

**B eclipses:** none detected. Gaia-predicted B times inside the data:
- s1 1351.99 ± 0.61, partly flagged.
- s27 2057.23 ± 0.85, fully covered with unflagged data.
- s95 B windows (3879.1, 3908.5) fall outside the sector.

## 3. Ephemeris and Gaia comparison
From `ephem2.py`; the conjunctions come from `conjmc.py` using this star's own corr_vec.

- **A ephemeris:** T0 = 1337.4273 ± 16.9 min, P = 29.38001 ± 0.00022 d (epochs 0, 24, 87).
  - O−C: +5.2, −7.3, +2.0 min; χ² 0.20 for 1 degree of freedom. Errors include a 20-min floor, the scatter between pipelines in s1.
  - My own TESScut times give P 29.37990.
- **Against Gaia:**
  - P differs by −0.0057 d, which is −0.43σ.
  - The cycle-count aliases N = 23 and N = 25 would sit at +95σ and −88σ from Gaia's P, so the count is unambiguous.
  - Observed minus Gaia's predicted A conjunction: +0.003 d (+0.01σ), −0.157 d (−0.21σ), −0.519 d (−0.33σ).
- **e cos ω and e sin ω:** these can't be measured from eclipses without B. Gaia's Monte Carlo gives B−A phase separation 0.4978 ± 0.0258, e cos ω −0.003 ± 0.040, e sin ω +0.088 ± 0.021.

## 4. Independence tests
- **Other pipelines (s1):** eleanor-lite, TASOC and both TGLC fluxes all show A at 0.37–0.55%, within 1 h of QLP.
- **Own photometry** from TESScut in all three sectors: see section 2.
- **Per-pixel regression** (`pixlite.py`, per pixel: quadratic + trapezoid template):
  - The flux deficit peaks on the target pixel or the one next to it in every sector, at S/N 12–21.
  - The fractional depth is roughly the same across the PSF core.
  - Deficit centroid offsets from the target: (−0.22, +0.01), (−0.08, +0.03), (−0.08, +0.23) px.
  - These do not point toward the only G<15 neighbour, which sits at (−0.68, +1.59), (−0.50, +1.66) and (+0.66, −1.61) px; in s95 the offset points the opposite way.
  - Aperture depths (1×1 / 3×3 / 5×5): s1 0.82 / 0.47 / 0.41%; s27 0.50 / 0.45 / 0.43%; s95 0.39 / 0.40 / 0.39%.
- **Neighbour dilution** (dip each neighbour would need, depth × 10^(0.4 Δm)):

| Neighbour | Separation | Dip needed | Comment |
|---|---|---|---|
| G 14.46 | 36.5″ | 10.6% | A known δ Sct/γ Dor; can't make a 20-h flat-bottomed dip; no deficit at its pixel |
| G 15.39 | 52.7″ | 25% | |
| G 15.21 | 87.6″ | 21% | |
| all others (G>16) | | >50% | |

- **B null and limits** (`bscan.py`, `bjoint.py`, `bflank.py`, `bview.py`):
  - At the Gaia-predicted centre, the 22–24 h box depth is −32 to −62 ppm in s27 (empirical sd about 190) and about −220 ppm in s1 (sd 245).
  - Joint statistic over phases away from A and B: sd 208 ppm, 95th percentile +341.
  - The only positive point is at phase 0.480 (2056.65): +647 ppm in the box fit, but only +223 ppm when referenced to the flanks. At the same phase s1 gives +981 ppm, which equals the null maximum and sits next to scattered light.
  - So this is a weak hint, not a detection.
  - s27 excludes a B deeper than about 600 ppm at phases 0.49–0.52.

## 5. Physics
From `phys2.py`.
- **Mass function:** f(M) = 0.01187 M☉.
- **Companion mass at i = 90°:** 0.27 / 0.34 / 0.41 / 0.47 M☉ for M1 = 1.0 / 1.5 / 2.0 / 2.5 M☉.
- **Orbit size:** a = 43–58 R☉; R1/a = 0.08–0.105.
- **Companion radius:** the 0.45% depth on a 4.56 R☉ giant gives k ≈ 0.064 and R2 ≈ 0.29 R☉. That is an M dwarf, consistent with m2.
- **Which star is in front:** at A (ν = 90° − ω, close to periastron) the companion transits the giant. The A timing agrees with Gaia's RV-derived conjunction, which settles this.
- **Durations:** predicted central T14 at A is 17–23 h; observed 20–21 h (central transit for M1 about 1.5). At B it would be 21–28 h.
- **Expected B depth:** a full occultation of an M dwarf would be about 570–1100 ppm (blackbody surface-brightness ratio, or absolute-magnitude estimate). The impact parameter at B is 1.21 × b_A, so B would be missed only if b_A > ~0.78. Otherwise B must lie near phase 0.48 (e cos ω ≈ −0.03, 0.7σ from Gaia) or be at the shallow end of that range.
- Depth, duration and shape all fit one geometry. The missing B is a mild tension, not a refutation.

## 6. Verdict: CONFIRMED (A eclipses)
The deciding numbers:
- Three A events in three sectors, seen in five independent reductions in s1 and in my own pixel photometry in every sector.
- The deficit is centred on the target.
- P matches Gaia at −0.43σ, and every event matches Gaia's A conjunction within 0.33σ.
- The s95 time was predicted from s1 and s27 to within 2 minutes.
- The depth equals k² for the companion mass implied by the mass function.

**Next predicted eclipses (BTJD):**

| A (±0.6 h) | B, Gaia phase separation (±0.76 d) | B at the 0.480 hint |
|---|---|---|
| 4363.568 | 4378.19 | 4377.67 |
| 4392.948 | 4407.57 | 4407.05 |
| 4422.328 | 4436.95 | 4436.43 |
| 4451.708 | 4466.33 | 4465.81 |
| 4481.088 | 4495.71 | 4495.19 |

**What would settle it further:**
- An unflagged TESS (or ground-based, ≤300 ppm) observation of a B window around phase 0.47–0.52, to detect or rule out the M-dwarf occultation.
- RVs or spectroscopy to fix M1 and R1.
- ExoFOP CTOI check once the service is back.
