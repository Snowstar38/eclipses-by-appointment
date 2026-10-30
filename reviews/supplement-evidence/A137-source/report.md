# TIC 1260529 (TYC 6579-2222-1, Gaia DR3 5652319283872158336): per-object vet

Opus 5.5 subagent, wave 3, 2026-10-19. Resumed a dead session's folder. Every number below comes from a file in this folder,
either produced by the dead session's scripts (`vet-out.txt`, `bkgreg-out.txt`, `cats-out.txt`, `morecats-out.txt`, `mastlc-out.txt`)
or by this session (`indep-out.txt`, `tglc-out.txt`, `diff2-out.txt`, `sec-out.txt`, `sec2-out.txt`, `hbtest-out.txt`,
`geom-out.txt`, `physics-out.txt`, `conjepoch-out.txt`, `flagged-out.txt`). Downloads are in
`C:\Home\sky\data\qlp-sb-p20-60\pervet1260529\`.

## Verdict: CONFIRMED (an eclipsing SB1, grazing primary eclipse at Gaia conjunction A, with a shallow secondary)

The deciding numbers:
- **Timing locked to the RV orbit.** At the Gaia epoch (BTJD ~389), where Gaia's period error does not propagate, the TESS primary falls
  **−0.28 h (−0.29σ) from conjunction A** (predicted 389.6657 ± 0.0401 d, MC with corr_vec; ω–Tp corr 0.9994). At the TESS sectors the offset
  grows from +3.5 h to +11.7 h (all +1.7..+1.9σ). That drift is just the period difference: TESS P 10.992454(8) d vs Gaia 10.990961(780), +1.9σ.
- **On target.** The out-minus-in difference image, fitted with a free-position Gaussian in five TESS-SPOC TPF sectors, puts the source
  **1.0, 3.6, 2.5, 1.8 and 1.1″ from the target** (s8, 34, 35, 61, 62). If the Gaussian is pinned on the 9.4″ G 15.43 Gaia VARIABLE /
  VSX ROT neighbour instead, χ² is worse by 103, 136, 162, 278 and 164. That neighbour would need an impossible ~50% dip (10.85 ppt × 10^(0.4·4.17) = 0.51).
  QLP centroids during eclipse do not move: dX −0.02 ± 0.23, dY +0.02 ± 0.12 mpix. A 9.4″ source would shift them by ~5 mpix.
  SPOC DV gives a difference-image offset of 0.35 ± 2.54″. The batch diffimg (s34) reports peak_on_target.
- **Not a heartbeat.** On the same harmonic base, the trapezoid has χ² 757 (1500 bins). A Kumar heartbeat with Gaia's e/ω is worse by
  **+2959**; with e free within 3σ of Gaia, by +2953; even with e free up to 0.9 (best e 0.84, ruled out by the RV e = 0.034), by +100.
  The conjunction lies at ν = 75°, not near periastron.
- **Repeats in other pipelines.** SPOC PDCSAP gives 11.17 / 10.99 / 10.91 / 11.49 / 10.48 ppt (s8/34/35/61/62). SPOC SAP gives 9.85–10.15 ppt.
  TGLC s8 aperture gives 15.8 ppt; TGLC is deeper on both stars of this batch, and its psf_flux is all NaN for this star. QLP SAP gives 10.85 ± 0.12 ppt.
- **Prior detection (not a catalogue entry).** SPOC flagged it as a TCE in s61–62: multi-sector DV `s0056-s0069`, P 10.99301 ± 0.00055,
  epoch 2972.8802, depth 11224 ± 251 ppm, 3.85 h, b 0.97, Rp 36 R⊕. Its weak-secondary test found **0.63 ± 0.17 ppt at 5.663 d = phase 0.515**.
  ExoFOP lists no TOI or CTOI. There is no VSX/ASAS-SN entry at the target, no SB9, no WDS, nothing in Gaia vari_eclipsing_binary
  or vari_summary, and nothing in Prša+2022, IJspeert+2024 or Kostov+2025. SIMBAD has it as SB* only. A web search on the TYC and TIC names found nothing.

## 1. Archives
`cats.py --r 60` (APPOINTMENTS_DATA = $TEMP\hunt-sb1-scale): VSX has only the ROT star Gaia DR3 5652319180792945152 at 9″ (G 15.43). That is
a neighbour, not the target, and is excluded above. ASAS-SN: none. SIMBAD: TYC 6579-2222-1 [SB*]. `morecats.py`: SB9 none, WDS none,
J/AJ/160/111 none; ExoFOP has no TOIs, CTOIs, imaging, spectroscopy or companions. Gaia TAP (`gaia.json`) gives SB1 P 10.990961(780),
e 0.0342(107), ω 14.7(21.7)°, Tp −1.5258(6560), K1 40.59(50) km/s, 15 RV epochs, significance 81, RUWE 1.06, no vari rows.
TIC: Teff 5657 K, logg 3.76, R 2.19 R☉, M 1.0 (likely low for this subgiant), contratio 0.107.

## 2. Eclipse measurements (QLP SAP, QUALITY==0, untrimmed; `vet-out.txt`)
Global trapezoid: depth 10.96 ppt, T14 3.78 h, T12 1.51 h, flat bottom 0.76 h. The shape is nearly V, as expected for a grazing eclipse.
There are 8 primaries, all with S/N 23–37 and depths 10.3–11.5 ppt (constancy χ² 8.8/7). Odd and even depths are 10.98 ± 0.18 and 10.74 ± 0.16.
Background: the median in-minus-out is +1.0 ppt of target, and a fake eclipse would need +80 e⁻/s. Regressing on background implies at most 0.06 ppt.
None of the 8 events is within 0.5 d of a listed sector-wide systematic. Two windows contain a bit-32 cadence, and their depths are normal.
The control phases are all consistent with zero, with no S/N > 3 in any of them.
Blind census: 11 dips at S/N ≥ 4; 8 are the eclipses, and none of the off-ephemeris dips is ≥ half the eclipse depth.
Events in flagged data only:
- s099, E137 (all cadences carry QLP bit 29): **11.49 ± 0.60 ppt at 4072.1205 ± 0.0023**. The ephemeris predicted 4072.1262 (O−C −8 ± 3 min), 2.9 yr after the last Q0 eclipse.
- s035 2269.36: 10.8 ± 4.5 ppt, too noisy to use.

## 3. Ephemeris, secondary, e cos ω / e sin ω
Primary: **P = 10.992454 ± 0.000008 d, T0 = 2566.15999 ± 0.00035 BTJD** (n 8, χ²/dof 5.0/6, O−C rms 1.1 min). Versus Gaia P: +1.9σ.
Secondary (`sec-out.txt`, `sec2-out.txt`; per-epoch local quadratic + trapezoid, inverse-variance stack):
- **0.40 ± 0.09 ppt at phase 0.5140 (± 0.0007 by profile; ± 0.0015 across duration scalings)**, S/N 4.5.
- Control phases have |S/N| ≤ 2.7. Every sector group is positive: s8 0.65 ± 0.21, s34/35 0.35 ± 0.18, s61/62 0.40 ± 0.14, s99 0.23 ± 0.22.
- A shorter duration (T14 × 0.6) is mildly preferred: S/N 5.0, 0.55 ± 0.11 ppt.
- SPOC DV independently places its weak secondary at phase 0.515.
- **e cos ω ≈ (π/2)(Δφ − 0.5) = +0.022 ± 0.002**, against Gaia's +0.031 ± 0.010 (0.9σ). Gaia predicts Δφ = 0.5196 ± 0.0066; this is 0.8σ from the measurement.
- e sin ω cannot be measured from the durations at this S/N. See §5 for what the depth ratio implies.

## 4. Independence
- Other pipelines: TESS-SPOC (PDCSAP and SAP) for all five SPOC sectors, and TGLC s8 (`indep-out.txt`, `tglc-out.txt`).
- Difference images: the free-position fit in five TPF sectors (`diff2-out.txt`). The older pinned-PSF script (`tpfdiff.py`) is
  unreliable for single-event sectors (zero scatter); for s61 it gives target χ² 24903 vs 66361 for the 9.4″ star.
- Neighbours (Gaia G < 17 within 90″) and the dip each would need: 13.28 at 70″ → 69 ppt; 14.34 at 55″ → 184 ppt;
  14.64 at 34″ → 243 ppt; 15.36 at 18.8″ → 0.47; 15.43 at 9.4″ (VARIABLE/ROT) → 0.51.
  Every one of them is 1–3.6″-incompatible with the difference-image source at ≥ 7″ separation.

## 5. Physics
- Mass function: f(M) = 0.0761 M☉. With i ≈ 84–86° and M1 1.0–1.4, m2 = 0.57–0.70 M☉. The companion is an early-M or late-K
  dwarf (R2 ≈ 0.5–0.6 R☉, T2 ≈ 3700–4000 K); a = 24–27 R☉, a/R1 ≈ 11–12.
- The central-chord duration would be 8.6–9.4 h; the observed 3.8 h together with the near-V shape requires a **grazing** chord (b ≈ 1.06–1.11 R1).
  SPOC DV independently fits b 0.97, k 0.15.
- Conjunction A has the RV primary behind, so the companion transits the primary: the deep eclipse is the primary eclipse. That is what is observed.
- **Tension, worth stating once.** For e sin ω ≈ 0 a grazing geometry gives a secondary of ~2.5–3.2 ppt for this companion, not 0.40
  (`geom.py`: limb-darkened two-sphere orbit model). Matching 11 ppt / 3.8–4.2 h primary **and** a 0.4–0.7 ppt, ~2.7 h secondary needs
  the secondary chord to be more grazing, which means **e sin ω ≈ +0.04** (e ≈ 0.046, ω ≈ 60°). Gaia's e sin ω is +0.008 ± 0.013,
  so the tension is ~2.5σ (and e, ω are within ~1–2σ).
- The alternative, a much cooler companion (J = 0.037 → T2 ≈ 2800 K), contradicts the mass function. The tension does not bear on whether
  this is an eclipse (that is settled by timing, centroids and shape). It does bear on the companion's parameters, and an RV e sin ω or a
  higher-S/N secondary would settle it.

## Row fixes for the paper table
| field | ledger | fix |
|---|---|---|
| P (d) | 10.99253 | **10.992454 ± 0.000008** |
| T0 (BTJD) | — | **2566.15999 ± 0.00035** |
| depth (ppt) | 9.3 | **10.85 ± 0.12** (QLP SAP trapezoid; SPOC PDCSAP 10.5–11.5) |
| T14 (h) | — | **3.78** (near-V, grazing) |
| n events | 8 | 8 Q0 (+1 flagged s099 at the predicted time) |
| dphi | +0.013 | +0.013 to +0.044 across the sectors (Gaia P drift, +1.9σ); **−0.001 (−0.29σ) at the Gaia epoch** |
| secondary | — | **0.40 ± 0.09 ppt at phase 0.514** (S/N 4.5; SPOC DV 0.63 ± 0.17 at 0.515) |
| prior art | — | SPOC TCE (DV s0056–s0069, s61–62 data); not a TOI; not in any EB catalogue |

## Next predicted eclipses (BTJD)
- Primary: **4401.8998, 4412.8923, 4423.8847** (± 2 min). Folding in the s099 flagged event's −8 min O−C would shift these by a few minutes.
- Secondary (phase 0.514, ~0.4 ppt): **4407.5499, 4418.5424, 4429.5348** (± 24 min).

## Addendum 2026-10-21 (Fable, 03:30 session): the e sin ω tension re-priced (`esw.py` / `esw-out.txt`)
Two tests on the §5 tension, one negative and one positive:
- **It is not a covariance artefact.** The 2.5σ used Gaia's marginal e sin ω error; re-done against Gaia's full
  (P, e, ω, Tp) covariance, conditioned on the TESS e cos ω (+0.0220 ± 0.0012, 8× tighter than Gaia's), the answer
  does not move: corr(e cos ω, e sin ω) in the Gaia solution is −0.015, conditional e sin ω +0.0090 ± 0.0126, and the
  geometry-required +0.044 ± 0.004 sits **+2.65σ** away either way. Joint 2D Mahalanobis of (e cos ω_TESS,
  e sin ω_needed) under Gaia: 2.76 (p = 0.022).
- **The secondary's duration independently supports the grazing reading.** The depth-matching geometry
  (e sin ω ≈ +0.044) predicts the secondary lasts ~0.71× the primary's T14; Gaia's e sin ω (+0.008) predicts ~1.0×.
  A fixed-template scan (fT 0.4–1.3, phase profiled) peaks at fT 0.5 (S/N 5.02) and prices the two predictions at
  **Δ(S/N)² = +3.4 in favour of the short secondary** — depth and duration agree with each other and disagree with Gaia.
- Net: the eclipse geometry is self-consistent at **e ≈ 0.049, ω ≈ 63°** (vs Gaia e 0.034 ± 0.011, ω 15 ± 22°: 1.4σ
  and 2.2σ separately, p = 0.022 jointly). The economical reading is that Gaia's ω is the off quantity, not the
  secondary. Context: wave 4's 288160281 and wave 3's 260789413 / 430987029 all show the opposite-direction version
  (Gaia e biased high for near-circular orbits, the Lucy–Sweeney direction); 1260529 is so far the only case where
  the eclipses want *more* eccentricity than Gaia — which is what makes it worth the DR4 epoch-RV check rather than
  a bias explanation.

## What would settle it further
- An RV e sin ω (or a higher-S/N secondary with a measured duration) to resolve the depth-ratio tension.
- A reprocessing of s099 that unflags the cadences (or a second pipeline for s099), to confirm the 2.9-year forward prediction.
- A spectrum to fix M1 and R1.
