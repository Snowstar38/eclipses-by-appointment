# Download all QLP and TESS-SPOC light curves for both targets.
import lightkurve as lk, sys, os
D='/tmp/claude-0/-home-user-eclipses-paper-review/55c92ff4-798a-544f-be03-9888c6804905/scratchpad/data/vet02'
for tic in ['470235665','379251709']:
    sr=lk.search_lightcurve(f'TIC {tic}', author=['QLP','TESS-SPOC'])
    print(tic); print(sr)
    lcs=sr.download_all(download_dir=f'{D}/{tic}')
    print(tic,'downloaded',len(lcs),flush=True)
