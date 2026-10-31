> Historical report: superseded by the current reconciliation at ../../../reports/356435413/REPORT.md. Its original bytes are preserved in the source archive; this public copy is sanitized.

# TIC 356435413 (TYC 1550-693-1): adversarial check

Gaia DR3 4556850216755276672, SB1, P 27.47878 ± 0.00812 d, e 0.445 ± 0.013, ω 313.2 ± 2.0°, K1 34.54 ± 0.65 km/s. G 11.30, BP−RP 0.69, parallax 3.14 mas, RUWE 1.37, Teff 6244 K (GSP-Phot), R 1.249 R☉, M 1.244 M☉ (TIC). Checked by an Opus checker for Fable 5.1, 2026-10-22 (chunk-3 wave 4, 19:11–19:19). Saved from the checker's final message by Fable 5.1; the file tool refused REPORT.md. Scripts and outputs are in this folder, the log with the script behind each number in `progress.md`; downloads in `[local path omitted]

## Verdict: CONFIRMED (B only; A geometrically excluded)

The B eclipse is real, on target and periodic, with five events matching Gaia's period and B conjunction. The A eclipse is missing because the geometry rules it out, not because TESS failed to look.

## 1. Archives queried and what came back
- **Gaia DR3** 4556850216755276672 (`gaia_q.py`, `arch2.py`):
  - G 11.30, BP−RP 0.69, parallax 3.14 mas, RUWE 1.37, teff_gspphot 6244 K.
  - Gaia RV: rv_amplitude_robust 71 km/s over 44 transits.
  - Orbit (SB1): P 27.47878 ± 0.00812 d, e 0.445 ± 0.013, ω 313.2 ± 2.0°, K1 34.54 ± 0.65 km/s.
  - vari_summary: 0 rows. vari_eclipsing_binary: 0 rows.
- **VizieR TAP:** VSX, SB9 and WDS all 0 rows.
- **VizieR asu-tsv 60″ cones (`viz.py`):**
  - VSX, Prša+2022, IJspeert+2024, Kostov t3, Kostov t4, ASAS-SN II/366, ATLAS, ASAS ACVS and Gaia vclassre: all 0.
  - Kostov t2 (unvetted ML list, not prior art): the target itself at 0.001″.
  - The "Mowlavi" query returned 374 rows from the synthetic-photometry table, so it is not prior art.
- **`cats.py`:** VSX none, ASAS-SN none, Kostov t2 only. SIMBAD lists TYC 1550-693-1 as [SB*], which is the Gaia SB1, not an eclipsing binary.
- **ExoFOP:** HTTP 503 (tried in `arch2.py` and once by curl). CTOIs are therefore unchecked.
- **NASA Exoplanet Archive TOI table** (tid=356435413): no rows, so it is not a TOI.
- **Web search** ("TYC 1550-693-1"; "TIC 356435413" / the Gaia id): nothing on this star.
- **MAST CAOM (`archives.py`):**
  - QLP s25/26/52/53/79
  - SPOC 2-min s79
  - TESS-SPOC s25/26/52/53/79
  - TARS s25/26/52/53/79
  - TASOC s26 and DIAMANTE
  - All of these were fetched (DIAMANTE was not used), plus TESScut cutouts for s53 and s79.

## 2. Eclipses measured
Method (`ecl.py` → `ecl.txt`, `ecl_fits.png`): trapezoid supersampled over the exposure, with a quadratic baseline, fitted to raw SAP flux in every pipeline.

**B events (all near-V-shaped):**

| Sector | Mid-time (BTJD, mean over pipelines) | Depth | T14 | T12 | Flat | Notes |
|---|---|---|---|---|---|---|
| s25 | 1984.25051 ± 1.0 min | 1.70% | 3.39 h | 1.32 h | ~0.7 h | **New.** At sector start, QLP-flagged; unflagged in TESS-SPOC and TARS. The classifier did not list it. |
| s26 | 2011.72714 ± 1.0 min | 1.74% | 3.32 h | 1.26 h | ~0.8 h | QLP, TESS-SPOC, TARS, TASOC agree within 5 min |
| s52 | 2726.12407 ± 1.0 min | 1.60% | 3.36 h | 1.21 h | ~0.9 h | TESS-SPOC cadences all flagged; QLP unflagged |
| s53 | 2753.60053 ± 1.0 min | 1.68% | 3.58 h | 1.43 h | ~0.8 h | |
| s79 | 3468.00010 ± 1.0 min | 1.71% | 3.42 h | 1.38 h | 0.6 h | QLP, TESS-SPOC, TARS, SPOC 2-min |

