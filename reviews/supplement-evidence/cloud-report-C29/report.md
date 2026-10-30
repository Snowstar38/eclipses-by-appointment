# TIC 285942031: PROBABLE

Queue position 12; batch02. Review by GPT-6.1 Sol with a fresh GPT-6.1 Terra helper, supervised by Astra. Physical classification and prior-catalogue status are separate.

## Deciding assessment

Deep, repeated discrete eclipses are real and source fits favor the target in two detector sectors. The Gaia orbit has material timing tension, so the geometry check is not fully passed.

## Raw events and eclipse period

Three cached QLP SAP_FLUX sectors were checked with QUALITY=0, local quadratic baseline plus trapezoid fits. 5 representative fits were retained in raw-events.json, 5 clear of fit bounds. Depth range 10.113–11.857 percent. Period from representative event centers: 2.6068541455671475. Search-cycle counts are conditional on the initial search, not a blind period discovery. No timing uncertainty or ephemeris prediction is claimed.

{
  "period_d": 2.6068541455671475,
  "epoch_btjd": 1795.1495351827527,
  "n_events": 5,
  "residual_rms_min": 1.9711095797469935,
  "note": "unweighted representative events, conditional on original search cycle counts; no uncertainty inferred"
}

## Source imaging and independent reduction

Signed difference images, Gaussian free-center diagnostics and fixed-coordinate target-versus-neighbour fits are preserved in raw-evidence. The fixed-position neighbour/target residual sums of squares consistently favor the target. Ratios are descriptive, not formal significance; source PRF mismatch is a limitation.

Fresh TESScut cutouts are a distinct custom aperture reduction of the same TESS photons as QLP; they are not SPOC and do not supply an independent telescope. MAST product-inventory queries were attempted and timed out for all ten; this is a service limitation, not absence of products. Signed in/out images use adjacent pre/post windows. Positive-clipped centroids and Gaussian formal errors are diagnostics subject to PRF mismatch; target-specific repeat tests and capable-neighbour comparisons govern attribution.

## Gaia geometry

Photometric period 2.606854146 d versus Gaia 2.607369245 ± 0.00013636 d; difference -3.78 Gaia sigma. Nearest approximate conjunction A: offset -0.355 d; linear covariance error 0.074 d, conservative sum bound 0.342 d. Observed median duration 3.74 h versus approximate central feasibility 5.47 h. Phase uncertainty and approximate geometry are retained rather than treating a linear sigma as exact.

Computed receipt: gaia-geometry.json. Linear covariance propagation uses SB1 correlation order P,gamma,K1,e,omega,Tp; conjunction uses edge-on approximation. The mass-function/MS-radius duration is a feasibility estimate, not a physical fit. Circular/low-eccentricity periastron phases may be weakly constrained.

## Prior EB coverage

no identified prior EB; seven-scope coverage complete: yes. Reused central coverage-matrix.csv and catalogue-scope.json: VSX, SIMBAD primary type, Gaia DR3 EB, Prsa2022, IJspeert2024, Kostov2025 vetted tables3/4, ASAS-SN. SB* or ROT alone are not EB identifications. This scoped result is not an exhaustive discovery claim.

## Completion, limitations and next check

Execution: completed representative full review; scientific ambiguity: Gaia period differs by -3.78 sigma; approximate conjunction is 0.355 d off versus linear covariance error 0.074 d. The conservative sum error is 0.342 d; a nonlinear orbital posterior or fresh RV fit is needed before treating this as the Gaia eclipsing system.

Next deciding check: Reassess Gaia orbital uncertainties/correlations or obtain an updated radial-velocity orbit to resolve the eclipse-versus-Gaia timing tension.

Provenance: cache-manifest.json preserves original cached FITS paths and SHA256; identity-checks.json matches TICID/SECTOR for all30 input QLP files. tesscut-downloads.json records fresh source URLs and zip hashes; signed images and helper evidence have hashes. manifest.json records deliverable checksums. Adapted scripts are retained. No source-paper edits or publication performed.
