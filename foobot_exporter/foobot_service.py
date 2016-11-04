import urllib.request
import json

from django.conf import settings

def get_devices(username, secretKey):
    url = settings.FOOBOT_API_BASE_URL + '/owner/' + username + '/device/'
    request = get_authenticated_request(url, secretKey)
    return get_json_response(request)

def get_authenticated_request(url, secretKey):
    headers = {
        'Content-Type': 'application/json',
        'X-API-KEY-TOKEN': secretKey
    }
    return urllib.request.Request(url, headers=headers)

def get_json_response(request):
    response = urllib.request.urlopen(request).readall().decode('utf-8')
    return  json.loads(response)

