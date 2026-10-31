# Independent helper audit

Scope: ten fixed queue entries; inspected representative raw-event and difference-image contact sheets, 377389892 alias fold and the revised 407207285 cutout. Independently recomputed weighted linear ephemerides with least squares from measured, timing-usable centers, not predicted event times. The reproducible script and full numerical output including SHA-256 of each measurement JSON, raw windows and deciding cutout JSON are `helper/refit.py` and `helper/refit.txt`. They are a refit of saved measured centers, not independent extraction of raw flux or independent observations. Epoch is the fitted reference at the minimum measured cycle; selected same-kind event, primary by convention unless independently identified. Error is the stated half-cadence-or-formal weighted covariance with inflation if reduced chi-square >1, not total uncertainty. Screening cycle assignment is not a blind search of all aliases.

| TIC | usable events | Period days | fit error days | Epoch BTJD | median fitted depth ppt | Gaia closest conjunction offset / linear covariance days |
|---|---:|---:|---:|---:|---:|---:|
|377389892|11|4.5881927790|0.000009692|1875.076828|227.45|0.0287 / 0.0682|
|88811793|10|7.4357138600|0.00001722|1660.055392|63.74|0.0819 / 0.3482|
|467753507|4|9.9441928263|0.00001585|2917.634183|30.16|0.1555 / 0.2391|
|350760292|4|4.6960724668|0.0003660|3805.776681|62.87|0.0399 / 0.5407|
|371241950|13|5.8085988833|0.000006663|1575.385620|83.56|0.1723 / 0.0952|
|407207285|6|12.8149004912|0.00003923|1767.675037|67.19|0.1645 / 0.1043|
|177257211|17|3.5443290949|0.000003074|1329.024558|55.82|0.0426 / 0.1043|
|29114881|6|12.6025319623|0.00003144|2478.484406|57.39|0.0282 / 1.0251|
|77605102|5|11.2688089976|0.00001406|1548.900078|167.86|-0.2980 / 0.2565|
|35635884|8|5.5005487862|0.00001077|2203.820743|117.74|-0.0088 / 0.1319|

All ten values agree with lead fits. The Gaia offsets and uncertainties above reproduce saved geometry; the linear uncertainties rely on Gaia covariance and edge-on conjunction approximation, not a sigma rejection rule. Duration comparison is approximate and does not fit inclination or component radii. Single-sector 350760292 timing is necessarily short-baseline and the P/2 and 2P possibilities are not excluded solely by this fit; historical sector39 cutout supplies earlier observations, while the Gaia P=4.6961324 d supports the adopted period. For other systems the repeated same-selected-kind events support the adopted photometric cycle count and Gaia provides an independent orbital-period constraint, though subtle eclipses at other phases and twice-period symmetry cannot be ruled out from selected windows alone.

377389892: inspected fold shows deep primary every 4.588 d and a much shallower feature at half phase. Folding at 1.147 d overlays deep eclipse, shallow eclipse and out-of-eclipse points; a quarter-period orbital interpretation does not reproduce equal events. The catalogued VSX EA match concerns novelty separately from the physical association. The fold PNG supports 4.588 d against the catalog alias; selected timing uses the deeper event.

88811793: target deficit centroid is 0.087 pixel from target, versus approximately 0.75 pixel from the capable neighbor at 14.54 arcsec; another capable source is 27.33 arcsec away. The image favors target, but the close neighbor is unresolved at TESS scale without calibrated multisource PRF localization; PROBABLE is appropriate. Pixel fractional losses are blended-light losses, not the source-intrinsic eclipse required by a particular neighbor.

407207285: inspected the revised two-event long-window sector17 cutout. Target deficit centroid offset is 0.142 pixel; target pixel contains the peak. Background-subtracted 1/3/5 pixel aperture depths are 69.28/68.37/67.49 ppt versus raw median 67.19 ppt. The closest potentially concerning 18.27 arcsec Gaia source would require 2.53 times its full light under the stated flux budget; no catalogued neighbor in the saved 60 arcsec list is capable under that approximation. Previous short-duration extraction underestimates depth; use revised cutout rather than the original 6-ppt output. Cutout extraction reuses TESS photons and is not an independent observation. Residual model and unlisted/unresolved stars remain limitations.

Other target deficit peaks and neighboring Gaia locations were inspected in the contact sheet. Capable catalog neighbors for 350760292, 371241950, 29114881 and 35635884 lie away from the target-centered deficit; 350760292 is crowded with a poor total-light PSF residual, so centroid interpretation is approximate. No capable catalog neighbors appear in the saved lists for 377389892, 467753507, 177257211 and 77605102. Target-centered morphology and flux-budget tests support the lead conclusions at TESS resolution, subject to unresolved and uncatalogued contaminants. Fractional pixel losses cannot establish intrinsic neighbor eclipse depths. Sector-dependent aperture depths and alternative extraction use same photons.

Artifact hashes: each numerical data and deciding difference JSON hash is in `helper/refit.txt`; the lead retains FITS, alternate-reduction, geometry and report hashes in its SHA256SUMS. Lead follow-up resolution: `source_report` for 407207285 was corrected to the revised decisive artifact `407207285/revised-cutout/diff_revised-long-window.json` SHA256 b837d4a84e02ba24db95029fc5f606537d252b19fd74577cacc195639ee06ed7. Preserve both provenance and this distinction.

Lead follow-up: helper numerical script was rerun unchanged against frozen current geometry, updating the407207285 offset to0.1645d and refreshing refit.txt hashes. This narrow update does not constitute an additional independent helper extraction.
