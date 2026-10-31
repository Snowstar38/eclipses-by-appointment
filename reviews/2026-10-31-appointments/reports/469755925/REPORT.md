# TIC 469755925: bounded evidence reconciliation

Physical verdict: **confirmed**. Five-check review completion: **complete** (representative-event reuse audit, not an all-event rerun). Catalogue novelty is a separate central review.

Period 23.322969 +/- 1.4e-05 d; detected deep-eclipse epoch 1675.73779 BTJD; representative pipeline depth 40.5 ppt. Original timing uncertainties retained. B-only systems use the observed B as the deep-eclipse epoch.

## Deciding checks

Three A and five B events across four sectors; joint timing 6.74/5 dof and Gaia P -0.08 sigma. Up to five pipelines recover the eclipses. New sector13 per-pixel regression locates A deficit 2.13 arcsec from target, target depth 40.18 +/-0.78 ppt, 76 cadences (12 in core); G12.44 at74.8 arcsec shows -0.65 ppt, versus required137 ppt. B deficit offset2.75 arcsec. Mass function0.01219 Msun and central duration support an M-dwarf companion.

Raw repeated events, eclipse-derived timing, target attribution, a second reduction and Gaia-compatible geometry all pass at the scope permitted by the data. Same-photon reductions check robustness and are not independent observations. The source timing, pixel, pipeline and physical outputs were inspected; representative pixel maps were visually inspected in representative_pixels.jpg. No inherited CONFIRMED label was used as a substitute for these checks.

## Limitations and next check

S94 A is quality-flagged; confirmation also rests on clean s13 and s67 A events. B pixel depth5.93 +/-0.81 ppt exceeds pipeline2.8–4.0 ppt; low-S/N/background-template extraction is attribution only, not adopted depth.

Next check: Another clean secondary for depth and geometry.

Evidence provenance: original report SHA256 8c1f2cf4693ead5144a715e9010b8dc0e3090b521411d045082f993aa18e299c, verified unchanged against queue.csv. Deciding outputs, analysis scripts and cached FITS are hashed in evidence_manifest.json; report source is REPORT.md under historical vet469755925. Historical source bytes were not edited. This review uses existing raw-event measurements rather than claiming a fresh extraction of all cadences.

Pixel centroid caveat: positive-clipped centroids within a target-centered5x5 box are descriptive offsets, not calibrated uncertainties or exclusion radii. Formal pixel errors omit correlated noise; unresolved faint blends remain possible. Helper inspection is recorded in HELPER-AUDIT.md.


Public evidence: [historical report](../../evidence/469755925/historical/REPORT.md) (historical; superseded by this reconciliation); see the export manifest for deciding artifacts and source/export hashes. Stable review key: P010.
