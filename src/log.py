from colored import stylize, fg

levels = { 'TOPIC', 'INFO','JOIN','LEAVE','TALK','EMOTE', 'WHISPER', 'IN', 'DEBUG'}

def level(lvl):
    match lvl:
        case "TALK":
            _lvl = stylize(lvl.upper())


def info(msg):
    print(f"[{level('info')}]\t{msg}")

def talk(user, msg):
    print(f"[{level('info')}]\t{msg}")

def info(msg):
    print(f"[{level('info')}]\t{msg}")

def info(msg):
    print(f"[{level('info')}]\t{msg}")
