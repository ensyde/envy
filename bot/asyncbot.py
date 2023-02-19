import asyncio
import logging
from ..queue.async_queue import AsyncQueue
from .util.base import AsyncBase

class AsyncBot(AsyncBase):
    def __init__(self) -> None:
        super().__init__()
        self.config = {}

        self.channel = None
        self.users = set()
        self.banned_users = []
        self.events = {
                "TALK": "",
                "JOIN":"",
                "LEAVE": "",
                "WHISPER": "",
                "EMOTE": "",
                "TOPIC":"",
                "INFO": "",
                "OK": "",
                "FAIL": "",
                "PING": ","
                }

    async def connect(self):
        pass

    def disconnect(self):
        pass

    async def rc(self):
        pass

    async def send(self, msg):
        pass

    async def run(self):
        pass


