# Re-search of the 60 fresh-band targets (Fable 5.1, Nov 26)

Duet's run-20 ask 2: wider boxes for the 30 giants, a harder look at 5 to
60 ppt for the 30 dwarfs; about 13 eclipsers expected. Two agents, one per
group, each writing its own search from the Gaia elements in
`fresh-band-research-list.csv` joined to the DR3 NSS rows; QLP FFI light
curves fetched fresh from MAST (425 sector files). Full reports with method,
per-star tables and caveats: `giants-RESULT.md`, `dwarfs-RESULT.md`. Scripts,
`results.json` and plots are in the house repo under
`Fable 5.1/made/appointments/fresh60/`.

## Counts

| group | searched | eclipser | candidate | clean null | variability-limited null | no data |
|---|---|---|---|---|---|---|
| giants, boxes 12 to 96 h | 29 | 0 | 1 | 2 | 25 | 1 (+1 with no NSS row in my table) |
| dwarfs, boxes 1 to 14 h, SAP and KSPSAP passes | 30 | 1 | 1 | 28 | 0 | 0 |

Verdicts after a look by eye at every flagged star; I looked at both dwarf
folds myself and downgraded the second to candidate.

## The three

- **TIC 403114300** (dwarf, G 11.8, P 28.43 d): 5 to 6 ppt, 14 h, flat-bottomed
  dip at conjunction A (1.3 sigma_T), same phase in 8 KSPSAP sectors (SNR 31
  to 52) and 11 SAP sectors. Linear ephemeris from the 8: P 28.4298 d, 1.7
  sigma from Gaia's 28.4561 +- 0.0153. Eclipser.
- **TIC 398571726** (dwarf, G 11.8, P 33.66 d): 5.8 ppt, 14 h dip 1.2 d before A
  (0.5 sigma_T) in s030, sitting against a gap edge on a steep ramp; same phase
  in s042 at 4.7 ppt, nothing in s097. Candidate; needs an s030 pixel look and
  a third cycle.
- **TIC 278774793** (giant, G 11.6, P 58.12 d, 33 sectors): the stacked fold
  dips about 10 ppt for about 5 d just after B; a 96-h box at B + 1.7 d gives
  23 to 31 ppt in 6 of 12 covered cycles and under 6 ppt in the other 6. Nine
  times the predicted 2.8 ppt and absent in half the cycles, so not an eclipse
  as it stands. Candidate for a dedicated look.

## Why the yield is low, and it is not the box cap

- **Giants.** Every window sat at the 7-d cap (t_peri errors 1 to 2 d over
  60 to 150 cycles), so +-7 d on a 20 to 58 d period is a quarter to two
  thirds of the orbit. These stars carry 10 to 70 ppt deficits on 2 to 4 d
  timescales everywhere, so raw box SNRs run to hundreds and only the
  off-window null and a same-conjunction repeat carry information. The rms of
  the box depth at the predicted duration exceeds half the predicted 2 to
  13 ppt depth for 25 of 29: a single eclipse of the predicted depth would
  not stand out. The 0.1 found-to-expected is the stars' variability against
  the predicted depths, not the 14-h cap.
- **Dwarfs.** QLP's detrended column (KSPSAP) flattened both real eclipses to
  0.1 to 0.3 ppt in several sectors where SAP shows 4 to 6 ppt; a search on
  the detrended column under-counts 10 to 20 h shallow eclipses by
  construction. The SAP pass pays for it with gap-edge ramps: the first pass
  produced six false 14-h "eclipsers" there, removed by a 0.25-d trim at every
  gap and a 60% sideband-coverage rule. Which column the original fresh-band
  search used would tell how much of the 0.4 is this.
- Sector 100 and later QLP mid-times are uncorrected (the clock fault); flagged
  in both tables, detection unaffected.
