# Re-query Gaia DR3 nss_two_body_orbit (Heidelberg TAP) for bit_index and corr_vec.
import requests
q="""SELECT source_id, nss_solution_type, period, period_error, t_periastron, t_periastron_error, eccentricity, eccentricity_error,
arg_periastron, arg_periastron_error, center_of_mass_velocity, semi_amplitude_primary, semi_amplitude_primary_error, bit_index, corr_vec, goodness_of_fit, significance, flags
FROM gaiadr3.nss_two_body_orbit WHERE source_id IN (2287291537931000064, 519027491846682624)"""
r=requests.post('https://gaia.ari.uni-heidelberg.de/tap/sync',data=dict(REQUEST='doQuery',LANG='ADQL',FORMAT='csv',QUERY=q),timeout=300)
print(r.status_code); print(r.text)
open('gaia_nss_tap.csv','w').write(r.text)
