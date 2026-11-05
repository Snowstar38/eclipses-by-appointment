# TIC 102305337 — CONFIRMED

Bounded full physical review: **COMPLETE**. Review ID R701. Ten-target sealed queue position 4 is an operational order, not a scientific rank. Physical outcome is **CONFIRMED**: repeated raw SAP eclipses, the same-kind cycle count, and a separate reduction of the same pixels are secure. The deciding pixel, neighbor and Gaia checks available here are compatible with the target/orbit assignment. A matching eclipsing-binary entry for this exact TIC appears in IJspeert et al. (2024), so this is a known recovery in the queried catalogue scope. Catalogue evidence is in `batch-shared/../remaining_cached/catalogue-recovery-late/coverage-matrix.csv`; physical and novelty statuses are separate.

## Raw SAP events and timing

The sealed snapshot maps TIC 102305337 to Gaia DR3 6142739540447453952 and 5 QLP FITS receipts. `measure_raw.py` verified every FITS SHA-256 before fitting quality-zero raw `SAP_FLUX` with free-center trapezoids. Fitted model amplitude and realized central depth are separate in `measurements.json`; the median realized depth of timing-usable events is 18.50 ppt. The screen period/epoch only located windows. The same-kind fit uses 5 usable centers spanning cycles 0–109, including an adjacent-cycle anchor. It yields P = 23.321993637 ± 0.000066817 d, reference epoch BTJD 1589.45468593 ± 0.00628330 d at cycle 0; reduced χ² = 6.33. Errors are weighted fit covariance with individual max(formal center covariance, half cadence) and scatter inflation if χ² > 1. They exclude model, pipeline, source and long-term systematics; they are not total ephemeris uncertainty. The named epoch is the selected eclipse kind, not an assumed primary.

| Sector | same-kind cycle | mid BTJD | center error d | realized depth ppt |
|---|---|---|---|---|
| 10 | 0 | 1589.48701 | 0.010417 | 18.67 |
| 64 | 63 | 3058.73828 | 0.001157 | 18.50 |
| 101 | 108 | 4108.23206 | 0.001157 | 14.53 |
| 102 | 109 | 4131.55094 | 0.001157 | 14.18 |

Representative raw panels and all retained/excluded fits are in `raw-events.png` and `measurements.json`. 

Actual quality-zero main windows with bilateral sidebands (5 clean sampled) and opposite half-phase windows (5 clean sampled) are in `batch-shared/coverage-alias.json`. Incomplete or flagged windows are not nulls. The adjacent-cycle pair fixes the integer count between separated events; the opposite-phase sampled losses test P/2 and are not counted as same-kind cycles. Representative coverage (local robust scatter shown for main windows):

| Sector | cycle | core quality-0 | main deficit ppt | OOT scatter ppt |
|---|---|---|---|---|
| 10 | 0 | 4 | 17.08 | 0.22 |
| 64 | 63 | 52 | 18.00 | 0.84 |
| 102 | 109 | 52 | 13.22 | 0.73 |

| Sector | cycle | core quality-0 | opposite deficit ppt |
|---|---|---|---|
| 10 | -1 | 6 | 0.06 |
| 64 | 62 | 52 | -0.03 |
| 102 | 109 | 47 | 0.42 |


## Source attribution and alternate extraction

The helper's representative sector 10 QLP aperture products show KSPSAP_FLUX_SML 17.20 ppt; KSPSAP_FLUX 17.85 ppt; KSPSAP_FLUX_LAG 18.03 ppt These repeat the event in different QLP apertures but are not independent pipeline evidence. A separately extracted background-subtracted TESScut light curve in sector 10 has 1×1/3×3/5×5 aperture losses of 22.41/18.71/18.53 ppt and a positive difference-centroid offset of 0.129 pixel from the target (descriptive, not a calibrated localization likelihood). The 60-arcsec Gaia neighbor cone is documented in `batch-shared/helper-pixels/gaia-all.raw` with its hash receipt. Its optimistic capability test compares a neighbor's **intrinsic** eclipse fraction to the minimum measured QLP or custom-aperture loss (17.20 ppt); G-band and unit throughput are proxies, and a positive offset alone is not a calibrated exclusion.

No Gaia G-measured neighbor passed the optimistic capability test within 60 arcsec.

## Gaia geometry and outcome

Gaia's SB1 orbit has P = 23.31316748 ± 0.00860817 d, e = 0.2132, ω = 67.94°, and primary-velocity mass function 0.0023 solar masses. The selected eclipse period minus Gaia's is 0.00883 d. Closest edge-on conjunction A is 0.3904 d (0.0167 phase) from the measured epoch; source-specific Gaia full-covariance linear propagation gives 0.4903 d at that epoch. `batch-shared/gaia-geometry.json` retains both conjunctions and covariance order. This comparison is descriptive, not a calibrated orbit-ownership probability. Eclipse durations and depths are stellar-eclipse compatible in a roughly 20–24 d orbit, without fitted stellar masses/radii.

**Limitations:** A custom TESScut aperture of the same TESS photons reproduces the deficit, but it is not an independent observing occasion. Early and late depths differ by roughly 4 ppt, consistent with extraction or aperture variation; timing remains repeated.

**Next decisive check:** Acquire a clean future eclipse to refine the ephemeris and check long-term stability.
