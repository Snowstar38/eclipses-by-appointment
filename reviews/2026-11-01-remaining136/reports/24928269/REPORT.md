# TIC 24928269: CONFIRMED

Full bounded physical review: **COMPLETE**. Physical classification is separate from catalogue recovery/novelty; historical screening was not an admission verdict.

1. **Raw events.** 12 free-center trapezoid measurements from quality-zero QLP SAP_FLUX in sectors [3, 30, 97]; 12 enter the reported ephemeris. Representative raw light curves and numerical windows show repeated eclipse morphology. Predictions guided the windows and are not measurements. Flagged or uncovered windows are not clean nulls.
2. **Timing and aliases.** Measured recurring-eclipse timing supported. P=6.5557481629 +/- 0.0000077663 d; reference BTJD=1387.1372325. Epoch kind: Selected repeating eclipse; depth rank to be checked against other event kind. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. The formal error column is the local free-center model covariance; the input error adds a half-cadence floor. Singular/unidentifiable centers are excluded. Cycle/parity counts are in [../alias-audit.json](../../campaign/batch01/alias-audit.json). Selected eclipse means the measured recurrence, with no assumption that it is the deeper primary. The bounded half/double check does not prove all possible aliases absent. 
3. **Attribution.** Fresh difference stack in sector 97 has 7 events; target coordinate [7.76964353045026, 7.698866310414914], deficit [7.846047728639347, 7.684373126419072]; offset 0.078 pixel. The image-model fractional residual 0.209 is not a localization uncertainty. Every capable Gaia neighbor in the retained 60-arcsec table was inspected: None under the approximate G-band brightness screen within 60 arcsec. The intrinsic loss proxy uses a pairwise G-band flux budget and cannot be directly compared with diluted pixel fractional loss. Close blends and passband/aperture response limit exclusion claims. Twelve deep raw eclipses over S3/30/97. Sector-dependent depth is consistent with changing dilution; isolated target-centered deficit.
4. **Alternative reduction.** Fresh TESScut background-subtracted target-centered 1x1/3x3/5x5 depths are 85.35/85.78/83.76 ppt; selected QLP fitted median 77.24 ppt. This reruns the historical extraction primitive using the fresh ephemeris and measured duration, with identity and source hashes checked. The alternative extraction and the QLP data for this sector share the same TESS photons; they test processing robustness and are not independent observations. Distinct sectors are distinct observing occasions on one instrument. Depth differences can reflect dilution, aperture and background response; intrinsic binary depth is not inferred.
5. **Gaia geometry/physical plausibility.** Exact DR3 source 2460872435038706944, orbital P=6.5555008903 d, e=0.03484. Closest edge-on conjunction offset=-0.00266 d (-0.00041 phase), full source-specific covariance linear timing allowance=0.17924 d. Full 6x6 orbit correlation matrix is positive definite (helper receipt). Mass function=0.02874 solar masses; adopted primary mass=1.23, minimum secondary mass=0.429. Rough central duration=6.00 h versus observed median=5.07 h. Radius and main-sequence companion assumptions make this a plausibility calculation, not a fitted geometry or calibrated significance veto. Shorter observed duration can reflect impact parameter and model assumptions. Orbit agreement does not establish ownership among unresolved sources.

**Deciding limit:** Twelve deep raw eclipses over S3/30/97. Sector-dependent depth is consistent with changing dilution; isolated target-centered deficit.

**Next check:** Optional resolved photometry and spectroscopy for precision physical parameters.

Catalogue recovery is recorded centrally in [../../shared-catalogues/coverage-matrix.csv](../../campaign/shared-catalogues/coverage-matrix.csv). A successful cone with no exact eclipsing target classification is distinct from a failed query; known recoveries must not count as new additions. No exhaustive literature priority claim is made.

| Sector | Search cycle | Measured midpoint BTJD | Formal center error d | Timing input error d | Depth ppt | Timing status |
|---|---:|---:|---:|---:|---:|---|
| 3 | 0 | 1387.1372902 | 0.000277692 | 0.0104169 | 83.67 | selected |
| 3 | 1 | 1393.6936237 | 0.000339641 | 0.0104169 | 83.56 | selected |
| 3 | 2 | 1400.2487076 | 0.000163537 | 0.0104169 | 83.54 | selected |
| 30 | 112 | 2121.3811531 | 0.000281748 | 0.00347229 | 87.16 | selected |
| 30 | 114 | 2134.4922055 | 0.000213255 | 0.00347229 | 86.27 | selected |
| 97 | 389 | 3937.3234800 | 0.000208905 | 0.00115741 | 75.93 | selected |
| 97 | 390 | 3943.8789339 | 0.000189922 | 0.00115741 | 75.40 | selected |
| 97 | 391 | 3950.4348892 | 0.000246981 | 0.00115741 | 76.20 | selected |
| 97 | 392 | 3956.9904867 | 0.000210853 | 0.00115741 | 75.78 | selected |
| 97 | 393 | 3963.5466919 | 0.000365138 | 0.00115741 | 76.83 | selected |
| 97 | 394 | 3970.1019276 | 0.00018623 | 0.00115741 | 76.72 | selected |
| 97 | 396 | 3983.2129381 | 0.000171054 | 0.00115741 | 77.64 | selected |

Evidence: [measurements.json](../../campaign/batch01/24928269/measurements.json), [raw-windows.csv](../../campaign/batch01/24928269/raw-windows.csv), [raw-events.png](../../campaign/batch01/24928269/raw-events.png), [fresh-pixels/diff_fresh.json](../../campaign/batch01/24928269/fresh-pixels/diff_fresh.json)/png, historical original receipts, [../measurement-source-receipts.json](../../campaign/batch01/measurement-source-receipts.json), [../identity-check.json](../../campaign/batch01/identity-check.json), [../alias-audit.json](../../campaign/batch01/alias-audit.json), [../gaia-geometry.json](../../campaign/batch01/gaia-geometry.json) and [../helper-audit.md](../../campaign/batch01/helper-audit.md). Original inputs and fresh outputs are covered by [../SHA256SUMS.json](../../campaign/batch01/SHA256SUMS.json) and [../source-hashes.json](../../campaign/batch01/source-hashes.json).


Stable review key: R541.

Deciding evidence and numeric artifacts:
- [fresh-pixels/diff_fresh.json](../../campaign/batch01/24928269/fresh-pixels/diff_fresh.json)
- [fresh-pixels/diff_fresh.png](../../campaign/batch01/24928269/fresh-pixels/diff_fresh.png)
- [fresh-pixels/gaia.json](../../campaign/batch01/24928269/fresh-pixels/gaia.json)
- [fresh-pixels/run.log](../../campaign/batch01/24928269/fresh-pixels/run.log)
- [historical/diff_s97.json](../../campaign/batch01/24928269/historical/diff_s97.json)
- [historical/diff_s97.png](../../campaign/batch01/24928269/historical/diff_s97.png)
- [historical/gaia.json](../../campaign/batch01/24928269/historical/gaia.json)
- [measurements.json](../../campaign/batch01/24928269/measurements.json)
- [raw-events.png](../../campaign/batch01/24928269/raw-events.png)
- [raw-windows.csv](../../campaign/batch01/24928269/raw-windows.csv)

[Batch audits and scripts](../../campaign/batch01/INDEX.md). [Depth correction provenance](../../campaign/depth-audit/README.md).
