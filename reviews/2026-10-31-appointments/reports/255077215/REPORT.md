# TIC 255077215: bounded evidence reconciliation

Physical verdict: **confirmed**. Five-check review completion: **complete** (representative-event reuse audit, not an all-event rerun). Catalogue novelty is a separate central review.

Period 26.26204 +/- 1.6e-05 d; detected deep-eclipse epoch 1637.34726 BTJD; representative pipeline depth 56.0 ppt. Original timing uncertainties retained. B-only systems use the observed B as the deep-eclipse epoch.

## Deciding checks

Four A and three B events; primary linear timing spans96 cycles. TESS-SPOC and eleanor recover earlier eclipses. s39 pixel deficits are4.9arcsec(A) and3.0arcsec(B) from target, and primary dilution rules out neighbours. Gaia P -0.13sigma; LD fit e0.340, omega203.8deg agrees with orbit.

Raw repeated events, eclipse-derived timing, target attribution, a second reduction and Gaia-compatible geometry all pass at the scope permitted by the data. Same-photon reductions check robustness and are not independent observations. The source timing, pixel, pipeline and physical outputs were inspected; representative pixel maps were visually inspected in representative_pixels.jpg. No inherited CONFIRMED label was used as a substitute for these checks.

## Limitations and next check

S65 secondary arrives31–42min late after common-mode correction; unexplained. This does not remove repeated A timing or agreement of earlier B events. Quoted period error is original formal fit and predictions need timing-systematic allowance.

Next check: Clean secondary to resolve s65 timing shift.

Evidence provenance: original report SHA256 1c6cd9b663daf6b4c1c9e0621b11cabe4a486f4550d690aed41e53ece8beb332, verified unchanged against queue.csv. Deciding outputs, analysis scripts and cached FITS are hashed in evidence_manifest.json; report source is REPORT.md under historical vet255077215. Historical source bytes were not edited. This review uses existing raw-event measurements rather than claiming a fresh extraction of all cadences.


Public evidence: [historical report](../../evidence/255077215/historical/REPORT.md) (historical; superseded by this reconciliation); see the export manifest for deciding artifacts and source/export hashes. Stable review key: P012.
