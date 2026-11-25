# Paired review of the remaining 402 Fable candidates

The review covers all 402 remaining TIC apertures from the earlier [Fable shortlist](../2026-11-24-fable-shortlist/README.md). It adds 9 physical hosts, including 6 confirmed and 3 probable systems. The [host measurements](host-stars.csv) give the period, epoch, eclipse depth, attribution and limits of each addition.

| Outcome | Apertures |
|---|---:|
| Confirmed addition | 6 |
| Probable addition | 3 |
| Previously reported eclipse or eclipse candidate | 26 |
| Identified non-eclipse explanation | 5 |
| Unresolved signal or host | 100 |
| Insufficient eclipse evidence | 262 |

## Per-star evidence

The [402 decisions](adjudications.csv) join the [batch assignments](batches.csv), the [sector-by-sector photometry](sol/sector-measurements.csv), the [visual reviews](terra/visual_readings.csv), and the [image fits](source-screen.csv). The first 40 batches contain ten apertures each. The final batch contains two. Visual plot paths in the decision and reading tables are relative to the `terra` directory.

Sol measured the trial primary, secondary and alternating minima in individual sectors using both SAP and PDCSAP. Terra inspected Fable’s saved folds and the new sector plots. The plotted trial period can differ from the final orbital period. In selected fields, individual deep events suggested an alternative clock. The [corrected-clock fits](sol/recovered-clocks) record which predicted events fell in observed windows, including windows without a dimming. The [independently timed eclipses and phase-specific images](reclocked) test those clocks.

The [pixel records](pixels) give the archive URL and FITS hash, individual events, Gaia source comparisons and nearby stars bright enough to supply the signal. A source can produce a sharp phase-folded eclipse in a neighbouring aperture. The [neighbour identifications](alternate) and [survey data](ground-final) record those distinctions. Source checks include [earlier linear-period and harmonic matches](credit/wide-clock-matches.json), [Gaia and prior lists](credit/all-sources.json), [NASA and ExoFOP candidate tables](credit/planet-archive-matches.json) and [individual target bibliographies](credit/individual). The source checks are limited to the named catalogues and archived measurements.

## Earlier identifications and the recovered clocks

Two TESS apertures also had independent Kepler/K2 observations. Dolorous_Edd reported EPIC 248459053 (TIC 277876971) as a detached eclipsing binary at 16.766 days on September 2, 2017. The TESS ephemeris predicts both families in the Campaign 14 observations. [Planet Hunters discovery post](https://talk.planethunters.org/boards/BPH0000007/discussions/DPH0001l5s/#59ab45e5b94190007100026d) · [K2 measurements](k2/277876971.json).

David Canal Vallina listed EPIC 212004082 (TIC 184916459) at 25.81 days in Table A.2 of the Universidad de Oviedo Campaign 18 thesis, with detached eclipses and rotational variability. TESS, K2 and ASAS-SN recover the eclipses. [Original thesis](https://digibuo.uniovi.es/dspace/bitstream/handle/10651/60643/TFM_DavidCanalVallina.pdf?isAllowed=y&sequence=4) · [K2 measurements](k2/184916459.json).

For TIC 423355654, two TESS visits caught the same unequal eclipse pair. Their 760.24-day separation admitted many integer cycle counts. ASAS-SN and ZTF independently favor 38 cycles, giving a 20.0062-day period. Both eclipse images in both sectors locate the dimming on TIC 423355654. [Folded TESS and ground photometry](sol/panels/recovered-clocks/423355654-ground.png) · [Integer-cycle test](alias-ground-423355654.json).

## Triage comparison

The original ranks and inputs for all 402 were frozen before adjudication. The [analysis plan](study/analysis-plan.md) defines three rankings and review budgets of 23 and 100. The [comparison](study/review-budget-yield.csv) counts unique catalogue additions and previously identified eclipses separately. Unresolved and insufficient cases stay in the denominator for the yield of this review. Their underlying eclipse status remains open.

The original [features and ranks](study/frozen-features.csv), [per-feature counts](study/feature-yield.csv), and [full cumulative curves](study/cumulative-yield.csv) are available for reuse. Recompute the tables with `python study/evaluate.py adjudications.csv` from this directory. This cohort had already passed earlier selection and follow-up was deeper for interesting signals. Estimates apply to this remaining shortlist.
Read the [triage results and interpretation](study/README.md) or view the [cumulative yield plot](study/triage-yield.png).

A separate [exploratory test of deep dips in the saved folds](study/exploratory-fold-discrepancy.md) examines a clue noticed during follow-up. The exact [original inputs](fable-inputs) and [offline verification script](audit.py) are included.
