import sys
# reload(sys)
# sys.setdefaultencoding('utf8')

from os import path
import argparse
import os
import requests
import json
from requests import ReadTimeout


def strToJson(jstr):
    print(jstr)
    jbean = json.loads(jstr)
    result = ''

    for data in jbean:
        result = result + data['name'] + '\n'

        if 'trans' in data:
            for dt in data['trans']:
                result = result + dt + '\n'

        if 'inputting' in data:
            if 0 < len(data['inputting']):
                result = result + '可能是\n'
                for di in data['inputting']:
                    result = result + di + '\n'
            else:
                result = result + '尚未录入\n'

    return result[:-1]


async def getTranslation(text):
    url = "https://lab.magiconch.com/api/nbnhhsh/guess"
    data = {"text": text}
    print(text)
    # print(type(text))
    try:
        with open(path.join(path.dirname(__file__), 'database.json'), 'r', encoding='utf8') as fp:
            database = json.load(fp)
        res = requests.post(url=url, data=data)
        print(res.text)
        # print(type(res.text))
        str_user = database.get(text, 'None')
        if res.status_code == 200:
            if str_user != 'None':
                if res.text[len(res.text)-4] == '[':
                    return strToJson(res.text[0:len(res.text) - 3] + '\"' + str_user + '\"]}]')
                return strToJson(res.text[0:len(res.text) - 3] + ',\"' + str_user + '\"]}]')
            return strToJson(res.text)
    except (ConnectionError, ReadTimeout):
        print('Crawling Failed', url)
        # return strToJson('[{[\"网络连接失败!\",\"' + text + '\",\"' + str_user + '\"]}]')
        return
    except IOError:
        print('IO Failed')
        # return strToJson('IOError')
        return


if __name__ == '__main__':
    str1 = getTranslation('xxxybm')
    print(str1)
