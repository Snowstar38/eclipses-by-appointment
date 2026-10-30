# TIC 320195702

CONFIRMED. Execution: complete. Scoped novelty: no identified prior EB.

Raw QLP SAP_FLUX with QUALITY=0 yields 4 representative events in sectors [20, 46, 72]; depths 113.52 to 118.89 ppt. Quadratic local baseline plus trapezoid, native cadence, derives P=2.583171934 d from event centres. Timing RMS=2.603 min; unweighted and conditional on the search cycle counts, without a fitted uncertainty. For two-event solutions, near-zero RMS is algebraic and is not a precision claim. The helper and lead inspected the representative raw event panel and reviewed the deciding measurements; sector-dependent aperture dilution and baseline changes remain in the depths.

Cached difference-image deficit peaks at the target pixel; target/deficit distance 3.941 arcsec. No Gaia G-band flux-capable neighbour within the cached 60 arcsec search. Centroid displacements are descriptive, without calibrated uncertainty; G/TESS band differences, uncatalogued blends and PSF modelling limit the test. 

Independent TESScut pixel aperture extraction sector 45 confirms event depths 96.48, 95.95, 96.92, 96.90, 95.89, 95.42, 95.24, 96.24, 96.01 ppt. Independent 3x3 target aperture with per-cadence faint-pixel background; core medians versus local pre/post baseline, without formal errors or dilution correction. This uses the same TESS images through an independent extraction pipeline, not an independent observation. Gaia coordinates projected through the cutout WCS verify the target position and header sector. Input paths/URIs and SHA256 are preserved in raw-evidence/independent-results.json.

Gaia SB1 P=2.583194044 d, difference -0.42 Gaia sigma. Closest edge-on conjunction A offset -0.02825 d versus linear full SB1 covariance error 0.03575 d; timing differences and propagation limits are retained. Observed median duration 2.87 h versus approximate central main-sequence feasibility 4.55 h; mass function 0.09787 solar masses. This is a geometry feasibility check, not a fitted stellar solution or measured inclination. Linear propagation can be approximate for nearly circular orbits.

Seven-scope central catalogue matrix marks coverage complete and no identified prior EB for this target. SIMBAD SB* alone is not an EB type; Kostov table2 is unvetted. Historical five-arcsecond batteries retain condensed rather than raw per-query receipts; VSX/ASAS-SN cones are 60 arcsec. Scope and alternate-identity limitations apply. See catalogue-review.json and ../shared-catalogues/README.md for exact coverage.

Evidence: raw-evidence/raw-events.json, raw-evidence/qlp-manifest.json, source-review.json, gaia-geometry.json, catalogue-review.json, and provenance hashes.
Contributor note: an automated photometry helper measured representative raw events and checked independent reductions; the lead reviewed the deciding evidence.
