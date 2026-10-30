# TIC 384249385 (TYC 9010-4187-1): per-object vet
Opus-model subagent for Fable 5, 2026-10-18 (saved by Fable from the agent's final message; the write tool refused in-agent). Batch row: G 11.26, P 7.80588 d, 2.9 ppt, 12 events, dphi +0.017.

## Verdict: CONFIRMED, occultation of the M-dwarf companion by the primary

**Deciding numbers:**
1. **Right conjunction:** the eclipse is −0.68σ from Gaia conjunction B in s011, the conjunction where the primary is in front. A is excluded at 5.7–16σ.
2. **Right period:** TESS P = 7.805870 ± 0.000011 d against Gaia's 7.806941 ± 0.0013 (−0.83σ). There are 17 events, all at S/N > 3, with consistent depths (χ² 17.5/16).
3. **Right star:**
   - The G 13.82 star 13" away (TIC 384244452) shows a 27–39 ppt dip in its own QLP and TGLC-PSF light curves. That is about what it would need (≈ 32 ppt) to be the source, so it was tested directly.
   - Difference-image positions along the target→neighbour axis exclude the neighbour as host at **8.6σ, 10.3σ, 18.6σ and 8.6σ** in s038, s100, s101 and s102. The implied loss on the target is 3.0–3.8 ppt.
   - The neighbour's dip is leakage from the target; TGLC's PSF fit can't separate stars 0.6 px apart. The neighbour should **not** be catalogued as an eclipser.

**Row fixes:**
- Depth is **3.3 ppt** (paper 2.9).
- Event count is **17** (paper 12; s011 and s012 add 5).
- The conjunction offset is **−0.017 at conjunction B**; the CSV's +0.017 has the sign dropped. If the paper calls this a primary eclipse or transit, it should say occultation.

**Other checks:**
- **Second pipelines:** PDCSAP 3.98, TARS 2.8–4.0 and TGLC 3.5 ppt all agree.
- **Background:** at most ±0.26 ppt per sector, against a 1.7–2.6 ppt dip in the same windows.
- **Systematics and control phases:** no momentum-dump or listed systematic overlaps an event. All control phases are null.
- **Archives:** no VSX, ASAS-SN, EB-table, WDS or SB9 match; no TOI/CTOI; no literature found.
- **Physics:**
  - f(M) = 0.0168, so m2 ≈ 0.43 Msun. At B the separation is 0.78a near periastron.
  - The 3.24 h duration and 1.30 h ingress (1.25 h predicted) match a partial occultation of a ~0.44 Rsun companion, whose TESS light is ~5–9 ppt. A transit at the same geometry would be ~80–100 ppt deep.
  - No transit is seen at A (< 0.15 ppt, 2σ). A Monte Carlo over the Gaia errors and stellar parameters gives 48% of plausible configurations with no detectable transit there, so its absence is consistent.

**Caveats:**
- Only one eclipse kind is seen, so there is no e cos ω / e sin ω check from the light curve.
- A wide-box dip at phase 0.385 (S/N 4.7) is not at Gaia's A (0.472 ± 0.015). It looks driven by a single s102 dip at BTJD 4132.90 (phase 0.41).

**Next eclipses (BTJD):**
- Occultation: 4402.9219 ± 0.0014, 4410.7278, 4418.5337 (generally 3653.55840 + 7.805870·(E−262)).
- A transit at A, if one exists, would fall near 4406.61 ± 0.12.
