# TIC 52855832 (TYC 4030-58-1): per-object vet
Opus-model subagent for Fable 5, 2026-10-18 (saved by Fable from the agent's final message; the write tool refused in-agent). Batch row: G 11.46, P 2.41137 d, 7.1 ppt, 47 events, dphi +0.011, diffimg offset 2.26".

## Verdict: CONFIRMED. A strongly grazing EB with both eclipses detected; the primary is a γ Dor pulsator.

**Deciding numbers**
1. **Both eclipse kinds present in all 5 sectors**, including the 2019–20 30-min sectors, measured after prewhitening the γ Dor pulsation (10 frequencies per sector plus 4 orbital harmonics).
   - Primary: 9.06 ± 0.12 ppt, 42 of 43 events at S/N > 3.
   - Secondary: 5.01 ± 0.12 ppt, 36 of 41 events at S/N > 3.
   - TESS-SPOC s024 independently gives SAP 8.6 / 4.7 ppt and PDCSAP 9.9 / 5.5 ppt (primary / secondary).
2. **Right time and period.**
   - Primary: P = 2.4113702 ± 0.0000015 d, T(n = 348) = 2632.73471 ± 0.00044 BTJD, O−C rms 4.3 min. Secondary: P = 2.4113694 ± 0.0000020 d.
   - Gaia: P = 2.411344 ± 0.000139 d (+0.19σ).
   - The primary falls at Gaia conjunction A, +0.034 ± 0.129 d (+0.3σ), and is the deeper eclipse, so the hotter primary is the star being eclipsed. B excluded at 9.5σ for the primary. Secondary at phase 0.49973 ± 0.00031 vs Gaia's B prediction 0.505 ± 0.016.
3. **e cos ω and e sin ω agree with Gaia.** Light curve: e cos ω = −0.0004 ± 0.0005; durations (1.92 and 2.04 h) give e sin ω ≈ +0.03 ± 0.03. Gaia: +0.015 ± 0.026 and +0.020 ± 0.024.

**Pulsation is not the source**
- Dominant mode f1 = 1.2515 c/d = 3.017–3.019 × f_orb in every 200-s sector — close to but not locked to 3·f_orb (beat ~133 d).
- The eclipses stay at fixed orbital phase across 6 years while the pulsation phase drifts relative to them.
- Within s058 the pulsation troughs happen to line up with the eclipses — worth knowing when reading the plots.

**Systematics**
- SAP_BKG shows no excess at either eclipse (in−out ≤ 0.5σ). Centroid shifts ≤ 0.003 px.
- One s085 event (3616.57) is near the listed 3616.5 systematic; irrelevant among 84 events.

**Independence and blends**
- The s024 TPF difference image (30-min, pulsation-limited) is inconclusive: peak S/N 3.6; can't separate the target from the G 16.27 at 12.6" (0.6 px), which would need ~75%.
- The batch c4 diffimg puts the peak on target, 2.26" offset, but psf_frac_resid 0.895 — weak.
- Neighbours that could host by dilution alone: G 11.08 at 81" (~6 ppt), G 13.76 at 37" (~75 ppt), others.
- **What settles attribution:** both eclipse kinds match the target's own Gaia SB1 period and conjunctions within 0.2–0.3σ. A neighbour coincidence at that level is implausible.

**Physics: a real tension for the paper's prose**
- f(M) = 0.0433 Msun. For M1 = 1.3–1.6 Msun and i ≥ 72°, m2 = 0.52–0.62 Msun → a ~3900–4100 K companion.
- But the secondary/primary depth ratio is 0.55 (0.48 from s024 alone); in a grazing circular orbit that is the surface-brightness ratio, needing ~5600 K.
- Likely resolution: **Gaia's K is diluted by the companion's lines in the RVS spectrum.** A 0.95 Msun, 5600 K companion would give a true K1 ≈ 82 km/s and a blended ≈ 66 km/s, against Gaia's 55.8. If so, the system is a likely SB2 and m2 ≈ 0.9 Msun.
- Central transit would last ~5.6 h vs observed 1.9–2.0 h: strongly grazing, b/(R1+R2) ≈ 0.94.
- e ≈ 0, so no heartbeat concern.

**Archives**
- VSX lists Gaia DR3 522478549617967616 as DSCT|GDOR|SXPHE — a type revision: γ Dor pulsator plus EB. SIMBAD: [gD*]. Gaia DR3 has a vari_classification entry but no EB entry.
- ASAS-SN, SB9, WDS, J/AJ/160/111: none. ExoFOP: no TOI or CTOI. Web search: nothing.

**Period stability:** 2019–20 sectors give 2.411383 ± 0.000012 d; 2022–25 give 2.411353 ± 0.000003 d (2.4σ apart); dropping s085 shifts P by 4σ. Mild, probably pulsation-driven timing noise; apsidal or third-body effects not excluded.

**Next eclipses (BTJD)**
- Primary: 4335.1620 ± 0.0018, 4337.5734, 4339.9848.
- Secondary: 4336.3665 ± 0.0023, 4338.7779, 4341.1892.

**Changes to the paper row**
- The 7.1 ppt depth is the average over both eclipse kinds from the half-period search: replace with **primary 9.1 ppt and secondary 5.0 ppt**.
- Event count: **43 primaries plus 41 secondaries**, not 47 mixed.
- Note "γ Dor primary". If the paper interprets the companion from Gaia's K, flag the K-dilution/SB2 caveat.

**What would settle it further:** high-resolution spectra for the secondary's lines (an SB2 detection fixes both masses), and a 120-s/20-s TPF difference image.
