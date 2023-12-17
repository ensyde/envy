import asyncio
import logging


log = logging.getLogger("bncs")


class BncsClient:
    def __init__(self, bot):
        self.bot = bot
        self._connected = False
        # self.reader = None
        # self.writer = None
        self.log = log

    @property
    def connected(self):
        return self._connected

    async def connect(self, host: str, port: int):
        try:
            self.reader, self.writer = await asyncio.open_connection(
                    host, port
                )
        except (OSError, ConnectionError):
            log.error("Failed to connect")
            self._connected = False
            return False
        self._connected = True
        log.info(f"Successfully connected to {host}:{port}")
        return True

    def disconnect(self):
        if not self.connected:
            return
        self.writer.close()

    async def wait_close(self):
        if not self.connected:
            return
        await self.writer.wait_closed()

    async def recv(self):
        pass

    async def send(self, pkt):
        pass
