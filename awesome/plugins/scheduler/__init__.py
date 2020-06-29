from datetime import datetime
from ..schedule.data_process import get_schedule
from ..setu.setu import get_setu
from ..setu.setu import get_erciyuan

import nonebot
import pytz
from aiocqhttp.exceptions import Error as CQHttpError
from .scheduler import get_lasttime

import sys
sys.path.append("..")


@nonebot.scheduler.scheduled_job('cron', hour=12, minute=00)
@nonebot.scheduler.scheduled_job('cron', hour=18, minute=00)
async def f1():
    await send_schedule()


@nonebot.scheduler.scheduled_job('cron', hour=18, minute=1)
async def f2():
    await send_lasttime()


@nonebot.scheduler.scheduled_job('cron', hour=12, minute=00)
@nonebot.scheduler.scheduled_job('cron', hour=18, minute=2)
async def f5():
    await send_setu()


# @nonebot.scheduler.scheduled_job('cron', hour=16, minute=5, second=20)
# async def f5():
    # await send_schedule()


async def send_schedule():
    bot = nonebot.get_bot()
    now = datetime.now(pytz.timezone('Asia/Shanghai'))
    try:
        msg = get_schedule()
        await bot.send_group_msg(group_id=838698027, message=msg, auto_escape=True)
        await bot.send_group_msg(group_id=808619692, message=msg, auto_escape=True)
        # await bot.call_action('send_private_msg', {'user_id': 386302912, 'message': msg})

    except CQHttpError:
        pass


async def send_setu():
    bot = nonebot.get_bot()
    now = datetime.now(pytz.timezone('Asia/Shanghai'))
    try:
        msg = await get_setu()
        await bot.send_group_msg(group_id=130095390, message=msg[0])
        # await bot.call_action('send_private_msg', {'user_id': 386302912, 'message': msg})

    except CQHttpError:
        pass


async def send_lasttime():
    bot = nonebot.get_bot()
    now = datetime.now(pytz.timezone('Asia/Shanghai'))
    try:
        msg = get_lasttime()
        await bot.send_group_msg(group_id=130095390, message=msg)
        msg = await get_erciyuan()
        await bot.send_group_msg(group_id=130095390, message=msg[0])
        # await bot.call_action('send_private_msg', {'user_id': 386302912, 'message': msg})

    except CQHttpError:
        pass


if __name__ == '__main__':
    msg2 = get_schedule()
    print(type(msg2))
    print(type(f'hello'))
