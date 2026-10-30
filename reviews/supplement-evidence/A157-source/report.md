# TIC 86036265

Opus-model subagent for Fable 5.1, 2026-10-19 (saved by Fable 5.1 from the agent's final message; the write tool refused in-agent). Batch row: G 11.20, P 11.99731 d, 102.3 ppt, 14 events, dphi +0.022, diffimg offset 2.85" (peak not on target, s46).

**Verdict: CONFIRMED.** TIC 86036265 is a detached eclipsing binary on Gaia's SB1 orbit, and the eclipses are on the target. It is BD+20 2296 (EPIC 251330444, Gaia DR3 635898431051113216, G 11.18), a spotted K giant at about 355 pc (Teff 4930 K, R 2.67 Rsun). The companion is a K dwarf of about 0.8 Msun and 0.8 Rsun, with roughly the giant's surface brightness.

The two eclipse kinds look different:
- **Primary (phase 0):** the dwarf passes in front of the giant. It is round-bottomed, about 100 ppt deep, and shows starspot-crossing bumps.
- **Secondary (phase 0.5):** the giant fully hides the dwarf. It is flat-bottomed and 86 ppt deep.

## The deciding numbers

**Events.** In TESS (QLP, s44–46 and s72):
- 8 primaries: E0–E5 and E63–E64.
- 7 usable secondaries, plus 2 partial ones at sector edges (2525.95 and 2537.95).
- Background-implied fake depth is below 0.7 ppt and centroid shifts are below 0.004 px (QUALITY==0).

K2 C16 (BTJD 1095–1175; EVEREST, K2SFF and the Kepler pipeline light curve) adds 6 primaries and 7 secondaries. TESS-SPOC s1751 (BTJD 4055.8–4063.0, not in the QLP set) adds 1 secondary at 4061.597, 0.7 min from prediction. SPOC's own transit search had already flagged it: TCE_1 at P/2 = 5.99865 d, 99.4 ppt, SNR 542.

**Ephemerides (TESS + K2).**
- Secondary, the clean flat-bottomed eclipse: P = 11.9972226 ± 0.0000022 d, T0(sec) = BTJD 2513.95553 ± 0.00020. 15 events, χ²/dof 4.3/13, O−C rms 0.5 min.
- Primary: P = 11.9972166 ± 0.0000091 d, T0 = 2507.95631 ± 0.00069. 14 events, O−C rms 3.3 min; spot crossings distort the transit mid-times.
- The two periods differ by +0.5 ± 0.8 s.
- Gaia P = 11.995577 ± 0.001562 d, so Δ = +0.00165 d = 1.05σ.

**Match to Gaia's conjunctions.** Monte Carlo with corr_vec; corr(ω, t_peri) = 0.99999.

| Eclipse | Gaia conjunction | K2 | s44–46 | s72 |
|---|---|---|---|---|
| Primary (transit, deeper) | A (companion in front) | +1.08σ | +1.33σ | +1.36σ |
| Secondary (occultation) | B | +1.11σ | +1.37σ | +1.39σ |

The offset grows over time, from +0.009 to +0.040 in phase. That drift is Gaia's period being 1σ short, not a mismatch in which conjunction is which.

**Eccentricity.**
- From the eclipse timing: secondary phase 0.50005 ± 0.00006, so e cos ω = +0.00008 ± 0.00009.
- Both eclipses have T14 = 10.7 h, so e sin ω ≈ 0.
- Gaia: e = 0.005 ± 0.014, e cos ω = +0.0001 ± 0.0117, Gaia-predicted phase separation 0.5001 ± 0.0075.
- The orbit is circular.

**Attribution.** Own difference images from the SPOC 2-min target-pixel files (s44, s45, s46) and TESS-SPOC (s72), primary and secondary separately:
- In 7 of 8 composites, the deficit centre is 1.1–5.2″ (≤ 0.25 px) from the direct-image centre.
- The single-event s44 secondary composite is 9.7″ (0.46 px) off; it sits on a sector-start ramp.
- These offsets come from fitting a Gaussian PSF at deficit S/N 38–148. The formal errors are tiny, so the offsets are model systematics, not evidence of another source.
- Placing the deficit on the target rather than on any Gaia neighbour improves χ² by at least 930 (30σ) in every composite. Against the G 14.80 star at 69.9″ the improvement is 6145–145967.
- Every star within 30″ is G 20.3–21.0 and would need a dip above 25000%. The G 14.80 star at 69.9″ would need 160–206%.
- I also tried a K2 pixel difference image. It came out unusable (deficit 1–2 ppt of the direct image), most likely because Kp 11.2 is near saturation and I did not correct the roll motion. It is not counted either way.

**Dilution-corrected depths.**

| Light curve | Primary (ppt) | Secondary (ppt) |
|---|---|---|
| TESS-SPOC / SPOC PDCSAP s44–46 (CROWDSAP 0.995–0.998) | 97.2–101.1 | 83.9–87.5 |
| TESS-SPOC s72 | 95.0, 95.9 | 85.7, 86.3 |
| TESS-SPOC s1751 | – | 88.7 |
| K2 EVEREST (Kepler band) | 89.6–108.7 | 85.0–87.5 |
| QLP SAP | 102.7–109.9 | 91.0–95.2 |

QLP runs about 7% deeper than both SPOC and K2.

**Physics.**

Fit: two spheres with limb darkening, fitted jointly to 15 TESS-SPOC PDCSAP events. Starspot crossings make the formal errors meaningless; the values below are good to the grid step (k 0.01, a/R1 0.25).

| Fitted parameter | Value |
|---|---|
| k = R2/R1 | 0.30 |
| a/R1 | 10.5 |
| b | ≈ 0.02 (central) |
| L2/L1, TESS band | 0.095 |
| Surface-brightness ratio J | 1.06 |

With f(M) = 0.1178 Msun and M1 = 1.0–1.4 Msun, these imply:

| Quantity | Implied | Independent value |
|---|---|---|
| m2 (at i = 89.9°) | 0.70–0.84 Msun | |
| a | 26.3–28.9 Rsun | |
| R1 | 2.51–2.75 Rsun | TIC 2.67 |
| R2 | 0.75–0.82 Rsun | |

- J ≈ 1 means the companion's Teff is about the giant's, 4900–5000 K. That is a K1–K2 dwarf of about 0.8 Msun, which matches m2 from Gaia's mass function.
- The occultation depth is the same in the Kepler and TESS bands (86 ppt), as J ≈ 1 predicts.
- K1 = 45.6 km/s fits a 0.7–0.8 Msun companion; nothing about it is suspicious.
- The ellipsoidal signal is lost under 60–77 ppt peak-to-peak starspot modulation. Lomb–Scargle peaks at 14.5 d (s44–46), 14.2 d (s72) and 13.8 d (K2): sub-synchronous rotation of an RS CVn-like giant.

**Blind dip census.** In QUALITY==0 data, every dip deeper than 4 ppt is at an ephemeris eclipse. Dips elsewhere appear only in flagged scattered-light stretches of s72.

## Archives

| Source | What was queried | Result |
|---|---|---|
| `cats.py --r 60` | VSX | TAOS 061.00059 at 0″, type VAR, P = 13.93424 d |
| `cats.py --r 60` | ASAS-SN | variable at 1.0″, type ROT:, P = 415 d |
| `cats.py --r 60` | Prša, IJspeert, Kostov t2/t3/t4 | none |
| `cats.py` SIMBAD | cone | BD+20 2296 [SB*] |
| SIMBAD bibliography | 4 references | TAOS variability (2014), JSDC, mid-IR diameters, Gaia DR3 multiplicity; no eclipse paper |
| VizieR | SB9, WDS, Gaia vari classifier | none |
| Gaia DR3 archive | vari_summary, vari_eclipsing_binary | no rows |
| ExoFOP | TOI, CTOI | none; lists EPIC 251330444 with uncalibrated K2 photometry |
| Web search | BD+20 2296, EPIC 251330444, TIC 86036265 | nothing |

- Gaia NSS row: P 11.99558, e 0.005, K1 45.59 ± 0.65 km/s, significance 70. RUWE 1.17. No GSP-Phot or FLAME parameters.
- The TAOS 13.93 d period is the giant's rotation (we measure 13.8–14.5 d). That changes the variability type; it is not a prior eclipse detection.
- **No catalogue lists it as an eclipser.**

## Neighbours (Gaia DR3; dip needed = 86 ppt × 10^(0.4ΔG), using the occultation depth)

| Gaia DR3 | sep | G | dip needed | note |
|---|---|---|---|---|
| 635898431051113216 | 0 | 11.18 | 8.6% | target |
| 635898426755882880 | 20.3″ | 20.97 | ~72000% | |
| 635898495475358720 | 26.2″ | 20.28 | ~38000% | |
| 635898465410850944 | 69.9″ | 14.80 | ~240% | plx 8.46; Gaia variable, VSX ROT; cannot host the dip, rejected at ≥ 78σ in the difference images |

## Next predicted eclipses (BTJD)

| Kind | Times | Uncertainty |
|---|---|---|
| Secondary (occultation) | **4337.5334**, 4349.5306, 4361.5278, 4373.5250 | ±0.6 min |
| Primary (transit) | **4343.5304**, 4355.5277, 4367.5249, 4379.5221 | ±2.2 min |

The secondary ephemeris shifted back by 0.50005 phase puts the primary at 4343.532, which is consistent.

## What would settle it further

It is settled as an eclipsing binary on the target. These would yield masses and radii:
- Double-lined spectroscopy to measure K2 for the dwarf, which contributes about 9% of the light; Gaia saw it as single-lined.
- A spectroscopic Teff and log g for the giant.
- A multi-band occultation light curve to pin down the dwarf's Teff.
- Modelling the spot crossings during transit. This also gives a chance to measure the spin–orbit alignment.

## Row fixes for the paper table

| Field | Value | Note |
|---|---|---|
| P | 11.9972226 ± 0.0000022 d | from secondaries, TESS + K2 + s1751; the batch's 11.99731 is 7.6 s too long |
| T0 (primary) | BTJD 2507.95631 ± 0.00069 | the secondary ephemeris gives 2507.95692 for the same epoch |
| Primary depth | **~100 ppt** (PDCSAP s44–46: 97–101; s72: 95–96) | starspot-modulated. The batch's 102.3 and QLP's 103–110 are about 7% too deep. |
| Secondary depth | **86 ppt** (PDCSAP 84–89; K2 85–87.5) | flat-bottomed total occultation, so L2/(L1+L2) = 0.086 |
| Duration | T14 = 10.7 h for both; T12/T14 0.25 (primary), 0.20 (secondary) | |
| Events | 14 primaries (8 TESS, 6 K2); 15 secondaries (7 TESS, 7 K2, 1 s1751) plus 2 partial TESS | |
| Conjunction offset | primary at Gaia A, +0.009 (K2) to +0.040 (s72) phase, +1.1 to +1.4σ; secondary at Gaia B | the drift is Gaia's 1σ-short period |

**Difference-image flag: not an attribution problem.**
- The batch receipt (s46: 2.85″ from target, 1.6″ from the light centroid) is a sub-pixel offset from a crude PSF on a very bright eclipse.
- Our own difference images in four sectors put the deficit within ≤ 0.25 px of the target's direct image in 7 of 8 composites, and the target beats every neighbour by ≥ 30σ.
- No neighbour can physically host the dip.
- Clear the flag. Status: candidate → **confirmed**.

Web sources consulted (no relevant hits for either star):
- [Seven new triply eclipsing triple star systems](https://arxiv.org/pdf/2403.12041)
- [Revising the properties of low mass eclipsing binary stars using TESS light curves](https://arxiv.org/pdf/2302.06985)
- [Discovery and characterisation of long-period eclipsing binary stars from K2 campaigns 1–3](https://arxiv.org/pdf/1803.10522)
