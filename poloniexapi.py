import time
import json
import requests
import hmac
import hashlib
import urllib

class Connection(object):

    def __init__(self, Key="", Secret="", timeout=120):
        self.Key = Key
        self.Secret = Secret
        self.timeout = timeout
        self.nonce = int(time.time()*1000000)

    def __call__(self, command, args={}):

        args['command'] = command
        args['nonce'] = self.nonce
        
        try:
            data = urllib.parse.urlencode(args)
            sign = hmac.new(self.Secret.encode('utf-8'), data.encode('utf-8'), hashlib.sha512)

            response = requests.post('https://poloniex.com/tradingApi', data=args,
                                      headers={'Sign': sign.hexdigest(), 'Key': self.Key},
                                      timeout=self.timeout)

        except Exception as exception: raise exception
        
        finally: self.nonce += 1
        
        try: return json.loads(response.text, parse_float=unicode)
        except NameError: return json.loads(response.text, parse_float=str)
