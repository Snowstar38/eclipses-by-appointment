# TIC 326623940

CONFIRMED. Execution: complete. Scoped novelty: no identified prior EB.

Raw QLP SAP_FLUX with QUALITY=0 yields 6 representative events in sectors [11, 100, 102]; depths 106.83–116.33 ppt. Quadratic local baseline plus trapezoid, native cadence, derives P=7.393782739 d from event centres. Timing RMS=1.262 min; unweighted and conditional on the search cycle counts, without a fitted uncertainty. For two-event solutions, near-zero RMS is algebraic and is not a precision claim. The lead inspected the raw event panel.

Cached eclipse deficit peaks at the target pixel, offset 3.242 arcsec. No Gaia G-band flux-capable neighbour is recorded within 60 arcsec. Centroid displacement is descriptive; G/TESS band differences, unresolved or uncatalogued blends and PSF modelling limit this test. High PSF residual limits characterization; attribution uses the deficit peak and neighbour comparison. 

Independent TESScut pixel aperture extraction sector 65 confirms event depths 100.85, 100.49, 99.68, 99.76 ppt. Independent 3x3 target aperture with per-cadence faint-pixel background; core medians versus local pre/post baseline, without formal errors or dilution correction. This uses the same TESS images through an independent extraction pipeline, not an independent observation. Gaia coordinates projected through the cutout WCS verify the target position and header sector. Input paths/URIs and SHA256 are preserved in raw-evidence/independent-results.json.

Gaia SB1 P=7.393323173 d, difference 0.90 Gaia sigma. Closest edge-on conjunction A offset 0.09756 d versus linear full SB1 covariance error 0.09165 d; no significant timing contradiction. Observed median duration 9.54 h versus approximate central main-sequence feasibility 10.34 h; mass function 0.14891 solar masses. This is a geometry feasibility check, not a fitted stellar solution or measured inclination. Linear propagation can be approximate for nearly circular orbits.

Seven-scope central catalogue matrix status is no identified prior EB; coverage is yes. See the target-specific matches in catalogue-review.json. SIMBAD SB* alone is not an EB type; Kostov table2 is unvetted. Historical five-arcsecond batteries retain condensed rather than raw per-query receipts; VSX/ASAS-SN cones are 60 arcsec. Scope and alternate-identity limitations apply. See catalogue-review.json and ../shared-catalogues/README.md for exact coverage.

Evidence: raw-evidence/raw-events.json, raw-evidence/qlp-manifest.json, source-review.json, gaia-geometry.json, catalogue-review.json, and provenance hashes.

The 0.20 arcsec VSX VAR entry GDS_J1400595-632825 may be the target; exact ASAS-SN ROT: and VAR do not classify an EB. Retain the identity caveat without treating it as prior-EB evidence.

Independent measurements use core medians rather than the QLP trapezoid depth, so numerical equality of the depths is not assumed. Product-inventory failures are preserved; this check uses an independent aperture extraction, not a separately delivered pipeline product.

Separate central open-release comparison found no exact Gaia/TIC overlap in the available track3/dossier tables; overlap with the embargoed 93-system release is unknown. This is not an additional EB gate. See ../shared-catalogues/README.md.
