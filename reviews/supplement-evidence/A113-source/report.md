# TIC 352914772 (TYC 4251-1144-1) -- adversarial check, 2026-10-17

**Verdict: CONFIRMED.** A detached, eccentric eclipsing binary at **P = 23.6371 d**, with both eclipse kinds on the target. Gaia's SB2C period of 37.665 d is wrong.

## Archives
| Source | Query | Result |
|---|---|---|
| `cats.py --r 60` | VSX, ASAS-SN, EB catalogues, SIMBAD | VSX TAP returned 503, so I redid it via VizieR asu-tsv: 0 rows within 60". ASAS-SN II/366: none. Prša+2022, IJspeert+2024, Kostov t2/t3/t4: none within 5". SIMBAD: TYC 4251-1144-1 [SB*]. |
| VizieR | SB9, WDS (30") | none |
| Gaia DR3 | vari_summary, vari_eclipsing_binary | no rows; phot_variable_flag NOT_AVAILABLE |
| ExoFOP | TOI / CTOI | none; TIC contamination ratio 0.094 |
| Web | TYC and TIC names | nothing |

It is not previously known as an eclipser. Its MAST light curves are QLP, TESS-SPOC FFI and TASOC (s15), over 13 sectors (s15–17, 24, 56–58, 76–78, 83–85).

Gaia NSS SB2C:
- P 37.6646 ± 0.0154 d, circular
- K1 38.42 ± 0.69 km/s, K2 42.37 ± 3.22 km/s
- 20 RV transits; goodness_of_fit 25.6 (a poor fit); RUWE 1.35

## Eclipses
I fitted raw QLP SAP_FLUX (q==0, no trimming) with a trapezoid times a quadratic baseline (`ecl.py`, `ecl.json`, `ecl_P.png`, `ecl_S.png`).

**Primaries.** 13 fitted, plus s15 E0 at 1722.59, which is entirely flagged but plainly present in the flagged cadences (`fold.png`).
- Depth 14.5–15.4%; T14 8.38–8.41 h; T12 3.45 h; flat bottom 1.45–1.50 h.
- Mid-time errors are 0.1–0.5 min.
- Within s57 there are two primaries 23.637 d apart with equal depths (15.14% and 15.19%). This alone rules out a 37.665-d period.

**Secondaries.** 13 fitted, plus s58 E49 at 2896.92, which is flagged but present.
- Depth 1.84–2.20%; T14 8.8–9.4 h.

**Other checks.**
- Background and centroids show no event-like excursion beyond the ≤10-mpx shifts expected from a 15% dimming of the target with neighbours in the aperture.
- Blind census of all 13 sectors (1.5-d running median, 1-h bins, threshold 0.3%; `census.py`): no other dips.

## Ephemeris (`ephem.py`, `ephem.json`, `oc.png`)
| | T0 (BTJD) | P (d) | χ² / dof |
|---|---|---|---|
| P-kind | 1722.59629 (143) | 23.637271 (22) | 1999 / 11 |
| S-kind | 1738.69628 (62) | 23.637135 (11) | 35.7 / 11 |

- Mean secondary phase: 0.68113.

**Gaia's period.** Gaia's 37.6646 d is **14.03 d = 913 σ** away. 1/23.6373 − 1/37.6646 = 1/63.5 d, which matches Gaia's 63-d scan-precession alias. No n/m ratio rescues it: 3/2 × P = 35.456 d is still 144 σ off. Folding at 37.6646 d, or at ±3 σ from it, scatters the eclipses over about 10 phases (`fold.png`).

**The O-C is curved.**
- Primaries: −6.8 min (2019) → +2.0 (2022) → 0 (2024) → −1.6 (2025). A quadratic fit gives χ² 10.6.
- The secondary-minus-primary separation within a cycle falls by 14 min over 6 years: 16.1040 → 16.0930 → 16.0896 → 16.090 d.
- TESS-SPOC PDCSAP s16/17/24 reproduce the 2019 times to ≤1.1 min, so this is in the data, not a QLP artefact.
- GR plus tidal apsidal motion would give ~0.01 min over this baseline. If the signal is real it points to a third body. This is a side finding and is not needed for the verdict.

## Independence
**Second pipeline.** TESS-SPOC FFI (s16, 17, 24, 57, 84):
- Mid-times agree with QLP to 0.0–0.1 min (200-s primaries) and ≤1.5 min (secondaries).
- PDCSAP depths are 14.4–15.4% and 1.9–2.1%, with the same durations.

**Difference images.** TESScut s57, 15×15 (`diff_s57P`, `diff_s57P2`, `diff_s57S`), covering both s57 primaries and the s57 secondary:
- The deficit centroid lies 2.2–2.4" from the out-of-eclipse light centroid, i.e. 0.1–0.2 px from the target's Gaia position.
- The 3×3 box on the target holds 0.80–0.81 of the deficit, matching its 0.79–0.80 share of the light.
- At the pixel of the G 13.11 neighbour (31") the fractional depth is 6% against 14% on the target (0.8% against 1.8% for the secondary).

**Neighbour dilution** (Gaia, G < 16 within 90"):

| Neighbour | Separation | Primary would need | Secondary would need | Status |
|---|---|---|---|---|
| G 15.82 | 9.4" | 143× its depth | 315% | impossible |
| G 13.11 | 31.4" | 180% | 26% | primary impossible; secondary excluded by the difference image |

## Physics
**My own EB model** (`ebfit.py`): two limb-darkened spheres on a Kepler orbit, fitted to the 2022 200-s eclipses of both kinds. Residual rms 0.66 ppt, with no structure (`ebfit.png`).

| Quantity | Value |
|---|---|
| e cos ω | 0.2801 ± 0.0006 |
| e sin ω | 0.226 ± 0.009 |
| e | 0.360 |
| i | 86.73° |
| R1/a, R2/a | 0.0512, 0.0258 (R2/R1 = 0.50) |
| Surface-brightness ratio J | 0.63 |
| L2/L1 (TESS band) | 0.16 |
| Periastron | BTJD 3611.986 + n × 23.63714 |

- **Primary eclipse:** the smaller, cooler star transits the larger star near periastron (r = 0.71a, b = 0.79 R1).
- **Secondary eclipse:** a grazing occultation of the small star near apastron (r = 1.12a).
- For a total mass of 2.2–3.2 Msun: a = 45–51 Rsun, R1 = 2.3–2.6 Rsun (an evolved primary; TIC gives R 3.5 and Gaia logg 3.54), R2 = 1.2–1.3 Rsun.
- **Gaia's circular solution is excluded:** e must be at least e cos ω = 0.280.

**Gaia's K's at the true orbit (P 23.637 d, e 0.36):**
- M1 sin³i = 0.59 [0.51, 0.69] Msun, M2 sin³i = 0.54 [0.49, 0.59] Msun, so M_total ≈ 1.13 Msun at i = 86.7°.
- That is impossible for a G 10.43 star at 509 pc (M_G ≈ +1.5 to +1.9).
- Plausible masses (1.5 + 1.2–1.35 Msun) imply K1, K2 of about 52 and 58 km/s at 23.64 d.
- So Gaia's K's are about 70–75% of the true values, which is what an RV orbit fitted at an alias period produces. The published SB2C orbit does not fit a 23.64-d eccentric orbit as it stands. That counts against the Gaia solution, not against the eclipses.
- The mass ratio K1/K2 = 0.91 ± 0.07 and the light ratio of 0.16 (subgiant plus MS companion) are mutually plausible.

**The orbit should be:** P 23.63714 d, e 0.36, periastron BTJD 3611.986, i 86.7°.

## Next eclipses (BTJD)
These come from a linear fit to E ≥ 70 only, because the O-C is curved. Allow ±10 min for the ETV.

| Kind | Ephemeris | Next times |
|---|---|---|
| P-kind | 1722.60576 + 23.637138 E | 3660.8511, 3684.4882, 3708.1254, 3731.7625, 3755.3996, 3779.0368 |
| S-kind | 1738.69540 + 23.637137 E | 3653.3035, 3676.9406, 3700.5778, 3724.2149, 3747.8520, 3771.4892 |

## What would settle it further
- Ground-based RVs over one 23.6-d cycle would replace the alias SB2C solution and give true masses: with i known, K1 and K2 of roughly 52/58 km/s should come out.
- Continued eclipse timing would test the curved O-C and the shrinking primary–secondary separation (third body?).
