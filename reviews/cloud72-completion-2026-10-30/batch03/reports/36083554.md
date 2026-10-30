# TIC 36083554: CONFIRMED

Queue position 23; batch03. Anonymous project coordinator review with an independent measurement helper.

## Deciding assessment

Repeated discrete eclipses are present in raw QLP flux; representative event centers give a coherent eclipse period. Fresh independent aperture reduction and source localization are assessed below.

## Raw flux and period

Cached QLP SAP_FLUX, QUALITY=0; 3 representative sectors. Local quadratic baseline plus trapezoid fits retained 5 trial events. Only repeated discrete eclipse morphology supports an eclipse period. Search cycle counts were initial constraints, not independent period discovery. Lead inspected raw-event-panels.png and ambiguous-folds.png; smooth-variable fits hitting duration bounds are not eclipses.

Accepted event-derived period: 15.974024163426064 d.

Initial measurement receipt (superseded where rejected above):
```json
{
  "period_d": 15.974024163426064,
  "epoch_btjd": 1496.4368213575215,
  "n_events": 5,
  "residual_rms_min": 2.302940486572714,
  "note": "unweighted representative events, conditional on original search cycle counts; no uncertainty inferred"
}
```

## Fresh source and independent reduction

Two fresh detector-sector signed difference stacks favor the target, with free Gaussian offsets and fixed-position capable-neighbour comparisons below. Neighbour capability uses a conservative depth/magnitude threshold; TIC cones extend 60 arcsec. Ratios are descriptive residual comparisons and do not imply calibrated probabilities. Custom TESScut aperture extraction independently recovers the events from the same TESS photons as QLP.

```json
[
  {
    "sector": 7,
    "target_offset_arcsec": 1.0002671054830687,
    "min_neighbour_target_sse_ratio": 54.527241876955294,
    "capable_neighbour_count": 11
  },
  {
    "sector": 61,
    "target_offset_arcsec": 2.4025059769389188,
    "min_neighbour_target_sse_ratio": 15.686721955051661,
    "capable_neighbour_count": 10
  }
]
```

Custom TESScut reduction is independent of QLP processing but uses the same photons; it is not SPOC or an independent telescope. Signed in/out images use adjacent pre/post baselines. Gaussian formal errors exclude PRF systematics; fixed-coordinate source comparisons and repeat source positions govern attribution. Fresh downloads, TIC cones, signed arrays, plots and source scripts are preserved in raw-evidence.

## Gaia geometry

Event-derived P=15.974024163 d; Gaia P=15.980986459 +/- 0.006281408 d. Difference -1.11 Gaia sigma is descriptive. Approximate conjunction A offset 0.017 d; covariance linear error 0.456 d; conservative absolute-sum bound 2.293 d. Median fitted duration 4.43 h; approximate central duration 6.18 h. Geometry is physically feasible within approximate radii and propagated orbital phase uncertainty.

The computed gaia-geometry.json uses edge-on conjunction approximation, BTJD conversion Tp+389, and full SB1 covariance ordering P,gamma,K1,e,omega,Tp. Linear uncertainty is approximate, especially with weak eccentricity. Mass-function/main-sequence radius estimates test duration feasibility only; there is no fitted physical model or automatic sigma rejection.

## Catalogue status

no identified prior EB; all seven central scopes complete: yes. Central shared-catalogues coverage includes VSX, SIMBAD primary type, GaiaDR3 EB, Prsa2022, IJspeert2024, Kostov2025 vetted tables3/4 and ASAS-SN. SB* or ROT alone is not prior EB evidence. This is scoped novelty coverage, not an exhaustive discovery claim.

## Completion and limitations

Full representative review complete. Scientific ambiguity: Representative review; no exhaustive event or sector fits. Independent custom extraction shares TESS photons with QLP. Pixel PRF and catalogue completeness limit astrometry; no formal calibrated PRF significance is claimed.

Next test: Optional improved spectroscopy and photometry would refine binary characterization.

Provenance: cache-manifest.json gives original cached FITS paths and SHA256. Fresh TESScut URLs/hashes are in tesscut-downloads.json. Helper raw evidence and retained scripts permit reproduction. manifest.json hashes deliverables. No source paper, prior adjudication or publication was changed.
