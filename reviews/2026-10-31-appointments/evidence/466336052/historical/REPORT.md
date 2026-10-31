> Historical report: superseded by the current reconciliation at ../../../reports/466336052/REPORT.md. Its original bytes are preserved in the source archive; this public copy is sanitized.

# TIC 466336052 (TYC 1121-892-1): adversarial check

Gaia DR3 SB1, P 32.1465 ± 0.0462 d, e 0.233 ± 0.048, ω 313.6 ± 12.9°, K1 14.55 km/s. G 11.45, BP−RP 0.82, parallax 3.08 mas, RUWE 1.00; TIC R 1.44 R☉, Teff ~5850 K. Checked by an Opus checker for Fable 5.1, 2026-10-22 (chunk-3 wave 5, 19:22–19:30). Saved from the checker's final message by Fable 5.1; the file tool refused REPORT.md. Scripts and outputs are in this folder, each step and the script behind each number in `progress.md`; downloads in `[local path omitted]

## Verdict: CONFIRMED (A eclipses only)

This is an eclipsing companion to the Gaia SB1, with the companion in front of the primary at conjunction A. Only two A eclipses exist, and B has never been observed.

### 1. Archives (what was queried and what came back)
- **Gaia DR3** (`gaia_q.py`, `arch2.py`):
  - Star: G 11.45, BP−RP 0.82, parallax 3.08 mas, RUWE 1.00, non_single_star 2.
  - Orbit (NSS SB1): P 32.1465 ± 0.0462 d, e 0.233 ± 0.048, ω 313.6 ± 12.9°, K1 14.55 km/s. rv_amplitude_robust is 28.7 km/s.
  - vari_summary and vari_eclipsing_binary: 0 rows.
- **Neighbours:** no Gaia source brighter than G 15 within 60″. The nearest bright ones are G 13.97 at 65.5″ and G 16.08 at 68.4″.
- **VizieR TAP** (VSX, SB9, WDS): 0 rows.
- **VizieR asu-tsv 60″ cone** (`viz.py`): 0 rows from VSX, Prša+2022, IJspeert+2024, Kostov t2/t3/t4, ASAS-SN II/366, SB9, WDS, ATLAS, Gaia vclassre and ASAS ACVS. The "Mowlavi" query hits a synthetic-photometry table, which is not prior art.
- **`cats.py`:** VSX none, ASAS-SN none. SIMBAD lists TYC 1121-892-1 as [SB*] only.
- **ExoFOP: HTTP 503** both in `arch2.py` and in a direct retry, so CTOIs are unchecked. The NASA Exoplanet Archive TOI table has no TOI for tid 466336052.
- **MAST CAOM** (`archives.py`): QLP, TARS and TESS-SPOC exist for s55 (600 s) and s82 (200 s). There is no SPOC 2-min, TGLC or eleanor product.
- **Web search** ("TYC 1121-892-1" / "TIC 466336052"): nothing about this star.

### 2. Eclipses measured
Method: trapezoid fit to raw SAP, quadratic baseline, error = profile χ² × red-noise β. Script `ecl.py`, output `ecl.txt`.

| Event | Pipeline | t0 (BTJD) | ±min | depth | T14 h | T12 h | flat h |
|---|---|---|---|---|---|---|---|
| A s55 | QLP q0 | 2818.48301 | 0.6 | 4.41% | 9.62 | 1.97 | 5.68 |
| A s55 | TESS-SPOC | 2818.48311 | 0.7 | 4.12% | 9.60 | 1.98 | 5.64 |
| A s55 | TARS | 2818.48286 | 0.6 | 4.14% | 9.49 | 1.90 | 5.69 |
| A s82 | QLP q0 | 3557.68402 | 0.8 | 4.28% | 9.64 | 2.03 | 5.58 |
| A s82 | TESS-SPOC | 3557.68434 | 0.8 | 4.07% | 9.63 | 2.04 | 5.55 |
| A s82 | TARS | 3557.68534 | 0.6 | 3.95% | 9.77 | 2.09 | 5.59 |

