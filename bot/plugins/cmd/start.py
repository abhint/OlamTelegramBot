from pyrogram.filters import command
from ...olambot import OlamBot, filters


@OlamBot.on_message(filters.command("start"))
async def onStart(_, msg):
    await msg.reply(
        "hi"
    )
