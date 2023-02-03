# import socket as net
from bot import Bot
from util.log import log
from threading import Thread
from consts import NAME, VER, AUTHOR


def connect(bot):
    bot.connect()
    bot.login()
    _recv = Thread(target=bot.loop, args=[])
    _input = Thread(target=_user_input, args=[bot])
    _recv.start()
    _input.start()


def main():
    log.bot(NAME)
    log.bot(f"ver{VER}")
    log.bot(AUTHOR)
    bot = Bot()
    print(bot.config.username)
    print(bot.config.port)
    connect(bot)


def _user_input(bot):
    while True:
        msg = input("")
        if msg == "/shitlist":
            log.bot(bot.config.shitlist)
        elif msg == "/userlist":
            for u in bot.channel.userlist:
                log.bot(u)
        elif msg == "/ver":
            log.bot(f"{NAME} :: {VER} :: {AUTHOR}")
        else:
            bot.send(msg)


if __name__ == '__main__':
    main()
