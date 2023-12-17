
SID_AUTH_INFO = b'\x50'
SID_PING = b'\x25'
SID_AUTH_CHECK = b'\x51'
SID_REQUIREDWORK = b'\x4c'
SID_AUTH_ACCOUNTLOGON= b'\x53'
SID_AUTH_ACCOUNTLOGONPROOF = b'\x54'
SID_NULL = b'\x00'
SID_NETGAMEPORT = b'\x45'
SID_ENTERCHAT = b'\x0a'
SID_JOINCHANNEL = b'\x0c'
SID_CHATEVENT = b'\x0f'
SID_CHATCOMMAND = b'\x0e'
SID_CLANINFO = b'\x75'
SID_CLANMEMBERLIST = b'\x7d'
SID_CLANMEMBERSTATUSCHANGE = b'\x7f'
SID_MESSAGEBOX = b'\x19'
SID_CLANINVITATION = b'\x77'
SID_CLANMEMBERREMOVED= b'\x7e'
SID_FRIENDSUPDATE = b'\x66'
SID_FRIENDSLIST = b'\x65'
SID_FLOODDETECTED = b'\x13'
SID_FRIENDSADD = b'\x67'

KR_GOOD = b'\x00\x00\x00\x00'
KR_OLD_GAME_VERSION = b'\x00\x01\x00\x00'
KR_INVALID_VERSION = b'\x01\x01\x00\x00'
KR_ROC_KEY_IN_USE = b'\x01\x02\x00\x00'
KR_TFT_KEY_IN_USE = b'\x11\x02\x00\x00'

NULL = b'\x00'
NULL_2 = b'\x00\x00'
NULL_3 = b'\x00\x00\x00'
NULL_4 = b'\x00\x00\x00\x00'

EID_SHOWUSER = b'\x01\x00\x00\x00'
EID_JOIN = b'\x02\x00\x00\x00'
EID_LEAVE = b'\x03\x00\x00\x00'
EID_WHISPER = b'\x04\x00\x00\x00'
EID_TALK = b'\x05\x00\x00\x00'
EID_BROADCAST = b'\x06\x00\x00\x00'
EID_CHANNEL = b'\x07\x00\x00\x00'
EID_USERFLAGS = b'\x09\x00\x00\x00'
EID_WHISPERSENT = b'\x0a\x00\x00\x00'
EID_CHANNELFULL = b'\x0d\x00\x00\x00'
EID_CHANNELDOESNOTEXIST = b'\x0e\x00\x00\x00'
EID_CHANNELRESTRICTED = b'\x0f\x00\x00\x00'
EID_INFO = b'\x12\x00\x00\x00'
EID_ERROR = b'\x13\x00\x00\x00'
EID_EMOTE = b'\x17\x00\x00\x00'

CLANRANK_INITIATE = 0
CLANRANK_PEON = 1
CLANRANK_GRUNT = 2
CLANRANK_SHAMAN = 3
CLANRANK_CHIEFTAN = 4

# Bitfield
FRIENDSTATUS_MUTUAL = 1
FRIENDSTATUS_DND= 2
FRIENDSTATUS_AWAY = 4

# Value
FRIENDLOCATION_OFFLINE = 0
FRIENDLOCATION_NOTCHAT = 1
FRIENDLOCATION_CHAT = 2
FRIENDLOCATION_PUB = 3
FRIENDLOCATION_PRIVHIDE = 4
FRIENDLOCATION_PRIVSHOW = 5
