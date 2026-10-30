import lightkurve as lk, sys, os
D='/tmp/claude-0/-home-user-eclipses-paper-review/55c92ff4-798a-544f-be03-9888c6804905/scratchpad/data/vet04'
for tic in ['283532878','407877153']:
    sr=lk.search_lightcurve('TIC '+tic, author=['QLP','TESS-SPOC','SPOC'])
    print(tic); print(sr)
    lcs=sr.download_all(download_dir=os.path.join(D,tic))
    for lc in lcs:
        print(lc.meta['AUTHOR'], lc.meta['SECTOR'], lc.meta.get('EXPOSURE', ''), lc.filename)
