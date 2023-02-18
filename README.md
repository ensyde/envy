---
title: Envy Bot
output: pdf_document
---

# Envy

## About

**Bot for Init6/Discord/Irc/Bncs**
> **Version: v0.1.0**

> Author: [P$Y](https://github.com/ensyde/envy)
---
## Project layout

```
envy/
    protocols/          #Protocol/Connection code for each type
        init6/          # Init6
        bncs/           # Battle.net 1.0 using binary login
        discord/        # Discord
        irc/            # Irc
    bot.py              # Main bot class
    config.py           # Config
    main.py             # Main
```

If you want to learn more about ``setup.py`` files, check out `this repository <https://github.com/kennethreitz/setup.py>`_.

---
## Notes {#custom-id}
### Connection Protocols
- Init6/Warnet
- Discord
- Irc
- Bncs/Battle.net


### Access
- S safelist
- X shitlist
- O operator
- M master
- I info
---
### TODO {#todo}
- [x] Discord
- [ ] Bncs
- [ ] Irc
- [ ] Init6
- [ ] Commands
- [ ] Db
