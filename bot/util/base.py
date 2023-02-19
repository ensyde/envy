from abc import ABC, abstractmethod
from socket import socket, AF_INET, SOCK_STREAM
import logging
import asyncio


class Base(ABC):
    def __init__(self):
        self.log = logging.getLogger("Bot")
        self.__connected = False
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
                "PING": ""
                }

    @property
    def connected(self):
        return self.__connected

    @abstractmethod
    def disconnect(self):
        pass 

class SyncBase(Base):
    def __init__(self) -> None:
        super().__init__()
        self._socket = None

    def connect(self, host, port):
        if not isinstance(host, str) or not isinstance(port, int):
            raise ValueError(f"[ERR] {__class__}.{__name__} requires host: str and port: int")

        try:
            self._socket = socket(AF_INET, SOCK_STREAM)
            self._socket.connect(host, port)
        except Exception as ex:
            self.log.error(f"[ERR] Error while connecting...")
            self.log.error(f"[ERR] Exception raised: {ex}")


class AsyncBase(Base):
    def __init__(self) -> None:
        super().__init__()
        self.__reader, self.__writer = None

    async def connect(self, host="ash.wserv.org", port=6112):
        if not isinstance(host, str) or not isinstance(port, int):
            raise ValueError(f"[ERR] {__class__}.{__name__} requires host: str and port: int")

        self.log.info(f"Connecting to {host}:{port}")
        try:
            self.__reader, self.__writer = \
                await asyncio.open_connection(host, port, family=AF_INET)
        except Exception as ex:
            self.log.error(f"[ERR] Error while connecting...")
            self.log.error(f"[ERR] Exception raised: {ex}")
            return False

        self.log.info(f"Connected to {host}")
        self.__connected = True

        loop = asyncio.get_event_loop()
