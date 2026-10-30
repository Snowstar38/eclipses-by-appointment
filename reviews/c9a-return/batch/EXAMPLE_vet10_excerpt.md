# vet10: adversarial check of TIC 399758284 (TYC 97-228-1) and TIC 4341778 (TYC 7691-3893-1)

Opus 5.5 subagent, 2026-10-11/12, for Fable 5.1 (stopped once by the usage limit, resumed from `progress.md`). Its file-write tool refused REPORT.md, so Fable 5.1 saved its returned text here unchanged. Scripts `s1`–`s13`, outputs, plots and `progress.md` are in this folder; downloads in `%TEMP%\appointments\vet10\`. Notation: A = the companion passes in front of the giant (Gaia's RV star); B = the companion is hidden behind it.

Both stars survived every test: other pipelines, other stars in the same sector, pixels, the timing, and the physics. Both are **CONFIRMED** eclipsing binaries. In each, a giant orbits a hotter, smaller companion on a circular orbit, and the eclipses fall where Gaia's SB1 orbit says they should.

The by-eye classifier found both stars correctly but got several numbers wrong:
- **TIC 399758284:** the depths are A 0.45–0.6% and B 1.3–1.44%, not A 0.8% and B 1.1%. The eclipses last 42–43 h, not 34–36 h.
- **TIC 4341778:** the eclipses last 30.5 h, not ~1.5 d. Both kinds have the same near-V shape. The classifier missed a whole B eclipse, 8.8% deep, at s8 1528.08.

## 1. Archives and web
- **`cats.py` (60″):** 399758284: one VSX entry, **ASASSN-V J045420.57+062810.8, type ROT, P 39.81 d**, at 0″; full VizieR row: g max 11.68, amplitude 0.25 mag in g, epoch 2458153.54; SIMBAD type SB*. 4341778: nothing in VSX at the target (the only entry is a ROT star 51″ away, G 15.9); in Kostov table 2 (unvetted, doesn't count); SIMBAD type SB*. Neither is in ASAS-SN II/366.
## 2. Independence, systematics, pixels
- **Other pipelines (raw columns):** 399758284 s5 A: ELEANOR-lite 0.65%, T16 0.66–0.95%, TASOC 0.89%, TGLC PSF 0.73% (aperture 0.99%). 4341778 s8 B: ELEANOR 8.2–9.5%, T16 7.7–8.9%, TGLC PSF 9.4%; s9 A: ELEANOR 2.2%, T16 1.9–2.1%, TEQUILA 2.1%, TGLC PSF 2.5%; s62 A: TESS-SPOC SAP 2.2%, PDCSAP 2.4%. Detrended columns (T16 EPD/TFA, TGLC cal_*, KSPSAP) remove or weaken the long eclipses, as expected.
- **Common mode:** same window test on 219–284 unrelated stars per sector; sector medians −0.01% to +0.09%; the target ranked first or second in its sector wherever printed.
- **Neighbours:** 399758284: nothing brighter than G 17.95 within 60″. 4341778: the only star that could arithmetically produce the A depth is G 13.30 at 45.7″ (needs a 33% dip; for B over 100%).
- **TESScut difference images:** 4341778 s35 B: per-pixel fractional depth peaks at 8.76% on the target pixel (5.0% at the G 13.3 star's pixel, the target's wings). 399758284 s32 B: peaks on the target pixel (1.77%), noisier. TGLC PSF photometry also puts both signals on the target.
- **Blind dip census** (raw SAP / 4-d running median): 399758284: only A and B events plus four 0.35–0.67% features at 1451.85, 2184.34, 4030.38, 4038.94, each within 0.3 d of a data gap. 4341778: only the eclipses; the s99 A eclipse at 4058.75 falls in the 4055.7–4063.0 gap.

## 3. TIC 399758284 = TYC 97-228-1 (P 40.51 d)

**Measurements** (raw SAP, QUALITY==0, trapezoid with quadratic baseline, prayer-bead errors):

| Event | Mid (BTJD) | Depth | T14 / T23 |
|---|---|---|---|
| B s32 | 2193.1093 ± 0.0032 | 1.32% | 42.0 / 31.3 h |
| B s98 | 4016.0744 ± 0.0039 | 1.44% | 43.4 / 31.2 h |
| A s5 | 1443.679 ± 0.018 | 0.45% (0.42–0.70% across pipelines) | 40 / 30 h, red noise |
| A s98 | 3995.78 ± ~0.05 | 0.46% | fit with B's shape fixed |
| B s5 (ingress only) | 1463.951 | — | +35 min from ephemeris |

The A s98 ingress is lost (stray-light flags until 3994.66, centroid step at the 3995.6 gap): the weakest event. Background flat and centroids smooth through all good events. In s32, QLP's bit-4096 flag switches on inside the eclipse itself.

**Ephemeris** (joint fit): T0(A) = 1443.6733 ± 0.0170, **P = 40.51032 ± 0.00011 d**. B only: 40.51034 ± 0.00011; A only: 40.50954 ± 0.00084. O−C: +8, −63, −0.4, +0.5 min (the −63 is the compromised s98 A). B at phase **0.49988 ± 0.00043**, so e cos ω = −0.0002 ± 0.0007 (Gaia +0.003 ± 0.006; Gaia's e = 0.015 ± 0.007 is a 2σ detection): circular. Gaia P differs by +1.16σ; all four events fall 0.08–0.22σ (+0.3 to +0.8 d) from Gaia's conjunctions.

**Physics:** joint two-sphere fit with limb darkening, circular: a/R1 = 5.27, b = 0.78, i = 81.4°, k = 0.072–0.073, J = 2.5–2.7, companion 1.40% of the TESS light, RMS 0.77 ppt. Both kinds flat-bottomed (A a full transit, B a total occultation; B deeper because the companion is hotter). Central T14 would be 63 h; observed 42–43 h follows from b = 0.78. f(m) = 0.148 M☉: for M1 = 1.0–1.5 M☉, m2 = 0.79–0.98 M☉, a = 60–67 R☉, R1 = 11.4–12.8 R☉ (TIC 10.8), R2 = 0.84–0.93 R☉. T2 ≈ 5900–6000 K from J with T1 = 4574 K: a G dwarf whose radius, temperature, light share and mass all agree with the mass function.

**The VSX ROT signal:** real, but spots, not the eclipses. A 0.25 mag amplitude in g is far beyond what 0.5–1.4% eclipses or ~0.5% ellipsoidal variation could produce; the star is spectroscopically active and TESS shows 2–3% spot-like drifts in every sector. P_rot 39.81 d = 0.983 × P_orb: near-synchronous rotation, typical of an RS CVn-type giant. The rotation period could not be measured independently (sectors shorter than the period; ASAS-SN photometry not obtained).

**Verdict: CONFIRMED.** A detached eclipsing binary: K giant and G dwarf. VSX should add EA with P = 40.5103 d, keeping ROT (EA+ROT/RS).

**Next eclipses** (BTJD, ±0.02 d; T14 about 1.78 d): A: 4360.417, 4400.927, 4441.437, 4481.947. B: 4340.157, 4380.667, 4421.177, 4461.688.

**What would settle it further:** a B eclipse with both edges in clean data; a spectrum to test for the faint G companion (about 1.4% of the light).

