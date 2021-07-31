from bot.olambot import OlamBot, filters
from bot.helpers.malayalam_dict import malayalamDictBot

@OlamBot.on_message()
async def malayalamDict(client, msg):
    word = malayalamDictBot(msg.text)
    w = f"\n".join(word)
    await client.send_message(
        chat_id=msg.chat.id,
        text=f" {msg.text.capitalize()}\n {w}",
        parse_mode="html"
    )

