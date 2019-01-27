import requests
from scipy.io import wavfile


profile_ids = {
    'amir': "2172cefe-5bb8-4ae5-ae21-6bd7918bc6f8",
    'kris': "f61b6b1b-ed36-42b7-8821-d6fd12de7c1a",
    'illya': "3d081222-13d8-42a5-b3c7-058e1dcbf77e",
    'isac': "8d73c6b4-6e32-474a-9f85-ccb948618ae9"
}

key = 'f5b04a627bc34ce3be21e50984fd953e'

phrases = [\
    {"phrase": "i am going to make him an offer he cannot refuse"},
    {"phrase": "houston we have had a problem"},
    {"phrase": "my voice is my passport verify me"},
    {"phrase": "apple juice tastes funny after toothpaste"},
    {"phrase": "you can get in without your password"},
    {"phrase": "you can activate security system now"},
    {"phrase": "my voice is stronger than passwords"},
    {"phrase": "my password is not your business"},
    {"phrase": "my name is unknown to you"},
    {"phrase": "be yourself everyone else is already taken"}
]


def create_enrollment(profile_id, data):
    url = 'https://westus.api.cognitive.microsoft.com/spid/v1.0/verificationProfiles/{}/enroll'.format(profile_id)
    # url = 'https://westus.api.cognitive.microsoft.com/spid/v1.0/verificationPhrases'

    json_data = {
        "locale": "en-us",
    }

    headers = {
        "Ocp-Apim-Subscription-Key": key,
        'Content-Type': 'application/json',
    }

    try:
        response = requests.post(url, data=data, json=json_data, headers=headers)
        print('response:', response.status_code)
        if response.status_code == 200:
            print(response.text)
            return True
        else:
            print('Error:{}, {}, {}'.format(response.status_code, response.text, response.content))
            return False
    except Exception as e:
        print('[Errno {0}] {1}'.format(e.errno, e.strerror))
        return False


def enroll(name, files):
    profile_id = profile_ids[name]
    print(files)
    for file in files:
        data = open(file, "rb").read()
        if create_enrollment(profile_id, data):
            print('SUCCESS: Enrollment for file {} for user {}'.format(file, name))
        else:
            print('FAILED: Enrollment for file {} for user {}'.format(file, name))


if __name__ == '__main__':
    # worked: offer1
    # filename = 'data/illya-offer1.wav'
    # f = open(filename, "rb").read()
    # fs, data = wavfile.read(filename)
    # print(data.shape)
    # print(f)
    # create_enrollment(profile_ids[0], data[:, 0].tobytes())
    import glob
    files = glob.glob('data/Iyad*.wav')
    enroll('illya', files)
    # create_enrollment(profile_ids['illya'], f)
