# Discord Token Protector

# :warning: Pay attention to everything that is written!

### How it works?

Think... Today's internet token grabbers or the vast majority works by accessing your Discord folder in 
`%APPDATA%/discord` so basically this program changes your Discord's "settings" so that it doesn't use this default folder anymore and use one with another name and thus making the token grabber difficult to work.

Every `electron` program like discord for example, has a file called `name.asar`, if you extract this file you "get the source" of the program and so we edit the location where the token will be saved.

`Node` is used to extract the `asar file`, as you can see here.
[View](https://github.com/zimzika/Anti-Token-Grabber/blob/master/protector.py#L46)

And here we change the directory used by Discord.
[View](https://github.com/zimzika/Anti-Token-Grabber/blob/master/protector.py#L64)

#### Ok, once you understand these things you must take the risk of using this program, to ensure that nothing goes out of the way, follow the tips below...

## How to use?

- Install Python 3.9
- Install NodeJS
- Download this repository ([Download](https://github.com/zimzika/Anti-Token-Grabber/archive/refs/heads/master.zip))
- Open Powershell or CMD as administrator and execute this script `protector.py`
- Await for finish
- After this close any instance of Discord
- Go to `%APPDATA%` and delete `discord folder`
- :tada: Your discord is now protected