# Fetch Gaia DR3 nss_two_body_orbit rows (incl. corr_vec, bit_index) for the five targets (Heidelberg TAP mirror).
import requests
ids='2194224406993202176,2206975649496007936,2194235436469405952,2009695569526354048,2165710668881281536'
q=f'SELECT source_id,nss_solution_type,bit_index,period,period_error,t_periastron,t_periastron_error,eccentricity,eccentricity_error,arg_periastron,arg_periastron_error,center_of_mass_velocity,semi_amplitude_primary,goodness_of_fit,significance,flags,corr_vec FROM gaiadr3.nss_two_body_orbit WHERE source_id IN ({ids})'
r=requests.post('https://gaia.ari.uni-heidelberg.de/tap/sync',data={'REQUEST':'doQuery','LANG':'ADQL','FORMAT':'csv','QUERY':q},timeout=300)
open('[local path omitted]','w').write(r.text); print(r.text[:3000])
