# TIC 126758342: bounded evidence reconciliation

Physical verdict: **confirmed**. Five-check review completion: **complete** (representative-event reuse audit, not an all-event rerun). Catalogue novelty is a separate central review.

Period 22.86993 +/- 8e-05 d; detected deep-eclipse epoch 1729.54161 BTJD; representative pipeline depth 20.0 ppt. Original timing uncertainties retained. B-only systems use the observed B as the deep-eclipse epoch.

## Deciding checks

Three B eclipses at cycles0/31/47 with residuals <=2min; TESS-SPOC all sectors and TASOC s15 recover them. Three pixel fits locate deficit2–4arcsec from target. P/2,/3,/4 covered aliases excluded. Gaia P -1.10sigma and conjunction offsets -0.9 to-1sigma. Partial occultation model predicts depth and absent A.

Raw repeated events, eclipse-derived timing, target attribution, a second reduction and Gaia-compatible geometry all pass at the scope permitted by the data. Same-photon reductions check robustness and are not independent observations. The source timing, pixel, pipeline and physical outputs were inspected; representative pixel maps were visually inspected in representative_pixels.jpg. No inherited CONFIRMED label was used as a substitute for these checks.

## Limitations and next check

Gaia eccentricity and omega broad; A misses in83% of permitted historical model draws, not certainty. Primary_epoch field uses detected deeper B eclipse.

Next check: Refined RV orbit or next B eclipse.

Evidence provenance: original report SHA256 216a10c95e5b442fa92b27189a74ff80643eb5121d3c34111d4cbcbb27679d15, verified unchanged against queue.csv. Deciding outputs, analysis scripts and cached FITS are hashed in evidence_manifest.json; report source is REPORT.md under historical vet126758342. Historical source bytes were not edited. This review uses existing raw-event measurements rather than claiming a fresh extraction of all cadences.


Public evidence: [historical report](../../evidence/126758342/historical/REPORT.md) (historical; superseded by this reconciliation); see the export manifest for deciding artifacts and source/export hashes. Stable review key: P014.
