from config import Config
from time import time
import logging
import asyncio


log = logging.getClient("bot")


class Bot:
    def __init__(self, loop=asyncio.get_event_loop()):
        self.loop = loop
        self.logger = log
        self.startedat = time()
        self.running = True
        self.config = Config.load()
        log.debug("Config file loaded.")

    def run(self):
        pass

    def stop(self):
