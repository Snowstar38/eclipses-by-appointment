# T008: TIC 37647565

**Physical verdict:** PLAUSIBLE. **Bounded review:** COMPLETE. **Novelty:** UNKNOWN (shared catalogue gates, not inferred from physical evidence).

Sector 62 shows ingress, a central data gap, and a strong recovery compatible with a broad eclipse; its fitted center at the gap edge is not a measured minimum. No same-kind repeat is established in the cached sectors. A newer sector-109 cutout covers a bounded flat interval, but that interval does not test all period aliases.

## Raw events and recurrence

Source FITS checked by SHA-256; 5 cached sectors, 1 retained dip windows re-examined in quality-zero raw SAP. Screening windows were predictions, not eclipse centers. All retained-window plots are `lead-raw-*.png`; numeric source receipts and local-fit diagnostics are `lead-numeric.json`.

| Sector | Screen BTJD | Fit BTJD | Raw deficit (ppt) | Fit caveat |
|---:|---:|---:|---:|---|
| 62 | 3002.414 | 3002.4041 | 124.3 | unusable covariance/shape |

## Clock and orbit

- No repeat clock is measured.
- Gaia DR3 SB1 orbit: P=44.44072 d. Nearest edge-on conjunction at evaluation BTJD 3002.4137 differs by +11.737 d, with source-specific linear covariance sigma 2.953 d (+3.97 sigma). This is a compatibility check, not proof of source ownership.

## Source and independent reduction

A valid difference centroid is unavailable in the checked TESSCut aperture. The cutout lies on the detector edge with zero-valued pixels, so its negative fixed-window difference is not a sensitive refutation. Same-photon TESSCut extraction is an independent reduction, not another observing occasion. 1 Gaia neighbors within 120 arcsec pass the optimistic G-band full-throughput disappearance screen; neighbor positions and flux-ratio assumptions are in `helper-neighbors-all.json`.

**Limitations:** One broad raw event has a central 1.6-d gap, so its center and depth are not secure. The sector-62 TESSCut is on a zero-pixel detector edge and cannot test the source. New sector 109 is flat only in BTJD 4318.56–4338.74.

**Next check:** Get a target-centered alternative reduction and another eclipse occasion.

## Evidence

- `lead-numeric.json`, `lead-timing.json`, and `lead-raw-*.png`: raw SAP and timing.
- `../helper-spatial.json`, `../helper-spatial-rest.json`, `../helper-neighbors-all.json`, `../helper-gaia-covariance.json`: independent pixel, neighbor, orbital checks.
- `../../source-packets/37647565/sources.json`: frozen bulk and FITS provenance.
