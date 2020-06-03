import json
import time
from os import path

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
    elif day.find('后天') != -1:
        tday = time.localtime(time.time()).tm_wday + 2
    elif day.find('昨') != -1:
        tday = time.localtime(time.time()).tm_wday - 1
        if tday == -1:
            tday = 7
    else:
        tday = -1
    return tday


def get_schedule(day: str) -> str:
    print("into get_schedule")
    # 读取json中的课程数据
    # print(type(day))
    with open(path.join(path.dirname(__file__), 'data.json'), 'r', encoding='utf8')as fp:
        data = json.load(fp)

    # 分析日期
    tday = switch.get(day, get_day(day))
    if tday == -1:
        return

    # 初始化
    str_o = "当天课表:\n"
    flag = 0

    # 拼接课表
    for i in range(0, 5):
        lesson = data['time'][tday][i]
        if lesson == 0:
            flag = flag + 1
            continue

        str_o += "\n"
        str_o += data['lesson'][lesson-1]['name']
        str_o += "\n上课时间\n"
        str_o += data['timeline'][i]
        str_o += "\n会议id：\n"
        str_o += data['lesson'][lesson-1]['id']
        if data['lesson'][lesson-1]['passwd'] == "-1":
            str_o += "\n\n"
            continue

        str_o += "\n会议密码:\n"
        str_o += data['lesson'][lesson-1]['passwd']
        str_o += "\n"

    if flag == 5:
        str_o += "这天没有课哦"
    return str_o


if __name__ == '__main__':
    get_schedule("今天")
