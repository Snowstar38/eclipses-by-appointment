# TIC 395790195: bounded evidence reconciliation

Physical verdict: **confirmed**. Five-check review completion: **complete** (representative-event reuse audit, not an all-event rerun). Catalogue novelty is a separate central review.

Period 55.460424 +/- 3.3e-05 d; detected deep-eclipse epoch 1756.37044 BTJD; representative pipeline depth 130.0 ppt. Original timing uncertainties retained. B-only systems use the observed B as the deep-eclipse epoch.

## Deciding checks

Two B eclipses separated30 cycles plus one A; B-only period55.460424d agrees Gaia +1.31sigma and excludes29/31cycle alternatives. TESS-SPOC and TASOC recover earlier events. s16A/s76B pixel fits locate deficit3.7/2.4arcsec from target. Joint model e0.3837, omega169.07deg matches Gaia and both partial eclipses.

Raw repeated events, eclipse-derived timing, target attribution, a second reduction and Gaia-compatible geometry all pass at the scope permitted by the data. Same-photon reductions check robustness and are not independent observations. The source timing, pixel, pipeline and physical outputs were inspected; representative pixel maps were visually inspected in representative_pixels.jpg. No inherited CONFIRMED label was used as a substitute for these checks.

## Limitations and next check

Adopt timing-only B period/error; tighter joint-model55.460455 +/-0.000021d is conditional on model. Only two same-kind epochs, cycle count constrained by Gaia.

Next check: Another B eclipse to test cycle count.

Evidence provenance: original report SHA256 bd035fa79e078350bb85a8031fc99c3db204b27899db2b644f976e8a5938bbc2, verified unchanged against queue.csv. Deciding outputs, analysis scripts and cached FITS are hashed in evidence_manifest.json; report source is REPORT.md under historical vet395790195. Historical source bytes were not edited. This review uses existing raw-event measurements rather than claiming a fresh extraction of all cadences.


Public evidence: [historical report](../../evidence/395790195/historical/REPORT.md) (historical; superseded by this reconciliation); see the export manifest for deciding artifacts and source/export hashes. Stable review key: P016.
