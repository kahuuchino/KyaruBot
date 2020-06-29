from nonebot import on_command, CommandSession
from .getTrans import getTranslation
from .CRUD import add_to_json
from .CRUD import del_to_json


__plugin_name__ = '能不能好好说话'
__plugin_usage__ = r"""
缩写翻译

命令：缩写 [英文缩写]
本功能需要@机器人使用
自建词条命令：学英语 [英文缩写]:[中文名称]
删除指定词条命令：删英语 [英文缩写]
"""


# 注册nbnhhsh函数为命令处理器
@on_command('nbnhhsh', aliases=('缩写', '查缩写',))
async def nbnhhsh(session: CommandSession):
    # 获取英文缩写
    abbr = session.get('abbr', prompt='你想查哪个？')
    # 获取全名
    full = await getTranslation(abbr)
    # 发送全名
    await session.send(full)


@on_command('addabbr', aliases=('增加词条', '学英语'))
async def addabbr(session: CommandSession):
    # 获取增加的词典
    abbr = session.get('abbr', prompt='你想说哪个？')
    print(abbr)
    # 添加进文件
    full = add_to_json(abbr)
    # 发送结果
    await session.send(full)
    return


@on_command('delabbr', aliases=('删除词条', '删英语'))
async def delabbr(session: CommandSession):
    # 获取要删除的词典
    abbr = session.get('abbr', prompt='你想说哪个？')
    print(abbr)
    # 添加进文件
    full = del_to_json(abbr)
    # 发送结果
    await session.send(full)
    return


# 注册analysis函数为命令解析器
@nbnhhsh.args_parser
@addabbr.args_parser
@delabbr.args_parser
async def _(session: CommandSession):
    # 去掉消息首尾的空白符
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        # 该命令第一次运行（第一次进入命令会话）
        if stripped_arg:
            # 第一次运行参数不为空，意味着用户直接将缩写跟在命令名后面，作为参数传入
            session.state['abbr'] = stripped_arg
        return

    if not stripped_arg:
        # 用户没有发送有效的缩写（而是发送了空白字符）
        session.pause('你想说哪个？')

    # 如果当前正在向用户询问更多信息，且用户输入有效，则放入会话状态
    session.state[session.current_key] = stripped_arg
