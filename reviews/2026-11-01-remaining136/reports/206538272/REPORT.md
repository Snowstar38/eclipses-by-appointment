# TIC 206538272: CONFIRMED

Full bounded physical review: **COMPLETE**. Physical outcome and catalogue novelty are separate; a known recovery is not a new addition.

1. **Raw repeated events.** 21 free-center local trapezoid measurements in quality-zero QLP SAP_FLUX; 21 centers enter timing, in sectors [28, 68, 92]. Predictions locate windows and are not measurements. Flagged or uncovered windows are not clean nulls. Twenty-one deep events recur; nineteen shallower secondary fits at phase 0.50006 distinguish eclipse kinds. No capable Gaia neighbor within 60 arcsec.
2. **Timing and aliases.** Measured recurring-eclipse period P=3.1388019249 +/- 0.0000021104 days, epoch BTJD=2063.4906776. Epoch kind is the selected recurring eclipse; deeper-primary rank is not assumed. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. There are 16 adjacent same-kind pairs within sectors. Selected depths occur comparably in both cycle parities; doubling does not reveal alternating selected-event kinds. Halving interleaves a shallow secondary or sampled baseline, not the selected eclipse. Actual measured secondary-candidate phase=0.500060, depth=45.96 ppt, 19 usable fits. Actual phase scans and candidate fits are retained; secondary usability is a heuristic amplitude/local-scatter check, not calibrated significance. No exhaustive all-alias search or calibrated secondary-null confidence is asserted.
3. **Pixel attribution.** Fresh S28 difference stack contains 5 selected eclipses. Target WCS pixel=[7.906055696455212, 7.20140362062328], deficit centroid=[8.041218553144338, 7.290939336940613], descriptive offset=0.162 pixel. Neither offset nor image residual is a calibrated localization uncertainty or universal veto. All capable Gaia neighbors: None under the approximate pairwise G-band flux screen within 60 arcsec.. Capability is a G-band pairwise flux-budget proxy; color and aperture response limit precision. Intrinsic neighbor losses are never equated to diluted pixel fractional loss. Same-unit actual deficits and field morphology are independently recorded in [../terra-pixel-audit.json](../../campaign/batch04/terra-pixel-audit.json); close blends retain uncertainty.
4. **Alternative reduction.** Reused, read and rerun TESScut primitive subtracts faint-pixel background, with symmetric local side windows and selected eclipse core; fresh target-centered 1x1/3x3/5x5 depths=179.54/168.57/86.99 ppt. QLP fitted median=204.10 ppt. Aperture, dilution and background response explain why these are not intrinsic-depth measurements. This reduction and the retained QLP sector share TESS photons, testing processing robustness rather than independent observations. Distinct sectors remain occasions on one instrument.
5. **Gaia geometry.** Source 6822324759628771840; P=3.1385994235 +/- 0.0001972352 days, e=0.05956. Closest edge-on conjunction offset=0.05815 days (0.01853 phase), source-specific full covariance linear allowance=0.09340 days. Other conjunction relative phase=0.47011, linear phase allowance=0.02561. Full correlation matrix minimum eigenvalue=0.0006272. These linear allowances are descriptive, not calibrated significance. Near Gaia reference the projected epoch offset=-0.04978 days, period-projection allowance alone=0.00112 days (ignores fit covariance/model systematics). Mass function=0.089806 solar masses; adopted primary mass=1.06, minimum secondary mass=0.637. Approximate central duration=4.87 hours versus observed median=3.82 hours. TIC radius, edge-on geometry and main-sequence secondary assumptions make this a plausibility test, not a fitted physical characterization. Impact parameter can shorten duration. Agreement does not by itself establish ownership.

**Deciding limitation:** Twenty-one deep events recur; nineteen shallower secondary fits at phase 0.50006 distinguish eclipse kinds. No capable Gaia neighbor within 60 arcsec.

**Next check:** Optional resolved photometry and spectroscopy for improved localization and physical parameters.

Shared catalogue results are in [../../shared-catalogues/coverage-matrix.csv](../../campaign/shared-catalogues/coverage-matrix.csv). Successful no-matches are distinct from failed queries; no exhaustive priority claim is made. TIC 295771108 is a known exact ASAS-SN EA recovery.

