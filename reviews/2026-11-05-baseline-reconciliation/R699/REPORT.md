# TIC 230130556 — PROBABLE

Bounded full physical review: **COMPLETE**. Review ID R699. Ten-target sealed queue position 2 is an operational order, not a scientific rank. Physical outcome is **PROBABLE**: repeated raw SAP eclipses, the same-kind cycle count, and a separate reduction of the same pixels are secure. A capable Gaia neighbor or Gaia-orbit mismatch remains unresolved. A matching eclipsing-binary entry for this exact TIC appears in IJspeert et al. (2024), so this is a known recovery in the queried catalogue scope. Catalogue evidence is in `batch-shared/../remaining_cached/catalogue-recovery-late/coverage-matrix.csv`; physical and novelty statuses are separate.

## Raw SAP events and timing

The sealed snapshot maps TIC 230130556 to Gaia DR3 1650036657422885504 and 38 QLP FITS receipts. `measure_raw.py` verified every FITS SHA-256 before fitting quality-zero raw `SAP_FLUX` with free-center trapezoids. Fitted model amplitude and realized central depth are separate in `measurements.json`; the median realized depth of timing-usable events is 14.35 ppt. The screen period/epoch only located windows. The same-kind fit uses 38 usable centers spanning cycles 0–86, including an adjacent-cycle anchor. It yields P = 22.258902273 ± 0.000019196 d, reference epoch BTJD 1732.51398855 ± 0.00136106 d at cycle 0; reduced χ² = 1.17. Errors are weighted fit covariance with individual max(formal center covariance, half cadence) and scatter inflation if χ² > 1. They exclude model, pipeline, source and long-term systematics; they are not total ephemeris uncertainty. The named epoch is the selected eclipse kind, not an assumed primary.

| Sector | same-kind cycle | mid BTJD | center error d | realized depth ppt |
|---|---|---|---|---|
| 15 | 0 | 1732.51325 | 0.010417 | 14.81 |
| 16 | 1 | 1754.77221 | 0.010417 | 14.47 |
| 56 | 50 | 2845.45827 | 0.001157 | 13.92 |
| 86 | 86 | 3646.78128 | 0.001157 | 14.12 |

Representative raw panels and all retained/excluded fits are in `raw-events.png` and `measurements.json`. 

Actual quality-zero main windows with bilateral sidebands (38 clean sampled) and opposite half-phase windows (37 clean sampled) are in `batch-shared/coverage-alias.json`. Incomplete or flagged windows are not nulls. The adjacent-cycle pair fixes the integer count between separated events; the opposite-phase sampled losses test P/2 and are not counted as same-kind cycles. Representative coverage (local robust scatter shown for main windows):

| Sector | cycle | core quality-0 | main deficit ppt | OOT scatter ppt |
|---|---|---|---|---|
| 15 | 0 | 13 | 14.64 | 0.50 |
| 56 | 50 | 113 | 14.21 | 1.44 |
| 86 | 86 | 113 | 14.07 | 1.55 |

| Sector | cycle | core quality-0 | opposite deficit ppt |
|---|---|---|---|
| 15 | -1 | 13 | 0.14 |
| 56 | 49 | 113 | 0.63 |
| 86 | 86 | 113 | -0.70 |


## Source attribution and alternate extraction

The helper's representative sector 20 QLP aperture products show KSPSAP_FLUX_SML 14.10 ppt; KSPSAP_FLUX 14.72 ppt; KSPSAP_FLUX_LAG 15.14 ppt These repeat the event in different QLP apertures but are not independent pipeline evidence. A separately extracted background-subtracted TESScut light curve in sector 20 has 1×1/3×3/5×5 aperture losses of 13.24/13.54/13.30 ppt and a positive difference-centroid offset of 0.092 pixel from the target (descriptive, not a calibrated localization likelihood). The 60-arcsec Gaia neighbor cone is documented in `batch-shared/helper-pixels/gaia-all.raw` with its hash receipt. Its optimistic capability test compares a neighbor's **intrinsic** eclipse fraction to the minimum measured QLP or custom-aperture loss (13.16 ppt); G-band and unit throughput are proxies, and a positive offset alone is not a calibrated exclusion.

| Gaia DR3 source | sep arcsec | G | minimum intrinsic eclipse % |
|---|---|---|---|
| 1650036657422884992 | 23.88 | 14.58 | 30.3 |


## Gaia geometry and outcome

Gaia's SB1 orbit has P = 22.24496215 ± 0.02368029 d, e = 0.3243, ω = 305.22°, and primary-velocity mass function 0.0037 solar masses. The selected eclipse period minus Gaia's is 0.01394 d. Closest edge-on conjunction A is 0.6378 d (0.0287 phase) from the measured epoch; source-specific Gaia full-covariance linear propagation gives 1.3352 d at that epoch. `batch-shared/gaia-geometry.json` retains both conjunctions and covariance order. This comparison is descriptive, not a calibrated orbit-ownership probability. Eclipse durations and depths are stellar-eclipse compatible in a roughly 20–24 d orbit, without fitted stellar masses/radii.

**Limitations:** A custom TESScut aperture of the same TESS photons reproduces the deficit, but it is not an independent observing occasion. 1 Gaia DR3 neighbor(s) within 60 arcsec pass an optimistic G-band/full-throughput capability screen; the target-centered difference image does not conclusively resolve source ownership at TESS pixel scale.

**Next decisive check:** Obtain higher-resolution photometry during a predicted eclipse to resolve the Gaia neighbors, then compare the eclipse clock with an updated radial-velocity orbit.
