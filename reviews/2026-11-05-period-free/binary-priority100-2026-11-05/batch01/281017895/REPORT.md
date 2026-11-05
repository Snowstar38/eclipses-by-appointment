# T005: TIC 281017895

**Physical verdict:** CONFIRMED. **Bounded review:** COMPLETE. **Novelty:** UNKNOWN (shared catalogue gates, not inferred from physical evidence).

Deep raw eclipses recur in adjacent sectors 10–11 and 64–65, with shallow opposite-conjunction dips near half phase. The deep centers give 28.028754 d and the shallower kind independently gives 28.027860 d, with local-trend timing limitations.

## Raw events and recurrence

Source FITS checked by SHA-256; 7 cached sectors, 11 retained dip windows re-examined in quality-zero raw SAP. Screening windows were predictions, not eclipse centers. All retained-window plots are `lead-raw-*.png`; numeric source receipts and local-fit diagnostics are `lead-numeric.json`.

| Sector | Screen BTJD | Fit BTJD | Raw deficit (ppt) | Fit caveat |
|---:|---:|---:|---:|---|
| 10 | 1577.763 | 1577.7953 | 62.3 | finite |
| 10 | 1591.764 | 1591.8604 | 28.0 | finite |
| 11 | 1606.118 | 1605.8276 | 60.1 | finite |
| 11 | 1619.618 | 1619.8854 | 32.4 | finite |
| 37 | 2320.541 | 2320.6261 | 20.7 | unusable covariance/shape |
| 64 | 3063.370 | 3063.3245 | 61.0 | finite |
| 64 | 3048.995 | 3049.3270 | 26.1 | finite |
| 65 | 3091.450 | 3091.3464 | 57.2 | finite |
| 65 | 3077.610 | 3077.3170 | 20.4 | finite |
| 99 | 4068.624 | 4068.3458 | 30.4 | finite |
| 99 | 4051.908 | 4052.0222 | 4.2 | finite |

## Clock and orbit

- deep: 28.028754 d from sectors 10, 11, 64, 65, integer cycles 0, 1, 53, 54; timing allowance 0.000072 d (2 events: half-cadence or finite formal timing allowance; >=3: residual scatter or cadence floor, no pipeline systematic calibration).
- shallow: 28.027860 d from sectors 10, 11, 64, 65, integer cycles 0, 1, 52, 53; timing allowance 0.000365 d (2 events: half-cadence or finite formal timing allowance; >=3: residual scatter or cadence floor, no pipeline systematic calibration).
- Gaia DR3 SB1 orbit: P=28.02695 d. Nearest edge-on conjunction at evaluation BTJD 3063.3245 differs by +0.034 d, with source-specific linear covariance sigma 1.013 d (+0.03 sigma). This is a compatibility check, not proof of source ownership.

## Source and independent reduction

WCS difference centroid is 0.078 TESS pixels from the target; custom TESSCut depth is 23.82 ppt. The nearest G-capable Gaia neighbor is 1.91 pixels from the loss centroid, versus 0.078 pixel for the target. Same-photon TESSCut extraction is an independent reduction, not another observing occasion. 9 Gaia neighbors within 120 arcsec pass the optimistic G-band full-throughput disappearance screen; neighbor positions and flux-ratio assumptions are in `helper-neighbors-all.json`.

**Limitations:** Long local baseline trends affect depth and timing; the 0.0005-d period allowance exceeds the formal deep-fit scatter. QLP corrected flux suppresses the event. The TESSCut reduction reproduces it at lower dilution-dependent depth.

**Next check:** Obtain additional short-cadence eclipses with stable aperture photometry.

## Evidence

- `lead-numeric.json`, `lead-timing.json`, and `lead-raw-*.png`: raw SAP and timing.
- `../helper-spatial.json`, `../helper-spatial-rest.json`, `../helper-neighbors-all.json`, `../helper-gaia-covariance.json`: independent pixel, neighbor, orbital checks.
- `../../source-packets/281017895/sources.json`: frozen bulk and FITS provenance.
