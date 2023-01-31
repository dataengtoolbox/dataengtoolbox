import time
import datetime as dt
from typing import Optional

from dataengtoolbox.utils import hello, timeit
from dataengtoolbox.version import version


# Command Line Interface
class CLI:

    def __init__(self):
        self.version = version
        self.execution_timestamp = dt.datetime.utcnow()

    def hello(self, name: Optional[str] = None):
        return hello(name=name)

    def add(self, *args) -> int:
        return sum(args)

    @timeit
    def sleep(self, duration: int = 3):
        time.sleep(duration)

    @staticmethod
    def square(num: int) -> int:
        return num ** 2


CLI.square(num=5)
