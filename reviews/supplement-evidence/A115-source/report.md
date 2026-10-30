# TIC 447307865 (TYC 9038-1390-1, Gaia DR3 5830628390235398272, SB2): adversarial check, 2026-10-17

**Verdict: CONFIRMED.** This is a grazing eclipse between the two near-twin stars of the Gaia SB2, seen at the A conjunction. P = 40.01697 ± 0.00002 d. There are **five** eclipses, not three: s012 and s039 were missed by the classifier.

## Archives (queried 2026-10-17)
- TAPVizieR returned HTTP 503, so I used VizieR asu-tsv cones of 60". VSX has only Gaia DR3 5830628390235409792 [E, P 0.327 d] at 36.8". That star is G 18.78, so it cannot produce a 1.2% dip.
- SB9, WDS, ASAS-SN, Prša+2022, IJspeert+2024, Kostov+2025 t2/t3/t4: none. The target has no rows in Gaia's vari tables. ExoFOP has no TOI and no CTOI. SIMBAD has TYC 9038-1390-1 [SB*], which is the Gaia orbit only. I did not run a web search beyond these catalogues.
- Gaia AP, fitted as if single: Teff 5707 K, R 2.10 Rsun, L 4.24 Lsun.
- Neighbours: G 13.02 at 36.7" would need a ≥15% eclipse and G 13.13 at 52.6" ≥17%. The rest within 60" are G ≥ 14.2 (≥40%) or the G 16.9–17.4 pair at 7" (>100%).

## Eclipses
I fitted QLP SAP_FLUX with a trapezoid times a quadratic baseline, with prayer-bead errors. This star does not pulsate.

| sector | t0 (BTJD) | QLP depth | own 3x3 TESScut depth | T14 | T12 | notes |
|---|---|---|---|---|---|---|
| s012 | 1628.6571 ± 0.0015 | 1.23% (30-min) | 1.34% | 5.3 h | 1.9 h | q=0, new |
| s039 | 2388.9805 ± 0.0009 | 1.33% | 1.28% | 5.3 h | 1.8 h | every cadence q=4096; new |
| s066 | 3109.2857 ± 0.0012 | 1.38% | 1.27% | 5.3 h | 2.0 h | dip cadences q=0 |
| s101 | 4109.7093 ± 0.0005 | 1.24% | 1.28% | 5.4 h | 2.1 h | clean |
| s102 | 4149.7270 ± 0.0007 | 1.05% | 1.27% | 5.4 h | 2.1 h | clean |

- **The s066 event is real.** I took 19 unrelated stars on the same camera 2 / CCD 4 at all cadences: their median shows a +0.001% deficit at 3109.28, and none dips by more than 0.3%. The cadences inside the dip are q=0; the flagged stretch (bit 30) starts around 3109.5, after egress. The fit is identical with or without the flagged cadences. TARS photometry recovers the event (1.32%), and so does my own TESScut photometry (1.27%).
- **The s039 event is real** even though every cadence is flagged: 15 same-CCD stars are clean at that time, and TARS gives 1.45%.
- **The s093 dip at 3849.85 is a sector systematic.** It is a 0.4% pre-gap drop, and 12 of 21 unrelated stars on the same CCD show it too (median 0.36%).
- **Depth is constant:** 1.27–1.28% in my own aperture in every 2021–2026 sector. The QLP s102 value of 1.05% is a QLP artefact. A grazing eclipse is very sensitive to inclination, so this rules out any measurable inclination drift.
- **Census:** the primaries are the only dips deeper than 0.3% in any sector.
- **Difference images** (TESScut s039/066/101/102): the largest deficit is on the target pixel every time, and the deficit centroid sits 1.3–4.4" from the light centroid. The G 13.02 star on the adjacent pixel shows 0.3–0.9%, which is the wing of the target's PSF; it would need 15%.

## Ephemeris
- Five events give T0 = 1628.6578 ± 0.0009 and P = 40.01697 ± 0.00002 d, with χ² = 1.0 for 3 degrees of freedom and every |O−C| ≤ 1.1 min.
- **The two clean events alone fix the period:** s101 to s102 is one cycle, P = 40.0177 ± 0.0010. s066 then falls exactly 25.000 cycles before s101, so the cycle count is unambiguous.
- Compared with Gaia: P = 39.9995 ± 0.0261 d, a difference of +0.67σ. The events fall +0.75 to +0.80σ after the A conjunction. At the Gaia epoch the ephemeris gives 388.108 against Gaia's A conjunction at 387.74 ± 0.60 (+0.6σ). Gaia's B conjunction is 24 d away.
- Only one eclipse kind is seen, so e cos ω and e sin ω cannot be measured from the light curve. Gaia gives e sin ω = 0.065.

## Physics
- M1 sin³i = 1.041 Msun and M2 sin³i = 1.062 Msun, so the stars are near twins (q = 0.98). a sin i = 63.1 Rsun.
- At A (ν = 90° − ω), component 1 is behind and is eclipsed by component 2. The separation is 56.9 Rsun and the sky speed 10.76 Rsun/d. **The central duration for R1 + R2 ≈ 3.0 Rsun would be 13.4 h; the observed 5.35 h therefore means the eclipse is grazing.**
- I fitted the s101 event with two limb-darkened disks, assuming equal stars and equal light and fixing the sky speed from the Gaia orbit. The best fit is **R = 1.6 Rsun each at b = 0.91** (b being the minimum separation as a fraction of R1 + R2), with residuals at the noise level. R = 1.5 is worse by Δχ² 36 and R = 1.7 by Δχ² 107. Two 1.5–1.6 Rsun stars at 5700 K reproduce Gaia's combined L = 4.2 and R_single = 2.1.
- **So 1.2–1.3% in 5 h fits a grazing eclipse of two similar stars.** A small companion transiting one of them fits worse (Δχ² +87 to +107) and is ruled out anyway, because K1 ≈ K2 makes the companion a near-equal-mass star.
- **The other eclipse belongs at B**, at A + 24.75 ± 0.91 d. At B the stars are farther apart by r_B/r_A = (1 + e sin ω)/(1 − e sin ω) = 1.135 ± 0.056. That puts the closest approach at 3.32 Rsun against R1 + R2 = 3.2 Rsun, so **for the nominal orbit B narrowly misses**. B would be eclipsed only if the ratio is below 1.10 (about 0.6σ), and even then very shallowly.
- **B is covered:** the window falls in s039, s093, s100, s102 and s103, and the stack covers the whole ±3σ range. Nothing is found above about 0.03% in a 4.5-h box. The only feature is the s102 4133.0 common-mode step, which lands at offset 23.17 d.

## Next eclipses (BTJD)
- A (1.27%, 5.4 h, V-shaped): 4349.812, 4389.829, 4429.846, 4469.863 (±0.002)
- B (expected absent; if grazing, ≲0.03%): 4334.5, 4374.6, 4414.6 (±0.9)

## What would settle it further
- High-resolution spectra that resolve both line sets, giving the light ratio and the two radii. Together with the duration and depth this pins b. A light ratio well away from 1 would force a refit with unequal stars.
- A ground-based light curve of the 4349.81 eclipse, which is 1.3% deep and 5 h long. It would also check the A-only geometry against e sin ω.
