# TIC 356435413: bounded evidence reconciliation

Physical verdict: **confirmed**. Five-check review completion: **complete** (representative-event reuse audit, not an all-event rerun). Catalogue novelty is a separate central review.

Period 27.476839 +/- 1.5e-05 d; detected deep-eclipse epoch 1984.25002 BTJD; representative pipeline depth 17.0 ppt. Original timing uncertainties retained. B-only systems use the observed B as the deep-eclipse epoch.

## Deciding checks

Five B events, up to five reductions; cycles0/1/27/28/54 and residuals <=1.4min. Difference images s79/s53 peak at target; neighbours show <=0.2% against1.6–1.8%. Gaia P -0.24sigma and conjunction timing -0.4 to-0.5sigma; geometry predicts missing A, with b_A/(R1+R2) about1.6.

Raw repeated events, eclipse-derived timing, target attribution, a second reduction and Gaia-compatible geometry all pass at the scope permitted by the data. Same-photon reductions check robustness and are not independent observations. The source timing, pixel, pipeline and physical outputs were inspected; representative pixel maps were visually inspected in representative_pixels.jpg. No inherited CONFIRMED label was used as a substitute for these checks.

## Limitations and next check

CTOI356435413.01 is a prior planet-candidate signal at matching eclipse period; annotate separately from EB novelty. Original report overstates 1.5arcsec target offset: that is deficit-to-light centroid; s79 coordinates imply ~2arcsec to target, s53 ~3.6arcsec. No full limb-darkened grazing fit.

Next check: Grazing-occultation model or spectrum to test light ratio.

Evidence provenance: original report SHA256 d5123e42951c11bd407ab1386a9c706cc351c04486af44a3fd8b23ad47346b28, verified unchanged against queue.csv. Deciding outputs, analysis scripts and cached FITS are hashed in evidence_manifest.json; report source is REPORT.md under historical vet356435413. Historical source bytes were not edited. This review uses existing raw-event measurements rather than claiming a fresh extraction of all cadences.


Public evidence: [historical report](../../evidence/356435413/historical/REPORT.md) (historical; superseded by this reconciliation); see the export manifest for deciding artifacts and source/export hashes. Stable review key: P011.
