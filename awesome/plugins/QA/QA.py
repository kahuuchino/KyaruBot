import json
from os import path


async def add(self, ask, ans):

    with open(path.join(path.dirname(__file__), 'data.json'), 'r', encoding='utf8')as fp:
        data = json.load(fp)

    data[ask] = ans

    with open(path.join(path.dirname(__file__), 'data.json'), 'w+', encoding='utf8')as fp:
        json.dump(data, fp)

    return


def delete(key):

    with open(path.join(path.dirname(__file__), 'data.json'), 'r', encoding='utf8')as fp:
        data = json.load(fp)

    del data[key]

    with open(path.join(path.dirname(__file__), 'data.json'), 'w+', encoding='utf8')as fp:
        json.dump(data, fp)

    return


if __name__ == '__main__':
    add('1', '2')
