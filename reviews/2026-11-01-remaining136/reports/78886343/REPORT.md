# TIC 78886343: CONFIRMED

Full bounded physical review: **COMPLETE**. Physical classification is separate from catalogue recovery/novelty; historical screening was not an admission verdict.

1. **Raw events.** 8 free-center trapezoid measurements from quality-zero QLP SAP_FLUX in sectors [43, 45, 72]; 8 enter the reported ephemeris. Representative raw light curves and numerical windows show repeated eclipse morphology. Predictions guided the windows and are not measurements. Flagged or uncovered windows are not clean nulls.
2. **Timing and aliases.** Measured recurring-eclipse timing supported. P=8.1943751036 +/- 0.0000175843 d; reference BTJD=2479.3243437. Epoch kind: Selected repeating eclipse; depth rank to be checked against other event kind. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. The formal error column is the local free-center model covariance; the input error adds a half-cadence floor. Singular/unidentifiable centers are excluded. Cycle/parity counts are in [../alias-audit.json](../../campaign/batch01/alias-audit.json). Selected eclipse means the measured recurrence, with no assumption that it is the deeper primary. The bounded half/double check does not prove all possible aliases absent. 
3. **Attribution.** Fresh difference stack in sector 43 has 3 events; target coordinate [7.020139253913671, 7.16586789211822], deficit [6.954075516953401, 7.164599708152924]; offset 0.066 pixel. The image-model fractional residual 0.999 is not a localization uncertainty. Every capable Gaia neighbor in the retained 60-arcsec table was inspected: Gaia 3428059934359773440: 36.94 arcsec, G=13.122, intrinsic required loss proxy=0.479; Gaia 3428059930060420608: 51.67 arcsec, G=12.226, intrinsic required loss proxy=0.298. The intrinsic loss proxy uses a pairwise G-band flux budget and cannot be directly compared with diluted pixel fractional loss. Close blends and passband/aperture response limit exclusion claims. Eight deep raw eclipses; compact deficit is near the target, distinct from both capable neighbors (approximately 1.7 and 2.4 pixels away). Bright off-target light displaces the out-of-eclipse centroid; it does not move the deficit peak. Target attribution is favored at TESS resolution.
4. **Alternative reduction.** Fresh TESScut background-subtracted target-centered 1x1/3x3/5x5 depths are 148.98/108.88/46.83 ppt; selected QLP fitted median 157.32 ppt. This reruns the historical extraction primitive using the fresh ephemeris and measured duration, with identity and source hashes checked. The alternative extraction and the QLP data for this sector share the same TESS photons; they test processing robustness and are not independent observations. Distinct sectors are distinct observing occasions on one instrument. Depth differences can reflect dilution, aperture and background response; intrinsic binary depth is not inferred.
5. **Gaia geometry/physical plausibility.** Exact DR3 source 3428060033139635072, orbital P=8.1931724592 d, e=0.07441. Closest edge-on conjunction offset=0.22692 d (0.02770 phase), full source-specific covariance linear timing allowance=0.43137 d. Full 6x6 orbit correlation matrix is positive definite (helper receipt). Mass function=0.042875 solar masses; adopted primary mass=1.31, minimum secondary mass=0.524. Rough central duration=5.65 h versus observed median=4.96 h. Radius and main-sequence companion assumptions make this a plausibility calculation, not a fitted geometry or calibrated significance veto. Shorter observed duration can reflect impact parameter and model assumptions. Orbit agreement does not establish ownership among unresolved sources.

**Deciding limit:** Eight deep raw eclipses; compact deficit is near the target, distinct from both capable neighbors (approximately 1.7 and 2.4 pixels away). Bright off-target light displaces the out-of-eclipse centroid; it does not move the deficit peak. Target attribution is favored at TESS resolution.

**Next check:** Optional resolved photometry and spectroscopy for precision physical parameters.

Catalogue recovery is recorded centrally in [../../shared-catalogues/coverage-matrix.csv](../../campaign/shared-catalogues/coverage-matrix.csv). A successful cone with no exact eclipsing target classification is distinct from a failed query; known recoveries must not count as new additions. No exhaustive literature priority claim is made.

| Sector | Search cycle | Measured midpoint BTJD | Formal center error d | Timing input error d | Depth ppt | Timing status |
|---|---:|---:|---:|---:|---:|---|
| 43 | 0 | 2479.3245025 | 0.000393849 | 0.00347256 | 155.60 | selected |
| 43 | 1 | 2487.5190390 | 0.000329102 | 0.00347256 | 156.95 | selected |
| 43 | 2 | 2495.7125372 | 0.0002809 | 0.00347256 | 160.64 | selected |
| 45 | 6 | 2528.4907727 | 0.000332102 | 0.0034724 | 160.15 | selected |
| 45 | 7 | 2536.6851645 | 0.000290897 | 0.0034724 | 160.04 | selected |
| 45 | 8 | 2544.8790784 | 0.000349266 | 0.0034724 | 157.69 | selected |
| 72 | 96 | 3265.9841647 | 0.000222825 | 0.00115746 | 155.35 | selected |
| 72 | 98 | 3282.3732894 | 0.000243797 | 0.00115746 | 154.75 | selected |

Evidence: [measurements.json](../../campaign/batch01/78886343/measurements.json), [raw-windows.csv](../../campaign/batch01/78886343/raw-windows.csv), [raw-events.png](../../campaign/batch01/78886343/raw-events.png), [fresh-pixels/diff_fresh.json](../../campaign/batch01/78886343/fresh-pixels/diff_fresh.json)/png, historical original receipts, [../measurement-source-receipts.json](../../campaign/batch01/measurement-source-receipts.json), [../identity-check.json](../../campaign/batch01/identity-check.json), [../alias-audit.json](../../campaign/batch01/alias-audit.json), [../gaia-geometry.json](../../campaign/batch01/gaia-geometry.json) and [../helper-audit.md](../../campaign/batch01/helper-audit.md). Original inputs and fresh outputs are covered by [../SHA256SUMS.json](../../campaign/batch01/SHA256SUMS.json) and [../source-hashes.json](../../campaign/batch01/source-hashes.json).


Stable review key: R544.

Deciding evidence and numeric artifacts:
- [fresh-pixels/diff_fresh.json](../../campaign/batch01/78886343/fresh-pixels/diff_fresh.json)
- [fresh-pixels/diff_fresh.png](../../campaign/batch01/78886343/fresh-pixels/diff_fresh.png)
- [fresh-pixels/gaia.json](../../campaign/batch01/78886343/fresh-pixels/gaia.json)
- [fresh-pixels/run.log](../../campaign/batch01/78886343/fresh-pixels/run.log)
- [historical/diff_s43.json](../../campaign/batch01/78886343/historical/diff_s43.json)
- [historical/diff_s43.png](../../campaign/batch01/78886343/historical/diff_s43.png)
- [historical/gaia.json](../../campaign/batch01/78886343/historical/gaia.json)
- [measurements.json](../../campaign/batch01/78886343/measurements.json)
- [raw-events.png](../../campaign/batch01/78886343/raw-events.png)
- [raw-windows.csv](../../campaign/batch01/78886343/raw-windows.csv)

[Batch audits and scripts](../../campaign/batch01/INDEX.md). [Depth correction provenance](../../campaign/depth-audit/README.md).
