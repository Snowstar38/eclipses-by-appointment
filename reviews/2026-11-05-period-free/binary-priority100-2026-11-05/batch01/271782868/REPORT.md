# T010: TIC 271782868

**Physical verdict:** REFUTED. **Bounded review:** COMPLETE. **Novelty:** UNKNOWN (shared catalogue gates, not inferred from physical evidence).

QLP SAP has a 31.19-ppt rectangular loss in sector 88. A target-centered TESSCut 3x3 with 5552-count baseline, using the same 103 core and 129-cadence flank windows, has −1.10-ppt loss and remains flat. This is positive contrary evidence for an eclipse on the selected Gaia target. It does not show that the star cannot be a binary or identify the source of the QLP rectangle.

## Raw events and recurrence

Source FITS checked by SHA-256; 4 cached sectors, 1 retained dip windows re-examined in quality-zero raw SAP. Screening windows were predictions, not eclipse centers. All retained-window plots are `lead-raw-*.png`; numeric source receipts and local-fit diagnostics are `lead-numeric.json`.

| Sector | Screen BTJD | Fit BTJD | Raw deficit (ppt) | Fit caveat |
|---:|---:|---:|---:|---|
| 88 | 3691.705 | 3691.7274 | 30.3 | finite |

## Clock and orbit

- No repeat clock is measured.
- Gaia DR3 SB1 orbit: P=35.65126 d. Nearest edge-on conjunction at evaluation BTJD 3691.7046 differs by -0.113 d, with source-specific linear covariance sigma 2.429 d (-0.05 sigma). This is a compatibility check, not proof of source ownership.

## Source and independent reduction

WCS difference centroid is 0.521 TESS pixels from the target; custom TESSCut depth is -3.38 ppt. The narrower, target-centered 3x3 simultaneous check in `helper-T010-comparison.png` is decisive; the broad 5x5 difference statistic is not used. Same-photon TESSCut extraction is an independent reduction, not another observing occasion. 10 Gaia neighbors within 120 arcsec pass the optimistic G-band full-throughput disappearance screen; neighbor positions and flux-ratio assumptions are in `helper-neighbors-all.json`.

**Limitations:** The sector-88 QLP rectangle is contradicted by simultaneous target-centered TESSCut flux; its QLP aperture/background origin is unresolved. Sector-109 cutout has near-zero target flux and supplies no sensitive null.

**Next check:** Inspect the QLP sector-88 aperture and background pixels to identify the rectangular signal origin.

## Evidence

- `lead-numeric.json`, `lead-timing.json`, and `lead-raw-*.png`: raw SAP and timing.
- `../helper-spatial.json`, `../helper-spatial-rest.json`, `../helper-neighbors-all.json`, `../helper-gaia-covariance.json`: independent pixel, neighbor, orbital checks.
- `../../source-packets/271782868/sources.json`: frozen bulk and FITS provenance.
