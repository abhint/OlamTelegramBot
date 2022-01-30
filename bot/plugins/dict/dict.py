from bot.olambot import OlamBot
from pyrogram.types import Message
from bot.helpers.malayalam_dict import do_search


@OlamBot.on_message()
async def malayalam_dict(client: OlamBot, msg: Message):
    word, ps_result, result = do_search(msg.text)
    dict_result = "\n".join(ps_result)
    w = (f'__{result}__\n'
         f'{dict_result}')
    await client.send_message(
        chat_id=msg.chat.id,
        text=f"{msg.text.capitalize()}{w}",
        parse_mode='md'
    )
