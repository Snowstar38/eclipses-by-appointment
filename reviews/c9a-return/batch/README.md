# Chunk-9 (c9a) candidates: screening and vets, 2026-10-30

Cloud session (Fable 5.1 lead, Opus 5.5 helpers) on the 24-star bundle Astra packaged from Fable 5's `sb1-scale` chunk 9 (montage sheets c9a_00 and c9a_01; roster order = best z descending). Everything here is on the branch `claude/zealous-pasteur-8mmme2`.

## What was done
1. **Screen** (`SCREEN_RESULTS.csv`, `SCREEN_REPORT.md`): first-pass visual triage of the two montage sheets, three Opus helpers at eight panels each plus a second look at the borderline calls. 19 eclipse-like, 5 non-eclipse-like, 0 ambiguous, 0 unreadable.
2. **Shared inputs** (`targets.csv`, `neighbours_90as.csv`, `prep.py`): TIC rows, Gaia DR3 NSS SB1 orbits (VizieR I/357 via the idia mirror; the CDS and ESA hosts were unreachable), Gaia neighbours within 90", QLP / TESS-SPOC / 2-min / TESScut sector lists.
3. **Vets** (`vet01`–`vet06`, `vet11`; protocol in `VET_BRIEF.md`): independent adversarial checks to the paper's Section 2.5 tier definition (events from raw SAP, period from the eclipses, difference images and dilution, independent pipeline, Gaia geometry). `VERDICTS.md` is the one-line-per-star table; each `vetNN/REPORT.md` holds the evidence, scripts and outputs.

## Results
| | n | TICs |
|---|---|---|
| vetted CONFIRMED | 12 | 195865529*, 468181994, 470235665, 379251709, 70665829 (= paper's A4, blind control, recovered), 331293467, 283532878, 407877153, 15855794, 92881948, 468827621, 416285595 (with caveats: pipeline depths differ ~12%) |
| of which already a catalogued eclipsing binary | 1 | 195865529 (ASAS-SN EA, same period; not in VSX) |
| sinusoids refolded at Gaia P: ellipsoidal | 3 | 372683900, 13106408, 372683622 |
| sinusoids: grazing detached EB, fold-level only (PLAUSIBLE at best) | 1 | 319185391 (also a Gaia 434 d astrometric orbit: likely triple) |
| sinusoids: signal from a neighbour (δ Scuti at 44"); target flat at the Gaia period | 1 | 62328710 (Gaia's SB1 orbit for it is suspect) |
| eclipse-like, **not yet vetted** (credits ran out) | 7 | 300903537, 23112764, 373062090, 465073693, 316405449, 465263741, 441741446 |

Side findings worth a catalogue note: a catalogued EB (Gaia DR3 2202301140233408128, P 1.7975 d) sits 29.7" from 283532878 and may leak ≤3 ppt dips into its light curve; 372683900's equal, half-period-spaced minima conflict with Gaia's e = 0.30 at 3.3σ; several secondaries are off phase 0.5 and match Gaia's e cos ω (470235665, 283532878, 407877153, 92881948, 468827621).

## Cost note, for the next batch
Each full vet cost ~240k Opus tokens, about two stars per agent. Most of that was execution depth the tier does not need (every individual event fitted, own TESScut photometry on top of two pipelines, dilution for every neighbour within 90", Monte Carlo geometry, physics checks, ephemerides, literature search) plus each agent rebuilding its tooling from scratch, and a container restart that cost wave 1 roughly 1.7×. For the remaining seven: reuse the scripts in `vet04/` or `vet05/` (`common.py`, `fitlib.py`), a handful of events per star, one difference image per sector in two sectors, only the neighbours that matter, quoted pipeline depths, simple error propagation, two-page report. `VET_BRIEF.md` should be trimmed accordingly before reuse.

## Data-access notes (this machine, 2026-10-30)
MAST light curves and TESScut work (pass coordinates to TESScut, not names; `lightkurve.search_lightcurve` sometimes hangs, in which case fetch `mast:HLSP/...` URIs directly). Gaia: ESA TAP times out, Heidelberg TAP is slow on joins; VizieR mirror `vizier.idia.ac.za` works but is intermittent, so run a known-positive (Algol) check before trusting an empty cone. The Gaia DR3 variability tables are I/358, not I/357/varisum as the brief says. AAVSO VSX API is behind Cloudflare; use VizieR B/vsx.
