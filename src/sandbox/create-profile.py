import requests

# "2172cefe-5bb8-4ae5-ae21-6bd7918bc6f8"
# "f61b6b1b-ed36-42b7-8821-d6fd12de7c1a"
# "3d081222-13d8-42a5-b3c7-058e1dcbf77e"
# "8d73c6b4-6e32-474a-9f85-ccb948618ae9"

key = 'f5b04a627bc34ce3be21e50984fd953e'


def create_profile():
    url = 'https://westus.api.cognitive.microsoft.com/spid/v1.0/verificationProfiles'
    json_data = {
      "locale": "en-us",
    }

    headers = {
        "Ocp-Apim-Subscription-Key": key,
        'Content-Type': 'application/json',
    }

    params = {
    }

    try:
        response = requests.post(url, json=json_data, headers=headers, params=params)
        print('response:', response.status_code)
        if response.status_code == 200:
            print(response.text)
            return response.text
        else:
            return 'Error:{}, {}, {}'.format(response.status_code, response.text, response.content)
    except Exception as e:
        return '[Errno {0}] {1}'.format(e.errno, e.strerror)


if __name__ == '__main__':
    create_profile()
