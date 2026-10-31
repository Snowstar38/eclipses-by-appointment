import pathlib,json,csv,hashlib,math
import numpy as np
O=pathlib.Path(__file__).parent;T=json.load(open(O/'timing-results.json'));G=json.load(open(O/'geometry-results.json'));TG=json.load(open(O/'catalogues/targets-selected.json'));B=json.load(open(O/'band-results-72.json'));F=[json.loads(l) for l in open(O/'fresh-results-96.jsonl')]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
keys=['167178300','325573958','155303130','382042754','389128842'];rows=[]
for k in keys:
 w=O/k;t=T[k];g=G[k];p=json.load(open(w/'diff_pilot.json'));good=[e for e in t['events'] if e['reliable_for_fit']];sep=21*np.linalg.norm(p['deficit_minus_target_px']);sid=TG[k]['gaia']['source_id'];nb=[r for r in p['neighbours_60'] if r['possible'] and r['source_id']!=sid];band=k in keys[:2];known=k=='155303130';kind='B' if known else 'A';verdict='PROBABLE' if band else 'CONFIRMED';method='Gaia period fold / 12-14.8d selection-gap recovery' if band else 'fresh Gaia-conjunction appointments G11.5-12 P20-60d'
 limitations=('Capable Gaia neighbours remain at '+', '.join(str(r['sep'])+'arcsec' for r in nb)+'. Deficit centroid favors target, but close blend is unresolved without a PRF/deblend uncertainty test.' if band else 'Pilot characterization; period errors are scatter-only. No exhaustive literature priority claim.')
 novelty='known IJspeert2024 EB recovery; zero new-system addition' if known else 'no prior EB identified in seven scoped groups; cachedChopardv1.2.0 exact IDs no overlap; laterreleases/embargo93 unknown'
 bandnote=' The band pilot tests underreviewed/threshold-selected outcomes; the original SB1 fold already searched this period range, so these are not recoveries from an SB1 veto.' if band else ''
 epochnote=' This reference epoch is extrapolated from the fitted sector33/72 timings, not a directly fitted eclipse at BTJD1479.' if k=='167178300' else ''
 text=f'''# TIC {k}: {verdict}

Scientific method/population: {method}. Physical review completion: complete bounded first pass, independently audited in [helper/AUDIT.md](../helper/AUDIT.md); supervisor admission pending.{bandnote} Catalogue novelty is separate: {novelty}.

1. Repeated raw eclipses: PASS. {len(good)} fit-eligible raw SAP events in sectors {sorted(set(e['sector'] for e in good))}. Trapezoid depths median {np.median([e['depth_ppt'] for e in good]):.2f} ppt; duration median {np.median([e['duration_h'] for e in good]):.2f} h. All saved events, rejected fits and raw files are identified in timing-results.json; no claim that other sectors are clean nulls. QUALITY==0 used. Existing raw observations were remeasured, not merely called eclipses from BLS.
2. Eclipse timing: PASS. P={t['period_days']:.10f} d; {kind}-eclipse reference epoch BTJD {t['epoch_btjd']:.8f}; OLS scatter SE {t['period_scatter_se_days']:.9g} d; residual RMS {t['timing_rms_minutes']:.3f} min.{epochnote} This SE excludes cadence/template/extraction systematics and is not calibrated coverage. Fits are representative, not all-event precision ephemerides.
3. Target pixels: {'UNCERTAIN' if band else 'PASS'}. Sector {p['sector']}, {p['n_events']} event stack, peak pixel {p['peak_deficit_px']} equals target {p['target_pixel']}; centroid-target {sep:.2f} arcsec. {len(nb)} distinct Gaia neighbours could supply the flux under the conservative total-flux bound. {'Close neighbours prevent an unqualified target identification; nearest-target centroid supports but does not settle it.' if band else ('The marginally capable neighbour at32.394arcsec is spatially distinct from the1.51arcsec target-centered deficit; it is not discarded merely because it is faint.' if known else 'All distinct Gaia neighbours within 60arcsec are too faint under the conservative bound.')} Catalogue incompleteness/unresolved companions are not excluded. Gaia position used consistently with target ID. The older diffstack n_possible field includes the target itself; this report explicitly removes it.
4. Alternative reduction: PASS as a processing check. Own TESScut extraction using median faint-pixel background and target 3x3 aperture reproduces deficit {p['depth_ap3']*1000:.2f} ppt. The difference-stack receipt records per-event aperture depths. These are the same TESS photons, not an independent observing occasion; dilution/apertures explain differing QLP depths.
5. Gaia geometry: PASS for consistency, not a precision solution. Eclipse P differs from Gaia by {g['eclipse_period_difference_sigma']:.3f} quoted Gaia period errors. {kind}-conjunction epoch difference {g['conjunctions'][kind]['offset_sigma']:.3f} propagated marginal-error sigma. Gaia mass function {g['mass_function_solar']:.4f} solar masses, minimum companion mass {g['minimum_companion_mass_solar']:.3f} solar masses for TIC primary mass {g['primary_mass_TIC']:.3f}. TIC R1={g['primary_radius_TIC']:.3f} solar radii. Illustrative edge-on R2=1solar-radius duration at this conjunction {g['illustrative_central_duration_hours'][kind]:.2f} h, longer than observed; impact/inclination can shorten it. This is an existence/consistency check, not a fitted mass-radius claim. Correlated Gaia errors were not modeled; no arbitrary sigma veto.

Seven catalogue groups: fresh VSX60arcsec, ASAS-SN60arcsec, SIMBAD exactGaiaDR3, Gaia vari_eclipsing_binary exactID, Prsa2022 5arcsec, IJspeert2024 5arcsec, vetted Kostov2025 tables3+4 5arcsec all returned successful receipts. {'IJspeert contains exactTIC/Gaia. VSX DSCT and ASAS-SN ROT: classify the same star differently; its eclipses were already published.' if known else 'No on-target EB match in this bounded scope. Any VSX/ASAS-SN neighbour is retained as attribution evidence, not mistaken for target identity.'} Full rows, UTC queries and response hashes are in [catalogue coverage](../catalogues/coverage-matrix.csv). The latter two Kostov tables form one group. No external messaging or public/paper edits.

Limitations: {limitations}
Next check: {'Pixel/PRF assessment against capable neighbours before any confirmed admission; supervisor review.' if band else 'Supervisor review before admission; independent helper audit completed.'}

Lead audit: scripts inspected and deciding numeric outputs reconciled with raw SAP plots, full Gaia NSS metadata, source IDs and real TESScut pixels. Apparent failure/non-detection is not called physical refutation unless contrary evidence is present. Independent [helper audit](../helper/AUDIT.md) uncertainty caveats are retained. The helper verified deciding artifacts, not an exhaustive literature search.
'''
 (w/'REPORT.md').write_text(text)
 receipts=[w/'diff_pilot.json',w/'gaia.json',O/'timing-results.json',O/'geometry-results.json',w/'REPORT.md',w/'diffstack-local.py',w/f"tesscut_s{p['sector']:03d}.fits"]
 (w/'deciding-hashes.json').write_text(json.dumps({str(x.relative_to(O)):sha(x) for x in receipts},indent=1))
 rows.append({'tic':k,'physical_verdict':verdict,'full_review_completion':'complete bounded first pass; independent helper audit completed','period_days':t['period_days'],'period_error_days':t['period_scatter_se_days'],'primary_epoch_btjd':t['epoch_btjd'] if kind=='A' else '', 'depth_ppt':float(np.median([e['depth_ppt'] for e in good])),'limitations':limitations,'next_check':'supervisor review; source deblend for band cases','source_report':str(w/'REPORT.md'),'report':str(w/'REPORT.md'),'scientific_method':method,'novelty_status':novelty,'epoch_btjd':t['epoch_btjd'],'epoch_kind':kind,'period_error_meaning':t['error_meaning']})
