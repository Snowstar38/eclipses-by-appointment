# TIC 285385215

Opus-model subagent for Fable 5.1, 2026-10-19 (saved by Fable 5.1 from the agent's final message; the write tool refused in-agent). Batch row: G 11.11, P 8.20744 d, 61.7 ppt, 2 events, dphi +0.017, diffimg offset 0.98" (peak not on target, s58).

**Verdict: CONFIRMED.** TIC 285385215 is an eclipsing binary on Gaia's SB1 orbit, and the eclipses are on the target. It is TYC 2327-1770-1 (Gaia DR3 132815820610967680, G 11.11), a G8/K0 dwarf at 156 pc. The companion is an M dwarf of about 0.33 Msun in a grazing orbit (b ≈ 0.88).

## The deciding numbers

**Events.** The primary eclipse is measured at 7 epochs, not 2:

| Sector | Epochs measured |
|---|---|
| s18 | E0, E1, E2 |
| s58 | E134, E135 |
| s85 | E221, E222 |

- E133 (2889.59) falls in a data gap.
- E223 (3628.23) sits in a scattered-light mess (background ×20). The dip is visible, but the measurement is rejected.
- The batch count of "2 events" came from keeping only QUALITY==0 at 200-s cadence.
- Of the 7, five are QUALITY==0 in at least one pipeline. The flagged ones carry bit 4096 (s18) or QLP bit 30 (s58/s85).
- Through every event, the background-implied fake depth is below 1.1 ppt, the centroid shift is below 0.002 px, and O−C is ≤ 1 min.

**Secondary eclipse.** Detected at 8 epochs at phase 0.50029 ± 0.00025.
- Depth: 5.6–6.0 ppt in TESS-SPOC PDCSAP, 5.9–7.4 ppt in QLP SAP.
- Strength: Δχ² 207–567 per event.

**Ephemerides.**
- Primary: P = 8.2074497 ± 0.0000015 d, T0 = BTJD 1797.97260 ± 0.00021. χ²/dof 10.8/5; O−C ≤ 1.0 min.
- Secondary: P = 8.2074441 ± 0.0000153 d, T0 = 1802.07870 ± 0.00208. O−C up to 10 min, from scattered light in s85.
- Gaia P = 8.207075 ± 0.001056 d, so Δ/σ = +0.35.

**Match to Gaia's conjunctions.** Monte Carlo over Gaia's errors with corr_vec; corr(ω, t_peri) = +0.99986.

| Eclipse | Gaia conjunction | Offset s18 | Offset s58 | Offset s85 |
|---|---|---|---|---|
| Primary | A (companion in front) | +0.78σ | +0.70σ | +0.68σ |
| Secondary | B | +0.13σ | +0.32σ | +0.38σ |

- The primary offsets are +3.7 to +6.6 h.
- Gaia predicts the secondary 0.515 ± 0.014 in phase after the primary; the measured 0.5003 is 1.1σ from that.

**Eccentricity.**
- From the eclipse timing: e cos ω = +0.0005 ± 0.0004.
- From the duration ratio (secondary/primary = 1.04): e sin ω ≈ +0.02 ± 0.03. This is coarse.
- Gaia: e cos ω = +0.024 ± 0.022, e sin ω = +0.001 ± 0.028.
- The two agree. The orbit is effectively circular.

**Attribution.** Own difference images from the TESS-SPOC target-pixel files in all three sectors:
- In every primary composite, the deficit centre is 0.9–1.7″ (≤ 0.08 px) from the direct-image centre.
- Placing the deficit on the target rather than on the G 17.32 neighbour at 20.3″ improves χ² by:

| Composite | Δχ² | Significance |
|---|---|---|
| Primary s18 | +99.5 | 10σ |
| Primary s58 | +17931 | 134σ |
| Primary s85 | +1249 | 35σ |
| Secondary s58 | +273 | 16.5σ |

- Every Gaia neighbour within 60″ would need a fractional dip above 1100% for the primary and above 200% for the secondary.

**Physics.**

Fit: two spheres with quadratic limb darkening, a circular orbit, and one light ratio shared by both eclipses. It is fitted jointly to the 200-s PDCSAP primary and secondary events.

| Fitted parameter | Value |
|---|---|
| k = R2/R1 | 0.32 (2σ: 0.32–0.42) |
| a/R1 | 19.5 |
| b | 0.88 (1σ: 0.88–0.94) |
| L2/L1, TESS band | 0.0087 |
| Surface-brightness ratio J | 0.085 |

With f(M) = 0.0251 Msun and M1 = 0.86–0.93 Msun, these imply:

| Quantity | Implied | Independent value |
|---|---|---|
| m2 (at i = 87.4°) | 0.33–0.345 Msun | |
| a | 18.1–18.6 Rsun | |
| R1 | 0.93–0.95 Rsun | Gaia/TIC 1.01 ± 0.05 |
| R2 | 0.30 Rsun | about 0.32 expected for a 0.33 Msun M dwarf |
| ρ1 | 1.07 solar | TIC 0.92 ± 0.22 |

- One geometry explains the V-shaped 64 ppt grazing primary, the 6 ppt secondary, the 2.9 h duration and K1 = 30.9 km/s. The eclipsed star has the target's density.
- The expected ellipsoidal amplitude is about 0.05 ppt, so its absence is expected.
- The 17–32 ppt peak-to-peak modulation is starspots. The Lomb–Scargle peak is at 9.4–9.8 d, near-synchronous with the orbit.

**Blind dip census.** In QUALITY==0 data, every dip deeper than 3 ppt in all three sectors is at a primary or secondary ephemeris time. Dips elsewhere appear only in flagged scattered-light stretches.

## Archives

| Source | What was queried | Result |
|---|---|---|
| `cats.py --r 60` (APPOINTMENTS_DATA set) | VSX, ASAS-SN, Prša+2022, IJspeert+2024, Kostov+2025 t2/t3/t4 | none |
| `cats.py` SIMBAD | cone | TYC 2327-1770-1 [SB*] at 0.0″; its only reference is the Gaia DR3 multiplicity paper |
| VizieR | SB9 (30″), WDS (60″), Gaia vari classifier, VSX (120″) | none |
| Gaia DR3 archive | vari_summary, vari_eclipsing_binary | no rows |
| ExoFOP | TOI, CTOI, files, spectra, imaging | none; contamination ratio 0.0063 |
| Web search | TYC and TIC names | nothing |

- Gaia NSS row: P 8.20707, e 0.031 ± 0.027, ω 10.5 ± 53°, K1 30.92 ± 0.93 km/s, significance 33. RUWE 1.01, ipd_frac_multi_peak 0.
- **The eclipses are new.**

## Neighbours (Gaia DR3, 60″; dip needed = 63.7 ppt × 10^(0.4ΔG))

| Gaia DR3 | sep | G | dip needed | note |
|---|---|---|---|---|
| 132815820610967680 | 0 | 11.11 | 6.4% | target |
| 132815820611210624 | 20.3″ | 17.32 | ~1960% | plx 6.83 vs 6.47: a wide M-dwarf companion (~3100 au projected); not variable in Gaia |
| 132815816315381760 | 22.0″ | 20.05 | >20000% | |
| 132815820610967424 | 35.3″ | 18.83 | ~7800% | |
| 132815781955415808 | 50.6″ | 19.63 | >16000% | |

## Next predicted eclipses (BTJD)

| Kind | Times | Uncertainty | Ephemeris |
|---|---|---|---|
| Primary | **4334.0746**, 4342.2820, 4350.4895, 4358.6969 | ±0.7 min | P 8.2074497 |
| Secondary | **4338.1789**, 4346.3864, 4354.5938, 4362.8013 | ±7.5 min | secondary's own |

The primary ephemeris shifted by +0.50029 phase gives the secondary at 4338.1807 and so on.

## What would settle it further

It is already settled as an eclipsing binary on the target. These would refine the parameters:
- A few RVs to tighten K1 and e.
- A spectroscopic Teff and log g for the primary.
- A ground-based multi-band light curve of one primary eclipse (4334.07 or 4342.28) to pin down the grazing chord and the M dwarf's radius.

## Row fixes for the paper table

| Field | Value | Note |
|---|---|---|
| P | 8.2074497 ± 0.0000015 d | batch: 8.20744 |
| T0 (primary) | BTJD 1797.97260 ± 0.00021 | |
| Primary depth | **63.7 ppt** | median of TESS-SPOC PDCSAP, crowding-corrected (CROWDSAP 0.992); range 62.0–65.1. QLP SAP: 64–66.6. The batch box depth (61.7) and search depth (51.3) are box-shape underestimates. |
| Secondary depth | 5.85 ppt (PDCSAP, 5.6–6.0) | at phase 0.50029 ± 0.00025 |
| Duration | primary T14 2.94 h, T12/T14 0.40 (near-V, grazing); secondary T14 3.06 h | the batch's "1.9 h" was the box width |
| Events | 7 primaries measured (5 QUALITY==0 in at least one pipeline) in s18, s58, s85; 1 more visible but corrupted (E223); 1 in a gap (E133); 8 secondaries measured | |
| Conjunction offset | primary at Gaia A, +0.019 to +0.034 phase (≤ +0.78σ); secondary at Gaia B | |

**Difference-image flag: not an attribution problem.**
- The batch receipt's 0.98″ offset (0.05″ from the light centroid) is sub-pixel scatter in the WCS, not a sign of a different source.
- Our own TESS-SPOC difference images put the deficit within 0.9–1.7″ of the target's direct-image centre.
- The target beats the nearest neighbour by 10σ, 134σ and 35σ in s18, s58 and s85.
- Clear the flag. Status: candidate → **confirmed**, with the secondary eclipse detected.
