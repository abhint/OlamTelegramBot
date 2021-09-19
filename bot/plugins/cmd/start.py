from pyrogram.filters import command
from ...olambot import OlamBot, filters
from .message import DEV, START, SOURCE


@OlamBot.on_message(filters.command("start"))
async def onStart(_, msg):
    await msg.reply(
        f"Hy <b>{msg.from_user.first_name},{START}{DEV}{SOURCE}</b>"
    )
