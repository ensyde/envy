from colored import stylize, fg
from datetime import datetime
levels = ['TOPIC', 'INFO', 'JOIN', 'WHISPER', 'IN', 'DEBUG']


def ts():
    now = datetime.now().strftime("%I:%M%p")
    return now


class log:
    @staticmethod
    def bot(msg):
        print(f"[{ts()}][{stylize('BOT', fg('blue'))}]\t {msg}")

    @staticmethod
    def succ(msg):
        print(f"[{ts()}][{stylize('BOT', fg('green'))}]\t {msg}")

    @staticmethod
    def error(msg):
        print(f"[{ts()}][{stylize('BOT', fg('red'))}]\t {msg}")

    @staticmethod
    def fail(msg):
        print(f"[{ts()}][{stylize('FAIL', fg('red'))}]\t\t {msg}")

    @staticmethod
    def ping(packet):
        print(f"[{ts()}][{stylize('PING', fg('cyan_3'))}]\t {packet}")

    @staticmethod
    def pong(packet):
        print(f"[{ts()}][{stylize('PONG', fg('green'))}]\t {packet}")

    @staticmethod
    def err(msg):
        print(f"[{ts()}][{stylize('ERROR', fg('red'))}] {msg}")

    @staticmethod
    def topic(msg):
        print(f"[{ts()}][{stylize('TOPIC', fg('yellow'))}]\t {msg}")

    @staticmethod
    def info(msg):
        print(f"[{ts()}][{stylize('INFO', fg('cyan'))}]\t {msg}")

    @staticmethod
    def debug(msg):
        print(f"[{ts()}][{stylize('DEBUG', fg('cyan'))}]\t {msg}")

    @staticmethod
    def emote(user, msg):
        print(f"[{ts()}][{stylize('EMOTE', fg('yellow'))}]\t \
{stylize(user, fg('blue'))}: {msg}")

    @staticmethod
    def talk(di, user, msg):
        print(f"[{ts()}][{stylize('TALK', fg('green'))}]\t \
{stylize(user, fg('blue'))}: {msg}")

    @staticmethod
    def whisper(di, user, msg):
        print(f"[{ts()}][{stylize('PRIV', fg('medium_purple_3b'))}]\t \
<{di.capitalize()} \
{stylize(user, fg('blue'))}>: \
{stylize(msg, fg('grey_42'))}")

    @staticmethod
    def leave(user):
        print(f"[{ts()}][{stylize('LEAVE', fg('indian_red_1c'))}]\t \
User {user} has left the channel")

    @staticmethod
    def chan(name):
        # name = ' '.join([str(s) for s in name if s])
        print(f"[{ts()}][{stylize('JOIN', fg('green'))}]\t \
You have joined: {name}")

    @staticmethod
    def join(flags, ping, user, stats):
        if flags == 18:
            flags = "Is currently a channel operator."
        else:
            flags = ""
        stats = stats[::-1]
        print(f"[{ts()}][{stylize('JOIN', fg('green'))}]\t \
{stylize(user, fg('blue'))} \
has joined the channel. Using {stats} \
and {ping}ms ping. {flags}")

    @staticmethod
    def _in(flags, ping, user, stats):
        if flags == str(18):
            flags = "Is currently a channel operator."
        else:
            flags = flags
        stats = stats[::-1]
        print(f"[{ts()}][{stylize('IN', fg('cyan'))}]\t User {user} \
is in the channel. Using {stats} \
and {ping}ms ping. {flags}")

    @staticmethod
    def update(flags, ping, user, stats):
        if flags == 18:
            flags = "Is currently a channel operator."
        else:
            flags = ""

        stats = stats[::-1]
        print(f"[{ts()}][{stylize('UPDATE', fg('cyan'))}] User {user} \
is in the channel. Using {stats} \
and {ping}ms ping. {flags}")

    @staticmethod
    def serverupdate(name, topic):
        print(f"[{ts()}][{stylize('UPDATE', fg('cyan'))}] \
Channel: {name} Topic: {topic}")

    @staticmethod
    def broadcast(name, msg):
        print(f"[{ts()}][{stylize('BROADCAST', fg('yellow'))}] \
{name}: {msg}")


if __name__ == '__main__':
    log.bot("Envy Bot")
    log.bot("v0.0.2")
    log.bot("P$Y/Omen")
    log.debug("Loading config")
    log.succ("Bot successfully connected")
    log._in("2", "14", "P$Y", "WAR2")
    log.join("2", "14", "P$Y", "WAR2")
    log.ping("c5j3")
    log.pong("c5j3")
    log.update("0", "14", "P$Y", "WAR2")
    log.talk("FROM", "P$Y", "Whats up bros")
    log.whisper("TO", "P$Y", "Whats wrong?")
    log.emote("Omen", "Envy Bot :: v0.0.2 :: P$Y/Omen")
    log.leave("Omen")
    log.err("Server shutting down")
    log.error("Bot error, shutting down.")
