# TIC 122024194

CONFIRMED. Execution: complete. Scoped novelty: no identified prior EB.

Raw QLP SAP_FLUX with QUALITY=0 yields 5 representative events in sectors [8, 36, 89]; depths 143.83 to 151.24 ppt. Quadratic local baseline plus trapezoid, native cadence, derives P=9.521588306 d from event centres. Timing RMS=0.584 min; unweighted and conditional on the search cycle counts, without a fitted uncertainty. For two-event solutions, near-zero RMS is algebraic and is not a precision claim. The helper and lead inspected the representative raw event panel and reviewed the deciding measurements; sector-dependent aperture dilution and baseline changes remain in the depths.

Cached eclipse difference image concentrates the lost flux in the target image; target/deficit distance 0.887 arcsec. Flux-capable neighbours are tested by spatial position and mixed own-pixel losses, which alone are not exclusions. Centroid displacements are descriptive, without calibrated uncertainty; bandpass differences, uncatalogued blends and PSF modelling limit attribution.  High PSF fractional residual (0.998) limits the scaled-image model; attribution instead uses localized eclipse deficit and the capable-neighbour comparison. Lead inspected the three-panel image: bright off-target star dominates total light but the eclipse deficit remains at the target, 59.34 arcsec from the only flux-capable catalogued neighbour.

Capable neighbour Gaia DR3 5316688342982264064: catalog separation 58.77 arcsec, required loss 62.83%, own-pixel loss 0.18%, deficit distance 59.34 arcsec. Pixel losses include mixed source flux and are supporting spatial diagnostics.

Independent TESScut pixel aperture extraction sector 62 confirms event depths 116.05, 115.79, 116.18 ppt. Independent 3x3 target aperture with per-cadence faint-pixel background; core medians versus local pre/post baseline, without formal errors or dilution correction. This uses the same TESS images through an independent extraction pipeline, not an independent observation. Gaia coordinates projected through the cutout WCS verify the target position and header sector. Input paths/URIs and SHA256 are preserved in raw-evidence/independent-results.json.

Gaia SB1 P=9.521738143 d, difference -0.21 Gaia sigma. Closest edge-on conjunction A offset 0.00764 d versus linear full SB1 covariance error 0.12863 d; timing differences and propagation limits are retained. Observed median duration 6.79 h versus approximate central main-sequence feasibility 8.63 h; mass function 0.07780 solar masses. This is a geometry feasibility check, not a fitted stellar solution or measured inclination. Linear propagation can be approximate for nearly circular orbits.

Seven-scope central catalogue matrix marks coverage complete and no identified prior EB for this target. SIMBAD SB* alone is not an EB type; Kostov table2 is unvetted. Historical five-arcsecond batteries retain condensed rather than raw per-query receipts; VSX/ASAS-SN cones are 60 arcsec. Scope and alternate-identity limitations apply. See catalogue-review.json and ../shared-catalogues/README.md for exact coverage.

Evidence: raw-evidence/raw-events.json, raw-evidence/qlp-manifest.json, source-review.json, gaia-geometry.json, catalogue-review.json, and provenance hashes.
Contributor note: an automated photometry helper measured representative raw events and checked independent reductions; the lead reviewed the deciding evidence.

Next tests for characterization: exposure-integrated eclipse modelling and stellar/RV constraints; refine dilution with resolved photometry where needed. These are follow-up opportunities rather than missing execution steps.
