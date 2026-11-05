# T004: TIC 241629469

**Physical verdict:** CONFIRMED. **Bounded review:** COMPLETE. **Novelty:** UNKNOWN (shared catalogue gates, not inferred from physical evidence).

Deep raw eclipses in sectors 65 and 102 are 28 cycles apart at 38.115712 d. Shallow events around 3090.5 and 4119.56, 27 cycles apart, support the same orbit at the opposite conjunction. The sector-102 gap limits timing precision but does not erase its ingress and egress.

## Raw events and recurrence

Source FITS checked by SHA-256; 5 cached sectors, 5 retained dip windows re-examined in quality-zero raw SAP. Screening windows were predictions, not eclipse centers. All retained-window plots are `lead-raw-*.png`; numeric source receipts and local-fit diagnostics are `lead-numeric.json`.

| Sector | Screen BTJD | Fit BTJD | Raw deficit (ppt) | Fit caveat |
|---:|---:|---:|---:|---|
| 65 | 3070.003 | 3070.0045 | 123.2 | finite |
| 65 | 3090.478 | 3090.4938 | 11.3 | unusable covariance/shape |
| 101 | 4119.566 | 4119.5589 | 11.3 | finite |
| 102 | 4137.235 | 4137.2444 | 69.0 | finite |
| 102 | 4144.428 | 4144.6188 | 5.5 | finite |

Shorter P/2 deep-event alias at BTJD 3089.0624 has 123/147 expected quality-zero core samples, 190/110 flank samples, a 0.0093-d largest core gap and -0.05-ppt core deficit versus a >100-ppt deep eclipse. The recorded gross-event sensitivity excludes a missed counterpart there; `lead-short-alias.json` and plot retain stricter coverage flags and additional P/3/P/4 checks.

## Clock and orbit

- deep: 38.115712 d from sectors 65, 102, integer cycles 0, 28; timing allowance 0.000058 d (2 events: half-cadence or finite formal timing allowance; >=3: residual scatter or cadence floor, no pipeline systematic calibration).
- shallow: 38.113525 d from sectors 65, 101, integer cycles 0, 27; timing allowance 0.003704 d (2 events: half-cadence or finite formal timing allowance; >=3: residual scatter or cadence floor, no pipeline systematic calibration).
- Gaia DR3 SB1 orbit: P=38.08938 d. Nearest edge-on conjunction at evaluation BTJD 3070.0045 differs by +1.263 d, with source-specific linear covariance sigma 2.674 d (+0.47 sigma). This is a compatibility check, not proof of source ownership.

## Source and independent reduction

WCS difference centroid is 0.084 TESS pixels from the target; custom TESSCut depth is 105.46 ppt. Same-photon TESSCut extraction is an independent reduction, not another observing occasion. 0 Gaia neighbors within 120 arcsec pass the optimistic G-band full-throughput disappearance screen; neighbor positions and flux-ratio assumptions are in `helper-neighbors-all.json`.

**Limitations:** The sector-102 deep event contains a 0.243-d data gap; its center is inferred from surviving ingress and egress. The 0.0005-d period allowance is conservative relative to the formal fit covariance. The shallow sector-65 fit covariance is singular and its center is not precision evidence.

**Next check:** Obtain one uninterrupted deep eclipse for a cleaner center and period.

## Evidence

- `lead-numeric.json`, `lead-timing.json`, and `lead-raw-*.png`: raw SAP and timing.
- `../helper-spatial.json`, `../helper-spatial-rest.json`, `../helper-neighbors-all.json`, `../helper-gaia-covariance.json`: independent pixel, neighbor, orbital checks.
- `../../source-packets/241629469/sources.json`: frozen bulk and FITS provenance.
