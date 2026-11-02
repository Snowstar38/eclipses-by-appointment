# TIC 13882408: CONFIRMED

Full bounded physical review: COMPLETE. Five repeated narrow deep primary eclipses and unequal secondary near0.486; no capable Gaia neighbor within60arcsec.

Raw QLP SAP_FLUX representative events and full-sector P/2P morphology were visually inspected. Quality-zero finite positive samples only; predictions guide windows and are never timings. 5 identifiable free-center timings define P=12.927313217175 +/- 0.000013499816d, reference BTJD=1519.208309786 +/- 0.002158091d. Epoch error meaning: Conservative linear timing-fit covariance under the stated cadence floor and scatter inflation; excludes uncalibrated shape and baseline systematics. Epoch kind: Deeper primary established by unequal observed secondary. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. Reduced chi square=0.4986003655328546; zero degrees of freedom is null. All errors retain their named meanings; no calibrated coverage is claimed. Selected same-kind recurring eclipse family; parity and P/2 coverage checked.

Depth=71.155976ppt is the median realized central trapezoid loss d*min(1,w/(2*k)); extrapolated amplitude and ingress remain separately in [measurements.json](../../campaign/batch13/13882408/measurements.json). Measured secondary phase 0.48647041, formal phase error 7.3685115e-05, realized depth 23.95888ppt. Formal pooled trapezoid covariance only; sector normalization, red noise and shape systematics uncalibrated. Secondary raw pooled windows, actual sectors/cycles and fitted phase are retained in [secondary-windows.csv](../../campaign/batch13/13882408/secondary-windows.csv) and [../secondary-phases.json](../../campaign/batch13/secondary-phases.json). No exhaustive blind alias search asserted. [../alias-audit.json](../../campaign/batch13/alias-audit.json) and [../half-period-coverage.json](../../campaign/batch13/half-period-coverage.json) retain recurrence/parity and sampled opposite-phase evidence. Flagged coverage is never a clean null.

Fresh TESScut difference image sector61 stacks2 core/bilateral-sideband events. Target pixel=[7.893511091501619, 7.941925378656464], deficit=[7.76109332104268, 7.981626293770827]; descriptive offset=0.13824pixel, field PSF residual=0.38774. No arbitrary centroid cut or calibrated localization error is imposed. Every capable neighbor below was inspected at its actual projected pixels; close overlapping neighbors retain probable ownership. Every capable neighbor is assessed above and below; close overlapping cases retain unresolved attribution. All Gaia neighbors are retained in pixel JSON.

| Source | Separation arcsec | G | Required intrinsic loss proxy | Pixel coordinate | Diluted pixel loss |
|---|---:|---:|---:|---|---:|
| None | | | | | |

G-band pairwise brightness screen assumes approximate passband/aperture response; intrinsic required eclipse cannot be directly compared with diluted pixel loss. Unresolved unlisted companions are not excluded.

Alternative reduction: independently extracted background-subtracted TESScut1x1/3x3/5x5 depths=63.81090/61.55883/57.26004ppt; QLP median=71.15598ppt. Pixel sector61 shares the same TESS photons with retained QLP and checks extraction robustness. Independent processing is not an independent instrument. Different apertures respond differently to dilution/background.

Gaia source5736720579555504256: period=12.927622285+/-0.004000789d; e=0.0321342; omega=242.2517626deg; periastron BTJD=386.94870895. Closest conjunction offset=0.0333081d (0.0025765phase), source-specific full-covariance linear error=0.4027193d. Correlation order P,gamma,K,e,omega,Tp with subindices0,3,4,5. Linear propagation is descriptive, not a Gaussian veto or ownership proof. Both conjunctions retained in [../gaia-geometry.json](../../campaign/batch13/gaia-geometry.json). Mass function=0.09320003solar, assumed M1=0.99, minimum M2=0.623787; approximate central duration=9.2793h versus observed=6.0115h. TIC radius/main-sequence companion scaling, edge-on conjunction and stellar evolution are assumptions; this is a plausibility check, not a fitted physical solution.

| Sector | Same-kind cycle | Measured BTJD | Formal center error d | Conservative input error d | Realized depth ppt |
|---|---:|---:|---:|---:|---:|
| 8 | 0 | 1519.209821234 | 0.000704539466 | 0.0104166517 | 71.15598 |
| 61 | 112 | 2967.067901383 | 0.000452535978 | 0.00115742444 | 71.44064 |
| 61 | 113 | 2979.994132044 | 0.000477591178 | 0.00115742444 | 71.63334 |
| 99 | 196 | 4052.962553803 | 0.00092889618 | 0.00115743754 | 62.77073 |
| 99 | 197 | 4065.888201469 | 0.000403088185 | 0.00115743754 | 65.27558 |

Catalogue novelty is separate from this physical verdict. Shared coverage matrix and source identity checks are authoritative for catalogue recovery; period agreement alone cannot establish attribution.


Stable review key: R667.

Deciding evidence and numeric artifacts:
- [fresh-pixels/diff_fresh.json](../../campaign/batch13/13882408/fresh-pixels/diff_fresh.json)
- [fresh-pixels/diff_fresh.png](../../campaign/batch13/13882408/fresh-pixels/diff_fresh.png)
- [fresh-pixels/gaia.json](../../campaign/batch13/13882408/fresh-pixels/gaia.json)
- [fresh-pixels/run.log](../../campaign/batch13/13882408/fresh-pixels/run.log)
- [historical/diff_s61.json](../../campaign/batch13/13882408/historical/diff_s61.json)
- [historical/diff_s61.png](../../campaign/batch13/13882408/historical/diff_s61.png)
- [historical/gaia.json](../../campaign/batch13/13882408/historical/gaia.json)
- [measurements.json](../../campaign/batch13/13882408/measurements.json)
- [phase-review.png](../../campaign/batch13/13882408/phase-review.png)
- [raw-events.png](../../campaign/batch13/13882408/raw-events.png)
- [raw-windows.csv](../../campaign/batch13/13882408/raw-windows.csv)
- [secondary-windows.csv](../../campaign/batch13/13882408/secondary-windows.csv)

[Batch audits and scripts](../../campaign/batch13/INDEX.md). [Depth correction provenance](../../campaign/depth-audit/README.md).
