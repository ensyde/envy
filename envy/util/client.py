import asyncio
from abc import ABC


class BaseClient(ABC):
    def __init__(self):
        super().__init__()
        self._connected = False

    @property
    def connected(self):
        return self._connected


