# Independent helper audit, batch 06

The lead's raw-window contact sheet was examined for all ten selected rows. H051, H052, H054, H057 and H058 show broad trends or discontinuities in the retained windows; H056 is a short dip amid rapid variability. These appearances describe the screened windows, not every possible astrophysical signal. H053, H055 and H059 share a time-coincident sector 94 trough, measured independently below. H060 required pixel-level inspection.

## S94 shared morphology

`helper-common-s94.py` reads and SHA256-hashes each original raw SAP FITS, selects quality zero, normalizes to BTJD 3872–3873.5, and takes 0.1-day median bins. The three pairs have 48 jointly populated bins and Pearson correlations 0.899, 0.991 and 0.909, respectively; `helper-common-s94.json` contains hashes and `helper-common-s94.png` the comparison. The synchronized morphology across widely separated targets is positive evidence for a shared systematic origin of these selected dips. It does not exclude other events elsewhere.

## H060 pixel context

The WCS target is at (5.133, 5.873) on the sector-23 cutout; a bright image is centered there, confirming measurable target flux in this cutout. `helper-h060-difference.py` compares 38 quality-zero cadences BTJD 1933.0–1933.8 with 52 at 1934.1–1935.2. The signed difference shows a strong central positive signal with negative adjacent pixels, consistent with image motion/redistribution, not a clean PSF-scaled disappearance. This diagnostic has no pointing or background model and does not localize an astrophysical source. Lead's QLP alternate reduction suppresses the trough; centroid drifts and the baseline is interrupted by a gap. Together these supply positive contrary evidence against interpreting the selected trough as a secure eclipse; they cannot rule out a real stellar eclipse or binarity in general. The alternate reduction and cutout use the same observing occasion. No Gaia-neighbor source attribution is claimed from these data.

The catalogue status remains UNKNOWN for every row, per campaign guidance. No separate network fetch was made.

## S96 shared morphology and final-row review

Independent 0.1-day quality-zero bins from BTJD 3923–3929 give Pearson r=0.9755 for H052 and H057 across 58 paired bins; `helper-common-s96.py`, `.json`, and `.png` preserve the comparison and FITS hashes. Shared timing and shape is direct contrary evidence for their selected troughs. H054 was included as a comparison and has weaker correlation; its own gap/reset evidence is separate. The ten final rows were checked for identities, UNKNOWN novelty, and unsupported timing fields. The lead was asked to cite this comparison and describe H060 using the full pixel redistribution evidence, without treating detrending alone as decisive.
