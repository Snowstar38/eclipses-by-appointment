# TIC 281393563: PROBABLE

Queue position 14; batch02. Review by GPT-6.1 Sol with a fresh GPT-6.1 Terra helper, supervised by Astra. Physical classification and prior-catalogue status are separate.

## Deciding assessment

Repeated deep detached eclipses have a coherent event-derived period and feasible Gaia geometry. Fresh source imaging was attempted, but crowding prevents a secure target assignment.

## Raw events and eclipse period

Three cached QLP SAP_FLUX sectors were checked with QUALITY=0, local quadratic baseline plus trapezoid fits. 6 representative fits were retained in raw-events.json, 6 clear of fit bounds. Depth range 7.027–9.69 percent. Period from representative event centers: 6.149828122486457. Search-cycle counts are conditional on the initial search, not a blind period discovery. No timing uncertainty or ephemeris prediction is claimed.

{
  "period_d": 6.149828122486457,
  "epoch_btjd": 1575.6730668128118,
  "n_events": 6,
  "residual_rms_min": 1.418844494519903,
  "note": "unweighted representative events, conditional on original search cycle counts; no uncertainty inferred"
}

## Source imaging and independent reduction

Sectors 10 and64 contain target-region deficits; sector64 also has a strong off-center deficit. Fixed-position capable-neighbour alternatives have residual ratios only1.03–1.99, with a degenerate free-center fit. This is an unresolved source gate, not unattempted work.

Fresh TESScut cutouts are a distinct custom aperture reduction of the same TESS photons as QLP; they are not SPOC and do not supply an independent telescope. MAST product-inventory queries were attempted and timed out for all ten; this is a service limitation, not absence of products. Signed in/out images use adjacent pre/post windows. Positive-clipped centroids and Gaussian formal errors are diagnostics subject to PRF mismatch; target-specific repeat tests and capable-neighbour comparisons govern attribution.

## Gaia geometry

Photometric period 6.149828122 d versus Gaia 6.149604702 ± 0.00058686 d; difference 0.38 Gaia sigma. Nearest approximate conjunction A: offset -0.047 d; linear covariance error 0.153 d, conservative sum bound 1.102 d. Observed median duration 7.05 h versus approximate central feasibility 9.81 h. Phase uncertainty and approximate geometry are retained rather than treating a linear sigma as exact.

Computed receipt: gaia-geometry.json. Linear covariance propagation uses SB1 correlation order P,gamma,K1,e,omega,Tp; conjunction uses edge-on approximation. The mass-function/MS-radius duration is a feasibility estimate, not a physical fit. Circular/low-eccentricity periastron phases may be weakly constrained.

## Prior EB coverage

no identified prior EB; seven-scope coverage complete: yes. Reused central coverage-matrix.csv and catalogue-scope.json: VSX, SIMBAD primary type, Gaia DR3 EB, Prsa2022, IJspeert2024, Kostov2025 vetted tables3/4, ASAS-SN. SB* or ROT alone are not EB identifications. This scoped result is not an exhaustive discovery claim.

## Completion, limitations and next check

Execution: completed representative full review; scientific ambiguity: The eclipses repeat, but the host is not separated from capable neighbours. Pixel models are degenerate in this crowded field.

Next deciding check: Obtain higher resolution time-series imaging or a validated multi-source PRF difference fit to identify the eclipsing host.

Provenance: cache-manifest.json preserves original cached FITS paths and SHA256; identity-checks.json matches TICID/SECTOR for all30 input QLP files. tesscut-downloads.json records fresh source URLs and zip hashes; signed images and helper evidence have hashes. manifest.json records deliverable checksums. Adapted scripts are retained. No source-paper edits or publication performed.
