import csv,json,pathlib
p=pathlib.Path(__file__).resolve().parent.parent
for row in csv.DictReader((p/'RESULTS.csv').open()):
 m=json.loads((p/row['tic']/'measurements.json').read_text())
 for key in ('period_days','period_error_days','primary_epoch_btjd','depth_ppt'):
  assert float(row[key]) == float(m[key]), (row['tic'],key)
 print(row['tic'], 'numeric results match')
