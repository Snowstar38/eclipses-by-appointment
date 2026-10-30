# TIC 123378551

Opus-model subagent for Fable 5.1, 2026-10-19 (saved by Fable 5.1 from the agent's final message; the write tool refused in-agent; the agent's own byline below says "Opus 5.5 subagent", meaning an Opus-model subagent, launched from Fable 5.1's session). Batch row: G 11.13, P 11.01057 d, 20.8 ppt, 7 events, dphi +0.027, diffimg offset 3.42" (peak not on target, s34; 54 neighbours in 60", 2 possible).

**TIC 123378551: per-object attribution vet (pervet-deep).** Opus 5.5 subagent, 2026-10-19.

The star is TYC 7652-366-1 = Gaia DR3 5535420719437355648: G 11.13, Teff about 6400–6500 K, R about 1.35 Rsun, parallax 3.49 mas, RUWE 1.95.

Gaia DR3 SB1 orbit:

| P (d) | e | ω (deg) | K1 (km/s) | corr(ω, Tp) |
|---|---|---|---|---|
| 11.00834 ± 0.00126 | 0.436 ± 0.017 | 181.8 ± 3.0 | 23.85 ± 0.60 | +0.89 |

## Verdict: CONFIRMED

The eclipse is on the target, at Gaia's conjunction A (the companion passes in front of the Gaia primary). The difference-image flag is a crowding artefact.

What decides it:
- **Difference images, six sectors.** I made my own for s7, 8, 34, 35, 62 and 88 (two events each, noise from 150 null windows, Gaussian-PRF scene fitted to every Gaia DR3 source within 90″).
  - In every sector the fitted deficit sits 1.1–3.3″ (0.05–0.16 px) from the target.
  - The only neighbour bright enough to make the dip is the G 12.41 star at 18.2″. As the host it is rejected by Δχ² = +1908, +930, +1245, +2142, +2621, +1615 (s7, 8, 34, 35, 62, 88). Scaled by the best fit's reduced χ², that is 18.3, 17.6, 19.1, 20.9, 27.4 and 18.8σ.
  - A model-free check agrees: the fractional loss on the target's pixel (14.7–17.9 ppt) is larger than on that neighbour's pixel (5.4–13.6 ppt) in all six sectors.
- **Timing.** The TESS ephemeris carried back to Gaia's epoch lands 0.065 d (1.0σ) from Gaia's conjunction A. P_TESS − P_Gaia = +0.0023 d (1.8σ).
- **Second pipelines.** TESS-SPOC SAP and PDCSAP, TGLC PSF-fit, TARS (including s61, which QLP lacks) and CDIPS all show every covered event, within 3 minutes of the QLP times.
- **Physics.** The mass function f(m) = 0.0113 Msun gives m2 ≈ 0.29–0.34 Msun, an M dwarf. A 2.6-hour, 22-ppt, V-shaped grazing eclipse at i ≈ 86° fits within the uncertainty in R1 and limb darkening (the geometry predicts 13–22 ppt).

## 1. Archives and web
- `cats.py 123378551 --r 60`: no VSX, no ASAS-SN. SIMBAD has only TYC 7652-366-1 [SB*]. No hit in Prša, IJspeert or Kostov.
- Gaia DR3: no vari_summary or vari_eclipsing_binary row for the target, and no eclipsing-binary row for any neighbour within 90″. One classifier row (5535420268461954816, ELL, score 0.08) lies outside 60″.
- SB9, WDS and J/AJ/160/111: none. ExoFOP: no TOI or CTOI, no imaging, spectroscopy or companions.
- A web search on all three identifiers found nothing that mentions the star.
- **Not previously catalogued as an eclipser.**
- The G 12.41 neighbour (Gaia DR3 5535420715138207360, 18.2″) has parallax 3.551 mas against the target's 3.492 mas. It is probably a physical wide companion (about 5000 au), so it had to be excluded with pixels, not with distance. It is not a catalogued variable.

## 2. Every eclipse
Fits use raw QLP SAP_FLUX with a trapezoid on a local quadratic baseline, integrated over the exposure (`ecl.py`). QLP has 12 primaries: 10 on QUALITY==0 data and 2 that need flagged cadences. TARS s61 adds 2 more (BTJD 2972.096 and 2983.107).

| sector | cycle | tc (BTJD) | depth (ppt) | T14 (h) | T23 (h) | note |
|---|---|---|---|---|---|---|
| 7 | −68 | 1496.6757 ± 0.0008 | 23.4 ± 0.9 | 2.50 | 0.62 | |
| 7 | −67 | 1507.6843 ± 0.0010 | 20.7 ± 0.9 | 2.40 | 0.72 | |
| 8 | −66 | 1518.6984 ± 0.0010 | 21.8 ± 0.8 | 2.59 | 0.65 | 3 flagged cadences in the event |
| 8 | −64 | 1540.7190 ± 0.0010 | 21.8 ± 0.8 | 2.59 | 0.65 | |
| 34 | −1 | 2234.3834 ± 0.0010 | 22.4 ± 0.9 | 2.69 | 0.40 | |
| 34 | 0 | 2245.3985 ± 0.0008 | 24.1 ± 0.8 | 2.50 | 0.50 | |
| 35 | 1 | 2256.4051 ± 0.0008 | 25.0 ± 0.6 | 2.69 | 0.40 | needs flagged cadences before the event |
| 35 | 3 | 2278.4262 ± 0.0008 | 23.4 ± 0.9 | 2.50 | 0.62 | 5 flagged cadences in the event |
| 62 | 68 | 2994.1173 ± 0.0003 | 21.8 ± 0.5 | 2.50 | 0.62 | |
| 62 | 69 | 3005.1273 ± 0.0003 | 24.5 ± 0.5 | 2.69 | 0.40 | |
| 88 | 132 | 3698.7972 ± 0.0003 | 21.7 ± 0.4 | 2.50 | 0.75 | |
| 88 | 133 | 3709.8083 ± 0.0005 | 24.1 ± 0.5 | 2.69 | 0.27 | |

- One cycle is lost: s35 cycle 2 (2267.42) falls in the data gap.
- **Background:** the unit-free background "fake depth" is at most 0.35 ppt for every event.
- **QLP centroids:** SAP_X and SAP_Y shift by +0.0015 to +0.004 px and −0.0007 to +0.002 px in eclipse. That is the size and sign expected when the target dims while the light centroid sits off it toward the neighbours.
- **Blind census** (`census.py`, 2.6-hour box, every sector): the primaries are the only dips deeper than 5 ppt.
- **Second-pipeline depths:**
  - TESS-SPOC PDCSAP (crowding-corrected; CROWDSAP 0.71–0.75): 20.8–23.7 ppt
  - TGLC PSF-fit: 19.5–23.0 ppt
  - TESS-SPOC SAP (not corrected for crowding): 14.7–17.6 ppt
- **The ~3.25-day, ~2% peak-to-peak quasi-sinusoid in every QLP and SPOC sector is not the target's** (`varimg.py`). Its in-phase fractional amplitude is 0.3–5.5 ppt on the target pixel and 20–60 ppt on pixels 2–3 px toward +column, from a source roughly 60″ or more away. It is contamination in the apertures.

## 3. Ephemeris and orbit
- **Primary, 12 events:** P = 11.010611 ± 0.000006 d, T0 = 2972.09636 ± 0.00034 BTJD.
  - χ²/dof = 5.6, with O−C within ±4 minutes and no trend. The errors are already scaled by √χ²_red; the contaminating 3.25-day signal is what inflates the scatter.
  - Against Gaia: P differs by +0.00227 ± 0.00126 d (1.8σ).
- **Conjunction at Gaia's epoch** (Monte Carlo through the full NSS covariance):
  - Gaia conjunction A = BTJD 384.538 ± 0.065. The TESS primary projected back = 384.603. The difference is +0.006 in phase (1.0σ).
  - At TESS epochs Gaia's window widens to ±0.2–0.45 d through the error on Gaia's P. The batch row's dphi of +0.027 sits inside that.
- **Secondary** (`sscan.py`, fixed shape, with look-elsewhere control):
  - At Gaia's predicted phase 0.2322 ± 0.0097: 0.27 ± 0.18 ppt, i.e. nothing.
  - **Tentative secondary at phase 0.2070 ± 0.001: 0.99 ± 0.17 ppt.**
    - z = 5.96, against a z spread of 1.24 at control phases, so about 4.8σ effective. The largest control peak away from the primary's wings is z = 3.98.
    - It holds for box durations from 2.0 to 3.5 h. Per-window depths scatter about 1.8× the noise.
  - If it is real, e cos ω = −0.479 ± 0.002 against Gaia's −0.435 ± 0.017 (2.6σ).
  - e sin ω can't be measured because the secondary is too weak to give a duration. Gaia gives −0.013, which predicts near-equal durations (2.7 h against 2.6 h).

## 4. Independence and attribution
- **Light curves:** see §2. Every pipeline shows every covered event.
- **Difference images:** see the Verdict for the per-sector Δχ² and σ. The fitted deficit's sky offsets from the target (east, north) in arcsec:

  | s34 | s7 | s8 | s35 | s62 | s88 |
  |---|---|---|---|---|---|
  | (+3.3, +0.3) | (+1.9, +1.0) | (+1.6, +0.3) | (+1.1, 0.0) | (+1.9, +0.7) | (+2.1, +0.9) |

  Per-event positions agree to within about 1.5″.
- There is a small, consistent eastward bias of about 2″ (0.1 px). It is best read as a systematic of the Gaussian PRF model, whose scene residual is 0.16–0.24. No Gaia source within 6″ could host the dip: the nearest, G 19.37 at 6.1″, would need a 4100% eclipse.
- **Neighbour dilution table** (depth needed = 22 ppt × 10^(0.4 ΔG)):

  | Gaia DR3 | G | separation | needs | result |
  |---|---|---|---|---|
  | 5535420715138207360 | 12.41 | 18.2″ | 7.1% | excluded at 17.6–27.4σ per sector |
  | 5535420341480232448 | 13.03 | 35.3″ | 12.7% | excluded at 19.7–31.9σ |

  Every other source within 60″ is G ≥ 17.6 and would need more than 100%. A host of the 22-ppt dip would have to be brighter than G ≈ 15.3.
- **Why the batch flagged it:**
  - The 7.25″ in the receipt is the deficit's distance from the *light* centroid, which is dragged 0.1–0.3 px toward the neighbours.
  - The peak-deficit pixel (8,8) is next to the target pixel (7,8): sub-pixel quantization.
  - psf_frac_resid = 0.68 comes from fitting D = a·I_out in a scene where 30–45% of I_out is other stars.
  - **This is a crowding artefact, like the five shallow cases.**

## 5. Physics
- **Companion:** f(m) = 0.01129 Msun gives m2 = 0.285, 0.315 or 0.343 Msun for M1 = 1.15, 1.35 or 1.55. That is an early-to-mid M dwarf, R2 ≈ 0.31 Rsun, T2 ≈ 3400 K.
- **Orbit size:** a = 24.7 Rsun. Separation is 20.3 Rsun at conjunction A and 19.7 Rsun at conjunction B.
- **Primary eclipse is grazing:**
  - A central chord at conjunction A would last 5.2 h. The observed 2.6 h means b ≈ 1.05 R1 and i ≈ 86°, which fits the V/narrow-U shape.
  - For k = 0.2–0.35 at that duration, the grazing depth is 13–15 ppt with R1 = 1.35 and 20–22 ppt with R1 = 1.2 (linear limb darkening u = 0.3–0.45).
  - The observed ~22 ppt (dilution-corrected, from PDCSAP and TGLC) is in that range. Grazing depth is steep in R1 and b, so this is consistency, not a measurement.
- **Which star is in front:** at conjunction A the companion is in front, so the observed eclipse is the M dwarf transiting the F star.
- **Expected secondary:** occultation of the M dwarf predicted at 1.4–2.0 ppt, with T14 about 2.7 h (b_B ≈ 1.03 R1). The tentative 1.0 ± 0.17 ppt is the right size.
- **Ellipsoidal variation:** about 60–100 ppm, undetectable under the 20-ppt contaminating signal.
- **Not a heartbeat:** conjunction A is at true anomaly −92°, well away from periastron, and the predicted tidal amplitude is about 0.1 ppt.
- **RUWE:** 1.95 is larger than this orbit explains (a1 sin i ≈ 0.08 mas), so another close companion is possible. Nothing here needs it.

## Next eclipses (BTJD)
- **Primary** (±0.0008 d formal; allow ±0.003 d for the O−C scatter): 4337.4121, 4348.4227, 4359.4333, 4370.4440, 4381.4546, 4392.4652, 4403.4758.
- **Tentative secondary** (phase 0.207, ±0.011 d): 4339.691, 4350.702, 4361.713, 4372.723, 4383.734, 4394.744, 4405.755.
- **Secondary in Gaia's window** (phase 0.2322 ± 0.0097, about ±0.11 d): 4339.97, 4350.98, 4361.99, 4373.00, 4384.01, 4395.02, 4406.03.

## What would settle it further
- Two or three more 200-second sectors, or a ground-based light curve at 1-ppt precision at the tentative secondary times. That would confirm the ~1-ppt secondary and pin e cos ω, which now sits 2.6σ from Gaia.
- One or two RVs near conjunction A or B; the primary should be at γ − 10.4 km/s at both.
- High-resolution imaging, to explain the RUWE of 1.95.

## Row fixes for the paper table
- **P:** 11.010611 ± 0.000006 d (row: 11.01057).
- **T0:** 2972.09636 ± 0.00034 BTJD; the primary is at Gaia's conjunction A (companion in front). The same ephemeris at cycle 0 gives 2245.3985.
- **Depth:**
  - QLP SAP trapezoid: 20.7–25.0 ppt, mean about 22.9. The row's 20.8 is the box mean.
  - Dilution-corrected: about 22 ± 1.5 ppt (PDCSAP 20.8–23.7, TGLC PSF 19.5–23.0).
  - Secondary: tentative 1.0 ± 0.17 ppt at phase 0.207; nothing at Gaia's 0.232 (0.27 ± 0.18 ppt).
- **Duration:** T14 = 2.6 ± 0.1 h, T23 ≈ 0.3–0.75 h (grazing, V/U shape).
- **Event count:**
  - 12 primaries in QLP (10 on QUALITY==0, 2 needing flagged cadences) across s7, 8, 34, 35, 62 and 88.
  - Plus 2 in TARS s61, for 14 distinct primaries.
  - The row's 7 is an undercount.
- **dphi:** +0.006 ± 0.006 in phase at Gaia's epoch (1.0σ). The row's +0.027 is the TESS-epoch value, inside Gaia's widened window.
- **Difference-image flag: crowding artefact, ON TARGET.**
  - Own difference images in 6 sectors put the deficit 1.1–3.3″ from the target.
  - The G 12.41 neighbour at 18.2″ (Gaia DR3 5535420715138207360, probably physical, needs 7.1%) is rejected at Δχ² +930 to +2621 (17.6–27.4σ) per sector.
  - No neighbour is a catalogued eclipser.
  - The status can go from candidate to confirmed.
