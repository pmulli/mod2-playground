import requests, hashlib, datetime, json

from pprint import pprint as pp

character_name = input('Input a Marvel character\'s name? ')

timestamp = datetime.datetime.now().strftime('%Y-%m-%d%H:%M:%S')
pub_key = 'd5a47e105cd60e3e3092513bccb8aa10'
priv_key = '282677b498851f024bc05e6c56f74ab74308bc12'

def hash_params():
    """ Marvel API requires server side API calls to include
    md5 hash of timestamp + public key + private key """

    hash_md5 = hashlib.md5()
    hash_md5.update(f'{timestamp}{priv_key}{pub_key}'.encode('utf-8'))
    hashed_params = hash_md5.hexdigest()

    return hashed_params

params = {'ts': timestamp, 'apikey': pub_key, 'hash': hash_params(), 'nameStartsWith' : character_name}

resp = requests.get('https://gateway.marvel.com:443/v1/public/characters', params=params)

if resp.status_code == 200:
    results = json.loads(resp.text)
    #pp(results)
    data = results.get('data')
    if data.get('count') > 0:
        results = data.get('results')
        for index in range(0, len(results)):
            print('ID: {}, Name: {}'.format(results[index].get('id'), results[index].get('name')))
    else:
        print('No character found for: {}'.format(character_name))
elif resp.status_code != 200:
    # This means something went wrong.
    print('API resp {}'.format(resp.status_code))
