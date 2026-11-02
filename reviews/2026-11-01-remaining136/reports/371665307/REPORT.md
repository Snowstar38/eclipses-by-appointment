# TIC 371665307: PROBABLE

Full bounded physical review: **COMPLETE**. Physical classification is separate from catalogue recovery/novelty; historical screening was not an admission verdict.

1. **Raw events.** 24 free-center trapezoid measurements from quality-zero QLP SAP_FLUX in sectors [16, 57, 84]; 10 enter the reported ephemeris. Representative raw light curves and numerical windows show repeated eclipse morphology. Predictions guided the windows and are not measurements. Flagged or uncovered windows are not clean nulls.
2. **Timing and aliases.** Candidate orbital timing; factor-two ambiguity retained. P=4.9908584340 +/- 0.0000131023 d; reference BTJD=1740.8463664. Epoch kind: Even-parity eclipse in candidate 4.99087-d orbit; deeper rank unestablished; half-period ambiguity retained. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. The formal error column is the local free-center model covariance; the input error adds a half-cadence floor. Singular/unidentifiable centers are excluded. Cycle/parity counts are in [../alias-audit.json](../../campaign/batch01/alias-audit.json). Selected eclipse means the measured recurrence, with no assumption that it is the deeper primary. The bounded half/double check does not prove all possible aliases absent. 
3. **Attribution.** Fresh difference stack in sector 57 has 5 events; target coordinate [7.311130466648379, 7.956803856146049], deficit [7.206752205666073, 8.051402306721076]; offset 0.141 pixel. The image-model fractional residual 0.630 is not a localization uncertainty. Every capable Gaia neighbor in the retained 60-arcsec table was inspected: Gaia 2007172155994105856: 12.99 arcsec, G=16.117, intrinsic required loss proxy=0.312; Gaia 2007172155994111872: 16.56 arcsec, G=16.343, intrinsic required loss proxy=0.382; Gaia 2007172911908346368: 20.49 arcsec, G=16.891, intrinsic required loss proxy=0.627; Gaia 2007172155994111232: 22.14 arcsec, G=15.053, intrinsic required loss proxy=0.123; Gaia 2007172155994105344: 33.25 arcsec, G=16.851, intrinsic required loss proxy=0.605; Gaia 2007172911908339328: 37.35 arcsec, G=16.597, intrinsic required loss proxy=0.480; Gaia 2007172052914892544: 37.89 arcsec, G=16.319, intrinsic required loss proxy=0.374; Gaia 2007172808829127552: 39.57 arcsec, G=14.885, intrinsic required loss proxy=0.107; Gaia 2007172190353853824: 44.61 arcsec, G=15.399, intrinsic required loss proxy=0.166; Gaia 2007172190353853952: 46.45 arcsec, G=16.691, intrinsic required loss proxy=0.523; Gaia 2007172190353846784: 47.65 arcsec, G=17.019, intrinsic required loss proxy=0.704; Gaia 2007172048609299072: 47.73 arcsec, G=16.853, intrinsic required loss proxy=0.606; Gaia 2007172190353849088: 49.31 arcsec, G=14.828, intrinsic required loss proxy=0.102; Gaia 2007172946262005248: 52.00 arcsec, G=17.011, intrinsic required loss proxy=0.699; Gaia 2007172121634381952: 53.03 arcsec, G=15.878, intrinsic required loss proxy=0.252; Gaia 2007172941962552320: 53.93 arcsec, G=16.705, intrinsic required loss proxy=0.530; Gaia 2007172121634391552: 54.66 arcsec, G=15.969, intrinsic required loss proxy=0.273; Gaia 2007172087274650752: 57.52 arcsec, G=16.163, intrinsic required loss proxy=0.325; Gaia 2007172121634386048: 58.96 arcsec, G=15.966, intrinsic required loss proxy=0.273; Gaia 2007171984195429760: 59.03 arcsec, G=16.782, intrinsic required loss proxy=0.568. The intrinsic loss proxy uses a pairwise G-band flux budget and cannot be directly compared with diluted pixel fractional loss. Close blends and passband/aperture response limit exclusion claims. Repeated 2.49543-day dips are real. Depth parity is not decisive; the quoted 4.99086-day candidate orbital ephemeris uses even half-period parity only and retains a factor-two ambiguity. The shallow crowded deficit has twenty currently flux-capable neighbors and does not uniquely establish target ownership.
4. **Alternative reduction.** Fresh TESScut background-subtracted target-centered 1x1/3x3/5x5 depths are 7.82/7.46/5.81 ppt; selected QLP fitted median 9.42 ppt. This reruns the historical extraction primitive using the fresh ephemeris and measured duration, with identity and source hashes checked. The alternative extraction and the QLP data for this sector share the same TESS photons; they test processing robustness and are not independent observations. Distinct sectors are distinct observing occasions on one instrument. Depth differences can reflect dilution, aperture and background response; intrinsic binary depth is not inferred.
5. **Gaia geometry/physical plausibility.** Exact DR3 source 2007172151688083072, orbital P=4.9910192319 d, e=0.05318. Closest edge-on conjunction offset=0.02306 d (0.00462 phase), full source-specific covariance linear timing allowance=0.10982 d. Full 6x6 orbit correlation matrix is positive definite (helper receipt). Mass function=0.23406 solar masses; adopted primary mass=1.39, minimum secondary mass=1.15. Rough central duration=10.24 h versus observed median=3.09 h. Radius and main-sequence companion assumptions make this a plausibility calculation, not a fitted geometry or calibrated significance veto. Shorter observed duration can reflect impact parameter and model assumptions. Orbit agreement does not establish ownership among unresolved sources.

