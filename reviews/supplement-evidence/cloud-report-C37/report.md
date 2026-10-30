# TIC 93783392: CONFIRMED

Queue position 20; batch02. Review by GPT-6.1 Sol with a fresh GPT-6.1 Terra helper, supervised by Astra. Physical classification and prior-catalogue status are separate.

## Deciding assessment

Repeated discrete eclipses are remeasured in raw QLP flux with a coherent event-derived period. Fresh custom TESScut extraction recovers the deficit, and source tests favor the target against all catalogue neighbours capable under the conservative magnitude limit.

## Raw events and eclipse period

Three cached QLP SAP_FLUX sectors were checked with QUALITY=0, local quadratic baseline plus trapezoid fits. 6 representative fits were retained in raw-events.json, 6 clear of fit bounds. Depth range 2.665–3.25 percent. Period from representative event centers: 3.8724081070823737. Search-cycle counts are conditional on the initial search, not a blind period discovery. No timing uncertainty or ephemeris prediction is claimed.

{
  "period_d": 3.8724081070823737,
  "epoch_btjd": 1630.7599836800352,
  "n_events": 6,
  "residual_rms_min": 3.507427667895757,
  "note": "unweighted representative events, conditional on original search cycle counts; no uncertainty inferred"
}

## Source imaging and independent reduction

Signed difference images, Gaussian free-center diagnostics and fixed-coordinate target-versus-neighbour fits are preserved in raw-evidence. The fixed-position neighbour/target residual sums of squares consistently favor the target. Ratios are descriptive, not formal significance; source PRF mismatch is a limitation.

Fresh TESScut cutouts are a distinct custom aperture reduction of the same TESS photons as QLP; they are not SPOC and do not supply an independent telescope. MAST product-inventory queries were attempted and timed out for all ten; this is a service limitation, not absence of products. Signed in/out images use adjacent pre/post windows. Positive-clipped centroids and Gaussian formal errors are diagnostics subject to PRF mismatch; target-specific repeat tests and capable-neighbour comparisons govern attribution.

## Gaia geometry

Photometric period 3.872408107 d versus Gaia 3.871849592 ± 0.00099811 d; difference 0.56 Gaia sigma. Nearest approximate conjunction A: offset 0.129 d; linear covariance error 0.361 d, conservative sum bound 0.973 d. Observed median duration 5.58 h versus approximate central feasibility 7.43 h. Phase uncertainty and approximate geometry are retained rather than treating a linear sigma as exact.

Computed receipt: gaia-geometry.json. Linear covariance propagation uses SB1 correlation order P,gamma,K1,e,omega,Tp; conjunction uses edge-on approximation. The mass-function/MS-radius duration is a feasibility estimate, not a physical fit. Circular/low-eccentricity periastron phases may be weakly constrained.

## Prior EB coverage

no identified prior EB; seven-scope coverage complete: yes. Reused central coverage-matrix.csv and catalogue-scope.json: VSX, SIMBAD primary type, Gaia DR3 EB, Prsa2022, IJspeert2024, Kostov2025 vetted tables3/4, ASAS-SN. SB* or ROT alone are not EB identifications. This scoped result is not an exhaustive discovery claim.

## Completion, limitations and next check

Execution: completed representative full review; scientific ambiguity: No exhaustive event/sector fit or detailed binary model; custom extraction shares TESS photons; 60 arcsec TIC neighbour search and uncalibrated PRF systematics limit the source assessment.

Next deciding check: Optional spectroscopy or higher spatial resolution photometry would refine characterization; no additional deciding gate is required by this representative review.

Provenance: cache-manifest.json preserves original cached FITS paths and SHA256; identity-checks.json matches TICID/SECTOR for all30 input QLP files. tesscut-downloads.json records fresh source URLs and zip hashes; signed images and helper evidence have hashes. manifest.json records deliverable checksums. Adapted scripts are retained. No source-paper edits or publication performed.
