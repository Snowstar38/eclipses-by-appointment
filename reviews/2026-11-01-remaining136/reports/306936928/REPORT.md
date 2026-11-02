# TIC 306936928: PROBABLE

Full bounded physical review: **COMPLETE**. Physical classification is separate from catalogue recovery/novelty; historical screening was not an admission verdict.

1. **Raw events.** 14 free-center trapezoid measurements from quality-zero QLP SAP_FLUX in sectors [33, 87]; 14 enter the reported ephemeris. Representative raw light curves and numerical windows show repeated eclipse morphology. Predictions guided the windows and are not measurements. Flagged or uncovered windows are not clean nulls.
2. **Timing and aliases.** Measured recurring-eclipse timing supported. Selected primary and unequal secondary morphology support the quoted orbital period; half/double hypotheses were checked. P=3.2658677781 +/- 0.0000031329 d; reference BTJD=2202.2402559. Epoch kind: Selected repeating eclipse, primary by convention; deeper/secondary identity not independently established. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. The formal error column is the local free-center model covariance; the input error adds a half-cadence floor. Singular/unidentifiable centers are excluded. Cycle/parity counts are in [../alias-audit.json](../../campaign/batch06/alias-audit.json). The epoch kind above states whether the fitted events are identified as deeper primary or selected eclipse by convention. The bounded half/double check does not prove all possible aliases absent.
3. **Attribution.** Fresh difference stack in sector 33 has 7 events; target coordinate [7.343879930269948, 7.9267470273072576], deficit [7.582796384292077, 8.026741837058745]; offset 0.259 pixel. The image-model fractional residual 0.584 is not a localization uncertainty. Every capable Gaia neighbor in the retained 60-arcsec table was inspected: Gaia 3032561616123801728: 10.59 arcsec, G=16.765, intrinsic required loss proxy=0.982; Gaia 3032561616123796352: 21.85 arcsec, G=15.627, intrinsic required loss proxy=0.356; Gaia 3032561581764068224: 22.78 arcsec, G=14.392, intrinsic required loss proxy=0.127; Gaia 3032567697797482112: 36.58 arcsec, G=16.204, intrinsic required loss proxy=0.593; Gaia 3032561822283763840: 37.84 arcsec, G=15.291, intrinsic required loss proxy=0.267. The intrinsic loss proxy uses a pairwise G-band flux budget and cannot be directly compared with diluted pixel fractional loss. Close blends and passband/aperture response limit exclusion claims. Repeated narrow primary and secondary dips are secure, but five flux-capable Gaia neighbors include a 10.59 arcsec G16.77 source requiring an almost total intrinsic eclipse. The compact blended deficit does not uniquely resolve target ownership; PROBABLE.
4. **Alternative reduction.** Fresh TESScut background-subtracted target-centered 1x1/3x3/5x5 depths are 15.54/13.83/12.35 ppt; selected QLP fitted median 18.87 ppt. This reruns the historical extraction primitive using the fresh ephemeris and measured duration, with identity and source hashes checked. The alternative extraction and the QLP data for this sector share the same TESS photons; they test processing robustness and are not independent observations. Distinct sectors are distinct observing occasions on one instrument. Depth differences can reflect dilution, aperture and background response; intrinsic binary depth is not inferred.
5. **Gaia geometry/physical plausibility.** Exact DR3 source 3032561611821997952, orbital P=3.2656610989 d, e=0.04672. Closest edge-on conjunction offset=0.05747 d (0.01760 phase), full source-specific covariance linear timing allowance=0.13828 d. Mass function=0.07895 solar masses; adopted primary mass=1.46, minimum secondary mass=0.722. Rough central duration=4.87 h versus observed median=2.25 h. Radius and main-sequence companion assumptions make this a plausibility calculation, not a fitted geometry or calibrated significance veto. Shorter observed duration can reflect impact parameter and model assumptions. Orbit agreement does not establish ownership among unresolved sources.

**Secondary phase check:** Pooled raw-window free-center phase=0.4995127844887043, depth=3.4525177588269473ppt. Formal pooled trapezoid covariance only; sector normalization, red noise and shape systematics uncalibrated. Weak secondary fits (especially314713331) describe inspected narrow dips and are not independent primary-eclipse evidence or calibrated detection significances. See [../secondary-phases.json](../../campaign/batch06/secondary-phases.json) and [../secondary-contact.png](../../campaign/batch06/secondary-contact.png).

**Deciding limit:** Repeated narrow primary and secondary dips are secure, but five flux-capable Gaia neighbors include a 10.59 arcsec G16.77 source requiring an almost total intrinsic eclipse. The compact blended deficit does not uniquely resolve target ownership; PROBABLE.

