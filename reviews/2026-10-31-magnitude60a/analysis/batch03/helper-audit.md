# Independent helper audit

I inspected both ten-target contact sheets containing the raw SAP events and historical difference images, the measured time series, the raw FITS cutout identity receipt, and the Gaia geometry implementation. I independently fitted a Gaussian eclipse plus linear baseline to each usable raw-window event, then fitted the resulting measured centers against cycle number by unweighted least squares. This changes the shape and weighting of the timing estimator and is a robustness check, not an independent observation or a calibrated uncertainty. Exact refit centers, per-target historical JSON/PNG/Gaia JSON, raw-window and measurement SHA-256 digests, selected QLP FITS digests, and original cutout hashes and WCS identity receipts are in helper-numerical-audit.json; executable method is helper-refit.py. The cutout sector header and target WCS position agree with the historical image identity for all ten. Gaussian and lead period estimates (days):

| TIC | Gaussian | Lead | Target attribution |
|---|---:|---:|---|
| 252737077 | 10.20344324 | 10.20344459 | Deficit centroid 0.20 px from target, 2.06 and 2.72 px from capable neighbors; severe crowding and dilution, poor total-light PSF fit. |
| 240771237 | 5.49610833 | 5.49611006 | Deficit 0.07 px from target versus 1.65 px from capable neighbor. |
| 369118947 | 5.35931325 | 5.35927348 | Deficit 0.18 px from target versus 2.64 px from capable neighbor; crowded field. |
| 399238907 | 4.14450970 | 4.14430546 | Deficit 0.13 px from target versus 0.73 px or farther from capable neighbors; only sector 80, five repeats. |
| 146319847 | 8.87055774 | 8.87055767 | Deficit 0.10 px from target versus 1.53 px from capable neighbor; crowded field. |
| 466690912 | 2.11596676 | 2.11596584 | Deficit 0.31 px from target versus 2.84 px from capable neighbor. |
| 436092743 | 13.12907339 | 13.12907240 | Deficit target-centered; no capable catalogued neighbor within 60 arcsec. |
| 38850860 | 8.41459163 | 8.41459320 | Deficit target-centered; no capable catalogued neighbor within 60 arcsec. |
| 140281693 | 3.87198205 | 3.87198202 | Deficit 0.10 px from target versus 1.91 px or farther from capable neighbors; poor total-light PSF fit. |
| 128460489 | 6.36287184 | 6.36287320 | Deficit 0.270 px from target and 0.516 px from closest capable neighbor; same rounded pixel, attribution unresolved. |

Raw windows show repeated dips, and free-shape measured midpoints rather than predicted stack centers support the listed cycle fits. The 436092743 raw dips alternate approximately 153 and 100 ppt; fitting odd deeper events alone gives 13.12907 d, while 6.56454 d is the alternating-event interval rather than the full orbit. For 399238907, full Gaia NSS period 4.1442204 d agrees with 4.1443055 d measured, unlike historical queue seed 4.14670 d. The five events cover just one sector and hence timing systematics remain. Other timings are selected repeating eclipses and their deeper/secondary identity is not established by this audit; no blind alias search claimed.

Historical cutout aperture measurements provide an alternative reduction of the same photons. Centroid comparisons are descriptive and uncalibrated; total-light PSF residuals near unity are poor in crowded cases and do not by themselves localize the eclipse. A local pixel fractional loss cannot be directly compared to a source-intrinsic required eclipse depth, particularly for the unresolved 11.02 arcsec neighbor of 128460489. I recommend PROBABLE for that target pending resolved observations or calibrated multi-source localization, and support the other nine as confirmed subject to their stated limitations.

I examined the Gaia geometry calculation: it maps the full NSS period, eccentricity, argument and periastron epoch to both edge-on conjunctions and propagates the corresponding covariance; the estimated central duration rests on approximate masses and radii and is not a full binary solution. These are consistency checks rather than calibrated significance vetoes. No material geometry mismatch requiring rejection emerged. The helper did not use historical screening verdicts as decisions or edit public files.
