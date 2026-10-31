# TIC 275065610: bounded evidence reconciliation

Physical verdict: **confirmed**. Five-check review completion: **complete** (representative-event reuse audit, not an all-event rerun). Catalogue novelty is a separate central review.

Period 28.04921 +/- 5e-05 d; detected deep-eclipse epoch 2023.8727 BTJD; representative pipeline depth 51.5 ppt. Original timing uncertainties retained. B-only systems use the observed B as the deep-eclipse epoch.

## Deciding checks

Four raw A eclipses; cycles 0/26/51/52, residuals under 1.6 min. TASOC raw s26 recovers the eclipse (42.9 ppt versus QLP 52.6 ppt). Four pixel regressions put the deficit 2.5–6.6 arcsec from the target and exclude the G12.11 neighbour. Gaia period -0.92 sigma; conjunction offsets about -1 sigma; fitted b_A=0.82 predicts b_B=2.51 and the absent B.

Raw repeated events, eclipse-derived timing, target attribution, a second reduction and Gaia-compatible geometry all pass at the scope permitted by the data. Same-photon reductions check robustness and are not independent observations. The source timing, pixel, pipeline and physical outputs were inspected; representative pixel maps were visually inspected in representative_pixels.jpg. No inherited CONFIRMED label was used as a substitute for these checks.

## Limitations and next check

TASOC depth is diluted and its epoch is about 14 min later than QLP; does not invalidate its eclipse detection. Dark-companion fit neglects a few percent secondary light.

Next check: A future raw A eclipse or double-lined spectrum.

Evidence provenance: original report SHA256 2b44bd41a8c8be4fb022415c0d9f9de2fee8307a7fbdf7f152d4bc6d73e79138, verified unchanged against queue.csv. Deciding outputs, analysis scripts and cached FITS are hashed in evidence_manifest.json; report source is REPORT.md under historical vet275065610. Historical source bytes were not edited. This review uses existing raw-event measurements rather than claiming a fresh extraction of all cadences.


Public evidence: [historical report](../../evidence/275065610/historical/REPORT.md) (historical; superseded by this reconciliation); see the export manifest for deciding artifacts and source/export hashes. Stable review key: P009.
