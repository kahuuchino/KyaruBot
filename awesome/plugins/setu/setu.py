# -*- coding: UTF-8 -*-
import requests
import os
import json
import time
from contextlib import closing
from os import path
from urllib.request import urlretrieve
import urllib.request
import random


param = {
    'apikey': '699356085ee39102792ec7',
    'r18': 0,
    'keyword': '',
    'num': 1,
    'proxy': 'i.pixiv.cat',
    'size1200': ''
}


url = 'https://api.lolicon.app/setu/'


async def get_setu():
    ret = requests.get(url, params=param)
    res = json.loads(ret.text)
    img_url = res['data'][0]['url']
    imgname = str(res['data'][0]['pid']) + img_url[len(img_url)-4:len(img_url)]
    # print(filename)
    if os.path.exists(path.join(path.dirname(__file__), imgname)) == False:
        # download(img_url, ('./%s' % filename))
        dl(img_url, imgname)
        print('down:%s ' % img_url)
    CQ = '[CQ:image,file=file:///' + path.join(path.dirname(__file__), imgname) + ']'
    print(CQ)
    return CQ, res['data'][0]['pid']


def download(img_url, img_path):
    errortext = ''
    try:
        res = requests.get(img_url)
        with open(img_path, "wb") as file:
            file.write(res.content)
    except:
        print('Failed to down url:%s, path:%s' % (img_url, img_path))
        errortext = errortext + '<Failed to down url:%s, path:%s>' % (img_url, img_path)


def dl(img, imgname):
    try:
        img_name = imgname
        filename = "D:\\source\\schedulerobot\\src\\awesome\\plugins\\setu\\" + img_name
        imgres = requests.get(img)
        print(filename)
        with open(filename, "wb") as f:
            f.write(imgres.content)
    except:
        print('Failed to down url:%s' % img)
        # return "failed"


async def get_erciyuan():
    t = time.localtime()
    if t.tm_hour >= 22:
        return await get_setu()
    else:
        num = random.randint(1, 8)
        name = str(num) + '.jpg'
        CQ = '[CQ:image,file=file:///' + path.join(path.dirname(__file__), name) + ']'
        print(CQ)
        return CQ, 0


if __name__ == '__main__':
    get_setu()
    # dl('https://i.pixiv.cat/img-master/img/2018/05/04/12/00/01/68567517_p0_master1200.jpg')
