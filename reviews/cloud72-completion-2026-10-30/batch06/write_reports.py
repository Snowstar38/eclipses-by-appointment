from pathlib import Path
import csv,json,hashlib
B=Path(__file__).parent;D=B.parent;R=B/'raw-evidence';T=json.load(open(B/'targets-selected.json'));Q={r['tic']:r for r in csv.DictReader((D/'queue.csv').open())};C=json.load(open(B/'catalogue-scope.json'));A=json.load(open(B/'decisions.json'));G=json.load(open(B/'gaia-geometry.json'));raw=json.load(open(R/'raw-events.json'));cov=json.load(open(R/'predicted-coverage.json'));pix=json.load(open(R/'pixel-results.json'));N=json.load(open(R/'neighbour-results.json'));rows=[];(B/'reports').mkdir(exist_ok=True)
for tic in T:
 a=A[tic];g=G[tic];coverage=[v for v in cov[tic]['nominal_tests'] if v['covered']];nr=[v for v in N if v['tic']==tic];src=[v for v in pix if v['tic']==tic];p=B/'reports'/f'{tic}.md'
 text=f'''# TIC {tic}: {a['verdict']}

Queue position {Q[tic]['queue_position']}; batch06. Review credits: GPT-6.1 Sol, fresh GPT-6.1 Terra review, supervised by Astra. This is AI review, not human validation.

1. Raw morphology and repeat assessment

{a['assessment']}

Three cached QLP SAP_FLUX FITS sectors were checked with QUALITY=0 and target/sector header verification. Local quadratic baseline plus trapezoid fits are in raw-events.json, including failed or boundary fits. No non-boundary fit exceeds three local residual RMS; no repeat eclipse series establishes a period. Original search period {raw[tic]['search_period']:.9f} d is retained only as a conditional alias, not a derived ephemeris. The full morphology overview explicitly checks features away from that alias; raw-event fits alone do not decide the result. Covered conditional phases: {json.dumps(coverage)}.

2. Source and independent reduction

{a['source']}

Fresh cutout sectors: {','.join(str(s['sector']) for s in src)}. Candidate capability counts: {','.join(str(s['sector'])+': '+str(len(s['capable_neighbours'])) for s in nr)}. Source comparisons are descriptive signed-image Gaussian fits, with no calibrated PRF confidence. Neighbour catalogue identity can include unresolved or duplicate records. The independent extraction subtracts each frame's lowest-30-pixel median background then sums a central 3x3 aperture, with QUALITY=0. It uses the same TESS photons through a distinct reduction, and is not SPOC. custom-morphology.png and custom-extraction.json preserve its deciding morphology.

3. Gaia orbit

{a['geometry']}

Gaia source {g['gaia_source_id']}; NSS P={g['gaia_P']:.9f} +/- {g['gaia_P_error']:.9f} d; e={g['e']:.5f}, omega={g['omega_deg']:.4f} degrees. No eclipse timing or geometry is inferred from this metadata. {a['gaia_association']}

4. Scoped prior EB coverage

{C[tic]['scoped_prior_eb_status']}; coverage complete: {C[tic]['coverage_complete']}. Reused centrally completed seven scopes: VSX, SIMBAD primary type, Gaia DR3 eclipsing binaries, Prsa2022, IJspeert2024, Kostov2025 vetted tables3/4, ASAS-SN. SB* and ROT alone are not EB identifications; Kostov table2 is unvetted. This is a scoped catalogue result, not an exhaustive discovery claim. Physical and novelty verdicts are separate.

5. Completion and limitations

The representative full review is complete. Scientific outcome: {('submitted eclipse interpretation refuted by a demonstrated smooth/systematic explanation' if a['verdict']=='REFUTED' else 'eclipse morphology and repetition remain unresolved; this is not a secure eclipse identification')}. Missing eclipse geometry reflects the absence of a valid eclipse series, not unfinished execution. {a['limitations']}

Next check: {a['next_check']}

Provenance: raw-evidence/cache-manifest.json preserves original cache paths and SHA256; identity-checks.json verifies all 15 QLP inputs; tesscut-downloads.json stores fresh URLs and zip hashes; TIC raw cones and adapted scripts are retained. manifest.json hashes deliverables. No paper edits, commits or publication were performed.
'''
 p.write_text(text,encoding='utf-8');rows.append({'queue_position':Q[tic]['queue_position'],'tic':tic,'physical_verdict':a['verdict'],'review_state':'completed','full_review_completion':'complete','remaining_full_review':'false','representative_eclipse_period_days':'','signal_class':a['signal_class'],'gaia_association':a['gaia_association'],'novelty_status':C[tic]['scoped_prior_eb_status'],'catalogue_coverage_complete':C[tic]['coverage_complete'],'report':p.relative_to(D).as_posix(),'limitations':a['limitations'],'next_check':a['next_check']})
rows.sort(key=lambda r:int(r['queue_position']))
with (B/'RESULTS.csv').open('w',newline='',encoding='utf-8') as f:w=csv.DictWriter(f,fieldnames=rows[0]);w.writeheader();w.writerows(rows)
json.dump(rows,open(B/'RESULTS.json','w'),indent=2)
json.dump({'batch':'batch06','files':[{'path':p.relative_to(B).as_posix(),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in B.rglob('*') if p.is_file() and p.name!='manifest.json']},open(B/'manifest.json','w'),indent=2)
