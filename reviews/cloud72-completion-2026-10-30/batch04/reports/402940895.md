# TIC 402940895: PLAUSIBLE

Queue position 40; batch04. Review by GPT-6.1 Sol with a fresh GPT-6.1 Terra helper, supervised by Astra. Physical classification and prior-catalogue status are separate.

## Deciding assessment

Small sharp depressions lie on strong discontinuous sector 12/93 trends, while sector 103 flux is severely corrupted. Custom sector 12 fixed-shape depths 0.53/0.76% show features in the same photons, but their morphology is baseline sensitive and a stable eclipse sequence is unestablished.

## Raw events and eclipse period

Two or three cached QLP SAP_FLUX sectors were checked with QUALITY=0. Representative events use local quadratic baselines plus trapezoid fits; TIC 60443793 instead uses the independently corrected alternating-minimum series, retained alongside the original search alias receipt. 5 representative fits were retained in raw-events.json, 5 clear of fit bounds. Depth range 0.0–0.674 percent. Period from representative event centers: not established as an eclipse period. Search-cycle counts are conditional on the initial search except where the corrected alternating-minimum receipt explicitly supersedes that alias. No timing uncertainty or ephemeris prediction is claimed.

Smooth-variable morphology is assessed in ambiguous-folds.json and helper receipts.

## Source imaging and independent reduction

Sector 12 signed diagnostic has 2.79 arcsec Gaussian target offset, but strong baseline structure and lack of a clean independent later-sector event prevent secure source validation. Fresh sectors 12/103 were extracted.

Fresh TESScut cutouts are a distinct custom aperture reduction of the same TESS photons as QLP; they are not SPOC and do not supply an independent telescope. No claim of a separate SPOC pipeline is made. Signed in/out images use adjacent pre/post windows. Positive-clipped centroids and Gaussian formal errors are diagnostics subject to PRF mismatch; target-specific repeat tests and capable-neighbour comparisons govern attribution.

## Gaia geometry

Gaia orbit P=16.44813821 d. No secure eclipse period exists for a meaningful conjunction/duration validation. 

Computed receipt: gaia-geometry.json. Linear covariance propagation uses SB1 correlation order P,gamma,K1,e,omega,Tp; conjunction uses edge-on approximation. The mass-function/MS-radius duration is a feasibility estimate, not a physical fit. Circular/low-eccentricity periastron phases may be weakly constrained.

## Prior EB coverage

no identified prior EB; seven-scope coverage complete: yes. Reused central coverage-matrix.csv and catalogue-scope.json: VSX, SIMBAD primary type, Gaia DR3 EB, Prsa2022, IJspeert2024, Kostov2025 vetted tables3/4, ASAS-SN. SB* or ROT alone are not EB identifications. This scoped result is not an exhaustive discovery claim.

## Completion, limitations and next check

Signal class: uncertain variability; Gaia association: not established.

Execution: completed representative full review; scientific ambiguity: Baseline/discontinuity sensitivity, corrupted sector 103, no secure eclipse period or repeated source validation.

Next deciding check: Re-extract clean sectors with robust background/pointing treatment before asserting eclipses.

Provenance: cache-manifest.json preserves original cached FITS paths and SHA256; identity-checks.json matches TICID/SECTOR for all28 input QLP files. tesscut-downloads.json records fresh source URLs and zip hashes; signed images and helper evidence have hashes. manifest.json records deliverable checksums. Adapted scripts are retained. No source-paper edits or publication performed.
