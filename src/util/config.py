from configparser import ConfigParser
import os

servers = ["ash.wserv.org", "la.wserv.org", "kc.wserv.org"]


class Config:
    def __init__(self, username, password, host, port, home, trigger,
                 master, idle, idle_interval
                 ):
        self._username = username
        self._password = password
        self._host = host
        self._port = port
        self._home = home
        self._trigger = trigger
        self._master = master
        self._idle = idle
        self._idle_interval = idle_interval
        self._access = []
        self._safelist = []
        self._shitlist = []

    def reloaddb(self):
        # self.access, self.safelist, self.shitlist = []
        self.load_access()
        self.load_safelist()
        self.load_shitlist()

    def load_access(self):
        print("loading access")
        print(f"Access cwd: {os.getcwd()}")
        with open('./config/access', "r") as f:
            self._access = f.read().split()

    @property
    def access(self):
        a = []
        for i in self._access:
            a.append(i)
        return a

    def load_shitlist(self):
        with open('./config/shitlist', "r") as f:
            self._shitlist = f.read().split()

    @property
    def shitlist(self):
        a = []
        for i in self._shitlist:
            a.append(i)
        return a

    def shitadd(self, name):
        with open('./config/shitlist', 'w+') as f:
            # shitlist = f.read().split()
            if name not in self._shitlist:
                self._shitlist.append(name)
            for shit in self._shitlist:
                f.write(shit + '\n')
            f.close()
        self.load_shitlist()

    def shitrem(self, name):
        with open('./config/shitlist', 'w+') as f:
            # shitlist = f.read().split()
            if name in self._shitlist:
                self._shitlist.remove(name)
            for shit in self._shitlist:
                f.write(shit + '\n')
            f.close()
        self.load_shitlist()

    def safeadd(self, name):
        with open('./config/safelist', 'w+') as f:
            # safelist = f.read().split()
            if name not in self._safelist:
                self._safelist.append(name)
            for safe in self._safelist:
                f.write(safe + '\n')
            f.close()
        self.load_safelist()

    def saferem(self, name):
        with open('./config/safelist', 'w+') as f:
            # safelist = f.read().split()
            if name in self._safelist:
                self._safelist.remove(name)
            for shit in self._safelist:
                f.write(shit + '\n')
            f.close()
        self.load_safelist()

    def load_safelist(self):
        with open('./config/safelist', "r") as f:
            self._safelist = f.read().split()

    def adduser(self, user):
        with open('./config/access', 'w+') as f:
            users = f.read().split()
            users.append(user) if user not in users else users
            for u in users:
                f.write(u + '\n')

    def remuser(self, user):
        with open('./config/access', 'w+') as f:
            users = f.read().split()
            users.remove(user) if user in users else users
            for u in users:
                f.write(u + '\n')
        self.load_access()

    @property
    def safelist(self):
        a = []
        for i in self._safelist:
            a.append(i)
        return a

    @property
    def username(self):
        return self._username

    @property
    def password(self):
        return self._password

    @property
    def host(self):
        return self._host

    @property
    def port(self):
        return self._port

    @property
    def home(self):
        return self._home

    @property
    def trigger(self):
        return self._trigger

    @property
    def master(self):
        return self._master

    @property
    def idle(self):
        return self._idle

    @property
    def idle_interval(self):
        return self._idle_interval

    def __str__(self):
        return f"Config\nUsername: {self.username}\nPassword: {self.password}\
                \nHost: {self.host}\nPort: {self.port}\nHome: {self.home}\
                \nTrigger: {self.trigger}\nMaster: {self.master}\
                \nIdle: {self.idle}\nIdle Interval: {self.idle_interval}\n"


def load_config(filename):
    if os.getcwd().endswith('envy'):
        filename = 'config/' + filename
    elif os.getcwd().endswith('src'):
        filename = '../config/' + filename
    cfgprsr = ConfigParser()
    cfgprsr.read(filename)
    cfgmain = cfgprsr['Main']
    u = cfgmain['username']
    pw = cfgmain['password']
    h = cfgmain['host']
    p = int(cfgmain['port'])
    hm = cfgmain['home']
    t = cfgmain['trigger']
    m = cfgmain['master']
    idle = cfgmain['idle']
    idleint = int(cfgmain['idle_interval'])
    return Config(u, pw, h, p, hm, t, m, idle, idleint)


if __name__ == '__main__':
    config = load_config('config.ini')
    print(config.idle)
    print(config)
    config.reloaddb()
    print(config._access)
    print(config.shitlist)
    print(config._safelist)