with open(O/'RESULTS.csv','w',newline='') as fo:
 wr=csv.DictWriter(fo,fieldnames=list(rows[0]));wr.writeheader();wr.writerows(rows)
# Attempt ledger: unique scientific targets in each pilot; category overlap stays explicit.
ledger=[]
for r in B:
 k=r['tic'];goods=[e for e in r['events'] if np.isfinite(e['snr']) and e['snr']>8 and .6<e['far']<1.6 and e['halves']]
 outcome='screen does not establish repeated raw eclipse; not a clean null'
 if k in ['167178300','325573958']:outcome='probable target EB; close-neighbour ambiguity'
 elif k in ['21411263','73023909','176048490']:outcome='existing c8-screened EB recovery; not new pilot discovery'
 elif k=='403769569':outcome='off-target eclipse; positive contrary pixel evidence (35arcsec offset)'
 elif k in ['301838765','342301761']:outcome='non-eclipse variability/alias; threshold coincidences not coherent eclipses'
 ledger.append({'category':'band','id':k,'availability':str(len(r['files']))+' cached sectors','outcome':outcome})
for r in json.load(open(O/'availability-summary.json')):ledger.append({'category':'new-sector repeats','id':r['tic'],'availability':json.dumps(r.get('sectors',r.get('error'))),'outcome':'no sectors beyond historical cache; no photometric new-repeat test'})
for r in json.load(open(O/'long-results.json')):ledger.append({'category':'long-duration ceiling','id':r['tic'],'availability':r.get('path',''),'outcome':'no secure repeated long eclipse; broad variability/ramps/steps dominate; some weak single depressions remain unexplained; duration-grid statistic alone insufficient'})
selection=json.load(open(O/'fresh-preregister-96.json'))['selected'];byid={v['gaia']['source_id']:k for k,v in json.load(open(O/'fresh-targets-96.json')).items()};fr={r['tic']:r for r in F}
pending={'267620340','307803633','452066647','274642438'}
for g in selection:
 k=byid.get(g['source_id']);r=fr.get(k,{})
 if not k:out='no exact TIC Gaia-ID match; retained as unavailable'
 elif r.get('err'):out='unavailable: '+r['err']
 elif k in ['155303130','382042754','389128842']:out='confirmed EB known recovery' if k=='155303130' else 'confirmed physical EB; seven-group scoped novelty negative'
 elif k=='119484185':out='short-period EB unrelated to Gaia41d; not appointment EB'
 elif k in pending:out='uncertain broad/complex dip; no secure Gaia-orbit eclipse; not counted'
 else:out='bounded screening did not establish eclipse; no completeness or clean-null claim'
 ledger.append({'category':'fresh appointments','id':k or 'GaiaDR3 '+g['source_id'],'availability':str(r.get('nsec','unmatched'))+' usable selected sectors','outcome':out})
