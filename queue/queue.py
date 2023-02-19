from threading import Thread, Lock
from queue import Queue
import time

class MsgQueue(Thread):
    def __init__(self):
        super().__init__(self)
        self.msgs = Queue()

    def run(self):
        pass
