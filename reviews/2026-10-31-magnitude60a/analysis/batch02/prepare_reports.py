from pathlib import Path
b=Path('[local path omitted]')
s=(b.parent/'batch01/write_reports.py').read_text()
a=s.index('special={');z=s.index('for q in csv.DictReader',a)
special={
'129565419':'Remote bright region dominates historical unrestricted peak and PSF residual0.968. Independent helper local5x5 re-stack residual0.115 and target centroid offset(-0.02,+0.01)pixel recover the target eclipse; three aperture depths24.40/23.92/22.14ppt support it. Capable neighbor38.91arcsec away lies1.90pixel from original deficit vs0.040pixel target.',
'125690413':'Structured sector41 baseline gives broad34ppt cycle196, residual -0.038d and reduced chi square5.25. Retained event and inflated covariance document this; clean22ppt repeats occur in sectors15/55. Capable neighbors are24.35arcsec or farther,1.55pixel or farther from deficit vs0.371pixel target. Timing errors are not total uncertainty.',
'445045766':'No capable catalogued neighbor within60arcsec. Deficit0.186pixel from target; three alternative aperture depths23.3-23.9ppt agree.',
'120037640':'Actual-epoch Gaia offset -0.189d (phase -0.051) exceeds historical phase screen; near Gaia reference projected offset is +0.045d. Gaia period uncertainty accumulates over baseline. Low eccentricity0.062 and recurrence agreement support association without arbitrary sigma veto. Capable neighbors are34.9arcsec or farther and1.72pixel or farther from deficit vs0.178pixel target.',
'448485777':'Crowded field: G13.14 neighbor16.26arcsec away requires16.1% eclipse, deficit0.615pixel from neighbor vs0.252pixel target. Another14.44arcsec neighbor requires97.6%. Target is favored by central deficit and deeper1x1 aperture, but blending and uncalibrated localization leave attribution physically unresolved after completed checks.',
'158647370':'No capable catalogued neighbor. Approximately85-95ppt eclipses repeat; custom aperture depths85-87ppt agree.',
'302190527':'No capable catalogued neighbor. Approximately275-283ppt raw eclipses repeat across widely separated sectors; alternative aperture depths255-263ppt are diluted extraction values.',
'138941853':'Approximately8-10ppt eclipses repeat in sectors6/32/98. Deficit0.087pixel from target vs nearest capable source1.127pixel. Near-reference Gaia offset0.352d is descriptive; low-eccentricity orbit conjunction is poorly constrained. Actual epoch offset0.036d with0.524d propagated Gaia uncertainty is compatible.',
'256665207':'Approximately6-7ppt flat-bottom eclipses repeat. No compelling even/odd split establishes half/double alias; full Gaia period agrees with recurrence. Nearest capable source32.78arcsec away,1.70pixel from deficit vs0.166pixel target.',
'91628894':'Deficit0.377pixel from target; light-centroid shift1.05arcsec is a different quantity. Nearest capable source19.20arcsec away requires38.1% eclipse and lies0.675pixel from deficit. Central lost-light peak and consistent10ppt aperture depths favor target; no calibrated subpixel uncertainty is inferred.'}
s=s[:a]+'special='+repr(special)+'\n'+s[z:]
s=s.replace("tic=='428691463'","tic=='448485777'")
s=s.replace('reference eclipse epoch BTJD','fitted ephemeris intercept at earliest retained cycle BTJD')
(b/'write_reports.py').write_text(s)
