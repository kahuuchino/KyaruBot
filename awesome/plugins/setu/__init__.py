from nonebot import on_command, CommandSession
from .setu import get_setu
from .setu import get_erciyuan


__plugin_name__ = '色图'
__plugin_usage__ = r"""
发色图

命令：色图
本功能需要@机器人使用
本功能在22:00-24:00时启用，其他时间回复二次元表情包，此外在每天12:00和18:00自动发送一张图片
"""


@on_command('setu', aliases=('色图',), only_to_me=True)
async def setu(session: CommandSession):
    reply = await get_erciyuan()
    # 发送结果
    # if reply != '':
    print(reply[1])
    print(type(reply[1]))
    if reply[1] == 0:
        await session.send(reply[0])
    else:
        await session.send(reply[0])
        # await session.send('PID: %d \n当前色图发送几率为33' % reply[1])
