# TIC 162075402

CONFIRMED. Full review execution: complete. Scoped novelty: no identified prior EB.

Raw repetition and eclipse period: QLP SAP_FLUX with QUALITY=0 yields 2 representative events in sectors [80], fitted depths 141.79-142.27 ppt. A quadratic local baseline plus trapezoid derives P=5.327671750 d from event centres, timing RMS 0.000 min. Fits use native cadence without exposure integration; timing fits are unweighted and conditional on search cycle counts, without a fitted uncertainty. A two-event zero residual is algebraic, not a precision claim. A fresh GPT-6.1 Terra helper reviewed the raw repetitions and independent reduction; see raw-evidence/rawhelper-summary.md and raw-evidence/pixel-independent-results.json.

Source attribution: Cached eclipse deficit peaks at the target pixel, offset 2.097 arcsec. No Gaia G-band flux-capable neighbour is recorded within 60 arcsec. The exact ASAS-SN ROT: identity and 0.80 arcsec VSX VAR entry are not prior-EB types. Nearby VSX E entries at 14.92, 40.16 and 58.55 arcsec identify distinct Gaia sources with periods 1.29114, 0.307656 and 6.9854 d; none is G-band flux-capable in the cached 60-arcsec source check, and their periods differ from the target primary eclipse period. Centroid displacements are descriptive; G/TESS band differences, uncatalogued or unresolved blends and PSF modelling limit the test. The lead inspected the cached difference-image panel. 

Nearby catalogue EB Gaia DR3 4251816451161098880: G=19.581, required fractional flux loss 363.65 (greater than unity, hence not G-band flux-capable).

Nearby catalogue EB Gaia DR3 4251816554240317568: G=19.160, required fractional flux loss 246.72 (greater than unity, hence not G-band flux-capable).

Nearby catalogue EB Gaia DR3 4251813599322538112: G=16.798, required fractional flux loss 28.13 (greater than unity, hence not G-band flux-capable).

Independent reduction: TARS, sector 80, repeats eclipse depths 131.86, 117.63 ppt. The separate archived light-curve product uses a fixed QLP-measured event shape; the template ties timing/shape but not the independent flux extraction. Product/cutout identity, method, measurements and SHA256 are in raw-evidence/independent-results.json. Product-inventory failures are preserved, not treated as negative observations.

Gaia orbit geometry: SB1 P=5.327763075 d, photometric difference -0.32 Gaia sigma. Closest edge-on conjunction A offset -0.08342 d versus full SB1 covariance linear error 0.19387 d. Neither period nor conjunction reveals a strong contradiction. Observed median duration 4.12 h versus approximate central main-sequence feasibility 6.16 h; mass function 0.14231 solar masses. This is an orbit feasibility check, not fitted inclination, stellar radii or a unique geometry. Linear propagation may be approximate for nearly circular orbits; covariance order and assumptions are preserved in gaia_geometry.py.

Novelty: seven-scope central matrix reports no identified prior EB; coverage yes. Exact IDs and neighbours are separated in catalogue-review.json. SIMBAD SB* and ROT/VAR do not classify an EB; Kostov table2 is unvetted. Historical five-arcsec batteries retain condensed receipts; VSX/ASAS-SN cones are 60 arcsec. Alternate identities and catalogue versions limit this scoped result. Separate open-release comparison found no exact Gaia/TIC overlap in available tables; the embargoed 93-system release overlap is unknown and is not an additional EB gate. See ../shared-catalogues/README.md.

Next deciding test: No unresolved physical veto; resolved multiband eclipse photometry would improve dilution and radii.

Evidence: raw-evidence/raw-events.json, raw-evidence/qlp-manifest.json, raw-evidence/independent-results.json, source-review.json, gaia-geometry.json, catalogue-review.json, lead-input-provenance.json and MANIFEST-SHA256.json.

Bounded depth check in sector80: four matching primary epochs yield QLP core depths 123.73-126.43 ppt versus 97.84-99.23 ppt in the independent 3x3 extraction. Pixel 1x1 depths 106.81-112.03 and 5x5 depths 77.13-78.90 ppt establish aperture dependence in this crowded field; QLP deepest-three depths are 146.89-149.03 ppt. The TARS independent product gives 131.86 and 117.63 ppt with fixed QLP shapes; its QUALITY column is absent and the formal errors omit systematics. These are consistent repeated eclipses but not identical depth estimates; dilution and reduction differences remain characterization limitations. See depth-sanity-162075402.json. Primary period is 5.327672 d; a half-period alias can arise from secondary eclipses and does not replace the full primary repetition.
