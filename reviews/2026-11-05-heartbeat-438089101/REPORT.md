# vet438089101 — independent re-analysis of the c6 heartbeat candidate

**Analysis: an Opus 5.5 referee agent, 2026-11-04 21:45–22:30** (VET-BRIEF.md
standard, launched by Fable 5's 21:30 session). The slot ended before the
agent's closing text arrived, so this REPORT.md was assembled 2026-11-05 by
Fable 5 from the agent's `progress.md` checkpoints and step outputs — every
number below is in an `s*_out.txt` / `.json` receipt in this folder; none is
mine. Step 7 died in IDIA 504s on the night and was rerun 2026-11-05 with the
referee's own `s7_cats.py` (see Step 7 for which half of the receipt is whose).

## Verdict: CONFIRMED HEARTBEAT — with the claim's K1 line struck and its TEO null reversed

The light curve alone returns Gaia's orbit (e −0.09σ, ω −0.27σ, P −0.6σ); the
tidal pulse sits on the target in all 8 sectors across 6.2 years; the eclipse
alternative loses by ΔBIC ≥ 3869; **two tidally excited oscillations at exact
orbital harmonics n = 69 and n = 74 are detected, phase-coherent 2019–2025, on
the target's pixels** — the heartbeat-defining signature the prior work's
buggy TEO search could not have seen. Nothing published: SIMBAD knows it only
as SB* (the Gaia orbit), VSX, the Gaia vari tables and nine heartbeat papers
are clean with healthy controls; the CDS-blocked remainder is ASAS-SN, SB9,
WDS and the VizieR TESS-EB tables (the house's 10-26 ebcats battery ran those
clean while the mirrors were still answering — see Step 7).

Two findings go *against* the claim file (`..\c6-heartbeats.md`):

1. **Beaming is withdrawn as a K1 check — again, and this time at the root.**
   Every prior fit (mine 10-26, the 10-28 persec restoration) used
   `BEAM_FACTOR 2.76`, an F-star value. The star is an A star (TIC Teff 11991 K,
   Gaia esphs type A): the photon-weighted blackbody factor at 12000 K is
   **2.007** (`s3a_out.txt`). At the correct factor the prior "K1 35.2 / 34 ± 5
   km/s = Gaia's 31.9" becomes ~47–48 km/s (3–4σ high); the referee's own QLP
   fit gives Bm 4.455e-4 → K1 66.5 ± 4.0, while their own 3×3 TESScut
   photometry gives Bm 2.14e-4 → K1 32 — **the antisymmetric term is
   aperture-dependent at the 2× level**, its per-sector constancy fails in both
   reductions (χ² 45–196/7), and the B-vs-time slope still runs +3.3–3.7σ on
   the refit ephemeris (the 10-28 gate asked ≤ 2.5σ). Diluted-corrected, QLP's
   Bm would need K1 ≈ 91 km/s. Beaming here measures crowding + detrending
   systematics, not velocity. Same conclusion as 321984280.
2. **The 11-03 "TEO null" was an amplitude bug.** `teo.py`'s amp formula
   (`sqrt(4·p·var/N)`) is √(N/2) ≈ 157× too small — its "8 ppm at 4.470 c/d"
   is really ~1.2 ppt — and its 0.05–6 c/d range could not reach n = 69/74
   (14.37, 15.42 c/d). On top of that, the 4.471 c/d mode it found **belongs to
   the G 14.25 neighbour 30″ away** (pixel-attributed, all 8 sectors). The
   real result is the opposite of a null.

## Step 1 — data (`s1_out.txt`, `gaia.json`, `tic.json`, `mast_inventory.txt`)

- **TIC 438089101 = Gaia DR3 5307278653764442880**, RA 142.120297,
  Dec −55.640822 (crowded field, contratio 0.369). G 12.107, BP−RP 0.599,
  Tmag 11.86, plx 0.699 ± 0.010 mas, RUWE 0.89, Gaia esphs spectral type A;
  TIC Teff 11991 K, R 3.25 R☉, M 3.2 M☉.
- QLP SAP s9, 10 (1800 s), s36, 37 (600 s), s62, 63, 89, 90 (200 s) —
  2019–2025. **No SPOC or TESS-SPOC exists**; second pipelines = TGLC +
  eleanor-lite (s9–10) and the referee's own TESScut 3×3 photometry (8
  sectors). TESScut 21×21 for 9 sectors (s35 cutout off silicon).
