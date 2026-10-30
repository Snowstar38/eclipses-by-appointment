# TIC 4646090: CONFIRMED

Queue position 39; batch04. Review by GPT-6.1 Sol with a fresh GPT-6.1 Terra helper, supervised by Astra. Physical classification and prior-catalogue status are separate.

## Deciding assessment

Three narrow, locally flat-baseline eclipses in sectors 4 and 31 give 10.7303766 d. Raw depths 1.95?2.26% and durations 2.75?3.46 h recur; the distinct custom extraction recovers all three at 0.59?0.64% aperture depth. Dilution differs between reductions. Source and independent gates pass; Gaia period and phase are feasible at the precision available.

## Raw events and eclipse period

Two or three cached QLP SAP_FLUX sectors were checked with QUALITY=0. Representative events use local quadratic baselines plus trapezoid fits; TIC 60443793 instead uses the independently corrected alternating-minimum series, retained alongside the original search alias receipt. 3 representative fits were retained in raw-events.json, 3 clear of fit bounds. Depth range 1.945–2.265 percent. Period from representative event centers: 10.73037662305058. Search-cycle counts are conditional on the initial search except where the corrected alternating-minimum receipt explicitly supersedes that alias. No timing uncertainty or ephemeris prediction is claimed.

{
  "period_d": 10.73037662305058,
  "epoch_btjd": 1419.05639053136,
  "n_events": 3,
  "residual_rms_min": 1.164581672824554,
  "note": "unweighted representative events, conditional on original search cycle counts; no uncertainty inferred"
}

## Source imaging and independent reduction

Signed deficits in both sectors prefer the target. Free-Gaussian offsets are 0.46 and 2.28 arcsec, versus a capable TIC 4646088 neighbour 6.96 arcsec away (7.53 and 9.32 arcsec from fitted deficits). Fixed-neighbour / target SSE is 5.34 and 5.65 in sector stacks; per-event ratios 5.34,3.57,4.27 also favor target. These descriptive comparisons, repeated across sectors/events, support attribution; no calibrated PRF confidence is asserted.

Fresh TESScut cutouts are a distinct custom aperture reduction of the same TESS photons as QLP; they are not SPOC and do not supply an independent telescope. No claim of a separate SPOC pipeline is made. Signed in/out images use adjacent pre/post windows. Positive-clipped centroids and Gaussian formal errors are diagnostics subject to PRF mismatch; target-specific repeat tests and capable-neighbour comparisons govern attribution.

## Gaia geometry

Gaia orbit P=10.72678235 d. Representative photometric period 10.73037662 d; difference / Gaia quoted period error 1.05. Closest edge-on conjunction A: offset 0.612 d, covariance-linear error 0.457 d. Observed duration median 3.22 h; approximate central duration 8.06 h. These are feasibility diagnostics, not significance vetoes or a fitted geometry. 

Computed receipt: gaia-geometry.json. Linear covariance propagation uses SB1 correlation order P,gamma,K1,e,omega,Tp; conjunction uses edge-on approximation. The mass-function/MS-radius duration is a feasibility estimate, not a physical fit. Circular/low-eccentricity periastron phases may be weakly constrained.

## Prior EB coverage

no identified prior EB; seven-scope coverage complete: yes. Reused central coverage-matrix.csv and catalogue-scope.json: VSX, SIMBAD primary type, Gaia DR3 EB, Prsa2022, IJspeert2024, Kostov2025 vetted tables3/4, ASAS-SN. SB* or ROT alone are not EB identifications. This scoped result is not an exhaustive discovery claim.

## Completion, limitations and next check

Signal class: target eclipsing binary; Gaia association: consistent within approximate orbit/geometry checks.

Execution: completed representative full review; scientific ambiguity: Gaia phase offset is 1.34 covariance-linear error units; grazing geometry can shorten the approximate central duration. No detailed physical fit or calibrated astrometric uncertainty.

Next deciding check: Characterize dilution and grazing geometry if needed.

Provenance: cache-manifest.json preserves original cached FITS paths and SHA256; identity-checks.json matches TICID/SECTOR for all28 input QLP files. tesscut-downloads.json records fresh source URLs and zip hashes; signed images and helper evidence have hashes. manifest.json records deliverable checksums. Adapted scripts are retained. No source-paper edits or publication performed.
