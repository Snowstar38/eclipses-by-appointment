# T006: TIC 46744354

**Physical verdict:** CONFIRMED. **Bounded review:** COMPLETE. **Novelty:** UNKNOWN (shared catalogue gates, not inferred from physical evidence).

Two clean raw eclipses in sectors 32 and 33 are 43.062 d apart. The two-cycle alias predicts a fully observed midpoint at BTJD 2204.770 with only 0.17 ppt deficit; three- and four-cycle aliases likewise predict a clean null. This supports one orbital cycle between the events.

## Raw events and recurrence

Source FITS checked by SHA-256; 4 cached sectors, 2 retained dip windows re-examined in quality-zero raw SAP. Screening windows were predictions, not eclipse centers. All retained-window plots are `lead-raw-*.png`; numeric source receipts and local-fit diagnostics are `lead-numeric.json`.

| Sector | Screen BTJD | Fit BTJD | Raw deficit (ppt) | Fit caveat |
|---:|---:|---:|---:|---|
| 32 | 2183.237 | 2183.2390 | 29.9 | finite |
| 33 | 2226.279 | 2226.3010 | 32.0 | finite |

## Clock and orbit

- deep: 43.062062 d from sectors 32, 33, integer cycles 0, 1; timing allowance 0.004910 d (2 events: half-cadence or finite formal timing allowance; >=3: residual scatter or cadence floor, no pipeline systematic calibration).
- Gaia DR3 SB1 orbit: P=43.08673 d. Nearest edge-on conjunction at evaluation BTJD 2183.2390 differs by -1.497 d, with source-specific linear covariance sigma 2.227 d (-0.67 sigma). This is a compatibility check, not proof of source ownership.

## Source and independent reduction

WCS difference centroid is 0.165 TESS pixels from the target; custom TESSCut depth is 32.85 ppt. Same-photon TESSCut extraction is an independent reduction, not another observing occasion. 1 Gaia neighbors within 120 arcsec pass the optimistic G-band full-throughput disappearance screen; neighbor positions and flux-ratio assumptions are in `helper-neighbors-all.json`.

**Limitations:** Only two observed eclipse centers; the period allowance is driven by half-cadence timing and does not calibrate model systematics.

**Next check:** Observe a third eclipse to refine the period.

## Evidence

- `lead-numeric.json`, `lead-timing.json`, and `lead-raw-*.png`: raw SAP and timing.
- `../helper-spatial.json`, `../helper-spatial-rest.json`, `../helper-neighbors-all.json`, `../helper-gaia-covariance.json`: independent pixel, neighbor, orbital checks.
- `../../source-packets/46744354/sources.json`: frozen bulk and FITS provenance.
