# T007: TIC 142761762

**Physical verdict:** PLAUSIBLE. **Bounded review:** COMPLETE. **Novelty:** UNKNOWN (shared catalogue gates, not inferred from physical evidence).

Broad shallow depressions appear in sectors 7, 34, 61 and 88, roughly 38.88 d apart under one cycle assignment, but the sector-34 and sector-61 occasions are partly gapped and have strong changing baselines. The sector-61 post-gap egress is real positive recurrence evidence yet does not choose among 18/19/20-cycle long-baseline aliases. A deeper narrow S88 dip occurs near opposite phase. The eclipse interpretation and clock remain insecure.

## Raw events and recurrence

Source FITS checked by SHA-256; 4 cached sectors, 5 retained dip windows re-examined in quality-zero raw SAP. Screening windows were predictions, not eclipse centers. All retained-window plots are `lead-raw-*.png`; numeric source receipts and local-fit diagnostics are `lead-numeric.json`.

| Sector | Screen BTJD | Fit BTJD | Raw deficit (ppt) | Fit caveat |
|---:|---:|---:|---:|---|
| 7 | 1499.578 | 1499.5882 | 27.0 | finite |
| 34 | 2238.265 | 2239.5879 | 24.5 | unusable covariance/shape |
| 88 | 3696.272 | 3696.3453 | 76.6 | finite |
| 88 | 3715.705 | 3715.7806 | 40.1 | finite |
| 88 | 3703.279 | 3703.4302 | 8.0 | finite |

Sector 61 partial occasion: at predicted BTJD 2977.050, quality-zero core 466/691 expected samples with missing ingress, 15.7-ppt median deficit and 8.2-ppt flank scatter. The observed post-gap egress supports recurrence but does not count integer cycles. Newly fetched S109 has nonzero target flux but trend-dominated edge predictions; see `lead-newsector-coverage.json`.

## Clock and orbit

- No repeat clock is measured.
- Gaia DR3 SB1 orbit: P=38.85832 d. Nearest edge-on conjunction at evaluation BTJD 3696.2723 differs by +2.641 d, with source-specific linear covariance sigma 1.255 d (+2.10 sigma). This is a compatibility check, not proof of source ownership.

## Source and independent reduction

WCS difference centroid is 0.282 TESS pixels from the target; custom TESSCut depth is 21.15 ppt. Same-photon TESSCut extraction is an independent reduction, not another observing occasion. 10 Gaia neighbors within 120 arcsec pass the optimistic G-band full-throughput disappearance screen; neighbor positions and flux-ratio assumptions are in `helper-neighbors-all.json`.

**Limitations:** Broad dips ride changing baseline slopes; S34 and S61 have missing ingress or baseline, so centers are not precise. The 18/19/20-cycle interpretations of the long separation all predict the roughly third-spaced partial occasions. A narrow deep event occurs only in S88. New S109 has changing baseline and edge windows, not a decisive alias test.

**Next check:** Observe an uninterrupted shallow and deep eclipse pair to establish morphology, source and integer cycle count.

## Evidence

- `lead-numeric.json`, `lead-timing.json`, and `lead-raw-*.png`: raw SAP and timing.
- `../helper-spatial.json`, `../helper-spatial-rest.json`, `../helper-neighbors-all.json`, `../helper-gaia-covariance.json`: independent pixel, neighbor, orbital checks.
- `../../source-packets/142761762/sources.json`: frozen bulk and FITS provenance.
