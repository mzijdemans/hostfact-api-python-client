import json
from datetime import date
import urllib.parse

from io import BytesIO

import pycurl
import os

from os.path import join, dirname
from dotenv import load_dotenv


class HostFactAPI:

    def __init__(self, url='', api_key=''):
        dotenv_path = '.env'  # join(dirname(__file__), '.env')
        load_dotenv(dotenv_path)
        if url == '':
            self.url = os.getenv('HOSTFACT_DEFAULT_URL')
        if api_key == '':
            self.api_key = os.getenv('HOSTFACT_DEFAULT_KEY')

    def sendRequest(self, controller, action, params=None):

        if params is None:
            params = {}

        params['api_key'] = self.api_key
        params['controller'] = controller
        params['action'] = action

        buffer = BytesIO()
        ch = pycurl.Curl()
        ch.setopt(pycurl.URL, self.url)
        ch.setopt(pycurl.SSL_VERIFYHOST, 0)
        ch.setopt(pycurl.SSL_VERIFYPEER, False)
        # ch.setopt(pycurl.RETURNTRANSFER, 1)
        ch.setopt(pycurl.TIMEOUT, 10)
        ch.setopt(pycurl.POST, 1)


        data = url_encoder(params)
        ch.setopt(pycurl.POSTFIELDS, data)
        ch.setopt(pycurl.WRITEDATA, buffer)
        #ch.setopt(pycurl.VERBOSE, 1)
        ch.perform()

        curlResp = buffer.getvalue()

        if ch.getinfo(pycurl.RESPONSE_CODE) != 200:
            result = {
                'controller': 'invalid',
                'action': 'invalid',
                'status': 'error',
                'date': date.today(),
                'errors': curlResp
            }
        else:
            result = json.loads(curlResp.decode('utf-8'))
        ch.close()

        return result

# source: https://stackoverflow.com/a/43347067/2385117
def url_encoder(params):
    g_encode_params = {}

    def _encode_params(params, p_key=None):
        encode_params = {}
        if isinstance(params, dict):
            for key in params:
                encode_key = '{}[{}]'.format(p_key,key)
                encode_params[encode_key] = params[key]
        elif isinstance(params, (list, tuple)):
            for offset,value in enumerate(params):
                encode_key = '{}[{}]'.format(p_key, offset)
                encode_params[encode_key] = value
        else:
            g_encode_params[p_key] = params

        for key in encode_params:
            value = encode_params[key]
            _encode_params(value, key)

    if isinstance(params, dict):
        for key in params:
            _encode_params(params[key], key)

    return urllib.parse.urlencode(g_encode_params)

def print_r_pre(data):
    print(data)
