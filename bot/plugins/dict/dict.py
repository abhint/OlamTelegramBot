from bot.olambot import OlamBot
from pyrogram.types import Message
from bot.helpers.malayalam_dict import searchWord


@OlamBot.on_message()
async def malayalam_dict(client: OlamBot, msg: Message):
    try:
        word, entries, definition = searchWord(msg.text)
        print(entries)
    except Exception as err:
        print(err)
        await msg.reply(f'നിങ്ങള്‍ അന്വേഷിച്ച "<b>{msg.text}</b>" എന്ന പദത്തിന്റെ അര്ത്ഥം കണ്ടെത്താനായില്ല. ')
        return
    entries_join = "\n".join(entries)
    entries_msg = f'\n{entries_join}\n' if entries else "\n"
    definition_join = "\n".join(definition)
    message = f'{word}{entries_msg}{definition_join}'
    await client.send_message(
        chat_id=msg.chat.id,
        text=message,
    )
