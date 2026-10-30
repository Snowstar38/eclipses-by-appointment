# TIC 201317466: PROBABLE

Queue position 27; batch03. Anonymous project coordinator review with an independent measurement helper.

## Deciding assessment

Deep repeated eclipses are real and coherent. Association with the published Gaia SB1 orbit remains unresolved because its conjunction misses the eclipse by a substantial fraction of a cycle, beyond the conservative linear propagated uncertainty.

## Raw flux and period

Cached QLP SAP_FLUX, QUALITY=0; 2 representative sectors. Local quadratic baseline plus trapezoid fits retained 4 trial events. Only repeated discrete eclipse morphology supports an eclipse period. Search cycle counts were initial constraints, not independent period discovery. Lead inspected raw-event-panels.png and ambiguous-folds.png; smooth-variable fits hitting duration bounds are not eclipses.

Accepted event-derived period: 5.623860159150563 d.

Initial measurement receipt (superseded where rejected above):
```json
{
  "period_d": 5.623860159150563,
  "epoch_btjd": 2772.3289690349256,
  "n_events": 4,
  "residual_rms_min": 0.5278820914721635,
  "note": "unweighted representative events, conditional on original search cycle counts; no uncertainty inferred"
}
```

## Fresh source and independent reduction

Two fresh detector-sector signed difference stacks favor the target, with free Gaussian offsets and fixed-position capable-neighbour comparisons below. Neighbour capability uses a conservative depth/magnitude threshold; TIC cones extend 60 arcsec. Ratios are descriptive residual comparisons and do not imply calibrated probabilities. Custom TESScut aperture extraction independently recovers the events from the same TESS photons as QLP.

```json
[
  {
    "sector": 54,
    "target_offset_arcsec": 0.11507353740750183,
    "min_neighbour_target_sse_ratio": 15.652494055094234,
    "capable_neighbour_count": 2
  },
  {
    "sector": 80,
    "target_offset_arcsec": 3.540797490060455,
    "min_neighbour_target_sse_ratio": 23.02100675329804,
    "capable_neighbour_count": 2
  }
]
```

Custom TESScut reduction is independent of QLP processing but uses the same photons; it is not SPOC or an independent telescope. Signed in/out images use adjacent pre/post baselines. Gaussian formal errors exclude PRF systematics; fixed-coordinate source comparisons and repeat source positions govern attribution. Fresh downloads, TIC cones, signed arrays, plots and source scripts are preserved in raw-evidence.

## Gaia geometry

Event-derived P=5.623860159 d; Gaia P=5.625963779 +/- 0.000558314 d. Difference -3.77 Gaia sigma is descriptive. Approximate conjunction A offset -1.208 d; covariance linear error 0.228 d; conservative absolute-sum bound 0.694 d. Median fitted duration 5.97 h; approximate central duration 7.50 h. Geometry is physically feasible within approximate radii and propagated orbital phase uncertainty.

The computed gaia-geometry.json uses edge-on conjunction approximation, BTJD conversion Tp+389, and full SB1 covariance ordering P,gamma,K1,e,omega,Tp. Linear uncertainty is approximate, especially with weak eccentricity. Mass-function/main-sequence radius estimates test duration feasibility only; there is no fitted physical model or automatic sigma rejection.

## Catalogue status

no identified prior EB; all seven central scopes complete: yes. Central shared-catalogues coverage includes VSX, SIMBAD primary type, GaiaDR3 EB, Prsa2022, IJspeert2024, Kostov2025 vetted tables3/4 and ASAS-SN. SB* or ROT alone is not prior EB evidence. This is scoped novelty coverage, not an exhaustive discovery claim.

## Completion and limitations

Full representative review complete. Scientific ambiguity: Representative review; no exhaustive event or sector fits. Independent custom extraction shares TESS photons with QLP. Pixel PRF and catalogue completeness limit astrometry; no formal calibrated PRF significance is claimed. Gaia has only 15 RV epochs, modestly constrained eccentricity (0.125 +/- 0.061), and strongly correlated periastron parameters. A 1.208 d conjunction offset versus 0.228 d linear covariance error and 0.694 d conservative sum bound is a physical phase discrepancy; no automatic sigma veto is applied.

Next test: Refit the RV orbit or evaluate a nonlinear orbital posterior against the observed eclipse timing to resolve Gaia association.

Provenance: cache-manifest.json gives original cached FITS paths and SHA256. Fresh TESScut URLs/hashes are in tesscut-downloads.json. Helper raw evidence and retained scripts permit reproduction. manifest.json hashes deliverables. No source paper, prior adjudication or publication was changed.
