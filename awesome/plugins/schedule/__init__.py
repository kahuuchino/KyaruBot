from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand
from jieba import posseg

from .data_process import get_schedule


# 注册schedule函数为命令处理器
@on_command('schedule', aliases=('近期考试', '考试',), only_to_me=True)
async def schedule(session: CommandSession):

    # day = session.get('day', prompt='哪天？')

    timetable = get_schedule()

    await session.send(timetable)


# 注册analysis函数为命令解析器
# @schedule.args_parser
# async def _(session: CommandSession):
    # 去掉消息首尾的空白符
    # stripped_arg = session.current_arg_text.strip()

    # if session.is_first_run:
        # 该命令第一次运行（第一次进入命令会话）
        # if stripped_arg:
            # 第一次运行参数不为空，意味着用户直接将日期跟在命令名后面，作为参数传入
            # session.state['day'] = stripped_arg
        # return

    # if not stripped_arg:
        # 用户没有发送有效的日期（而是发送了空白字符）
        # session.pause('哪天？')

    # 如果当前正在向用户询问更多信息，且用户输入有效，则放入会话状态
    # session.state[session.current_key] = stripped_arg


# on_natural_language 装饰器将函数声明为一个自然语言处理器
# @on_natural_language(keywords={'课表'}, only_to_me=True)
# async def _(session: NLPSession):
    # 去掉消息首尾的空白符
    # stripped_msg = session.msg_text.strip()
    # 对消息进行分词和词性标注
    # words = posseg.lcut(stripped_msg)

    # day = None
    # operate = None
    # 遍历 posseg.lcut 返回的列表
    # for word in words:
        # 每个元素是一个 pair 对象，包含 word 和 flag 两个属性，分别表示词和词性
        # if word.flag == 't':
            # day = word.word
            # break
        # if word.flag == 'v':
        # operate = word.word
        # break

    # 返回意图命令，前两个参数必填，分别表示置信度和意图命令名
    # return IntentCommand(90.0, 'schedule', current_arg=day or '')
