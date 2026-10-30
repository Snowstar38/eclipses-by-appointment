# TIC 455491894 (TYC 3608-1307-1) -- adversarial check, 2026-10-17

**Verdict: PLAUSIBLE.** The two B-kind dips are real, on target, and exactly 3 Gaia periods apart, so they almost certainly belong to the SB2. Two things keep this short of CONFIRMED:
- There are only two events, both of one kind.
- Their phase is 1.57 d early. Once TESS pins the period, that is 5.6–13 σ off Gaia's prediction, not the classifier's −2.8 σ.

## Archives
| Source | Query | Result |
|---|---|---|
| `cats.py --r 60` and VizieR asu-tsv | VSX, ASAS-SN, SB9, WDS, Prša+2022, IJspeert+2024, Kostov t3/t4 (TAPVizieR was returning 503) | none |
| SIMBAD | position | TYC 3608-1307-1 [SB*] |
| Gaia DR3 | vari_summary, vari_eclipsing_binary | no rows |
| ExoFOP | TOI / CTOI | none; contamination ratio 0.21 |
| Web | TYC and TIC names | nothing |
| Kostov+2025 table 2 (unvetted ML list) | 60" cone | flags the **neighbour** TIC 455491931 (34", Tmag 13.46, = Gaia G 14.44), not the target |

Gaia NSS SB2:
- P 57.3498 ± 0.0100 d, e 0.3464 ± 0.0057, ω 312.29 ± 1.14°, T_peri BTJD 414.716 ± 0.188
- K1 33.66 ± 0.33 km/s, K2 36.96 ± 0.27 km/s
- 28 RV transits; goodness_of_fit 28.8 (a poor fit)

MAST light curves: QLP, TARS and TESS-SPOC FFI for s16, 56, 76, 83.

## Eclipses
Raw QLP SAP_FLUX, q==0, no trimming (`ecl.py`):

| Event | Mid-time (BTJD) | Depth | T14 | T12 | Flat bottom |
|---|---|---|---|---|---|
| s76 B | 3392.13935 ± 0.7 min | 2.31% | 5.43 h | 2.03 h | 1.36 h |
| s83 B | 3564.19008 ± 0.6 min | 2.30% | 5.52 h | 2.21 h | 1.10 h |

- Neither event has a flagged cadence in eclipse. Background and centroid excursions are ≤ 1.5 mpx.
- s76 has no data gap within 2 d. The s83 gap (3564.84–3565.03) starts 0.53 d after egress, so both events have full pre- and post-baseline.
- The classifier's "2.6% V, 3.4 h" was a box estimate; the trapezoid has a short flat bottom.
- TESS-SPOC PDCSAP gives 3392.13793 (2.28%, 5.39 h) and 3564.18991 (2.36%, 5.47 h): the same events, within 2 min.

**Common mode** (`commonmode.py`, every star in the shared folder):
- At 3564.19 the target dips 2.04% and ranks 1st of 249. The other stars' median is 0.015%; the 23 on the target's camera/CCD have median 0.04% and max 0.10%.
- At the listed common-mode time 3564.45 the other stars' median is 0.05% and the target reads −0.04%, i.e. clean.
- At s76 3392.14 the target ranks 1st of 227; the other stars' median is −0.006%.
- So neither event is a sector systematic.

**Blind census** (>0.3%, 1-h bins): nothing else in s16, s56 or s83. s76 has 0.3–0.38% wiggles at 3371.4–3373.4 inside an SAP hump; there the target ranks 7th of 149, so this is common-mode-like and not eclipse-shaped.

## Ephemeris
- The spacing is 172.05073 d = 3 × **57.35024 ± 0.0003 d**, which matches Gaia's P to 0.04 σ. P/2 and P/4 are not compatible with Gaia's P.
- With P fixed at the TESS value, Gaia predicts B at 3393.712 and 3565.763. Both observed events are **−1.573 d** early, by the same amount.
- **The classifier's −2.8 σ is out of date.** It included Gaia's period error × 51 cycles (0.51 d), which the TESS spacing removes. Conditioned on the TESS P, the predicted-B σ is 0.22 d with independent errors, 0.12 d with corr(T_peri, ω) = +0.926 (the only strong term in corr_vec), or 0.28 d with −0.926. That makes the offset −7.3, −13.4 or −5.6 σ.
- **A period shift within Gaia's errors cannot explain it.** It would need P = 57.319 d (−3 σ_Gaia), and the TESS spacing excludes that at about 100 σ.
- **Single-parameter fixes:** T_peri −1.573 d (−8.4 σ), or ω +17.7° (+15.5 σ, giving e cos ω 0.300 instead of 0.233), or e −0.172 (−30 σ).
- The most economical reading is that Gaia's T_peri (and perhaps ω) errors are underestimated about 3–7× (gof 28.8). Without an A eclipse the photometry cannot measure e cos ω independently.

