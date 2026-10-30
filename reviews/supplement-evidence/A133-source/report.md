# TIC 359299569 (TYC 8666-1738-1, Gaia DR3 6063854975652939136): per-object vet
Opus-model subagent for Fable 5, 2026-10-18 (saved by Fable from the agent's final message; the write tool refused in-agent). Batch row: G 11.09, P 7.14910 d, 8.2 ppt, 17 events, dphi +0.029; was on the batch "diffimg peak not on target" outlier list.

**Verdict: CONFIRMED.** The F subgiant (TIC: Teff 6939 K, R 2.91 Rsun, M 1.52) is transited by its Gaia SB1 companion, an M dwarf of about 0.22 Msun. **The "diffimg peak not on target" flag is an artefact.**

**Archives**
- `cats.py --r 60`: no VSX, ASAS-SN, Prša, IJspeert or Kostov entry. SIMBAD: SB* at 0".
- Gaia: no variability entries.
- Gaia NSS SB1: P 7.149945 ± 0.000850 d, e 0.045 ± 0.036, ω 200 ± 34°, K1 17.16 ± 0.56 km/s, significance 31, RUWE 1.07.
- SB9, WDS and J/AJ/160/111: none. ExoFOP: no TOI or CTOI. Web search: no hits.
- **New as an eclipsing binary.**
- Crowded field (galactic latitude 6.6°): 23 Gaia stars brighter than G 17 within 90".

**Light curve** (sectors 11, 38, 64, 99, 100, 102; `vet-out.txt`, `fold_oc.png`)
- Flat-bottomed transit: depth 7.88 ppt (QLP, diluted), T14 7.08 h, T12 0.71 h; steep ingress decisively preferred over V (Δχ² 4260).
- 17 events at S/N 25–66. Odd vs even depths: 7.88 vs 7.74 ppt.
- QLP depth varies by sector (s38 8.82, s64 8.17, s100 7.27 ppt; χ² 210/16) — QLP aperture contamination; the pixel-level depths don't show it.
- Background regression could fake at most 0.10 ppt. Two windows contain bit-32 cadences; none near the known systematic times.
- Blind census: no off-ephemeris dip deeper than 3.9 ppt. Real red noise present (S/N-scan rms 2.8; off-ephemeris S/N 4–8 dips are ~1 ppt).

**Ephemeris**
- P = 7.149090 ± 0.000002 d; T0 = 3352.39715 ± 0.00031 BTJD; χ² 27.9/15; O−C rms 2.3 min.
- Jackknife: no event or sector moves P by more than 1e−6 d.
- Gaia: ΔP = −1.0σ. Conjunction A matched at −1.14 to −1.37σ.

**Secondary eclipse (tentative)**
- 0.41 ± 0.05 ppt at phase 0.499 (Gaia predicts B at 0.4768 ± 0.017).
- After red noise, effective significance ≈ 3σ, and sectors disagree (s100: −0.10 ± 0.10 ppt). If real, e cos ω ≈ 0.

**On-target vs neighbour** (`localise.py`, `localise-out.txt`, `localise_*.png`)
- Method: model the out-of-eclipse scene from Gaia positions (restricted to ±4 px because of a bright star at the TESScut corner), fit a free Gaussian to the difference image, jackknife over events.

| Sector | Pixel product | Diff-image offset from target | Nearest alternative |
|---|---|---|---|
| s11 | SPOC target pixels | 0.07 px | Δχ² +442 |
| s38 | SPOC target pixels | 0.07 px | Δχ² +711 (G 15.87 at 27", 36σ) |
| s64 | TESScut | 0.05 px | Δχ² +2189 (30σ) |
| s100 | TESScut | 0.05 px | Δχ² +2735 (36σ) |
| s102 | TESScut | 0.40 ± 0.27 px | Δχ² +1676 (8σ) |

- Aperture-invariance: depth falls monotonically with aperture radius, as an on-target dip must (s64: 8.82 → 6.91 ppt from r = 0.8 to 4 px). Undiluted depth 8.9–10.3 ppt (scene model: ~9.0–9.7).
- Single-pixel apertures on neighbours show much smaller depths — the leakage expected from the target.
- Independent deblending: TGLC PSF photometry s11 gives 8.97 ± 0.18 ppt. TESS-SPOC PDCSAP: 8.77 (s11), 9.04 (s38) ppt.
- A neighbour host would need: G 15.87 at 27" → 63% dip; G 14.0 at 50" → ~11%. All excluded by position.
- **What tripped the batch flag:** the batch's own deficit was only 0.9" from the target; its *light* centroid is pulled by crowding, and a bright star at the TESScut corner breaks any unrestricted scene fit.

**Physics**
- f(M) = 0.0037 Msun, so m2 = 0.20–0.25 Msun; a = 18.8 Rsun.
- Central transit would last 9.2 h; observed 7.1 h gives b ≈ 0.6–0.7.
- Limb-darkened fit to the 3.3-min sectors: shape alone is degenerate between companion size and dilution; with dilution set from the pixel-level depth and a/R1 from Kepler: k = 0.10 (R2 ≈ 0.29 Rsun), b = 0.55, a/R1 = 7 (within Δχ² 7 of best).
- Transit stellar density 0.12–0.15 solar vs 0.062 ± 0.014 from TIC — consistent if R1 ≈ 2.6 Rsun, which Gaia's logg 3.79 suggests.
- Ellipsoidal: 0.47 ppt observed vs 0.68 predicted. Predicted secondary 0.5–0.7 ppt undiluted (~0.4–0.55 in QLP), consistent with the tentative 0.41.
- No heartbeat: e = 0.045 and a flat-bottomed 7 h transit rule it out.

**Next predicted eclipses (BTJD)**
- Primary (±1 min): 4403.3134, 4410.4624, 4417.6115.
- Secondary (Gaia phase, ±2.8 h): 4406.722, 4413.871. On the tentative phase-0.499 detection: 4406.881, 4414.030.

**Paper row changes:** remove the "diffimg peak not on target" outlier flag; note the depth is diluted (8.2 ppt in QLP, ~9.3 ppt undiluted). Nothing to strike or demote.
