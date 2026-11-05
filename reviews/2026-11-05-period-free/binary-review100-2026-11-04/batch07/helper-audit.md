# Independent helper audit — batch07

I inspected raw-window panels and final rows for all ten IDs, and directly checked H066, H067 and H070. RESULTS has exactly H061–H070, with queue TICs matching, UNKNOWN catalogue statuses, and no unsupported photometric period or epoch. H066/H067 PLAUSIBLE and eight flag-specific REFUTED results are consistent with the reviewed morphology; these do not negate Gaia spectroscopic binaries or unrelated events.

H066 sector 19: 169 quality-zero points within two days of BTJD 1820.9536 show a roughly symmetric 1.3 ppt SAP depression. It is suppressed in KSPSAP; after linear time detrending SAP and centroid X correlate r=0.504, but suppression and correlation do not prove an instrumental cause. H067 sector 94: 1055 quality-zero points in the corresponding window have time-detrended flux–X correlation 0.563; background correlation falls from 0.369 to -0.061 after time detrending. A gap, changing baseline and pointing association make a systematic credible, but do not prove it. Retaining PLAUSIBLE is appropriate. New-sector cutouts are insensitive to a shallow event and cannot refute recurrence.

The WCS positions of H066 and H067 in their independently downloaded 5x5 new-sector cutouts are (2.192, 2.748) and (2.536, 2.780), respectively, zero-indexed. These establish target placement in those cutouts; they do not localize the original-sector events. Numeric correlations, positions and independent source and cutout hashes are in helper-audit-numeric.json, reproducible with helper-audit.py.

H070 direct inspection: quality-zero SAP was 0.002096 at BTJD 2911.829757, rose to about 0.57 at the flagged 2912.311235 and reached 0.99084 by 2914.142238. The alleged dip lies on this recovery, not at a local minimum; no >0.02 d gap exists in the checked quality-zero sequence. The raw-window plotting script skipped this flag for insufficient side samples, so its absence from the plot is not evidence. helper-h070.py reads the direct FITS values.

H061 and H069 reports pair background and centroid changes with flux-level and gap evidence, not common-mode counts alone. H063 shows a gap-crossing step and slow recovery. Catalogue UNKNOWN remains separate from physical interpretation. No independent aperture attribution is claimed for a confirmed eclipse.

