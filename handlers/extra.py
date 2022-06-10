from aiogram import types, Dispatcher
from config import bot


# @dp.message_handler()
async def echo_and_ban(message: types.Message):
    bad_words = ['глупый', "дурак", "плохой", "лох"]
    for word in bad_words:
        if word in message.text.lower():
            await bot.send_message(message.chat.id,
                                   f"Не материмь {message.from_user.full_name}\n"
                                   f"Сам ты {word}")
            await bot.delete_message(message.chat.id, message.message_id)

    if message.text.startswith("pin"):
        await bot.pin_chat_message(message.chat.id, message.message_id)

    if message.text.lower() == "dice":
        a = (await bot.send_dice(message.chat.id, emoji="🎰"))
        print(a['dice']['value'])

def register_handlers_extra(dp: Dispatcher):
    dp.register_message_handler(echo_and_ban)
