import urllib.request
import json

from django.conf import settings

def get_devices(secretKey, username):
    url = settings.FOOBOT_API_BASE_URL + '/owner/' + username + '/device/'
    headers = {
        'Content-Type': 'application/json',
        'X-API-KEY-TOKEN': secretKey
    }
    request = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(request).readall().decode('utf-8')
    data = json.loads(response)
    print(data)

    return data

