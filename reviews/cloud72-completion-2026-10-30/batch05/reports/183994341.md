# TIC 183994341: CONFIRMED

Queue position 41; batch05. Automated GPT-6.1 Sol lead and independent fresh GPT-6.1 Terra review, supervised by Astra. The anonymous project coordinator supplied oversight; these are computational measurements, not human measurements.

## Assessment

Four repeated primary eclipses with raw depths25–29percent are on target and recovered independently. The eclipse period is approximately14.6655d; the ASAS-SN catalogue lists an incompatible2.9324d alias. The target is a known prior EB and excluded from new additions.

## Raw repetition and period

Accepted target eclipse period: 14.665514216226159 days. 2 representative cached QLP sectors were reviewed using SAP_FLUX and QUALITY=0. Original packet periods were treated as candidate aliases. Corrected event fits use local linear baselines and trapezoids on raw cadences; no exhaustive sector fit or physical binary model was required.

{
  "period_d": 14.665514216226159,
  "epoch_btjd": 3781.92483432609,
  "n_events": 4,
  "note": "Representative local event timing regression for939/183; direct consecutive event interval for431/222; no formal period error."
}

Representative accepted event measurements:
```json
[
  {
    "sector": 91,
    "tc": 3781.924758087458,
    "depth": 0.27811754249345844,
    "duration_d": 0.6709603998224439,
    "ingress_fraction": 0.4102676391311878,
    "residual_rms": 0.008400452725881942,
    "edge": false,
    "n_points": 393,
    "cycle": 0
  },
  {
    "sector": 91,
    "tc": 3796.5904251899988,
    "depth": 0.28747538323348454,
    "duration_d": 0.7030939389529461,
    "ingress_fraction": 0.4222486811501103,
    "residual_rms": 0.008485133785920739,
    "edge": false,
    "n_points": 366,
    "cycle": 1
  },
  {
    "sector": 92,
    "tc": 3811.255938179075,
    "depth": 0.24829805939567123,
    "duration_d": 0.6719697358685144,
    "ingress_fraction": 0.4078376270792781,
    "residual_rms": 0.00781992030528953,
    "edge": false,
    "n_points": 519,
    "cycle": 2
  },
  {
    "sector": 92,
    "tc": 3825.9213011451875,
    "depth": 0.25572653021110614,
    "duration_d": 0.6766583893637675,
    "ingress_fraction": 0.4180416685853718,
    "residual_rms": 0.007580250708817091,
    "edge": false,
    "n_points": 519,
    "cycle": 3
  }
]
```

## Source and independent reduction

Sectors91/92 free Gaussian offsets1.71/1.58arcsec favor the target; closest capable neighbours38arcsec or farther give substantially worse fixed-source residuals (ratios22.8–44.1). Independent custom apertures reproduce repeated eclipses.

Fresh 11x11 TESScuts and 60 arcsec TIC source cones were obtained. Signed in/out images compare local pre/post baselines. The source model includes signed pixel-integrated Gaussians and fixed source positions with free widths/amplitude/background. Residual ratios are descriptive and do not constitute calibrated PRF probabilities. Neighbours capable under a conservative brightness/depth limit were compared; throughput, uncatalogued sources and TIC photometry remain limitations.

The independent custom target aperture subtracts a per-cadence background from faint cutout pixels and uses the same TESS photons as QLP. It is a distinct extraction, not SPOC or a second telescope. Terra independently inspected raw/custom comparison and signed images; quantitative four-EB depths and receipts are in raw-evidence/terra-helper-results.json. See HELPER.md, all-raw.png, raw-event-panels.png and terra-independent-comparison.png.

## Gaia geometry and association

Four-event regression P14.665514216d versus Gaia14.670950076+/-0.003882078d. Approximate conjunction offset1.81d with propagated covariance0.93d and conservative absolute-sum1.76d; duration16.18h versus approximate central23.03h is physically feasible. The period, propagated approximate phase and duration are compatible with the Gaia orbit at current precision; the roughly1.9sigma phase difference alone is not a physical veto.

Association flag: compatible at approximate current precision; phase uncertainty retained.

The gaia-geometry.json calculation uses edge-on conjunctions, Tp+389 BTJD conversion, full SB1 covariance in P,gamma,K1,e,omega,Tp order, and linear propagation. Approximate mass function, TIC radius and main-sequence companion radius test feasibility, not a fitted geometry. No automatic Gaia sigma veto was applied.

## Catalogue coverage

known prior EB; seven-scope coverage complete: yes. Central coverage includes VSX, SIMBAD primary type, Gaia DR3 EB, Prsa2022, IJspeert2024, vetted Kostov2025 tables3/4 and ASAS-SN. SB* and ROT alone do not count as known EB. This scoped result is separate from physical assessment. TIC183994341 is known and excluded from new additions regardless of physical tier.

## Completion, limits and next check

Full representative review complete; remaining full review=false. Available deciding checks were attempted. Scientific uncertainty: Real repeated on-target known EB. Approximate Gaia conjunction phase and radii limit characterization. Catalogue period conflict is retained rather than forcing catalogue cycles. No new-discovery claim.

Next check: Resolve ASAS-SN period alias and obtain RV/orbital posterior or a joint timing/geometry analysis to settle the Gaia association.

Provenance: raw-evidence/cache-manifest.json hashes the cached original QLP files; identity-checks.json verifies TICID/sector. Fresh TESScut URLs/SHA256 are in tesscut-downloads.json; source cones and adapted scripts are retained. manifest.json hashes batch deliverables. No paper edits, source table edits, publication or commits were made.
