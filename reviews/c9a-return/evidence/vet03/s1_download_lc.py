import lightkurve as lk, sys
D='/tmp/claude-0/-home-user-eclipses-paper-review/55c92ff4-798a-544f-be03-9888c6804905/scratchpad/data/vet03'
for tic in ['70665829','331293467']:
    sr=lk.search_lightcurve('TIC '+tic, author=['QLP','TESS-SPOC','SPOC'])
    print(tic); print(sr)
    sr.download_all(download_dir=f'{D}/{tic}')
