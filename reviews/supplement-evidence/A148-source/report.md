# TIC 85944269: per-object vet
Opus 5.5 subagent for Fable 5, 2026-10-19 (wave 3b). Ledger row: G 11.48, P 3.02120 d, 13.1 ppt, 90 events, dphi +0.026.
Star: TYC 2669-4733-1, Gaia DR3 2033384753750667264, d ≈ 1.04 kpc, Teff 6470 K. The TIC radius is 4.84 Rsun, but see Physics below. TIC contratio 0.62, |b| = 1.4°. Gaia NSS **SB1**: P 3.021253 ± 0.000242 d, e 0.085 ± 0.052, ω 150 ± 43°, K1 31.7 ± 3.0 km/s.

## Verdict: CONFIRMED. A grazing eclipsing binary (primary and secondary) with ellipsoidal variation, and it is the Gaia SB1 itself. The component properties do not fit a simple picture (see Physics).

**Deciding numbers**
1. **Same period as the Gaia orbit.** P = 3.021219 ± 0.000003 d (TESS) against Gaia's 3.021253 ± 0.000242: **−0.14σ**.
2. **On the right conjunction.** The deeper eclipse falls on Gaia conjunction A (companion in front, primary eclipsed) at **−0.023 to −0.029 in phase (−1.7 to −2.1 h, −0.33 to −0.55σ)** in every sector.
   - The secondary sits at phase 0.50185 ± 0.00020. Gaia predicts 0.464 ± 0.032 (1.2σ).
3. **Two eclipse kinds, both detected in every sector.**

   | Eclipse | Depth (QLP SAP) | T14 | T12/T14 | Events (Q0) | S/N per event |
   |---|---|---|---|---|---|
   | Primary | 17.33 ± 0.10 ppt | 4.62 h | 0.4 | 48 | 8–35 |
   | Secondary | 11.02–11.16 ± 0.09 ppt | 4.44 h | 0.35 | 47 | 9–23 |

   - The secondary has its own ephemeris: P2 = 3.021213 ± 0.000002, −1.6σ from P.
4. **On target.**
   - TESS-SPOC difference images in s014, s041, s054 and s055 all favour a PSF at the target over the next-best star, G 12.73 at 22.8″, by Δχ² = 995 / 8965 / 5575 / 5580. The loss-weighted centroid is within 0.5–1 px of the target.
   - The batch diffimg agrees (s075: on target, 4.6″).
   - QLP centroid in−out: dX −0.4 ± 0.3, dY +0.4 ± 0.3 mpix.
   - Neighbour dips needed:

     | Neighbour | Needed dip |
     |---|---|
     | G 12.73 at 22.8″ | 5.5% |
     | G 14.17 at 38″ | 21% |
     | G 15.7–15.9 at 28–49″ | 88–99% |
     | VSX Gaia DR3 2033384753703991680 (G 18.45 [L] at 25″) | ~800% |

     Only the first two are photometrically possible, and the pixels exclude both.
5. **Independent pipelines.**
   - TESS-SPOC PDCSAP (crowding-corrected) gives a primary depth of 19.6–20.3 ppt (s014/41/54/55); SPOC-SAP gives 12.5–15.7 ppt.
   - The ratio of eclipse depth to ellipsoidal amplitude is the same within scatter in QLP (3.24–3.69), SPOC-SAP (2.97–3.67) and PDCSAP (3.50–4.63). The eclipses and the ellipsoidal variation therefore come from the same diluted source.

**Measurements (QLP SAP_FLUX, QUALITY = 0, no trimming)**
- **Primary depth:** χ² for constant depth 114/47, from sector-to-sector QLP dilution (s055 16.85 against 17.4–17.7 elsewhere). Odd 17.49 ± 0.14, even 17.17 ± 0.14.
- **Flagged cadences:** about 14 more primaries in flagged-only cadences show 11–20 ppt dips at the predicted times. One s014 epoch inside a scattered-light (QUALITY 6144) region does not.
- **Ephemeris:** T0 = 2951.66557 ± 0.00045 BTJD. χ² 145.8/46 (errors ×1.78), O−C rms 5.7 min.
  - The s014 primaries (30-min cadence) run 6–17 min early; dropping s014 moves P to 3.021209.
  - The s014 secondaries are not correspondingly early (about −2 min). So this is most likely a cadence/template effect, not an ETV. Worth a look, not a claim.
