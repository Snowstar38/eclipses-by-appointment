# TIC 174303697 — PROBABLE

Bounded full physical review: **COMPLETE**. Review ID R700. Ten-target sealed queue position 3 is an operational order, not a scientific rank. Physical outcome is **PROBABLE**: repeated raw SAP eclipses, the same-kind cycle count, and a separate reduction of the same pixels are secure. A capable Gaia neighbor or Gaia-orbit mismatch remains unresolved. A matching eclipsing-binary entry for this exact TIC appears in IJspeert et al. (2024), so this is a known recovery in the queried catalogue scope. Catalogue evidence is in `batch-shared/../remaining_cached/catalogue-recovery-late/coverage-matrix.csv`; physical and novelty statuses are separate.

## Raw SAP events and timing

The sealed snapshot maps TIC 174303697 to Gaia DR3 1924017843915357440 and 3 QLP FITS receipts. `measure_raw.py` verified every FITS SHA-256 before fitting quality-zero raw `SAP_FLUX` with free-center trapezoids. Fitted model amplitude and realized central depth are separate in `measurements.json`; the median realized depth of timing-usable events is 179.40 ppt. The screen period/epoch only located windows. The same-kind fit uses 3 usable centers spanning cycles 53–89, including an adjacent-cycle anchor. It yields P = 20.688331458 ± 0.000039918 d, reference epoch BTJD 2855.89089696 ± 0.00083000 d at cycle 53; reduced χ² = 0.06. Errors are weighted fit covariance with individual max(formal center covariance, half cadence) and scatter inflation if χ² > 1. They exclude model, pipeline, source and long-term systematics; they are not total ephemeris uncertainty. The named epoch is the selected eclipse kind, not an assumed primary.

| Sector | same-kind cycle | mid BTJD | center error d | realized depth ppt |
|---|---|---|---|---|
| 57 | 53 | 2855.89071 | 0.001157 | 179.74 |
| 57 | 54 | 2876.57942 | 0.001157 | 179.31 |
| 84 | 89 | 3600.67082 | 0.001157 | 179.40 |

Representative raw panels and all retained/excluded fits are in `raw-events.png` and `measurements.json`. 

Actual quality-zero main windows with bilateral sidebands (3 clean sampled) and opposite half-phase windows (1 clean sampled) are in `batch-shared/coverage-alias.json`. Incomplete or flagged windows are not nulls. The adjacent-cycle pair fixes the integer count between separated events; the opposite-phase sampled losses test P/2 and are not counted as same-kind cycles. Representative coverage (local robust scatter shown for main windows):

| Sector | cycle | core quality-0 | main deficit ppt | OOT scatter ppt |
|---|---|---|---|---|
| 57 | 0 | 112 | 163.35 | 1.08 |
| 57 | 1 | 113 | 163.96 | 1.05 |
| 84 | 36 | 113 | 163.71 | 1.21 |

| Sector | cycle | core quality-0 | opposite deficit ppt |
|---|---|---|---|
| 84 | 35 | 111 | 0.18 |


## Source attribution and alternate extraction

The helper's representative sector 57 QLP aperture products show No QLP aperture variants in this file. These repeat the event in different QLP apertures but are not independent pipeline evidence. A separately extracted background-subtracted TESScut light curve in sector 57 has 1×1/3×3/5×5 aperture losses of 151.44/146.83/140.20 ppt and a positive difference-centroid offset of 0.058 pixel from the target (descriptive, not a calibrated localization likelihood). The 60-arcsec Gaia neighbor cone is documented in `batch-shared/helper-pixels/gaia-all.raw` with its hash receipt. Its optimistic capability test compares a neighbor's **intrinsic** eclipse fraction to the minimum measured QLP or custom-aperture loss (140.20 ppt); G-band and unit throughput are proxies, and a positive offset alone is not a calibrated exclusion.

No Gaia G-measured neighbor passed the optimistic capability test within 60 arcsec.

## Gaia geometry and outcome

Gaia's SB2 orbit has P = 20.68233098 ± 0.00120448 d, e = 0.4928, ω = 43.42°, and primary-velocity mass function 0.3827 solar masses. The selected eclipse period minus Gaia's is 0.00600 d. Closest edge-on conjunction A is 0.9415 d (0.0455 phase) from the measured epoch; source-specific Gaia full-covariance linear propagation gives 0.1471 d at that epoch. `batch-shared/gaia-geometry.json` retains both conjunctions and covariance order. This comparison is descriptive, not a calibrated orbit-ownership probability. Eclipse durations and depths are stellar-eclipse compatible in a roughly 20–24 d orbit, without fitted stellar masses/radii.

**Limitations:** A custom TESScut aperture of the same TESS photons reproduces the deficit, but it is not an independent observing occasion. The measured eclipse is 0.942 d from the closest Gaia conjunction, 6.4 times its propagated Gaia linear error; the published Gaia orbit and eclipse clock may refer to different or inaccurately modeled motion. Sector 16 has a flagged preceding core and a clean later eclipse whose egress is beyond the sector edge; neither supplies a full center fit.

**Next decisive check:** Recheck the Gaia source/orbit assignment with new radial velocities at predicted conjunctions.
