# TIC 392794270: CONFIRMED

Full bounded physical review: **COMPLETE**. Physical classification is separate from catalogue recovery/novelty; historical screening was not an admission verdict.

1. **Raw events.** 7 free-center trapezoid measurements from quality-zero QLP SAP_FLUX in sectors [45, 46, 72]; 7 enter the reported ephemeris. Representative raw light curves and numerical windows show repeated eclipse morphology. Predictions guided the windows and are not measurements. Flagged or uncovered windows are not clean nulls.
2. **Timing and aliases.** Measured recurring-eclipse timing supported. Selected primary and unequal secondary morphology support the quoted orbital period; half/double hypotheses were checked. P=8.0693890282 +/- 0.0000305111 d; reference BTJD=2530.1503849. Epoch kind: Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. The formal error column is the local free-center model covariance; the input error adds a half-cadence floor. Singular/unidentifiable centers are excluded. Cycle/parity counts are in [../alias-audit.json](../../campaign/batch06/alias-audit.json). The epoch kind above states whether the fitted events are identified as deeper primary or selected eclipse by convention. The bounded half/double check does not prove all possible aliases absent.
3. **Attribution.** Fresh difference stack in sector 46 has 3 events; target coordinate [7.599025882750558, 7.57969604350226], deficit [7.501264762064753, 7.610329271099777]; offset 0.102 pixel. The image-model fractional residual 0.075 is not a localization uncertainty. Every capable Gaia neighbor in the retained 60-arcsec table was inspected: None under the approximate G-band brightness screen within 60 arcsec. The intrinsic loss proxy uses a pairwise G-band flux budget and cannot be directly compared with diluted pixel fractional loss. Close blends and passband/aperture response limit exclusion claims. Repeated sharp box eclipses are distinct from strong changing baseline variability. No secure secondary phase is assigned. The target-centered difference image and no capable Gaia neighbor support ownership.
4. **Alternative reduction.** Fresh TESScut background-subtracted target-centered 1x1/3x3/5x5 depths are 23.48/23.56/23.59 ppt; selected QLP fitted median 24.33 ppt. This reruns the historical extraction primitive using the fresh ephemeris and measured duration, with identity and source hashes checked. The alternative extraction and the QLP data for this sector share the same TESS photons; they test processing robustness and are not independent observations. Distinct sectors are distinct observing occasions on one instrument. Depth differences can reflect dilution, aperture and background response; intrinsic binary depth is not inferred.
5. **Gaia geometry/physical plausibility.** Exact DR3 source 3863614109736230656, orbital P=8.0698655652 d, e=0.09715. Closest edge-on conjunction offset=0.02801 d (0.00347 phase), full source-specific covariance linear timing allowance=0.97097 d. Mass function=0.011284 solar masses; adopted primary mass=0.9, minimum secondary mass=0.246. Rough central duration=7.27 h versus observed median=7.57 h. Radius and main-sequence companion assumptions make this a plausibility calculation, not a fitted geometry or calibrated significance veto. Shorter observed duration can reflect impact parameter and model assumptions. Orbit agreement does not establish ownership among unresolved sources.

**Secondary phase check:** No secure secondary identified amid strong non-eclipse variability; phase 0.5 tested visually, not a clean null. Weak secondary fits (especially314713331) describe inspected narrow dips and are not independent primary-eclipse evidence or calibrated detection significances. See [../secondary-phases.json](../../campaign/batch06/secondary-phases.json) and [../secondary-contact.png](../../campaign/batch06/secondary-contact.png).

**Deciding limit:** Repeated sharp box eclipses are distinct from strong changing baseline variability. No secure secondary phase is assigned. The target-centered difference image and no capable Gaia neighbor support ownership.

**Next check:** Optional resolved photometry and spectroscopy for precision physical parameters.

Catalogue recovery is recorded centrally in [../../shared-catalogues/coverage-matrix.csv](../../campaign/shared-catalogues/coverage-matrix.csv). A successful cone with no exact eclipsing target classification is distinct from a failed query; known recoveries must not count as new additions. No exhaustive literature priority claim is made.

| Sector | Search cycle | Measured midpoint BTJD | Formal center error d | Timing input error d | Depth ppt | Timing status |
|---|---:|---:|---:|---:|---:|---|
| 45 | 0 | 2530.1482583 | 0.005159 | 0.005159 | 23.90 | selected |
| 45 | 2 | 2546.2885931 | 0.00316943 | 0.00347257 | 25.73 | selected |
| 46 | 3 | 2554.3596239 | 0.00667629 | 0.00667629 | 27.22 | selected |
| 46 | 4 | 2562.4295151 | 0.00595019 | 0.00595019 | 23.34 | selected |
| 46 | 5 | 2570.4982179 | 0.00123878 | 0.00347255 | 24.33 | selected |
| 72 | 91 | 3264.4636348 | 0.00116102 | 0.00116102 | 26.70 | selected |
| 72 | 92 | 3272.5410419 | 0.00286001 | 0.00286001 | 23.35 | selected |

Evidence: [measurements.json](../../campaign/batch06/392794270/measurements.json), [raw-windows.csv](../../campaign/batch06/392794270/raw-windows.csv), [raw-events.png](../../campaign/batch06/392794270/raw-events.png), [fresh-pixels/diff_fresh.json](../../campaign/batch06/392794270/fresh-pixels/diff_fresh.json)/png, historical original receipts, [../download-receipts.json](../../campaign/batch06/download-receipts.json), [../identity-check.json](../../campaign/batch06/identity-check.json), [../alias-audit.json](../../campaign/batch06/alias-audit.json), [../gaia-geometry.json](../../campaign/batch06/gaia-geometry.json) and [../helper-audit.md](../../campaign/batch06/helper-audit.md). Original inputs and fresh outputs are covered by [../SHA256SUMS.json](../../campaign/batch06/SHA256SUMS.json) and [../source-hashes.json](../../campaign/batch06/source-hashes.json).


Stable review key: R595.

Deciding evidence and numeric artifacts:
- [fresh-pixels/diff_fresh.json](../../campaign/batch06/392794270/fresh-pixels/diff_fresh.json)
- [fresh-pixels/diff_fresh.png](../../campaign/batch06/392794270/fresh-pixels/diff_fresh.png)
- [fresh-pixels/gaia.json](../../campaign/batch06/392794270/fresh-pixels/gaia.json)
- [fresh-pixels/run.log](../../campaign/batch06/392794270/fresh-pixels/run.log)
- [historical/diff_s46.json](../../campaign/batch06/392794270/historical/diff_s46.json)
- [historical/diff_s46.png](../../campaign/batch06/392794270/historical/diff_s46.png)
- [historical/gaia.json](../../campaign/batch06/392794270/historical/gaia.json)
- [measurements.json](../../campaign/batch06/392794270/measurements.json)
- [phase-check.json](../../campaign/batch06/392794270/phase-check.json)
- [raw-events.png](../../campaign/batch06/392794270/raw-events.png)
- [raw-windows.csv](../../campaign/batch06/392794270/raw-windows.csv)

[Batch audits and scripts](../../campaign/batch06/INDEX.md). [Depth correction provenance](../../campaign/depth-audit/README.md).
