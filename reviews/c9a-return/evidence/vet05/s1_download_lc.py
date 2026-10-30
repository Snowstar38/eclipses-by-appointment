import lightkurve as lk, sys
D='/tmp/claude-0/-home-user-eclipses-paper-review/55c92ff4-798a-544f-be03-9888c6804905/scratchpad/data/vet05'
for tic in ['15855794','92881948']:
    sr=lk.search_lightcurve('TIC '+tic)
    print(tic); print(sr)
    sel=sr[[ (a in ('QLP','TESS-SPOC','SPOC')) for a in sr.author]]
    lcs=sel.download_all(download_dir=f'{D}/{tic}')
    for lc in lcs:
        print(lc.meta.get('SECTOR'), lc.meta.get('AUTHOR'), lc.meta.get('EXPOSURE', ''), len(lc), lc.meta.get('FILENAME',''))
