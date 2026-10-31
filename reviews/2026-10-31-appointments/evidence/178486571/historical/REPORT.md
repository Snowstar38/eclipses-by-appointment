> Historical report: superseded by the current reconciliation at ../../../reports/178486571/REPORT.md. Its original bytes are preserved in the source archive; this public copy is sanitized.

# TIC 178486571 (TYC 5402-712-1): adversarial check

Gaia DR3 SB1, P 33.64989 ± 0.02128 d, e 0.5499 ± 0.0388, ω 16.98 ± 3.42°, K1 27.49 ± 1.40 km/s, significance 19.7. G 11.27, BP−RP 0.80, parallax 2.76 mas, RUWE 1.53; TIC Teff ~6450 K, R 1.73 R☉, M 1.31 M☉. Checked by an Opus checker for Fable 5.1, 2026-10-22 (chunk-3 wave 4, 19:11–19:20). Saved from the checker's final message by Fable 5.1; the file tool refused REPORT.md. Scripts and outputs are in this folder, a checkpoint for each step in `progress.md`; downloads in `[local path omitted]

## Verdict: CONFIRMED

The three A eclipses are real and come from the target, and their period agrees with Gaia's SB1 orbit to 1.0σ. I saw no B eclipse, and the geometry says there shouldn't be a detectable one.

## 1. Archives and web
- **Gaia DR3** (`gaia_q.py`, `arch2.py` → `gaia.json`, `archives2.json`):
  - The star: G 11.27, BP−RP 0.80, parallax 2.76 mas, RUWE 1.53.
  - The SB1 orbit: P 33.64989 ± 0.02128 d, e 0.5499 ± 0.0388, ω 16.98 ± 3.42°, Tp −7.653 ± 0.396 (BTJD 381.35), K1 27.49 ± 1.40 km/s, significance 19.7.
  - vari_summary and vari_eclipsing_binary both returned 0 rows.
  - Neighbours brighter than G 15 within 90″:
    - G 14.94 at 1.7″
    - G 14.60 at 15.6″
    - G 12.38 at 51.8″
    - G 10.96 at 81.5″
- **ExoFOP** returned HTTP 503 twice (once from the script, once with curl), so CTOIs are unchecked. The NASA Exoplanet Archive TOI table has no TOI for this TIC.
- **cats.py:** VSX none, ASAS-SN none. SIMBAD lists it as [SB*] only.
- **viz.py** (VizieR asu-tsv, 60″ cone):
  - 0 rows from VSX, Prša+2022, IJspeert+2024, Kostov t2/t3/t4, ASAS-SN II/366, SB9, WDS, Gaia DR3 vclassre, ASAS ACVS and VizieR-TAP VSX/SB9/WDS.
  - ATLAS has a row only for the G 12.38 neighbour at 51.6″, classed "dubious" with P 75.5 d. That is not the target.
  - The "Mowlavi" query returned 519 rows from the synthetic-photometry table, which is not prior art.
- **MAST CAOM** (`archives.py`): QLP s7/33/87; TESS-SPOC s7/33; TARS s7/33/87; TGLC s7 (for both the target and the 1.7″ neighbour); eleanor-lite s7; T16 s7. There is no SPOC 2-min data. I downloaded everything except T16.
- **Web search** for "TYC 5402-712-1" OR "TIC 178486571" found nothing about this star.
- **Status:** no catalogue, TOI or literature entry calls it an eclipsing binary. It is new as an eclipser.

## 2. Eclipses measured
Trapezoid fits to raw SAP plus each pipeline's flux (`ecl.py` → `ecl.txt`, `ecl_fits.png`):

