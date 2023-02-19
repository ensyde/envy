from asyncio import Queue, sleep
import time

class AsyncQueue(Queue):
    def __init__(self, maxsize: int = ...):
        super().__init__(maxsize)

    async def get(self):
        return await super().get()

    async def get_nowait(self) -> _T:
        return super().get_nowait()

    async def put(self, item):
        return await super().put(item)
