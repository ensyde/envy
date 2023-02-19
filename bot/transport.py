import asyncio
import random

from asyncio import Protocol

from typing import Sequence, Optional, Tuple, Callable, Dict, Coroutine, AnyStr, TYPE_CHECKING, Any


class BotProtocol(Protocol):
    def __init__(self, host, port, username, 
                 pw, home, logger=None,
                 loop=None):
        self.logger = logger
        self.host = host
        self.port = port

        self.username = username
        self.pw = pw
        self.home = home

        self.buf = b""
        self.loop = loop or asyncio.get_event_loop()

        self.handlers: Dict[int, Tuple[str, Callable]] = {}

    def register(self, cmd, handler):
        _id = 0
        while not _id or _id in self.handlers:
            _id = random.randint(1, (2 ** 32) - 1)
        self.handlers[_id] = (cmd, handler)
        return _id

    def unregister(self, _id):
        del self.handlers[_id]
