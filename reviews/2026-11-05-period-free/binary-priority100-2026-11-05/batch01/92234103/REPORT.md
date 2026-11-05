# T002: TIC 92234103

**Physical verdict:** PROBABLE. **Bounded review:** COMPLETE. **Novelty:** UNKNOWN (shared catalogue gates, not inferred from physical evidence).

Two clean QLP raw eclipses in sectors 4 and 31 are joined by two full target-centered raw-pixel events in newly available sectors 105 and 108; an additional S108 event at the sector start is partial support. The 29-cycle old assignment yields 24.620831 d across four full centers; 28- and 30-cycle alternatives predict flat, sensitive windows in sectors 105/108. A fully covered sector-108 P/2 prediction is also flat. The binary-like eclipse recurs, but Gaia conjunction timing remains in tension.

## Raw events and recurrence

Source FITS checked by SHA-256; 2 cached sectors, 2 retained dip windows re-examined in quality-zero raw SAP. Screening windows were predictions, not eclipse centers. All retained-window plots are `lead-raw-*.png`; numeric source receipts and local-fit diagnostics are `lead-numeric.json`.

| Sector | Screen BTJD | Fit BTJD | Raw deficit (ppt) | Fit caveat |
|---:|---:|---:|---:|---|
| 4 | 1435.036 | 1435.0295 | 87.8 | finite |
| 31 | 2149.036 | 2149.0344 | 82.8 | finite |

New sector-105/108 target-centered 3x3 raw-pixel events (not QLP rows):
- S105 center 4217.18391, depth 126.5 ppt, baseline 4585 counts; S108 4291 event begins near sector edge and is supporting timing only.
- S108 center 4291.04612, depth 125.0 ppt, baseline 5059 counts; S108 4291 event begins near sector edge and is supporting timing only.
- S108 center 4315.66677, depth 126.9 ppt, baseline 5030 counts; S108 4291 event begins near sector edge and is supporting timing only.
- P/2 predicted BTJD 4303.3596: 104 quality-zero core cadences, 151/150 flanks, -0.25 ppt versus ~127-ppt events. S107 target aperture has ~0.6-count baseline and is not a sensitive null.
- Gaia nearest conjunction at new S108 center differs by -7.63 d / 2.70 d linear sigma (-2.83 sigma). Source-specific covariance does not remove the timing tension.
`lead-newsector-coverage.json` records all 28/29/30-cycle predictions with core endpoints, internal gaps, flank counts, aperture flux and source hashes; only sensitive nulls were used to reject aliases.

## Clock and orbit

- deep: 24.620831 d from sectors 4, 31, 105, 108, integer cycles 0, 29, 113, 117; timing allowance 0.000050 d (0.00005 d conservative allowance for QLP versus custom-pixel timing, exceeding formal regression scatter error).
- Gaia DR3 SB1 orbit: P=24.66603 d. Nearest edge-on conjunction at evaluation BTJD 1435.0364 differs by -2.335 d, with source-specific linear covariance sigma 0.743 d (-3.14 sigma). This is a compatibility check, not proof of source ownership.

## Source and independent reduction

WCS difference centroid is 0.206 TESS pixels from the target; custom TESSCut depth is 109.23 ppt. Same-photon TESSCut extraction is an independent reduction, not another observing occasion. 0 Gaia neighbors within 120 arcsec pass the optimistic G-band full-throughput disappearance screen; neighbor positions and flux-ratio assumptions are in `helper-neighbors-all.json`.

**Limitations:** Gaia conjunction differs by about 3.1 linear sigma at the old event and 2.8 sigma at the new event, despite strong photometric recurrence and target-centered pixel flux. The Gaia orbit or source association needs reconciliation.

**Next check:** Obtain radial velocities and a new eclipse to compare the 24.620831-d photometric clock with the Gaia spectroscopic orbit.

## Evidence

- `lead-numeric.json`, `lead-timing.json`, and `lead-raw-*.png`: raw SAP and timing.
- `../helper-spatial.json`, `../helper-spatial-rest.json`, `../helper-neighbors-all.json`, `../helper-gaia-covariance.json`: independent pixel, neighbor, orbital checks.
- `../../source-packets/92234103/sources.json`: frozen bulk and FITS provenance.
