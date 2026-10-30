# Siblings: more transiting planets around the hunt's known planet hosts (2026-10-11, ~16:00)

The hunt removed every TOI/CTOI host from its sample before searching. Multi-planet
systems are common around M dwarfs, so those removed hosts are the likeliest place for
a planet nobody has listed yet. This pass takes them back, masks every known signal,
and searches what's left.

## Sample and data
The parent sample again (TIC 8.2 via MAST, Teff 3200-4300, Tmag 8.5-11, d < 40 pc,
DWARF): **3490 stars** (`$TEMP/hunt-sib/tic.json`). `$TEMP/hunt/targets.json` has only
2537 of them because it's capped at 5000 rows of a wider query. Hosts are any of those
with a TOI or an unpromoted CTOI in the ExoFOP tables fetched 2026-10-11:
**78 hosts, 101 signals** (`hosts.py`). Confirmed transiting planets in NASA
`pscomppars` that don't match a TOI period are added as masks (`fetch.py`): GJ 9827 c
and d, LHS 1903 e. The light curves are SPOC 2-min PDCSAP for each sector where it
exists and QLP otherwise: 686 files, 623 of them SPOC.

## Search (`search.py`)
Per sector: QUALITY==0, trim 0.5 d at gaps, **mask every known signal at ±1.5 durations**
around the ephemeris (a single window for single-transit CTOIs), 10-min bins (20 for
>12-sector CVZ stars), 1-d running median, clip at +3/-20σ. Then one coherent BLS over
all sectors, P 0.5-30 d (capped at baseline/2), boxes 0.72-4.1 h, on the hunt's grid
(oversampling 3, or 1.5 for CVZ stars). Top 6 peaks per star. `rank.py` flags:
aliases (n/m ≤ 7, 0.1%) of known planets or stronger peaks, `leak` (on a known-planet
alias peak's epochs), `sameev` (re-using a stronger peak's events), 12-14.8 d (TESS
orbit), boxes pinned at 4.1 h (variability), < 3 events.

**Calibration**, each run with one known planet left unmasked: TOI-270 b (3.360163 d,
SNR 28.8), TOI-1730 b (2.155517 d, 14.1), L 98-59 b / TOI-696.01 (0.86023 d, ~0.85 R_E,
17.6). **3/3 come back as the top peak.** The other peaks are their integer aliases.

## Results: 78 hosts, 0 errors

### TOI-6284 (TIC 286763141): two more transit signals, one of them in no catalogue
M dwarf, Teff 3548 (TIC), 0.47 R_sun, 21.0 pc (Gaia plx 47.48), Tmag 9.72, RUWE 1.19, Gaia/VSX rotation
variable at 0.02 mag. 8 sectors (S9, S35, S36, S62, S63, S89, S90, S99), 2019-2025. TOI-6284.01 is a PC at 3.4476 d,
320 ppm, 0.83 R_E. ExoFOP shows no CTOIs and no notes, NASA has no confirmed planets, and one web search finds no paper.

With .01 masked, the search's top two peaks are:

| | **7.349277 d** | **5.244544 d** (7.349 also masked) |
|---|---|---|
| depth | 420 ± 32 ppm (SNR 13.3) | 326 ± 28 ppm (SNR 11.7) |
| Rp | ~1.05 R_E | ~0.92 R_E |
| events | 21, all positive | 26, all positive |
| per sector | 327-552 ppm, 8 sectors | 269-419 ppm, 8 sectors |
| odd/even | 2.1σ | 0.6σ |
| phase 0.5 | -37 ± 32 | -23 ± 28 |
| duration | 1.58 h box, depth flat to ~2 h then falls (max central 2.13 h) | flat to ~1.75 h then falls (max central 1.91 h) |
| FFI core / halo (5 sectors) | 397 ± 44 / 322 ± 182 ppm | 286 ± 38 / 207 ± 166 ppm |
| SPOC | **TCE 1 of the S1-S96 run** (P 7.349322, 469 ± 48 ppm, MES 10.2), not a TOI or CTOI | **not in any DV report** (S1-S65, S1-S96) |

The known TOI, run the same way unmasked, comes back at 3.447593 d, 306 ppm, SNR
14.1, with FFI core/halo 277 ± 34 / 388 ± 137. So both new signals are about as
strong as the TOI itself, and in the pixels they look like it.

Period ratios: 5.2445 / 3.4476 = **1.521** (3:2 is 1.5) and 7.3493 / 5.2445 =
**1.401** (7:5 is 1.4). That would be a compact, near-resonant chain of three planets
of Earth size or smaller. 5.2445 isn't an alias
of 7.349 (5/7 of it is 5.2495, and that ephemeris drifts ~1.4 d off over the baseline)
or of the TOI. Events stay coherent over six years and 8 sectors, which momentum dumps and the
spacecraft orbit don't do.

What these tests don't exclude: TIC neighbours inside one pixel at Tmag 17.6-17.9 (13-20″,
~8 mag fainter), which would need ~60% eclipses, and anything closer than Gaia
resolves. The core/halo test has no leverage inside ~1.7 px. The 1.6-2 h durations
argue for the M dwarf's density (a central transit across a Sun-like star at 5.24 d
lasts ~3.6 h; a grazing EB could still be short). Settling it is ground-based
seeing-limited photometry and high-resolution imaging, i.e. TFOP's job.

**Rolled null** (`null.py`, .01 and 7.349 masked, 36 trials, top 6 peaks kept per trial): **0/36 reach the observed 11.6 at any period** (median best 9.1, 95% 9.5, max 9.9, all of them long-period families of 1-9 events). Below 10 d, only one trial put any peak in its top six at all (8.3). The observed 7.349 d is 13.3. Neither signal is something this light curve's red noise makes.

