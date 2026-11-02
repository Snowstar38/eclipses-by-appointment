# TIC 150008480: PROBABLE

Full bounded physical review: **COMPLETE**. Physical classification is separate from catalogue recovery/novelty; historical screening was not an admission verdict.

1. **Raw events.** 11 free-center trapezoid measurements from quality-zero QLP SAP_FLUX in sectors [61, 88]; 11 enter the reported ephemeris. Representative raw light curves and numerical windows show repeated eclipse morphology. Predictions guided the windows and are not measurements. Flagged or uncovered windows are not clean nulls.
2. **Timing and aliases.** Measured recurring-eclipse timing supported. P=4.9001176563 +/- 0.0000153100 d; reference BTJD=2967.3669874. Epoch kind: Selected repeating eclipse; depth rank to be checked against other event kind. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. The formal error column is the local free-center model covariance; the input error adds a half-cadence floor. Singular/unidentifiable centers are excluded. Cycle/parity counts are in [../alias-audit.json](../../campaign/batch01/alias-audit.json). Selected eclipse means the measured recurrence, with no assumption that it is the deeper primary. The bounded half/double check does not prove all possible aliases absent. 
3. **Attribution.** Fresh difference stack in sector 88 has 6 events; target coordinate [7.949368002849406, 7.814154538161146], deficit [7.840202825047673, 7.884281988246106]; offset 0.130 pixel. The image-model fractional residual 0.852 is not a localization uncertainty. Every capable Gaia neighbor in the retained 60-arcsec table was inspected: Gaia 5598671598997580160: 21.97 arcsec, G=16.992, intrinsic required loss proxy=0.640; Gaia 5598672049978646528: 23.92 arcsec, G=16.517, intrinsic required loss proxy=0.416; Gaia 5598671976954710528: 33.79 arcsec, G=16.674, intrinsic required loss proxy=0.480; Gaia 5598671672021524736: 38.52 arcsec, G=15.384, intrinsic required loss proxy=0.152; Gaia 5598671976956157696: 39.45 arcsec, G=17.455, intrinsic required loss proxy=0.976; Gaia 5598672015618461696: 42.89 arcsec, G=16.796, intrinsic required loss proxy=0.536; Gaia 5598671981258727424: 43.01 arcsec, G=16.760, intrinsic required loss proxy=0.518; Gaia 5598672084337939328: 43.79 arcsec, G=15.165, intrinsic required loss proxy=0.126; Gaia 5598671672021097856: 46.32 arcsec, G=16.372, intrinsic required loss proxy=0.365; Gaia 5598660230228212224: 53.18 arcsec, G=15.908, intrinsic required loss proxy=0.241; Gaia 5598672015618457600: 58.32 arcsec, G=17.149, intrinsic required loss proxy=0.738. The intrinsic loss proxy uses a pairwise G-band flux budget and cannot be directly compared with diluted pixel fractional loss. Close blends and passband/aperture response limit exclusion claims. Eleven shallow repeated raw eclipses; eleven capable neighbors within 60 arcsec and a noisy deficit leave source attribution unresolved. The Gaia conjunction discrepancy is -0.043 phase, within the descriptive orbit timing uncertainty, and is not evidence of unique target ownership.
4. **Alternative reduction.** Fresh TESScut background-subtracted target-centered 1x1/3x3/5x5 depths are 8.61/8.46/6.69 ppt; selected QLP fitted median 8.71 ppt. This reruns the historical extraction primitive using the fresh ephemeris and measured duration, with identity and source hashes checked. The alternative extraction and the QLP data for this sector share the same TESS photons; they test processing robustness and are not independent observations. Distinct sectors are distinct observing occasions on one instrument. Depth differences can reflect dilution, aperture and background response; intrinsic binary depth is not inferred.
5. **Gaia geometry/physical plausibility.** Exact DR3 source 5598671976949355264, orbital P=4.9006621570 d, e=0.05643. Closest edge-on conjunction offset=-0.21183 d (-0.04322 phase), full source-specific covariance linear timing allowance=0.34169 d. Full 6x6 orbit correlation matrix is positive definite (helper receipt). Mass function=0.042527 solar masses; adopted primary mass=1.25, minimum secondary mass=0.509. Rough central duration=7.10 h versus observed median=2.85 h. Radius and main-sequence companion assumptions make this a plausibility calculation, not a fitted geometry or calibrated significance veto. Shorter observed duration can reflect impact parameter and model assumptions. Orbit agreement does not establish ownership among unresolved sources.

