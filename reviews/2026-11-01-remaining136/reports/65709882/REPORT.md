# TIC 65709882: CONFIRMED

Full bounded physical review: **COMPLETE**. Physical classification is separate from catalogue recovery/novelty; historical screening was not an admission verdict.

1. **Raw events.** 4 free-center trapezoid measurements from quality-zero QLP SAP_FLUX in sectors [7, 61, 88]; 4 enter the reported ephemeris. Representative raw light curves and numerical windows show repeated eclipse morphology. Predictions guided the windows and are not measurements. Flagged or uncovered windows are not clean nulls.
2. **Timing and aliases.** Measured recurring-eclipse timing supported. P=15.1185128633 +/- 0.0000390171 d; reference BTJD=1496.1875304. Epoch kind: Selected repeating eclipse; depth rank to be checked against other event kind. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. The formal error column is the local free-center model covariance; the input error adds a half-cadence floor. Singular/unidentifiable centers are excluded. Cycle/parity counts are in [../alias-audit.json](../../campaign/batch01/alias-audit.json). Selected eclipse means the measured recurrence, with no assumption that it is the deeper primary. The bounded half/double check does not prove all possible aliases absent. 
3. **Attribution.** Fresh difference stack in sector 7 has 2 events; target coordinate [7.94178071976971, 7.742445486437363], deficit [7.965526147928077, 7.85884305040405]; offset 0.119 pixel. The image-model fractional residual 0.999 is not a localization uncertainty. Every capable Gaia neighbor in the retained 60-arcsec table was inspected: Gaia 5609864391149987072: 22.11 arcsec, G=15.147, intrinsic required loss proxy=0.624; Gaia 5609864425509719680: 41.71 arcsec, G=14.509, intrinsic required loss proxy=0.366; Gaia 5609864421205498240: 50.71 arcsec, G=10.613, intrinsic required loss proxy=0.053; Gaia 5609864356790241792: 50.73 arcsec, G=15.532, intrinsic required loss proxy=0.870; Gaia 5609911326554371712: 52.71 arcsec, G=15.649, intrinsic required loss proxy=0.964. The intrinsic loss proxy uses a pairwise G-band flux budget and cannot be directly compared with diluted pixel fractional loss. Close blends and passband/aperture response limit exclusion claims. Four deep raw eclipses including consecutive S7 events support recurrence. Fresh deficit lies 0.12 pixel from target while all five capable alternatives are at least about one pixel away. The very bright off-target light dominates the full image but not its compact deficit. Attribution favors target at TESS resolution; nearest capable neighbor limits subpixel claims.
4. **Alternative reduction.** Fresh TESScut background-subtracted target-centered 1x1/3x3/5x5 depths are 29.76/12.73/4.12 ppt; selected QLP fitted median 44.35 ppt. This reruns the historical extraction primitive using the fresh ephemeris and measured duration, with identity and source hashes checked. The alternative extraction and the QLP data for this sector share the same TESS photons; they test processing robustness and are not independent observations. Distinct sectors are distinct observing occasions on one instrument. Depth differences can reflect dilution, aperture and background response; intrinsic binary depth is not inferred.
5. **Gaia geometry/physical plausibility.** Exact DR3 source 5609864386845761152, orbital P=15.1280611937 d, e=0.25942. Closest edge-on conjunction offset=-0.40112 d (-0.02651 phase), full source-specific covariance linear timing allowance=0.35535 d. Full 6x6 orbit correlation matrix is positive definite (helper receipt). Mass function=0.097082 solar masses; adopted primary mass=1.19, minimum secondary mass=0.703. Rough central duration=15.17 h versus observed median=13.55 h. Radius and main-sequence companion assumptions make this a plausibility calculation, not a fitted geometry or calibrated significance veto. Shorter observed duration can reflect impact parameter and model assumptions. Orbit agreement does not establish ownership among unresolved sources.

**Deciding limit:** Four deep raw eclipses including consecutive S7 events support recurrence. Fresh deficit lies 0.12 pixel from target while all five capable alternatives are at least about one pixel away. The very bright off-target light dominates the full image but not its compact deficit. Attribution favors target at TESS resolution; nearest capable neighbor limits subpixel claims.

**Next check:** Optional resolved photometry and spectroscopy for precision physical parameters.

Catalogue recovery is recorded centrally in [../../shared-catalogues/coverage-matrix.csv](../../campaign/shared-catalogues/coverage-matrix.csv). A successful cone with no exact eclipsing target classification is distinct from a failed query; known recoveries must not count as new additions. No exhaustive literature priority claim is made.

| Sector | Search cycle | Measured midpoint BTJD | Formal center error d | Timing input error d | Depth ppt | Timing status |
|---|---:|---:|---:|---:|---:|---|
| 7 | 0 | 1496.1864876 | 0.00352353 | 0.0104166 | 44.39 | selected |
| 7 | 1 | 1511.3015204 | 0.00315238 | 0.0104166 | 45.11 | selected |
| 61 | 98 | 2977.8023105 | 0.00182987 | 0.00182987 | 44.32 | selected |
| 88 | 146 | 3703.4901278 | 0.00164383 | 0.00164383 | 38.68 | selected |

Evidence: [measurements.json](../../campaign/batch01/65709882/measurements.json), [raw-windows.csv](../../campaign/batch01/65709882/raw-windows.csv), [raw-events.png](../../campaign/batch01/65709882/raw-events.png), [fresh-pixels/diff_fresh.json](../../campaign/batch01/65709882/fresh-pixels/diff_fresh.json)/png, historical original receipts, [../measurement-source-receipts.json](../../campaign/batch01/measurement-source-receipts.json), [../identity-check.json](../../campaign/batch01/identity-check.json), [../alias-audit.json](../../campaign/batch01/alias-audit.json), [../gaia-geometry.json](../../campaign/batch01/gaia-geometry.json) and [../helper-audit.md](../../campaign/batch01/helper-audit.md). Original inputs and fresh outputs are covered by [../SHA256SUMS.json](../../campaign/batch01/SHA256SUMS.json) and [../source-hashes.json](../../campaign/batch01/source-hashes.json).


Stable review key: R549.

Deciding evidence and numeric artifacts:
- [fresh-pixels/diff_fresh.json](../../campaign/batch01/65709882/fresh-pixels/diff_fresh.json)
- [fresh-pixels/diff_fresh.png](../../campaign/batch01/65709882/fresh-pixels/diff_fresh.png)
- [fresh-pixels/gaia.json](../../campaign/batch01/65709882/fresh-pixels/gaia.json)
- [fresh-pixels/run.log](../../campaign/batch01/65709882/fresh-pixels/run.log)
- [historical/diff_s07.json](../../campaign/batch01/65709882/historical/diff_s07.json)
- [historical/diff_s07.png](../../campaign/batch01/65709882/historical/diff_s07.png)
- [historical/gaia.json](../../campaign/batch01/65709882/historical/gaia.json)
- [measurements.json](../../campaign/batch01/65709882/measurements.json)
- [raw-events.png](../../campaign/batch01/65709882/raw-events.png)
- [raw-windows.csv](../../campaign/batch01/65709882/raw-windows.csv)

[Batch audits and scripts](../../campaign/batch01/INDEX.md). [Depth correction provenance](../../campaign/depth-audit/README.md).
