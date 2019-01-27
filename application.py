#!/usr/local/bin/python3
import logging
from applicationinsights.logging import enable
from flask import Flask
from flask import request as freq
from src.api.common.utils import get_azure_token
from src.api.speach2code.speach2text import speach2text
from src.api.speach2code.text2code import text2code
from src.api.speach_rec.voice_recognition import voice_rec
from src.keys import keys

key = keys['insights']
enable(key)
app = Flask(__name__)


@app.route('/')
def index():
    return 'Speach to Text api! ;-)'


@app.route('/speachToText/v1.0/toCode', methods=['POST'])
def to_code():
    logging.error('speach to code end point')

    data = freq.data
    logging.error('%s', str(data))

    key = keys['speachToText']
    token = get_azure_token(key)

    text_response = speach2text(token, data)
    print('text_response:', text_response)
    intent = text2code(token, text_response)


    return intent


@app.route('/speachRec/v1.0/speaker', methods=['POST'])
def speaker():
    data = freq.data
    app.logger.info('Speaker end point')

    speaker_id = voice_rec(data)
    return speaker_id


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
