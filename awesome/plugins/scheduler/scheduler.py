from datetime import datetime

def get_lasttime() -> str:
    # str_o = ''
    cur_day = datetime.now()
    next_day = datetime(2020, 12, 24)
    day = (next_day - cur_day).days
    str_o = "距离考研还有" + str(day) + "天，今天你学习了吗？\n"
    return str_o


if __name__ == "__main__":
    print(get_lasttime())
