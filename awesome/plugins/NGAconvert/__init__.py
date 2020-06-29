from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand
from jieba import posseg

from .nga2md import ngalink


@on_command('ngaconvert', aliases=('CQ:rich',))
async def ngaconvert(session: CommandSession):
    message = session.state.get('msg')
    # if message.find('NGA玩家社区') != -1:
        # print('into function')
        # reply = await ngalink(message)
        # print(reply)
        # await session.send(reply)
            # await session.send(reply)


@on_natural_language(keywords={'CQ:rich'}, only_to_me=False)
async def _(session: NLPSession):
    msg = session.msg
    # print(msg)
    # 以置信度 60.0 返回 tuling 命令
    # 确保任何消息都在且仅在其它自然语言处理器无法理解的时候使用 tuling 命令
    return IntentCommand(60.0, 'ngaconvert', args={'msg': msg})
