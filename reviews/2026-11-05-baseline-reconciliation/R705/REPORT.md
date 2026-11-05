# TIC 431996459 — PROBABLE

Bounded full physical review: **COMPLETE**. Review ID R705. Ten-target sealed queue position 8 is an operational order, not a scientific rank. Physical outcome is **PROBABLE**: repeated raw SAP eclipses, the same-kind cycle count, and a separate reduction of the same pixels are secure. A capable Gaia neighbor or Gaia-orbit mismatch remains unresolved. A matching eclipsing-binary entry for this exact TIC appears in IJspeert et al. (2024), so this is a known recovery in the queried catalogue scope. Catalogue evidence is in `batch-shared/../remaining_cached/catalogue-recovery-late/coverage-matrix.csv`; physical and novelty statuses are separate.

## Raw SAP events and timing

The sealed snapshot maps TIC 431996459 to Gaia DR3 5714824595764475520 and 4 QLP FITS receipts. `measure_raw.py` verified every FITS SHA-256 before fitting quality-zero raw `SAP_FLUX` with free-center trapezoids. Fitted model amplitude and realized central depth are separate in `measurements.json`; the median realized depth of timing-usable events is 51.36 ppt. The screen period/epoch only located windows. The same-kind fit uses 4 usable centers spanning cycles 0–93, including an adjacent-cycle anchor. It yields P = 23.873538742 ± 0.000051947 d, reference epoch BTJD 1494.73997534 ± 0.00467791 d at cycle 0; reduced χ² = 0.40. Errors are weighted fit covariance with individual max(formal center covariance, half cadence) and scatter inflation if χ² > 1. They exclude model, pipeline, source and long-term systematics; they are not total ephemeris uncertainty. The named epoch is the selected eclipse kind, not an assumed primary.

| Sector | same-kind cycle | mid BTJD | center error d | realized depth ppt |
|---|---|---|---|---|
| 7 | 0 | 1494.73885 | 0.010417 | 51.01 |
| 88 | 92 | 3691.10480 | 0.001157 | 51.55 |
| 88 | 93 | 3714.97979 | 0.001157 | 51.17 |

Representative raw panels and all retained/excluded fits are in `raw-events.png` and `measurements.json`. 

Actual quality-zero main windows with bilateral sidebands (4 clean sampled) and opposite half-phase windows (4 clean sampled) are in `batch-shared/coverage-alias.json`. Incomplete or flagged windows are not nulls. The adjacent-cycle pair fixes the integer count between separated events; the opposite-phase sampled losses test P/2 and are not counted as same-kind cycles. Representative coverage (local robust scatter shown for main windows):

| Sector | cycle | core quality-0 | main deficit ppt | OOT scatter ppt |
|---|---|---|---|---|
| 7 | 0 | 11 | 51.86 | 0.73 |
| 88 | 92 | 111 | 52.67 | 2.36 |
| 88 | 93 | 113 | 52.13 | 2.01 |

| Sector | cycle | core quality-0 | opposite deficit ppt |
|---|---|---|---|
| 7 | 0 | 12 | 0.25 |
| 61 | 62 | 113 | -0.38 |
| 88 | 92 | 104 | 0.28 |


## Source attribution and alternate extraction

The helper's representative sector 7 QLP aperture products show KSPSAP_FLUX_SML 49.40 ppt; KSPSAP_FLUX 51.20 ppt; KSPSAP_FLUX_LAG 52.24 ppt These repeat the event in different QLP apertures but are not independent pipeline evidence. A separately extracted background-subtracted TESScut light curve in sector 7 has 1×1/3×3/5×5 aperture losses of 52.94/52.85/49.30 ppt and a positive difference-centroid offset of 0.137 pixel from the target (descriptive, not a calibrated localization likelihood). The 60-arcsec Gaia neighbor cone is documented in `batch-shared/helper-pixels/gaia-all.raw` with its hash receipt. Its optimistic capability test compares a neighbor's **intrinsic** eclipse fraction to the minimum measured QLP or custom-aperture loss (49.30 ppt); G-band and unit throughput are proxies, and a positive offset alone is not a calibrated exclusion.

| Gaia DR3 source | sep arcsec | G | minimum intrinsic eclipse % |
|---|---|---|---|
| 5714824492689613568 | 54.18 | 13.00 | 25.1 |


## Gaia geometry and outcome

Gaia's SB1 orbit has P = 23.86560768 ± 0.01272228 d, e = 0.3453, ω = 208.75°, and primary-velocity mass function 0.0474 solar masses. The selected eclipse period minus Gaia's is 0.00793 d. Closest edge-on conjunction A is 0.7238 d (0.0303 phase) from the measured epoch; source-specific Gaia full-covariance linear propagation gives 0.7274 d at that epoch. `batch-shared/gaia-geometry.json` retains both conjunctions and covariance order. This comparison is descriptive, not a calibrated orbit-ownership probability. Eclipse durations and depths are stellar-eclipse compatible in a roughly 20–24 d orbit, without fitted stellar masses/radii.

**Limitations:** A custom TESScut aperture of the same TESS photons reproduces the deficit, but it is not an independent observing occasion. 1 Gaia DR3 neighbor(s) within 60 arcsec pass an optimistic G-band/full-throughput capability screen; the target-centered difference image does not conclusively resolve source ownership at TESS pixel scale.

**Next decisive check:** Obtain higher-resolution photometry during a predicted eclipse to resolve the Gaia neighbors, then compare the eclipse clock with an updated radial-velocity orbit.
