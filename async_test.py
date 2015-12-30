#! /usr/bin/env python

# Python 3 forward compatability imports.
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from __future__ import unicode_literals

import uweclang
import trollius as asyncio
from trollius import From

# Configure logging.
import logging
logger = logging.getLogger('uweclang')
sh = logging.StreamHandler()
sh.setFormatter(logging.Formatter(
    '[%(name)s] %(filename)s:%(lineno)d at %(asctime)s: %(levelname)s %(message)s',
    '%H:%M:%S'
))
logger.addHandler(sh)
logger.setLevel(logging.DEBUG)

@asyncio.coroutine
def factorial(name, number):
    f = 1
    for i in range(2, number+1):
        print("Task %s: Compute factorial(%s)..." % (name, i))
        logger.debug('test message')
        yield From(asyncio.sleep(1))
        f *= i
    print("Task %s: factorial(%s) = %s" % (name, number, f))


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    tasks = [
        asyncio.ensure_future(factorial("A", 2)),
        asyncio.ensure_future(factorial("B", 3)),
        asyncio.ensure_future(factorial("C", 4))]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
    logging.shutdown()
    print('Done')
