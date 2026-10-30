# TIC 305944592 (TYC 9053-432-1, Gaia DR3 5910672149533277952): adversarial check, 2026-10-17

**Verdict: CONFIRMED.** It is a single-lined F subgiant with an M-dwarf companion that transits it once per orbit, at the Gaia A conjunction. P = 34.48723 ± 0.00005 d.

## Archives (queried 2026-10-17)
- TAPVizieR returned HTTP 503 (so `cats.py` gave "VSX: error"). I repeated the queries as VizieR asu-tsv cones of 60": VSX found only Gaia DR3 5910672179592197504 [DSCT|GDOR], which is 10.7" away at G 17.69. That star cannot produce either the 0.86% dips or the 0.2% pulsations, so the VSX entry is not prior art. SB9, WDS, ASAS-SN II/366, Prša+2022, IJspeert+2024 OBAF-EB, Kostov+2025 t2/t3/t4 and Gaia I/358 veb all returned nothing.
- Gaia DR3 vari_summary, vari_eclipsing_binary and vari_classifier_result have no rows. SIMBAD has TYC 9053-432-1 [SB*] at 0.0", which is the Gaia orbit only. ExoFOP has no TOI, no CTOI and no spectra. I did not run a web search beyond these catalogues.
- Gaia AP: Teff 6608 K, logg 3.62, R_FLAME 3.25 Rsun, M_FLAME 1.85 Msun, L 18 Lsun. TIC gives R 3.27 Rsun and M 1.46 Msun. RUWE 0.95.

## Eclipses
I fitted SAP_FLUX from QLP with a trapezoid times a quadratic baseline. The star pulsates coherently at 12.00, 13.22, 10.65, 9.75, 10.96 and 9.42 c/d, with the same set of modes in every sector from 2019 to 2026. I removed 12 sine terms per sector (prewhitening), which cuts the rms from 0.26% to about 0.1%. Errors come from a prayer-bead (cyclic residual-shift) analysis.

| sector | t0 (BTJD) | depth (QLP pw) | own 3x3 TESScut depth | T14 | T12 |
|---|---|---|---|---|---|
| s012 (partial, egress only, all flagged) | 1626.113 ± 0.008 | (shape fixed) | – | – | – |
| s013 | 1660.6024 ± 0.0037 | 0.953% | 0.866% | 19.2 h | 3.2 h |
| s039 | 2384.8401 ± 0.0026 | 0.872% | 0.862% | 17.7 h | 0.9 h |
| s100 (partial, clean q=0 egress) | 4074.714 ± 0.005 | (shape fixed) | – | – | – |
| s101 | 4109.1966 ± 0.0027 | 0.789% | 0.859% | 18.4 h | 2.3 h |
| s102 | 4143.6876 ± 0.0036 | 0.744% | 0.859% | 18.2 h | 2.0 h |

- **Two more events than the classifier reported:** partial eclipses at s012 1626.11 and s100 4074.71, each with egress at the predicted time.
- **Detrending and flags:** fits on raw q=0 data, on all cadences, and on prewhitened data agree to within 0.007 d in t0. In s013 there are 10 flagged cadences inside the event (9 with q=4096 and 1 with q=4132, a background spike). Dropping the spike and including the rest gives 0.918% and t0 1660.6014. The flags make no difference.
- **Depth is constant:** the fall seen in QLP (0.95 → 0.74%) comes from QLP's aperture and background handling, not the star. In my own fixed 3x3 aperture the four depths are 0.866, 0.862, 0.859 and 0.859%, constant to 1% between 2019 and 2026. Durations are 18.3–19.8 h, so there is no sign of the impact parameter changing.
- **Other pipelines agree:** TESS-SPOC s013 gives SAP 0.86% / PDCSAP 0.92%, T14 19 h. TESS-SPOC s039 gives 0.85% / 0.87%, 18.5 h. Eleanor-lite s013 gives 0.87–0.93%, and eleanor-lite s012 recovers the partial event at 1626.14.
- **Difference images** (TESScut, all four full events): the largest deficit is on the target pixel every time, and the deficit centroid sits 3–7" (under 0.35 px) from the light centroid. The only neighbour bright enough to matter is G 12.34 at 53"; it would need a ≥5.7% eclipse, and its own pixel shows −0.1% to +0.2%. All other neighbours are G ≥ 14.7 and would need eclipses deeper than about 75%.
- **Census:** with 6, 12 and 19-h boxes in every sector, the four eclipses are the only dips deeper than 0.3%.

## Ephemeris
- T0 = BTJD 1626.1182 ± 0.0026, P = 34.48723 ± 0.00005 d. The fit uses all 6 events: χ² = 3.3 for 4 degrees of freedom, every |O−C| under 7 min. The cycle count is unique because s101 and s102 hold consecutive eclipses.
- Compared with Gaia: P_Gaia = 34.5029 ± 0.0432 d, a difference of −0.36σ.
- Projected back to the Gaia epoch, the ephemeris puts an eclipse at 384.578. Gaia's A conjunction there is 384.40 ± 0.96 (+0.19σ). Gaia's B conjunction is 19 d away. In the 2019–2026 windows the events fall 0.17–0.29σ early.
- Only one eclipse kind is seen, so e cos ω and e sin ω cannot be measured from the light curve. Gaia gives e cos ω = −0.081 and e sin ω = −0.246.

## Physics
- Mass function f(m) = 0.00525 Msun, so m2(i = 90°) = 0.248 Msun for M1 = 1.46, or 0.289 Msun for M1 = 1.85.
- a = 53–57 Rsun.
- From the depth, k = 0.093, which gives **R2 = 0.30 Rsun. That is the main-sequence radius of a 0.25–0.29 Msun M dwarf**, so the mass from the RVs and the radius from the eclipse agree.
- The A conjunction (companion in front) falls near apastron: separation 66–71 Rsun, sky speed 7.6–8.2 Rsun/d. The **predicted central duration is 20.8–22.6 h**. The observed 18.7 h implies b = 0.48–0.62 and i = 88.3–88.7°. The T12/T14 ratio gives b ≈ 0.36 independently, roughly consistent. The predicted 19-h duration fits.
- **The secondary (B) eclipse is geometrically required** (b_B ≈ 0.3, T14 ≈ 12–13 h) but should be only about 0.04–0.07% deep (my crude M-dwarf surface-brightness estimate). It falls at A + 15.54 ± 1.19 d. Nothing is detected. Stacking every sector in a 12.5-h box gives at most 0.034% (at A + 15.21 d), and noise peaks of the same height appear elsewhere, so the upper limit is about 0.035%. This is mild tension at most. The classifier's "no B at 0.3%" is fully expected.

## Next eclipses (BTJD)
- A (0.86%, 18.7 h): 4350.609, 4385.096, 4419.584, 4454.071 (±0.005)
- B (≲0.05%, about 12.5 h): 4331.7, 4366.2, 4400.6, 4435.1 (±1.2)

## What would settle it further
- A spectrum at quadrature, to check the K1 and γ of the RV orbit.
- A stacked TESS secondary at the 0.03% level, which would also measure e cos ω (from the timing) and the M-dwarf temperature.
- Ground photometry of the A eclipse on 4350.61, which is above the ~0.3% level that ground photometry reaches.
