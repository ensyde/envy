# Envy

**About**
A chat/war bot for init6/warnet, a custom Battle.net 1.0 server with only the channel system implemented. Used to mimic old school clan/channel warring.

---

## Protocol & Events

**Initial connection sequence:**
- C1 (C>S)
- ACCT <ACCOUNT> (C->S)
- PASS <PASSWORD> (C->S)
- HOME <CHANNEL> (C->S)
- LOGIN (C->S)
- OK || FAIL <REASON> (C<-S)

**Events**
The format of incoming data separated at \r\n and empty strings removed from array is as following:
> COMMAND EVENT DIR? FLAGS? PING? NAME MSG

Commands & Events:
| COMMAND | EVENT     |  DIR?   |       | FLAGS? | PING? | NAME? | DATA  |
| --------|-----------|---------|-------|--------|-------|-------|-------|
| SERVER  | INFO      |         |       |        |       |       |  msg  |
| SERVER  | ERROR     |         |       |        |       |       |  msg  |
| SERVER  | TOPIC     |         |       |        |       |       | topic |
| SERVER  | BROADCAST |         |       |        |       | name  |  msg  |
| SERVER  | UPDATE    |         |       |        |       | name  | msg   |
|         |           |         |       |        |       |       |       |
| USER    | IN        |         |       | flags  | ping  | name  | stats | 
| USER    | JOIN      |         |       | flags  | ping  | name  | stats | 
| USER    | LEAVE     |         |       |        |       | name  |       | 
| USER    | WHISPER   | TO/FROM |       |        |       | name  | msg   | 
| USER    | TALK      | TO/FROM |       |        |       | name  | msg   | 
| USER    | EMOTE     |         |       |        |       | name  | msg   |   
| USER    | UPDATE    |         |       | flags   | ping  | name  | stats |
|         |           |         |       |        |       |       |       |
| CHANNEL | JOIN      |         |       |        | flags  | name  |       |
| CHANNEL | TOPIC     |         |       |        |       | topic |       |
|         |           |         |       |        |       |       |       |
| PING    | cookie    |         |       |        |       |       |       |
| FAIL    | reason    |         |       |        |       |       |       |
| OK      |           |         |       |        |       |       |       |


