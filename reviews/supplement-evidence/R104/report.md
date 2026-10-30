# TIC 100249241

CONFIRMED. Execution: complete. Scoped novelty: no identified prior EB.

Raw QLP SAP_FLUX with QUALITY=0 yields 4 representative events in sectors [15, 41, 82]; depths 114.97–116.56 ppt. Quadratic local baseline plus trapezoid, native cadence, derives P=17.852265983 d from event centres. Timing RMS=1.421 min; unweighted and conditional on the search cycle counts, without a fitted uncertainty. For two-event solutions, near-zero RMS is algebraic and is not a precision claim. The lead inspected the raw event panel.

Cached eclipse deficit peaks at the target pixel, offset 2.492 arcsec. No Gaia G-band flux-capable neighbour is recorded within 60 arcsec. Centroid displacement is descriptive; G/TESS band differences, unresolved or uncatalogued blends and PSF modelling limit this test. High PSF residual limits characterization; attribution uses the deficit peak and neighbour comparison. 

Independent TESScut pixel aperture extraction sector 82 confirms event depths 100.33, 99.25 ppt. Independent 3x3 target aperture with per-cadence faint-pixel background; core medians versus local pre/post baseline, without formal errors or dilution correction. This uses the same TESS images through an independent extraction pipeline, not an independent observation. Gaia coordinates projected through the cutout WCS verify the target position and header sector. Input paths/URIs and SHA256 are preserved in raw-evidence/independent-results.json.

Gaia SB1 P=17.851383953 d, difference 0.22 Gaia sigma. Closest edge-on conjunction A offset -0.07218 d versus linear full SB1 covariance error 0.24995 d; no significant timing contradiction. Observed median duration 5.33 h versus approximate central main-sequence feasibility 9.24 h; mass function 0.09142 solar masses. This is a geometry feasibility check, not a fitted stellar solution or measured inclination. Linear propagation can be approximate for nearly circular orbits.

Seven-scope central catalogue matrix status is no identified prior EB; coverage is yes. See the target-specific matches in catalogue-review.json. SIMBAD SB* alone is not an EB type; Kostov table2 is unvetted. Historical five-arcsecond batteries retain condensed rather than raw per-query receipts; VSX/ASAS-SN cones are 60 arcsec. Scope and alternate-identity limitations apply. See catalogue-review.json and ../shared-catalogues/README.md for exact coverage.

Evidence: raw-evidence/raw-events.json, raw-evidence/qlp-manifest.json, source-review.json, gaia-geometry.json, catalogue-review.json, and provenance hashes.

Independent measurements use core medians rather than the QLP trapezoid depth, so numerical equality of the depths is not assumed. Product-inventory failures are preserved; this check uses an independent aperture extraction, not a separately delivered pipeline product.

Separate central open-release comparison found no exact Gaia/TIC overlap in the available track3/dossier tables; overlap with the embargoed 93-system release is unknown. This is not an additional EB gate. See ../shared-catalogues/README.md.
