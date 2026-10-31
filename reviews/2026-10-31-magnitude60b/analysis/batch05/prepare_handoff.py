from pathlib import Path
import csv,json,shutil,hashlib,numpy as np
B=Path(__file__).parent;SB=Path('[local path omitted] 5/made/sb1-scale');out={}
notes={'388152396':'Selected shallower eclipse at phase0; deeper distinct eclipse near phase0.34. S81 cycle67 unrelated local dip +0.20..0.45d masked from baseline fit; both sides retained. No half/double adoption.', '11249710':'Two distinct similar-depth eclipses at phases0 and0.34 establish retained eccentric orbital period; selected phase0 event kind, not claim deepest primary.', '314991763':'Deep primary phase0 and shallower secondary phase0.5 establish full orbital period.', '102716983':'Extra S59 QLP downloaded because initial three selected sectors yielded only two timed events. S59 cycles94,95 now provide consecutive recurrence and four timed eclipses total. Close capable neighbours14.39/14.45arcsec remain attribution concern.', '331861613':'Extra earlier S18 downloaded because initial three sectors yielded only two timed events. S17 cycle0,S18 cycle2,S85 cycle102 repeat at three epochs, but no adjacent-cycle pair; S58 cycle62 has zero quality-zero samples in +/-0.2d, not null. Integer/subharmonic ambiguity requires helper decision; full available QLP list17,18,58,85 checked. Close capable14arcsec neighbour also unresolved.'}
for r in csv.DictReader(open(B/'queue.csv')):
 tic=r['tic'];m=json.load(open(B/tic/'measurements.json'));ev=sorted([e for e in m['events'] if e.get('timing_usable')],key=lambda e:e['mid_btjd']);src=next((SB/'diffimg'/tic).glob('diff_s*.json'));D=B/tic/'historical';D.mkdir(exist_ok=True)
 for p in [src,src.with_suffix('.png'),src.parent/'gaia.json']:shutil.copy2(p,D/p.name)
 pairs=[dict(sector=a['sector'],cycles=[a['cycle'],b['cycle']]) for a,b in zip(ev,ev[1:]) if a['sector']==b['sector'] and b['cycle']-a['cycle']==1]
 out[tic]=dict(within_sector_consecutive_pairs=pairs,cycles=[e['cycle'] for e in ev],note=notes.get(tic,'Representative raw events support same event kind at retained photometric period; no persistent unequal alternating sequence seen. The measured period is seeded by the historical photometric branch, not an exhaustive alias search.'))
 m['epoch_kind']='Selected shallower eclipse' if tic=='388152396' else 'Selected phase-zero eclipse; not assumed deepest primary';json.dump(m,open(B/tic/'measurements.json','w'),indent=2)
json.dump(out,open(B/'alias-audit.json','w'),indent=2)
h={}
for p in B.rglob('*'):
 if p.is_file() and p.name!='PROVISIONAL-SHA256SUMS.json':h[str(p)]=hashlib.sha256(p.read_bytes()).hexdigest()
for r in json.load(open(B/'download-receipts.json')):h[r['path']]=r['sha256']
for r in json.load(open(B/'pixel-audit.json')).values():h[r['cutout_path']]=r['cutout_sha256']
json.dump(h,open(B/'PROVISIONAL-SHA256SUMS.json','w'),indent=2)
