# TIC 54140419: CONFIRMED

Full bounded physical review: COMPLETE. Historical search period13.91484d drifts off actual observed family. It selected only noise near sector7 historical center and fails later sector88 alignment. Refitting actual sector61/88 morphology gives three same-kind primary timings, including adjacent sector61 cycles0/1, and period13.91907814d. Fresh availability7/34/61/88 prompted sector34 retrieval, without an additional fitted primary. Sparse/gapped/flagged windows are not clean nulls. No secure secondary; no capable neighbor within60arcsec.

Raw QLP SAP_FLUX representative events and full-sector P/2P morphology were visually inspected. Quality-zero finite positive samples only; predictions guide windows and are never timings. 3 identifiable free-center timings define P=13.919078140041 +/- 0.000026996652d, reference BTJD=2966.086176674 +/- 0.000826230d. Epoch error meaning: Conservative linear timing-fit covariance under the stated cadence floor and scatter inflation; excludes uncalibrated shape and baseline systematics. Epoch kind: Selected repeating eclipse; deeper/secondary identity not established. Linear timing fit using conservative per-event max(formal trapezoid covariance error, half cadence); covariance inflated when reduced chi square exceeds one. Not calibrated coverage or total uncertainty; pipeline timing offsets, trapezoid shape and baseline model systematics are not calibrated. Reduced chi square=0.19512640486348248; zero degrees of freedom is null. All errors retain their named meanings; no calibrated coverage is claimed. Selected same-kind recurring eclipse family; parity and P/2 coverage checked.

Depth=94.127114ppt is the median realized central trapezoid loss d*min(1,w/(2*k)); extrapolated amplitude and ingress remain separately in [measurements.json](../../campaign/batch13/54140419/measurements.json). No secure secondary; exploratory fit is not interpreted as an eclipse timing or counterpart. Secondary raw pooled windows, actual sectors/cycles and fitted phase are retained in [secondary-windows.csv](../../campaign/batch13/54140419/secondary-windows.csv) and [../secondary-phases.json](../../campaign/batch13/secondary-phases.json). No exhaustive blind alias search asserted. [../alias-audit.json](../../campaign/batch13/alias-audit.json) and [../half-period-coverage.json](../../campaign/batch13/half-period-coverage.json) retain recurrence/parity and sampled opposite-phase evidence. Flagged coverage is never a clean null.

Fresh TESScut difference image sector61 stacks2 core/bilateral-sideband events. Target pixel=[7.472352087007673, 7.05230092005368], deficit=[7.522434515537192, 7.0929768179015955]; descriptive offset=0.06452pixel, field PSF residual=0.38941. No arbitrary centroid cut or calibrated localization error is imposed. Every capable neighbor below was inspected at its actual projected pixels; close overlapping neighbors retain probable ownership. Every capable neighbor is assessed above and below; close overlapping cases retain unresolved attribution. All Gaia neighbors are retained in pixel JSON.

| Source | Separation arcsec | G | Required intrinsic loss proxy | Pixel coordinate | Diluted pixel loss |
|---|---:|---:|---:|---|---:|
| None | | | | | |

G-band pairwise brightness screen assumes approximate passband/aperture response; intrinsic required eclipse cannot be directly compared with diluted pixel loss. Unresolved unlisted companions are not excluded.

Alternative reduction: independently extracted background-subtracted TESScut1x1/3x3/5x5 depths=85.34416/84.70230/81.08119ppt; QLP median=94.12711ppt. Pixel sector61 shares the same TESS photons with retained QLP and checks extraction robustness. Independent processing is not an independent instrument. Different apertures respond differently to dilution/background.

Gaia source3035960206561478144: period=13.912957407+/-0.005045410d; e=0.2230642; omega=70.5079319deg; periastron BTJD=391.32917599. Closest conjunction offset=0.3901117d (0.0280394phase), source-specific full-covariance linear error=0.8339847d. Correlation order P,gamma,K,e,omega,Tp with subindices0,3,4,5. Linear propagation is descriptive, not a Gaussian veto or ownership proof. Both conjunctions retained in [../gaia-geometry.json](../../campaign/batch13/gaia-geometry.json). Mass function=0.05330113solar, assumed M1=1.06, minimum M2=0.507919; approximate central duration=6.3313h versus observed=4.3203h. TIC radius/main-sequence companion scaling, edge-on conjunction and stellar evolution are assumptions; this is a plausibility check, not a fitted physical solution.

| Sector | Same-kind cycle | Measured BTJD | Formal center error d | Conservative input error d | Realized depth ppt |
|---|---:|---:|---:|---:|---:|
| 61 | 0 | 2966.086534696 | 0.00036099984 | 0.00115739451 | 94.12711 |
| 61 | 1 | 2980.004889908 | 0.000334324037 | 0.00115739451 | 93.05731 |
| 88 | 53 | 3703.797324982 | 0.000645702504 | 0.00115739945 | 94.83659 |

Catalogue novelty is separate from this physical verdict. Shared coverage matrix and source identity checks are authoritative for catalogue recovery; period agreement alone cannot establish attribution.


Stable review key: R669.

Deciding evidence and numeric artifacts:
- [fresh-pixels/diff_fresh.json](../../campaign/batch13/54140419/fresh-pixels/diff_fresh.json)
- [fresh-pixels/diff_fresh.png](../../campaign/batch13/54140419/fresh-pixels/diff_fresh.png)
- [fresh-pixels/gaia.json](../../campaign/batch13/54140419/fresh-pixels/gaia.json)
- [fresh-pixels/run.log](../../campaign/batch13/54140419/fresh-pixels/run.log)
- [historical/diff_s61.json](../../campaign/batch13/54140419/historical/diff_s61.json)
- [historical/diff_s61.png](../../campaign/batch13/54140419/historical/diff_s61.png)
- [historical/gaia.json](../../campaign/batch13/54140419/historical/gaia.json)
- [measurements.json](../../campaign/batch13/54140419/measurements.json)
- [phase-review.png](../../campaign/batch13/54140419/phase-review.png)
- [raw-events.png](../../campaign/batch13/54140419/raw-events.png)
- [raw-windows.csv](../../campaign/batch13/54140419/raw-windows.csv)
- [secondary-windows.csv](../../campaign/batch13/54140419/secondary-windows.csv)

[Batch audits and scripts](../../campaign/batch13/INDEX.md). [Depth correction provenance](../../campaign/depth-audit/README.md).
