# T001: TIC 219739532

**Physical verdict:** PROBABLE. **Bounded review:** COMPLETE. **Novelty:** UNKNOWN (shared catalogue gates, not inferred from physical evidence).

Many raw eclipses recur in two distinct kinds over sectors 15–85. The deep kind repeats at 28.035775 d; the shallow kind independently gives 28.035757 d. The 4.66-d separation of kinds is compatible with the strongly eccentric Gaia orbit. The 2.71-arcsec neighbor is bright enough that its eclipse could make the observed blended deficit, so source ownership remains open.

## Raw events and recurrence

Source FITS checked by SHA-256; 34 cached sectors, 54 retained dip windows re-examined in quality-zero raw SAP. Screening windows were predictions, not eclipse centers. All retained-window plots are `lead-raw-*.png`; numeric source receipts and local-fit diagnostics are `lead-numeric.json`.

| Sector | Screen BTJD | Fit BTJD | Raw deficit (ppt) | Fit caveat |
|---:|---:|---:|---:|---|
| 15 | 1712.012 | 1711.9047 | 34.5 | finite |
| 16 | 1739.947 | 1739.9382 | 41.1 | finite |
| 17 | 1767.926 | 1767.9760 | 19.2 | finite |
| 18 | 1796.031 | 1796.0110 | 34.3 | finite |
| 19 | 1819.385 | 1819.3843 | 122.9 | finite |
| 19 | 1824.052 | 1824.0465 | 36.6 | finite |
| 21 | 1875.449 | 1875.4555 | 126.9 | finite |
| 21 | 1880.116 | 1880.1183 | 34.1 | finite |
| 22 | 1903.491 | 1903.4913 | 119.4 | finite |
| 22 | 1908.158 | 1908.1536 | 34.4 | finite |
| 23 | 1931.533 | 1931.5268 | 130.0 | finite |
| 23 | 1936.075 | 1936.1900 | 2.9 | finite |
| 24 | 1959.574 | 1959.5628 | 129.6 | finite |
| 24 | 1964.324 | 1964.2240 | 25.1 | finite |
| 25 | 1992.345 | 1992.2608 | 39.3 | finite |
| 25 | 1987.407 | 1987.5890 | 1.0 | unusable covariance/shape |
| 41 | 2436.204 | 2436.1710 | 154.9 | finite |
| 41 | 2440.899 | 2440.8333 | 44.7 | finite |
| 47 | 2604.386 | 2604.3855 | 148.0 | finite |
| 47 | 2581.066 | 2581.0124 | 42.8 | finite |
| 48 | 2632.421 | 2632.4213 | 148.5 | finite |
| 49 | 2660.456 | 2660.4570 | 153.9 | finite |
| 50 | 2688.491 | 2688.4929 | 159.4 | finite |
| 51 | 2716.553 | 2716.5286 | 153.5 | finite |
| 52 | 2721.192 | 2721.1872 | 42.2 | finite |
| 52 | 2735.962 | 2736.4622 | 25.9 | finite |
| 54 | 2772.600 | 2772.6002 | 149.7 | finite |
| 54 | 2777.267 | 2777.2635 | 44.9 | finite |
| 55 | 2800.635 | 2800.6357 | 152.5 | finite |
| 55 | 2805.280 | 2805.2981 | 45.1 | finite |
| 56 | 2828.669 | 2828.6717 | 154.5 | finite |
| 56 | 2833.329 | 2833.3339 | 44.8 | finite |
| 57 | 2856.708 | 2856.7073 | 161.0 | finite |
| 57 | 2861.366 | 2861.3692 | 44.9 | finite |
| 58 | 2884.734 | 2884.7432 | 158.8 | finite |
| 58 | 2889.366 | 2889.3603 | 50.0 | unusable covariance/shape |
| 74 | 3333.189 | 3333.1930 | 114.9 | unusable covariance/shape |
| 74 | 3337.960 | 3337.9772 | 44.7 | finite |
| 75 | 3361.335 | 3361.3514 | 153.6 | finite |
| 75 | 3366.009 | 3366.0133 | 44.2 | finite |
| 76 | 3389.410 | 3389.3872 | 154.3 | finite |
| 76 | 3394.055 | 3394.0496 | 44.5 | finite |
| 77 | 3422.158 | 3422.0837 | 46.4 | finite |
| 79 | 3473.352 | 3473.3632 | 143.6 | finite |
| 79 | 3478.164 | 3478.1556 | 43.5 | finite |
| 80 | 3501.524 | 3501.5322 | 154.4 | finite |
| 81 | 3529.591 | 3529.5658 | 154.1 | finite |
| 82 | 3557.600 | 3557.6017 | 155.5 | finite |
| 82 | 3534.232 | 3534.2284 | 45.9 | finite |
| 83 | 3562.218 | 3562.2634 | 46.3 | finite |
| 84 | 3585.642 | 3585.6376 | 155.3 | finite |
| 84 | 3590.385 | 3590.2997 | 45.4 | finite |
| 85 | 3613.688 | 3613.6733 | 156.0 | finite |
| 85 | 3618.341 | 3618.3354 | 45.2 | finite |

## Clock and orbit

- deep: 28.035775 d from sectors 19, 21, 22, 23, 24, 41, 47, 48, 49, 50, 51, 54, 55, 56, 57, 58, 75, 76, 80, 81, 82, 84, 85, integer cycles 0, 2, 3, 4, 5, 22, 28, 29, 30, 31, 32, 34, 35, 36, 37, 38, 55, 56, 60, 61, 62, 63, 64; timing allowance 0.000020 d (2 events: half-cadence or finite formal timing allowance; >=3: residual scatter or cadence floor, no pipeline systematic calibration).
- shallow: 28.035757 d from sectors 15, 16, 17, 18, 19, 21, 22, 23, 24, 25, 41, 47, 52, 54, 55, 56, 57, 74, 75, 76, 77, 79, 82, 83, 84, 85, integer cycles 0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 26, 31, 36, 38, 39, 40, 41, 58, 59, 60, 61, 63, 65, 66, 67, 68; timing allowance 0.000016 d (2 events: half-cadence or finite formal timing allowance; >=3: residual scatter or cadence floor, no pipeline systematic calibration).
- Gaia DR3 SB1 orbit: P=28.03092 d. Nearest edge-on conjunction at evaluation BTJD 1903.4910 differs by +0.266 d, with source-specific linear covariance sigma 0.481 d (+0.55 sigma). This is a compatibility check, not proof of source ownership.

## Source and independent reduction

WCS difference centroid is 0.077 TESS pixels from the target; custom TESSCut depth is 118.97 ppt. Same-photon TESSCut extraction is an independent reduction, not another observing occasion. 1 Gaia neighbors within 120 arcsec pass the optimistic G-band full-throughput disappearance screen; neighbor positions and flux-ratio assumptions are in `helper-neighbors-all.json`.

**Limitations:** A Gaia neighbor 2.71 arcsec away could produce the observed loss; the TESS difference centroid cannot resolve it.

**Next check:** Resolve the target and close Gaia neighbor with high-resolution in-eclipse imaging.

## Evidence

- `lead-numeric.json`, `lead-timing.json`, and `lead-raw-*.png`: raw SAP and timing.
- `../helper-spatial.json`, `../helper-spatial-rest.json`, `../helper-neighbors-all.json`, `../helper-gaia-covariance.json`: independent pixel, neighbor, orbital checks.
- `../../source-packets/219739532/sources.json`: frozen bulk and FITS provenance.
