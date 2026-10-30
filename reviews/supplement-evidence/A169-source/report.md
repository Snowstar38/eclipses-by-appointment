# TIC 284533163 (TYC 4020-206-1, F star, Teff 6431 TIC / 7077 Gaia, R ≈ 2.2–2.5 Rsun): per-object vet

**Verdict: CONFIRMED.** A δ Scuti / γ Dor hybrid F star is eclipsed every 2.349378 d by a ≈0.21 Msun M dwarf. The batch depth scatter (relMAD 0.39) is about 80% the star's own pulsation and about 20% a QLP sector-17 dilution problem. Once both are handled, the eclipse depth is constant.

Wave 4, 2026-10-20/21. Resumed from a killed session; receipts checked against fresh runs. (Saved by the parent session; the file-write tool refused REPORT.md for the subagent.)

## 1. Archives
- `cats.py --r 60`: VSX shows only a ROT star (G 16.37) at 49″. ASAS-SN none. SIMBAD [SB*] with one reference (Gaia DR3 multiplicity).
- Gaia NSS SB1: P 2.349632 ± 0.000163, e 0.175 ± 0.094, ω 326 ± 19°, K1 25.9 ± 2.1 km/s. vari tables empty.
- Not in any EB table (batch c4-ebcats and own VizieR cones: SB9, WDS, GCVS, Prša, IJspeert, Gaia vEB, Kostov).
- J/A+A/689/A177 returns a wide comoving-pair row (G 19.1 at 184″), which is irrelevant.
- ExoFOP: no TOI or CTOI. A web search found nothing. DTARPS and DIAmante don't cover this northern field (Dec +63°).
- MARVELS and DIAmante: none.

## 2. Chasing the depth scatter (the special instruction: relMAD 0.39)
**The star pulsates.** A Lomb-Scargle periodogram of the out-of-eclipse light (puls.py) shows coherent modes in every sector from 2019 to 2024:

| Frequency (c/d) | Semi-amplitude (ppt) |
|---|---|
| 11.759 | 10.4 |
| 11.995 | 8.3 |
| 11.25 | 3.7 |
| 12.85 | 1.3 |
| 1.33 | 4.2 |
| 1.43 | 3.4 |

The ~2 h main modes beat across a 5 h eclipse. That is why the batch saw an out-of-eclipse scatter of about 10 ppt per event and a relMAD of 0.39.

**After removing 20 sinusoids per sector** (clean.py):

| Sample | relMAD |
|---|---|
| All 50 events | 0.124 (raw SAP, same estimator: 0.269) |
| Excluding s017 | 0.070 |
| s058 onward | 0.054 |

- Event-to-event rms is 1.45 ppt, the same as the same estimator at control phases (1.24–1.72 ppt). The remaining scatter is noise.
- Leftover pulsation imprint on the depths is ≤ 1 ppt.

**QLP s017 is an instrumental outlier.** Every variability amplitude in QLP s017 is ×0.63 of the other sectors (11.759 c/d mode 6.5 vs 10.4 ppt; 1.33 c/d mode 2.8 vs 4.2 ppt), and its eclipse depth is ×0.65 (10.8 vs 16.4 ppt).
- The depth-to-pulsation ratio is the same in every product: 1.66 in QLP s17, against 1.51–1.67 elsewhere. So something dilutes all of the star's light uniformly.
- The cleaned residual in s017 is 3× noisier (5.6 vs 1.6–1.8 ppt in s018/s024 at the same cadence).
- QLP s017 has higher background (SAP_BKG 193 vs 109 e⁻/s in s018/s024), and 420 of its 1130 cadences are flagged (bit 4096 ×294, 6144 ×126).
- **TESS-SPOC s017 looks normal**: PDCSAP depth 17.6 ± 1.0 ppt, pulsation 10.85 ppt, rms 1.5 ppt (spoc-out.txt). The problem is QLP s017 only.

**Background:** a per-event regression of flux against SAP_BKG gives a median possible fake dip of 0.13 ppt (max 1.9), uncorrelated with depth (r = +0.06).
**Other checks:** 2 events have bit-32 cadences; their depths (18.3 vs 16.3 ppt) show no systematic. No events at the sector-wide systematic times. Centroid shift +0.8 ± 0.2 mpix.

