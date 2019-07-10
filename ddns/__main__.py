from . import ctx
import io
import requests
import subprocess


authn = {'X-Auth-Email': ctx['CF_EMAIL'],
         'X-Auth-Key': ctx['CF_API_KEY']}


def fetch_dns():
    url = f'''https://api.cloudflare.com/client/v4/zones/\
{ctx['CF_ZONE']}/dns_records?type=A&name={ctx['CF_DOMAIN']}'''
    r = requests.get(url, headers={**authn, 'Content-Type': 'application/json'})
    payload = r.json()
    #if payload['success']:
    #    raise IOError()
    result = payload['result'][0]
    domain_id, domain_addr = (result['id'], result['content'])
    return (domain_id, domain_addr)


def update_dns(addr):
    dm_id, dm_addr = fetch_dns()

    url = f'''https://api.cloudflare.com/client/v4/zones/\
{ctx['CF_ZONE']}/dns_records/{dm_id}'''

    #if payload['success']:
    #    raise IOError()
    payload = {'type': 'A',
               'name': ctx['CF_DOMAIN'],
               'content': addr}

    r = requests.put(url,
                     headers={**authn, 'Content-Type': 'application/json'},
                     json=payload)


    with io.open('/tmp/ddns_addr', 'w') as f:
        f.write(addr)


def resolve_addr():
    dig_cmd = 'dig +short myip.opendns.com @resolver1.opendns.com'
    cp = subprocess.run(dig_cmd.split(),
                   check=True,
                   stdout=subprocess.PIPE,
                   stderr=subprocess.PIPE)
    return cp.stdout.decode().strip()


def main():
    ch_addr = None
    try:
        with io.open('/tmp/ddns_addr', 'r') as f:
            ch_addr = f.readline()
    except IOError:
        pass

    curr_addr = resolve_addr()
    if curr_addr != ch_addr:
        update_dns(curr_addr)