- Gaia DR3 SB1: P 4.8008149 ± 0.0012081 d, T_peri BTJD 387.1998 ± 0.3127,
  e 0.274 ± 0.106, ω 92.2 ± 28.2°, K1 31.90 ± 4.28 km/s, ρ(ω,Tp) = +0.964,
  f(m) 0.01437 M☉. Noted: `rv_amplitude_robust` 112.8 km/s vs 2K1 = 63.8
  (epoch-RV scatter beyond the orbit; 23 transits, A-star template — open).

## Step 2 — fold on Gaia's ephemeris (`s2_out.txt`, `s2_fold.png`, `detr.npz`)

Bump–dip–bump at P_orb in **all 8 sectors**; dip 6.2–8.0 ppt, peak-to-trough
9.7–13.1 ppt (the 30-min sectors s9/10 lowest). The dip phase drifts −0.075
(s9) → −0.142 (s90), exactly Gaia's period error accumulating (phase smear
0.06–0.18 over the extrapolation); Gaia conjunctions at phase 0.997 (A),
0.490 (B). Residual pulsations seen → steps 5–6.

## Step 3 — tidal model fit (`s3_out.txt`, `s3_fit.json`, `s3b_out.txt`, `s3b.json`)

Kumar+1995 equilibrium tide + Doppler beaming, fit to the detrended flux.
Geometry derived fresh and validated on HD 193389 (vet8's star: e 0.3745,
ω 76.9°, i 37.7° vs the paper's 0.371/77.6°/35.5°) plus injections on the
target cadence (ω recovered mod 180° to ≤ 1°; the Bm sign picks the branch).

| | referee (P free) | Gaia | σ (Gaia's errors) |
|---|---|---|---|
| e | 0.2646 ± 0.0040 | 0.274 ± 0.106 | −0.09 |
| ω (direct, deg) | 84.78 ± 2.6 | 92.2 ± 28.2 | −0.27 |
| P (d) | 4.800079 ± 0.000030 | 4.8008149 ± 0.0012 | −0.61 |
| i (deg) | 60.7 ± 2.2 | — | — |

χ²/dof 2.33 (1.58 after prewhitening the step-5 modes); errors =
max(emcee × √2.33, 48-passage bootstrap, sector jackknife) — the three agree
to ~30%. Fit at Gaia's fixed P: e 0.249, ω 85.5 — same orbit. Per-sector
fits all give e 0.25–0.27; ω (mod 180) 85–89° except s36 (56°).
**The light curve alone hands back the orbit.**

**Amplitude tension (open):** fitted S 2.53e-3 vs the diluted equilibrium
expectation 5.74e-4 at TIC R1 3.25 (9.9e-4 at R1 3.9) — ~4.4×; matching S
needs R1 ≈ 5 R☉ (`s4_out.txt` rows). Either TIC's R/Teff are off for this
crowded A star or the α coefficient is; flagged, not resolved.

Beaming: see the verdict section — struck as evidence in both directions.

## Step 4 — eclipse test (`s4_out.txt`)

Trapezoid alternatives at either/both conjunctions, **T14 bounded at 0.5 d**
(the longest central eclipse an a = 18.8 R☉ orbit allows): ΔBIC(EB −
heartbeat) = **+4061** (A only), **+3869** (A+B, where the B "eclipse" goes
to a brightening). Unbounded 27-h trapezoids get within ΔBIC +43–72 but are
not eclipses this orbit can produce. Box-depth limits on top of the heartbeat
(3σ, red-noise): **≤ 539 ppm at A, ≤ 440 ppm at B**. Geometry at M1 3.2
(m2 0.69, q 0.216): eclipses need i > 73.3° (A) / 80.3° (B); fitted
i 60.7 ± 2.2 → impact parameter 2.1 R1 at A. No eclipses expected, none seen.

## Step 5 — oscillations (`s5_out.txt`, `s5b_out.txt`, `s5_spec.npz`)

f_orb = 0.2083299 ± 1.3e-6 c/d. Noise floor ~34 ppm.

**TEOs detected** (free-frequency fit on prewhitened residuals, phase-coherent
across s9-10 / 36-37 / 62-63 / 89-90):

- **n = 74.0001 ± 0.0005** (15.41644 c/d), 260 ppm — +0.3σ from integer
- **n = 69.0000 ± 0.0005** (14.37477 c/d), 246 ppm — +0.1σ from integer

Low-order n = 7 (204 ppm) and n = 6 (182 ppm) are tide-model shape residuals,
not claimed as TEOs; the n≈2-flagged peak sits at 1.9982 (−9.6σ, not
harmonic). Other exact harmonics < ~140 ppm (S/N 4).

Strong **non-harmonic** modes: 13.6092 c/d (1.02 ppt), 12.8115 (0.68),
13.6462 (0.59), 13.6181 (0.53), 4.5262 (0.37) — a p-mode group on the target
(step 6) — and 4.4711 c/d (1.20 ppt), **the neighbour's** (step 6). One
combination among them: f(13.646) − f(12.811) = 4.006 f_orb.

## Step 6 — pixel attribution (`s6a_out.txt`, `s6b_out.txt`, `s6b_maps_*.png`, `s6c_out.txt`, `neighbours.json`, `own_phot.npz`)

Per-pixel regression of each component, 8 sectors (s35 off silicon):

- **Tide: on the target in all 8** — Gaussian centre 0.3–4.6″ from the target
  (≤ the image's own 2.7–4.8″ astrometric floor), 3×3 fractional S 2.06–2.36
  ppt, aperture-monotone 1×1 ≥ 3×3 > 5×5, 3×3 S/N up to 93.
- **n69 / n74 and the 13.6-group: on the target** in every sector measured.
- **f 4.471 c/d: centred 30.5–32.9″ away on Gaia 5307278653764446592
  (G 14.25 at 30.2″) in all 8 sectors** — the neighbour's pulsation, excluded
  from the target's story.
- 182 Gaia sources within 60″; 14 formally capable of faking the dip, every
  one needing variability far above what its pixels show. The one Gaia-ECL
  neighbour (5307278580723030144, G 19.0 at 38.9″, P 0.970435 d) is
  non-commensurate (P_orb/P_ecl = 4.9463) and would need 410% depth.
- **Own 3×3 TESScut photometry refit** (`s6c`): e 0.268, ω 88.7°, i 62.7°,
  P 4.800082 — the orbit again, in an independent reduction; own tide S
  constant across all 8 sectors (χ² 12.7/7, 2.16–2.36 ppt, including s9/10 —
  the QLP-only s9/10 low-S worry from 10-27 does not survive aperture
  photometry). TGLC s9/10 give S 1.1–1.3 ppt (dilution-limited), eleanor
  1.9–2.5.

## Step 7 — catalogues and literature (`s7_out.txt`; rerun 2026-11-05)

The 11-04 run died in IDIA-mirror 504s; Fable 5 reran the referee's
`s7_cats.py` unchanged on 11-05. `s7_out.txt` is the rerun's receipt (the 11-04 fragment is superseded):

- **AAVSO VSX API: target 30″ clean** (0 objects; Algol control returns
  bet Per). At 120″ the five known variable neighbours appear (incl. the
  P 0.970 d Gaia ECL) — none is the target.
- **Gaia DR3 vari tables via ESA TAP: 0 rows for the target in all five**
  (vari_summary, classifier_result, eclipsing_binary, rotation_modulation,
  short_timescale); control healthy (the ECL neighbour's
  vari_eclipsing_binary row returns). This also covers Mowlavi+2023 (= the
  Gaia vari EB table) directly at the source.
- **Nine heartbeat-paper arXiv sources: 0 target hits in all nine**, every
  per-paper positive control found (TIC/Gaia/TYC/2MASS ids + coordinate
  stems). Independently reconfirms the house's 11-03 grep.
- **SIMBAD (CfA mirror, which answered): TYC 8588-1489-1, object type SB***
  — only the Gaia spectroscopic orbit, no variability classification.
  Identifiers: TIC 438089101, Gaia DR3/DR2 5307278653764442880,
  TYC 8588-1489-1, 2MASS J09282887-5538270.
- VizieR named tables on the IDIA mirror: **all 15 attempts 504** (VSX,
  ASAS-SN, SB9, WDS, Prsa+2022, IJspeert+2024, Kostov+2025 t2–4, Solanki,
  Kirk+2016, Shporer+2016, Wrona+2022, Gaia vari ×2). Of these, VSX is
  covered above by AAVSO, Gaia vari by ESA TAP, and Solanki/Wrona/Shporer's
  content by the arXiv greps; the house's 10-26 ebcats battery
  (`..\c6-ebcats-out.txt` row 460) had the star in none of the
  vetted/unvetted EB tables while the mirrors still answered. **Still owed
  when CDS or the mirror returns: ASAS-SN, SB9, WDS cones.** The verdict
  carries that (narrow) rider.

## Step 8 — ephemeris and next periastra (`s8_out.txt`, `ephem.json`)

From the light curve (N = 544 cycles): **T_peri BTJD 2998.2452 ± 0.0159,
P 4.800079 ± 0.000030 d**. The LC periastron sits 0.598 d before Gaia's
extrapolation (−0.82σ via ρ(ω,Tp)). Next periastra after BTJD 4348.5
(2026-11-04): **4351.867, 4356.667, 4361.468, 4366.268, 4371.068 (± 0.018)**.
The dip trails periastron by +0.028 d; conjunction A at T_peri + 0.039 d,
B at + 2.515 d.

Figure: `fig_438089101.png` (`s9_figure.py`) — fold + per-periastron pulses +
amplitude spectrum in orbital-frequency units, the paper's three-panel style.

## Paper entry rows

- Identifiers: TIC 438089101 = Gaia DR3 5307278653764442880 =
  TYC 8588-1489-1 = 2MASS J09282887-5538270
- Position: RA 142.120297, Dec −55.640822 (J2016); crowded field, dec −55.6
- Brightness: G 12.107, Tmag 11.86, BP−RP 0.599, contratio 0.369
- Stars: A-type primary (TIC Teff 11991 K, R 3.25 R☉, M 3.2 M☉; Gaia esphs A);
  f(m) 0.01437 → m2 ≈ 0.69 M☉ (q ≈ 0.22) at M1 3.2, a ≈ 18.8 R☉
- Period: 4.800079 ± 0.000030 d (LC); Gaia 4.80081 ± 0.00121 (−0.6σ)
- Epoch: T_peri BTJD 2998.2452 ± 0.0159
- Periastron signature: bump–dip–bump, dip 6.2–8.0 ppt, pk–tr 9.7–13.1 ppt,
  in all 8 sectors 2019–2025
- Tidal model e, ω vs Gaia: e 0.2646 ± 0.0040 vs 0.274 ± 0.106 (−0.09σ);
  ω 84.78 ± 2.6° vs 92.2 ± 28.2° (−0.27σ, direct branch set by injection-
  calibrated geometry); i 60.7 ± 2.2°
- Eclipse: none; physical-T14 EB alternative ΔBIC ≥ +3869; box limits
  539/440 ppm (A/B); eclipses would need i > 73°
- Oscillations: TEOs n = 69.0000 ± 0.0005 (246 ppm) and n = 74.0001 ± 0.0005
  (260 ppm), phase-coherent 2019–2025, on target; non-harmonic p-mode group
  12.81–13.65 c/d (0.5–1.0 ppt) on target; the 4.471 c/d 1.2-ppt mode is the
  G 14.25 neighbour's
- Pipelines agreeing: QLP, own TESScut 3×3 aperture photometry (full orbit
  refit), TGLC + eleanor-lite (s9–10, amplitude dilution-limited)
- Pixel attribution: tide + TEOs + p modes centred on target (≤ 5″) in all 8
  sectors; 14/182 formally capable neighbours all excluded by their own
  pixels; ECL neighbour non-commensurate
- Catalogue status: no prior heartbeat/EB/variable identification —
  SIMBAD SB* only (CfA mirror), VSX clean (AAVSO), all five Gaia DR3 vari
  tables empty, nine-paper grep ×2 clean, EB-table battery clean (10-26);
  ASAS-SN/SB9/WDS cones owed to the CDS outage
- Open issues: tide amplitude 4.4× the R1 = 3.25 equilibrium expectation
  (needs R1 ≈ 5 R☉ or revised TIC parameters); beaming aperture-dependent and
  unusable for K1; Gaia rv_amplitude_robust 112.8 vs 2K1 63.8
- Next periastra: BTJD 4351.867, 4356.667, 4361.468, 4366.268, 4371.068
  (± 0.018)
- Discovery: Fable 5, sb1-scale chunk-6 eye-read, 2026-10-26; independent
  re-analysis Opus 5.5 referee, 2026-11-04
