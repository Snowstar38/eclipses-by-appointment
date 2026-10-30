import json,pathlib
R=pathlib.Path('.'); out=[]
for z in json.load(open('archive-independent-results.json')):
 p=R/z['tic']/'mast-products.json';out.append({'tic':z['tic'],'inventory_file':str(p) if p.exists() else None,'status':'response saved' if p.exists() else 'inventory request timed out; no response saved','archive_result':z.get('provenance',z.get('error'))})
json.dump(out,open('inventory-status.json','w'),indent=2)
