# TIC 343452418 — PROBABLE

Bounded full physical review: **COMPLETE**. Review ID R702. Ten-target sealed queue position 5 is an operational order, not a scientific rank. Physical outcome is **PROBABLE**: repeated raw SAP eclipses, the same-kind cycle count, and a separate reduction of the same pixels are secure. A capable Gaia neighbor or Gaia-orbit mismatch remains unresolved. A matching eclipsing-binary entry for this exact TIC appears in IJspeert et al. (2024), so this is a known recovery in the queried catalogue scope. Catalogue evidence is in `batch-shared/../remaining_cached/catalogue-recovery-late/coverage-matrix.csv`; physical and novelty statuses are separate.

## Raw SAP events and timing

The sealed snapshot maps TIC 343452418 to Gaia DR3 5803519896675623552 and 9 QLP FITS receipts. `measure_raw.py` verified every FITS SHA-256 before fitting quality-zero raw `SAP_FLUX` with free-center trapezoids. Fitted model amplitude and realized central depth are separate in `measurements.json`; the median realized depth of timing-usable events is 56.16 ppt. The screen period/epoch only located windows. The same-kind fit uses 9 usable centers spanning cycles 0–121, including an adjacent-cycle anchor. It yields P = 20.819273044 ± 0.000022017 d, reference epoch BTJD 1630.88476252 ± 0.00236939 d at cycle 0; reduced χ² = 0.28. Errors are weighted fit covariance with individual max(formal center covariance, half cadence) and scatter inflation if χ² > 1. They exclude model, pipeline, source and long-term systematics; they are not total ephemeris uncertainty. The named epoch is the selected eclipse kind, not an assumed primary.

| Sector | same-kind cycle | mid BTJD | center error d | realized depth ppt |
|---|---|---|---|---|
| 12 | 0 | 1630.87861 | 0.010417 | 56.16 |
| 12 | 1 | 1651.70233 | 0.010417 | 55.55 |
| 66 | 71 | 3109.05350 | 0.001157 | 59.94 |
| 102 | 121 | 4150.01607 | 0.001157 | 53.13 |

Representative raw panels and all retained/excluded fits are in `raw-events.png` and `measurements.json`. 

Actual quality-zero main windows with bilateral sidebands (8 clean sampled) and opposite half-phase windows (8 clean sampled) are in `batch-shared/coverage-alias.json`. Incomplete or flagged windows are not nulls. The adjacent-cycle pair fixes the integer count between separated events; the opposite-phase sampled losses test P/2 and are not counted as same-kind cycles. Representative coverage (local robust scatter shown for main windows):

| Sector | cycle | core quality-0 | main deficit ppt | OOT scatter ppt |
|---|---|---|---|---|
| 12 | 1 | 9 | 54.26 | 0.40 |
| 93 | 106 | 77 | 56.70 | 1.75 |
| 102 | 121 | 76 | 51.01 | 1.05 |

| Sector | cycle | core quality-0 | opposite deficit ppt |
|---|---|---|---|
| 13 | 1 | 9 | 0.55 |
| 93 | 106 | 77 | 0.32 |
| 103 | 121 | 78 | -0.16 |


## Source attribution and alternate extraction

The helper's representative sector 13 QLP aperture products show KSPSAP_FLUX_SML 52.87 ppt; KSPSAP_FLUX 55.33 ppt; KSPSAP_FLUX_LAG 56.67 ppt These repeat the event in different QLP apertures but are not independent pipeline evidence. A separately extracted background-subtracted TESScut light curve in sector 13 has 1×1/3×3/5×5 aperture losses of 52.01/51.48/50.69 ppt and a positive difference-centroid offset of 0.115 pixel from the target (descriptive, not a calibrated localization likelihood). The 60-arcsec Gaia neighbor cone is documented in `batch-shared/helper-pixels/gaia-all.raw` with its hash receipt. Its optimistic capability test compares a neighbor's **intrinsic** eclipse fraction to the minimum measured QLP or custom-aperture loss (49.77 ppt); G-band and unit throughput are proxies, and a positive offset alone is not a calibrated exclusion.

| Gaia DR3 source | sep arcsec | G | minimum intrinsic eclipse % |
|---|---|---|---|
| 5803519931035360768 | 27.79 | 14.11 | 71.4 |


## Gaia geometry and outcome

Gaia's SB1 orbit has P = 20.83626670 ± 0.00923000 d, e = 0.3427, ω = 312.77°, and primary-velocity mass function 0.0360 solar masses. The selected eclipse period minus Gaia's is -0.01699 d. Closest edge-on conjunction B is -0.9980 d (-0.0479 phase) from the measured epoch; source-specific Gaia full-covariance linear propagation gives 0.7078 d at that epoch. `batch-shared/gaia-geometry.json` retains both conjunctions and covariance order. This comparison is descriptive, not a calibrated orbit-ownership probability. Eclipse durations and depths are stellar-eclipse compatible in a roughly 20–24 d orbit, without fitted stellar masses/radii.

**Limitations:** A custom TESScut aperture of the same TESS photons reproduces the deficit, but it is not an independent observing occasion. 1 Gaia DR3 neighbor(s) within 60 arcsec pass an optimistic G-band/full-throughput capability screen; the target-centered difference image does not conclusively resolve source ownership at TESS pixel scale.

**Next decisive check:** Obtain higher-resolution photometry during a predicted eclipse to resolve the Gaia neighbors, then compare the eclipse clock with an updated radial-velocity orbit.
