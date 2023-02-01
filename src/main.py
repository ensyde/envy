from bot import Bot
from util.log import log
from threading import Thread


def connect(bot):
    bot.connect()
    bot.login()
    _recv = Thread(target=bot.loop, args=[])
    _input = Thread(target=_user_input, args=[bot])
    _recv.start()
    _input.start()


def main():
    log.bot("Envy Bot")
    log.bot("v0.0.2")
    log.bot("P$Y/Omen")
    bot = Bot()
    print(bot.config.username)
    print(bot.config.port)
    connect(bot)


def _user_input(bot):
    while True:
        msg = input("")
        if msg:
            bot.send(msg)


if __name__ == '__main__':
    main()

