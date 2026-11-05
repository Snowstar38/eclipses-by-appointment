# TIC 207780183 — PROBABLE

Bounded full physical review: **COMPLETE**. Review ID R703. Ten-target sealed queue position 6 is an operational order, not a scientific rank. Physical outcome is **PROBABLE**: repeated raw SAP eclipses, the same-kind cycle count, and a separate reduction of the same pixels are secure. A capable Gaia neighbor or Gaia-orbit mismatch remains unresolved. A matching eclipsing-binary entry for this exact TIC appears in IJspeert et al. (2024), so this is a known recovery in the queried catalogue scope. Catalogue evidence is in `batch-shared/../remaining_cached/catalogue-recovery-late/coverage-matrix.csv`; physical and novelty statuses are separate.

## Raw SAP events and timing

The sealed snapshot maps TIC 207780183 to Gaia DR3 6064737986576373504 and 7 QLP FITS receipts. `measure_raw.py` verified every FITS SHA-256 before fitting quality-zero raw `SAP_FLUX` with free-center trapezoids. Fitted model amplitude and realized central depth are separate in `measurements.json`; the median realized depth of timing-usable events is 80.96 ppt. The screen period/epoch only located windows. The same-kind fit uses 5 usable centers spanning cycles 0–114, including an adjacent-cycle anchor. It yields P = 21.770614152 ± 0.000025834 d, reference epoch BTJD 1621.05097518 ± 0.00254756 d at cycle 0; reduced χ² = 0.54. Errors are weighted fit covariance with individual max(formal center covariance, half cadence) and scatter inflation if χ² > 1. They exclude model, pipeline, source and long-term systematics; they are not total ephemeris uncertainty. The named epoch is the selected eclipse kind, not an assumed primary.

| Sector | same-kind cycle | mid BTJD | center error d | realized depth ppt |
|---|---|---|---|---|
| 11 | 0 | 1621.04897 | 0.010417 | 80.96 |
| 65 | 67 | 3079.68232 | 0.001157 | 87.35 |
| 100 | 113 | 4081.13133 | 0.001157 | 74.67 |
| 101 | 114 | 4102.89995 | 0.001157 | 74.08 |

Representative raw panels and all retained/excluded fits are in `raw-events.png` and `measurements.json`. 

Actual quality-zero main windows with bilateral sidebands (5 clean sampled) and opposite half-phase windows (5 clean sampled) are in `batch-shared/coverage-alias.json`. Incomplete or flagged windows are not nulls. The adjacent-cycle pair fixes the integer count between separated events; the opposite-phase sampled losses test P/2 and are not counted as same-kind cycles. Representative coverage (local robust scatter shown for main windows):

| Sector | cycle | core quality-0 | main deficit ppt | OOT scatter ppt |
|---|---|---|---|---|
| 11 | 0 | 12 | 68.75 | 0.77 |
| 65 | 67 | 113 | 71.91 | 2.62 |
| 101 | 114 | 112 | 61.76 | 1.50 |

| Sector | cycle | core quality-0 | opposite deficit ppt |
|---|---|---|---|
| 65 | 67 | 97 | 10.56 |
| 99 | 112 | 111 | 5.28 |
| 102 | 115 | 112 | 5.20 |


## Source attribution and alternate extraction

The helper's representative sector 11 QLP aperture products show KSPSAP_FLUX_SML 72.50 ppt; KSPSAP_FLUX 73.93 ppt; KSPSAP_FLUX_LAG 73.57 ppt These repeat the event in different QLP apertures but are not independent pipeline evidence. A separately extracted background-subtracted TESScut light curve in sector 11 has 1×1/3×3/5×5 aperture losses of 78.87/75.33/53.32 ppt and a positive difference-centroid offset of 0.034 pixel from the target (descriptive, not a calibrated localization likelihood). The 60-arcsec Gaia neighbor cone is documented in `batch-shared/helper-pixels/gaia-all.raw` with its hash receipt. Its optimistic capability test compares a neighbor's **intrinsic** eclipse fraction to the minimum measured QLP or custom-aperture loss (53.32 ppt); G-band and unit throughput are proxies, and a positive offset alone is not a calibrated exclusion.

| Gaia DR3 source | sep arcsec | G | minimum intrinsic eclipse % |
|---|---|---|---|
| 6064737913537984256 | 58.21 | 12.64 | 21.6 |
| 6064738192734834432 | 57.14 | 13.39 | 37.8 |


## Gaia geometry and outcome

Gaia's SB1 orbit has P = 21.74952890 ± 0.01828839 d, e = 0.3202, ω = 259.13°, and primary-velocity mass function 0.1048 solar masses. The selected eclipse period minus Gaia's is 0.02109 d. Closest edge-on conjunction B is 1.0414 d (0.0479 phase) from the measured epoch; source-specific Gaia full-covariance linear propagation gives 0.9816 d at that epoch. `batch-shared/gaia-geometry.json` retains both conjunctions and covariance order. This comparison is descriptive, not a calibrated orbit-ownership probability. Eclipse durations and depths are stellar-eclipse compatible in a roughly 20–24 d orbit, without fitted stellar masses/radii.

**Limitations:** A custom TESScut aperture of the same TESS photons reproduces the deficit, but it is not an independent observing occasion. 2 Gaia DR3 neighbor(s) within 60 arcsec pass an optimistic G-band/full-throughput capability screen; the target-centered difference image does not conclusively resolve source ownership at TESS pixel scale. Several opposite-half-phase windows have broad, shallower deficits displaced about 0.20 d from exact half phase; these are a possible eccentric-orbit secondary eclipse, not same-kind timing points.

**Next decisive check:** Obtain higher-resolution photometry during a predicted eclipse to resolve the Gaia neighbors, then compare the eclipse clock with an updated radial-velocity orbit.
