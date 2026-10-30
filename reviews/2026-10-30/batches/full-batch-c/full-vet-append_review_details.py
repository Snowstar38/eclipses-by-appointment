from pathlib import Path
import json,math
F=Path('C:/Home/Astra/made/binary-handoff-2026-10-30/full-batch-c/full-vet'); controls={'158545440':.11,'339787086':2.17,'341432079':.30,'144749615':2.83,'304033253':.61,'117919258':.23,'97509220':3.43,'148618714':1.60,'266540667':.64,'285145433':.18}
for i,v in controls.items():
 p=F/i/'REPORT.md';s=p.read_text(encoding='utf-8');s+=f'\n## Final adversarial review details\n\nThe largest positive off-phase fixed-template control depth was {v:.2f}ppt. Controls calibrate low-frequency/modulated residuals; they are not an exact multiple-trial probability for the optimized secondary. '
 if i=='97509220':s+='The3.43ppt control exceeds the candidate1.80ppt secondary, so no secure secondary or geometry derived from that candidate is claimed. Primary-only EB classification rests on the repeatability, pixels, independent TARS reduction and RV companion. '
 elif i=='117919258':s+='The0.23ppt control is well below the2.68ppt secondary; both individual events support it, but their two-event span cannot provide an independent secondary period. '
 else:s+='The repeat secondary signal is stronger than the off-phase controls and recurs in multiple sectors. '
 if i=='339787086':
  r=json.load(open(F/i/'fit-results.json'));ep=r['ephemeris'];k=(4343.5-ep['Tref'])/ep['P'];sig=math.hypot(ep['Tref_error'],k*ep['P_error']);s+=f'\n\nThe photometric versus Gaia SB2 period discrepancy is4.46sigma under the quoted uncertainties. Primary chi2/dof1796.6/20 and sector-coherent O-C of roughly-9 to+10min demonstrate limitations of a single linear ephemeris and its formal timing errors. At2026-10-30 the propagated formal linear timing scale alone is about{sig*1440:.1f}min; it is not a complete predictive error. Use at least +/-0.05d (72min) around a nominal prediction as a provisional observing search window, not a calibrated confidence interval or guarantee; further timing evolution may require more. The target is confirmed as an EB; the exact connection of all eclipses to the published SB2 orbital parameters remains imperfect, and the281-day astrometric-orbit association remains unestablished. '
 p.write_text(s+'\n',encoding='utf-8')
(F/'NEXT-BATCH.md').write_text('''# Batch C reproducibility and reuse

Ten reviewed targets; all physical CONFIRMED, with separate incomplete novelty bibliography. Reports carry explicit reviewed reasons, rather than inheriting automatic verdicts. Data manifests and detailed outputs are complete. No source status edits or commits.

Portable calculations reuse A rawSAP event, ephemeris, phase-control and geometry primitives after per-source checks. C adds validated SB2 covariance layout (bit255, seven parameters,21 correlations) for339787086; never select its separate280.99d Orbital row as the eclipse RV orbit. Its measured SB2 dynamical minima in sb2-dynamics.json supersede the TIC-M1/SB1 surrogate. Secondary fitted phases are conditional and97509220's optimized peak fails controls. Geometry fixed dimensions/free scales cannot produce precise component claims, especially339787086.

Targeted pixel_selective.py compares all fresh Gaia G<15 sources in old hashed TESScut cubes for97509220 and341432079, resolving capable-neighbour ambiguity. Expanded sigma grid avoids975's original boundary. Gaussian PSF/systematics prevent calibrated significance. Prior diffimg was sufficient elsewhere; old/new schema duplicate records are one measurement.

Terra bulk-summary and BULK-NOTES document independent full49QLP analysis and all10 independent reductions (9SPOC/TESS-SPOC,1TARS). Catalogue note and raw IDIA receipts retain fresh nine-table results. Write reviewed reports with write_reviewed_reports.py, then apply append_review_details.py to restore explicit control and prediction addenda. All FITS are under ignored data/.
''',encoding='utf-8')
print('appended10review addenda')
