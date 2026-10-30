# TIC 60443793: REFUTED

Queue position 31; batch04. Review by GPT-6.1 Sol with a fresh GPT-6.1 Terra helper, supervised by Astra. Physical classification and prior-catalogue status are separate.

## Deciding assessment

The original 6.510555 d search alias is wrong for the prominent eclipse train. Forty-eight raw minima give 1.29738064 d spacing; alternating depths imply a candidate 2.5947613 d binary period. Fresh imaging places these real EB photons off target, so the target-EB association is refuted. This is neither a confirmed target nor a target by-catch EB.

## Raw events and eclipse period

Two or three cached QLP SAP_FLUX sectors were checked with QUALITY=0. Representative events use local quadratic baselines plus trapezoid fits; TIC 60443793 instead uses the independently corrected alternating-minimum series, retained alongside the original search alias receipt. 48 representative fits were retained in raw-events.json, 48 clear of fit bounds. Depth range 3.462–21.691 percent. Period from representative event centers: 2.594761285455248. Search-cycle counts are conditional on the initial search except where the corrected alternating-minimum receipt explicitly supersedes that alias. No timing uncertainty or ephemeris prediction is claimed.

{
  "minimum_spacing_d": 1.297380642727624,
  "candidate_binary_period_d": 2.594761285455248,
  "epoch_btjd": 1658.3489391171465,
  "residual_rms_min": 11.60045026187536,
  "n_events": 48,
  "note": "Cycle count conditional on approximate 1.297 d spacing; alternating depths suggest double spacing as binary period. No uncertainty or secure alias test."
}

## Source imaging and independent reduction

S 13/S 93 signed deficits are off target. Free-Gaussian offsets about 58 arcsec align with capable TIC 60443695 at 59.38 arcsec separation. Fixed-coordinate neighbour/target SSE 0.0032 and 0.0229 strongly favor that neighbour in two sectors; positive-clipped centroids alone give 44.7/50.2 arcsec. Scores are descriptive, with PRF/systematic caveats. Candidate neighbour identity is an inference, not a full adjudication of that star.

Fresh TESScut cutouts are a distinct custom aperture reduction of the same TESS photons as QLP; they are not SPOC and do not supply an independent telescope. No claim of a separate SPOC pipeline is made. Signed in/out images use adjacent pre/post windows. Positive-clipped centroids and Gaussian formal errors are diagnostics subject to PRF mismatch; target-specific repeat tests and capable-neighbour comparisons govern attribution.

## Gaia geometry

Gaia orbit P=6.51870479 d. Representative photometric period 2.59476129 d; difference / Gaia quoted period error -1927.55. Closest edge-on conjunction A: offset -1.217 d, covariance-linear error 0.569 d. Observed duration median 4.67 h; approximate central duration 243.51 h. These are feasibility diagnostics, not significance vetoes or a fitted geometry. 

Computed receipt: gaia-geometry.json. Linear covariance propagation uses SB1 correlation order P,gamma,K1,e,omega,Tp; conjunction uses edge-on approximation. The mass-function/MS-radius duration is a feasibility estimate, not a physical fit. Circular/low-eccentricity periastron phases may be weakly constrained.

## Prior EB coverage

no identified prior EB; seven-scope coverage complete: yes. Reused central coverage-matrix.csv and catalogue-scope.json: VSX, SIMBAD primary type, Gaia DR3 EB, Prsa2022, IJspeert2024, Kostov2025 vetted tables3/4, ASAS-SN. SB* or ROT alone are not EB identifications. This scoped result is not an exhaustive discovery claim.

## Completion, limitations and next check

Signal class: off-target eclipsing binary contamination; Gaia association: photometric train does not trace target Gaia orbit.

Execution: completed representative full review; scientific ambiguity: Neighbour EB period remains a candidate and has not undergone independent alias/geometry review as its own target. The target giant-radius estimate is also incompatible with interpreting this short period as its simple detached binary orbit.

Next deciding check: Review TIC 60443695 separately if desired.

Provenance: cache-manifest.json preserves original cached FITS paths and SHA256; identity-checks.json matches TICID/SECTOR for all28 input QLP files. tesscut-downloads.json records fresh source URLs and zip hashes; signed images and helper evidence have hashes. manifest.json records deliverable checksums. Adapted scripts are retained. No source-paper edits or publication performed.
