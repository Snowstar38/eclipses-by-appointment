# TIC 411647453: REFUTED

Queue position 29; batch03. Anonymous project coordinator review with an independent measurement helper.

## Deciding assessment

Real narrow eclipses contaminate the target aperture, but the proposed target Gaia-period eclipse association is refuted. Two detector sectors place the deficit on nearby TIC 411647413 rather than TIC 411647453. The approximately 0.9151763 d short-period signal gives about seven dips per 6.394568 d screen fold; that screen interval is not a valid target eclipse period.

## Raw flux and period

Cached QLP SAP_FLUX, QUALITY=0; 3 representative sectors. Local quadratic baseline plus trapezoid fits retained 6 trial events. Only repeated discrete eclipse morphology supports an eclipse period. Search cycle counts were initial constraints, not independent period discovery. Lead inspected raw-event-panels.png and ambiguous-folds.png; smooth-variable fits hitting duration bounds are not eclipses.

Accepted event-derived period: none for the target d.

Initial measurement receipt (superseded where rejected above):
```json
{
  "period_d": 6.394515949153654,
  "epoch_btjd": 1603.7676801779019,
  "n_events": 3,
  "residual_rms_min": 61.848856830139425,
  "note": "unweighted representative events, conditional on original search cycle counts; no uncertainty inferred"
}
```

## Fresh source and independent reduction

Sectors11/99 Gaussian deficit centers are 15.09/14.20 arcsec from the target, but 0.56/1.64 arcsec from TIC411647413, separated14.76 arcsec. Fixed neighbour/target SSE ratios are0.362/0.144, consistently favoring that neighbour. A short-period contaminating EB is strongly inferred; its precision ephemeris and novelty were not reviewed.

```json
[
  {
    "sector": 11,
    "target_offset_arcsec": 15.09238254714884,
    "min_neighbour_target_sse_ratio": 0.36214401303402544,
    "capable_neighbour_count": 18
  },
  {
    "sector": 99,
    "target_offset_arcsec": 14.197941851487595,
    "min_neighbour_target_sse_ratio": 0.1436331918871176,
    "capable_neighbour_count": 25
  }
]
```

Custom TESScut reduction is independent of QLP processing but uses the same photons; it is not SPOC or an independent telescope. Signed in/out images use adjacent pre/post baselines. Gaussian formal errors exclude PRF systematics; fixed-coordinate source comparisons and repeat source positions govern attribution. Fresh downloads, TIC cones, signed arrays, plots and source scripts are preserved in raw-evidence.

## Gaia geometry

The original conditional 6.394515949 d regression aliased unrelated eclipse dips. It is rejected as an eclipse-derived target period; no Gaia-conjunction association is established.

The computed gaia-geometry.json uses edge-on conjunction approximation, BTJD conversion Tp+389, and full SB1 covariance ordering P,gamma,K1,e,omega,Tp. Linear uncertainty is approximate, especially with weak eccentricity. Mass-function/main-sequence radius estimates test duration feasibility only; there is no fitted physical model or automatic sigma rejection.

## Catalogue status

no identified prior EB; all seven central scopes complete: yes. Central shared-catalogues coverage includes VSX, SIMBAD primary type, GaiaDR3 EB, Prsa2022, IJspeert2024, Kostov2025 vetted tables3/4 and ASAS-SN. SB* or ROT alone is not prior EB evidence. This is scoped novelty coverage, not an exhaustive discovery claim.

## Completion and limitations

Full representative review complete. Scientific ambiguity: The contaminating eclipses are real; REFUTED applies to target attribution and Gaia-period interpretation. TIC411647413 is an inferred by-catch host subject to pixel model systematics, not a new confirmed catalogue object.

Next test: Higher resolution event photometry can establish the contaminant host and measure its orbital period precisely.

Provenance: cache-manifest.json gives original cached FITS paths and SHA256. Fresh TESScut URLs/hashes are in tesscut-downloads.json. Helper raw evidence and retained scripts permit reproduction. manifest.json hashes deliverables. No source paper, prior adjudication or publication was changed.