| Event | Pipelines (t0 agreement) | QLP t0 (BTJD) | Depth | T14 | T12 | Flat |
|---|---|---|---|---|---|---|
| s7 (30-min cadence) | QLP, TESS-SPOC, TARS, eleanor, TGLC aperture, TGLC PSF (≤1.0 min scatter) | 1494.7835 | 4.8–6.3% (QLP 5.38%) | 5.0–5.2 h | 1.9–2.0 h | 1.1–1.25 h |
| s33 (sector start) | QLP, TESS-SPOC, TARS (1.6 min scatter) | 2201.8761 | 4.4–5.7% | 4.9–5.2 h | 1.9 h | 1.15 h |
| s87 (200 s cadence) | QLP, TARS (1.8 min) | 3683.4036 | 5.0–5.5% | 5.1 h | 2.0 h | 1.1 h |

- **The flagged s33 eclipse:** QLP flags part of the ingress, but the whole event is unflagged in TESS-SPOC (data start 2201.74). TESS-SPOC's all-cadence fit gives the same t0 to within 0.2 min.
- **s87:** the egress is cut off at 0.976 by the regular 3683.48–3683.69 data gap. The first cadence after the gap carries bit 32 (reaction-wheel desaturation). Ingress, bottom and the start of egress are seen in QLP and TARS.
- **Background and centroids:** no SAP_BKG excursion larger than 1.2 sd (each in its own units). Centroid shifts are ≤0.012 px in QLP and ≤0.005 px in TESS-SPOC MOM_CENTR.
- **Common-mode test** (`commonmode.py`): for each eclipse time I measured the same box in every other star's file from that sector (415–432 stars):
  - Same camera/CCD (30–33 stars): largest dip 0.11% in s7, 0.47% in s33, 0.40% in s87; none above 1%.
  - Not systematics, including the pre-gap s87 event.
- **Blind census** (`census.py`): only these three events exceed max(0.4%, 5 sd) in any sector, with flagged cadences either included or excluded.
- **No B eclipse seen.** The only covered B window is s87 at 3677.42 ± 0.62 d (A + 0.8222 P):
  - Every QLP cadence within ±1σ is flagged for scattered light.
  - TARS covers the window: 1-h bin scatter 0.09%, deepest bin 0.19%. So B is shallower than about 0.3%.
  - All other B windows (s7, s33) fall outside the sectors.