- **Orbit shape:** e cos ω = +0.0031 ± 0.0003 from the secondary phase (light-travel time about 30 s, negligible), consistent with circular; Gaia gives −0.07 ± 0.05.
  - The duration ratio (0.96) implies e sin ω of about −0.02, but grazing eclipses make that number unreliable.
  - Gaia's e = 0.085 ± 0.052 is 1.6σ from zero.
  - This is a 3-d near-circular orbit, so the heartbeat blind spot does not apply.
- **Ellipsoidal (cos 2φ semi-amplitude):** 4.3–5.4 ppt in QLP, 4.3–5.7 in PDCSAP.
- **Systematics:** no event lies within 0.5 d of a listed sector-wide systematic, and five windows contain a bit-32 cadence. Background regression allows at most 1.9 ppt of fake depth per event (typically under 0.7), against a 17 ppt eclipse. Control phases 0.125–0.875 (excluding 0.5) are all within ±0.43 ppt.
- **Blind census:** every dip deeper than 0.5× the primary is a primary or a secondary. The remaining S/N 4–5.6 dips are 2.4–3.6 ppt features clustered at phase ±0.3, which is ellipsoidal residue.
- **Archives:** cats.py found no VSX, ASAS-SN, Prša, IJspeert or Kostov entry at the target; its only VSX hit is the G 18.45 [L] star at 25″. SIMBAD has TYC 2669-4733-1 only as [SB*]. SB9, WDS and J/AJ/160/111 have nothing. Gaia vari tables are empty. ExoFOP has no TOI/CTOI. A web search on the TYC, TIC and Gaia ids found nothing. **New as an eclipsing binary.**

**Physics: a real tension, recorded rather than resolved**
- **Mass function:** f(m) = 0.0099 M☉ (±29%). For M1 = 1.32–1.6 M☉ that gives m2 = 0.30–0.37 M☉ at i = 65–90°, and a ≈ 10.3–11.0 Rsun.
- **The eclipses demand a bright companion.** The secondary/primary depth ratio of 0.644 fixes the companion's TESS surface brightness at 0.64× the primary's, i.e. **Teff2 ≈ 5600–5700 K**. A 0.3 M☉ main-sequence star (about 3400 K) would give a ratio near 0.1.
- **But a bright companion breaks the RVs.** A main-sequence companion that hot (about 1 M☉) would need K1 ≈ 84 sin i km/s, against Gaia's 31.7 ± 3.0.
- **The ellipsoidal amplitude disagrees with the TIC radius.** About 5.4 ppt implies q(R1/a)³ ≈ 4.5 × 10⁻³. With Gaia's q (about 0.23) that needs **R1 ≈ 2.8–3.1 Rsun, not the TIC's 4.84**; with 4.84 Rsun the ellipsoidal would be 21–30 ppt. With q of about 0.76, R1 would be about 2.1 Rsun.
- **Durations are consistent but uninformative.** The 4.6 h eclipses are grazing (half-chord about 2.1 Rsun against a central duration of order 8–12 h), so they say nothing more.
- **Possible resolutions:**
  - Gaia's SB1 K1 is depressed by line blending in an unrecognised SB2.
  - The companion is a low-mass but hot stripped/pre-He-WD star (EL CVn-like, though cool for that class).
  - There is third light inside the Gaia source.
- None of these moves the eclipses off the Gaia binary: the period, the conjunction, the pixels and the shared ellipsoidal all tie them to it.

**Row fixes for the paper table**
- P: 3.02120 → **3.021219 ± 0.000003 d**; T0 **2951.66557 ± 0.00045 BTJD**. The search found P2 = 1.5106 (half the period), so the resolved period is right.
- Depth: 13.1 → **primary 17.3 ppt, secondary 11.1 ppt** (QLP SAP; PDCSAP primary about 20 ppt crowding-corrected). The 13.1 was the both-kinds average at P/2.
- Durations: **T14 4.6 / 4.4 h**, V-ish, grazing.
- Events: **48 primaries + 47 secondaries** in Q0.
- dphi: primary on conjunction A at −0.026 (−0.4σ); secondary at phase 0.5019.
- Notes: ellipsoidal 4.3–5.7 ppt; e cos ω +0.003. Flag the K1 / depth-ratio / ellipsoidal tension.

**Next predicted times (BTJD)**
- Primary: **4335.3839, 4338.4052, 4341.4264** (± 0.0013 d).
- Secondary: **4336.9001, 4339.9214, 4342.9426** (± 0.0015 d).

