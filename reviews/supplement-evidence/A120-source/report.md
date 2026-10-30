# TIC 382605794 (TYC 8982-3032-1): per-object vet
Opus-model subagent for Fable 5, 2026-10-18 (saved by Fable from the agent's final message; the write tool refused in-agent). Batch row: G 10.58, P 2.14079 d, 2.8 ppt, 71 events, dphi +0.012.

## Verdict: CONFIRMED, grazing transit of the F star by its M-dwarf companion

**Deciding numbers:**
1. **Right conjunction:** the eclipse lands +0.50σ from Gaia conjunction A in s011 (the sector nearest Gaia's epoch), the conjunction where the companion is in front. B is excluded at 6–19σ.
2. **Right period:** TESS P = 2.140795 ± 0.000001 d against Gaia's 2.140700 ± 0.000082 (+1.2σ). All 81 events have positive depth; O−C rms is 6 min.
3. **Right star:**
   - The eclipse-to-ellipsoidal ratio is about 1.0 in every pipeline (QLP, TESS-SPOC PDCSAP and SAP, TARS, TGLC), so both signals come from one star.
   - The bright neighbour (G 10.25 at 27", TIC 382605852) shows 0.39 ± 0.25 ppt in its PSF-deblended TGLC light curve; the target shows 2.74 ± 0.24.
   - TESS-SPOC pixel difference images in s065 and s038 prefer the target over every neighbour by Δχ² ≥ 285.

**Row fixes:**
- Depth is **3.1 ppt** (paper 2.8); PDCSAP, which corrects for crowding, gives 3.4–4.0.
- Event count is **81** (paper 71).

**Other checks:**
- **Archives:** no VSX, ASAS-SN or EB-table match; Gaia vari tables empty; SIMBAD lists it only as SB*; no TOI/CTOI; no literature found.
- **WDS:** the target and the 27" neighbour are the visual pair TOB 243 (first observed 1923). The neighbour shares the parallax and proper motion, so this is probably a triple.
- **Background:** the in-eclipse change is +9 ± 12 e-/s, against +41 e-/s needed to fake the dip. A regression test bounds any background-made dip at < 0.09 ppt per sector.
- **Systematics and control phases:** no event falls near a listed sector-wide systematic time. All control phases are null.
- **Physics:**
  - Companion m2 ≈ 0.32–0.34 Msun on a graze (i ≈ 73°, b ≈ 1.1). A limb-darkened model reproduces both the 3.1 ppt depth and the 1.7 h duration.
  - The ellipsoidal (3.2 ppt) runs 0.56–0.66× the simple prediction, which hints R1 is nearer 1.75 Rsun than the TIC's 2.07.

**Caveats:**
- Depth varies across sectors more than noise allows (χ² 123/80). The shallower sectors (s099–101) use QLP's newer 3×3 aperture, so read it as aperture systematics.
- A tentative secondary sits at phase 0.500 (0.2–0.4 ppt, S/N 3.4). That depth fits the companion's occultation, and the phase implies e ≈ 0. That is 2.2σ from Gaia's e cos ω, but Gaia's e = 0.066 reads as the usual positive bias for near-circular orbits.
- Doppler beaming (expected ~0.4 ppt) isn't detected (≤ 0.12 ppt). Likely FFI detrending eating a 2-day signal; it doesn't affect attribution.

**Next eclipses (BTJD):**
- Primary: 4400.0135 ± 0.0007, 4402.1543, 4404.2951 (generally 3055.59400 + 2.140795·(E−680)).
- Secondary, if real: 4401.0839, 4403.2247.
