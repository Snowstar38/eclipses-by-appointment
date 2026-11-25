# Ground tests of ten archived fold predictions

The ground archives yielded 12,179 usable measurements across nine of the ten apertures. The original TESS period, epoch and box width were held fixed for each star. None passed the independent ground test. Three targets had enough cycles and off-phase controls in at least one filter for the full test. The other seven had insufficient coverage, including one with no archive measurements. Even the three complete tests can miss shallow eclipses. [Ten individual outcomes](outcomes.csv) · [Ground measurements around the predictions](archived-predictions.png)

For TIC 135180054, the original screening box predicted a 646-parts-per-thousand loss. Five ASAS-SN g observations sampled its tested core over three cycles. Their median after equal weighting by cycle was 0.016 mag brighter than baseline. The single V point was within 0.003 mag of baseline. Those observations fail to reproduce a deep eclipse at the archived times. The clock was measured from sparse TESS sampling, so the test leaves other epochs open. Across the ten targets the three supplemental ephemerides per star also returned no passing tests. These were the other archived half-period solution, its TESS-only phase refit, and the Gaia period anchored at the original TESS epoch. [Original inputs and hashes](archived-clocks.csv) · [Supplemental timing hypotheses](other-tess-clocks.csv) · [All filter and ephemeris results](phase-checks.csv)

## Coverage and method

The ZTF g and r query used a 2.16-arcsecond radius. TIC 347447876 returned 196 raw rows and the remaining nine requests returned empty tables. ASAS-SN Sky Patrol returned 14,055 rows at nine of the ten positions using a four-arcsecond master-list search. TIC 244201152 was absent in both cones. The ASAS-SN light curves use wider photometric apertures, so the measurements can include neighboring sources. [ZTF queries and hashes](receipts.json) · [ASAS-SN queries and hashes](asassn-receipts.json) · [ZTF API](https://irsa.ipac.caltech.edu/docs/program_interface/ztf_lightcurve_api.html) · [Sky Patrol photometry](https://asas-sn.github.io/skypatrol/additional.html)

We used quality-zero ZTF points and good-quality ASAS-SN detections with magnitude error between zero and 0.2 mag. We subtracted a separate median for each object, filter and ASAS-SN camera with at least 15 points. Each tested object and filter needed at least 30 retained points. ZTF mid-exposure UTC was converted to barycentric TDB at Palomar. For ASAS-SN we used the supplied JD minus 2,457,000 as an approximate time coordinate. We repeated the tests with the predicted centers shifted by ±0.008 day to check sensitivity to the time convention.

The core spans ±0.36 of the full TESS box width, capped at ±4% of a cycle. We took the median magnitude change in each observed cycle and then the median across cycles. Support requires four sampled cycles, a dimming at least three times the largest of 0.005 mag, the median formal error and robust full-series scatter, and a deeper median than at least 95% of usable shifted phases. We tested 100 evenly spaced phase shifts and required at least 40 usable comparisons with at least three sampled cycles each. All summary classifications refer to the original TESS prediction. Timing errors, observing gaps and blending can reduce recovery. The figure displays one day around each archived center with a shared vertical scale, and retains the measurements outside the plotting limits in the underlying tests.

An exploratory test fixed the period at the catalogued Gaia value and the width at the archived TESS width. It selected the deepest of 256 evenly spaced phases in the earlier half of each ground series, requiring four sampled cycles there. It then tested that phase once on the later half using the same controls. Nine series from five targets supported a training-phase choice. None passed in the independent time interval. [Chronological holdout](ground-holdout.csv)

## Replay

Run the commands below in this directory, substituting a writable local cache path. Requirements are NumPy, pandas, Requests, Astropy, Matplotlib and pyasassn. ASAS-SN also requests citation of Shappee et al. and Kochanek et al. for uses of its light curves. [Survey acknowledgements](https://www.astronomy.ohio-state.edu/asassn/public/)

```sh
python fetch.py CACHE
python asassn.py CACHE
python check.py CACHE --extra other-tess-clocks.csv
python plot.py CACHE
```
