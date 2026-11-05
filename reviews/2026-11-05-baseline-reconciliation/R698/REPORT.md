# TIC 349978696 — CONFIRMED

Bounded full physical review: **COMPLETE**. Review ID R698. Ten-target sealed queue position 1 is an operational order, not a scientific rank. Physical outcome is **CONFIRMED**: repeated raw SAP eclipses, the same-kind cycle count, and a separate reduction of the same pixels are secure. The deciding pixel, neighbor and Gaia checks available here are compatible with the target/orbit assignment. A matching eclipsing-binary entry for this exact TIC appears in IJspeert et al. (2024), so this is a known recovery in the queried catalogue scope. Catalogue evidence is in `batch-shared/../remaining_cached/catalogue-recovery-late/coverage-matrix.csv`; physical and novelty statuses are separate.

## Raw SAP events and timing

The sealed snapshot maps TIC 349978696 to Gaia DR3 2274702988786236800 and 25 QLP FITS receipts. `measure_raw.py` verified every FITS SHA-256 before fitting quality-zero raw `SAP_FLUX` with free-center trapezoids. Fitted model amplitude and realized central depth are separate in `measurements.json`; the median realized depth of timing-usable events is 169.42 ppt. The screen period/epoch only located windows. The same-kind fit uses 28 usable centers spanning cycles 0–93, including an adjacent-cycle anchor. It yields P = 20.756657664 ± 0.000017929 d, reference epoch BTJD 1716.70706125 ± 0.00133653 d at cycle 0; reduced χ² = 0.49. Errors are weighted fit covariance with individual max(formal center covariance, half cadence) and scatter inflation if χ² > 1. They exclude model, pipeline, source and long-term systematics; they are not total ephemeris uncertainty. The named epoch is the selected eclipse kind, not an assumed primary.

| Sector | same-kind cycle | mid BTJD | center error d | realized depth ppt |
|---|---|---|---|---|
| 15 | 0 | 1716.70612 | 0.010417 | 146.03 |
| 18 | 4 | 1799.73324 | 0.010417 | 172.44 |
| 19 | 5 | 1820.49188 | 0.010417 | 167.26 |
| 58 | 57 | 2899.83515 | 0.001157 | 170.29 |
| 86 | 93 | 3647.07702 | 0.001157 | 166.84 |

Representative raw panels and all retained/excluded fits are in `raw-events.png` and `measurements.json`. 

Actual quality-zero main windows with bilateral sidebands (28 clean sampled) and opposite half-phase windows (19 clean sampled) are in `batch-shared/coverage-alias.json`. Incomplete or flagged windows are not nulls. The adjacent-cycle pair fixes the integer count between separated events; the opposite-phase sampled losses test P/2 and are not counted as same-kind cycles. Representative coverage (local robust scatter shown for main windows):

| Sector | cycle | core quality-0 | main deficit ppt | OOT scatter ppt |
|---|---|---|---|---|
| 15 | 0 | 8 | 126.11 | 2.04 |
| 58 | 57 | 78 | 140.70 | 0.88 |
| 86 | 93 | 78 | 137.50 | 0.72 |

| Sector | cycle | core quality-0 | opposite deficit ppt |
|---|---|---|---|
| 15 | 0 | 8 | 0.41 |
| 56 | 53 | 78 | 0.17 |
| 85 | 91 | 75 | 0.10 |


## Source attribution and alternate extraction

The helper's representative sector 25 QLP aperture products show KSPSAP_FLUX_SML 141.49 ppt; KSPSAP_FLUX 147.38 ppt; KSPSAP_FLUX_LAG 150.74 ppt These repeat the event in different QLP apertures but are not independent pipeline evidence. A separately extracted background-subtracted TESScut light curve in sector 25 has 1×1/3×3/5×5 aperture losses of 138.72/140.09/139.05 ppt and a positive difference-centroid offset of 0.134 pixel from the target (descriptive, not a calibrated localization likelihood). The 60-arcsec Gaia neighbor cone is documented in `batch-shared/helper-pixels/gaia-all.raw` with its hash receipt. Its optimistic capability test compares a neighbor's **intrinsic** eclipse fraction to the minimum measured QLP or custom-aperture loss (138.72 ppt); G-band and unit throughput are proxies, and a positive offset alone is not a calibrated exclusion.

No Gaia G-measured neighbor passed the optimistic capability test within 60 arcsec.

## Gaia geometry and outcome

Gaia's SB2 orbit has P = 20.75580433 ± 0.00194027 d, e = 0.4418, ω = 315.43°, and primary-velocity mass function 0.1223 solar masses. The selected eclipse period minus Gaia's is 0.00085 d. Closest edge-on conjunction B is 0.4102 d (0.0198 phase) from the measured epoch; source-specific Gaia full-covariance linear propagation gives 0.1430 d at that epoch. `batch-shared/gaia-geometry.json` retains both conjunctions and covariance order. This comparison is descriptive, not a calibrated orbit-ownership probability. Eclipse durations and depths are stellar-eclipse compatible in a roughly 20–24 d orbit, without fitted stellar masses/radii.

**Limitations:** A custom TESScut aperture of the same TESS photons reproduces the deficit, but it is not an independent observing occasion.

**Next decisive check:** Acquire a clean future eclipse to refine the ephemeris and check long-term stability.
