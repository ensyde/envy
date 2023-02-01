from objects.user import User
# from user import User


class Channel:
    def __init__(self, name):
        self.name = name
        self.topic = ""
        self.userlist = []
        self.ops = []

    def add_user(self, name, flags=None, ping=None, stats=None):
        if flags == 18:
            self.ops.append(name)
        self.userlist.append(name) if name not in self.userlist \
            else self.userlist
        # self.userlist.append(name)

    def add_username(self, name, flags=None, ping=None, stats=None):
        self.userlist.append(User(name, flags=flags, ping=ping, stats=stats))

    def rem_user(self, user):
        self.userlist.remove(user) if user in self.userlist \
            else self.userlist

    def __str__(self):
        return f"Channel: {self.name} Userlist: {self.userlist}"
