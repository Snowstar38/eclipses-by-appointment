# T009: TIC 466741366

**Physical verdict:** CONFIRMED. **Bounded review:** COMPLETE. **Novelty:** UNKNOWN (shared catalogue gates, not inferred from physical evidence).

Repeated raw eclipses form two distinct kinds. Kind A recurs in sectors 37, 64 and 100 with a 42.568962-d clock; kind B in sectors 64 and 90 gives 42.568189 d. The second kind and multiple cycle baselines support recurrence and reject a score-only interpretation.

## Raw events and recurrence

Source FITS checked by SHA-256; 8 cached sectors, 7 retained dip windows re-examined in quality-zero raw SAP. Screening windows were predictions, not eclipse centers. All retained-window plots are `lead-raw-*.png`; numeric source receipts and local-fit diagnostics are `lead-numeric.json`.

| Sector | Screen BTJD | Fit BTJD | Raw deficit (ppt) | Fit caveat |
|---:|---:|---:|---:|---|
| 37 | 2330.430 | 2330.4867 | 17.6 | finite |
| 37 | 2320.736 | 2320.9407 | 14.2 | unusable covariance/shape |
| 64 | 3044.981 | 3044.9855 | 19.8 | finite |
| 64 | 3054.078 | 3054.1773 | 16.2 | finite |
| 90 | 3768.660 | 3768.6447 | 18.2 | finite |
| 99 | 4067.997 | 4067.3713 | 5.6 | finite |
| 100 | 4075.745 | 4075.8161 | 10.9 | finite |

## Clock and orbit

- kind_a: 42.568962 d from sectors 37, 64, 100, integer cycles 0, 17, 41; timing allowance 0.000487 d (2 events: half-cadence or finite formal timing allowance; >=3: residual scatter or cadence floor, no pipeline systematic calibration).
- kind_b: 42.568189 d from sectors 64, 90, integer cycles 0, 17; timing allowance 0.000140 d (2 events: half-cadence or finite formal timing allowance; >=3: residual scatter or cadence floor, no pipeline systematic calibration).
- Gaia DR3 SB1 orbit: P=42.55749 d. Nearest edge-on conjunction at evaluation BTJD 3768.6450 differs by +0.065 d, with source-specific linear covariance sigma 1.088 d (+0.06 sigma). This is a compatibility check, not proof of source ownership.

## Source and independent reduction

WCS difference centroid is 0.321 TESS pixels from the target; custom TESSCut depth is 10.36 ppt. The nearest G-capable Gaia neighbor is 1.86 pixels from the loss centroid, versus 0.321 pixel for the target. Same-photon TESSCut extraction is an independent reduction, not another observing occasion. 21 Gaia neighbors within 120 arcsec pass the optimistic G-band full-throughput disappearance screen; neighbor positions and flux-ratio assumptions are in `helper-neighbors-all.json`.

**Limitations:** A sector-37 opposite-kind center fit has singular covariance and is excluded. Sector-99 broad variability is not used as a precise eclipse center.

**Next check:** Observe another clean eclipse in each kind to improve timing and assess depth changes.

## Evidence

- `lead-numeric.json`, `lead-timing.json`, and `lead-raw-*.png`: raw SAP and timing.
- `../helper-spatial.json`, `../helper-spatial-rest.json`, `../helper-neighbors-all.json`, `../helper-gaia-covariance.json`: independent pixel, neighbor, orbital checks.
- `../../source-packets/466741366/sources.json`: frozen bulk and FITS provenance.