**Deciding limit:** Eleven shallow repeated raw eclipses; eleven capable neighbors within 60 arcsec and a noisy deficit leave source attribution unresolved. The Gaia conjunction discrepancy is -0.043 phase, within the descriptive orbit timing uncertainty, and is not evidence of unique target ownership.

**Next check:** Resolved eclipse photometry or multi-source PRF localization; distinguish alternating event kinds.

Catalogue recovery is recorded centrally in [../../shared-catalogues/coverage-matrix.csv](../../campaign/shared-catalogues/coverage-matrix.csv). A successful cone with no exact eclipsing target classification is distinct from a failed query; known recoveries must not count as new additions. No exhaustive literature priority claim is made.

| Sector | Search cycle | Measured midpoint BTJD | Formal center error d | Timing input error d | Depth ppt | Timing status |
|---|---:|---:|---:|---:|---:|---|
| 61 | 301 | 2967.3693978 | 0.0019375 | 0.0019375 | 9.20 | selected |
| 61 | 302 | 2972.2629428 | 0.00412332 | 0.00412332 | 8.41 | selected |
| 61 | 303 | 2977.1704736 | 0.00306238 | 0.00306238 | 8.64 | selected |
| 61 | 304 | 2982.0643101 | 0.00372941 | 0.00372941 | 8.12 | selected |
| 61 | 305 | 2986.9618408 | 0.00319197 | 0.00319197 | 8.71 | selected |
| 88 | 449 | 3692.5818366 | 0.00353184 | 0.00353184 | 12.12 | selected |
| 88 | 450 | 3697.4909404 | 0.00311603 | 0.00311603 | 9.73 | selected |
| 88 | 451 | 3702.3836062 | 0.00381891 | 0.00381891 | 7.77 | selected |
| 88 | 452 | 3707.2868200 | 0.00354984 | 0.00354984 | 9.21 | selected |
| 88 | 453 | 3712.1823973 | 0.00298151 | 0.00298151 | 7.65 | selected |
| 88 | 454 | 3717.0830767 | 0.00278977 | 0.00278977 | 9.73 | selected |

Evidence: [measurements.json](../../campaign/batch01/150008480/measurements.json), [raw-windows.csv](../../campaign/batch01/150008480/raw-windows.csv), [raw-events.png](../../campaign/batch01/150008480/raw-events.png), [fresh-pixels/diff_fresh.json](../../campaign/batch01/150008480/fresh-pixels/diff_fresh.json)/png, historical original receipts, [../measurement-source-receipts.json](../../campaign/batch01/measurement-source-receipts.json), [../identity-check.json](../../campaign/batch01/identity-check.json), [../alias-audit.json](../../campaign/batch01/alias-audit.json), [../gaia-geometry.json](../../campaign/batch01/gaia-geometry.json) and [../helper-audit.md](../../campaign/batch01/helper-audit.md). Original inputs and fresh outputs are covered by [../SHA256SUMS.json](../../campaign/batch01/SHA256SUMS.json) and [../source-hashes.json](../../campaign/batch01/source-hashes.json).


Stable review key: R542.

Deciding evidence and numeric artifacts:
- [fresh-pixels/diff_fresh.json](../../campaign/batch01/150008480/fresh-pixels/diff_fresh.json)
- [fresh-pixels/diff_fresh.png](../../campaign/batch01/150008480/fresh-pixels/diff_fresh.png)
- [fresh-pixels/gaia.json](../../campaign/batch01/150008480/fresh-pixels/gaia.json)
- [fresh-pixels/run.log](../../campaign/batch01/150008480/fresh-pixels/run.log)
- [historical/diff_s88.json](../../campaign/batch01/150008480/historical/diff_s88.json)
- [historical/diff_s88.png](../../campaign/batch01/150008480/historical/diff_s88.png)
- [historical/gaia.json](../../campaign/batch01/150008480/historical/gaia.json)
- [measurements.json](../../campaign/batch01/150008480/measurements.json)
- [raw-events.png](../../campaign/batch01/150008480/raw-events.png)
- [raw-windows.csv](../../campaign/batch01/150008480/raw-windows.csv)

[Batch audits and scripts](../../campaign/batch01/INDEX.md). [Depth correction provenance](../../campaign/depth-audit/README.md).
