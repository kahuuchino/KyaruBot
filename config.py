from nonebot.default_config import *
from datetime import timedelta

# 配置管理员
SUPERUSERS = {386302912}

# 命令起始符
COMMAND_START = {'!',  '！', '#', ''}

# 反代地址与端口
HOST = '127.0.0.1'
PORT = 8086

SESSION_CANCEL_EXPRESSION = (
    '好的',
    '好的吧',
    '好吧，那就不打扰啦'
)


# SESSION_RUN_TIMEOUT = timedelta(seconds=10)

if __name__ == "__main__":
    print('AMD YES')
