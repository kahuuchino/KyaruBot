from datetime import datetime

import nonebot
import pytz
from aiocqhttp.exceptions import Error as CQHttpError

import sys
sys.path.append("..")
from ..schedule.data_process import get_schedule


@nonebot.scheduler.scheduled_job('cron', hour=7, minute=55)
async def f1():
    await send_schedule()


@nonebot.scheduler.scheduled_job('cron', hour=9, minute=55)
async def f2():
    await send_schedule()


@nonebot.scheduler.scheduled_job('cron', hour=13, minute=55)
async def f3():
    await send_schedule()


@nonebot.scheduler.scheduled_job('cron', hour=15, minute=55)
async def f4():
    await send_schedule()


# @nonebot.scheduler.scheduled_job('cron', hour=16, minute=5, second=20)
# async def f5():
    # await send_schedule()


async def send_schedule():
    bot = nonebot.get_bot()
    now = datetime.now(pytz.timezone('Asia/Shanghai'))
    try:
        msg = get_schedule('今天')
        await bot.send_group_msg(group_id=838698027, message=msg, auto_escape=True)
        # await bot.call_action('send_private_msg', {'user_id': 386302912, 'message': msg})

    except CQHttpError:
        pass


if __name__ == '__main__':
    msg2 = get_schedule("今天")
    print(type(msg2))
    print(type(f'hello'))
