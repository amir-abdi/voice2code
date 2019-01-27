import requests
import json


def speach2text(token, data):
    url = 'https://westus2.stt.speech.microsoft.com/speech/recognition/conversation/cognitiveservices/v1'
    headers = {
        # "Ocp-Apim-Subscription-Key": key,
        'Authorization': 'Bearer {}'.format(token.decode('ascii')),
        'Content-type': 'audio/ogg; codecs=opus',  # 'audio/wav; codecs=audio/pcm; samplerate=16000',
        'Accept': 'application/json',

        }
    params = {
        'language': 'en-CA',
    }
    # data = data['data']
    print('data', data)
    try:
        response = requests.post(url, data=data, headers=headers, params=params)
        print('response:', response.status_code)
        if response.status_code == 200:
            print(response.text)
            response_text = json.loads(response.text)
            return response_text['DisplayText']
            # return response_text
        else:
            return 'Error:{}, {}, {}'.format(response.status_code, response.text, response.content)
    except Exception as e:
        return '[Errno {0}] {1}'.format(e.errno, e.strerror)
