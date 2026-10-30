# TIC 156851362

CONFIRMED. Full review execution: complete. Scoped novelty: no identified prior EB.

Raw repetition and eclipse period: QLP SAP_FLUX with QUALITY=0 yields 2 representative events in sectors [72], fitted depths 124.76-129.83 ppt. A quadratic local baseline plus trapezoid derives P=4.033256871 d from event centres, timing RMS 0.000 min. Fits use native cadence without exposure integration; timing fits are unweighted and conditional on search cycle counts, without a fitted uncertainty. A two-event zero residual is algebraic, not a precision claim. A fresh GPT-6.1 Terra helper reviewed the raw repetitions and independent reduction; see raw-evidence/rawhelper-summary.md and raw-evidence/pixel-independent-results.json.

Source attribution: Cached eclipse deficit peaks at the target pixel, offset 1.239 arcsec. No Gaia G-band flux-capable neighbour is recorded within 60 arcsec. Centroid displacements are descriptive; G/TESS band differences, uncatalogued or unresolved blends and PSF modelling limit the test. 

Independent reduction: SPOC, sector 72, repeats eclipse depths 118.22, 122.98 ppt. The separate archived light-curve product uses a fixed QLP-measured event shape; the template ties timing/shape but not the independent flux extraction. Product/cutout identity, method, measurements and SHA256 are in raw-evidence/independent-results.json. Product-inventory failures are preserved, not treated as negative observations.

Gaia orbit geometry: SB1 P=4.033324341 d, photometric difference -0.37 Gaia sigma. Closest edge-on conjunction A offset -0.08128 d versus full SB1 covariance linear error 0.15110 d. Neither period nor conjunction reveals a strong contradiction. Observed median duration 4.25 h versus approximate central main-sequence feasibility 5.09 h; mass function 0.05981 solar masses. This is an orbit feasibility check, not fitted inclination, stellar radii or a unique geometry. Linear propagation may be approximate for nearly circular orbits; covariance order and assumptions are preserved in gaia_geometry.py.

Novelty: seven-scope central matrix reports no identified prior EB; coverage yes. Exact IDs and neighbours are separated in catalogue-review.json. SIMBAD SB* and ROT/VAR do not classify an EB; Kostov table2 is unvetted. Historical five-arcsec batteries retain condensed receipts; VSX/ASAS-SN cones are 60 arcsec. Alternate identities and catalogue versions limit this scoped result. Separate open-release comparison found no exact Gaia/TIC overlap in available tables; the embargoed 93-system release overlap is unknown and is not an additional EB gate. See ../shared-catalogues/README.md.

Next deciding test: No unresolved physical veto; resolved multiband eclipse photometry would improve dilution and radii.

Evidence: raw-evidence/raw-events.json, raw-evidence/qlp-manifest.json, raw-evidence/independent-results.json, source-review.json, gaia-geometry.json, catalogue-review.json, lead-input-provenance.json and MANIFEST-SHA256.json.

The two fitted QLP events span approximately four primary cycles. Five independently extracted pixel dips recover the approximately4.03 d repetition. The two-event photometric period has no fitted uncertainty; this is sufficient repetition evidence without a precise ephemeris claim.
