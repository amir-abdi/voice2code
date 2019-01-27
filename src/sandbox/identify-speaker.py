import requests
from scipy.io import wavfile


profile_ids = {
    'amir': "2172cefe-5bb8-4ae5-ae21-6bd7918bc6f8",
    'kris': "f61b6b1b-ed36-42b7-8821-d6fd12de7c1a",
    'illya': "3d081222-13d8-42a5-b3c7-058e1dcbf77e",
    'isac': "8d73c6b4-6e32-474a-9f85-ccb948618ae9"
}

key = 'f5b04a627bc34ce3be21e50984fd953e'


def identify_speaker(data):
    url = 'https://westus.api.cognitive.microsoft.com/spid/v1.0/identify'

    identificationProfileIds = ''
    for value in profile_ids.values():
        identificationProfileIds += value + ','
    identificationProfileIds = identificationProfileIds[:-1]
    print(identificationProfileIds)

    params = {
        'identificationProfileIds': identificationProfileIds,
        'shortAudio': True,
    }

    json_data = {
        "locale": "en-us",
    }

    headers = {
        "Ocp-Apim-Subscription-Key": key,
        'Content-Type': 'application/json',
    }

    try:
        response = requests.post(url, data=data, json=json_data, headers=headers, params=params)
        print('response:', response.status_code)
        if response.status_code == 202:
            print(response.headers['Operation-Location'])
            return response.headers['Operation-Location']
        else:
            print('Error:{}, {}, {}'.format(response.status_code, response.text, response.content))
            return False
    except Exception as e:
        print('[Errno {0}] {1}'.format(e.errno, e.strerror))
        return False


def get_status(location):
    headers = {
        "Ocp-Apim-Subscription-Key": key,
        'Content-Type': 'application/json',
    }
    response = requests.get(location, headers=headers)


    print(response.text)


if __name__ == '__main__':
    # filename = 'data/offer1.wav'
    # f = open(filename, "rb").read()
    # operation_location = identify_speaker(f)
    # get_status(operation_location)
    #
    get_status('https://westus.api.cognitive.microsoft.com/spid/v1.0/operations/4f793519-c7a3-4624-8490-0b74ca43173c')
