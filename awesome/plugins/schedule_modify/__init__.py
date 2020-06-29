from nonebot import on_command, CommandSession
from .data_modify import modify_schedule
import sys
sys.path.append("../../..")
# import config


SUPERUSER = 386302912


# 注册schedule函数为命令处理器
@on_command('modify', aliases=('修改课表'), permission=SUPERUSER)
async def modify(session: CommandSession):
    # 获取修改内容
    operate = session.get('operate', prompt='输入修改内容')
    # 修改课程表
    cmd = modify_schedule(operate)
    # 发送结果
    if cmd == 1:
        await session.send(operate + '\n操作完成')
    else:
        await session.send('操作失败')

# 注册analysis函数为命令解析器
@modify.args_parser
async def _(session: CommandSession):
    # 去掉消息首尾的空白符
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        # 该命令第一次运行（第一次进入命令会话）
        if stripped_arg:
            # 第一次运行参数不为空，意味着用户直接将日期跟在命令名后面，作为参数传入
            session.state['operate'] = stripped_arg
        return

    if not stripped_arg:
        # 用户没有发送有效的日期（而是发送了空白字符）
        session.pause('输入修改内容')

    # 如果当前正在向用户询问更多信息，且用户输入有效，则放入会话状态
    session.state[session.current_key] = stripped_arg


@on_command('love', aliases=('48974654'), permission=SUPERUSER, only_to_me=True)
async def modify(session: CommandSession):
    await session.send('老公mua')
