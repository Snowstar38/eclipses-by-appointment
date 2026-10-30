# TIC 39069184

PLAUSIBLE. Execution: complete. Scoped novelty: no identified prior EB.

Raw QLP SAP_FLUX with QUALITY=0 yields 6 representative events in sectors [1, 29, 96]; depths 209.62–266.92 ppt. Quadratic local baseline plus trapezoid, native cadence, derives P=3.350034558 d from event centres. Timing RMS=0.331 min; unweighted and conditional on the search cycle counts, without a fitted uncertainty. For two-event solutions, near-zero RMS is algebraic and is not a precision claim. The lead inspected the raw event panel.

Cached eclipse deficit peaks at the target pixel, offset 1.448 arcsec. A flux-capable Gaia neighbour is only 2.21 arcsec away (0.105 TESS pixel). The deficit is nominally closer to the target, but centroid errors are uncalibrated and own-pixel loss mixes the two sources; attribution remains ambiguous at this separation. This prevents a target-specific confirmation despite strong repeated eclipses. Centroid displacement is descriptive; G/TESS band differences, unresolved or uncatalogued blends and PSF modelling limit this test. Lead inspected the cached difference-image panel.

Capable neighbour Gaia DR3 4704376708370040960: catalog separation 2.21 arcsec, required loss 68.27%, own-pixel loss 13.07%, deficit distance 3.58 arcsec. Pixel losses include mixed source flux and are supporting spatial diagnostics.

Independent TESScut pixel aperture extraction sector 28 confirms event depths 178.03, 171.18, 180.40, 175.63, 178.57, 170.92 ppt. Independent 3x3 target aperture with per-cadence faint-pixel background; core medians versus local pre/post baseline, without formal errors or dilution correction. This uses the same TESS images through an independent extraction pipeline, not an independent observation. Gaia coordinates projected through the cutout WCS verify the target position and header sector. Input paths/URIs and SHA256 are preserved in raw-evidence/independent-results.json.

Gaia SB1 P=3.349923348 d, difference 0.91 Gaia sigma. Closest edge-on conjunction A offset 0.03245 d versus linear full SB1 covariance error 0.03525 d; no significant timing contradiction. Observed median duration 3.64 h versus approximate central main-sequence feasibility 4.61 h; mass function 0.11861 solar masses. This is a geometry feasibility check, not a fitted stellar solution or measured inclination. Linear propagation can be approximate for nearly circular orbits.

Seven-scope central catalogue matrix status is no identified prior EB; coverage is yes. See the target-specific matches in catalogue-review.json. SIMBAD SB* alone is not an EB type; Kostov table2 is unvetted. Historical five-arcsecond batteries retain condensed rather than raw per-query receipts; VSX/ASAS-SN cones are 60 arcsec. Scope and alternate-identity limitations apply. See catalogue-review.json and ../shared-catalogues/README.md for exact coverage.

Evidence: raw-evidence/raw-events.json, raw-evidence/qlp-manifest.json, source-review.json, gaia-geometry.json, catalogue-review.json, and provenance hashes.

Physical verdict is PLAUSIBLE because source attribution to the Gaia SB1 remains unresolved against the flux-capable 2.21 arcsec neighbour. Execution is complete; the limitation is scientific ambiguity.

Independent measurements use core medians rather than the QLP trapezoid depth, so numerical equality of the depths is not assumed. Product-inventory failures are preserved; this check uses an independent aperture extraction, not a separately delivered pipeline product.

Separate central open-release comparison found no exact Gaia/TIC overlap in the available track3/dossier tables; overlap with the embargoed 93-system release is unknown. This is not an additional EB gate. See ../shared-catalogues/README.md.
