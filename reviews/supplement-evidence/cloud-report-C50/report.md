# TIC 443106429: PROBABLE

Queue position 33; batch04. Review by GPT-6.1 Sol with a fresh GPT-6.1 Terra helper, supervised by Astra. Physical classification and prior-catalogue status are separate.

## Deciding assessment

Four narrow raw eclipses in sectors 11 and 65 give 12.7955335 d, consistent with Gaia. Raw depths 1.82?2.84%, duration about 10.2 h; custom extraction recovers four at 1.84?3.33%. Eclipses are real and repeat, but the close host remains unresolved.

## Raw events and eclipse period

Two or three cached QLP SAP_FLUX sectors were checked with QUALITY=0. Representative events use local quadratic baselines plus trapezoid fits; TIC 60443793 instead uses the independently corrected alternating-minimum series, retained alongside the original search alias receipt. 4 representative fits were retained in raw-events.json, 4 clear of fit bounds. Depth range 1.825–2.841 percent. Period from representative event centers: 12.795533464914396. Search-cycle counts are conditional on the initial search except where the corrected alternating-minimum receipt explicitly supersedes that alias. No timing uncertainty or ephemeris prediction is claimed.

{
  "period_d": 12.795533464914396,
  "epoch_btjd": 1606.1515052693348,
  "n_events": 3,
  "residual_rms_min": 0.2322850788714703,
  "note": "unweighted representative events, conditional on original search cycle counts; no uncertainty inferred"
}

## Source imaging and independent reduction

Sector 11 deficit lies 0.59 arcsec from target, with capable TIC 443106423 only 3.88 arcsec away; fixed-neighbour/target SSE 1.83 favors target. Extra fresh sector 65 was obtained; noisy one-event signed deficit has 13.4 arcsec fitted offset and close-neighbour/target SSE 0.99, failing independent separation. Source testing was attempted and remains scientifically ambiguous.

Fresh TESScut cutouts are a distinct custom aperture reduction of the same TESS photons as QLP; they are not SPOC and do not supply an independent telescope. No claim of a separate SPOC pipeline is made. Signed in/out images use adjacent pre/post windows. Positive-clipped centroids and Gaussian formal errors are diagnostics subject to PRF mismatch; target-specific repeat tests and capable-neighbour comparisons govern attribution.

## Gaia geometry

Gaia orbit P=12.79551859 d. Representative photometric period 12.79553346 d; difference / Gaia quoted period error 0.00. Closest edge-on conjunction A: offset -0.230 d, covariance-linear error 0.565 d. Observed duration median 10.23 h; approximate central duration 22.45 h. These are feasibility diagnostics, not significance vetoes or a fitted geometry. 

Computed receipt: gaia-geometry.json. Linear covariance propagation uses SB1 correlation order P,gamma,K1,e,omega,Tp; conjunction uses edge-on approximation. The mass-function/MS-radius duration is a feasibility estimate, not a physical fit. Circular/low-eccentricity periastron phases may be weakly constrained.

## Prior EB coverage

no identified prior EB; seven-scope coverage complete: yes. Reused central coverage-matrix.csv and catalogue-scope.json: VSX, SIMBAD primary type, Gaia DR3 EB, Prsa2022, IJspeert2024, Kostov2025 vetted tables3/4, ASAS-SN. SB* or ROT alone are not EB identifications. This scoped result is not an exhaustive discovery claim.

## Completion, limitations and next check

Signal class: repeating eclipsing signal; likely target; Gaia association: period/conjunction feasible, host unresolved.

Execution: completed representative full review; scientific ambiguity: Host not robustly separated from 3.88 arcsec capable neighbour; this is the one unresolved protocol gate.

Next deciding check: Resolve target versusTIC 443106423 with higher spatial resolution eclipse photometry.

Provenance: cache-manifest.json preserves original cached FITS paths and SHA256; identity-checks.json matches TICID/SECTOR for all28 input QLP files. tesscut-downloads.json records fresh source URLs and zip hashes; signed images and helper evidence have hashes. manifest.json records deliverable checksums. Adapted scripts are retained. No source-paper edits or publication performed.
