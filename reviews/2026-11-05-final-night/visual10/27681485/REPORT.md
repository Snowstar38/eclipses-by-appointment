# X007 / TIC 27681485

Gaia DR3 655828900372514688; frozen visual10 queue, M029.

Completion: COMPLETE_BOUNDED. Physical tier: **PLAUSIBLE**. Association: UNRESOLVED_CLOCK_AND_GAIA_GEOMETRY.

S44/S45 have convincing 1.90/1.88 d flat-bottomed events with trapezoid centers 2505.65630/2542.17602 BTJD, depth 8.58/8.41 ppt. A compatible S72 notch at 3272.3503 is highly baseline dependent; cycles 0,1,21 give descriptive P36.50930 d using conservative timing allowances 0.03,0.03,0.15 d. S46 late partial primary ingress is supporting morphology, not a timing. Its singular covariance is excluded. S44 independent custom aperture shows 7.73 ppt and a target-centered deficit. Integer divisors 2-10 were checked against actual coverage, but P/2 remains viable: the S46 intermediate window has an actual ~8.8 ppt notch and the S71 intermediate window is ramp dominated, not a clean null. The notch alone cannot establish opposite-kind identity. Only S44/S45 are secure complete events; S72 and partial S46 cannot establish a unique same-kind clock. The plausible tier retains strong real eclipse-like variability while withholding a system/clock association. Full Gaia covariance predicts conjunction B about 2.46 d early (95%offset[0.99,3.93]d), a material~3sigma tension despite broad period agreement.

Limitations: Complete capable-neighbor inventory remains unknown after two failed Gaia requests. S72 duration 1.21 d differs from earlier 1.9 d and lies on steep trend; model-dependent late timing and Gaia geometry prevent confirmation. Neither 36.50930 d nor its half is a unique orbital-period solution. No formal precision error is claimed.

Next check: Resolve capable close neighbors, obtain source-specific eclipse photometry, and test whether Gaia orbit bias or another binary explains the phase offset.

## Scope and provenance

Raw QLP SAP was read with finite positive flux and QUALITY=0; source SHA256 and FITS TICID were checked before use. 5 cached sectors were inspected; exact sample membership and queue hash are unchanged. Representative full-sector context and ranked windows are in `all-sectors.png` and `ranked-windows.png`; raw coverage and selected screen windows are in `screen.json`. Detector contrast is a maximized ordering statistic, not calibrated eclipse significance. Event-kind assignments come from raw morphology, not the selection cue.

Alternative TESScut extractions test processing/source location using the same photons, not an independent observing occasion. The bounded review does not require all-event/all-sector precision characterization. Completion means the deciding bounded review is finished and limitations are explicitly adjudicated; it does not mean every possible observation or catalogue has succeeded. Physical tier is independent of catalogue novelty and publication eligibility. Central scoped catalogue receipts are under `../shared-catalogues/`; failed requests are unknown, and no claim of exhaustive priority is made. Parent owns final catalogue/novelty eligibility.

Numeric evidence: `../lead-source-receipts.json`, `../lead-clocks.json`, `../initial-minima-diagnostics.json` (superseded fits explicitly not used), `../lead-deciding-checks.json`, `../lead-gaia-covariance.json`, and helper artifacts where present.
