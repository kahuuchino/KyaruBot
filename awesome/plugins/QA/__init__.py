from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand
import json
from os import path
from jieba import posseg
from .QA import add
from .QA import delete


__plugin_name__ = '我问你答'
__plugin_usage__ = r"""
我问你答

命令:我问[问题内容]你答[回答内容]
本功能需要@机器人使用
添加问题内容后，直接在群里发送问题内容时机器人会自动回复，无需@
若需删除已添加的问题，请使用
命令:忘掉 [问题内容]
"""


@on_command('add')
async def add(session: CommandSession):
    # message = session.state.get('msg')
    print(type(session))
    print(session)
    print(type(session.args))
    print(session.args)
    msg = session.args['msg']
    ask = session.args['ask']
    ans = session.args['answer']

    if search(ask, ans):
        if ask != '' and ans != '':

            with open(path.join(path.dirname(__file__), 'data.json'), 'r', encoding='utf8')as fp:
                data = json.load(fp)

            data[ask] = ans

            with open(path.join(path.dirname(__file__), 'data.json'), 'w+', encoding='utf8')as fp:
                json.dump(data, fp)

            await session.send('又学到了没用的东西')
    else:
        await session.send('爬')


@on_command('qa')
async def qa(session: CommandSession):
    message = session.state.get('msg')
    with open(path.join(path.dirname(__file__), 'data.json'), 'r', encoding='utf8')as fp:
        data = json.load(fp)
    if data.get(message) != None:
        await session.send(data[message])


@on_command('remove', aliases=('忘掉',), only_to_me=True)
async def remove(session: CommandSession):
    message = session.state.get('msg')
    if message.find('凯露') == -1 or message.find('喵帕斯') == -1:
        delete(message)
        await session.send('奇怪的知识减少了')
    else:
        await session.send('爪巴')



@remove.args_parser
async def _(session: CommandSession):
    # 去掉消息首尾的空白符
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        # 该命令第一次运行（第一次进入命令会话）
        if stripped_arg:
            # 第一次运行参数不为空，意味着用户直接将日期跟在命令名后面，作为参数传入
            session.state['msg'] = stripped_arg
        return


@on_natural_language(keywords='我问', only_to_me=False)
async def _(session: NLPSession):
    msg = session.msg
    # print(msg)
    # words = posseg.lcut(msg)
    flag_ask = msg.find('我问')
    flag_ans = msg.find('你答')
    if flag_ans == -1:
        return
    ask = msg[flag_ask+2:flag_ans]
    answer = msg[flag_ans+2:]
    # for word in words:
        # print(word.word)
        # if flag_ask == 1:
            # ask += word.word
        # if flag_ans == 1:
            # answer += word.word
        # if word.word == '问':
            # flag_ask = 1
        # if word.word == '答':
            # flag_ask = 0
            # flag_ans = 1
        # print(word.flag)
    # flag_ask = 0
    # flag_ans = 0
    print(ask)
    print(answer)
    # 以置信度 60.0 返回 tuling 命令
    # 确保任何消息都在且仅在其它自然语言处理器无法理解的时候使用 tuling 命令
    return IntentCommand(90.0, 'add', args={'msg': msg, 'ask': ask, 'answer': answer})


@on_natural_language(only_to_me=False)
async def _(session: NLPSession):
    msg = session.msg
    return IntentCommand(60.0, 'qa', args={'msg': msg})


id_list = [
    '凯露',
    '喵帕斯',
    '优衣'
]


def search(ask, ans):
    for i in range(0, len(id_list)):
        if ask.find(id_list[i]) != -1 or ans.find(id_list[i]) != -1:
            return 0
    return 1