**Would settle it further:**
- A spectrum to test for SB2 lines (decides the K1 question).
- A light-curve model with ellipsoidal, beaming and reflection terms to fit R1/a, q and the light ratio jointly.
- 2-min photometry of s014-like epochs to test the 10-min O−C offset.

---

## Addendum (Fable, 2026-10-20 21:30 session): the tension, pushed as far as the archives go

Receipts: `spec.py`/`spec-out.txt`, `vsweep.py`/`vsweep-out.txt`,
`tension.py`/`tension-out.txt`, `lamost_meta.py`.

**The spectrum gate is a real dead end in current archives.** LAMOST LRS has
no spectrum of this star in DR1, DR2, DR4, DR5, DR7 or **DR11 (V/162, Luo+
2026)** — 8″ cones, catalogue ids validated against a dense test field first
(several guessed ids in `spec.py`'s first pass were nonexistent tables, which
VizieR reports identically to a miss; `vsweep.py` is the corrected
instrument). APOGEE DR17 (III/286): nothing. GCVS: nothing. So the SB2-line
test waits for new data — realistically Gaia DR4 epoch RVs.

**Gaia DR3 RV diagnostics kill the "K1 is secretly ~84 km/s" escape.**
`rv_amplitude_robust = 67.0 km/s` over 25 transits — the raw epoch-RV spread,
no orbit fit involved — against 2·K1 = 63.4 (ratio 1.06). A 1 M☉
main-sequence companion needs a spread of ~168. For blending to compress
epoch RVs 2.5× the companion would have to rival the primary in RVS flux,
which the 0.64 depth ratio already forbids (it fixes the companion's
*surface brightness*, and a near-equal-flux companion would give a near-unity
depth ratio and double lines Gaia's pipeline flags as SB2). Gaia's K1 stands;
**M2 = 0.30 ± 0.03 M☉** (f(M) = 0.0099, M1 1.32–1.6, i ≳ 75°).

**The ellipsoidal half of the tension dissolves: TIC's radius is the
outlier.** Four instruments independent of the TIC converge on R1 ≈ 3 R☉:
ellipsoidal q(R1/a)³ → 2.80 (q 0.227, a 10.35); **Gaia vbroad = 54.3 ± 18.7
km/s** → R_sync = 3.2 ± 1.1 if tidally synchronized (P 3.02 d; TIC's 4.84
predicts 81 km/s, −1.4σ); SHBoost (V/160, Gaia DR3 ML) logg 3.70 + M 1.78 →
3.1; GDR2AP (V/155) R0best 3.41. The TIC's 4.84 comes from blended
photometry at |b| = 1.4° with contratio 0.62.

**What genuinely remains, and the reading it points to.** A 0.30 M☉
companion with TESS-band surface brightness 0.64× a 6466 K primary (T2 ≈
5600–5700 K) cannot be a main-sequence star (an M dwarf gives ~0.1). The
self-consistent picture is a **stripped post-mass-transfer companion** — the
R CMa / EL CVn-precursor family: M2 ≈ 0.3, T2 ≈ 5650, R2 ≤ its Roche lobe of
2.7 R☉ (tension.py; a detached, shrinking proto-He-WD at R2 ~ 1–2 R☉
contributes 6–20% of the light and keeps the donor's own distortion signal
small, as observed). The primary at R1 ≈ 3, M1 ≈ 1.3–1.8 would be the spun-up
accretor. One loose thread survives: at plx 0.935 mas the source wants
L ≈ 22–41 L☉ (A_G 0–0.66), i.e. R ≈ 3.8–5.1 at 6466 K — a factor ~1.5–2 more
light than an R1 = 3 primary plus stripped companion supply. Either the
extinction/BC budget at 1 kpc in the plane absorbs it, or there is third
light inside the Gaia source (RUWE 0.86 and ipd_frac_multi_peak 0 exclude
only *resolved* companions; a tertiary would also dilute the TESS depths —
ratios, and hence T2, unaffected).

**For the paper row:** keep CONFIRMED; the note should say "companion is
likely a stripped post-mass-transfer star (R CMa/EL CVn-like): M2 ≈ 0.3 M☉
from Gaia K1 (raw epoch spread confirms), T2 ≈ 5650 K from the depth ratio,
R1 ≈ 3 R☉ from ellipsoidal + vbroad + two Gaia AP catalogues (TIC's 4.84 is
blend-inflated); possible unresolved third light at the ~30–50% level."
No LAMOST/APOGEE spectrum exists; Gaia DR4 epoch RVs are the next decisive
instrument.
