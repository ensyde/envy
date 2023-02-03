import socket
from util.config import load_config
from util.log import log
from objects.channel import Channel
import time
from consts import VER, AUTHOR, NAME
from threading import Thread

PONG = False
# IN = False


class Bot:
    def __init__(self):
        self.config = load_config('config.ini')
        self.config.reloaddb()
        self.access = self.config.access
        self.shitlist = self.config.shitlist
        self.safelist = self.config.safelist
        self._connected = False
        self._socket = None
        self.channel = None
        self.is_op = False
        self._idle = True

    def idle(self):
        while self._idle:
            time.sleep(500)
            self.send(f"/me {NAME} :: v{VER} :: {AUTHOR}")

    def connect(self):
        host = self.config.host
        port = int(self.config.port)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((host, port))
            log.succ(f"Successfully connected to {host}")
            self._connected = True
        except Exception as e:
            log.err("Failed to connect")
            log.err(f"{e}")
            self._connected = False
        self._socket = s
        self._idle = Thread(target=self.idle, args=[])

    def disconnect(self):
        log.debug("Closing connection")
        self._connected = False
        self._socket.shutdown()
        self._socket.close()

    def set_channel(self, name):
        # self._current_channel = name
        # self._users_in_channel = []
        self.channel = Channel(name)

    @property
    def connected(self):
        return self._connected

    def send(self, data):
        # log.debug("Sending: " + data)
        self._socket.sendall((data + "\r\n").encode('utf-8'))

    def login(self):
        log.bot("Attempting to send login info.")
        try:
            self.send("C1")
            self.send(f"ACCT {self.config.username}")
            self.send(f"PASS {self.config.password}")
            self.send(f"HOME {self.config.home}")
            self.send("LOGIN")
        except Exception as e:
            self._connected = False
            log.err("Login info failed to send")
            log.err(f"{e}")

    def loop(self):
        file = self._socket.makefile()
        while self.connected:
            line = file.readline().strip().split(" ")
            arr = [str(a) for a in line if a]
            cmd, *_ = arr
            if cmd == 'OK':
                log.succ("Successfully connected!")
            elif cmd == 'FAIL':
                cmd, *rest = arr
                rest = " ".join([str(s) for s in rest if s])
                log.fail(rest)
            elif cmd == 'PING':
                cmd, *event = arr
                event = " ".join([str(e) for e in event if e])
                self.send(f"/PONG {event}")
                if PONG:
                    log.pong(event)
            else:
                if cmd == "USER":
                    cmd, event, *rest = arr

                    match event:
                        case "TALK":
                            di, user, *m = rest
                            msg = " ".join([str(_m) for _m in m if _m])
                            log.talk(di, user, msg)
                            if (self.has_access(user)) and \
                                    (msg.startswith(self.config.trigger)):
                                self.cmd_handler(user, msg)
                            elif (self.has_access(user)) and \
                                    (msg == "?trigger"):
                                self.send(f"Trigger: {self.config.trigger}")
                        case "EMOTE":
                            user, *m = rest
                            msg = " ".join([str(_m) for _m in m if _m])
                            log.emote(user, msg)
                        case "WHISPER":
                            di, user, *m = rest
                            msg = " ".join([str(_m) for _m in m if _m])
                            log.whisper(di, user, msg)
                        case "JOIN":
                            flags, ping, user, stats = rest
                            self.channel.add_user(user)
                            log.join(flags, ping, user, stats)
                            self.has_op(user, flags)
                            # if self.is_op:
                            #    self.check_shitlist(user)
                        case "LEAVE":
                            user = " ".join([str(s) for s in rest if s])
                            self.channel.rem_user(user)
                            log.leave(user)
                        case "IN":
                            flags, ping, user, stats = rest
                            self.channel.add_user(user)
                            self.has_op(user, flags)
                            # if (user == self.config.username) and \
                            #         (flags == str(18)):
                            #     self.is_op = True
                            #     self.check_shitlist(user)
                            # # log._in(flags, ping, user, stats)
                        case "UPDATE":
                            flags, ping, user, stats = rest
                            self.channel.add_user(user)
                            self.has_op(user, flags)
                            # if (user == self.config.username) and \
                            #         (flags == str(18)):
                            #     self.is_op = True
                            #     self.check_shitlist(user)
                            # log.update(flags, ping, user, stats)
                        case _:
                            log.debug("Unknown USER event")
                elif cmd == "SERVER":
                    cmd, event, *rest = arr

                    match event:
                        case "TOPIC":
                            topic = " ".join([str(s) for s in rest if s])
                            log.topic(topic)
                        case "INFO":
                            msg = " ".join([str(s) for s in rest if s])
                            log.info(msg)
                        case "BROADCAST":
                            name, *m = rest
                            msg = " ".join([str(s) for s in m if s])
                            log.broadcast(name, msg)
                        case "UPDATE":
                            name, *t = rest
                            topic = " ".join([str(s) for s in t if s])

                            log.serverupdate(name, topic)
                        case "ERROR":
                            rest = " ".join([str(e) for e in rest])
                            log.err(rest)
                        case _:
                            log.debug("Unknown SERVER event")
                elif cmd == "CHANNEL":
                    cmd, event, *rest = arr

                    match event:
                        case "JOIN":
                            name = rest[0]
                            self.set_channel(name)
                            log.chan(name)
                        case "TOPIC":
                            topic = " ".join([str(s) for s in rest if s])
                            log.topic(topic)
                        case _:
                            log.debug("Unknown CHANNEL event")

    def has_op(self, name, flags):
        if (name == self.config.username) and \
          (flags == str(18)):
            self.send("I have gained channel ops!")
            self.is_op = True
            self.check_shitlist(name)

    def has_access(self, name):
        if name == self.config.master:
            return True
        else:
            for n in self.config.access:
                if name == n:
                    return True
            return False

    def cmd_handler(self, user, msg):
        cmd, *rest = msg.lstrip(self.config.trigger).split()
        cmd = cmd.lower()
        msg = " ".join([str(s) for s in rest if s])
        if ' ' in msg:
            msg = msg.split()
            name = msg.pop(0)
            has_msg = True
            msg = " ".join([str(s) for s in msg if s])
        else:
            has_msg = False
            name = msg
        match cmd:
            case 'help':
                self.send("Current commands: say, \
ver, ban, unban, kick, op, designate, join")
            case 'say':
                if msg.startswith('/'):
                    msg = msg.lstrip('/')
                self.send(msg)
            case 'ver' | 'version' | 'about':
                self.send(f'{NAME} :: v{VER} :: {AUTHOR}')
            case 'ban' | 'b':
                if self.is_op:
                    if not self.check_safelist(name):
                        self.send(f"/ban {name} {msg if has_msg else ''}")
                    else:
                        self.send(f"User {name} is safelisted.")

                    # self.send(f"/ban {msg}")
                else:
                    self.send("I am not channel operator.")
            case 'unban' | 'ub':
                if self.is_op:
                    self.send(f"/unban {name}")
                else:
                    self.send("I am not channel operator.")

            case 'kick' | 'k':
                if self.is_op:
                    self.send(f"/kick {name} {msg if has_msg else ''}")
                else:
                    self.send("I am not channel operator.")
            case 'op':
                if self.is_op:
                    self.send(f"/designate {name}")
                    self.send("/resign")
                else:
                    self.send("I am not channel operator.")

            case 'designate':
                if self.is_op:
                    self.send(f"/designate {name}")
                else:
                    self.send("I am not channel operator.")
            case 'join' | 'j':
                self.send(f"/join {name}")
            case 'users':
                u = ' '.join([str(s) for s in self.config.access if s])
                self.send(f"Users: {u}")
            case 'home':
                self.config.set_home(name)
                self.send(f"Home: {self.config.home}")
            case 'master':
                self.send(f"Master: {self.config.master}")
            case 'shitlist':
                self.send(f"Shitlist: {self.config.shitlist}")
            case 'safelist':
                self.send(f"Safelist: {self.config.safelist}")
            case 'shitadd':
                self.config.shitadd(msg)
                self.send('User/tag added to shitlist.')
            case 'shitrem':
                self.config.shitrem(msg)
                self.send('User/tag removed from shitlist.')
            case 'safeadd':
                self.config.safeadd(msg)
                self.send('User/tag added to safelist.')
            case 'saferem':
                self.config.saferem(msg)
                self.send('User/tag removed from safelist.')

    def check_shitlist(self, user):
        for shit in self.config.shitlist:
            if user.find(shit) >= 0:
                self.send(f"/ban {user} Shitlist")
                time.sleep(1)

    def check_safelist(self, user):
        for safe in self.config.safelist:
            if user.find(safe) >= 0:
                return True
        return False
