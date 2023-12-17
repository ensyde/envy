import os.path
import json


CFGDIR = "configs/"
FILENAME = "config.json"


class Config:
    acct: str
    pw: str
    home: str
    host: str
    port: int
    game: str
    cdkey: str
    xpkey: str
    verbyte: str

    @staticmethod
    def load(filename: str = FILENAME):
        file = CFGDIR + filename
        with open(file, "r") as f:
            data = json.load(f)
        return Config(**data)
