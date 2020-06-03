import json
# import sys
from os import path
# sys.path.append("..")


def modify_schedule(operate: str) -> int:
    with open(path.join(path.dirname(__file__), '..', 'schedule', 'data.json'), 'r', encoding='utf8')as fp:
        data = json.load(fp)
    flag = 1
    lesson = operate.split(',')
    for index in data['lesson']:
        if index['name'] == lesson[0]:
            index['id'] = lesson[1];
            if len(lesson) == 3:
                index['passwd'] = lesson[2]
            else:
                index['passwd'] = '-1'
            flag = 0
            break
    with open(path.join(path.dirname(__file__), '..', 'schedule', 'data.json'), 'w+', encoding='utf8')as fp:
        json.dump(data, fp)
    if flag == 0:
        return 1
    else:
        return 0


if __name__ == "__main__":
    cmd = modify_schedule("DSP原理及应用,123456,123")
    print(cmd)
