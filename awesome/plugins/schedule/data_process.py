import json
import time
from os import path
from datetime import datetime

switch = {
    "周一": 0,
    "周二": 1,
    "周三": 2,
    "周四": 3,
    "周五": 4,
    "周六": 5,
    "周日": 6,
    "周天": 7,
}


def get_day(day: str) -> int:
    if day.find('今') != -1:
        tday = time.localtime(time.time()).tm_wday
    elif day.find('明') != -1:
        tday = time.localtime(time.time()).tm_wday + 1
        if tday == 7:
            tday = 0
    elif day.find('后天') != -1:
        tday = time.localtime(time.time()).tm_wday + 2
        if tday == 7:
            tday = 0
        elif tday == 8:
            tday = 1
    elif day.find('昨') != -1:
        tday = time.localtime(time.time()).tm_wday - 1
        if tday == -1:
            tday = 6
    else:
        tday = -1
    return tday


def get_schedule() -> str:
    print("into get_schedule")
    # 读取json中的课程数据
    # print(type(day))
    with open(path.join(path.dirname(__file__), 'data.json'), 'r', encoding='utf8')as fp:
        data = json.load(fp)

    # 初始化
    str_o = ""
    flag = 0

    # 拼接课表
    # for i in range(0, len(data['lesson'])):
        # str_o += "\n"
        # str_o += data['lesson'][i]['name']
        # str_o += " "
        # str_o += data['lesson'][i]['type']
        # str_o += "\n"
        # str_o += "时间："
        # str_o += data['lesson'][i]['time']
        # str_o += "\n"

    cur_day = datetime.now()
    next_day = datetime(2020, 12, 24)
    day = (next_day - cur_day).days
    str_o += "\n距离考研还有"
    str_o += str(day)
    str_o += "天，今天你学习了吗？\n"
    str_o += '不会有人不学习吧，不会吧不会吧不会吧\n'

    return str_o


if __name__ == '__main__':
    print(get_schedule())
