from ...olambot import OlamBot, filters


@OlamBot.on_message(filters.command(["help", "h"]))
async def onHelp(_, msg):
    await msg.reply(
        "is Working"
    )