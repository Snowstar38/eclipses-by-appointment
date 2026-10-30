# TIC 437230270

Opus-model subagent for Fable 5.1, 2026-10-19 (saved by Fable 5.1 from the agent's final message; the write tool refused in-agent; the agent's own byline below says "Opus 5.5 subagent", meaning an Opus-model subagent, launched from Fable 5.1's session). Batch row: G 11.49, P 11.87057 d, 124.7 ppt, 10 events, dphi +0.023, diffimg offset 2.65" (peak not on target, s9).

**TIC 437230270: per-object attribution vet (pervet-deep).** Opus 5.5 subagent, 2026-10-19.

The star is TYC 6635-619-1 = Gaia DR3 3537372345302366848: G 11.49, TIC Teff 5894 K (Gaia GSP-Phot 5661 K), TIC R 1.51 Rsun, TIC M 1.07 Msun, parallax 2.86 mas, RUWE 0.99.

Gaia DR3 SB1 orbit (goodness of fit 2.64):

| P (d) | e | ω (deg) | K1 (km/s) | corr(ω, Tp) |
|---|---|---|---|---|
| 11.874084 ± 0.001091 | 0.299 ± 0.014 | 32.6 ± 3.5 | 52.59 ± 0.81 | +0.97 |

## Verdict: CONFIRMED

This is a detached, double-eclipsing G-star + K-dwarf binary on the target. The primary is at Gaia's conjunction A, and there is a strong secondary. The difference-image flag is pixel quantization.

What decides it:
- **Attribution.** Own difference images:
  - Primary, five sectors (s9, 36, 63, 90, 100): deficit 0.2–1.8″ from the target.
  - Secondary, four sectors (s36, 63, 90, 100): deficit 0.6–2.7″ from the target.
  - Only 4 Gaia sources lie within 60″, all G ≥ 16.64. To make the primary they would need eclipses of at least 1580% (the G 16.64 star would need 138% even for the secondary). They are also rejected directly by Δχ² ≥ 39,000 (15–38σ scaled) for the primary and +430 to +1216 (17–28σ) for the secondary.
- **Both eclipses, consistently.** 10 primaries at 135–138 ppt (PDCSAP) and 10 secondaries at 11–13 ppt. Primary O−C is within 0.8 minutes. The secondary has the same period as the primary (difference +0.000004 ± 0.000007 d), so there is no apsidal motion over 7 years.
- **Timing against Gaia.** At Gaia's epoch the primary lands 0.069 d (1.8σ) from conjunction A.
- **Physics.** f(m) = 0.155 Msun gives m2 ≈ 0.82–0.86 Msun, a K dwarf. A two-eclipse geometry fits both depths and both durations at i ≈ 86.5–87° (§5).

## 1. Archives and web
- `cats.py 437230270 --r 60`: no VSX, no ASAS-SN. SIMBAD has TYC 6635-619-1 [SB*].
- Kostov+2025 table 2 (J/ApJS/279/50) has it at 0.001″. That is the unvetted ML list and doesn't count as prior art.
- Gaia DR3: no vari_summary or vari_eclipsing_binary row, and no variability rows for any neighbour.
- SB9, WDS and J/AJ/160/111: none. ExoFOP: no TOI or CTOI, no imaging or spectroscopy.
- A web search on all three identifiers found nothing.
- **Not previously catalogued as an eclipser.**
- MAST has QLP for s9, 36, 63, 90 and 100; TESS-SPOC for s9, 36 and 63; TGLC for s9; TARS for s9, 36, 63 and 90; ELEANOR-LITE and T16 for s9.

## 2. Every eclipse
Fits use raw QLP SAP_FLUX, QUALITY==0, with a trapezoid on a local quadratic baseline (`ecl.py`).

**Primaries:**

| sector | tc (BTJD) | depth (ppt) | T14 (h) | T23 (h) |
|---|---|---|---|---|
| 9 | 1548.3157 ± 0.0003 | 132.3 | 4.13 | 0.83 |
| 9 | 1560.1863 ± 0.0003 | 133.0 | 4.03 | 0.81 |
| 36 | 2284.2900 | 139.2 | 4.13 | |
| 36 | 2296.1605 | 137.8 | | |
| 63 | 3020.2643 | 139.7 | | |
| 63 | 3032.1348 | 138.3 | | |
| 90 | 3756.2390 | 135.6 | | |
| 90 | 3768.1091 | 135.7 | | |
| 100 | 4076.7434 | 118.4 | | |
| 100 | 4088.6135 | 118.7 | | |

- All tc errors are about ±0.0003 d. Every primary has T14 of 4.03–4.13 h and T23 of about 0.8 h. Depth errors are 0.3–0.7 ppt.
- s100 cycle 215 (4100.49) has only flagged or partial data.
- The QLP depth in s100 is low (118 ppt) because of the QLP aperture or background in that sector. My own s100 difference image gives the same target-only depth as the other sectors (about 110–120 ppt in the core window).

**Secondaries** (phase 0.628): 1567.6441, 2291.7512, 2303.6183, 3015.8534, 3027.7255, 3039.5940 (flagged cadences, ±0.0033), 3751.8266, 3763.6987, 4084.2016, 4096.0746. Errors are ±0.0005–0.0013 d. Depths are 11.0–13.7 ppt, T14 3.17–3.65 h, T23 0.4–1.1 h.

- **Background and centroids:** the background fake depth is at most 0.46 ppt for every event. QLP centroid shifts are at most 0.009 px.
- **Blind census** (4-hour box, every sector): only the primaries and secondaries.
- **Second pipelines:**
  - TESS-SPOC PDCSAP (s9, 36, 63; CROWDSAP 0.989–0.992): primary 136.2–138.0 ppt, secondary 11.6–13.0 ppt.
  - TESS-SPOC SAP: 133.9–136.8 ppt and 11.3–12.8 ppt.
  - TARS (s9–s90): 131–147 ppt and 10.6–16.1 ppt.
  - TGLC s9: PSF 108.8 ppt / 8.8 ppt, aperture 151.6 ppt / 12.8 ppt (its calibration differs).
  - Times agree to 1–2 minutes.

## 3. Ephemeris and orbit
- **Primary:** P = 11.870552 ± 0.000001 d, T0 = 2937.17038 ± 0.00009 BTJD (χ²/dof = 0.76).
- **Secondary:** P = 11.870556 ± 0.000007 d, T0 = 3407.58163 ± 0.00044 BTJD (χ²/dof = 4.4).
- **Phase separation:** 0.62842 ± 0.00004.
- **Against Gaia:**
  - P_TESS − P_Gaia = −0.00353 d (3.2σ).
  - At Gaia's epoch the primary is at 385.0016 against conjunction A at 384.933 ± 0.039 (+0.069 d, 1.8σ). The deep eclipse is conjunction A: the K dwarf in front of the G star.
  - At the s9 epoch the primary is 0.28 d *before* Gaia's conjunction A (1548.316 against 1548.593 ± 0.132), so dphi = −0.023. That matches the c4 vetsum; **the paper table's +0.023 has the wrong sign.**
- **e cos ω** from the phase separation (exact Kepler): +0.2005 ± 0.0002. Gaia gives +0.2519 ± 0.0131 (phase separation 0.6603 ± 0.0081), a **3.9σ disagreement**. Gaia's goodness of fit of 2.64 suggests its errors are underestimated by roughly 1.5–2×. A companion supplying about 20–25% of the light could also bias an SB1 solution.
- **e sin ω** isn't free from the duration ratio alone (T14 of 4.10 and 3.35 h) because the impact parameters differ between the two conjunctions; see §5.

## 4. Independence and attribution
- **Light curves:** see §2; TESS-SPOC, TARS and TGLC all show both eclipses.
- **Difference images, primary.** Fitted deficit offsets from the target (east, north) in arcsec:

  | s9 | s36 | s63 | s90 (1 event) | s100 |
  |---|---|---|---|---|
  | (+0.2, +1.6) | (+1.1, +0.1) | (+1.4, +1.0) | (+1.6, −0.1) | (0.0, −0.2) |

  The fractional loss on the target pixel is 107–111 ppt, the largest in the scene.
- **Difference images, secondary:** offsets are s36 (0.0, +1.4), s63 (0.0, +0.6), s90 (+0.4, +0.5) and s100 (+2.6, +0.2).
- **Neighbour dilution table** (depth needed = 137 ppt × 10^(0.4 ΔG); every entry is impossible):

  | Gaia DR3 | G | separation | needs |
  |---|---|---|---|
  | 3537372345302783872 | 19.15 | 26.8″ | 15,873% |
  | 3537372418317693440 | 16.64 | 37.3″ | 1580% (138% even for the secondary) |
  | 3537372139144349696 | 18.54 | 41.4″ | 9037% |
  | 3537372139146119936 | 20.05 | 51.4″ | 36,476% |

  None is a catalogued variable.
- **Why the batch flagged it:** the 2.65″ deficit-to-target offset with the peak on the pixel next to the target is sub-pixel quantization. Its psf_frac_resid (0.10) and deficit-to-light offset (0.9″) were already clean. **This is an artefact, ON TARGET.**

## 5. Physics
- **Companion:** f(m) = 0.1555 Msun gives m2 = 0.82–0.86 Msun for M1 = 1.07–1.15, a K dwarf (R2 ≈ 0.8 Rsun, T2 ≈ 5000 K). It supplies about 15–25% of the TESS light.
- **Gaia's orbit with the TIC radius fails:** with Gaia's (e, ω) and R1 = 1.51, a 4.1-hour primary can be at most about 65 ppt deep, and the secondary chord would miss (b_B ≈ 1.6 R1). That combination cannot produce the observed pair.
- **A free geometry fit does** (`geom.py`; e cos ω fixed at 0.2005, surface-brightness ratio J solved from the secondary, linear limb darkening, rectilinear chords; observables T14_A = 4.10 ± 0.10 h, T14_B = 3.35 ± 0.15 h, depth_A = 137 ± 4 ppt, depth_B = 12.0 ± 0.5 ppt):
  - Solutions with χ² < 4 need e sin ω = +0.10 to +0.29 (Gaia's +0.161 is inside), R1 = 1.0–1.35, k = 0.42–1.0, J = 0.23–1.5, i = 86.5–87.1°, e = 0.22–0.35.
  - A Gaia-consistent example: R1 = 1.10, k = 0.74 (R2 = 0.81 Rsun, a main-sequence 0.82 Msun star), e sin ω = 0.16, J = 0.46, i = 86.8°, e = 0.257.
  - This needs R1 smaller than the TIC's 1.51, which treats the binary as a single star. The remaining tension is between Gaia's (e, ω) and the photometric e cos ω (3.9σ).
- **Expected out-of-eclipse signal:** ellipsoidal plus reflection of about 0.2–0.4 ppt. The test was not attempted reliably because QLP and SPOC have 5–15 ppt of slow systematics.
- **Shape:** depths, durations, the 4-hour U/V primary and the K-dwarf secondary all fit one detached geometry. A 13.7% eclipse with K1 = 52.6 km/s and m2 ≈ 0.8 Msun is self-consistent, not the "deep eclipse with tiny K1" pattern.

## Next eclipses (BTJD)
- **Primary** (±0.0002 d): 4337.8955, 4349.7661, 4361.6366, 4373.5072, 4385.3777, 4397.2483.
- **Secondary** (±0.0007 d): 4345.3556, 4357.2261, 4369.0967, 4380.9672, 4392.8378, 4404.7083.

## What would settle it further
- High-resolution spectra to look for the K dwarf's lines (SB2). A full RV solution would test Gaia's ω and e against the photometric e cos ω = 0.2005.
- A joint light-curve model (limb darkening, third light about 0) with an SED fit to separate R1 from the companion's light.

## Row fixes for the paper table
- **P:** 11.870552 ± 0.000001 d (row: 11.87057).
- **T0:** 2937.17038 ± 0.00009 BTJD (primary, Gaia's conjunction A).
- **Depth:**
  - Primary 137 ± 1 ppt (PDCSAP, CROWDSAP 0.99; QLP SAP 132–140, s100 118). The row's 124.7 is the box median.
  - Secondary 12.0 ± 0.5 ppt at phase 0.62842 ± 0.00004 (PDCSAP 11.6–13.0; QLP 11.0–13.7).
- **Duration:** primary T14 = 4.1 ± 0.1 h (T23 ≈ 0.8 h); secondary T14 = 3.35 ± 0.15 h.
- **Event count:** 10 primaries (s9, 36, 63, 90 and 100, two each, all QUALITY==0) and 10 secondaries (9 on QUALITY==0 plus s63 at 3039.594 using flagged cadences).
- **dphi:** −0.023 at the s9 epoch (row: +0.023; the sign is wrong). At Gaia's epoch: +0.069 d, 1.8σ.
- **e cos ω:** 0.2005 photometric against Gaia's 0.252 ± 0.013 (3.9σ).
- **Difference-image flag: pixel-quantization artefact, ON TARGET.**
  - Primary: deficit 0.2–1.8″ from the target in 5 sectors.
  - Secondary: deficit 0.6–2.7″ from the target in 4 sectors.
  - No neighbour within 60″ can host either eclipse; the closest candidate would need 1580% (138% for the secondary).
  - Not a catalogued eclipser, apart from the unvetted Kostov table 2 flag.
  - The status can go from candidate to confirmed.