## A-kind
- Gaia's e and ω put A at B + 19.958 ± 0.233 d (phase 0.348).
- **s83 3584.147:** q==0 data, one-sided baseline; depth +0.02 ± 0.01% for T14 of 5.5–9 h.
- **s16 1748.94:** flagged cadences only; +0.04 ± 0.04%.
- **s56 2838.59:** falls in the data gap.
- At Gaia's nominal unshifted A times: s16 1750.51 is in a gap, s56 2840.17 is covered and flat, s83 3585.72 is after the sector ends.
- **Phase coverage:** 99.5% of the orbit is measurable with a 6-h box. The max box depth over phases 0.25–0.45 after B is 0.12%, and the only uncovered sliver is 0.345–0.350, at the end of s83.
- **Constraint:** no A eclipse deeper than about 0.05% if A − B ≤ 20.1 d. That covers about 74% of the Gaia A − B distribution; A − B > 20.1 d is unconstrained.
- **This absence is expected.** The conjunction separations are 0.700a at B (near periastron) and 1.183a at A, so b_A = 1.69 b_B.

## Independence
**Second pipeline:** TESS-SPOC (above).

**Difference images** (TESScut s76 and s83; `diff_s76B`, `diff_s83B`):
- The flux lost peaks on the target pixel. The deficit centroid is 0.16 px (s76) and 0.09 px (s83) from the target's Gaia position.
- The deficit is more concentrated than the light: 0.82 of it sits in the 3×3 box, which holds only 0.64 of the light.

**Neighbour dilution:** fractional dip each neighbour would need for a 2.3% dip on the target.

| Neighbour | Separation | Would need |
|---|---|---|
| G 12.87 | 51" | 20% |
| G 13.73 | 29" | 45% |
| G 13.81 | 39" | 49% |
| G 14.40 | 29" | 84% |
| G 14.44 (= the Kostov-flagged TIC 455491931) | 35" | 87% |
| everything fainter than G ≈ 14.7 | — | >100% |

The 20–87% cases are physically possible on dilution alone, but every one of those stars lies 1.4–2.4 px from the deficit centroid, and their pixels show lower fractional depth (0.6–1.9%) than the target pixel (2.1–2.2%). They are excluded.

## Physics
**Masses from Gaia's K's** (P 57.350 d, e 0.346):
- M1 sin³i = 0.904 ± 0.015 Msun, M2 sin³i = 0.823 ± 0.017 Msun, q = 0.910
- a sin i = 75.07 Rsun; f(M) = 0.187 Msun

**Which star is in front at each conjunction:**
- At B (ν = 270° − ω) the Gaia primary is in front: the observed eclipse is a grazing occultation of the Gaia secondary.
- At A the secondary would be in front, but the separation there is 1.69× larger.

**My EB model** (`ebfit.py`): Gaia e and ω fixed, star 2 = Gaia primary, four radius/light-ratio priors (R_prim/R_sec, L_prim/L_sec = 1/1, 1.15/1.5, 1.3/2, 0.9/0.7; `ebfit_con_*`). All four fit the two B eclipses equally well (rms 0.71 ppt):
- i 87.4–87.6°
- R1 + R2 = 0.035–0.036a = 2.6–2.7 Rsun, i.e. about 1.35 Rsun each
- b_B = 0.86–0.87, so b_A = 1.45–1.48 (in units of R1 + R2): **no A eclipse is predicted under any of them.** This is consistent with what the data show.

**Luminosity check:** two stars of about 1.35 Rsun and 5700 K give M_G ≈ 3.5, against the observed 3.2–3.4 (parallax 3.626 mas). TIC's single-star R of 1.96 is √2 × 1.39. So at i ≈ 87.5° the masses of about 0.90 + 0.82 Msun are consistent with slightly evolved, old G stars.

## Next eclipses (BTJD)
| Kind | Times | Uncertainty |
|---|---|---|
| B | 3621.5403, 3678.8906, 3736.2408, 3793.5910, 3850.9413 (3564.19008 + 57.35024 n) | ±0.4–2.2 min |
| A (only if Gaia e, ω are right; none is expected geometrically) | 3641.498, 3698.849, 3756.199, 3813.549, 3870.899 | ±0.23 d |

## What would settle it
- A third B eclipse at a predicted time (e.g. 3621.540, which ground photometry could catch: 2.3% deep, 5.5 h) would confirm the period and the phase.
- Ground RVs at a few phases would fix T_peri and ω and test the −1.57 d offset directly. The offset predicts periastron at BTJD 3567.41 + 57.35024 n (Gaia T_peri 414.716 − 1.573, carried forward 55 cycles), 3.22 d after the s83 B eclipse.