### TOI-1467 (TIC 240968774): SPOC's unpromoted second TCE, found again blind
Teff 3834 (TIC), 0.49 R_sun, 37.4 pc, Tmag 10.60, Gaia RUWE 1.47 (Keck AO found no companions, per the
discovery paper, arXiv 2311.00688, which used S17/18/58 only). TOI-1467 b is 5.971 d.
Top clean peak: **P 3.154127 d, 532 ± 59 ppm (SNR 9.0-9.2), ~1.24 R_E**, 21 of 21 events
positive, S17/S18/S58/S85 at 501/618/445/578 ppm, odd/even 0.4σ, phase 0.5 -111 ± 60,
1.08 h box (max central 1.66 h; coplanar scaling from b's 1.55 h predicts 1.25 h).
Its margin over the star's other peaks (2.8) is second only to TOI-6284's 7.349 d (4.4), once known-signal leaks are set aside.
**Rolled null: 0/60 trials reach 9.2 (median 6.6, 95% 6.9, max 7.7).**

SPOC's S14-S86 multi-sector DV already has it as **TCE 2**: P 3.154093 d, epoch 1767.450,
513 ± 84 ppm, Rp 1.12, MES 8.62, bootstrap false-alarm 1.5e-17, odd/even significance 0.18,
weak secondary 2.7σ, multi-sector centroid offset 37 ± 31″ (uninformative). It isn't a TOI
or a CTOI. Two pipelines finding it independently on the same pixels is
agreement, not new data.

### TOI-6255 (TIC 261135533): a background eclipsing binary 29″ south
P 14.486682 d, 1399 ppm, 5 events all positive, odd = even. It isn't TOI-6255 b leaking (events
fall at scattered b phases), it isn't momentum dumps (nearest 6-56 h away), and it isn't
the TESS orbit (5.5-10.1 d after orbit start, no pattern). P/2 is excluded: the odd
epochs at 7.24 d give -57 ± 101. But in the 200-s FFIs (`pix_261135533_s56/83.png`)
the deficit peaks 1.5-2 px off the M dwarf in both sectors, and its centroid
(`where.py`) lands 9.6″ (S56) and 5.1″ (S83) from **TIC 261126769 = Gaia DR3
1956328333130771456** (G 15.65, BP-RP 0.82, plx 0.54 mas, RUWE 1.01, no Gaia variability
or NSS flag), 29″ S of the target. Since that star is ~5 mag fainter, the eclipse on it is ~10%+.
VSX has nothing there, only a ROT 26″ away. It's probably an uncatalogued eclipsing
binary, P = 14.487 d, or 28.97 d if the eclipses are twins. Two sectors of
centroid with unquantified noise, so: "probably".

### Everything else
The rest of the clean list is leakage from known planets with imprecise ephemerides:
TOI-732 c (the TOI period is 0.009% off and drifts ~3 h by 2019), CTOI 206556127.01
(P 1.10625 vs a true 1.10549), CTOI 231279823.01 (its listed duration 0.116 is in days,
not hours), and CTOI 307210830.04 (1.048 vs 1.04918). Or variability (boxes pinned at
4.1 h; GJ 806's 0.612 d peak needs a 2.2 h transit where 0.9 h is the maximum), or
long-period families carried by 2-3 events with margins ≤ 1.5.

## If someone picks this up
- TOI-6284 is the one that matters. The next step belongs to people: a CTOI on ExoFOP (which
  needs an account, so it's the project coordinator's call, like VSX), then TFOP seeing-limited photometry
  of the neighbours inside one pixel. Predicted transits: 5.244544 d from BTJD 1546.8554,
  7.349277 d from 1551.8654 (both from this search; SPOC has 7.349322 / 1544.5090).
- TOI-1467's 3.154 d is SPOC TCE 2 already; a CTOI would put it in front of TFOP.
- The masks follow catalogue ephemerides. Four hosts leaked because a catalogue period or
  duration was off. A refit-then-mask step would close that.

## Files
`hosts.py` (sample + masks), `fetch.py`, `search.py` (`--keep` for calibration;
`SIB_HOSTS=hosts_extra.json` adds vet-only masks), `rank.py`, `vet.py`, `events.py`,
`durscan.py`, `dumps.py`, `null.py`, `corehalo.py` (stacked on-target test),
`where.py`, `cats.py` (VSX + Gaia DR3), `dvlist.py` / `dvtce.py` (SPOC DV TCEs). Results kept here: `hosts.json`, `search.jsonl`, `null_<tic>.txt`.
Data in `$TEMP/hunt-sib` (refetch with `fetch.py`).

## Prior report (checked the same evening): not new
All three signals are already in **Tschudi, arXiv:2607.23781** (v3, 2026-08-03,
submitted to AJ), "A uniform transit survey of 461 ExoFOP M-dwarf TOI hosts".
I confirmed the paper exists via the arXiv API; the per-signal numbers come
from the literature agent's reading:
- TOI-6284 "02": 5.244499 d, 298 ± 90 ppm, FPP 6.7%, tier 1
- TOI-6284 "03": 7.349312 d, 465 ± 125 ppm, FPP 24.9%, tier 1. The paper
  calls it a "candidate three-planet chain" and names an EB on the star as
  the remaining route; it doesn't mention the SPOC TCE.
- TOI-1467 "02": 3.154156 d, 533 ± 215 ppm, tier 2, grazing, near 2:1 with b
None of them is a TOI or CTOI yet. So this search is an **independent
recovery** with different code and data handling (our depths 326 ± 28 and
420 ± 32 ppm, 0/36 rolled nulls reaching 11.6), not a discovery. The only
thing we add: SPOC flagged 7.349 d as a TCE in its S1-S96 run, which the
preprint doesn't cite.
The independent re-reduction was stopped once the preprint turned up.
