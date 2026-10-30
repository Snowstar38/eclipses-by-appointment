# TIC 126363604: PROBABLE

Queue position 16; batch02. Review by GPT-6.1 Sol with a fresh GPT-6.1 Terra helper, supervised by Astra. Physical classification and prior-catalogue status are separate.

## Deciding assessment

Four sharp repeat eclipses are visible over a variable stellar baseline; all four centers define an eclipse period. Raw-event scatter is inflated by variability, so the initial depth/RMS gate was explicitly relaxed after fold inspection. Fresh imaging supports the target but does not fully exclude its closest capable source.

## Raw events and eclipse period

Three cached QLP SAP_FLUX sectors were checked with QUALITY=0, local quadratic baseline plus trapezoid fits. 4 representative fits were retained in raw-events.json, 4 clear of fit bounds. Depth range 0.789–1.165 percent. Period from representative event centers: 16.505959732386128. Search-cycle counts are conditional on the initial search, not a blind period discovery. No timing uncertainty or ephemeris prediction is claimed.

{
  "period_d": 16.505959732386128,
  "epoch_btjd": 1505.614116361415,
  "n_events": 4,
  "residual_rms_min": 14.198163488304088,
  "note": "Four visible sharp events; no per-point depth/RMS gate because stellar baseline variation inflates RMS. Unweighted cycle counts conditional on original search."
}

## Source imaging and independent reduction

Four individual signed difference images in sectors7,61,88 place fitted deficits3.93,1.34,0.81,0.82 arcsec from the target. Nearest capable neighbour is11.14 arcsec. The first-sector fixed-source residual ratio is only1.78; repeat source positions support the target but the PSF systematics are uncalibrated. Custom extraction recovers repeated deficits in the same TESS photons.

Fresh TESScut cutouts are a distinct custom aperture reduction of the same TESS photons as QLP; they are not SPOC and do not supply an independent telescope. MAST product-inventory queries were attempted and timed out for all ten; this is a service limitation, not absence of products. Signed in/out images use adjacent pre/post windows. Positive-clipped centroids and Gaussian formal errors are diagnostics subject to PRF mismatch; target-specific repeat tests and capable-neighbour comparisons govern attribution.

## Gaia geometry

Photometric period 16.505959732 d versus Gaia 16.499031114 ± 0.00363290 d; difference 1.91 Gaia sigma. Nearest approximate conjunction B: offset 0.657 d; linear covariance error 0.290 d, conservative sum bound 1.352 d. Observed median duration 8.22 h versus approximate central feasibility 22.88 h. Phase uncertainty and approximate geometry are retained rather than treating a linear sigma as exact.

Computed receipt: gaia-geometry.json. Linear covariance propagation uses SB1 correlation order P,gamma,K1,e,omega,Tp; conjunction uses edge-on approximation. The mass-function/MS-radius duration is a feasibility estimate, not a physical fit. Circular/low-eccentricity periastron phases may be weakly constrained.

## Prior EB coverage

no identified prior EB; seven-scope coverage complete: yes. Reused central coverage-matrix.csv and catalogue-scope.json: VSX, SIMBAD primary type, Gaia DR3 EB, Prsa2022, IJspeert2024, Kostov2025 vetted tables3/4, ASAS-SN. SB* or ROT alone are not EB identifications. This scoped result is not an exhaustive discovery claim.

## Completion, limitations and next check

Execution: completed representative full review; scientific ambiguity: Closest capable host not conclusively excluded under the source model; approximate Gaia conjunction offset0.657 d has linear covariance error0.290 d, with broad conservative uncertainty. Stellar variability affects local timing/depth.

Next deciding check: Validate the repeated difference-image astrometry with a multi-source PRF or higher resolution event photometry; refine Gaia conjunction uncertainty if needed.

Provenance: cache-manifest.json preserves original cached FITS paths and SHA256; identity-checks.json matches TICID/SECTOR for all30 input QLP files. tesscut-downloads.json records fresh source URLs and zip hashes; signed images and helper evidence have hashes. manifest.json records deliverable checksums. Adapted scripts are retained. No source-paper edits or publication performed.
