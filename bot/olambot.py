from logging import root
from os import name
from pyrogram import *
from sample_cofig import (
    API_ID,
    API_HASH,
    BOT_TOKEN
)
from bot import __version__ , __copyright__ , __license__

class OlamBot(Client):
    def __init__(self):
        name = self.__class__.__name__.lower()
        super().__init__(
            name,
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            plugins={
                "root": "bot/plugins"
            },
            parse_mode="html"
        )

    async def start(self):
        await super().start()
        print(f"\n\nOlam {__version__}, {__copyright__}\nLicensed under the terms of the {__license__}\n\n")

    async def stop(self, *arg):
        await super().stop()
