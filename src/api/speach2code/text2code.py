import requests
from src.keys import keys

key = keys['luis']


def text2code(token, input_text):
    url = 'https://westus2.api.cognitive.microsoft.com/luis/v2.0/apps/b7c7ebff-4bc3-4fb2-824c-622a9cadebe7'

    headers = {
        'Ocp-Apim-Subscription-Key': key,
        # 'Authorization': 'Bearer {}'.format(token.decode('ascii')),
    }

    params = {
        'q': input_text,
        # Optional request parameters, set to default values
        'timezoneOffset': '0',
        'verbose': 'true',
        'spellCheck': 'false',
        'staging': 'false',
    }

    try:
        response = requests.get(url, headers=headers, params=params)
        # print('response:', response.status_code)
        if response.status_code == 200:
            print(response.text)
            return response.text
        else:
            return 'Error:{}, {}, {}'.format(response.status_code, response.text, response.content)
    except Exception as e:
        return "[Errno {0}] {1}".format(e.errno, e.strerror)


