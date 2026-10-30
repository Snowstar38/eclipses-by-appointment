import json,csv,pathlib,numpy as np
r=pathlib.Path(__file__).parent; d=json.loads((r.parent/'selected.json').read_text()); rows={x['source_id']:x for x in csv.DictReader(open(r'C:\Home\Astra\made\binary-handoff-2026-10-30\shared-full-review\gaia-nss-ari.csv'))}; rng=np.random.default_rng(405)
for tic,target in d['targets'].items():
 row=rows[target['gaia']['source_id']]; keys=['period','center_of_mass_velocity','semi_amplitude_primary','eccentricity','arg_periastron','t_periastron']; mu=np.array([float(row[k]) for k in keys]); sig=np.array([float(row[k+'_error']) for k in keys]); corr=np.eye(6); z=[float(x) for x in row['corr_vec'].strip('{}').split(',')]; n=0
 for j in range(1,6):
  for i in range(j):corr[i,j]=corr[j,i]=z[n];n+=1
 eig=np.linalg.eigvalsh(corr); cov=corr*sig[:,None]*sig[None,:]; samp=rng.multivariate_normal(mu,cov,120000); ok=(samp[:,0]>0)&(samp[:,3]>=0)&(samp[:,3]<1); samp=samp[ok]; P=samp[:,0];e=samp[:,3];omega=np.deg2rad(samp[:,4]); tp=samp[:,5]+389
 def conj(angle):
  nu=angle-omega; E=2*np.arctan2(np.sqrt(1-e)*np.sin(nu/2),np.sqrt(1+e)*np.cos(nu/2)); M=E-e*np.sin(E);return tp+(M%(2*np.pi))*P/(2*np.pi)
 A=conj(np.pi/2); B=conj(3*np.pi/2); data=json.loads((r/f'{tic}_measurements.json').read_text()); ep=data['ephemeris']; sectors=sorted(set(x['sector'] for x in data['events'])); output=[]
 for sector,epoch in [(None,389)]+[(sec,np.median([x['tc'] for x in data['events'] if x['sector']==sec])) for sec in sectors]:
  phot=ep['T0']+round((epoch-ep['T0'])/ep['P'])*ep['P']; cycle=round((epoch-ep['T0'])/ep['P']); v=np.array([1.,cycle]); phot_err=float(np.sqrt(v@np.array(ep['covariance'])@v));entry={'sector':sector,'epoch':float(epoch),'phot_primary':float(phot),'phot_error_d':phot_err}
  for name,c in [('A',A),('B',B)]:
   near=c+np.round((phot-c)/P)*P; delta=phot-near; entry[name+'_offset_d']=float(np.median(delta));entry[name+'_sigma_d']=float(np.std(delta));entry[name+'_offset_sigma']=float(np.median(delta)/np.sqrt(np.std(delta)**2+phot_err**2))
  output.append(entry)
 phase=((B-A)/P)%1
 result={'eigenvalues':eig.tolist(),'samples_retained':len(samp),'samples_total':120000,'physical_e_rejection_fraction':float(1-ok.mean()),'omega_tp_corr':float(corr[4,5]),'A_to_B_phase_quantiles':np.quantile(phase,[.16,.5,.84]).tolist(),'primary_comparisons':output,'period_difference_sigma':float((ep['P']-mu[0])/np.sqrt(ep['covariance'][1][1]+sig[0]**2))}
 (r/f'{tic}_gaia_mc.json').write_text(json.dumps(result,indent=2));print(tic,'e reject',round(1-ok.mean(),3),'phase',np.quantile(phase,[.16,.5,.84]),'Gaia epoch offsets A/B',output[0]['A_offset_sigma'],output[0]['B_offset_sigma'])
