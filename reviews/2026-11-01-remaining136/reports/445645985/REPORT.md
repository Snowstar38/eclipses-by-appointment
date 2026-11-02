# TIC 445645985: CONFIRMED

Full bounded physical review: COMPLETE. Four repeated primary eclipses with observed shallow secondary near0.7873; two capable40.88/50.73arcsec sources lie away from compact deficit.

Raw QLP SAP_FLUX representative events and full-sector P/2P morphology were visually inspected. Quality-zero finite positive samples only; predictions guide windows and are never timings. 4 identifiable free-center timings define P=15.941576101817 +/- 0.000107173044d, reference BTJD=1792.415356135 +/- 0.007403165d. Epoch error meaning: Conservative linear timing-fit covariance under the stated cadence floor and scatter inflation; excludes uncalibrated shape and baseline systematics. Epoch kind: Deeper primary established by unequal observed secondary. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. Reduced chi square=0.29470213321940947; zero degrees of freedom is null. All errors retain their named meanings; no calibrated coverage is claimed. Selected same-kind recurring eclipse family; parity and P/2 coverage checked.

Depth=130.086715ppt is the median realized central trapezoid loss d*min(1,w/(2*k)); extrapolated amplitude and ingress remain separately in [measurements.json](../../campaign/batch12/445645985/measurements.json). Measured secondary phase 0.78731516, formal phase error 0.00014117914, realized depth 11.45414ppt. Formal pooled trapezoid covariance only; sector normalization, red noise and shape systematics uncalibrated. Secondary raw pooled windows, actual sectors/cycles and fitted phase are retained in [secondary-windows.csv](../../campaign/batch12/445645985/secondary-windows.csv) and [../secondary-phases.json](../../campaign/batch12/secondary-phases.json). No exhaustive blind alias search asserted. [../alias-audit.json](../../campaign/batch12/alias-audit.json) and [../half-period-coverage.json](../../campaign/batch12/half-period-coverage.json) retain recurrence/parity and sampled opposite-phase evidence. Flagged coverage is never a clean null.

Fresh TESScut difference image sector18 stacks2 core/bilateral-sideband events. Target pixel=[7.247130469941494, 7.757436670640473], deficit=[7.4102256455206295, 7.725583538361966]; descriptive offset=0.16618pixel, field PSF residual=0.98672. No arbitrary centroid cut or calibrated localization error is imposed. Every capable neighbor below was inspected at its actual projected pixels; close overlapping neighbors retain probable ownership. Other capable sources are displaced from compact deficit core but crowding limits localization. All Gaia neighbors are retained in pixel JSON.

| Source | Separation arcsec | G | Required intrinsic loss proxy | Pixel coordinate | Diluted pixel loss |
|---|---:|---:|---:|---|---:|
| 457464083466986496 | 40.87769335827198 | 14.203033 | 0.6692969762611214 | [9.169950482032025, 7.9998241896658655] | 0.027349025705879323 |
| 457464323985153280 | 50.72814082885142 | 13.59876 | 0.43915109035103744 | [6.949760464515536, 10.149413553030303] | 0.0021670009135249173 |

G-band pairwise brightness screen assumes approximate passband/aperture response; intrinsic required eclipse cannot be directly compared with diluted pixel loss. Unresolved unlisted companions are not excluded.

Alternative reduction: independently extracted background-subtracted TESScut1x1/3x3/5x5 depths=118.15505/105.77361/61.59252ppt; QLP median=130.08672ppt. Pixel sector18 shares the same TESS photons with retained QLP and checks extraction robustness. Independent processing is not an independent instrument. Different apertures respond differently to dilution/background.

Gaia source457464113524362496: period=15.937289414+/-0.013099912d; e=0.4995792; omega=12.8087903deg; periastron BTJD=388.25615447. Closest conjunction offset=0.4497241d (0.0282184phase), source-specific full-covariance linear error=0.7154511d. Correlation order P,gamma,K,e,omega,Tp with subindices0,3,4,5. Linear propagation is descriptive, not a Gaussian veto or ownership proof. Both conjunctions retained in [../gaia-geometry.json](../../campaign/batch12/gaia-geometry.json). Mass function=0.03734818solar, assumed M1=1.152, minimum M2=0.459445; approximate central duration=5.8238h versus observed=4.9374h. TIC radius/main-sequence companion scaling, edge-on conjunction and stellar evolution are assumptions; this is a plausibility check, not a fitted physical solution.

| Sector | Same-kind cycle | Measured BTJD | Formal center error d | Conservative input error d | Realized depth ppt |
|---|---:|---:|---:|---:|---:|
| 18 | -1 | 1792.413881246 | 0.000532514466 | 0.0104166891 | 131.58724 |
| 18 | 0 | 1808.357701957 | 0.000482518907 | 0.0104166891 | 118.50418 |
| 58 | 68 | 2892.384726070 | 0.000286241987 | 0.00115741244 | 129.76512 |
| 58 | 69 | 2908.325073058 | 0.0002261763 | 0.00115741244 | 130.40831 |

Catalogue novelty is separate from this physical verdict. Shared coverage matrix and source identity checks are authoritative for catalogue recovery; period agreement alone cannot establish attribution.


Stable review key: R654.

Deciding evidence and numeric artifacts:
- [fresh-pixels/diff_fresh.json](../../campaign/batch12/445645985/fresh-pixels/diff_fresh.json)
- [fresh-pixels/diff_fresh.png](../../campaign/batch12/445645985/fresh-pixels/diff_fresh.png)
- [fresh-pixels/gaia.json](../../campaign/batch12/445645985/fresh-pixels/gaia.json)
- [fresh-pixels/run.log](../../campaign/batch12/445645985/fresh-pixels/run.log)
- [historical/diff_s18.json](../../campaign/batch12/445645985/historical/diff_s18.json)
- [historical/diff_s18.png](../../campaign/batch12/445645985/historical/diff_s18.png)
- [historical/gaia.json](../../campaign/batch12/445645985/historical/gaia.json)
- [measurements.json](../../campaign/batch12/445645985/measurements.json)
- [phase-review.png](../../campaign/batch12/445645985/phase-review.png)
- [raw-events.png](../../campaign/batch12/445645985/raw-events.png)
- [raw-windows.csv](../../campaign/batch12/445645985/raw-windows.csv)
- [secondary-windows.csv](../../campaign/batch12/445645985/secondary-windows.csv)

[Batch audits and scripts](../../campaign/batch12/INDEX.md). [Depth correction provenance](../../campaign/depth-audit/README.md).
