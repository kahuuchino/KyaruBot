from nonebot import on_command, CommandSession
from .getTrans import getTranslation


# 注册nbnhhsh函数为命令处理器
@on_command('nbnhhsh', aliases=('缩写', '查缩写',))
async def nbnhhsh(session: CommandSession):
    # 获取日期
    abbr = session.get('abbr', prompt='你想查哪个？')
    # 拼接课程表
    full = await getTranslation(abbr)
    # 发送课程表
    await session.send(full)

# 注册analysis函数为命令解析器
@nbnhhsh.args_parser
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
        session.pause('你想查哪个？')

    # 如果当前正在向用户询问更多信息，且用户输入有效，则放入会话状态
    session.state[session.current_key] = stripped_arg