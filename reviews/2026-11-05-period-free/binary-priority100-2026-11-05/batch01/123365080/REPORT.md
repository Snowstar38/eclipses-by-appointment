# T003: TIC 123365080

**Physical verdict:** CONFIRMED. **Bounded review:** COMPLETE. **Novelty:** UNKNOWN (shared catalogue gates, not inferred from physical evidence).

Deep raw eclipses recur in sectors 97 and 104 five cycles apart. Shallow eclipses in sectors 3 and 97 give 48.527215 d over 53 cycles, agreeing with the 48.527672-d deep clock. The two kinds are separated by the eccentric-orbit phase; their independent cycle spans address aliases.

## Raw events and recurrence

Source FITS checked by SHA-256; 4 cached sectors, 4 retained dip windows re-examined in quality-zero raw SAP. Screening windows were predictions, not eclipse centers. All retained-window plots are `lead-raw-*.png`; numeric source receipts and local-fit diagnostics are `lead-numeric.json`.

| Sector | Screen BTJD | Fit BTJD | Raw deficit (ppt) | Fit caveat |
|---:|---:|---:|---:|---|
| 3 | 1399.140 | 1399.1400 | 23.1 | finite |
| 97 | 3953.427 | 3953.4326 | 125.3 | finite |
| 97 | 3971.059 | 3971.0824 | 20.6 | finite |
| 104 | 4196.036 | 4196.0710 | 117.4 | finite |

Shorter P/2 deep-event alias at BTJD 3977.6964 has 138/138 expected quality-zero core samples, 195/195 flank samples, a 0.0023-d largest core gap and +0.16-ppt core deficit versus a >100-ppt deep eclipse. The recorded gross-event sensitivity excludes a missed counterpart there; `lead-short-alias.json` and plot retain stricter coverage flags and additional P/3/P/4 checks.

## Clock and orbit

- deep: 48.527672 d from sectors 97, 104, integer cycles 0, 5; timing allowance 0.000327 d (2 events: half-cadence or finite formal timing allowance; >=3: residual scatter or cadence floor, no pipeline systematic calibration).
- shallow: 48.527215 d from sectors 3, 97, integer cycles 0, 53; timing allowance 0.000198 d (2 events: half-cadence or finite formal timing allowance; >=3: residual scatter or cadence floor, no pipeline systematic calibration).
- Gaia DR3 SB1 orbit: P=48.62184 d. Nearest edge-on conjunction at evaluation BTJD 3953.4330 differs by -7.668 d, with source-specific linear covariance sigma 4.768 d (-1.61 sigma). This is a compatibility check, not proof of source ownership.

## Source and independent reduction

WCS difference centroid is 0.122 TESS pixels from the target; custom TESSCut depth is 159.09 ppt. Same-photon TESSCut extraction is an independent reduction, not another observing occasion. 0 Gaia neighbors within 120 arcsec pass the optimistic G-band full-throughput disappearance screen; neighbor positions and flux-ratio assumptions are in `helper-neighbors-all.json`.

**Limitations:** The two same-kind deep centers give a conditional five-cycle clock; two shallow events over 53 cycles independently agree. Long-baseline Gaia covariance is linearized.

**Next check:** Acquire another primary eclipse to sharpen the clock and orbit comparison.

## Evidence

- `lead-numeric.json`, `lead-timing.json`, and `lead-raw-*.png`: raw SAP and timing.
- `../helper-spatial.json`, `../helper-spatial-rest.json`, `../helper-neighbors-all.json`, `../helper-gaia-covariance.json`: independent pixel, neighbor, orbital checks.
- `../../source-packets/123365080/sources.json`: frozen bulk and FITS provenance.