| Sector | Search cycle | Measured BTJD | Formal error d | Input allowance d | Depth ppt | Status |
|---|---:|---:|---:|---:|---:|---|
| 28 | 0 | 2063.4913360 | 0.000683353 | 0.00347229 | 204.63 | used |
| 28 | 1 | 2066.6299949 | 0.000479729 | 0.00347229 | 208.19 | used |
| 28 | 2 | 2069.7683520 | 0.000408709 | 0.00347229 | 203.07 | used |
| 28 | 3 | 2072.9013610 | 0.00326028 | 0.00347229 | 208.68 | used |
| 28 | 4 | 2076.0459376 | 0.000609328 | 0.00347229 | 201.01 | used |
| 28 | 5 | 2079.1848453 | 0.000345642 | 0.00347229 | 206.91 | used |
| 28 | 6 | 2082.3238183 | 0.00039525 | 0.00347229 | 203.69 | used |
| 68 | 348 | 3155.7945700 | 0.000287064 | 0.00115743 | 211.08 | used |
| 68 | 349 | 3158.9327084 | 0.000179889 | 0.00115743 | 206.84 | used |
| 68 | 350 | 3162.0717640 | 0.000175358 | 0.00115743 | 206.85 | used |
| 68 | 351 | 3165.2102760 | 0.000242832 | 0.00115743 | 205.94 | used |
| 68 | 353 | 3171.4878038 | 0.000182 | 0.00115743 | 208.00 | used |
| 68 | 354 | 3174.6260857 | 0.000334604 | 0.00115743 | 202.87 | used |
| 68 | 355 | 3177.7654193 | 0.000194385 | 0.00115743 | 210.57 | used |
| 92 | 555 | 3805.5257811 | 0.000255913 | 0.00115752 | 202.71 | used |
| 92 | 556 | 3808.6643363 | 0.000259275 | 0.00115752 | 204.10 | used |
| 92 | 557 | 3811.8031678 | 0.000368917 | 0.00115752 | 200.32 | used |
| 92 | 559 | 3818.0808595 | 0.000322586 | 0.00115752 | 203.57 | used |
| 92 | 560 | 3821.2197113 | 0.000309955 | 0.00115752 | 201.29 | used |
| 92 | 561 | 3824.3585864 | 0.000328223 | 0.00115752 | 200.65 | used |
| 92 | 562 | 3827.4971159 | 0.000284624 | 0.00115752 | 202.10 | used |

Evidence: [measurements.json](../../campaign/batch04/206538272/measurements.json), [raw-windows.csv](../../campaign/batch04/206538272/raw-windows.csv), [raw-events.png](../../campaign/batch04/206538272/raw-events.png), [fresh-pixels/diff_fresh.json](../../campaign/batch04/206538272/fresh-pixels/diff_fresh.json)/png, historical originals, [../identity-check.json](../../campaign/batch04/identity-check.json), [../alias-audit.json](../../campaign/batch04/alias-audit.json), [../secondary-measurements.json](../../campaign/batch04/secondary-measurements.json), [../secondary-phase-scan.json](../../campaign/batch04/secondary-phase-scan.json)/png, [../gaia-geometry.json](../../campaign/batch04/gaia-geometry.json), [../terra-pixel-audit.json](../../campaign/batch04/terra-pixel-audit.json) and [../helper-audit.md](../../campaign/batch04/helper-audit.md). Exact sources and outputs are covered by [../SHA256SUMS.json](../../campaign/batch04/SHA256SUMS.json). The methods snapshot freezes the read methods without hashing a mutable canonical page.


Stable review key: R571.

Deciding evidence and numeric artifacts:
- [fresh-pixels/diff_fresh.json](../../campaign/batch04/206538272/fresh-pixels/diff_fresh.json)
- [fresh-pixels/diff_fresh.png](../../campaign/batch04/206538272/fresh-pixels/diff_fresh.png)
- [fresh-pixels/gaia.json](../../campaign/batch04/206538272/fresh-pixels/gaia.json)
- [fresh-pixels/run.log](../../campaign/batch04/206538272/fresh-pixels/run.log)
- [historical/diff_s28.json](../../campaign/batch04/206538272/historical/diff_s28.json)
- [historical/diff_s28.png](../../campaign/batch04/206538272/historical/diff_s28.png)
- [historical/gaia.json](../../campaign/batch04/206538272/historical/gaia.json)
- [measurements.json](../../campaign/batch04/206538272/measurements.json)
- [raw-events.png](../../campaign/batch04/206538272/raw-events.png)
- [raw-windows.csv](../../campaign/batch04/206538272/raw-windows.csv)

[Batch audits and scripts](../../campaign/batch04/INDEX.md). [Depth correction provenance](../../campaign/depth-audit/README.md).
