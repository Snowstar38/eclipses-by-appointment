from pathlib import Path
import csv,json,collections
D=Path(__file__).resolve().parent;ev=json.loads((D/'dips.json').read_bytes())
notes={
'167710':('no','A very large positive flare or background pulse precedes the deepest negative excursion at BTJD 2344.22. Only one short stable two-channel trigger appears away from it, with three cadences in broad sector noise.'),
'113655666':('no','One real asymmetric dropout reaches 173 ppt at BTJD 2491.27973 in S43 in both channels, flanked by a clean baseline at ±0.15 d. No second isolated event appears in S42 or S43. The automated contiguous-data trigger missed this event.'),
'187261476':('yes','Seventeen discrete ~32 ppt primary minima at P=1.17899242 d and T0=2912.222483 BTJD in S59, median FWHM 2.63 h, 90th-percentile timing residual 1.01 min. Both SAP and PDCSAP recover the narrow dips on top of broader orbital modulation. A separate complex ~400 ppt dip near BTJD 2917.6–2917.9 is excluded from the short-period fit.'),
'192745310':('no','Isolated three-to-seven-cadence threshold crossings in S91 are comparable with the full-sector PDC point scatter of 64 ppt. The S51 scatter is 55 ppt. No clean structured pair.'),
'259514170':('no','S3, S30 and S32 have approximately 1 ppt point scatter and zero detections. S5 contains strong slopes and level changes near gaps with zero common stable windows; no corroborated pair.'),
'307907698':('no','S21 has a bright upward disturbance. S48 short three-cadence depressions occur at ordinary low points within ~69 ppt point scatter. No well-defined pair.'),
'356752132':('no','One genuine V-like isolated depression in S42 at BTJD 2454.764 has median core depths of 432 ppt SAP and 481 ppt PDCSAP. Other short triggers in four sectors are consistent with 14–17 ppt point scatter; no independently verified repeat.'),
'436583779':('no','The S5 apparent dip drives the calibrated flux below zero. Few-cadence negative runs in other sectors occur in 160–191 ppt scatter. No reliable pair; sensitivity is poor.'),
'468346631':('no','In S42 36% of the finite PDC series lies below zero, with large trends and a dropout adjoining a gap. S43 shows no common threshold window. Source flux is poorly measured in the disturbed sector.'),
'867844953':('no','Very large sinuous variation occupies both sectors; median-flux normalization gives thousands of ppt single-cadence scatter. No common SAP/PDC window with stable baselines in either sector. Eclipse sensitivity is poor.')}
out=[]
for tic,ss in ev.items():
 rows=[r for s in ss for r in s['events'] if all(r.get(k) and r[k]['stable'] for k in ('sap','pdc'))]
 status,note=notes[tic];out.append(dict(tic=tic,sectors='|'.join(str(s['sector']) for s in ss),common_numeric_windows=len(rows),endpoint=status,assessment=note))
with (D/'assessment.csv').open('w',encoding='utf8',newline='') as f:
 w=csv.DictWriter(f,out[0],lineterminator='\n');w.writeheader();w.writerows(out)
