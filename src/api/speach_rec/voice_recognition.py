import requests
import json
from src.keys import keys

key = keys['speakerRecog']


def voice_rec(data):

    url = 'https://westus.api.cognitive.microsoft.com/spid/v1.0/identify'
    headers = {
        "Ocp-Apim-Subscription-Key": key,
        # 'Authorization': 'Bearer {}'.format(token.decode('ascii')),
        'Content-type': 'audio/wav; codecs=audio/pcm; samplerate=16000',
        'Accept': 'application/json',
        }
    params = {
        'identificationProfileIds': 'en-CA',
    }

    try:
        response = requests.post(url, data=data, headers=headers, params=params)
        print('response:', response.status_code)

        if response.status_code == 200:
            print(response.text)
            response_text = json.loads(response.text)
            return response_text['DisplayText']
        else:
            return 'Error:{}, {}, {}'.format(response.status_code, response.text, response.content)
    except Exception as e:
        return '[Errno {0}] {1}'.format(e.errno, e.strerror)
