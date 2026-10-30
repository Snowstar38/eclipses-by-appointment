# TIC 71866523: PLAUSIBLE

Queue position 32; batch04. Review by GPT-6.1 Sol with a fresh GPT-6.1 Terra helper, supervised by Astra. Physical classification and prior-catalogue status are separate.

## Deciding assessment

Sectors 6/33 are nearly flat with a weak sector 33 depression; sector 87 is dominated by a large positive transient/systematic. No secure repeating eclipse sequence or eclipse-derived period is established.

## Raw events and eclipse period

Two or three cached QLP SAP_FLUX sectors were checked with QUALITY=0. Representative events use local quadratic baselines plus trapezoid fits; TIC 60443793 instead uses the independently corrected alternating-minimum series, retained alongside the original search alias receipt. 2 representative fits were retained in raw-events.json, 1 clear of fit bounds. Depth range 0.099–0.099 percent. Period from representative event centers: not established as an eclipse period. Search-cycle counts are conditional on the initial search except where the corrected alternating-minimum receipt explicitly supersedes that alias. No timing uncertainty or ephemeris prediction is claimed.

Smooth-variable morphology is assessed in ambiguous-folds.json and helper receipts.

## Source imaging and independent reduction

Fresh sectors 6/87 custom extraction attempted the independent gate; no sufficient isolated eclipse exists for a meaningful signed source image.

Fresh TESScut cutouts are a distinct custom aperture reduction of the same TESS photons as QLP; they are not SPOC and do not supply an independent telescope. No claim of a separate SPOC pipeline is made. Signed in/out images use adjacent pre/post windows. Positive-clipped centroids and Gaussian formal errors are diagnostics subject to PRF mismatch; target-specific repeat tests and capable-neighbour comparisons govern attribution.

## Gaia geometry

Gaia orbit P=15.39210899 d. No secure eclipse period exists for a meaningful conjunction/duration validation. 

Computed receipt: gaia-geometry.json. Linear covariance propagation uses SB1 correlation order P,gamma,K1,e,omega,Tp; conjunction uses edge-on approximation. The mass-function/MS-radius duration is a feasibility estimate, not a physical fit. Circular/low-eccentricity periastron phases may be weakly constrained.

## Prior EB coverage

no identified prior EB; seven-scope coverage complete: yes. Reused central coverage-matrix.csv and catalogue-scope.json: VSX, SIMBAD primary type, Gaia DR3 EB, Prsa2022, IJspeert2024, Kostov2025 vetted tables3/4, ASAS-SN. SB* or ROT alone are not EB identifications. This scoped result is not an exhaustive discovery claim.

## Completion, limitations and next check

Signal class: uncertain variability; Gaia association: not established.

Execution: completed representative full review; scientific ambiguity: Weak single feature and transient/baseline ambiguity; available work was attempted.

Next deciding check: Require a clean repeated negative event before EB classification.

Provenance: cache-manifest.json preserves original cached FITS paths and SHA256; identity-checks.json matches TICID/SECTOR for all28 input QLP files. tesscut-downloads.json records fresh source URLs and zip hashes; signed images and helper evidence have hashes. manifest.json records deliverable checksums. Adapted scripts are retained. No source-paper edits or publication performed.