**Next check:** Resolved eclipse photometry or multi-source PRF localization; distinguish alternating event kinds.

Catalogue recovery is recorded centrally in [../../shared-catalogues/coverage-matrix.csv](../../campaign/shared-catalogues/coverage-matrix.csv). A successful cone with no exact eclipsing target classification is distinct from a failed query; known recoveries must not count as new additions. No exhaustive literature priority claim is made.

| Sector | Search cycle | Measured midpoint BTJD | Formal center error d | Timing input error d | Depth ppt | Timing status |
|---|---:|---:|---:|---:|---:|---|
| 33 | 217 | 2202.2418554 | 0.00106251 | 0.00347228 | 20.93 | selected |
| 33 | 218 | 2205.5070455 | 0.00135498 | 0.00347228 | 19.67 | selected |
| 33 | 219 | 2208.7721713 | 0.000827799 | 0.00347228 | 21.51 | selected |
| 33 | 220 | 2212.0372461 | 0.00131487 | 0.00347228 | 19.04 | selected |
| 33 | 222 | 2218.5702969 | 0.0013536 | 0.00347228 | 14.80 | selected |
| 33 | 223 | 2221.8345328 | 0.00085435 | 0.00347228 | 18.20 | selected |
| 33 | 224 | 2225.0993307 | 0.00142478 | 0.00347228 | 19.35 | selected |
| 87 | 665 | 3665.3503026 | 0.00117801 | 0.00117801 | 20.98 | selected |
| 87 | 666 | 3668.6145142 | 0.0013157 | 0.0013157 | 18.70 | selected |
| 87 | 667 | 3671.8803126 | 0.00146109 | 0.00146109 | 16.39 | selected |
| 87 | 668 | 3675.1463076 | 0.00162138 | 0.00162138 | 17.26 | selected |
| 87 | 670 | 3681.6791059 | 0.00119067 | 0.00119067 | 16.52 | selected |
| 87 | 671 | 3684.9431140 | 0.00114514 | 0.00115742 | 18.33 | selected |
| 87 | 672 | 3688.2099483 | 0.00151347 | 0.00151347 | 22.23 | selected |

Evidence: [measurements.json](../../campaign/batch06/306936928/measurements.json), [raw-windows.csv](../../campaign/batch06/306936928/raw-windows.csv), [raw-events.png](../../campaign/batch06/306936928/raw-events.png), [fresh-pixels/diff_fresh.json](../../campaign/batch06/306936928/fresh-pixels/diff_fresh.json)/png, historical original receipts, [../download-receipts.json](../../campaign/batch06/download-receipts.json), [../identity-check.json](../../campaign/batch06/identity-check.json), [../alias-audit.json](../../campaign/batch06/alias-audit.json), [../gaia-geometry.json](../../campaign/batch06/gaia-geometry.json) and [../helper-audit.md](../../campaign/batch06/helper-audit.md). Original inputs and fresh outputs are covered by [../SHA256SUMS.json](../../campaign/batch06/SHA256SUMS.json) and [../source-hashes.json](../../campaign/batch06/source-hashes.json).

Depth correction audit (2026-11-02): realized trapezoid decrement replaces its unconstrained amplitude parameter. Original input windows, fitted centers/widths, timing selections and physical verdict are retained; capable-neighbor membership is unchanged. See [../../depth-audit/README.md](../../campaign/depth-audit/README.md).


Stable review key: R590.

Deciding evidence and numeric artifacts:
- [fresh-pixels/diff_fresh.json](../../campaign/batch06/306936928/fresh-pixels/diff_fresh.json)
- [fresh-pixels/diff_fresh.png](../../campaign/batch06/306936928/fresh-pixels/diff_fresh.png)
- [fresh-pixels/gaia.json](../../campaign/batch06/306936928/fresh-pixels/gaia.json)
- [fresh-pixels/run.log](../../campaign/batch06/306936928/fresh-pixels/run.log)
- [historical/diff_s33.json](../../campaign/batch06/306936928/historical/diff_s33.json)
- [historical/diff_s33.png](../../campaign/batch06/306936928/historical/diff_s33.png)
- [historical/gaia.json](../../campaign/batch06/306936928/historical/gaia.json)
- [measurements.json](../../campaign/batch06/306936928/measurements.json)
- [phase-check.json](../../campaign/batch06/306936928/phase-check.json)
- [raw-events.png](../../campaign/batch06/306936928/raw-events.png)
- [raw-windows.csv](../../campaign/batch06/306936928/raw-windows.csv)

[Batch audits and scripts](../../campaign/batch06/INDEX.md). [Depth correction provenance](../../campaign/depth-audit/README.md).