**Deciding limit:** Repeated 2.49543-day dips are real. Depth parity is not decisive; the quoted 4.99086-day candidate orbital ephemeris uses even half-period parity only and retains a factor-two ambiguity. The shallow crowded deficit has twenty currently flux-capable neighbors and does not uniquely establish target ownership.

**Next check:** Resolved eclipse photometry or multi-source PRF localization; distinguish alternating event kinds.

Catalogue recovery is recorded centrally in [../../shared-catalogues/coverage-matrix.csv](../../campaign/shared-catalogues/coverage-matrix.csv). A successful cone with no exact eclipsing target classification is distinct from a failed query; known recoveries must not count as new additions. No exhaustive literature priority claim is made.

| Sector | Search cycle | Measured midpoint BTJD | Formal center error d | Timing input error d | Depth ppt | Timing status |
|---|---:|---:|---:|---:|---:|---|
| 16 | 0 | 1740.8435444 | 0.00493599 | 0.0104168 | 8.23 | selected |
| 16 | 1 | 1743.3340499 | 0.00267524 | 0.0104168 | 8.73 | other parity |
| 16 | 5 | 1753.3187725 | 0.00176773 | 0.0104168 | 8.28 | other parity |
| 16 | 6 | 1755.8188187 | 0.00183474 | 0.0104168 | 8.38 | selected |
| 57 | 446 | 2853.8061349 | 0.0023894 | 0.0023894 | 12.07 | selected |
| 57 | 447 | 2856.2837163 | 0.0042196 | 0.0042196 | 9.39 | other parity |
| 57 | 448 | 2858.7885673 | 315465 | 315465 | 9.79 | excluded center covariance |
| 57 | 449 | 2861.2908682 | 0.00326148 | 0.00326148 | 7.04 | other parity |
| 57 | 452 | 2868.7849608 | 0.00283299 | 0.00283299 | 9.56 | selected |
| 57 | 453 | 2871.2739818 | 0.0027109 | 0.0027109 | 8.66 | other parity |
| 57 | 454 | 2873.7704600 | 0.00216753 | 0.00216753 | 11.45 | selected |
| 57 | 455 | 2876.2691219 | 0.00370213 | 0.00370213 | 8.73 | other parity |
| 57 | 456 | 2878.7618079 | 0.00254927 | 0.00254927 | 8.81 | selected |
| 57 | 457 | 2881.2600958 | 0.00158823 | 0.00158823 | 9.33 | other parity |
| 84 | 739 | 3584.9736429 | 0.00328012 | 0.00328012 | 10.43 | other parity |
| 84 | 740 | 3587.4662218 | 0.00254042 | 0.00254042 | 12.18 | selected |
| 84 | 741 | 3589.9605175 | 0.00298326 | 0.00298326 | 11.35 | other parity |
| 84 | 742 | 3592.4536804 | 0.00223542 | 0.00223542 | 10.06 | selected |
| 84 | 743 | 3594.9504504 | 0.00253229 | 0.00253229 | 8.90 | other parity |
| 84 | 745 | 3599.9338603 | 0.00323209 | 0.00323209 | 11.03 | other parity |
| 84 | 746 | 3602.4290268 | 0.00319896 | 0.00319896 | 9.27 | selected |
| 84 | 747 | 3604.9287199 | 0.00173011 | 0.00173011 | 9.60 | other parity |
| 84 | 748 | 3607.4305489 | 0.00232786 | 0.00232786 | 8.93 | selected |
| 84 | 749 | 3609.9192061 | 0.00259463 | 0.00259463 | 7.41 | other parity |

Evidence: [measurements.json](../../campaign/batch01/371665307/measurements.json), [raw-windows.csv](../../campaign/batch01/371665307/raw-windows.csv), [raw-events.png](../../campaign/batch01/371665307/raw-events.png), [fresh-pixels/diff_fresh.json](../../campaign/batch01/371665307/fresh-pixels/diff_fresh.json)/png, historical original receipts, [../measurement-source-receipts.json](../../campaign/batch01/measurement-source-receipts.json), [../identity-check.json](../../campaign/batch01/identity-check.json), [../alias-audit.json](../../campaign/batch01/alias-audit.json), [../gaia-geometry.json](../../campaign/batch01/gaia-geometry.json) and [../helper-audit.md](../../campaign/batch01/helper-audit.md). Original inputs and fresh outputs are covered by [../SHA256SUMS.json](../../campaign/batch01/SHA256SUMS.json) and [../source-hashes.json](../../campaign/batch01/source-hashes.json).


Stable review key: R548.

Deciding evidence and numeric artifacts:
- [fresh-pixels/diff_fresh.json](../../campaign/batch01/371665307/fresh-pixels/diff_fresh.json)
- [fresh-pixels/diff_fresh.png](../../campaign/batch01/371665307/fresh-pixels/diff_fresh.png)
- [fresh-pixels/gaia.json](../../campaign/batch01/371665307/fresh-pixels/gaia.json)
- [fresh-pixels/run.log](../../campaign/batch01/371665307/fresh-pixels/run.log)
- [historical/diff_s57.json](../../campaign/batch01/371665307/historical/diff_s57.json)
- [historical/diff_s57.png](../../campaign/batch01/371665307/historical/diff_s57.png)
- [historical/gaia.json](../../campaign/batch01/371665307/historical/gaia.json)
- [measurements.json](../../campaign/batch01/371665307/measurements.json)
- [raw-events.png](../../campaign/batch01/371665307/raw-events.png)
- [raw-windows.csv](../../campaign/batch01/371665307/raw-windows.csv)

[Batch audits and scripts](../../campaign/batch01/INDEX.md). [Depth correction provenance](../../campaign/depth-audit/README.md).
