from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand
import nonebot
import pytz
from datetime import datetime
import json
from os import path


@on_command('tm')
async def tm(session: CommandSession):
    m = session.state.get('msg')
    bot = nonebot.get_bot()
    now = datetime.now(pytz.timezone('Asia/Shanghai'))
    await bot.send_group_msg(group_id=814975474, message=m)


# @on_natural_language(only_to_me=True)
# async def _(session: NLPSession):
    # msg = session.msg
    # print(msg)
    # 以置信度 60.0 返回 tuling 命令
    # 确保任何消息都在且仅在其它自然语言处理器无法理解的时候使用 tuling 命令
    # return IntentCommand(60.0, 'tm', args={'msg': msg})
