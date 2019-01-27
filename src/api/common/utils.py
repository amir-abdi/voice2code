import http.client, urllib.parse, json


def get_azure_token(key):
    params = {'mkt': 'en-US',
              'mode': 'proof'}

    host = 'westus2.api.cognitive.microsoft.com'
    path = '/sts/v1.0/issueToken'

    headers = {'Ocp-Apim-Subscription-Key': key,
               'Content-Type': 'application/x-www-form-urlencoded',
               'Content-Length': 0}

    conn = http.client.HTTPSConnection(host)
    params = urllib.parse.urlencode(params)
    conn.request("POST", path, params, headers)
    token = conn.getresponse()
    return token.read()

