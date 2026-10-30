# TIC 431762229: REFUTED

Queue position 45; batch05. Automated GPT-6.1 Sol lead and independent fresh GPT-6.1 Terra review, supervised by Astra. The anonymous project coordinator supplied oversight; these are computational measurements, not human measurements.

## Assessment

Repeated real eclipses contaminate the target aperture, but are spatially associated with TIC431762222, separated32.79arcsec. REFUTED applies to target attribution and the original Gaia-period eclipse interpretation.

## Raw repetition and period

Accepted target eclipse period: not established days. 3 representative cached QLP sectors were reviewed using SAP_FLUX and QUALITY=0. Original packet periods were treated as candidate aliases. Corrected event fits use local linear baselines and trapezoids on raw cadences; no exhaustive sector fit or physical binary model was required.

{
  "accepted_target_ephemeris": null,
  "reason": "No established target repeated eclipse; original alias fitter is not accepted evidence"
}

Representative accepted event measurements:
```json
[]
```

## Source and independent reduction

Two fresh detector-sector difference stacks repeatedly favor TIC431762222; fixed neighbour/target residual SSE ratios are0.0090/0.0188. Free Gaussian deficits lie close to that neighbour. The ratios are descriptive, not calibrated probabilities.

Fresh 11x11 TESScuts and 60 arcsec TIC source cones were obtained. Signed in/out images compare local pre/post baselines. The source model includes signed pixel-integrated Gaussians and fixed source positions with free widths/amplitude/background. Residual ratios are descriptive and do not constitute calibrated PRF probabilities. Neighbours capable under a conservative brightness/depth limit were compared; throughput, uncatalogued sources and TIC photometry remain limitations.

The independent custom target aperture subtracts a per-cadence background from faint cutout pixels and uses the same TESS photons as QLP. It is a distinct extraction, not SPOC or a second telescope. Terra independently inspected raw/custom comparison and signed images; quantitative four-EB depths and receipts are in raw-evidence/terra-helper-results.json. See HELPER.md, all-raw.png, raw-event-panels.png and terra-independent-comparison.png.

## Gaia geometry and association

The contaminating eclipse interval isapproximately1.94d; the original screen alias is rejected as a target eclipse period. No target Gaia orbit association is inferred.

Association flag: contaminating neighbour.

The gaia-geometry.json calculation uses edge-on conjunctions, Tp+389 BTJD conversion, full SB1 covariance in P,gamma,K1,e,omega,Tp order, and linear propagation. Approximate mass function, TIC radius and main-sequence companion radius test feasibility, not a fitted geometry. No automatic Gaia sigma veto was applied.

## Catalogue coverage

no identified prior EB; seven-scope coverage complete: yes. Central coverage includes VSX, SIMBAD primary type, Gaia DR3 EB, Prsa2022, IJspeert2024, vetted Kostov2025 tables3/4 and ASAS-SN. SB* and ROT alone do not count as known EB. This scoped result is separate from physical assessment. TIC183994341 is known and excluded from new additions regardless of physical tier.

## Completion, limits and next check

Full representative review complete; remaining full review=false. Available deciding checks were attempted. Scientific uncertainty: The contaminant is an inferred EB host; its catalogue novelty and precision binary orbit were not independently adjudicated. Source model systematics remain.

Next check: Higher resolution eclipse photometry can verify the contaminating host.

Provenance: raw-evidence/cache-manifest.json hashes the cached original QLP files; identity-checks.json verifies TICID/sector. Fresh TESScut URLs/SHA256 are in tesscut-downloads.json; source cones and adapted scripts are retained. manifest.json hashes batch deliverables. No paper edits, source table edits, publication or commits were made.