- **Quality flags:** no flagged cadences inside either eclipse. The all-cadence fits are the same as the q0 fits.
- **Background:**
  - s55: no excursion (ΔBKG −507, sd 2580, QLP units).
  - s82: ΔBKG is +2600 (sd 367) in QLP and +262 (sd 169) in TESS-SPOC. This is an end-of-orbit background ramp. The s55 eclipse has the same shape and depth without it.
- **Centroids:** shifts are ≤ 0.005 px.
- **Data gap:** QLP s82 has a gap starting at 3557.93, just after egress. TESS-SPOC covers through 3558.47.
- **Blind census** (`look.py`, 0.15 d and 0.3 d boxes, threshold 0.15%): besides the two A eclipses it found only:
  - s55 2803.2: flagged scattered-light region.
  - s55 2808.95 (0.17%): outside the B window. If it were B, the same phase in s82 (≈3548.1) should show a dip, and that data is clean and flat.
  - s82 3545.0–3545.45 (0.16%): common mode. `commonmode.py` shows 24 stars within 8° in s82 have a median dip of 0.125% there, and 62% have at least 0.1%.

### 3. Ephemeris and Gaia comparison
- **Linear ephemeris** (`physics.py`): with 23 cycles between the two eclipses, P = 32.139199 ± 0.000037 d and T0 = 2818.48299 ± 0.7 min. Two events leave no degrees of freedom, so there is no O−C test.
- **Period vs Gaia:** −0.16σ. The neighbouring cycle counts fail badly: N = 22 gives +31σ and N = 24 gives −29σ.
- **Conjunction times** (`conjmc.py`, using this star's own corr_vec):
  - A predicted 2818.80 ± 3.02; observed −0.32 d (−0.10σ).
  - A predicted 3558.17 ± 4.07; observed −0.49 d (−0.12σ).
  - Gaia's timing errors are large (≈3–4 d), so the timing agreement is weak evidence on its own.
- **Gaia's e cos ω and e sin ω:** the B−A phase separation is 0.6016 ± 0.0375. That gives e cos ω = 0.158 ± 0.059 and e sin ω = −0.161 ± 0.038. Conditioning on the observed A time (`bcond.py`) narrows the separation to 0.601 ± 0.034.
- **Where B should fall:** about 2805.67 ± 1.08 and 3544.87 ± 1.08. Both lie inside the heavy scattered-light spans in s55 and s82: QLP and TESS-SPOC are flagged there, TARS has a gap, and the background reaches 10⁵–10⁶.
- **Observed e cos ω / e sin ω:** not measurable, because no B eclipse is seen. Instead, the B miss outside the gap gives a constraint (step 4).

### 4. Independence
- **Second pipelines:** TESS-SPOC and TARS reproduce both A eclipses. Mid-times agree within 0.2 min (s55) and 1.9 min (s82), and depths are 3.95–4.41%.
- **Difference image** (TESScut 15×15; `diffimg.py`, output `diff.txt`):
  - s55: the deficit is on the target pixel (4.3%). The deficit centroid is 1.9″ from the light centroid.
  - s82: target pixel 4.4%, offset 2.9″.
  - Depth by aperture: 4.3 / 4.2 / 4.1% (s55) and 4.4 / 4.2 / 3.9% (s82) for 1×1 / 3×3 / 5×5.
  - At the G 13.97 neighbour's pixel the dip is 0.3–0.4%.
- **Dilution:** to make the A eclipse, the G 13.97 star at 65.5″ would need a 4.2% × 10^(0.4×2.52) ≈ 43% eclipse, which the pixel data rule out. The G 16.08 star would need more than 100%. Every other source within 60″ is G 17 or fainter.
- **B null** (`bnull.py`, outputs `bnull.txt` and `bnull.png`; 6.5 h and 5 h boxes, local linear baseline, red-noise β, q0 SAP from QLP and TESS-SPOC):
  - A B eclipse of 0.20% or deeper is excluded at 3σ for B−A separations 0.400–0.562 and 0.628–0.799 (and 0.613–0.618).
  - No separation shows a dip above 3σ.
  - The uncovered range 0.562–0.628 corresponds to e cos ω ≈ 0.10–0.21 (from the model) and contains about 67% of Gaia's conditioned probability.
  - So the miss is predicted by where the data are missing; it is not in tension with the orbit.

### 5. Physics
- **Mass function:** f(M) = 0.00943 M☉. At i = 90°, m2 is 0.244, 0.259, 0.274 and 0.294 M☉ for M1 = 1.0, 1.1, 1.2 and 1.35. The separation a is 45.8–50.2 R☉ (0.21–0.23 AU).
- **Separation at each conjunction** (M1 1.2): 55 R☉ at A and 39 R☉ at B.
- **Who is in front:** at A (ν = 90° − ω) the M dwarf transits the primary. B is the occultation of the M dwarf.
- **Limb-darkened two-sphere fit of the A eclipses** (`afit.py`, `afit.txt`; TESS-SPOC, e and ω fixed at Gaia and varied by ±1σ):
  - k = 0.196, b_A = 0.45, i = 89.3°, residual rms 1255 ppm.
  - R1 = 1.42–1.60 R☉ for M1 = 1.05–1.35, which matches the TIC value of 1.44 R☉. That is the stellar density implied by the transit shape plus Gaia's orbit landing on the target star.
  - R2 ≈ 0.29 R☉, which is right for a 0.25–0.29 M☉ M dwarf, as the mass function requires.
- **Durations:** the central T14 at A is 9.9–10.8 h and the observed 9.6–10.0 h fits b ≈ 0.45. Predicted B: b_B = 0.33, T14 7.0–8.1 h, depth 0.18%, 0.33% or 0.55% for surface-brightness ratio J = 0.05, 0.09 or 0.15. J ≈ 0.09 is expected for an M3–M4 dwarf against a 5850 K primary.
- **Is B guaranteed?** Yes: b_B is smaller than b_A, so B must happen. It is simply not covered.
- Depth, duration, shape and the companion's light (about 0.3% of the total) all fit one geometry.

### 6. Verdict
**CONFIRMED** (eclipses A only). The deciding numbers:
- The two A eclipses are identical in three pipelines.
- The difference image puts the dip on the target pixel, and no neighbour can supply it.
- The 23-cycle period matches Gaia at −0.16σ, and the neighbouring cycle counts are off by about 30σ.
- The transit-derived R1 (1.42–1.6 R☉) and R2 (≈0.29 R☉) match the TIC primary and the mass-function companion.

**Weaknesses:**
- Only two eclipses, so the ephemeris has no internal check.
- B is unobserved: in both sectors its predicted window sits inside flagged scattered light.
- CTOIs are unchecked because ExoFOP was down.

**Next predicted eclipses (BTJD):**
- **A:** 4361.1645, 4393.3037, 4425.4429, 4457.5821, 4489.7213, each ±2.6–2.8 min.
- **B** (Gaia ±1σ; the bnull-allowed range is in brackets):
  - 4348.35 ± 1.08 [4347.09–4349.21]
  - 4380.49 [4379.23–4381.35]
  - 4412.63 [4411.37–4413.49]
  - 4444.77 [4443.51–4445.63]
  - 4476.90 [4475.64–4477.77]

**What would settle it further:** a third A eclipse to test the ephemeris, and any B coverage at about 0.3% precision over ±1.1 d. A detected B time would give e cos ω directly, and its duration would give e sin ω to compare with Gaia's 0.158 and −0.161. Retrying ExoFOP for CTOIs is also still open.
