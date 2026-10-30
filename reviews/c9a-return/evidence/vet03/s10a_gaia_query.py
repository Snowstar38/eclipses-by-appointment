import requests
q="""SELECT source_id, nss_solution_type, period, period_error, t_periastron, t_periastron_error, eccentricity, eccentricity_error,
arg_periastron, arg_periastron_error, semi_amplitude_primary, semi_amplitude_primary_error, center_of_mass_velocity,
corr_vec, bit_index, obj_func, goodness_of_fit, significance, flags
FROM gaiadr3.nss_two_body_orbit WHERE source_id IN (3890379452571731456, 5866907704116761728)"""
r=requests.post('https://gaia.ari.uni-heidelberg.de/tap/sync',data=dict(REQUEST='doQuery',LANG='ADQL',FORMAT='csv',QUERY=q),timeout=300)
print(r.status_code); print(r.text)
open('s10a_gaia_nss.csv','w').write(r.text)
