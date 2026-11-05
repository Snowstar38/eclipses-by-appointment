import csv,json,pathlib
b=pathlib.Path(__file__).parent
for r in csv.DictReader((b/'queue.csv').open()):
 d=json.loads((b/r['tic']/'fold-inspection.json').read_text())
 print('\n',r['sample_id'],r['tic'])
 for w in d['windows']:
  if w['n_core']>5:
   print(w['trial'],w['sector'],round(w['predicted_btjd'],2),w['n_core'],w['n_left'],w['n_right'],round(w['sap_core_delta_ppt'],1) if w['sap_core_delta_ppt'] is not None else None,round(w['kspsap_core_delta_ppt'],1) if w['kspsap_core_delta_ppt'] is not None else None)
