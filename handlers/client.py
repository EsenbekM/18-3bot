from aiogram import types, Dispatcher
from aiogram.types import ParseMode, InlineKeyboardMarkup, InlineKeyboardButton
from config import bot
from database.bot_db import sql_command_random
from keyboards.client_kb import start_markup


# @dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply(f"Hello {message.from_user.full_name}!", reply_markup=start_markup)


# @dp.message_handler(commands=['quiz'])
async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("NEXT", callback_data='button_call_1')
    markup.add(button_call_1)

    question = 'Какого камня нет в реке ?'
    answers = [
        'Серого', "Круглого", "Сухого", "Мокрого", "Большого"
    ]
    await bot.send_poll(
        chat_id=message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="Изи же",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup
    )


async def show_random_user(message: types.Message):
    await sql_command_random(message)


def register_handler_client(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=['start'])
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_message_handler(show_random_user, commands=['random'])
