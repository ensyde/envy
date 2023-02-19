from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread
from dotenv import load_dotenv
import logging

load_dotenv("../")
log = logging.getLogger(__name__)
class Envy:
    def __init__(self) -> None:
        self.bots = []

    
    def __len__(self):
        return len(self.bots)
