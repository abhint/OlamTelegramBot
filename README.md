# OlamTelegramBot
### This bot is an English-Malayalam dictionary. This bot is built from Olam open-source data. Olam is an online website for English-Malayalam dictionaries.

#### 1. Clone the project repository

```sh
//With GitHub CLI
$ gh repo clone AbhijithNT/OlamTelegramBot
```

```sh
//With SSH
$ git clone git@github.com:AbhijithNT/OlamTelegramBot.git
```

```sh
//With HTTPS
$ git clone https://github.com/AbhijithNT/OlamTelegramBot.git
```
#### 2. change directory

```sh
cd OlamTelegramBot
```
#### 3. Install requirements
```sh
$ pip3 install -r requirements.txt
```

### Config / Secrets environment variables
#### Copy .env_sample to .env and add your private information

```env
API_ID = 
API_HASH = 
BOT_TOKEN = 
```

Go and get the bot token [@BotFather](https://telegram.dog/BotFather)

click the link to get your app id & api_hash [my.telegram.org](https://my.telegram.org/auth)

## Run your Bot

```sh
python3 -m bot
```

### Deploy

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/AbhijithNT/OlamTelegramBot/)

## Credits, and Thanks to

* [Olam](https://olam.in/open/) English-Malayalam dictionary dataset
* [Dan Tès](https://telegram.dog/haskell) for his[Pyrogram Library](https://github.com/pyrogram/pyrogram)

### LICENSE
- [ GPL-3.0 License](https://github.com/AbhijithNT/OlamTelegramBot/blob/main/LICENSE)
