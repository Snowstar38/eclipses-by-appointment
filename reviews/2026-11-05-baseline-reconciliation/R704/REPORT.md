# TIC 36721228 — CONFIRMED

Bounded full physical review: **COMPLETE**. Review ID R704. Ten-target sealed queue position 7 is an operational order, not a scientific rank. Physical outcome is **CONFIRMED**: repeated raw SAP eclipses, the same-kind cycle count, and a separate reduction of the same pixels are secure. The deciding pixel, neighbor and Gaia checks available here are compatible with the target/orbit assignment. A matching eclipsing-binary entry for this exact TIC appears in IJspeert et al. (2024), so this is a known recovery in the queried catalogue scope. Catalogue evidence is in `batch-shared/../remaining_cached/catalogue-recovery-late/coverage-matrix.csv`; physical and novelty statuses are separate.

## Raw SAP events and timing

The sealed snapshot maps TIC 36721228 to Gaia DR3 5414761825234703872 and 7 QLP FITS receipts. `measure_raw.py` verified every FITS SHA-256 before fitting quality-zero raw `SAP_FLUX` with free-center trapezoids. Fitted model amplitude and realized central depth are separate in `measurements.json`; the median realized depth of timing-usable events is 29.17 ppt. The screen period/epoch only located windows. The same-kind fit uses 6 usable centers spanning cycles 70–108, including an adjacent-cycle anchor. It yields P = 20.540391984 ± 0.000026224 d, reference epoch BTJD 2990.13719265 ± 0.00068668 d at cycle 70; reduced χ² = 0.12. Errors are weighted fit covariance with individual max(formal center covariance, half cadence) and scatter inflation if χ² > 1. They exclude model, pipeline, source and long-term systematics; they are not total ephemeris uncertainty. The named epoch is the selected eclipse kind, not an assumed primary.

| Sector | same-kind cycle | mid BTJD | center error d | realized depth ppt |
|---|---|---|---|---|
| 62 | 70 | 2990.13730 | 0.001157 | 29.28 |
| 62 | 71 | 3010.67789 | 0.001157 | 29.20 |
| 89 | 106 | 3729.59140 | 0.001157 | 28.74 |
| 90 | 108 | 3770.67166 | 0.001157 | 28.80 |

Representative raw panels and all retained/excluded fits are in `raw-events.png` and `measurements.json`. 

Actual quality-zero main windows with bilateral sidebands (6 clean sampled) and opposite half-phase windows (7 clean sampled) are in `batch-shared/coverage-alias.json`. Incomplete or flagged windows are not nulls. The adjacent-cycle pair fixes the integer count between separated events; the opposite-phase sampled losses test P/2 and are not counted as same-kind cycles. Representative coverage (local robust scatter shown for main windows):

| Sector | cycle | core quality-0 | main deficit ppt | OOT scatter ppt |
|---|---|---|---|---|
| 62 | 0 | 78 | 23.39 | 1.45 |
| 89 | 36 | 78 | 22.24 | 1.29 |
| 90 | 38 | 78 | 22.25 | 1.17 |

| Sector | cycle | core quality-0 | opposite deficit ppt |
|---|---|---|---|
| 9 | -70 | 9 | 0.16 |
| 63 | 1 | 78 | -0.07 |
| 99 | 52 | 78 | -0.05 |


## Source attribution and alternate extraction

The helper's representative sector 63 QLP aperture products show No QLP aperture variants in this file. These repeat the event in different QLP apertures but are not independent pipeline evidence. A separately extracted background-subtracted TESScut light curve in sector 63 has 1×1/3×3/5×5 aperture losses of 25.52/26.05/25.93 ppt and a positive difference-centroid offset of 0.192 pixel from the target (descriptive, not a calibrated localization likelihood). The 60-arcsec Gaia neighbor cone is documented in `batch-shared/helper-pixels/gaia-all.raw` with its hash receipt. Its optimistic capability test compares a neighbor's **intrinsic** eclipse fraction to the minimum measured QLP or custom-aperture loss (25.52 ppt); G-band and unit throughput are proxies, and a positive offset alone is not a calibrated exclusion.

No Gaia G-measured neighbor passed the optimistic capability test within 60 arcsec.

## Gaia geometry and outcome

Gaia's SB1 orbit has P = 20.54741671 ± 0.00710951 d, e = 0.1297, ω = 41.58°, and primary-velocity mass function 0.1534 solar masses. The selected eclipse period minus Gaia's is -0.00702 d. Closest edge-on conjunction A is -0.4396 d (-0.0214 phase) from the measured epoch; source-specific Gaia full-covariance linear propagation gives 0.8508 d at that epoch. `batch-shared/gaia-geometry.json` retains both conjunctions and covariance order. This comparison is descriptive, not a calibrated orbit-ownership probability. Eclipse durations and depths are stellar-eclipse compatible in a roughly 20–24 d orbit, without fitted stellar masses/radii.

**Limitations:** A custom TESScut aperture of the same TESS photons reproduces the deficit, but it is not an independent observing occasion.

**Next decisive check:** Acquire a clean future eclipse to refine the ephemeris and check long-term stability.
