from threading import Thread
from socket import socket, AF_INET, SOCK_STREAM

class Bot(Thread):
    def __init__(self, botid):
        Thread.__init__(self)
        self.config = {}

        self.socket = None
        self.__connected = False
        self.channel = ""

    @property
    def connected(self):
        return self.__connected
    
    @connected.setter
    def connected(self, val):
        if not type(val) == bool:
            raise ValueError("Bot.__connected requires a boolean value.")
        self.__connected = val
