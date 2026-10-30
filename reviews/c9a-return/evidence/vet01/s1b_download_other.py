# s1b: download the other-pipeline FFI light curves (TASOC for 195865529 s15, GSFC-ELEANOR-LITE for 468181994 s12/13)
import lightkurve as lk, warnings
warnings.filterwarnings('ignore')
D='/tmp/claude-0/-home-user-eclipses-paper-review/55c92ff4-798a-544f-be03-9888c6804905/scratchpad/data/vet01'
for tic,auth in [('195865529','TASOC'),('468181994','GSFC-ELEANOR-LITE')]:
    sr=lk.search_lightcurve(f'TIC {tic}',author=auth)
    print(sr)
    for i in range(len(sr)):
        try:
            lc=sr[i].download(download_dir=f'{D}/{tic}')
            print(tic,auth,i,lc.meta.get('SECTOR'),lc.columns, len(lc), sr[i].table['dataURL'][0] if 'dataURL' in sr[i].table.colnames else '')
        except Exception as e: print('fail',tic,auth,i,e)
