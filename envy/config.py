import os.path
import json


CFGDIR = "configs/"
FILENAME = "config.json"


class LoginConfig:
    acct: str
    pw: str
    home: str


class BncsConfig:
    host: str
    port: int
    game: str
    cdkey: str
    xpkey: str
    verbyte: str


class BnlsConfig:
    enabled: bool
    host: str
    port: int


class OptsConfig:
    trigger: str


class Config:
    login: LoginConfig
    bncs: BncsConfig
    bnls: BnlsConfig
    opts: OptsConfig

    @staticmethod
    def load(filename: str = FILENAME):
        file = CFGDIR + filename
        with open(file, "r") as f:
            data = json.load(f)
        return Config(**data)
