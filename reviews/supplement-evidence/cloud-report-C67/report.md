# TIC 9396327: PROBABLE

Queue position 50; batch05. Automated GPT-6.1 Sol lead and independent fresh GPT-6.1 Terra review, supervised by Astra. The anonymous project coordinator supplied oversight; these are computational measurements, not human measurements.

## Assessment

Six fully covered primary events repeat in raw flux with depth28–29percent and consistent discrete morphology. Independent aperture reduction reproduces the events and the signed deficit favors the target. The Gaia-orbit geometry check remains unresolved.

## Raw repetition and period

Accepted target eclipse period: 2.4416706861122432 days. 1 representative cached QLP sectors were reviewed using SAP_FLUX and QUALITY=0. Original packet periods were treated as candidate aliases. Corrected event fits use local linear baselines and trapezoids on raw cadences; no exhaustive sector fit or physical binary model was required.

{
  "period_d": 2.4416706861122432,
  "epoch_btjd": 3481.3231252924884,
  "n_events": 6,
  "note": "Representative local event timing regression for939/183; direct consecutive event interval for431/222; no formal period error."
}

Representative accepted event measurements:
```json
[
  {
    "sector": 80,
    "tc": 3481.323636157607,
    "depth": 0.28420131298250056,
    "duration_d": 0.13406369149885997,
    "ingress_fraction": 0.3540239651639954,
    "residual_rms": 0.012155047692972612,
    "edge": false,
    "n_points": 517,
    "cycle": 0
  },
  {
    "sector": 80,
    "tc": 3483.7643666168096,
    "depth": 0.2883310030553778,
    "duration_d": 0.13934346534258632,
    "ingress_fraction": 0.35414071040251316,
    "residual_rms": 0.009947821623346951,
    "edge": false,
    "n_points": 519,
    "cycle": 1
  },
  {
    "sector": 80,
    "tc": 3495.9727604242707,
    "depth": 0.2882585527080121,
    "duration_d": 0.13941595437124518,
    "ingress_fraction": 0.3526956252225945,
    "residual_rms": 0.008971962493992389,
    "edge": false,
    "n_points": 519,
    "cycle": 6
  },
  {
    "sector": 80,
    "tc": 3498.4150669656806,
    "depth": 0.28617070118118176,
    "duration_d": 0.1422442512820803,
    "ingress_fraction": 0.36315371152553355,
    "residual_rms": 0.008677686898336322,
    "edge": false,
    "n_points": 519,
    "cycle": 7
  },
  {
    "sector": 80,
    "tc": 3500.856001103531,
    "depth": 0.2879069502033062,
    "duration_d": 0.14331393223936886,
    "ingress_fraction": 0.3692578062889713,
    "residual_rms": 0.009958225508168744,
    "edge": false,
    "n_points": 519,
    "cycle": 8
  },
  {
    "sector": 80,
    "tc": 3503.298711756517,
    "depth": 0.28214056210063676,
    "duration_d": 0.14093323177085357,
    "ingress_fraction": 0.36372962582456636,
    "residual_rms": 0.009964507706264907,
    "edge": false,
    "n_points": 426,
    "cycle": 9
  }
]
```

## Source and independent reduction

Sector80 free Gaussian deficit lies0.56arcsec from target. Capable TIC neighbours51.4/55.9arcsec away have fixed neighbour/target SSE ratios74.9/70.5, strongly worse descriptively. The independent custom aperture reproduces repeated eclipses.

Fresh 11x11 TESScuts and 60 arcsec TIC source cones were obtained. Signed in/out images compare local pre/post baselines. The source model includes signed pixel-integrated Gaussians and fixed source positions with free widths/amplitude/background. Residual ratios are descriptive and do not constitute calibrated PRF probabilities. Neighbours capable under a conservative brightness/depth limit were compared; throughput, uncatalogued sources and TIC photometry remain limitations.

The independent custom target aperture subtracts a per-cadence background from faint cutout pixels and uses the same TESS photons as QLP. It is a distinct extraction, not SPOC or a second telescope. Terra independently inspected raw/custom comparison and signed images; quantitative four-EB depths and receipts are in raw-evidence/terra-helper-results.json. See HELPER.md, all-raw.png, raw-event-panels.png and terra-independent-comparison.png.

## Gaia geometry and association

Representative six-event regression gives2.441670686d (timing residuals below0.00056d); Gaia2.441934355+/-0.000085226d. A sector-end partial event was excluded because its distorted timing shifts the inferred period. Approximate conjunction A offset0.347d versus propagated covariance0.116d; period differences alone do not veto an EB. Duration3.36h is feasible relative to central4.81h. Secondary-event phase and propagated orbital phase prevent claiming a fully consistent Gaia association.

Association flag: unresolved; no firm by-catch.

The gaia-geometry.json calculation uses edge-on conjunctions, Tp+389 BTJD conversion, full SB1 covariance in P,gamma,K1,e,omega,Tp order, and linear propagation. Approximate mass function, TIC radius and main-sequence companion radius test feasibility, not a fitted geometry. No automatic Gaia sigma veto was applied.

## Catalogue coverage

no identified prior EB; seven-scope coverage complete: yes. Central coverage includes VSX, SIMBAD primary type, Gaia DR3 EB, Prsa2022, IJspeert2024, vetted Kostov2025 tables3/4 and ASAS-SN. SB* and ROT alone do not count as known EB. This scoped result is separate from physical assessment. TIC183994341 is known and excluded from new additions regardless of physical tier.

## Completion, limits and next check

Full representative review complete; remaining full review=false. Available deciding checks were attempted. Scientific uncertainty: Real on-target repeating EB; PROBABLE because the Gaia geometry/association check is unresolved. One fresh detector sector only; same-photon independent reduction. No firm by-catch flag: a modest period mismatch does not establish a separate orbit.

Next check: Refine Gaia conjunction predictions with orbital posterior and measure a second clean sector or obtain new RVs to test the orbit association.

Provenance: raw-evidence/cache-manifest.json hashes the cached original QLP files; identity-checks.json verifies TICID/sector. Fresh TESScut URLs/SHA256 are in tesscut-downloads.json; source cones and adapted scripts are retained. manifest.json hashes batch deliverables. No paper edits, source table edits, publication or commits were made.
