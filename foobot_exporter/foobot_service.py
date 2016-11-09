import urllib.request
import json

from django.conf import settings

def get_devices(username, secret_key):
    url = settings.FOOBOT_API_BASE_URL + '/owner/' + username + '/device/'
    request = get_authenticated_request(url, secret_key)
    return get_json_response(request)

def get_datapoints_last(secret_key, device_uuid, period, average_by, content_type):
    url = settings.FOOBOT_API_BASE_URL \
        + '/device/' + device_uuid  \
        + '/datapoint/' + str(period) \
        + '/last/' + str(average_by) + '/'

    
    request = get_authenticated_request(url, secret_key, content_type)
    if content_type == 'application/json':
        return get_json_response(request)
    else:
        return get_utf8_response(request)


def get_authenticated_request(url, secret_key, accept='application/json'):
    headers = {
        'Accept': accept,
        'X-API-KEY-TOKEN': secret_key
    }
    return urllib.request.Request(url, headers=headers)

def get_json_response(request):

    data = None
    try:
        response = urllib.request.urlopen(request)
        status_code = response.code
        data = json.loads(response.readall().decode('utf-8'))
    except urllib.error.HTTPError as e:
        status_code = e.code

    return (data, status_code)


def get_utf8_response(request):

    data = None
    try:
        response = urllib.request.urlopen(request)
        status_code = response.code
        data = response.readall().decode('utf-8')
    except urllib.error.HTTPError as e:
        status_code = e.code

    return (data, status_code)

