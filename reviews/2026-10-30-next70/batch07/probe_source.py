from pathlib import Path
import json,subprocess
B=Path('[local working path omitted; see provenance receipts]');R=B/'raw-evidence'; tic='233269866'; src=(B.parent/'batch06/raw-evidence/source_repeatability.py').read_text().replace('diff_s15.json','diff_s55.json'); (R/'source_repeatability.py').write_text(src)
r=next(x for x in json.loads((R/'search-receipts.json').read_text()) if x['tic']==tic)['P']; subprocess.run(['python',str(R/'source_repeatability.py'),tic,'55',str(r['P']),str(r['t0']),str(r['dur']*24),str(r['depth']/1e6)],cwd=R/tic,check=True)
