import json
from datetime import date
from urllib.parse import urlencode

from io import BytesIO

import pycurl
import os

from os.path import join, dirname
from dotenv import load_dotenv


class HostFactAPI:

    def __init__(self, url='', api_key=''):
        dotenv_path = join(dirname(__file__), '.env')
        load_dotenv(dotenv_path)
        if url == '':
            self.url = os.getenv('HOSTFACT_DEFAULT_URL')
        if api_key == '':
            self.api_key = os.getenv('HOSTFACT_DEFAULT_KEY')

    def sendRequest(self, controller, action, params={}):

        params['api_key'] = self.api_key
        params['controller'] = controller
        params['action'] = action

        buffer = BytesIO()
        ch = pycurl.Curl()
        ch.setopt(ch.URL, self.url)
        ch.setopt(ch.SSL_VERIFYHOST, 0)
        ch.setopt(ch.SSL_VERIFYPEER, False)
        # ch.setopt(ch.RETURNTRANSFER, 1)
        ch.setopt(ch.TIMEOUT, 10)
        ch.setopt(ch.POST, 1)
        data = urlencode(params)
        ch.setopt(ch.POSTFIELDS, data)
        ch.setopt(ch.WRITEDATA, buffer)

        ch.perform()
        curlResp = buffer.getvalue()

        if ch.getinfo(ch.RESPONSE_CODE) != 200:
            result = {
                'controller': 'invalid',
                'action': 'invalid',
                'status': 'error',
                'date': date.today(),
                'errors': curlResp
            }
        else:
            result = json.loads(curlResp)
        ch.close()

        return result


def print_r_pre(data):
    print(data)
