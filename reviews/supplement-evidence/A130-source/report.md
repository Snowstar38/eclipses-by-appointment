# TIC 240680969 (TYC 3261-1420-1): per-object vet
Opus-model subagent for Fable 5, 2026-10-18 (saved by Fable from the agent's final message; the write tool refused in-agent). Batch row: G 10.83, P 18.04742 d, 6.5 ppt, 4 events, dphi +0.018, diffimg offset 0.89".

## Verdict: CONFIRMED. The M dwarf companion transits the low-RGB primary at Gaia conjunction A, on a grazing chord (b ≈ 0.8).

**Deciding numbers**
1. **Right time.** There are 5 events: the paper's 4 plus an s017 event at 1778.684 (30-min cadence). All 5 sit at Gaia conjunction A, +1.8 to +1.9σ late (+0.31 to +0.67 d); the lag grows with time because the TESS period is slightly longer than Gaia's. Conjunction B is excluded at 22–44σ.
2. **Right period.** TESS: P = 18.047704 ± 0.000085 d, T0 = 1778.6842 ± 0.0063 BTJD (errors scaled by √(χ²/dof) = 3.5). Gaia: 18.04419 ± 0.00199 d (+1.76σ). Jackknife: dropping any one event gives P between 18.047681 and 18.047730 — no single event owns the period or the verdict. The four 200-s events alone predict the independent s017 event to −2.9 min.
3. **Right star.** The TESS-SPOC s057 difference image (2 events) prefers the target's PSF over every neighbour by Δχ² > 3e5, implying a 6.48 ppt dip on the target. The loss centroid is within 0.1 px of the target in s057 and s084, 0.3 px in s085. The only neighbour that could physically host the signal (G 14.22 at 52", needing 11–15%) is excluded by the difference image.

**Measurements** (raw QLP SAP, QUALITY==0, quadratic baseline over ±0.9 d, trapezoid)
- Shape: T14 = 0.30 d (7.2 h), ingress ≈ 0.25·T14.

| Sector | tc (BTJD) | Depth (ppt) | O−C (min) |
|---|---|---|---|
| s017 | 1778.6838 | 8.5 | −0.6 |
| s057 | 2861.5550 | 6.6 | +12.3 |
| s057 | 2879.5864 | 6.9 | −11.1 |
| s084 | 3601.4992 | 6.8 | −4.4 |
| s085 | 3619.5526 | 8.0 | +3.8 |

- **O−C scatter ±12 min against ~2 min formal** — probably red noise from the giant's surface plus spots on a 1.8 h ingress.
- **Depth varies between events** (~6.7 ppt s057/s084 vs ~8.3 ppt s017/s085), present in QLP-SAP, SPOC-SAP, PDCSAP and TARS (s085: 7.9/8.5/9.3/8.8 ppt), robust to baseline window 0.6–1.3 d and poly degree 1–3. Real, not a QLP artefact; likely spots on an active grazing chord (VSX: ROT, 58.5 d, ~4% modulation). A change in impact parameter from a third body can't be excluded with 5 events.
- **Systematics:** no listed systematic time within 2.9 d of an event; SAP_BKG and centroids smooth through every event; the s057 momentum dump is 0.8 d before the 2861.55 event. Blind census (0.30 d box, S/N > 6): only the 5 eclipses plus gap/segment-edge artefacts. Control phases 0.25/0.40/0.75/0.85 null below 0.25 ppt.

**Secondary eclipse / e cos ω**
- Gaia places conjunction B 10.599 ± 0.132 d after A. Six covered windows give −0.09 ± 0.06 ppt (2σ upper limit ~0.15 ppt). No occultation.
- So no light-curve test of e cos ω or e sin ω; Gaia's e = 0.202 ± 0.011, ω = 47.6 ± 3.4° stand untested.

**Physics**
- f(M) = 0.0104 Msun, so m2(i = 90°) = 0.25–0.34 Msun for M1 = 1.0–1.6 Msun. TIC: R1 = 2.87 Rsun, Teff 4771 K.
- At conj A the separation is 0.834a; a central transit would last 10–12 h. The observed 7.2 h total / 3.6 h flat need b ≈ 0.76–0.89 and k = 0.07–0.14 → R2 ≈ 0.2–0.35 Rsun, consistent with the M dwarf and the depth.
- At conj B the separation is 1.08a, b_B ≈ 1.0–1.15: occultation grazing or missed; a full occultation of a ~3400 K M dwarf would be ~2 ppt, so the null favours b_A ≳ 0.83 — consistent.
- Not a heartbeat: periastron at phase 0.92, 1.5 d before the event; the event is a sharp 7 h dip.

**Archives**
- cats.py: VSX ASASSN-V J003741.47+510219.2 is type ROT, P 58.46 d — a type revision, not prior art. SIMBAD: [SB*].
- Gaia DR3: no vari_summary, no vari_eclipsing_binary. SB9, WDS, J/AJ/160/111: none. ExoFOP: no TOI, CTOI, imaging or spectroscopy. Web search: nothing.

**Next eclipses (BTJD)**
- Primary: 4341.458 ± 0.014, 4359.506, 4377.554, 4395.601 (T = 1778.6842 + 18.047704·n).
- Secondary (probably grazing or absent): 4352.06 ± 0.13, 4370.11, 4388.15.

**Changes to the paper row:** keep it. Events: 5, not 4. Depth: 6.7–8.5 ppt and variable, not a single 6.5. Period: 18.04770 d.

**What would settle it further:** RVs, and more sectors to see whether the depth variation tracks the rotation.
