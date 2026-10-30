# Chunk 9 cloud screening, batch c9a sheets 00 and 01: first-pass visual morphology

Provisional visual triage labels only. Nothing here confirms or refutes an eclipsing binary, and nothing here is a novelty claim. Numeric prior scores were treated as context, not ground truth.

## Method

Two montage sheets, 24 panels, screened in roster order. Each panel was cropped from its sheet (grid located from the axes spines), upscaled 2x, and read by one of three independent helpers (8 stars each); panel titles were read and matched against ROSTER.csv for every star. A fourth reviewer independently re-examined the five medium-confidence calls (441741446, 316405449, 465263741, 13106408, 372683900) and two off-0.5 secondaries (373062090, 283532878) and agreed with all seven; the weakest eclipse-like call is 441741446, whose 1 to 2 bin dip is what a real 0.08 d eclipse at 18.8 d would look like at this binning but is also indistinguishable from a single glitch. Checksums in SHA256SUMS.txt verified. No catalogue searches, no new plots from data (no raw light curves were supplied).

## Counts

| category | n |
|---|---|
| eclipse-like | 19 |
| ambiguous | 0 |
| non-eclipse-like | 5 |
| unreadable | 0 |
| follow_up = yes | 8 |

All 24 panel titles were legible and matched the roster TIC.

## Notes by group

Eclipse-like with clean morphology (13, follow_up no): 195865529, 468181994, 470235665, 379251709, 70665829, 331293467, 283532878, 407877153, 15855794, 92881948, 468827621, 416285595, 300903537. Most show a narrow primary at phase 0 on a flat baseline with a shallower secondary. Several secondaries sit off phase 0.5 (470235665 at ~0.52, 70665829 at ~0.46, 283532878 at ~0.675, 407877153 at ~0.545, 92881948 at ~0.485, 468827621 at ~0.72), which if real indicates eccentric orbits; these are visual readings from 300-bin folds and need confirmation.

Eclipse-like with a caveat (6, follow_up yes):
- 441741446 (P 18.8 d): single very narrow dip, 1 to 2 bins wide, about 6 ppt in the fold versus 8.7 ppt BLS depth. At this period few events are folded; could be a single event or glitch.
- 373062090: 31 ppt primary plus a 2 ppt flat-bottomed feature near phase 0.41. Off-0.5 secondary needs confirming.
- 465073693 (P2 fold of a 6.27 d Gaia period): one 230 ppt dip at phase 0. Primary and secondary may be stacked; contamination ratio 0.57.
- 316405449: sharp ~22 ppt V dip at phase 0 on top of a strong ellipsoidal double wave (sin2 6075 ppm); no distinct secondary. Contamination 0.21.
- 465263741: 9 ppt primary and 3.5 ppt secondary, each only 1 to 2 bins wide in noisy (±1.5 ppt) data.
- 23112764: clean 22 ppt primary; the 3 ppt secondary is much broader than the primary and asymmetric, possibly flattening distortion or eccentricity.

Non-eclipse-like (5): 372683900, 13106408, 372683622, 319185391 are smooth single sinusoids in the P2 fold with no localized dip, consistent with ellipsoidal double waves at the Gaia period (sin2 exceeds the BLS depth in every case). 62328710 is a noisy sinusoid with three cycles across the plotted phase range (a ~P/3 harmonic) and contamination 1.3; possibly a neighbour or pulsation. Caveat: an equal-minima contact binary folded at half period is indistinguishable from an ellipsoidal variable in these plots, so the two large-amplitude cases (13106408 at ~55 ppt peak to peak, 372683900 at ~24 ppt) are flagged follow_up yes for a Gaia-period fold.

## Limitations

- Each panel is autoscaled to its deepest feature, so 1 to 3 ppt secondaries occupy a few pixels and shallow features in deep systems may be missed.
- 300 phase bins under-resolve the narrowest eclipses at long periods (1 to 2 bins), making them V-shaped and underestimating depth.
- The 2-day flattening can suppress long eclipses; absence of a feature is not a rejection.
- High contamination ratios (331293467 at 0.70, 465073693 at 0.57, 372683900 at 0.37, 195865529 at 0.37, 62328710 at 1.3) mean the signal source is not established by these plots.
- Crops carried stray tick labels from neighbouring panels; this did not affect any reading.

## Targeted larger plots requested

1. 441741446: zoom on phase 0 (±0.03) and a per-event plot to check that more than one event contributes.
2. 465263741: zoom on phases 0 and 0.5 with unbinned points overlaid.
3. 465073693: fold at the Gaia period (6.269 d) to separate primary and secondary.
4. 13106408 and 372683900: fold at the Gaia period (2.6375 d and 1.4765 d) to test for unequal minima.
5. 316405449: larger plot with the harmonic model removed to isolate the dip.
6. 373062090 and 283532878: zoom on the off-0.5 secondaries (phase ~0.41 and ~0.675) with per-sector colouring to exclude a single-sector glitch.
7. 23112764: zoom on the broad secondary at phase 0.5.

## Contributor note

Screened by Claude (Fable 5.1 as lead, three Opus 5.5 helpers reading eight panels each, one Fable fork for a second look at borderline calls). Labels are visual morphology only. the project coordinator's team should treat the eccentric-secondary and contamination remarks as prompts for checks, not findings. Thanks for the clear handoff package; the checksums and roster made the identification step unambiguous.
