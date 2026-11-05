# TIC 431589019 — PROBABLE

Bounded full physical review: **COMPLETE**. Review ID R707. Ten-target sealed queue position 10 is an operational order, not a scientific rank. Physical outcome is **PROBABLE**: repeated raw SAP eclipses, the same-kind cycle count, and a separate reduction of the same pixels are secure. A capable Gaia neighbor or Gaia-orbit mismatch remains unresolved. A matching eclipsing-binary entry for this exact TIC appears in IJspeert et al. (2024), so this is a known recovery in the queried catalogue scope. Catalogue evidence is in `batch-shared/../remaining_cached/catalogue-recovery-late/coverage-matrix.csv`; physical and novelty statuses are separate.

## Raw SAP events and timing

The sealed snapshot maps TIC 431589019 to Gaia DR3 3239612300010867072 and 3 QLP FITS receipts. `measure_raw.py` verified every FITS SHA-256 before fitting quality-zero raw `SAP_FLUX` with free-center trapezoids. Fitted model amplitude and realized central depth are separate in `measurements.json`; the median realized depth of timing-usable events is 56.94 ppt. The screen period/epoch only located windows. The same-kind fit uses 4 usable centers spanning cycles 0–123, including an adjacent-cycle anchor. It yields P = 20.884141362 ± 0.000029568 d, reference epoch BTJD 1444.90423768 ± 0.00330333 d at cycle 0; reduced χ² = 0.01. Errors are weighted fit covariance with individual max(formal center covariance, half cadence) and scatter inflation if χ² > 1. They exclude model, pipeline, source and long-term systematics; they are not total ephemeris uncertainty. The named epoch is the selected eclipse kind, not an assumed primary.

| Sector | same-kind cycle | mid BTJD | center error d | realized depth ppt |
|---|---|---|---|---|
| 5 | 0 | 1444.90281 | 0.010417 | 54.64 |
| 32 | 35 | 2175.84917 | 0.003472 | 61.76 |
| 32 | 36 | 2196.73356 | 0.003472 | 59.24 |
| 98 | 123 | 4013.65362 | 0.001157 | 51.99 |

Representative raw panels and all retained/excluded fits are in `raw-events.png` and `measurements.json`. 

Actual quality-zero main windows with bilateral sidebands (4 clean sampled) and opposite half-phase windows (2 clean sampled) are in `batch-shared/coverage-alias.json`. Incomplete or flagged windows are not nulls. The adjacent-cycle pair fixes the integer count between separated events; the opposite-phase sampled losses test P/2 and are not counted as same-kind cycles. Representative coverage (local robust scatter shown for main windows):

| Sector | cycle | core quality-0 | main deficit ppt | OOT scatter ppt |
|---|---|---|---|---|
| 5 | 0 | 6 | 51.23 | 1.24 |
| 32 | 36 | 15 | 51.59 | 2.25 |
| 98 | 123 | 52 | 44.72 | 1.35 |

| Sector | cycle | core quality-0 | opposite deficit ppt |
|---|---|---|---|
| 5 | 0 | 6 | -3.29 |
| 98 | 124 | 22 | 0.51 |


## Source attribution and alternate extraction

The helper's representative sector 5 QLP aperture products show KSPSAP_FLUX_SML 53.05 ppt; KSPSAP_FLUX 55.47 ppt; KSPSAP_FLUX_LAG 56.28 ppt These repeat the event in different QLP apertures but are not independent pipeline evidence. A separately extracted background-subtracted TESScut light curve in sector 5 has 1×1/3×3/5×5 aperture losses of 44.96/28.37/17.14 ppt and a positive difference-centroid offset of 0.090 pixel from the target (descriptive, not a calibrated localization likelihood). The 60-arcsec Gaia neighbor cone is documented in `batch-shared/helper-pixels/gaia-all.raw` with its hash receipt. Its optimistic capability test compares a neighbor's **intrinsic** eclipse fraction to the minimum measured QLP or custom-aperture loss (17.14 ppt); G-band and unit throughput are proxies, and a positive offset alone is not a calibrated exclusion.

| Gaia DR3 source | sep arcsec | G | minimum intrinsic eclipse % |
|---|---|---|---|
| 3239612609248510592 | 50.40 | 10.84 | 2.7 |
| 3239612609248511616 | 37.25 | 12.26 | 5.5 |


## Gaia geometry and outcome

Gaia's SB1 orbit has P = 20.86707448 ± 0.00892305 d, e = 0.5896, ω = 120.05°, and primary-velocity mass function 0.1296 solar masses. The selected eclipse period minus Gaia's is 0.01707 d. Closest edge-on conjunction A is 0.1868 d (0.0090 phase) from the measured epoch; source-specific Gaia full-covariance linear propagation gives 0.5038 d at that epoch. `batch-shared/gaia-geometry.json` retains both conjunctions and covariance order. This comparison is descriptive, not a calibrated orbit-ownership probability. Eclipse durations and depths are stellar-eclipse compatible in a roughly 20–24 d orbit, without fitted stellar masses/radii.

**Limitations:** A custom TESScut aperture of the same TESS photons reproduces the deficit, but it is not an independent observing occasion. 2 Gaia DR3 neighbor(s) within 60 arcsec pass an optimistic G-band/full-throughput capability screen; the target-centered difference image does not conclusively resolve source ownership at TESS pixel scale. The representative cutout has only four core frames and substantial aperture-dependent dilution amid two bright capable neighbors; target-like difference peak is insufficient for unique attribution.

**Next decisive check:** Obtain higher-resolution photometry during a predicted eclipse to resolve the Gaia neighbors, then compare the eclipse clock with an updated radial-velocity orbit.