## 3. Eclipse measurements, ephemeris, Gaia
- Cleaned shape: **depth 16.34 ± 0.06 ppt (event-scatter error ≈ 0.2), T14 4.98 h, T12 0.75 h, flat 3.49 h**. A V shape is rejected (Δχ² +6142).
- Odd 16.35 vs even 16.33 ± 0.09 ppt.
- Depth by sector (cleaned QLP): s018 16.59, s024 16.57, s058 15.81, s078 16.33, s085 17.13 ppt.
- **P = 2.349378 ± 0.000002 d, T0 = 2995.69666 ± 0.00046 BTJD**. O−C rms 8.9 min, from pulsation leftovers.
- Gaia P is off by −1.58σ (0.00026 d). The eclipse sits at Gaia conjunction A within −0.17σ to −0.93σ; the offset grows across sectors because of Gaia's P (compare at the Gaia epoch).
- **Secondary eclipse at phase 0.4975–0.500, depth 1.15 ± 0.30–0.38 ppt** (event-scatter errors; deep.py, sec_robust.py):
  - positive in all 6 sectors, both parities, and both detrendings (orbital harmonics removed, or kept with a local quadratic baseline);
  - the strongest peak anywhere else in the phase scan reaches only 2.6σ.
- The secondary phase gives e cos ω ≈ 0.00 ± 0.005. Gaia predicted phase 0.587 ± 0.048 (e cos ω 0.136 ± 0.076), a 1.8σ difference. Gaia's e itself is only 1.9σ from zero, and a 2.35 d orbit is expected to be circular.
- e sin ω can't be measured: the secondary is too shallow to give a duration ratio.
- **Ellipsoidal variation:** a cos 2φ term of 3.2–4.5 ppt per sector (undiluted sectors) against 4.5 ppt predicted from K1. This independently ties the RV companion to the eclipse period.

## 4. Independence
- TESS-SPOC (crowding factors 0.84–0.89): PDCSAP depth 17.6 / 18.3 / 16.1 ppt and SAP 16.2 / 14.8 / 14.6 ppt in s17/18/24.
- Difference images from the TESS-SPOC s17/18/24 pixel files: **the target wins every time** (χ² 433 / 669 / 381 against the next star's 1252 / 1039 / 728); the target's implied dip is 20.4 / 15.7 / 15.3 ppt. The batch QLP difference image also put the deficit on target.
- Neighbours: G 14.72 at 21″ would need about a 33% eclipse and fits worse. G 16.26 at 20″ would need more than 100%. G 13.6–14.7 stars at 53–83″ would need 12–33% and are rejected by the fits.

## 5. Physics (TIC M1 1.3, R1 2.50)
- Mass function f(m) = 0.00404 Msun, so **m2 = 0.21 Msun** (0.19–0.23). a = 8.5 Rsun.
- From the duration: b ≈ 0.52, i ≈ 81°, a/R1 3.93 (so R1 ≈ 2.2 Rsun).
- k = 0.128, so R2 ≈ 0.28–0.32 Rsun: a mildly inflated or irradiated M dwarf, or the b–limb-darkening degeneracy.
- Expected occultation: 0.9–1.5 ppt (thermal plus 0.42 ppt reflection) against 1.15 measured. Expected ellipsoidal 4.5 ppt against 3.2–4.5 measured.
- The companion is in front at conjunction A. Everything fits one geometry.

## 6. Verdict and predictions
**CONFIRMED.** The deciding numbers:
- Cleaned depth is constant (relMAD 0.07 excluding s017, 0.054 in s058+), with event scatter at the noise floor.
- s017 is explained by a uniform ×0.63 QLP dilution, confirmed by the clean SPOC s017 light curve.
- The difference image is on target in 3 sectors.
- The secondary (1.15 ppt at phase 0.50) and the ellipsoidal amplitude both match the physics of a ≈0.21 Msun companion.
- P agrees with Gaia at −1.6σ, and the eclipse sits at conjunction A.

Not catalogued anywhere. The pulsating primary is a bonus target (δ Sct in an eclipsing binary).

Next eclipses (BTJD):
- Primary (±2 min): 4337.1915, 4339.5409, 4341.8903, 4344.2396
- Secondary (phase 0.499 ± 0.003, ±10 min): 4338.363, 4340.713, 4343.062, 4345.412

What would settle it further: RVs to check whether e = 0, and a combined eclipse-plus-pulsation model to sharpen the depth and b.
