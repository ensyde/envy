# Envy

**About**
A chat/war bot for init6/warnet, a custom Battle.net 1.0 server with only the channel system implemented. Used to mimic old school clan/channel warring.

---

**Protocol & Events**

__Initial connection sequence:__
- C1 (C>S)
- ACCT <ACCOUNT> (C->S)
- PASS <PASSWORD> (C->S)
- HOME <CHANNEL> (C->S)
- LOGIN (C->S)
- OK || FAIL <REASON> (C<-S)


