# TIC 29741740

CONFIRMED. Full review execution: complete. Scoped novelty: no identified prior EB.

Raw repetition and eclipse period: QLP SAP_FLUX with QUALITY=0 yields 5 representative events in sectors [12, 66, 103], fitted depths 116.55-137.57 ppt. A quadratic local baseline plus trapezoid derives P=11.027857969 d from event centres, timing RMS 1.337 min. Fits use native cadence without exposure integration; timing fits are unweighted and conditional on search cycle counts, without a fitted uncertainty. A two-event zero residual is algebraic, not a precision claim. A fresh GPT-6.1 Terra helper reviewed the raw repetitions and independent reduction; see raw-evidence/rawhelper-summary.md and raw-evidence/pixel-independent-results.json.

Source attribution: Cached eclipse deficit peaks at the target pixel, offset 5.919 arcsec. The G-band flux-capable neighbour is 43.24 arcsec from the target and 50.58 arcsec from the eclipse deficit; the disappearing source is localized near the target rather than that neighbour. The field is crowded; faint neighbours and colour-dependent flux limits remain caveats. Centroid displacements are descriptive; G/TESS band differences, uncatalogued or unresolved blends and PSF modelling limit the test. The lead inspected the cached difference-image panel. 

Flux-capable Gaia DR3 5930552522426138880: separation 43.24 arcsec, required eclipse loss 39.53%, own-pixel loss 0.29%, deficit distance 50.58 arcsec. Own-pixel flux is mixed and does not alone exclude contamination.

Independent reduction: TESS-SPOC, sector 12, repeats eclipse depths 124.73 ppt. The separate archived light-curve product uses a fixed QLP-measured event shape; the template ties timing/shape but not the independent flux extraction. Product/cutout identity, method, measurements and SHA256 are in raw-evidence/independent-results.json. Product-inventory failures are preserved, not treated as negative observations.

Gaia orbit geometry: SB1 P=11.028952113 d, photometric difference -0.82 Gaia sigma. Closest edge-on conjunction A offset -0.12059 d versus full SB1 covariance linear error 0.12664 d. Neither period nor conjunction reveals a strong contradiction. Observed median duration 6.55 h versus approximate central main-sequence feasibility 9.15 h; mass function 0.14115 solar masses. This is an orbit feasibility check, not fitted inclination, stellar radii or a unique geometry. Linear propagation may be approximate for nearly circular orbits; covariance order and assumptions are preserved in gaia_geometry.py.

Novelty: seven-scope central matrix reports no identified prior EB; coverage yes. Exact IDs and neighbours are separated in catalogue-review.json. SIMBAD SB* and ROT/VAR do not classify an EB; Kostov table2 is unvetted. Historical five-arcsec batteries retain condensed receipts; VSX/ASAS-SN cones are 60 arcsec. Alternate identities and catalogue versions limit this scoped result. Separate open-release comparison found no exact Gaia/TIC overlap in available tables; the embargoed 93-system release overlap is unknown and is not an additional EB gate. See ../shared-catalogues/README.md.

Next deciding test: No unresolved physical veto; resolved multiband eclipse photometry would improve dilution and radii.

Evidence: raw-evidence/raw-events.json, raw-evidence/qlp-manifest.json, raw-evidence/independent-results.json, source-review.json, gaia-geometry.json, catalogue-review.json, lead-input-provenance.json and MANIFEST-SHA256.json.
