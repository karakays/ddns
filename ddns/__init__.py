import os


cf_secret = os.environ.get('CF_API_KEY')
cf_email = os.environ.get('CF_EMAIL')
cf_zone_id = os.environ.get('CF_ZONE')
cf_domain = os.environ.get('CF_DOMAIN')

if cf_secret is None:
    raise OSError('Please set environment variable CF_API_KEY.')

if cf_email is None:
    raise OSError('Please set environment variable CF_EMAIL')

if cf_zone_id is None:
    raise OSError('Please set environment variable CF_ZONE')

if cf_domain is None:
    raise OSError('Please set environment variable CF_DOMAIN')

ctx = {'CF_API_KEY' : cf_secret,
       'CF_EMAIL': cf_email,
       'CF_ZONE': cf_zone_id,
       'CF_DOMAIN': cf_domain}
