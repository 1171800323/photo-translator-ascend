import random
from hashlib import md5

import requests


class BaiduTranslator():
    def __init__(self, appid, appkey):
        self.appid = appid
        self.appkey = appkey
        self.endpoint = 'http://api.fanyi.baidu.com'
        self.path = '/api/trans/vip/translate'
        self.url = self.endpoint + self.path
        self.headers = {'Content-Type': 'application/x-www-form-urlencoded'}

    def get_result(self,  query, from_lang='en', to_lang='zh') -> list:
        query = "\n".join(query)
        salt = random.randint(32768, 65536)
        sign = make_md5(self.appid + query + str(salt) + self.appkey)

        payload = {'appid': self.appid, 'q': query, 'from': from_lang,
                   'to': to_lang, 'salt': salt, 'sign': sign}
        r = requests.post(self.url, params=payload, headers=self.headers)
        result_json = r.json()

        trans_result = result_json['trans_result']

        result = []

        for item in trans_result:
            result.append(item['dst'])

        return result


def make_md5(s, encoding='utf-8'):
    return md5(s.encode(encoding)).hexdigest()
