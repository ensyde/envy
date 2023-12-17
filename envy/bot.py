from config import Config
from bncs.client import BncsClient
from time import time
import logging
import asyncio


log = logging.getLogger("bot")


class Bot:
    def __init__(self, loop=asyncio.get_event_loop()):
        self.loop = loop
        self.logger = log
        self.startedat = time()
        self.running = True
        self.config = Config.load()
        log.debug("Config file loaded.")

    async def run(self):
        host = self.config.bncs.host
        port = self.config.bncs.port
        bncs = BncsClient(self)
        await bncs.connect(host, port)

    def stop(self):
        pass
