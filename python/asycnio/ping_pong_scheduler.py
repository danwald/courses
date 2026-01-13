import time
import uuid
from collections import deque
from typing import Generator


class Task:
    def __init__(self, coro: Generator):
        self.id = uuid.uuid4()
        self._coro = coro
        self.val = None

    def run(self):
        return self._coro.send(self.val)


class Scheduler:
    def __init__(self):
        self._queue = deque([])

    def create_task(self, coro: Generator):
        task = Task(coro)
        self._queue.append(task)

    def run_forever(self):
        while self._queue:
            task = self._queue.pop()
            try:
                task.run()
                self._queue.appendleft(task)
            except StopIteration as err:
                print(err.value)


def ping():
    while True:
        print("ping")
        time.sleep(1)
        (yield)


def pong():
    while True:
        print("pong")
        time.sleep(1)
        (yield)


if __name__ == "__main__":
    scheduler = Scheduler()
    scheduler.create_task(ping())
    scheduler.create_task(pong())
    scheduler.run_forever()
