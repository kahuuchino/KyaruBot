import sys
# reload(sys)
# sys.setdefaultencoding('utf8')

import argparse
import os
import requests
import json


def strToJson(jstr):
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
    res = requests.post(url=url, data=data)
    print(res.text)
    return strToJson(res.text)


if __name__ == '__main__':
    str1 = getTranslation('xxxybm')
    print(str1)
