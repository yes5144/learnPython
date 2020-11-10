# coding: utf8
# https://zhuanlan.zhihu.com/p/46948464
import datetime
import os
from apscheduler.schedulers.blocking import BlockingScheduler


def tick():
    print('Tick! the time is: %s' % datetime.datetime.now())


if __name__ == "__main__":
    scheduler = BlockingScheduler()
    # scheduler.add_job(tick, 'interval', seconds=3)
    scheduler.add_job(tick, 'cron', hour=9, minute=47)
    print('Press Ctrl+{0} to exit'.format('Break' if os.name ==
                                          'nt' else 'c   '))
    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        print('exiiiiit ok ')

# https://www.cnblogs.com/mangM/p/11187015.html
# http://sinhub.cn/2018/11/apscheduler-user-guide/