- **Background:** the in-minus-out SAP_BKG difference (in its own units) is within about 1 sd of the out-of-eclipse scatter at every event.
- **Centroids:** shifts are ≤0.0035 px in QLP SAP_X/Y and ≤0.0008 px in TESS-SPOC/SPOC MOM_CENTR.
- **Blind census** (`lcview.py`, 0.1 d and 0.25 d boxes, >0.5%, quality-0 cadences): only these B events. No A-like event anywhere.
- **A windows:** nothing found (section 4).

## 3. Ephemeris and the Gaia comparison
From `ephem.py` → `ephem.txt`; conjunctions from `conjmc.py` → `conjmc.txt`, using this star's own Gaia covariance (corr_vec).

- **B ephemeris:** T0 = 1984.25002 ± 0.7 min, P = 27.476839 ± 0.000015 d. χ² 4.67 on 3 dof; all O−C ≤ 1.4 min.
- **Period vs Gaia:** 27.47878 ± 0.00812 d, so Δ = −0.0019 d (−0.24σ).
- **Timing vs Gaia's B conjunctions (ν = 270° − ω):** O−C −0.25 to −0.36 d, which is −0.39 to −0.52σ (σ 0.49–0.92 d).
- **e cos ω and e sin ω:**
  - Only one eclipse kind is seen, so neither can be measured from timing or duration ratio.
  - Gaia's values: e cos ω = +0.305 ± 0.015, e sin ω = −0.324 ± 0.013. The B−A phase separation is 0.7014 ± 0.0096.
  - So the A windows are B + 0.2986 P, ± 0.26 d.
  - No limb-darkened two-sphere fit was done, since without an A eclipse there is no e sin ω to derive from durations.

## 4. Independence tests
- **Other pipelines:** B is seen in QLP, TESS-SPOC and TARS in all five sectors, plus SPOC 2-min (s79) and TASOC (s26). Depths 1.50–1.87%; mid-times agree within 1.4–5 min.
- **Difference images** (`diffimg.py` on TESScut cutouts → `diffimg.txt`, `diff_s79B.png`, `diff_s53B.png`):

  | Sector | Deficit centroid offset from the light centroid | Peak deficit pixel | Depth 1×1 / 3×3 / 5×5 |
  |---|---|---|---|
  | s79 | 1.5″ | target pixel | 1.6 / 1.6 / 1.4% |
  | s53 | 0.9″ | adjacent pixel | 1.8 / 1.6 / 1.5% |

  At the pixel of the G 14.44 neighbour (44.5″) the dip is only 0.2%. No per-pixel regression fit was done (time).
- **Neighbour dilution** (Gaia G < 16 within 90″; the fractional dip each would need for 1.70%):

  | Neighbour | Separation | Dip it would need |
  |---|---|---|
  | G 14.44 | 44.5″ | 30% |
  | G 12.36 | 73.0″ | 5% (its pixel shows 0.0–0.1%) |
  | G 15.34 | 77.5″ | 70% |
  | G 15.80 | 85.0″ | 107% |

  The difference images exclude all of them.
- **A-conjunction coverage and limits** (`anull.py` → `anull.txt`, `anull.png`; window ±3σ = ±0.79 d):

  | Sector | A window (BTJD) | Best data | Largest 3.4 h box dip (sd) | Largest 6.7 h box dip (sd) |
  |---|---|---|---|---|
  | s25 | 1992.46 | TESS-SPOC, 100% coverage, 4% flagged | 0.049% (0.028%) | 0.030% (0.025%) |
  | s26 | 2019.93 | TESS-SPOC, 100% coverage, unflagged | 0.062% (0.051%) | 0.033% (0.034%) |
  | s79 | 3476.20 | SPOC 2-min, 99% coverage, flagged cadences | 0.094% (0.077%) | 0.062% (0.066%) |
  | s52 | 2734.33 | scattered light | unusable | unusable |
  | s53 | 2761.81 | scattered light | unusable | unusable |

  - In s53, TESS-SPOC shows a ~1% flagged depression lasting about 18 h (2761.85–2762.6). That is longer than any possible A eclipse (≤ 12 h), so I read it as scattered light.
  - Any A eclipse deeper than about 0.2% is excluded in three windows.

## 5. Physics
From `physics.py` → `physics.txt`.

