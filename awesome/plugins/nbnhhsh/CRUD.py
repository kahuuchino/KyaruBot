import json
from os import path


def add_to_json(abbr: str) -> str:
    cmd = ''
    with open(path.join(path.dirname(__file__), 'database.json'), 'r', encoding='utf8')as fp:
        data = json.load(fp)
    operate = abbr.split(':')
    if len(operate) != 2:
        cmd = '输入参数有误，请用冒号分隔'
        return cmd
    if data.get(operate[0], 0) != 0:
        cmd = operate[0] + '已经存在，原值为' + operate[1] + '\n'
        print('too more key')
    data[operate[0]] = operate[1]
    cmd = cmd + "已增加新字典 " + operate[0] + ':' + operate[1]
    with open(path.join(path.dirname(__file__), 'database.json'), 'w+', encoding='utf8')as fp:
        json.dump(data, fp)
    return cmd


def del_to_json(abbr: str) -> str:
    cmd = ''
    with open(path.join(path.dirname(__file__), 'database.json'), 'r', encoding='utf8')as fp:
        data = json.load(fp)
    operate = abbr.split(':')
    # flag = 0
    for index in range(0,len(operate)):
        if data.get(operate[index], 0) != 0:
            del data[operate[index]]
            cmd = '已删除' + operate[index]
            # print('too more key')
            break
        else:
            cmd = '需删除条目不存在'
    with open(path.join(path.dirname(__file__), 'database.json'), 'w+', encoding='utf8')as fp:
        json.dump(data, fp)
    return cmd


if __name__ == "__main__":
    cmd1 = del_to_json("123:123")
    print(cmd1)
