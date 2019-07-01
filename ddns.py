import requests


CF_ZONE_ID = '989ae3839edf7364025e7b774dc16e79'
API_KEY = 'xxx'
E_MAIL = 'yyy'


authn = {'X-Auth-Email': 'email',
         'X-Auth-Key': 'key',
         'Content-Type': 'application/json'}

cf_base_url = f'''https://api.cloudflare.com/client/v4/zones/
    {CF_ZONE_ID}/dns_records?type=A&name=karakays.in'''

r = requests.get(cf_base_url, headers=authn)

if r.ok:
    raise IOError()

result = r.json()
name_id, name = (result['id'], result['content'])


print(name_id, name)


#cf_base_url = '''https://api.cloudflare.com/client/v4/zones/
#023e105f4ecef8ad9ca31a8372d0c353/dns_records/xxx'''
#r = requests.put('https://api.github.com/user', headers=authn)