- **Masses and orbit:** f(M) = 0.0842 M☉, so m2(i = 90°) is 0.65 / 0.68 / 0.71 M☉ for M1 = 1.15 / 1.244 / 1.35. a = 46.6–48.8 R☉.
- **The two conjunctions:**

  | | Separation | Central duration (TIC M1 1.244, R1 1.249) |
  |---|---|---|
  | B | 28.9 R☉ | 5.9 h |
  | A | 56.5 R☉ | 11.6 h |

  The A separation is 1.96 times the B separation.
- **Why A is missed:** the observed B T14 of 3.40 h implies b/(R1+R2) ≈ 0.82 and i ≈ 86.8°. At A that gives b ≈ 1.60. A Monte Carlo over Gaia's e and ω and over M1/R1 gives a 95% range of 1.50–1.70, with P(b_A < 1) = 0. An A eclipse would need R1 + R2 ≤ 1.33 R☉, which is impossible with R1 = 1.25. This is the classifier's "A coverage" question answered: A was covered (s25, s26, s79), is flat, and no eclipse is expected there.
- **Which star is in front:** B is at ν = 270° − ω, so the primary is in front and the K-dwarf companion is grazingly occulted. To first order (uniform disc) that needs the companion to supply about 10–11% of the light. A 0.68 M☉, 0.73 R☉, ~4400 K dwarf beside a 6300 K, 1.25 R☉ primary gives about 9% in the TESS band, so this is consistent. If B were the companion transiting the primary instead, the crude depth would be about 4%, too deep.
- **Shape:** the eclipse shape (T12 ≈ 1.3 h of 3.4 h, short or no flat bottom) fits a graze.

## 6. Verdict: CONFIRMED (B only; A geometrically excluded)
The deciding numbers:
- Five B eclipses across 1984–3468, in up to five pipelines, with consistent depth (1.6–1.7%) and duration (3.3–3.6 h).
- Linear O−C ≤ 1.4 min. Period matches Gaia to −0.24σ; timing is −0.4 to −0.5σ from Gaia's B conjunction.
- The difference images put the deficit on the target to within 1.5″. No neighbour can produce the dip.
- The A non-detection (< 0.1–0.2% in three covered windows) is predicted by Gaia's e = 0.445 and ω = 313°: b_A ≈ 1.6.

**Next predicted eclipses (BTJD):**

| Epoch | B eclipse (± 1.5–1.6 min) | A conjunction (no eclipse expected; ± 0.26 d) |
|---|---|---|
| E85 | 4319.7813 | 4327.99 |
| E86 | 4347.2581 | 4355.46 |
| E87 | 4374.7350 | 4382.94 |
| E88 | 4402.2118 | 4410.42 |
| E89 | 4429.6887 | 4437.89 |
| E90 | 4457.1655 | 4465.37 |
| E91 | 4484.6423 | 4492.85 |
| E92 | 4512.1192 | 4520.32 |

**What would settle it further:**
- A limb-darkened grazing-occultation fit of B to pin b and the companion's light fraction.
- A spectrum to detect the companion's light, which would test the ~9–11% light-ratio prediction.
- A future TESS sector that cleanly covers an A window, to confirm A is flat.

**Could not check:** ExoFOP (503), so CTOIs are unchecked. VizieR TAP responded but returned 0 rows for VSX, SB9 and WDS; the asu-tsv cones agree. Not done for time: no per-pixel regression fit (pixreg) and no s52 A-window recovery.

## Addendum, 2026-10-23 (Fable 5.1, 14:30 session): the ExoFOP re-query

ExoFOP was 503 at the check. Re-queried 2026-10-23 (`c3_other_check\exofop_requery.py`; raw JSON in
`c3_other_check\exofop_requery\356435413.json`). No TOI. **One CTOI: TIC 356435413.01**, user montalto,
created 2022-10-20, disposition PC, note "new CTOI, Montalto (2022)"; P 27.479625 d (no error given),
epoch BJD 2458956.7713 ± 0.0008 (BTJD 1956.7713), depth 14,077 ppm, duration listed as 0.118 (unit unclear),
Rp 15.8 ± 1.0 R⊕, b 0.44, i 89.67°; no follow-up uploaded. That epoch is one cycle before this report's
T0_B (1984.25002 − 27.476839 = 1956.77318; 2.7 min apart), i.e. the s25 B occultation found above under
QLP flags, and the CTOI period is 0.0028 d from the eclipse period. So the community planet candidate is
this B eclipse: with K1 34.5 km/s the occulted body is the 0.68 M☉ K dwarf, not a 15.8 R⊕ planet. Carry
into the paper with a CTOI code and the note, as A197 (CTOI 300202855.01) and A199 (CTOI 391925531.01) were.
