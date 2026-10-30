# TIC 449475961 (TYC 8994-1423-1, Gaia DR3 5868525051360765952): per-object vet

Opus 5.5 subagent, 2026-10-21. This session resumed work from a session that was killed on 2026-10-20; its `vet-out.txt`, `indep-out.txt`, `neighbours-out.txt` and `gaiatap-out.txt` were checked and hold up. New work this session:
- `locate.py` → `locate-out.txt` and `locate_s*.png`: own localization over 5 sectors.
- `timing.py` → `timing-out.txt` and `timing-events.json`: both eclipse kinds, ETV, e cos ω, and the comparison with Gaia at its own epoch.
- TESScut s100 and s101 cutouts, saved in `C:\Home\sky\data\qlp-sb-p20-60\vet449475961\`.
(Saved by the parent session; the file-write tool refused REPORT.md for the subagent.)

## Verdict: **CONFIRMED**: a detached, near-twin, grazing EB, and it is the Gaia SB2 itself. The eclipse is on target.

### Localization (the special instruction: the batch reported a 7.0″ offset)
**Own test.** For each sector:
1. Stack both eclipse kinds (they are equal depth) into in-eclipse and out-of-eclipse images.
2. Calibrate the WCS by fitting the out-of-eclipse image with Gaussian PSFs at all Gaia stars with G < 14.6 within 5 px, with free fluxes, a common shift and a free width.
3. Fit the difference image with one PSF at a free position, and separately at each star's calibrated position.

| Sector | Product | Eclipses | Free-fit deficit vs calibrated target | Δχ² of next-best star (G 14.49 at 17″) | Deficit / target flux |
|---|---|---|---|---|---|
| s011 | SPOC TPF | 7 | 1.3″ ± 1.3″ | +3493 | 2.27% |
| s038 | SPOC TPF | 11 | 1.8″ ± 1.3″ | +8600 | 2.06% |
| s064 | TESScut | 12 | 3.1″ ± 1.9″ | +14045 | 2.05% |
| s100 | TESScut | 12 | 0.9″ ± 0.6″ | +3027 | 1.94% |
| s101 | TESScut | 11 | 1.5″ (± 4″) | +37 (errors over-estimated, reduced χ² 0.03) | 1.92% |

- The halves-split is stable to ≤ 0.8″ in every sector.
- The missing flux is 1.9–2.3% of the target's own modelled flux, the same as the light-curve depth. So the deficit is the target's light, not a neighbour's.
- **Neighbour table:** no Gaia source of any listed magnitude lies within 17″.
  - Nearest are G 14.49 at 17.0″ (would need a 28–44% dip, with twin-equal primary and secondary) and G 15.18 at 18.4″ (26–74%). Their fixed-position fits lose by Δχ² ≥ 3000 in every sector except s101 (+37, the sector with over-estimated errors).
  - Brighter stars further out, such as G 12.27 at 72″ (Gaia VARIABLE, would need 9%), are 3.5 px away and would pull the deficit tens of arcseconds off, not 1–3″.
  - The VSX RS (41″, G 17.2) and L (48″, G 18.9) neighbours would need far more than 100%.

**Why the batch said 7.0″.** `diffimg/diffstack.py` takes a moment centroid in a 5×5 box centred on the rounded target pixel (ix = 7) and compares it with the uncalibrated catalogue position (x = 7.28). In `diff_s64.json`, the light centroid (6.98, 7.93) and the deficit centroid (6.96, 8.00) agree to 0.07 px (1.5″). Both sit about 0.30 px from the catalogue position because the box is centred off the star. That box-centring bias, not a displaced deficit, is the 7.0″. **Worth flagging for other batch stars whose target sits near a pixel edge.**

**Not separable:** Gaia RUWE 2.70 and ipd_frac_multi_peak 2 hint at an unresolved companion within about 1″. TESS cannot separate that, so "on target" here means on the unresolved Gaia source.

### Timing and the −8σ period tension
- **Ephemerides (raw QLP SAP, Q0, 30 events of each kind):**
  - Primary: P = 4.1731519 ± 0.0000014 d, T = 3037.02702 ± 0.00033 BTJD.
  - Secondary: P = 4.1731519 ± 0.0000016 d. P_sec − P_prim = 0.00 ± 0.18 s per cycle, so no apsidal motion.
- **Secondary phase:** 0.49985 ± 0.00012, which gives e cos ω = −0.0002 ± 0.0002. Gaia's +0.0256 ± 0.0097 is −2.7σ away. Gaia's e = 0.035 ± 0.011 is most likely a spurious-eccentricity artefact of a poor fit (gof 12.2). The orbit is circular, as expected for an F/G twin at 4.17 d.
- **Common-mode ETV:** per-sector O−C runs −1.0, −2.7, +2.8, +3.0, +0.6 and −2.0 min for primaries, and −1.6, −2.3, +2.6, +3.1, +1.3 and −1.6 min for secondaries, each ± 0.2–0.5 min.
  - Primaries and secondaries move together, which suggests a light-travel-time or third-body effect rather than starspots or apsidal motion. It fits the RUWE hint.
  - The s100→s101 swing of −2.6 min within one month would mean a short outer period. Alternatively it is a QLP time-stamp effect; the two are not separated here.
- **Gaia's period:** 4.173881 ± 0.000092, which is +8.0σ from TESS. Comparing at Gaia's own epoch (BTJD ~389, MC with corr_vec):
  - Gaia conjunction A is 386.956 ± 0.012, and the TESS primary falls 2.9 h later.
  - Gaia conjunction B is 389.111 ± 0.016, and the TESS secondary falls 1.2 h later.
  - Near s011 the offsets are −2.3 h (A) and −4.0 h (B).
  - An unrelated EB would land at a random phase. Instead the eclipses match Gaia's conjunctions to 0.01–0.04 in phase at epochs 1200 d apart. The leftover hours are the size Gaia's own period error implies (0.00073 d accumulates 4.4 h across its 1038-d baseline).
  - The −8σ is therefore Gaia's error bar, understated in a perturbed solution (gof 12.2, RUWE 2.7, possibly the tertiary). It is not evidence of a different star.

### Light curve, independence, physics
- **Depths:**
  - Primary 19.16 ± 0.06 ppt, secondary 19.29 ± 0.09 ppt. Odd and even primaries are equal (19.15 vs 19.16).
  - T14 is 3.0 h with a V shape (T12/T14 = 0.4).
  - The control phases at 0.125–0.875 (excluding 0.5) are all 0 within ±0.16 ppt.
  - Per-sector depths run from 17.2 (s101) to 21.4 ppt (s065) and **both kinds track each other**: for example s101 17.2/17.0 and s065 21.4/21.1. That is aperture or dilution in QLP. The adjacent-sector jump from s100 (19.2) to s101 (17.2) is too fast to be precession.
- **Background and systematics:** the background regression shows +0.27 ppt in eclipse, against +223 e⁻/s needed to fake the dip. One event has a bit-32 cadence; none falls on a listed sector-wide systematic.
- **Blind census:** every off-ephemeris dip at S/N ≥ 4 is a secondary, or a matched-filter sidelobe 0.17–0.19 d from an eclipse.
- **Second pipelines:** all at the same ephemeris.
  - TARS: 20.3–21.4 ppt in s011, s038, s064 and s065.
  - SPOC SAP: 20.2 (s011) and 19.5 ppt (s038).
  - PDCSAP: 23.7–24.6 ppt; crowding correction is applied there.
- **Physics:**
  - The SB2 gives K1 82.6 and K2 85.7 km/s, so M1 sin³i = 1.05 M☉, M2 sin³i = 1.01 M☉ (q = 0.965), and a sin i = 13.9 R☉.
  - Treat it as twin F/G stars (Gaia Teff 6356 K, logg 3.8), each about 1.5 R☉ since the TIC's 2.13 R☉ treats the pair as one star.
  - A central eclipse would last about 6.9 h; the observed 3.0-h V shape implies grazing, at a sky separation of about 0.90 (R1+R2), i ≈ 79°, masses about 1.11 and 1.07 M☉.
  - A two-limb grazing overlap gives roughly 1–2% per eclipse, equal for both kinds. That is consistent with the 19 ppt twin depths and with Gaia's near-equal K1 and K2. The SB2 needs sin i close to 1, so eclipses were expected a priori.

### Archives (step 1)
- `cats.py 449475961 --r 60` (re-run this session):
  - VSX has nothing at the target; Gaia DR3 5868524978316679552 [RS] at 41″ and 5868525051340908800 [L] at 48″ are both far too faint to matter.
  - ASAS-SN: none. SIMBAD: TYC 8994-1423-1 [SB*].
- The ebcats battery (Prša, IJspeert, Kostov) found none.
- Gaia vari_summary and vari_eclipsing_binary: no rows.
- SB9, WDS and J/AJ/160/111: none.
- ExoFOP: no TOI, CTOI or follow-up.
- A web search on "TYC 8994-1423-1", "TIC 449475961" and "Gaia DR3 5868525051360765952" found no mention.
- **Not previously catalogued as eclipsing.**

### Next predicted eclipses (BTJD; ± ~5 min, dominated by the ±3-min ETV)
| Kind | Times |
|---|---|
| Primary | 4334.8773, 4339.0504, 4343.2236, 4347.3968; then +4.1731519 d per cycle |
| Secondary | 4336.9638, 4341.1370, 4345.3101, 4349.4833 |

### What would settle it further
- **The ETV:** check whether the per-sector O−C pattern appears in SPOC or TARS times for s011, s038, s064 and s065. If it does, model it as LTTE to look for a tertiary, which RUWE 2.7 supports.
- **Gaia DR4 epoch RVs:** they should reproduce P = 4.17315 and a circular orbit.
- **High-resolution imaging:** this would resolve the ipd_frac_multi_peak companion.
