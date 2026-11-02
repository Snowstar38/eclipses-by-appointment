# TIC 429570033: CONFIRMED

Full bounded physical review: COMPLETE. Three deep narrow primary eclipses including consecutive sector84 cycles114/115 plus unequal secondary near0.682. Sector16 lacks a fitted primary, not a clean null. No capable neighbor within60arcsec.

Raw QLP SAP_FLUX representative events and full-sector P/2P morphology were visually inspected. Quality-zero finite positive samples only; predictions guide windows and are never timings. 3 identifiable free-center timings define P=16.146625951072 +/- 0.000104785390d, reference BTJD=3382.258545241 +/- 0.001155811d. Epoch error meaning: Conservative linear timing-fit covariance under the stated cadence floor and scatter inflation; excludes uncalibrated shape and baseline systematics. Epoch kind: Deeper primary established by unequal observed secondary. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. Reduced chi square=0.007650194010375677; zero degrees of freedom is null. All errors retain their named meanings; no calibrated coverage is claimed. Selected same-kind recurring eclipse family; parity and P/2 coverage checked.

Depth=293.446739ppt is the median realized central trapezoid loss d*min(1,w/(2*k)); extrapolated amplitude and ingress remain separately in [measurements.json](../../campaign/batch12/429570033/measurements.json). Measured secondary phase 0.68194978, formal phase error 2.3304537e-05, realized depth 50.12908ppt. Formal pooled trapezoid covariance only; sector normalization, red noise and shape systematics uncalibrated. Secondary raw pooled windows, actual sectors/cycles and fitted phase are retained in [secondary-windows.csv](../../campaign/batch12/429570033/secondary-windows.csv) and [../secondary-phases.json](../../campaign/batch12/secondary-phases.json). No exhaustive blind alias search asserted. [../alias-audit.json](../../campaign/batch12/alias-audit.json) and [../half-period-coverage.json](../../campaign/batch12/half-period-coverage.json) retain recurrence/parity and sampled opposite-phase evidence. Flagged coverage is never a clean null.

Fresh TESScut difference image sector56 stacks2 core/bilateral-sideband events. Target pixel=[7.397841537902449, 7.384829290605374], deficit=[7.240675753333409, 7.4119798681592615]; descriptive offset=0.15949pixel, field PSF residual=0.46517. No arbitrary centroid cut or calibrated localization error is imposed. Every capable neighbor below was inspected at its actual projected pixels; close overlapping neighbors retain probable ownership. Other capable sources are displaced from compact deficit core but crowding limits localization. All Gaia neighbors are retained in pixel JSON.

| Source | Separation arcsec | G | Required intrinsic loss proxy | Pixel coordinate | Diluted pixel loss |
|---|---:|---:|---:|---|---:|
| None | | | | | |

G-band pairwise brightness screen assumes approximate passband/aperture response; intrinsic required eclipse cannot be directly compared with diluted pixel loss. Unresolved unlisted companions are not excluded.

Alternative reduction: independently extracted background-subtracted TESScut1x1/3x3/5x5 depths=234.81677/225.63601/227.67984ppt; QLP median=293.44674ppt. Pixel sector56 is a distinct observing occasion on the same TESS instrument; no same-sector QLP comparison claimed. Independent processing is not an independent instrument. Different apertures respond differently to dilution/background.

Gaia source2179272526332127232: period=16.144166157+/-0.004812888d; e=0.2874276; omega=23.9610338deg; periastron BTJD=393.49150057. Closest conjunction offset=0.3608174d (0.0223497phase), source-specific full-covariance linear error=0.7578532d. Correlation order P,gamma,K,e,omega,Tp with subindices0,3,4,5. Linear propagation is descriptive, not a Gaussian veto or ownership proof. Both conjunctions retained in [../gaia-geometry.json](../../campaign/batch12/gaia-geometry.json). Mass function=0.0843095solar, assumed M1=1.449, minimum M2=0.739028; approximate central duration=5.8682h versus observed=4.8079h. TIC radius/main-sequence companion scaling, edge-on conjunction and stellar evolution are assumptions; this is a plausibility check, not a fitted physical solution.

| Sector | Same-kind cycle | Measured BTJD | Formal center error d | Conservative input error d | Realized depth ppt |
|---|---:|---:|---:|---:|---:|
| 76 | 101 | 3382.258550532 | 0.000137417721 | 0.00115739355 | 293.44674 |
| 84 | 114 | 3592.164608524 | 0.000100868475 | 0.00115739031 | 292.12567 |
| 84 | 115 | 3608.311377345 | 0.00013170009 | 0.00115739031 | 295.40795 |

Catalogue novelty is separate from this physical verdict. Shared coverage matrix and source identity checks are authoritative for catalogue recovery; period agreement alone cannot establish attribution.


Stable review key: R655.

Deciding evidence and numeric artifacts:
- [fresh-pixels/diff_fresh.json](../../campaign/batch12/429570033/fresh-pixels/diff_fresh.json)
- [fresh-pixels/diff_fresh.png](../../campaign/batch12/429570033/fresh-pixels/diff_fresh.png)
- [fresh-pixels/gaia.json](../../campaign/batch12/429570033/fresh-pixels/gaia.json)
- [fresh-pixels/run.log](../../campaign/batch12/429570033/fresh-pixels/run.log)
- [historical/diff_s56.json](../../campaign/batch12/429570033/historical/diff_s56.json)
- [historical/diff_s56.png](../../campaign/batch12/429570033/historical/diff_s56.png)
- [historical/gaia.json](../../campaign/batch12/429570033/historical/gaia.json)
- [measurements.json](../../campaign/batch12/429570033/measurements.json)
- [phase-review.png](../../campaign/batch12/429570033/phase-review.png)
- [raw-events.png](../../campaign/batch12/429570033/raw-events.png)
- [raw-windows.csv](../../campaign/batch12/429570033/raw-windows.csv)
- [secondary-windows.csv](../../campaign/batch12/429570033/secondary-windows.csv)

[Batch audits and scripts](../../campaign/batch12/INDEX.md). [Depth correction provenance](../../campaign/depth-audit/README.md).
