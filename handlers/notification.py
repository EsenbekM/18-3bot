import asyncio
import aioschedule
from aiogram import types, Dispatcher
from config import bot


async def get_chat_id(message: types.Message):
    global chat_id
    chat_id = message.chat.id
    await bot.send_message(chat_id=chat_id, text="Got your id!")


async def go_to_sleep():
    await bot.send_message(chat_id=chat_id, text="Иди спать, Керемет коч бутту!")


async def wake_up():
    video = open('media/erjan.mp4', 'rb')
    await bot.send_video(chat_id=chat_id, video=video, caption="ВСТАВААААААААААЙ!")

async def scheduler():
    aioschedule.every().day.at('17:26').do(go_to_sleep)
    aioschedule.every().day.at('17:34').do(wake_up)
    # aioschedule.every().second.do(go_to_sleep)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(2)


def register_handler_notification(dp: Dispatcher):
    dp.register_message_handler(get_chat_id,
                                lambda word: 'разбуди' in word.text)
