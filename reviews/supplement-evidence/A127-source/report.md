# TIC 74180670 (TYC 8737-1439-1): per-object vet
Opus-model subagent for Fable 5, 2026-10-18 (saved by Fable from the agent's final message; the write tool refused in-agent). Batch row: G 10.95, P 18.42155 d, 5.5 ppt, 5 events, dphi +0.028.

## Verdict: CONFIRMED (eccentric, grazing EB with an M-dwarf companion; the verdict does not rest on any single event)

**Deciding numbers**
- **Secondary matches Gaia's eccentric orbit:** it sits at phase 0.66815 ± 0.00011, and Gaia's e = 0.301, ω = 331° predict B at 0.6665 ± 0.0173 after A (+0.09σ). The implied e cos ω is 0.2646, against Gaia 0.2615 ± 0.029. A background EB would have to share both the period and this e cos ω.
- **Period:** primary P = 18.4215088 ± 0.0000285 d, against Gaia 18.43027 ± 0.01423 (0.62σ). The secondaries give their own P = 18.4215431 ± 0.0000304, which agrees to 0.8σ.
- **Geometry fits Gaia's orbit with an M dwarf:** m2 = 0.28 M☉ at i ≈ 87.7° reproduces both the reversed durations and both depths:

| | Predicted (i ≈ 87.7°) | Observed |
|---|---|---|
| T14 at A (companion in front) | 3.0 h | 2.9–3.0 h |
| T14 at B (companion behind) | 4.0 h | 3.8–4.0 h |
| Transit depth | ~6.4 ppt | 6.1–6.5 ppt (PDCSAP) |
| Occultation depth | ~3.2 ppt (max 3.6 at T2 = 3300 K) | 3.9–4.0 ppt (PDCSAP) |

The occultation runs slightly deeper than predicted, which a T2 of about 3450 K would fix.

**Tiny-n check**
- There are 5 QLP primaries; dropping any one moves P by at most 0.72σ.
- 5 secondaries fix P independently (s12, s39, s100 and s104 individually at ≥12σ; s66 at 4.7σ), and s103 has a partial one.
- The s12 primary that QLP lost to a gap is recovered by TARS (5.9 ppt) and eleanor-lite (5.4 ppt). That makes 6 primaries.
- The s39 primary sits at the start of a background ramp (+1500 e⁻). TESS-SPOC PDCSAP and TARS both recover it, and the result holds without it.

**Archives**
- VSX only has an unrelated star at 48″. No EB-table hit, including Kostov t2. SIMBAD has TYC 8737-1439-1 [SB*], 1 ref (Gaia). No TOI or CTOI; web search found nothing. This is new.

**Systematics and neighbours**
- The blind census finds nothing at other phases except orbit-edge ramps (s66, s103) and features right before the s104 data gap.
- About 7% dilution: contratio 0.066, CROWDSAP 0.93.
- 8 neighbours could in principle host the dip. The strongest is G 14.63 at 36.9″, which would need 16% primary and 10% secondary dips.
- The diff image is on target (0.68″, but only 2 events in s104). The secondary-phase match and the consistent geometry rule out a blend much more strongly than the image does.

**Changes to the paper row**
- P should be **18.4215088(285)**; T0 = BTJD 3686.04707(105).
- QLP depth is 5.3–5.5 ppt; dilution-corrected about 6.2 ppt.
- Add the secondary: 3.3 ppt in QLP (3.9 ppt in PDCSAP) at phase 0.668.
- "5 events" should read 6 primaries plus 5 secondaries.
- The c3 eyeread note "secondary ~0.68" is confirmed.

**Next eclipses (BTJD)**
- Primary (±2 min): 4349.2214, 4367.6429, 4386.0644.
- Secondary (±4 min): 4343.1105, 4361.5320, 4379.9536.
