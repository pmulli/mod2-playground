import requests

resp = requests.get('http://rem-rest-api.herokuapp.com/api/[things]')

if resp.status_code != 200:
    # This means something went wrong.
    print('GET /api/[things] {}'.format(resp.status_code))
print(resp.json())

#for thing_item in resp.json():
#    print('{} {} {}'.format(thing_item['id'], thing_item['firstName'], thing_item['lastName']))