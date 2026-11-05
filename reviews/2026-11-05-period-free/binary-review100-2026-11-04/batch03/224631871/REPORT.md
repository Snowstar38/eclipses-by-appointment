# H023 — TIC 224631871

Physical verdict: **PROBABLE**. Bounded review: **COMPLETE**. Catalogue novelty: **UNKNOWN**; four scoped VizieR gates were unavailable after a positive-control timeout. A primary-table nonmatch is not novelty clearance.

Gaia DR3 source 1842411541148621312, SB1 period 45.00439 d. Frozen stratum `cross_method_dip`; sample ID is not a new-system acceptance. Quality-zero raw SAP sectors inspected: 14, 15, 41, 55, 82.

## Deciding evidence

Deeper eclipses in s14/s55/s82 have fitted centers BTJD 1699.9899, 2821.7915, 3539.7622 and a 41-cycle 44.87246 d clock with fitted epoch/intercept 1699.9871; shallower events in s15/s82 give ~44.8718 d. Their ~15.94 d separation agrees with the ~15.92 d Gaia eccentric-orbit conjunction separation. Independent TESSCut s55 aperture recovers ~16.7 ppt and difference centroid is 0.07 pixel from target.

## Limits and next check

The photometric period is 2.85 marginal Gaia period errors shorter than 45.00439 d, with ~2.9 d absolute phase drift at s14; orbital covariance is unavailable. Gaia neighbors at 13.5 and 19.4 arcsec are flux-capable and close enough to limit attribution despite the centroid favoring target. TESSCut shares photons with SAP; no calibrated period error. Deblend the close neighbors with high-resolution or simultaneous pixel photometry and test a new eclipse against both clocks.

## Reproducibility

`raw-inspection.json` verifies original bulk-result and FITS SHA-256 values and tabulates representative screening windows. `raw-windows.png` shows these raw windows; `orbit-context.json` and `.png` show full cached-sector SAP and Gaia edge-on conjunction predictions. Screening/conjunction times are not measured event centers. The frozen [source packet](../../source-packets/224631871/sources.json), [central novelty evidence](../../shared-catalogues/target-evidence.json), batch scripts and SHA256SUMS.json preserve receipts.

`local-fits.json` and `event-clock.json` preserve fitted centers, distinct eclipse kinds, conditional integer cycles, Gaia comparison and model limitations. [Independent pixel attribution](../helper-source-attribution.json) has Gaia/WCS neighbor positions, aperture extraction and difference image; the separate `lead-pixels` cutouts are retained with hashes.