## 3. Ephemeris and the Gaia comparison
From `ephem.py` and `conjmc.py`, using this star's own corr_vec:
- **A ephemeris:** T0 = 1494.78347 ± 0.0006 d (0.9 min), P = 33.671079 ± 0.000022 d, cycles 0/21/65. O−C is under 0.1 min (χ² 0.0 with 1 dof, so the formal error is optimistic; I'd allow ±5 min on predictions).
  - Half the period (16.8 d) is excluded: s7 covers 1511.6 and it is flat.
- **Against Gaia's period:** ΔP = +0.0212 d, which is +1.00σ.
- **Against Gaia's predicted A conjunctions:** +0.94, +1.38 and +2.32 d, which are +1.38, +1.23 and +1.13σ. This is one effect, not three: Gaia's P is 1σ short, as the classifier said.
- **Gaia's other predictions:** B−A phase separation 0.8222 ± 0.0184; e cos ω = 0.525 ± 0.031; e sin ω = 0.160 ± 0.040.
- **e cos ω and e sin ω from timing:** not possible, because only A is seen.
- **Limb-darkened two-sphere fit** (`ebA.py`, with Gaia's e and ω fixed):
  - The eclipse is grazing to high-impact (b_A ≈ 0.8–1.2 R1).
  - The radius ratio must be at least about 0.28 (k = 0.25 is worse by Δχ² +27; k = 0.2 by +2780). Above 0.3 the fit is flat out to 0.86, the usual grazing degeneracy.
  - r1 = 0.029–0.031, which gives R1 = 1.57–1.64 R☉ at M1 = 1.31. TIC says 1.73 R☉. So Gaia's e and ω reproduce the stellar density.

## 4. Independence tests
- **Other pipelines:** six independent light curves show the s7 event, three show s33 and two show s87. Times agree within 2 min. Depths range 4.4–6.3% because the apertures differ.
- **Per-pixel regression on TESScut 11×11 cutouts** (`pixreg.py` → `pix_s7A`, `pix_s33A` .json/.png):

| Sector | Deficit centroid to target | Depth: target pixel / 3×3 / 5×5 |
|---|---|---|
| s7 | 2.1″ | 5.14% / 4.84% / 4.13% |
| s33 | 3.8″ | 4.74% / 4.42% / 3.70% |

  - Neighbour pixels: G 12.38 shows 0.36% / 0.94%, but would need 15.2%. G 10.96 shows 0.05% / 0.54%, but would need 4.1%. Neither is the source.
  - The s87 cutout was requested but not used.
- **Neighbour dilution table** (depth × 10^(0.4 Δm)):

| Neighbour | Fractional dip it would need | Verdict |
|---|---|---|
| G 14.94 at 1.7″ | 162% | impossible |
| G 14.60 at 15.6″ | 118% | impossible |
| G 12.38 at 51.8″ | 15.2% | excluded by the pixel fit |
| G 10.96 at 81.5″ | 4.1% | excluded by the pixel fit |

- **TGLC PSF caution:** the TGLC PSF light curve of the 1.7″ neighbour shows a 97% "dip". That is the PSF fit trading flux between two sources 0.08 px apart, not a signal from the neighbour.

## 5. Physics
From `physics.py` → `physics.txt`:
- **Mass function:** f(M) = 0.0422 M☉, so m2(i = 90°) = 0.48 / 0.52 / 0.55 M☉ for M1 = 1.15 / 1.31 / 1.45. With i ≈ 86–88° the sin i correction is negligible. a = 52–55 R☉.
- **Separation at each conjunction** (M1 1.31): 32.3 R☉ at A, 44.6 R☉ at B, a ratio of 1.38.
- **Central durations:** 7.4–7.9 h at A and 10.2–11.0 h at B. The observed A duration of 5.1–5.3 h with a V-ish shape means high impact, consistent with the fit.
- **Which star is in front:** at A (ν = 90° − ω) the companion, a dwarf of about 0.5 M☉ and roughly 0.45–0.5 R☉ (k ≈ 0.3), transits the 6450 K primary. A 5.5% depth fits k ≈ 0.3 at b ≈ 0.9.
- **B is the companion's occultation**, at an impact parameter 1.38× larger:
  - k = 0.25 predicts 0.11%.
  - k = 0.3 predicts 0.03%.
  - k ≥ 0.35 means no eclipse at all.
  - The geometry therefore predicts the missing B, and the TARS limit (under 0.3%) is consistent with it.

## 6. Verdict: CONFIRMED
**The deciding numbers:**
- Three A eclipses repeat at P = 33.67108 d, matching Gaia's 33.6499 ± 0.0213 to 1.0σ.
- Each lands +1.1 to +1.4σ from Gaia's predicted A conjunction; that is the 1σ period difference compounding, not a timing problem.
- Up to six pipelines confirm them.
- 30–33 same-CCD stars are flat at each eclipse time (worst 0.47%).
- The pixel-level deficit sits on the target to within 2–4″, and every resolvable neighbour is excluded.
- The duration and the fitted stellar density are consistent with Gaia's e and ω and with the companion mass from the mass function.

**Next eclipses** (`next.txt`):
- **A (deep, about 5.5%, about 5.2 h), formal ±2.4 min, allow ±5 min:**
  - 4356.825 BTJD (2026-11-12 07:48 UTC)
  - 4390.496 (2026-12-15 23:54)
  - 4424.167 (2027-01-18 16:00)
  - 4457.838 (2027-02-21 08:07)
  - 4491.510 (2027-03-27 00:13)
- **B (expected 0.1% or less, or absent), ±0.62 d:** 4350.84, 4384.51, 4418.18, 4451.85, 4485.52.

**What would settle it further:**
- A clean B-window light curve at the ~0.05% level, or ground or TESS photometry, to measure k and b and break the grazing degeneracy.
- RVs or a future Gaia DR4 orbit at the eclipse period.
- One more A eclipse, to tighten P beyond three points.

**Services that could not be checked:** ExoFOP (503), so CTOIs remain unchecked. VizieR TAP worked for VSX/SB9/WDS on this run.
