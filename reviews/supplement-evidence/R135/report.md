# TIC 42318308

CONFIRMED. Execution: complete. Scoped novelty: no identified prior EB.

Raw QLP SAP_FLUX with QUALITY=0 yields 6 representative events in sectors [14, 53, 81]; depths 137.95 to 151.98 ppt. Quadratic local baseline plus trapezoid, native cadence, derives P=2.852761729 d from event centres. Timing RMS=2.667 min; unweighted and conditional on the search cycle counts, without a fitted uncertainty. For two-event solutions, near-zero RMS is algebraic and is not a precision claim. The helper and lead inspected the representative raw event panel and reviewed the deciding measurements; sector-dependent aperture dilution and baseline changes remain in the depths.

Cached eclipse difference image concentrates the lost flux in the target image; target/deficit distance 4.268 arcsec. Flux-capable neighbours are tested by spatial position and mixed own-pixel losses, which alone are not exclusions. Centroid displacements are descriptive, without calibrated uncertainty; bandpass differences, uncatalogued blends and PSF modelling limit attribution.  High PSF fractional residual (0.523) limits the scaled-image model; attribution instead uses localized eclipse deficit and the capable-neighbour comparison.

Capable neighbour Gaia DR3 2043690510556208128: catalog separation 16.59 arcsec, required loss 49.67%, own-pixel loss 8.49%, deficit distance 14.09 arcsec. Pixel losses include mixed source flux and are supporting spatial diagnostics.

Capable neighbour Gaia DR3 2043690544915953664: catalog separation 25.25 arcsec, required loss 82.77%, own-pixel loss 7.96%, deficit distance 29.96 arcsec. Pixel losses include mixed source flux and are supporting spatial diagnostics.

Independent TESScut pixel aperture extraction sector 40 confirms event depths 70.80, 76.06, 76.34, 73.03, 76.34, 75.15, 75.91, 72.24 ppt. Independent 3x3 target aperture with per-cadence faint-pixel background; core medians versus local pre/post baseline, without formal errors or dilution correction. This uses the same TESS images through an independent extraction pipeline, not an independent observation. Gaia coordinates projected through the cutout WCS verify the target position and header sector. Input paths/URIs and SHA256 are preserved in raw-evidence/independent-results.json.

Gaia SB1 P=2.852714047 d, difference 0.53 Gaia sigma. Closest edge-on conjunction A offset 0.01581 d versus linear full SB1 covariance error 0.05025 d; timing differences and propagation limits are retained. Observed median duration 2.96 h versus approximate central main-sequence feasibility 4.19 h; mass function 0.08975 solar masses. This is a geometry feasibility check, not a fitted stellar solution or measured inclination. Linear propagation can be approximate for nearly circular orbits.

Seven-scope central catalogue matrix marks coverage complete and no identified prior EB for this target. SIMBAD SB* alone is not an EB type; Kostov table2 is unvetted. Historical five-arcsecond batteries retain condensed rather than raw per-query receipts; VSX/ASAS-SN cones are 60 arcsec. Scope and alternate-identity limitations apply. See catalogue-review.json and ../shared-catalogues/README.md for exact coverage.

Evidence: raw-evidence/raw-events.json, raw-evidence/qlp-manifest.json, source-review.json, gaia-geometry.json, catalogue-review.json, and provenance hashes.
Contributor note: an automated photometry helper measured representative raw events and checked independent reductions; the lead reviewed the deciding evidence.

Next tests for characterization: exposure-integrated eclipse modelling and stellar/RV constraints; refine dilution with resolved photometry where needed. These are follow-up opportunities rather than missing execution steps.
