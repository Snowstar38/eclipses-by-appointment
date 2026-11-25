# 154 more mixed-method TESS leads

One eclipsing binary enters the catalogue from this review. **TIC 257808672** is a previously machine-flagged variable whose light appeared in the aperture of TIC 257808668. TESS resolves two eclipse families, and independent ground observations of the neighboring star recover both at the predicted times. We also recovered two earlier eclipse identifications and identified five asteroid crossings. [Host record](host-257808672.md) · [All 154 dispositions](outcomes.csv)

## An eclipsing binary in the neighboring aperture

Every one of 16 covered primary predictions showed a dip on a **3.19798973-day** clock in TESS sectors 55 and 82. Both eclipse families localize to the same neighbor, about 37 arcseconds from the nominated star. Its light also varies smoothly between eclipses, with a shape that changes from one sector to the next. [Separated TESS light curves](batch07/plots/257808668-neighbor-fold.png) · [Individual image measurements](batch07/neighbor-windows.csv)

ZTF resolves the neighboring star. We used the TESS period and epoch directly and fitted the broad modulation outside the eclipse windows. The median primary losses were 0.302 mag in green and 0.221 mag in red. The shallow secondary was also present in both bands, at 0.044 and 0.046 mag. Earlier work classified the source as a rotational or RS CVn variable, and Kostov et al. listed it as a machine eclipse candidate. The catalogue entry credits that history. [Ground-based light curves](ground/257808672-ztf.png) · [Measurements and cycle counts](ground/257808672-ztf.csv) · [Prior classifications](credit/donor-257808672/README.md)

## Five asteroids in four stellar apertures

Two apparent brightenings of **TIC 186817099** were separate crossings by **(4613) Mamoru** and **(16431) 1988 VH1**, about 42 days apart. Three other fields caught **(740) Cantabia**, **(914) Palisana** and **(2850) Mozhaiskij**. JPL tracks calculated from the spacecraft agree with all 153 sampled positions to within six arcseconds. For Palisana, the orbit comparison ruled out a much fainter asteroid that passed close to the measured position at one instant. A separate sector 45 event in the Mozhaiskij field remains unresolved. [Watch both crossings of the same field](followup/motion-186817099-pair.gif) · [All five tracks and observing dates](followup/motion-README.md)

## Two known eclipse sources

**TIC 120239458** shows a deep eclipse and a shallow eclipse 6.76222 days later. Théo Chopard-Vilhem's pilot had already identified the deep event. Using the full Gaia orbital covariance, we find that the eccentric 43.286-day orbit predicts 6.773 days between conjunctions, with a central 68% interval of 6.577–6.973 days. Two further TESS sectors nominally include the coordinates but place the star off the illuminated detector. [Two-minute light curves](batch16/120239458-two-eclipses.png) · [Orbital geometry and prior credit](batch16/gaia/README.md) · [Detector coverage](batch16/120239458-sector-coverage.png)

**WHAT236 5760 (TIC 298262982)** has a deep, broad eclipse that QLP correction almost removes. The complete sector 24 eclipse matches an ingress 48 cycles later. At that TESS-derived period of about 30.80065 days, independent ASAS-SN observations recover the loss across 20 green-band and seven V-band cycles. [Eclipse and ground predictions](batch16/298262982-eclipse.png)

## Coverage and triage

We reviewed 100 multi-sector dip leads, 30 brightening leads and 24 single-sector dip leads using 1,408 original target-sector QLP files. The final four were chosen by the depth of the original dip. This brings individual reviews of the original 2,904-target pool to **754**, leaving **2,150**. These deliberately selected groups do not estimate sky-wide occurrence rates. An independent early-to-late TESS period search flagged ten repeating signals, several with broad continuous modulation. Fixed-phase ASAS-SN or ZTF tests had usable series at 149 of the 154 nominated positions. Shallow signals and sparsely covered events remain open where the data cannot settle them. [Roster and selection ranks](roster.csv) · [Later-sector tests](independent/later-repeats.csv) · [Ground checks](ground/fixed-windows.csv)

The shorter 798-source comparison missed Chopard-Vilhem's pilot flag. We consequently searched text members of six available survey releases for the exact identifiers of all 154 targets and the resolved neighbor. Fifty-five of the nominated targets have an identifier in those files, often in broad processing or control lists. TIC 120239458 has an explicit prior eclipse flag. [File-by-file comparison](credit/survey-archive-matches.csv) · [Archive checksums](credit/survey-archives.json)

**Individual reports** · [01](batch01/README.md) · [02](batch02/README.md) · [03](batch03/README.md) · [04](batch04/README.md) · [05](batch05/README.md) · [06](batch06/README.md) · [07](batch07/README.md) · [08](batch08/README.md) · [09](batch09/README.md) · [10](batch10/README.md) · [11](batch11/README.md) · [12](batch12/README.md) · [13](batch13/README.md) · [14](batch14/README.md) · [15](batch15/README.md) · [16](batch16/README.md)

[Archive inputs and reproduction instructions](inputs/README.md) · [Public download replay checks](inputs/replay-qa.txt)
