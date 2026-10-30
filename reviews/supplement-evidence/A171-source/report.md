# TIC 191146789 (TYC 3248-1904-1, Gaia DR3 389224749709356544): per-object vet

Opus 5.5 subagent, wave 5, 2026-10-21. No earlier session had worked this star. (Saved by the parent session; the file-write tool refused REPORT.md for the subagent.)

## Verdict: **CONFIRMED** (the eclipse is real, on target, and tied to the Gaia orbit), **with a physics tension flagged**

**The numbers that decide it:**
- **Events:** mining flagged cadences took the count from **3 to 8**. All are listed below.
- **Period:** P = 7.7886371 ± 0.0000029 d, −0.38σ from Gaia.
- **Gaia conjunction A:** +0.70, +0.44 and +0.26 h from the eclipse in s017, s057 and s084 (≤ 0.65σ), and +1.05 h (1.8σ) at the Gaia epoch.
- **Localization:** the deficit is 0.0–3.1″ from the target in 4 products.

**The 8 events (events.py):**

| Sector | Event | Type | Depth (ppt) |
|---|---|---|---|
| s017 | E−139 | Q0 | 23.7 |
| s017 | E−137 | Q0 | 23.5 |
| s057 | E1 | Q0, pre-ingress flagged | 22.1 |
| s057 | E2 | every cadence flagged (bit 2³⁰), complete eclipse | 21.9 |
| s057 | E3 | ingress only | timing only |
| s084 | E95 | Q0 | 23.4 |
| s084 | E96 | Q0 | 22.9 |
| s084 | E97 | Q0 | 22.7 |

**Jackknife:** no single event controls the result.
- Dropping any one event moves P by ≤ 1.7×10⁻⁶ d and the depth by ≤ 0.16 ppt. Each dropped event lands within 2.0σ of the rest.
- Dropping a whole sector leaves P stable to ≤ 3×10⁻⁶ d.
- The batch's three s084 events, used alone, predict all five earlier events to within 1.1–1.3σ, so those are independent recoveries. With Gaia's P instead, the earlier events land within 0.4–0.7σ.

## Archives
Nothing eclipsing anywhere. Same battery as 88457347 (VSX, ASAS-SN, Prša, IJspeert, Kostov, SB9, WDS, J/AJ/160/111, ExoFOP, Gaia vari tables, web search); SIMBAD lists it as SB*. Gaia: e 0.035 ± 0.012, ω 37 ± 18°, K1 60.49 km/s, RUWE 1.33. Not previously catalogued as eclipsing.

## Light curve
- **Primary:** 22.7 ± 0.2 ppt, T14 3.42 h, T12/T14 0.4.
- **Background:** fakes ≤ 1.8% of the depth. E235 sits on a +939 e⁻/s ramp; that is the 1.8% case, and its depth holds.
- **Systematics:** no bit-32 cadences, and no event is near a listed systematic time.
- **Control phases:** all within ±0.28 ppt.
- **TESS-SPOC s017:** PDCSAP 22.5 / SAP 21.7 ppt at the same ephemeris.
- **Ellipsoidal variation:** present in every sector and pipeline, A2 +0.31 to +0.87 ppt with minima at the conjunctions.

## Secondary
- **Gaia prediction:** phase(B) 0.5162 ± 0.0061.
- **Fixed test at that phase:** +0.39 ± 0.12 ppt (3.2σ).
- **Best point in the scan:** 0.79 ± 0.13 ppt (6.2σ) at phase 0.520 with a short 2.5 h duration. It is positive in all three sectors (s017 +0.31 ± 0.30, s057 +0.79 ± 0.19, s084 +1.05 ± 0.21 ppt).
- **Controls:** rms 1.33σ, maximum +3.67σ.
- **e cos ω:** about +0.03, against Gaia's +0.025 ± 0.0095.
- **Overall:** no secondary deeper than about 1 ppt at any phase.

## Localization
- **Batch:** deficit−target 1.14″.
- **Own PSF fit:**

| Product | Offset from target | Missing flux / target flux |
|---|---|---|
| TESScut s017 | 2.1″ | 2.25% |
| TESScut s057 | 0.0″ | 2.01% |
| TESScut s084 | 0.9″ | 2.04% |
| SPOC TPF s017 | 3.1″ ± 1.9″ | 1.80% |

- The next-best star's fit is worse by Δχ² ≥ 550 in every product.
- **Neighbours:** G 15.25 and 15.71 at 34″ would need 71% and 118% dips; G 14.74 at 83″ would need 49%.

## Physics: the tension
- **Companion mass:** f(m) = 0.178 M☉, so m2 ≥ 0.93 M☉. A main-sequence companion that massive (about 5540 K) would carry 10–20% of the light.
- **Secondary prediction:** with Gaia's e sin ω (+0.020 ± 0.013), physics.py predicts a 10–18 ppt secondary eclipse. Observed: ≤ 0.8 ppt.
- **Shape can't decide it:** k 0.16–0.50 all fit (k ≥ 0.25 grazing). A grazing k ≈ 0.43 is within Δχ² 1.8 of the best fit.
- **To hide the occultation**, a normal main-sequence companion needs e sin ω ≳ 0.06–0.08 (R1 1.6–2.5). That is 3–5σ from Gaia's e sin ω, and about 3σ more eccentric overall (e ≈ 0.07 vs 0.035 ± 0.012).
  - It would make the conjunction-B chord ultra-grazing and short, which fits the 2.5-h hint at 0.52.
  - It runs in the same direction as 1260529, against the usual small-e failures.
- **Alternative:** a dark but massive companion, for example a close M+M pair.
  - A single compact object can't make a 22 ppt transit.
  - The depth constancy, χ²/dof 12.3/5, mildly allows varying transit shapes.
- **Duration:** under both hypotheses, T14 and Kepler's a give R1 ≈ 1.6–1.8 R☉, against TIC's 2.2.
- None of this undermines the eclipse or its tie to the Gaia orbit. It concerns what the companion is.

## Next predicted eclipses (BTJD)

| Kind | Times | Uncertainty |
|---|---|---|
| Primary | 4401.2330, 4409.0216, 4416.8103, 4424.5989 (then +7.7886371 d) | ±1–2 min |
| Secondary (≤0.8 ppt, phase ~0.519) | 4405.275, 4413.064, 4420.853, 4428.641 | ±~1.1 h |

## What would settle it further
- **RV spectroscopy:** look for SB2 lines; a G-type companion at 10–20% light should show them. This also tests e directly.
- **Occultation:** more sectors to confirm the phase-0.52 dip and its duration, which gives e sin ω.
- **Gaia DR4** epoch RVs.

**Row fixes:** P 7.7886371(29); depth 22.7 ppt; **8 events (not 3)**; offset confirmed on target; flag the companion-light / e sin ω tension.