with open(O/'ATTEMPTS.csv','w',newline='') as fo:
 wr=csv.DictWriter(fo,fieldnames=['category','id','availability','outcome']);wr.writeheader();wr.writerows(ledger)
freshtg=json.load(open(O/'fresh-targets-96.json'));downloads=json.load(open(O/'fresh-downloads-96.json'));summary={'band_science_targets':len(B),'band_raw_windows':sum(len(r['events']) for r in B),'new_sector_availability_queries':8,'long_duration_targets':16,'fresh_selected_science':len(selection),'fresh_control_selected':0,'fresh_TIC_matched':len(freshtg),'fresh_QLP_available':sum(bool(v['qlp']) for v in freshtg.values()),'fresh_execution_rows':len(F),'fresh_with_usable_sectors':sum(r.get('nsec',0)>0 for r in F),'fresh_download_jobs':len(downloads),'fresh_download_unavailable':sum(r['status']=='unavailable' for r in downloads),'fresh_known_recoveries':1,'fresh_strong_candidates':2,'band_probable_candidates':2,'unexecuted_extension_science':48,'attempt_rows_by_category':{c:sum(r['category']==c for r in ledger) for c in set(r['category'] for r in ledger)}}
(O/'summary.json').write_text(json.dumps(summary,indent=1));print(summary)
