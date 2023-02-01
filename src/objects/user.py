class User:
    def __init__(self, user, flags=None, ping=None, stats=None):
        self.user = user
        self.isMod = False
        if flags:
            self.flags = flags
            if flags == 18:
                self.isMod = True
        if ping:
            self.ping = ping
        if stats:
            self.stats = stats[::-1]

    def __str__(self):
        msg = f"User {self.user} "
        if self.stats:
            msg += f"using {self.stats} "
        if self.isMod:
            msg += "has channel operator "
        if self.ping:
            msg += f"with ping of {self.ping}ms."
        return f"User: {self.user} "
