# TIC 121277143 — PROBABLE

Bounded full physical review: **COMPLETE**. Review ID R706. Ten-target sealed queue position 9 is an operational order, not a scientific rank. Physical outcome is **PROBABLE**: repeated raw SAP eclipses, the same-kind cycle count, and a separate reduction of the same pixels are secure. A capable Gaia neighbor or Gaia-orbit mismatch remains unresolved. The completed scoped catalogue checks identify no prior eclipsing-binary entry for this exact target, but ASAS-SN has an exact ROT variable counterpart (period 726.95 d); this is not an EB classification. Novelty is provisionally unclaimed pending root acceptance and attribution follow-up. Catalogue evidence is in `batch-shared/../remaining_cached/catalogue-recovery-late/coverage-matrix.csv`; physical and novelty statuses are separate.

## Raw SAP events and timing

The sealed snapshot maps TIC 121277143 to Gaia DR3 2099147746755032448 and 8 QLP FITS receipts. `measure_raw.py` verified every FITS SHA-256 before fitting quality-zero raw `SAP_FLUX` with free-center trapezoids. Fitted model amplitude and realized central depth are separate in `measurements.json`; the median realized depth of timing-usable events is 7.43 ppt. The screen period/epoch only located windows. The same-kind fit uses 5 usable centers spanning cycles 0–85, including an adjacent-cycle anchor. It yields P = 21.513055420 ± 0.000087569 d, reference epoch BTJD 1687.23363839 ± 0.00710400 d at cycle 0; reduced χ² = 1.28. Errors are weighted fit covariance with individual max(formal center covariance, half cadence) and scatter inflation if χ² > 1. They exclude model, pipeline, source and long-term systematics; they are not total ephemeris uncertainty. The named epoch is the selected eclipse kind, not an assumed primary.

| Sector | same-kind cycle | mid BTJD | center error d | realized depth ppt |
|---|---|---|---|---|
| 14 | 0 | 1687.22795 | 0.010417 | 5.52 |
| 74 | 76 | 3322.22756 | 0.001346 | 7.43 |
| 80 | 84 | 3494.33073 | 0.001157 | 7.87 |
| 81 | 85 | 3515.84189 | 0.001157 | 8.13 |

Representative raw panels and all retained/excluded fits are in `raw-events.png` and `measurements.json`. The 3 fitted but timing-excluded windows remain recorded.

Actual quality-zero main windows with bilateral sidebands (7 clean sampled) and opposite half-phase windows (10 clean sampled) are in `batch-shared/coverage-alias.json`. Incomplete or flagged windows are not nulls. The adjacent-cycle pair fixes the integer count between separated events; the opposite-phase sampled losses test P/2 and are not counted as same-kind cycles. Representative coverage (local robust scatter shown for main windows):

| Sector | cycle | core quality-0 | main deficit ppt | OOT scatter ppt |
|---|---|---|---|---|
| 14 | 0 | 6 | 5.21 | 0.49 |
| 54 | 51 | 18 | 6.46 | 0.56 |
| 81 | 85 | 52 | 7.19 | 0.93 |

| Sector | cycle | core quality-0 | opposite deficit ppt |
|---|---|---|---|
| 14 | 0 | 3 | 0.23 |
| 54 | 51 | 17 | 0.40 |
| 81 | 85 | 52 | 0.01 |


## Source attribution and alternate extraction

The helper's representative sector 54 QLP aperture products show KSPSAP_FLUX_SML 5.80 ppt; KSPSAP_FLUX 6.25 ppt; KSPSAP_FLUX_LAG 6.54 ppt These repeat the event in different QLP apertures but are not independent pipeline evidence. A separately extracted background-subtracted TESScut light curve in sector 54 has 1×1/3×3/5×5 aperture losses of 5.67/6.20/6.12 ppt and a positive difference-centroid offset of 0.238 pixel from the target (descriptive, not a calibrated localization likelihood). The 60-arcsec Gaia neighbor cone is documented in `batch-shared/helper-pixels/gaia-all.raw` with its hash receipt. Its optimistic capability test compares a neighbor's **intrinsic** eclipse fraction to the minimum measured QLP or custom-aperture loss (5.67 ppt); G-band and unit throughput are proxies, and a positive offset alone is not a calibrated exclusion.

| Gaia DR3 source | sep arcsec | G | minimum intrinsic eclipse % |
|---|---|---|---|
| 2099147781115007616 | 34.55 | 16.18 | 97.5 |


## Gaia geometry and outcome

Gaia's SB1 orbit has P = 21.51476028 ± 0.00622134 d, e = 0.4265, ω = 133.54°, and primary-velocity mass function 0.0247 solar masses. The selected eclipse period minus Gaia's is -0.00170 d. Closest edge-on conjunction A is -0.4742 d (-0.0220 phase) from the measured epoch; source-specific Gaia full-covariance linear propagation gives 0.4185 d at that epoch. `batch-shared/gaia-geometry.json` retains both conjunctions and covariance order. This comparison is descriptive, not a calibrated orbit-ownership probability. Eclipse durations and depths are stellar-eclipse compatible in a roughly 20–24 d orbit, without fitted stellar masses/radii.

**Limitations:** A custom TESScut aperture of the same TESS photons reproduces the deficit, but it is not an independent observing occasion. 1 Gaia DR3 neighbor(s) within 60 arcsec pass an optimistic G-band/full-throughput capability screen; the target-centered difference image does not conclusively resolve source ownership at TESS pixel scale. Sector 40 lacks egress and sector 53 has broad baseline modulation; both are retained as detections but excluded from center timing.

**Next decisive check:** Obtain higher-resolution photometry during a predicted eclipse to resolve the Gaia neighbors, then compare the eclipse clock with an updated radial-velocity orbit.
